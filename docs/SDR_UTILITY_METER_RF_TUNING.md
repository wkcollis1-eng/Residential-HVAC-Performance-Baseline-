# Design/Test/Evaluation: SDR Utility Meter RF Tuning (rtlamr2mqtt)

**System:** rtlamr2mqtt add-on 2026.5.9, rtlamr v0.9.5 (bemasher/rtlamr), Nooelec NESDR SMArt v5 (RTL2832U + R820T2, 0.5 PPM TCXO)
**Meters:** gas (Itron 100G DLT / AL-425 body, ERT 20109304, SCM), electric (Vision VM1991 "Vision HP-RF", ERT 43344099, SCM), water (Neptune R900M v4, SN 1571014090, R900)
**Status as of 2026-09-14:** centerfreq and symbollength closed out 2026-08-25; gain/AGC closed out 2026-09-14. Config reverted to AGC. Revisit after planned antenna swap (W5012 + 2m MR-195, replacing 3m RG174 + loaded coil).
**Primary sources:** full detail lives in the `home-assistant-config` repo — `CHANGELOG.md` (2026-08-21 through 2026-08-26 entries) and `docs/addons/rtlamr2mqtt-recommended.yaml`. This document is a consolidated summary for reference from this repo; it does not replace those.

---

## 1. Background — what's being tuned and why

One RTL-SDR dongle receives three utility meters that transmit FHSS/OOK bursts in the 900-928 MHz ISM band. `rtlamr2mqtt` runs `rtl_tcp` + `rtlamr` with a fixed `-centerfreq` and `-symbollength` (sample rate/bandwidth), decoding SCM frames (gas, electric) and R900 frames (water) and publishing to MQTT/HA.

Goal driving this round of work: improve **gas** read cadence enough to resolve a single furnace burn cycle (10-20 min). Gas is the one meter where capture rate is operationally binding — electric is quantum-limited (its own counter only advances every ~54-86s, so it already has ~2.7x capture surplus) and water has ~12x margin over its 10-minute leak-detection hold.

---

## 2. Prior investigation (2026-08-21 to 2026-08-26) — summary

Full detail: `home-assistant-config/CHANGELOG.md`, `docs/addons/rtlamr2mqtt-recommended.yaml`.

### 2.1 Foundational fixes
- `listen_mode: true` is a **discovery-only** mode in this add-on (publishes nothing) — must stay `false`.
- `-unique=false` must be **explicit** on the `rtlamr:` line — `rtlamr`'s own default is `-unique=true`, which silently freezes `last_seen` on a flat meter.
- `rtltcp: -s <rate>` is **cosmetic**. `rtlamr` unconditionally overrides the sample rate on the control socket after connecting (`SampleRate = DataRate * ChipLength`, i.e. `32768 * symbollength`). Keep it numerically matched so `rtl_tcp` starts near where `rtlamr` is about to put it, but it does nothing on its own. **This is the same override mechanism that later explained the gain bug (§3).**

### 2.2 Centerfreq — was a coin flip, now pinned
Without an explicit `-centerfreq`, `rtlamr` picks between two built-in defaults (`scm`: 912.600155, `r900`: 912.380000) at random on every restart, because Go randomizes map iteration order when registering protocols. Pinned to **912,380,000 Hz** on 2026-08-25.

Swept 911.5 / 912.38 / 915.5 MHz at symbollength 80 (frames/min, measured):

| centre | gas | electric | water |
|---|---|---|---|
| 911.500 | 0.95 | 1.76 | 1.18 |
| **912.380 (kept)** | **1.05** | **1.87** | **1.23** |
| 915.500 | 0.25 | 2.09 | 1.17 |

**Verdict: "the centre-frequency search is finished. 912,380,000 is the answer."** 912.380 is a genuine local peak for gas; every direction away from it either helps nobody (lower) or costs gas heavily for an electric gain that doesn't matter (higher, since electric is quantum-limited anyway).

### 2.3 Symbollength — 72 → 80, and why it isn't a linear bandwidth trade
Legal values: 8/32/40/48/56/64/72/**80**/88/96 (rtlamr default is 72). Sample rate = `32768 * symbollength`.

The R820T2's analog IF filter bandwidth is tied to the sample rate by librtlsdr (`dev->bw > 0 ? dev->bw : dev->rate`), and the filter ladder has a hard threshold at 2,430,000 Hz: 72 (2,359,296) sits just under it (fine-grained ~2.3 MHz filter); 80 and above (2,621,440+) cross into a **6 MHz analog filter**. So 72→80 is not "11% more bandwidth" — it's a step onto a much wider analog passband that lets out-of-Nyquist channels alias in, at the cost of ~4 dB more noise. Measured effect at 80 vs 72 (24h): electric +23% (aliased coverage gain), water -14% (pure noise cost, no coverage gain — its 3 reliable phases degraded from ~99% to ~89%), gas unchanged. **Kept at 80** — the water cost is small in absolute terms (57.5% raw capture, ~49s mean heard interval vs a 10-min leak hold, still >10x margin) and the electric gain, while operationally moot on its own, doesn't hurt anything that matters.

### 2.4 Primary-source hardware identification (the FCC filing work)
Nameplate photos + FCC filings established the real hop sets, correcting several earlier assumption-based errors:

- **Electric (VM1991, FCC Y8E-VM1991):** 50 channels, 909.59-921.78 MHz (12.19 MHz span), 200 kHz spacing, OOK, FHSS.
- **Water (R900M, FCC P2SR900M):** 50 channels, 910-920 MHz. Manual states 14s transmit period; **measured grid was 28s** — this was a receiver artifact, not the meter: at 912.380 the Nyquist window functioned as a perfect parity filter on this meter's odd/even-indexed transmissions (0 odd-multiple-of-14s gaps in 2,077 observed; P ≤ 3×10⁻⁹). True capture at 912.380 is ~33.6%, not the naively-read 67.3%.
- **Gas (Itron 100G DLT on an American Meter AL-425 body, grantee EO9, FCC EO9100G — an earlier pass mis-identified this as the EWQ family and was corrected the same day):** 50 AM-modulated channels in **two disjoint 25-channel clusters**, 903.01-907.81 MHz and 922.01-926.81 MHz. **The gas meter's hop set and electric/water's hop set do not overlap — they are separated by a 14.2 MHz dead zone**, with electric and water living entirely inside it. Every gas frame this system has ever decoded arrived through the *analog filter skirt* (gas transmits loud — 0.26 W vs electric's 94.57 mW — so it leaks in from ~4.57 MHz outside the passband), not through genuine in-band reception.

### 2.5 Consequence: no single-dongle centerfreq trade exists between gas and electric/water
Because of the disjoint hop sets (§2.4), no 2.62 MHz (Nyquist) or 6 MHz (analog) window can contain a gas channel and an electric/water channel simultaneously. Tested/modeled near the one place the ranges almost touch (electric's edge at 921.78, gas's nearest channel at 922.01 — a 230 kHz gap):

| centre | gas channels in-window | electric Nyquist coverage | water Nyquist coverage |
|---|---|---|---|
| 912.38 (current) | 0 | 22% | 26% |
| 920.50 (candidate, tested on paper) | ~8-14 | 21% | 8% |

920.50 was **withdrawn before deployment** — it costs water ~18 points of coverage (roughly 2/3 of its margin) for a gas benefit that was never even confirmed by measurement. The only way to receive gas properly in-band is `-centerfreq=905400000`, which puts real gas channels inside Nyquist/analog windows — but that frequency is nowhere near electric/water's range, so it **loses both of them completely**. That's a second-dongle solution, not a retune.

### 2.6 Duty cycle / power
`sleep_for: 0` (continuous) costs ~4.30 W vs `sleep_for: 60`'s ~3.02 W, on a host that (as of this investigation) runs off a DIY LiFePO4 UPS during outages — so this is genuine outage-runtime cost (~30 min out of the post-UPS-swap ~133 min), not just an electricity-bill line item. Kept at `sleep_for: 0` because the capture-rate cost of duty-cycling was judged not worth the runtime, and because the electric ERT is mains-powered and stops transmitting during an outage anyway (gas is battery-powered and survives).

### 2.7 What was flagged but not yet tested as of 2026-08-26
`-tunergain` / AGC. The close, strong electric meter was hypothesized to possibly desense the front end via AGC pumping, which — if true — a fixed gain might relieve. Recorded as "back on the table" and not pursued further that week. **This is where today's work (§3) picks up.**

---

## 3. Today's investigation (2026-09-14) — gain / AGC

### 3.1 The bug: gain was never actually being set
An attempted manual gain sweep (`rtltcp: -s 2621440 -g <value>`) produced no consistent result. Root cause, confirmed two independent ways:

1. **Source (bemasher/rtlamr v0.9.5, the exact pinned version):** `flags.go` defines no gain flag at all. The gain-related flags rtlamr *does* recognize — `-tunergain`, `-gainbyindex`, `-tunergainmode`, `-agcmode` — are registered on **rtlamr's own** flag set (via the embedded rtltcp client library), not rtl_tcp's. In `main.go`, right after `Connect()`:
   ```go
   case "gainbyindex", "tunergainmode", "tunergain", "agcmode":
       gainFlagSet = true
   ...
   if !gainFlagSet {
       rcvr.SetGainMode(true)   // forces AUTO over the control socket
   }
   ```
   `-g` on the `rtltcp:` line only sets `rtl_tcp`'s own starting gain; since none of rtlamr's own gain flags were ever present on the `rtlamr:` line, `gainFlagSet` stayed false and `rtlamr` re-forced AGC immediately after every connect — stomping whatever `rtl_tcp` had started at. Same override mechanism as the `-s` sample-rate no-op from §2.1, different field.
2. **The deployed log, directly:** every `Starting rtlamr:` line across the entire sweep (11+ restarts, spanning the original test session) carried **no** `-tunergain`/`-gainbyindex`/`-agcmode` — confirming the gain value never reached rtlamr at all.

**Fix:** move gain onto the `rtlamr:` line — `-tunergain=<dB>` — and verify by grepping the next `Starting rtlamr:` log line for it.

### 3.2 What AGC actually does (verified from librtlsdr `tuner_r82xx.c`)
Enabling AGC is not "pick one gain value and hold it." It sets two register bits once (`LNA auto on`, `Mixer auto on`) that hand control to the **R820T2's own onboard hardware AGC loop**, which then runs autonomously at a chip-internal clock (60 Hz or 250 Hz, per register `0x1a`) for as long as the mode stays enabled — i.e. continuously adjusting gain every 4-16.7 ms, with zero host involvement, for the entire multi-hour run between restarts. That loop rate is the same order as the electric meter's ~5.9 ms burst duration, so the AGC-desense hypothesis (§2.7) was mechanistically plausible — fast enough to react within a single burst.

### 3.3 Full bracket test
R820T2 legal gain steps (dB, 29 discrete values): 0.0, 0.9, 1.4, 2.7, 3.7, 7.7, 8.7, 12.5, 14.4, 15.7, 16.6, 19.7, 20.7, 22.9, 25.4, 28.0, 29.7, 32.8, 33.8, 36.4, 37.2, 38.6, 40.2, 42.1, 43.4, 43.9, 44.5, 48.0, **49.6**.

Tested the two true endpoints plus one interior point against a pooled uncontrolled-AGC baseline, ~22.7 hours of data total:

| condition | duration | gas rate | electric rate | water rate |
|---|---|---|---|---|
| AGC (pooled, pre-fix restarts) | 1,149.6 min | 1.247/min | 2.863/min | 1.518/min |
| 0.0 dB (true min) | 38.4 min | 1.277/min | 2.450/min | 1.590/min |
| 40.2 dB | 60.6 min | 1.187/min | 2.935/min | 1.500/min |
| 49.6 dB (true max) | 110.9 min | 1.308/min | 2.804/min | 1.551/min |

Pairwise χ² (Poisson rate test) across every comparison: gas and water never exceeded χ²=0.45 (p>0.5) against any other condition — genuinely flat. Median inter-read gap for gas was **31.0 seconds in every single condition tested**, the strongest single indicator that gain (auto or fixed, anywhere in the 0-49.6 dB range) does not move gas or water capture in this system.

Electric showed the only non-null hint: 0.0 dB sat nominally lower than the three "real gain" conditions (which clustered tightly together). Pooling AGC + 40.2 + 49.6 (3,780 reads, 22 hours) against 0.0 dB gave χ²=2.21, p≈0.14 — never crossed significance, and **did not strengthen when the 49.6 dB sample was tripled from 33 to 111 minutes**, meaning more data isn't going to resolve it without a much larger run than is worth spending. Operationally moot regardless (§1 — electric is quantum-limited, not capture-limited).

### 3.4 Interpretation
This result is consistent with, not contrary to, §2.2-2.4: gas and water losses are **hop-coverage-limited** (the transmitter hopped outside the tuned window) rather than **sensitivity-limited** (signal was in-band but too weak to demodulate). Gain — of any kind — can only rescue the second failure mode. Since sweeping nearly the entire usable gain range produced no measurable change, sensitivity was never the bottleneck for either meter.

A methodology note worth preserving: **`max_gap` (worst-case reception age) is a high-variance statistic and unsafe to compare across single short windows.** Three consecutive 21-minute chunks at the *same* fixed gain (40.2 dB, no change at all) produced max gaps of 180s, 165s, and 121s purely from sampling noise — a wider spread than several of the cross-condition comparisons that initially looked promising. Median gap is the much more trustworthy statistic for this kind of test; treat any single-window max-gap comparison as provisional until repeated.

### 3.5 Decision
**Reverted to AGC** (2026-09-14) — statistically indistinguishable from every fixed value tested, and simpler to maintain (no pinned gain value to carry, no restart-time verification step). Config as currently deployed:

```yaml
custom_parameters:
  rtltcp: -s 2621440
  rtlamr: -unique=false -symbollength=80 -centerfreq=912380000
```

---

## 4. Other variables considered (uncontrolled, not yet tested here)

Raised 2026-09-14; recorded as [I] (plausible from general RF-engineering knowledge, not yet measured on this system) rather than established findings.

| variable | plausible mechanism | most relevant to |
|---|---|---|
| RF-band traffic / interference (neighbors' own meters, other 900 MHz devices) | raises local noise floor | electric — the only meter that showed any gain-sensitivity hint (§3.3) |
| Weather (humidity/rain through wall and ground paths) | wet building materials/soil attenuate UHF more than dry | speculative for all three; worth a seasonal comparison if long-term logging exists |
| Foliage | seasonal leaf-out attenuation | likely minor — paths are mostly through-structure, not through-yard |
| New RF sources near the antenna (this project's own LiFePO4 UPS / INA228 work, EV chargers, solar inverters) | switch-mode supply noise | partially controllable — keep new electronics away from the antenna's table |
| Gas meter's filter-skirt reception mode (§2.4) | gas is received via analog filter leakage, not in-band — makes it uniquely exposed to tuner temperature drift and filter response changes that don't affect the other two meters | gas specifically; first suspect if gas capture drifts without a config change |

None of these were tested this session. They're recorded so a future drift in capture rate isn't re-diagnosed as a gain or centerfreq problem before checking whether it's one of these first.

---

## 5. Open items / next steps

- [ ] **Antenna swap** (planned, not yet done): W5012 + 2m MR-195, replacing the current 3m RG174 + loaded coil on a magnetic base. Expected ~3 dB less system loss.
- [ ] **Revisit this whole investigation after the antenna swap.** A different antenna changes the actual SNR profile at the dongle, which could reopen questions this session closed (e.g., gain might become a real lever with a different noise floor / signal strength baseline than what was tested here). Don't assume today's null results carry over unchanged.
- [ ] Electric's weak 0.0 dB signal (§3.3) — not worth pursuing on its own; revisit only if electric capture becomes operationally relevant (it isn't currently, per §1).
- [ ] `-tunergain` is no longer flagged as "untested" — this document closes that thread from the 2026-08-26 CHANGELOG entry.

---

## 6. Verification method notes (for repeating this kind of test)

- The add-on prints the **full command line** for both `rtl_tcp` and `rtlamr` at `verbosity: info` on every restart — this is the cheap, decisive way to confirm a custom_parameters change actually reached the process it was intended for. Don't assume a flag took effect; grep the next restart's log line for it.
- Off-host, Supervisor's add-on-log API endpoints (`/api/hassio/addons/...`) reject a long-lived Core token (401) — this is expected, not a bug. The add-on's own Log page in the Supervisor UI (manual download) works fine for pulling a log to analyze off-host.
- Rate comparisons: use a Poisson two-sample χ² test (pooled rate → expected counts → `(obs-exp)²/exp` summed) rather than comparing raw percentages or "Nx" ratios — several apparent effects during this and the prior investigation (56.7%→38.0% on a longer sample, 87.5%→no effect, several "peak" gain readings) turned out to be short-sample noise once tested this way.
