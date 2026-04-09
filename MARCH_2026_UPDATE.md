# HVAC Performance Update: March 2026

**Version:** 1.5.1 (Corrected)  
**Date:** April 8, 2026  
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut  
**Corrections from v1.5.0:** Heating Intensity formula corrected throughout (§1, §2, §5);
HDD source discrepancy documented (§2); min/HDD seasonal framing corrected (§5);
Recommendations expanded with envelope monitoring context (§6).

---

## Executive Summary

March 2026 represents the transition into the spring shoulder season. As outdoor
temperatures rose, heating demand decreased significantly. The furnace ran 81.4 hours,
a 15.2% reduction from March 2025's 96.0 hours despite carrying 10.3% more HDD —
a favorable year-over-year runtime result. Domestic Hot Water (DHW) savings from the
recirculation optimization continue to be realized, with a 33.2% reduction in DHW gas
year-over-year.

**Key March 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas Consumption | 111.0 CCF | −36.6% MoM |
| Weather Severity | 767.6 HDD65 *(HA proxy)* | −29.5% MoM; BDL official = 709.0 HDD |
| Net Space Heating Gas | 96.0 CCF | −40.3% MoM |
| **Heating Intensity** | **125.1 CCF/1k HDD** | +4.1% vs March 2025; shoulder-season range |
| DHW Consumption | 15.0 CCF | −33.2% YoY; recirc optimization |
| HVAC Runtime | 81.4 hours | −15.2% YoY despite +10.3% HDD |
| Runtime / HDD | 6.4 min/HDD | Within normal shoulder-season range |

> **Correction note (v1.5.0 → v1.5.1):** The prior version computed Heating Intensity
> using *total* gas (111.0 CCF) instead of *net space heating* gas (total minus DHW =
> 96.0 CCF). This produced inflated values of 144.4 (Mar 2026) and 152.4 (Mar 2025)
> and incorrectly reported a year-over-year improvement. The corrected values are 125.1
> and 120.1 respectively — a modest 4.1% increase, not a decrease.

> **HDD proxy note:** The HA proxy records 767.6 HDD for March vs. BDL's official 709.0
> HDD (+8.3%). This is the opposite direction from the annual pattern (where HA
> undercounts by ~2.3%). Using BDL HDD yields a corrected intensity of **135.4
> CCF/1k HDD**. Both figures are well above the annual baseline; the proxy discrepancy
> does not change the qualitative interpretation for this month.

**Interpretation:** The runtime reduction (81.4h vs 96.0h) despite higher HDD is a
positive signal. However, the corrected Heating Intensity of 125.1 CCF/1k HDD shows
March 2026 was marginally worse than March 2025 (120.1), not better. Both values are
significantly above the annual baseline of 90.3 CCF/1k HDD, which is a normal and
expected artifact of shoulder-season physics (see §5 for detailed explanation) and
does not indicate system malfunction. March data alone cannot determine whether the
9.5% UA elevation observed in the 12-month rolling calculation is persistent; that
determination requires observing January–February data from the 2026–2027 heating season.

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

### March 2026 vs March 2025

| Metric | March 2025 | March 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 106.0 CCF | 111.0 CCF | +4.7% | Weather-driven; more HDD in 2026 |
| **DHW (Navien)** | 22.47 CCF | 15.00 CCF | **−33.2%** | Recirc optimization sustained |
| **Space Heating** | 83.53 CCF | 96.00 CCF | +14.9% | 10.3% more HDD; some real increase |
| **HDD65 (HA proxy)** | 695.5 | 767.6 | +10.3% | Colder March in 2026 |
| **Heating Intensity** *(corrected)* | **120.1 CCF/1k HDD** | **125.1 CCF/1k HDD** | **+4.1%** | Modest increase; both in shoulder-season range |
| **HVAC Runtime** | 96.0 hrs | 81.4 hrs | −15.2% | Less runtime despite more HDD — positive |
| **Runtime / HDD** | 8.28 min/HDD | 6.36 min/HDD | −23.2% | Seasonal load distribution effect |

> ~~Heating Intensity: March 2025 = 152.4 / March 2026 = 144.4 / Change = −5.3%~~  
> **Corrected:** These values used total gas (including DHW) as the numerator.
> The correct values use net space heating gas (total minus Navien DHW).
> The YoY direction reverses: intensity increased +4.1%, not decreased −5.3%.

**Key Insight:** Total gas is up 4.7% on 10.3% more HDD — meaning the system delivered
the additional heat demand with proportionally less gas, a favorable ratio. The 33.2%
DHW reduction provides a $12–15 estimated monthly offset that partially masks the
space heating increase in the total bill. The runtime reduction (−15.2%) despite
more heating demand is the clearest positive signal in the month.

The corrected heating intensity of 125.1 CCF/1k HDD being marginally above March 2025's
120.1 is not alarming in isolation. Shoulder-season intensity varies considerably based
on how HDD are distributed across the month — a handful of very mild days (mean temp
55–62°F) near the 65°F base temperature carry disproportionately high CCF/HDD relative
to cold days. March 2026 had more such near-base days.

---

## Month-over-Month Analysis

### Natural Gas (February 2026 → March 2026)

| Metric | February 2026 | March 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 175.0 | 111.0 | −36.6% |
| Space Heat CCF *(net of DHW)* | 161.4 | 96.0 | −40.5% |
| DHW CCF (Navien) | 13.6 | 15.0 | +10.3% |
| HDD65 *(see §4 note)* | 1,089.0 | 767.6 | −29.5% |
| **Heating Intensity** *(corrected)* | **148.2 CCF/1k HDD** | **125.1 CCF/1k HDD** | **−15.6%** |

> **Correction note:** Prior version's MoM Heating Intensity was not shown explicitly,
> but the Feb figure used in calculations was based on total gas (175 CCF), which would
> give 160.7 CCF/1k HDD — incorrect. The corrected Feb figure uses net heating gas
> (161.4 CCF) and the daily-CSV-derived HDD (1,089.0 per §4), giving 148.2 CCF/1k HDD.

**Analysis:** The −15.6% improvement in heating intensity from February to March reflects
the seasonal transition rather than any change in system behavior — both months are well
above the annual baseline of 90.3 due to shoulder-season physics. The slight increase in
DHW consumption (+10.3%) is typical for March; rising outdoor temperatures reduce the
incoming cold-water supply temperature differential, but the Navien's increased burner
activity to pre-heat the recirculation loop in the morning offsets this partially.

### HVAC Runtime (February 2026 → March 2026)

| Metric | February 2026 | March 2026 | MoM Change |
|---|---|---|---|
| Total Heating Hours | 158.0 | 81.4 | −48.5% |
| Zone Balance (1F%) | 45.6% | 49.6% | +4.0 pts |
| **min/HDD** | **8.71** | **6.36** | −27.0% |

> **HDD note:** February min/HDD of 8.71 uses the daily-CSV-derived HDD of 1,089.0
> (see §4). Using HA archive HDD (1,062.6) gives 8.92 min/HDD; using BDL official
> (1,125.0) gives 8.43 min/HDD. The directional conclusions are unchanged across all
> three sources.

**Analysis:** Runtime decreased sharply in proportion to the HDD reduction. The zone
balance improvement from 45.6% to 49.6% first-floor share reflects the reduced
second-floor cathedral ceiling load dominance as ΔT decreases — the 2F advantage
that drives its 54–58% typical winter share attenuates in mild weather.

---

## DHW Performance Update

### Sustained Recirculation Optimization Results

The recirculation schedule change (off 9 PM – 6 AM) continues to deliver consistent
year-over-year savings:

| Metric | March 2025 *(24hr recirc)* | March 2026 *(15hr recirc)* | Change |
|---|---|---|---|
| DHW Gas (Navien) | 22.47 CCF | 15.00 CCF | **−33.2%** |
| DHW Operating Hours | 12 hrs | 12 hrs | 0% |
| Implied gas per operating hour | 1.87 CCF/hr | 1.25 CCF/hr | −33.2% |

**Note:** With identical operating hours, the 33.2% gas reduction is attributable to
the recirc schedule change eliminating 9 hours of overnight pipe-heat maintenance per
day. The 12-month Navien archive totals 197.5 CCF vs the trailing-12-month estimate of
~210–215 CCF that would have prevailed under the prior 24-hour schedule — an annualized
saving of approximately 13–18 CCF (~$22–30/yr at current rates).

---

## HDD Methodology Note

Three HDD sources exist for February and March 2026 and they do not agree:

| Month | HA Proxy Archive | Daily CSV (Hi+Lo)/2 | BDL Official |
|---|---|---|---|
| January 2026 | 1,196.8 | — | 1,263.0 |
| February 2026 | 1,062.6 | **1,089.0** | 1,125.0 |
| March 2026 | **767.6** | — | 709.0 |
| Q1 2026 Total | 3,027.0 | — | 3,097.0 |

The daily CSV uses the simple (high + low) / 2 method, which matches the report's prior
February figure of 1,089.0 exactly. The HA proxy uses a 24-hour mean temperature from
the live weather API, which produces slightly different results particularly near the
65°F base temperature.

For **February**, the daily CSV method (1,089.0) is used in this report for internal
consistency with the runtime data. BDL's 1,125.0 is the authoritative reference.

For **March**, the HA proxy (767.6) is used as-is since the daily CSV does not cover
this month. BDL's 709.0 is 8.3% lower — the proxy overcounts March HDD. This makes
the CCF/1k HDD calculation appear slightly more favorable than it actually is; the
BDL-corrected March intensity is **135.4 CCF/1k HDD** vs the 125.1 shown in this report.

The Q1 total undercount of 70 HDD (HA proxy vs BDL) has been documented in prior
analysis. The annual rolling efficiency metric (105.0 CCF/1k HDD) is approximately
0.8–1.0 CCF/1k HDD elevated relative to what a BDL-denominator calculation would
produce — real but not the primary driver of the 14.7-point gap vs the 90.3 baseline.

---

## HVAC Runtime Performance

### Baseline Comparison

| Metric | Annual Baseline | March 2026 | Context |
|---|---|---|---|
| Runtime / HDD | 10.9 min/HDD | 6.36 min/HDD | Shoulder-season normal |
| Heating Intensity | 90.3 CCF/1k HDD | 125.1 CCF/1k HDD | Shoulder-season normal |
| Zone Balance Target | 50% ± 5% | 49.6% | ✓ Optimal |

> ~~"The runtime efficiency of 6.4 min/HDD is approximately 41% better than the baseline,
> which is typical for the shoulder season."~~  
> **Corrected:** Comparing a shoulder-season month against the annual average baseline
> (10.9 min/HDD) and calling the result "41% better" is misleading. The annual baseline
> is dominated by January and February, when high ΔT produces proportionally more runtime
> per HDD. March is structurally expected to read below 10.9 min/HDD in any normal year.
> March 2025's 8.28 min/HDD was already well below the 10.9 baseline. The correct
> comparison is March 2026 (6.36) vs March 2025 (8.28) — a 23.2% improvement
> year-over-year. This is more meaningful and reflects a genuine positive trend.

### Why Both Metrics Are Elevated vs the Annual Baseline

Both min/HDD and CCF/1k HDD are distance metrics — they measure fuel or time per unit
of heating demand. In cold months, each HDD represents a large temperature deficit (e.g.
65°F − 20°F = 45°F, for 45 HDD in a day). In mild months, each HDD represents a small
deficit (e.g. 65°F − 63°F = 2°F, for 2 HDD in a day).

The furnace's fixed combustion rate (60,556 BTU/hr input) means any single firing event
covers the same overhead regardless of the external load. On a 2-HDD day, that overhead
is amortized over 2 HDD; on a 45-HDD day, over 45 HDD. The annual baseline averages
across this full range. Comparing any single spring month against the annual figure
overstates efficiency in warm months and understates it in cold ones.

The min/HDD reduction from 8.28 (March 2025) to 6.36 (March 2026) is real and positive,
likely reflecting a combination of load distribution differences between the two Marches
and the ongoing CPH=3 cycling pattern that was still in place (the CPH change to 2 was
implemented April 1, 2026 — after this reporting period). This improvement does not
carry forward an inference about annual efficiency; it is a within-shoulder-season comparison.

---

## Recommendations

### Monitoring Priorities

1. **CPH=2 + 30s Fan Delay Impact:** The thermostat change implemented April 1, 2026
   should produce measurable results by May. Expected outcomes: avg cycle length
   increasing from ~7.3 min toward 9–10 min; furnace daily cycle count declining ~20–25%.
   Monitor `sensor.hvac_furnace_min_per_cycle_month` and `sensor.hvac_furnace_cycles_month`
   through April and May.

2. **12-Month Rolling UA Trend:** The current rolling UA of 540 BTU/hr-°F is 9.5% above
   the 493 baseline. As January and February 2025 (high-UA-signal months) cycle out of
   the 12-month window and January–February 2026 cycle in, the rolling figure will update.
   If the envelope is stable, UA should trend toward 493. If it remains at 540+ through
   the 2026–2027 heating season, the signal is persistent and warrants an energy audit
   (attic hatch seals, rim joists, recessed light penetrations).

3. **Heating Intensity Trajectory:** The rolling 12-month efficiency of 105.0 CCF/1k HDD
   is 14.7 points above the 90.3 baseline. The CPH correction is expected to contribute
   ~3–5 CCF/1k HDD improvement over a full heating season. The remainder of the gap
   will not be resolved by thermostat settings alone and tracks with the UA deviation.

4. **Spring Transition / Cooling Season Prep:** Begin monitoring CDD65 accumulation and
   first AC cycles once outdoor temperatures consistently exceed 65°F mean. Update
   `input_number.runtime_per_cdd_seed_mean` and `runtime_per_cdd_seed_stddev` after
   the first full week of AC operation.

5. **DHW Inlet Temperature Tracking:** As municipal water supply temperatures rise through
   spring, the Navien's energy demand per gallon decreases. Monitor whether the YoY DHW
   savings percentage holds or widens; a narrowing gap would indicate the inlet temperature
   effect is partially offsetting the recirc schedule gain.

### Pending Data

- **March 2026 Utility Bills:** Gas and electric bills pending (expected mid-April).
  Will update `monthly_gas_scg.csv`, `monthly_electricity_eversource.csv`, and all
  12-month gas/DHW/HDD archives upon receipt. The March bills will update the rolling
  12-month efficiency and UA sensors.
- **HDD Archive Reconciliation:** Consider populating a parallel BDL-sourced HDD archive
  (`input_number.hdd_archive_bdl_*`) to produce a proxy-corrected efficiency sensor
  alongside the existing HA-proxy-based metric. Q1 2026 BDL HDD available: Jan 1,263 /
  Feb 1,125 / Mar 709.

---

*Report generated using Home Assistant archived billing data, Navien tankless telemetry,
HA history_stats sensors, and daily HDD tracking via Hartford weather proxy.*  
*System: American Standard single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + Navien
NPE-240S2 tankless DHW. Two-zone forced air, 2,440 sq. ft., East Hampton CT.*