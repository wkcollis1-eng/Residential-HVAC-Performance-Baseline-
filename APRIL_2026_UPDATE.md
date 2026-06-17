# HVAC Performance Update: April 2026

**Version:** 1.6.0
**Date:** June 17, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Heating Intensity computed on **net space-heating gas** (total − Navien DHW),
per the v1.5.1 correction established in the March 2026 report. All intensity figures below,
and the `data/monthly_summary.csv` column, are on this basis.

---

## Executive Summary

April 2026 is the first full month of the spring shoulder season and the first full month
under the **CPH=2 + 30 s fan-delay** thermostat change (effective April 1). It produced the
strongest efficiency reading of the heating season so far: the furnace ran 38.4 hours — a
23.2% reduction from April 2025 despite carrying 11.9% more HDD — and net heating intensity
fell to 96.8 CCF/1k HDD, only 7.2% above the annual baseline and, notably, *below* March's
125.1 even though April was the milder month. That ordering runs against shoulder-season
physics and is the clearest efficiency signal of the season, though one month under CPH=2 is
confounded with a mild, high-solar-gain April and is not yet conclusive. DHW savings from the
recirculation optimization widened to −35.7% year-over-year.

**Key April 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas Consumption | 59.0 CCF | −46.8% MoM |
| Weather Severity | 472.3 HDD65 *(HA proxy)* | −38.5% MoM; BDL April reference not yet available |
| Net Space-Heating Gas | 45.72 CCF | −52.4% MoM |
| **Heating Intensity** *(net)* | **96.8 CCF/1k HDD** | −24.8% vs Apr 2025; +7.2% vs 90.3 baseline |
| DHW Consumption | 13.28 CCF | −35.7% YoY; recirc optimization |
| HVAC Runtime | 38.4 hours | −23.2% YoY despite +11.9% HDD |
| Runtime / HDD | 4.88 min/HDD | Shoulder-season normal |
| Avg Cycle Length | 8.2 min *(CSV-derived)* | up from 6.6 in March — CPH=2 directional |
| Zone Balance (1F) | 52.3% | Within 50% ± 5% target |
| Electric | 285 kWh / $81.48 | −17.2% kWh YoY |

> **Methodology note:** This report uses net space-heating gas for Heating Intensity, per
> v1.5.1. The repo's `monthly_summary.csv` `Heating_Intensity_CCF_1kHDD` column previously held
> total-gas values (e.g. Apr 2025 = 177.7); it has been recomputed to the net basis (Apr 2025 =
> 128.8) for **all** heating-season rows in the accompanying file. Review before committing —
> this changes every historical intensity value.

**Interpretation:** Two signals point the same direction. Runtime fell 23.2% on 11.9% more
HDD — a continuation and strengthening of the March pattern (−15.2% on +10.3%). And net
intensity at 96.8 is the lowest heating-season reading and sits below the milder-month
expectation. Candidate drivers are the CPH=2 change (longer cycles, less short-cycle overhead),
high April solar gain (actual furnace runtime ran ~20% below the degree-day model), and a
favorable HDD distribution with fewer near-base mild days than March. These cannot be
decomposed from a single month; the cleaner CPH=2 read will come from May, before the late-May
thermostat swap muddies it.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HDD Methodology Note](#hdd-methodology-note)
5. [HVAC Runtime Performance](#hvac-runtime-performance)
6. [Recommendations](#recommendations)

---

## Year-over-Year Analysis

### April 2026 vs April 2025

| Metric | April 2025 | April 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 75.0 CCF | 59.0 CCF | −21.3% | Less gas despite more HDD — favorable |
| **DHW (Navien)** | 20.66 CCF | 13.28 CCF | **−35.7%** | Recirc optimization sustained, widening |
| **Space Heating** *(net)* | 54.34 CCF | 45.72 CCF | −15.9% | Real reduction against +11.9% HDD |
| **HDD65 (HA proxy)** | 422.0 | 472.3 | +11.9% | Colder April in 2026 |
| **Heating Intensity** *(net)* | **128.8 CCF/1k HDD** | **96.8 CCF/1k HDD** | **−24.8%** | Strong improvement |
| **HVAC Runtime** | 50.0 hrs | 38.4 hrs | −23.2% | Less runtime despite more HDD |
| **Runtime / HDD** | 7.11 min/HDD | 4.88 min/HDD | −31.4% | Load distribution + CPH=2 |
| **Electric** | 344 kWh / $109.56 | 285 kWh / $81.48 | −17.2% / −25.6% | Lower use + lower effective rate |

**Key Insight:** Every fuel and runtime metric moved favorably against a colder month. The
−24.8% intensity improvement is the largest YoY shoulder-season gain recorded and is driven by
genuine reduced gas-per-HDD, not weather — April 2026 burned 0.097 CCF/HDD of space heat versus
0.129 in April 2025. The 35.7% DHW reduction (an estimated $14–16 monthly offset) continues to
soften the total bill. Unlike March, where corrected intensity was marginally *worse* YoY
(+4.1%), April's improvement is unambiguous and substantial.

The electric bill fell harder than usage (−25.6% vs −17.2% kWh) because the effective rate also
dropped (~0.319 → 0.286 $/kWh, −10%) — a rate tailwind on top of lower consumption.

---

## Month-over-Month Analysis

### Natural Gas (March 2026 → April 2026)

| Metric | March 2026 | April 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 111.0 | 59.0 | −46.8% |
| Space Heat CCF *(net of DHW)* | 96.0 | 45.72 | −52.4% |
| DHW CCF (Navien) | 15.00 | 13.28 | −11.5% |
| HDD65 | 767.6 | 472.3 | −38.5% |
| **Heating Intensity** *(net)* | **125.1 CCF/1k HDD** | **96.8 CCF/1k HDD** | **−22.6%** |

**Analysis:** Net space-heating gas fell 52.4% on a 38.5% HDD reduction — gas dropped *faster*
than demand, which is the opposite of the shoulder-season pattern (mild months normally read
higher intensity because the furnace's fixed combustion overhead is amortized over fewer HDD).
April reading *below* March on net intensity is therefore notable. It is consistent with the
CPH=2 change reducing per-cycle overhead and with high solar gain depressing actual heat demand
below the degree-day model. DHW dipped 11.5% MoM, normal for the seasonal transition.

### HVAC Runtime (March 2026 → April 2026)

| Metric | March 2026 | April 2026 | MoM Change |
|---|---|---|---|
| Total Heating Hours *(burner)* | 81.4 | 38.4 | −52.8% |
| Zone Balance (1F%) | 49.6% | 52.3% | +2.7 pts |
| Runtime / HDD | 6.4 | 4.88 | −23.8% |
| Avg Cycle Length *(CSV-derived)* | 6.6 min | 8.2 min | +24.2% |

**Analysis:** Runtime fell roughly in proportion to HDD. The zone balance continued its
shoulder-season shift toward first-floor dominance (49.6% → 52.3%) as the second-floor cathedral
load attenuates with declining ΔT — the same mechanism noted in March, one step further. The
avg cycle-length increase (6.6 → 8.2 min) moves in the direction the CPH=2 change was expected to
produce (target 9–10 min), but see the runtime section for the caveats on this figure.

---

## DHW Performance Update

### Sustained Recirculation Optimization Results

| Metric | April 2025 *(24 hr recirc)* | April 2026 *(15 hr recirc)* | Change |
|---|---|---|---|
| DHW Gas (Navien) | 20.66 CCF | 13.28 CCF | **−35.7%** |
| DHW Operating Hours | — | 11 hrs | — |
| DHW Recirc Hours | — | 32 hrs | — |
| Implied gas per operating hour | — | 1.21 CCF/hr | — |

**Note:** The April YoY DHW reduction (−35.7%) is slightly deeper than March's (−33.2%),
consistent with the recirculation schedule change (off 9 PM – 6 AM) delivering its largest
proportional savings as overnight ambient losses fall in milder weather. Prior-year April
operating/recirc hours were not captured under the old workflow, so the per-hour comparison
is single-sided this month; both fields are now archived going forward (see Recommendations).

---

## HDD Methodology Note

For April only the HA proxy archive is available; a BDL official April figure has not yet been
published into the parallel reference. The HA proxy ((high+low)/2 family) records 472.3 HDD.

| Month | HA Proxy Archive | BDL Official |
|---|---|---|
| February 2026 | 1,062.6 *(daily CSV 1,089.0)* | 1,125.0 |
| March 2026 | 767.6 | 709.0 |
| April 2026 | **472.3** | *(pending)* |

Per prior analysis the HA proxy and BDL diverge in sign by month (proxy over-counts March,
under-counts the annual total ~2.3%). Until the BDL April value is available, the net intensity
of 96.8 should be read with the same ±8% proxy band noted in March; the qualitative
conclusion — April near baseline and below March — holds across that band.

---

## HVAC Runtime Performance

### Baseline Comparison

| Metric | Annual Baseline | April 2026 | Context |
|---|---|---|---|
| Runtime / HDD | 10.9 min/HDD | 4.88 min/HDD | Shoulder-season normal (structurally below annual) |
| Heating Intensity *(net)* | 90.3 CCF/1k HDD | 96.8 CCF/1k HDD | +7.2% — closest to baseline of any heating month |
| Zone Balance Target | 50% ± 5% | 52.3% | ✓ Within band |

As established in March, comparing a shoulder month's min/HDD against the January–February-weighted
annual baseline overstates "efficiency"; the meaningful comparison is YoY. April 2026's 4.88 vs
April 2025's 7.11 (−31.4%) is the within-month figure, and it is genuinely favorable.

### CPH=2 First-Month Impact

April 1 was the CPH=3→2 + 30 s fan-delay change, making April the first full month under the new
cycling regime. From the daily CSV:

| Metric | March (CPH=3) | April (CPH=2) | Direction |
|---|---|---|---|
| Avg cycle length | 6.6 min | 8.2 min | +24% — toward the 9–10 min target |
| Furnace cycles (total) | 738 | 282 | −62% |
| Cycles / day | 23.8 | 9.4 | −60% |

The cycle-length increase is the expected CPH=2 signature and points the right way. **Two
caveats apply.** First, the cycle-count drop (−60%) is mostly demand-driven — April had less than
half March's heating hours — not a clean CPH=2 effect; the count would have fallen regardless.
Second, these figures are derived from the daily CSV (`furnace_runtime_min` / `furnace_cycles`)
and run below the `sensor.hvac_furnace_min_per_cycle_month` value the March report cited (~7.3 min
baseline). The HA monthly cycle sensors are authoritative; pull `sensor.hvac_furnace_cycles_month`
and `sensor.hvac_furnace_min_per_cycle_month` to confirm before drawing a firm CPH=2 conclusion.
The clean test is May, the last full month before the late-May Ecobee swap.

---

## Recommendations

### Monitoring Priorities

1. **CPH=2 confirmation (May):** April's cycle-length lift (6.6 → 8.2 min) is encouraging but
   confounded with mild weather and is CSV-derived. May is the decisive month — confirm with the
   HA monthly cycle sensors and isolate it before the Ecobee thermostats (installed ~May 29)
   change the controller behavior.

2. **Ecobee transition (May onward):** The Honeywell→Ecobee swap on ~May 29 means May is a
   split-controller month and June is the first full Ecobee month. Tag runtime and cycling data
   by controller for the Ecobee-vs-Honeywell baseline comparison; do not blend across the swap.

3. **12-Month Rolling UA Trend:** Unchanged guidance from March — the rolling UA (~540 vs 493
   baseline) will only resolve as Jan–Feb 2026 cycle into the window against Jan–Feb 2025. April
   shoulder data does not move this determination.

4. **Heating Intensity Trajectory:** April's 96.8 (net) is the closest-to-baseline heating-month
   reading of the season and supports the expectation that CPH=2 contributes a few CCF/1k HDD over
   a full season. Re-baseline only after a full 2026–2027 heating season under CPH=2.

5. **DHW per-hour tracking now enabled:** With `DHW_Op_Hrs` / `DHW_Recirc_Hrs` now archived
   (April: 11 / 32), the implied 1.21 CCF/operating-hour becomes a trackable series. Watch whether
   the YoY DHW savings hold or narrow as municipal inlet temperatures rise through summer.

### Pending / Data Hygiene

- **Intensity methodology correction (action required):** `data/monthly_summary.csv` has been
  recomputed to net-basis Heating Intensity for all heating-season rows. Review the diff and
  commit; this aligns the dataset with the v1.5.1 report methodology.
- **Q1 reconciliation:** Independent of April — the repo's committed March DHW (15.0) disagrees
  with the current archive (8.74), and February gas cost (248.0 repo vs 274.7 HA). Resolve before
  the next rolling-efficiency recompute, since the March DHW value feeds Space_Heat and intensity.

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-04
archive_slot: april
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/monthly_summary.csv)

DATA ENTERED
  HDD65:           472.3
  Gas_CCF:         59.0          Gas_Cost: 117.77
  DHW_CCF:         13.2810       (13.7727 Thm × 0.9643)
  Elec_kWh:        285.0         Elec_Cost: 81.48
  Heat_Total_Hrs:  38.4 (burner; 1F 20.1 / 2F 18.3 by Resideo 23:21 split)
  DHW_Op_Hrs:      11.0          DHW_Recirc_Hrs: 32.0

VALIDATION
  V1 range check:     FLAG — Gas −61% / Elec −34% vs trailing-3-mo avg; seasonal shoulder
                      transition (expected), confirmed in context. PASS in seasonal terms.
  V2 direction check: PASS — gas and runtime fell with HDD; intensity favorable, not anomalous.
  V-HVAC-2 (±15% of 90.3): PASS — net intensity 96.8 (+7.2%).
  V3 prior data:      PRESENT.

METRICS (before → after / YoY)
  Heating Intensity (net):  128.8 → 96.8 CCF/1k HDD  (−24.8% YoY)
  HVAC Runtime:             50.0 → 38.4 hrs          (−23.2% YoY, on +11.9% HDD)
  DHW:                      20.66 → 13.28 CCF        (−35.7% YoY)
  Runtime/HDD:              7.11 → 4.88 min/HDD       (−31.4% YoY)

FLAGS
  Intensity methodology corrected to net basis (v1.5.1) across full column — review before commit.
  CPH=2 first-month signal confounded with mild April + CSV-derived cycle metrics.

COMMIT MESSAGE (ready to use)
  git commit -m "2026.04: Add April HVAC performance data — 96.8 CCF/1k HDD (net); intensity column corrected to net basis"

README UPDATE NEEDED: NO — UA within prior documented range; no new record; methodology note already in report.
```

---

*Report generated using Home Assistant archived billing data, Navien tankless telemetry,
Resideo thermostat zone runtime, HA history_stats sensors, and daily HDD tracking via Hartford
weather proxy.*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + Navien NPE-240S2 tankless DHW.
Two-zone forced air, 2,440 sq. ft., East Hampton CT.*
