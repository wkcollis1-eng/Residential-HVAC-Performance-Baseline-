# HVAC Performance Update: June 2026

**Version:** 1.8.1
**Date:** July 7, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Cooling-season report. Heating Intensity is **not computed** this month (see advisory); cooling is tracked on a dual HDD/CDD basis (BDL official vs HA proxy) per v1.7.1.

**Revision 1.8.1 (July 7, 2026):** Incorporates authoritative sources that arrived after v1.8.0. (1) **Dehumidifier is full-month 134.7 kWh** — the Kasa-plug energy (in place since May) shows the unit ran all of June under an evolving control algorithm (dew-point early, RH-band 49%/46% later); the earlier "partial/70.85 kWh" reading was only 6/17–6/30 and has been corrected. (2) **DHW June 2025 recovered** (16.13 CCF, 54 recirc h) from the Navien log, enabling a clean DHW YoY (−28.5%), which is **recirc-schedule-led** (recirc 54→30 h). (3) **Electric cost added** ($114.74): cost −36.0% YoY, effective rate −20.7%. (4) SEM-Meter installed late June — 6/28 onward — so **AC energy is now metered but June is partial; first full SEM month is July.**

> **Data-integrity advisory (read first):** June 2026 is the **first full clean cooling month under the Ecobee controller** — the reset point flagged in the May report — and the billing/DHW/degree-day figures are clean. Five caveats apply and are flagged throughout:
> 1. **Heating Intensity is N/A.** Furnace runtime was **0.0 h**; with only 13–21 HDD there is no valid CCF/1k-HDD normalization. The `hvac_monthly.csv` heating-efficiency/`expected_runtime`/`deviation` fields (`0.0` / `0.48` / `−100%`) are summer null artifacts, not a performance signal.
> 2. **Dehumidifier ran all month under an evolving control algorithm.** Full-June dehumidifier energy is **134.7 kWh** (Kasa plug, in place since May). The control algorithm was tuned throughout June — dew-point control early (inefficient), transitioning to RH-band 49%/46% on/off control later (more efficient, still being validated) — so energy was consumed across the whole month, not just from 6/17. This is a **calendar-month** figure and does not map 1:1 onto the billing-cycle electric total (see caveat 3).
> 3. **Mixed measurement basis.** Runtime, cycles, HDD, CDD, and SEM/Kasa circuit energy are **calendar-month** (HA daily statistics). Gas and electric *bills* are **billing-cycle** values (electric dated 6/10, 30 days; gas dated 6/12, 29 days — each covering the prior ~30 days). YoY gas/electric are bill-to-bill and comparable, but do not align 1:1 with the calendar-month cooling/dehumidifier load.
> 4. **Proxy CDD under-counts.** The HA `outdoor_temp_live` proxy logged **150.6 CDD** vs BDL official **190** (−21%). The local sensor is the authoritative source for the house's own load; BDL is used for the normalized YoY comparison against the 2025 baseline.
> 5. **SEM-Meter installed late June.** The 16-CT whole-home monitor began logging **June 28**, so full-month AC/circuit energy is **not** available for June — the SEM data here (6/28 onward) is a late-June/July preview. **First full SEM month is July.** June cooling *energy* therefore remains runtime-derived; June cooling *runtime* (84.6 h) is measured.

---

## Executive Summary

June 2026 is the first uninterrupted full month on the Ecobee controller and the first clean cooling read of the year. It was a warm month (mean 70.1 °F, 150.6 proxy / 190 BDL CDD) with essentially all HVAC load on the cooling side: **84.6 cooling hours across 194 cycles, zero furnace runtime.** The bill signals are strongly favorable: gas fell 26% YoY and electricity fell **36% in dollars** (−19% kWh plus a −21% effective-rate tailwind). The gas drop is **DHW-led and largely recirculation-schedule-driven** — the recirc cut (54→30 h YoY) accounts for most of a −28.5% DHW reduction, which is 77% of the total gas drop. The headline engineering result is the first Ecobee-vs-Honeywell cooling comparison: on the BDL basis, cooling intensity is **26.7 min/CDD vs 30.0 last June (−11%)** — encouraging, but a single split-controller month that should not yet be read as a durable efficiency gain.

**Key June 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas Consumption | 17 CCF / $50.74 | −26.1% / −14.6% YoY; DHW + cooking, **no heating** |
| DHW (Navien) | 11.53 CCF | 11.9605 Thm × 0.9643; **−28.5% YoY** (vs 16.13 CCF, Jun 2025) |
| — recirc / op hours | 30 h / 10 h | recirc **54→30 h** YoY (−44%); the main lever |
| Net Gas (cooking + standby) | 5.47 CCF | 17 − 11.53; furnace off all month |
| Weather Severity | 21 HDD65 / 190 CDD65 *(BDL official)* | HA proxy: 13.4 HDD / 150.6 CDD |
| **Heating Intensity** | **N/A** | 0.0 furnace h; not normalizable at 13–21 HDD |
| **Cooling Runtime** | **84.6 hrs** *(2F)* | 194 cycles, mean 26.2 min/cycle; first full Ecobee month |
| **Cooling Intensity** *(BDL)* | **26.7 min/CDD** | proxy basis: 33.7 min/CDD |
| Electric | 505 kWh / **$114.74** | **−19.3% kWh / −36.0% $** YoY; effective rate −20.7% |
| Dehumidifier | **134.7 kWh** *(full month)* | Kasa plug; ran all June under evolving control (DP→RH-band) |
| Mean Outdoor Temp | 70.1 °F | 30/30 days present |

**Interpretation:** Bill-side, June is a quiet, favorable month: gas at a summer floor (DHW-led, recirc-driven), the electric bill down a third, and no heating load at all. The engineering story is entirely cooling and moisture. The Ecobee's first full cooling month shows ~11% lower runtime-per-CDD than the Honeywell's June 2025 (BDL basis), consistent with the min-runtime raise (10→15 min on Jun 7) lengthening cycles and trimming short-cycle overhead — but the controller change and the mid-month min-runtime change counsel treating this as a first data point, not a trend. Moisture is now a measured load, not an estimate: the dehumidifier drew **134.7 kWh** across June (a substantial calendar-month load), while its control was actively re-tuned from dew-point to RH-band logic mid-month. With the SEM-Meter installed late June, the full AC-vs-dehumidifier-vs-base-load decomposition arrives with the first complete SEM month (July); the 9-day tail here already shows cooling at ~61% of whole-home.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HDD & Cooling Methodology Note](#hdd--cooling-methodology-note)
5. [Cooling Runtime Performance](#cooling-runtime-performance)
6. [Recommendations](#recommendations)

---

## Year-over-Year Analysis

### June 2026 vs June 2025

| Metric | June 2025 | June 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 23 CCF / $59.39 | 17 CCF / $50.74 | **−26.1% / −14.6%** | Summer floor; DHW-led (see decomposition) |
| **DHW (Navien)** | 16.13 CCF *(9 op / 54 recirc h)* | 11.53 CCF *(10 op / 30 recirc h)* | **−28.5%** | Recirc cut 54→30 h is the main lever |
| **Electric** | 626 kWh / $179.41 | 505 kWh / $114.74 | **−19.3% kWh / −36.0% $** | Lower use **plus** −20.7% effective rate |
| **HDD65 (BDL official)** | 21 | 21 | flat | Negligible residual heating both years |
| **CDD65 (BDL official)** | 198 | 190 | −4.0% | Slightly milder cooling demand 2026 |
| **CDD65 (HA proxy)** | *n/a* | 150.6 | — | Local sensor under-counts vs BDL |
| **Cooling Runtime** | 99 hrs *(Honeywell; 2F 97 / 1F 2)* | 84.6 hrs *(Ecobee; 2F)* | **−14.5%** | Less runtime on a milder month |
| **Cooling Intensity** *(BDL)* | **30.0 min/CDD** | **26.7 min/CDD** | **−11.0%** | Ecobee vs Honeywell — first read, flagged |
| **Heating Intensity** | N/A | N/A | — | No heating either June |

**Gas decomposition (why gas fell −6.0 CCF YoY):** Splitting total gas into DHW + cooking/standby using the Navien figures — June 2025 was 16.13 DHW + 6.87 cooking; June 2026 is 11.53 DHW + 5.47 cooking. So **DHW accounts for −4.59 CCF (77%) of the −6.0 CCF drop**, cooking/standby for −1.41 CCF (23%). Both Junes have warm summer inlet, so the seasonal inlet effect is roughly common-mode — meaning the **recirculation-schedule cut (54→30 h) is the dominant controllable driver** of the −28.5% DHW and hence of most of the headline gas reduction. Per-operating-hour DHW gas fell 1.79→1.15 CCF/h (−36%), the cleaner efficiency indicator, consistent with less recirc standby to make up.

**Key Insight (cooling):** Cooling runtime fell 14.5% against a BDL CDD that fell only 4%. Normalizing, the Ecobee delivered June cooling at **26.7 min/CDD vs the Honeywell's 30.0 (−11%)** — the direction hoped for from the min-runtime and cycling changes, but resting on a single month spanning a controller change and a mid-month min-runtime raise, so a first data point, not a validated gain. The 2025 cooling figure (99 h) is from the baseline report on the Honeywell basis; the 2026 figure is the HA cooling accumulator — both second-floor-dominant, so directionally sound but not instrument-identical.

> **Caveats on the YoY rows:** Electric is bill-to-bill (June-dated bills, each covering ~mid-May→mid-June), so it lags the calendar-June cooling peak in both years — comparable to each other, but not a calendar-June cooling readout. The −20.7% effective rate ($0.2866→$0.2272/kWh) is the all-in bill rate; because 2026 spreads the ~$11 fixed charge over fewer kWh, the underlying energy-rate drop is larger still. DHW YoY uses the recovered June 2025 Navien value (16.723 Thm × 0.9643 = 16.13 CCF), not the overwritten archive slot.

---

## Month-over-Month Analysis

### Natural Gas (May 2026 → June 2026)

| Metric | May 2026 | June 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 39.0 | 17 | −56.4% |
| DHW CCF (Navien) | 14.33 | 11.53 | −19.5% |
| Net Gas *(cooking + standby)* | 24.67 *(residual heat)* | 5.47 *(no heat)* | heating ended |
| HDD65 *(BDL official)* | 222 | 21 | −90.5% |

**Analysis:** Space heating ended between May and June — May still carried 222 BDL HDD of residual heating; June carried none (0.0 furnace h). Total gas therefore collapsed to the summer floor of DHW plus cooking (17 CCF, of which 11.53 is DHW). DHW itself fell 19.5% MoM, from both warming municipal inlet temperature and the sustained recirc reduction (30 h in June). No heating-intensity comparison is meaningful across this transition.

### Electric & Cooling (May 2026 → June 2026)

| Metric | May 2026 | June 2026 | MoM Change |
|---|---|---|---|
| Electric *(bill-basis)* | 311 kWh / $82.66 | 505 kWh / $114.74 | **+62.4% / +38.8%** |
| Cooling Runtime | 20.2 hrs | 84.6 hrs | +319% |
| Dehumidifier *(Kasa)* | *not isolated* | 134.7 kWh *(full month)* | now measured |

**Analysis:** Electricity rose 62% MoM (kWh) as the first full cooling month and heavy dehumidifier operation came online; the bill rose less (+39%) thanks to the lower effective rate. Two big calendar-month loads are now measured: cooling runtime quadrupled (20.2 → 84.6 h), and the dehumidifier drew **134.7 kWh** across June under an actively-changing control algorithm (dew-point → RH-band). Note these are calendar-month figures against a billing-cycle electric total (505 kWh covers ~mid-May→mid-June), so they cannot be summed directly against the bill — the clean AC/dehumidifier/base-load split arrives with the first full SEM-Meter month (July).

---

## DHW Performance Update

### Recirculation-schedule reduction — the main gas lever this month

June 2026 DHW is **11.53 CCF** (11.9605 Navien Thm × 0.9643). The June 2025 comparator was recovered from the Navien log (16.723 Thm → 16.13 CCF), giving a clean **−28.5% YoY**:

| Metric | June 2025 *(24 h-ish recirc era)* | June 2026 *(reduced recirc)* | Change |
|---|---|---|---|
| DHW Gas (Navien) | 16.13 CCF | 11.53 CCF | **−28.5%** |
| DHW Operating Hours | 9 hrs | 10 hrs | +11% |
| DHW Recirc Hours | 54 hrs | 30 hrs | **−44.4%** |
| Implied gas per operating hour | 1.79 CCF/hr | 1.15 CCF/hr | **−35.7%** |

**Note:** The −28.5% DHW reduction is **recirculation-schedule-led**, not primarily inlet-temperature. Both Junes share warm summer inlet, so that seasonal effect is roughly common-mode; the difference is the deliberate recirc cut (54→30 h), which removes standby loop losses the burner would otherwise make up. The per-operating-hour figure (1.79→1.15 CCF/h, −36%) is the cleaner efficiency indicator and confirms the gain is structural, not a usage artifact — operating hours actually rose slightly (9→10). This DHW reduction (−4.59 CCF) is **77% of the total June gas drop**, so the recirc schedule is the dominant lever behind the headline gas number.

---

## HDD & Cooling Methodology Note

**Heating (HDD):** BDL official records **21 HDD** for June; the HA proxy logged 13.4. With furnace runtime at **0.0 h**, neither basis supports a heating-intensity calculation — June is reported as heating-inactive. The `heating_efficiency` / `expected_runtime` / `efficiency_deviation` cells in `hvac_monthly.csv` (`0.0` / `0.48` / `−100%`) are summer artifacts of the degree-day model and should be treated as null.

**Cooling (CDD / runtime):** This is June's headline metric and the first clean read. BDL official records **190 CDD**; the HA `outdoor_temp_live` proxy logged **150.6** (−21%). The gap is expected — BDL is the Bradley airport station; the proxy is the local sensor at the house, which is the authoritative source for the house's own cooling load (Pirate Weather runs warm on sunny afternoons and is not used). Cooling intensity is therefore reported dual-basis:

- **Proxy basis:** 84.6 h / 150.6 CDD = **33.7 min/CDD**
- **BDL basis:** 84.6 h / 190 CDD = **26.7 min/CDD**

The BDL basis is used for the YoY comparison (both years on the same station), giving 30.0 (2025) → 26.7 (2026), −11%. Begin treating the BDL cooling-intensity series as the primary cooling KPI from June forward.

---

## Cooling Runtime Performance

### Cooling — first full Ecobee month

June cooling ran **84.6 hours over 194 cycles**, all on the second floor, at a mean **26.2 min/cycle**. This is the first uninterrupted full month under the Ecobee Smart Enhanced controller and establishes the clean cooling baseline the May report deferred to June.

**Min-runtime change (10 → 15 min, Jun 7 ~18:00):** cycle length lifted modestly across the change —

- Through Jun 7 (4 cooling days): 918 min / 38 cycles = **24.2 min/cycle**
- Jun 8–30 (22 cooling days): 4,158 min / 156 cycles = **26.7 min/cycle**

The +2.5 min/cycle shift is directionally consistent with the higher minimum-runtime floor reducing short-cycling, though June's weather was also hotter in the back half, which lengthens cycles independently. The effect is real but not cleanly isolated from load within this single month.

**Zone distribution:** cooling remains essentially 100% second-floor, matching the 2025 baseline (2F 97 / 1F 2 of 99 h) — the cathedral-ceiling/solar-gain geometry drives the 2F cooling concentration, unchanged by the controller swap.

**AC energy — now metered (SEM), June partial.** The 16-CT SEM-Meter went in **late June (logging from 6/28)**, so full-month June cooling *energy* is not yet available and June cooling remains **runtime-derived** (84.6 h measured; the ~2.5 kW condenser draw is still the assumption for the full month). What the meter does confirm is the decomposition: **cooling electric = compressor (`sem_ac_energy`) + air-handler blower (`sem_furnace_energy`)** — the furnace blower is the shared indoor fan, and it draws in July with zero heating load, so it can only be running for cooling. Over the 6/28–7/6 tail, cooling ran **~61% of whole-home** (compressor ~46%, blower ~15%). The first full metered cooling month is **July**.

### Dehumidifier — full month measured, control under active tuning

Full-June dehumidifier energy is **134.7 kWh** (Kasa plug, in place since May). The control algorithm was re-tuned across the month — **dew-point control early (inefficient), transitioning to RH-band 49%/46% on-off later** (more efficient, still being validated) — which is why energy is present all month, not just from 6/17. This is a large calendar-month load (comparable in magnitude to the measured cooling tail), so the dehumidifier is a first-order term in the summer electric budget, not a rounding item. With the SEM-Meter now capturing AC and the Kasa capturing the dehumidifier, the July data will give the first clean AC / dehumidifier / base-load split — and a controlled read on whether the RH-band algorithm lowers dehumidifier kWh versus the dew-point period.

---

## Recommendations

### Monitoring Priorities

1. **July is the first clean electric decomposition.** The SEM-Meter (from 6/28) now meters AC (compressor + blower) and the Kasa meters the dehumidifier, so July's full month splits the summer electric into AC / dehumidifier / base load directly — no more baseline-subtraction estimate. Track it against the July bill on a **calendar-consistent** basis (SEM whole-home sum vs bill), noting the billing-cycle offset.

2. **Isolate the dehumidifier control comparison.** June ran two algorithms (dew-point early, RH-band 49%/46% later). Once July is fully on RH-band, compare dehumidifier kWh-per-RH-hour or kWh-per-CDD across the two regimes to validate whether RH-band is the efficiency win it appears to be. The 134.7 kWh June total is a large enough load to be worth optimizing.

3. **Treat June as the Ecobee cooling baseline.** The −11% BDL cooling-intensity result (30.0 → 26.7 min/CDD) is the first Ecobee-vs-Honeywell datapoint. Tag July and August by controller and watch whether the lower runtime-per-CDD holds through peak season before calling it an efficiency gain. July is already hotter (early daily CDD well above June), so it will be the stronger test — and the first month with cooling *energy*, not just runtime.

4. **12-Month Rolling UA — unchanged.** Cooling months do not move the UA determination; the read comes when the Jan–Feb 2026 heating months cycle through the window.

### Pending / Data Hygiene

- **Dehumidifier control regime dates:** record the dew-point → RH-band (49%/46%) transition date(s) within June so the July efficiency comparison has a clean control boundary.
- **Cooling energy vs runtime (June):** June cooling *energy* remains runtime-derived (SEM installed 6/28); keep June cooling-kWh labeled as estimated until superseded by the July metered month.
- **Confirm SEM CT assignment:** `sem_furnace_energy` is treated as the air-handler blower (cooling indoor fan); confirm against the SEM topology map before it anchors the July decomposition.
- **Billing-vs-calendar basis:** gas/electric bills are billing-cycle; SEM/Kasa/runtime are calendar-month — retained as a standing caveat, sharpened now that large calendar-month loads (dehumidifier 134.7 kWh) are measured against a billing-cycle electric total.

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-06
archive_slot: june
Repo(s) updated: Residential-HVAC-Performance-Baseline- (homeassistant/reports/hvac_monthly.csv — row present & validated)

DATA ENTERED / VALIDATED (June 2026)
  HDD65:        13.4 proxy   (BDL official 21)
  CDD65:        150.6 proxy  (BDL official 190)
  Furnace_Hrs:  0.0          -> Heating Intensity N/A (summer)
  Cool_Hrs:     84.6  [2F; 194 cycles; mean 26.2 min/cycle]
  Gas_CCF:      17           Gas_Cost: 50.74
  DHW_CCF:      11.53        (11.9605 Thm × 0.9643)   DHW_Op_Hrs: 10   DHW_Recirc_Hrs: 30
  Elec_kWh:     505          Elec_Cost: 114.74   (eff rate $0.2272/kWh)
  Dehum_kWh:    134.7        [FULL month; Kasa plug; ran all June under DP→RH-band control]
  Mean_Outdoor: 70.1 F

VALIDATION
  Daily→monthly reconciliation: PASS — HDD 13.4 / CDD 150.6 / furnace 0.0h / AC 84.6h / mean 70.1F all match hvac_monthly.csv (30/30 days present).
  Dehumidifier reconciliation: full-June 134.7 kWh (SEM/Kasa daily-max sum; 59.0 pre-6/17 + 75.7 post) — supersedes the v1.8.0 partial 70.85.
  V1 range check:     FLAG(expected) — Gas −56% MoM / Elec +62% MoM; seasonal heating→cooling transition. PASS in context.
  V2 direction check: N/A — no heating load; heating-intensity direction check not applicable in June.
  V-HVAC-2 (heating eff vs 90.3): N/A — 0.0 furnace h.
  V3 prior data:      PRESENT — June 2025 electric/gas/cooling/DHW all recovered (DHW from Navien log, 16.723 Thm).

METRICS (YoY, BDL basis where applicable)
  Cooling runtime:      99 → 84.6 hrs            (−14.5%)  [Honeywell → Ecobee]
  Cooling intensity:    30.0 → 26.7 min/CDD      (−11.0%)  [BDL; first Ecobee read, flagged]
  Gas:                  23 → 17 CCF              (−26.1%)  / cost $59.39 → $50.74 (−14.6%)
    of which DHW:       16.13 → 11.53 CCF        (−28.5%; recirc 54→30 h; 77% of gas drop)
  Electric:             626 → 505 kWh            (−19.3% kWh) / $179.41 → $114.74 (−36.0% $; eff rate −20.7%)

FLAGS
  Heating Intensity N/A — 0.0 furnace h; hvac_monthly.csv heating-eff/expected/deviation cells are summer null artifacts.
  Dehumidifier 134.7 kWh is FULL-month (Kasa); control re-tuned mid-month (dew-point → RH-band 49%/46%).
  Gas/electric bills are billing-cycle; SEM/Kasa/runtime are calendar-month — large calendar loads (dehum 134.7) don't sum onto the bill.
  Proxy CDD 150.6 under-counts BDL 190 (−21%); BDL used for YoY, proxy for house-load intensity.
  Cooling-intensity YoY crosses a controller change (Honeywell→Ecobee) + mid-month min-runtime raise (10→15, Jun 7) — first datapoint, not a trend.
  AC energy metered from 6/28 (SEM); June cooling energy still runtime-derived — first full metered month is July. Cooling = compressor (sem_ac_energy) + blower (sem_furnace_energy); CT map to confirm.

COMMIT MESSAGE (ready to use)
  git commit -m "2026.06: Add June HVAC data — first full Ecobee cooling month (84.6 h / 194 cyc, 26.7 min/CDD BDL, −11% YoY); gas −26% DHW/recirc-led (−28.5% DHW, recirc 54→30h); elec −36% $; dehum 134.7 kWh full-month; heating N/A"

README UPDATE NEEDED: NO — within documented ranges; June is heating-inactive and does not move UA/EUI baselines. Data-integrity notes captured in report.
```

---

*Report generated using Home Assistant daily statistics exports (`hvac_daily_2026.csv`, `hvac_monthly.csv`),
official Bradley/KBDL degree days (`bdl_degree_days.csv`, ACIS), Navien tankless telemetry (June 2026 archive +
June 2025 log, 16.723 Thm), SEM-Meter per-circuit energy (`energy_daily_master.csv`, from 6/28), Kasa
dehumidifier energy (`dehumidifier_today_s_consumption`, full June), HA electric/gas bill archives
($114.74 / $50.74), and HA runtime accumulators.*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + American Standard Silver 14 AC +
Navien NPE-240S2 tankless DHW. Two-zone forced air, 2,440 sq. ft., East Hampton CT.
Thermostats: Ecobee Smart Enhanced (first full cooling month, June 2026).*
