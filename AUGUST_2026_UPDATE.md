# HVAC Performance Update: August 2026

**Version:** 1.8.3
**Date:** October 15, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Cooling-season report. Heating Intensity is **not computed** (no furnace runtime). Degree days are **ACIS Hartford-Bradley (KBDL) HDD65/CDD65** throughout; the HA `outdoor_temp_live` proxy is shown as secondary only. Figures carry provenance tags: [M] measured, [S] spec, [D] derived (formula shown), [I] inferred (with its falsifying observation).

> **Data-integrity advisory (read first):**
> 1. **Complete month.** All 31 daily runtime rows and 31 SEM days are present, with no short-hour days [M]. Runtime per CDD uses the full month.
> 2. **Dehumidifier replaced.** The Aprilaire E080 replaced the Santa Fe Classic in August. Its first logged compressor cycle was 2026-08-05 [M, `SYSTEM_SPECIFICATIONS.md`]. The Kasa plug that switches the unit also meters it (`SYSTEM_SPECIFICATIONS.md`, Control). August dehumidifier energy is therefore mostly the new unit, and the July→August change mixes a unit swap, RH-threshold re-tuning, and weather.
> 3. **Mixed measurement basis.** Runtime, cycles, CDD and SEM/Kasa energy are calendar-month. The electric bill read 08-11 covers Jul 15–Aug 11 (28 days) in both years [M]. The gas bills are not the same length: the 2026 bill read 08-12 covers 28 days, and the 2025 bill read 08-14 covers 30 days [M]. DHW is calendar-month.
> 4. **2025 DHW was logged in therms.** The 2025 comparator is converted: 11.2357 Thm × 0.9643 = 10.83 CCF [D].

---

## Executive Summary

August 2026 was **hotter than August 2025**: 263 vs 170 BDL CDD [M], with BDL means of 73.2 °F and 69.6 °F [M]. Cooling still used **fewer minutes per CDD**. Runtime was 70.41 h on 263 CDD, or **16.1 min/CDD** [D: 70.41 × 60 / 263]. August 2025 used 62.07 h on 170 CDD, or **21.9 min/CDD** [D: 62.07 × 60 / 170]. That is one month, with no significance test; the September season review tests it on daily data. Runtime per CDD also fell from July to August in both years: 28.5 → 21.9 in 2025 and 26.6 → 16.1 in 2026 [D]. Single months therefore carry a within-season effect that a year-over-year pair cannot remove. Gas fell to 8 CCF, DHW to 5.59 CCF, and the electric bill to 724 kWh / $175.22 [M]. The SEM compressor drew **180.9 kWh**, or 0.688 kWh per BDL CDD [D: 180.9 / 263], at 2.57 kW per call-hour [D: 180.9 / 70.41].

**Key August 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas | 8 CCF / $36.27 [M] | bill read 08-12 |
| DHW (Navien) | 5.59 CCF [M] | 16 m³ Navien reading [D: 5.59 / 0.9643 / 0.36245]; op 8 h / recirc 12 h [M] |
| Net Gas (cooking + standby) | 2.41 CCF [D: 8 − 5.59] | mixed basis; at the 1-CCF bill resolution |
| Weather Severity | 0 HDD65 / 263 CDD65 *(BDL)* [M] | HA proxy: 0 HDD / 214.3 CDD [M] |
| **Heating Intensity** | **N/A** | furnace 0.0 h [M] |
| **Cooling Runtime** | **70.41 h** *(31 days, 2F)* [M] | HA accumulator 70.3 h [M] |
| **Cooling Intensity** *(BDL)* | **16.1 min/CDD** [D: 70.41 × 60 / 263] | lowest of the 2026 season |
| Cycles | 173 [M] | 24.4 min/cycle [D: 70.41 × 60 / 173]; 23 cooling days, 7.52 cycles per cooling day [D: 173 / 23] |
| AC compressor (SEM) | 180.9 kWh [M] | 0.688 kWh/BDL CDD [D]; 32.8% of whole-home [D: 180.9 / 550.7] |
| Electric | 724 kWh / $175.22 [M] | bill read 08-11, Jul 15–Aug 11 |
| Dehumidifier (Kasa) | 28.2 kWh [M] | Aprilaire E080 from 08-05 |
| Mean Outdoor Temp | 72.0 °F (HA) / 73.2 °F (BDL) [M] | |

**Interpretation:** August is the month where the controller comparison looks largest. It is also where the confounds are largest. The weather was hotter, but runtime per CDD fell within both seasons, and the 2F vent position and setpoints for both summers are unconfirmed (see the September report, Open Questions). The electric bill window was almost identical in cooling load across years: 252 vs 246 BDL CDD [D]. Even so, whole-house use was 5.57 kWh/day lower [D: 880 / 28 − 724 / 28]. A drop that size at equal CDD is not a cooling effect, and the September report shows it holds in every summer window.

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

### August 2026 vs August 2025

| Metric | August 2025 | August 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 16 CCF / $48.43 [M] | 8 CCF / $36.27 [M] | −8 CCF / −$12.16 [D] | DHW-led; 2025 bill 2 days longer |
| **DHW (Navien)** | 10.83 CCF *(6 op / 38 recirc h)* [D: 11.2357 Thm × 0.9643] | 5.59 CCF *(8 op / 12 recirc h)* [M] | −5.24 CCF, −48.4% [D: 5.59 / 10.83 − 1] | recirc hours 38 → 12 [M] |
| **Electric** | 880 kWh / $248.31 [M] | 724 kWh / $175.22 [M] | −17.7% kWh / −29.4% $ [D: 724 / 880 − 1; 175.22 / 248.31 − 1] | identical bill window (Jul 15–Aug 11) |
| **Effective rate** | $0.2822/kWh [D] | $0.2420/kWh [D] | −14.2% [D: 0.2420 / 0.2822 − 1] | all-in bill rate |
| **HDD65 (BDL)** | 19 [M] | 0 [M] | — | no furnace runtime either year |
| **CDD65 (BDL)** | 170 [M] | 263 [M] | +93 CDD, +54.7% [D: 263 / 170 − 1] | hotter August 2026 |
| **Cooling Runtime** | 62.07 h *(Honeywell; 2F 62.07 / 1F 0.00)* [M, Resideo daily] | 70.41 h *(Ecobee; 2F)* [M] | +8.34 h [D] | |
| **Cooling Intensity** *(BDL)* | **21.9 min/CDD** [D: 62.07 × 60 / 170] | **16.1 min/CDD** [D: 70.41 × 60 / 263] | −5.8 min/CDD [D] | single month, untested: see Sep season review |
| **Heating Intensity** | N/A | N/A | — | no heating |

**Gas decomposition:** Net gas (total − DHW) is 5.17 CCF in August 2025 [D: 16 − 10.83] and 2.41 CCF in August 2026 [D: 8 − 5.59]. The 2025 gas bill covers 30 days and the 2026 bill 28 [M], and DHW is calendar-month, so the residuals are not comparable at better than about 1 CCF.

**Key Insight (electric):** Over the identical Jul 15–Aug 11 window, BDL CDD was 252 (2025) and 246 (2026) [D, ACIS daily sums]: a 6-CDD difference. Whole-house use was 31.43 vs 25.86 kWh/day [D: 880 / 28; 724 / 28]. At 0.915 kWh per CDD for the compressor [D: 2026 daily OLS, n=90 days], 6 CDD accounts for about 5.5 kWh of the 156 kWh difference [D: 6 × 0.915; 880 − 724]. The rest is not explained by cooling load. The September report treats this across all four summer windows.

---

## Month-over-Month Analysis

### Natural Gas (July 2026 → August 2026)

| Metric | July 2026 | August 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 13 [M] | 8 [M] | −5 CCF [D] |
| DHW CCF (Navien) | 8.39 [M] | 5.59 [M] | −33.4% [D: 5.59 / 8.39 − 1] |
| Net Gas *(mixed basis)* | 4.61 [D] | 2.41 [D] | at bill resolution |
| HDD65 *(BDL)* | 2 [M] | 0 [M] | — |

**Analysis:** DHW fell by 2.80 CCF [D]. Recirculation fell from 17 to 12 h and operating hours from 10 to 8 [M]. Late-summer inlet water is the warmest of the year, which also lowers DHW gas, but inlet temperature is not measured here.

### Electric & Cooling (July 2026 → August 2026)

| Metric | July 2026 | August 2026 | MoM Change |
|---|---|---|---|
| Electric *(bill slot)* | 966 kWh / $210.69 [M] | 724 kWh / $175.22 [M] | −25.1% kWh [D: 724 / 966 − 1] |
| CDD65 *(BDL)* | 285 [M] | 263 [M] | −22 CDD [D] |
| Cooling Runtime | 113.61 h *(29 d)* [M] | 70.41 h *(31 d)* [M] | −43.2 h [D] |
| Cooling Intensity *(BDL)* | 26.6 min/CDD [D] | 16.1 min/CDD [D] | −10.5 min/CDD [D] |
| Cycles / min per cycle | 236 / 28.9 [M / D] | 173 / 24.4 [M / D] | |
| Cycles per day | 8.14 [D: 236 / 29] | 5.58 [D: 173 / 31] | 8 zero-run days in August [M] |
| Compressor (SEM) | 332.8 kWh [M] | 180.9 kWh [M] | −151.9 kWh [D] |
| Compressor kWh / BDL CDD | 1.168 [D] | 0.688 [D] | |
| Whole home (SEM) | 914.0 kWh [M] | 550.7 kWh [M] | −363.3 kWh [D] |
| Dehumidifier *(Kasa)* | 131.9 kWh [M] | 28.2 kWh [M] | −103.7 kWh [D]; unit replaced |

**Analysis:** CDD fell by 22 (−7.7% [D: 263 / 285 − 1]). Runtime fell by 43.2 h, and compressor energy by 151.9 kWh [D]. Cooling demand per degree-day fell inside the season. The same direction appears in 2025 (28.5 → 21.9 min/CDD [D]). Two years cannot establish a mechanism: candidates include solar angle, the building's stored heat, and humidity, and none was measured. The dehumidifier fell by 103.7 kWh [D]. The E080's measured average is 0.93 kWh/day [M: n=46 days, 2026-08-08..09-22, `SYSTEM_SPECIFICATIONS.md`], which predicts 28.8 kWh for a full month [D: 0.93 × 31], matching the August reading. The drop is a unit swap plus RH-threshold changes, and the two are not separated here.

---

## DHW Performance Update

| Metric | August 2025 | August 2026 | Change |
|---|---|---|---|
| DHW Gas (Navien) | 10.83 CCF [D] | 5.59 CCF [M] | −48.4% [D] |
| DHW Operating Hours | 6 h [M] | 8 h [M] | +2 h |
| DHW Recirc Hours | 38 h [M] | 12 h [M] | −26 h |
| Gas per operating hour | 1.81 CCF/h [D: 10.83 / 6] | 0.70 CCF/h [D: 5.59 / 8] | operating hours are integer-quantized |

**Note:** Operating hours rose (6 → 8) while gas fell, so per §5E the drop is *consistent with* the recirculation reduction (38 → 12 h), not proven by it. Navien resolution is ±0.17 CCF per month [D: 0.5 m³ × 0.36245 × 0.9643].

---

## HDD & Cooling Methodology Note

**Reference:** ACIS BDL daily HDD65/CDD65 [M]. August 2026: 0 HDD / 263 CDD. The HA proxy logged 0 HDD / 214.3 CDD [M], an under-count of 48.7 CDD [D: 263 − 214.3]. The proxy under-counted CDD in every summer month of 2026: 39.4 in June, 31.7 in July, 48.7 in August, and 12.2 in September [D: BDL − proxy]. Every per-CDD figure here uses BDL. Using the proxy instead would raise August cooling intensity to 19.7 min/CDD [D: 70.41 × 60 / 214.3].

---

## Cooling Runtime Performance

### Cooling — full month, SEM-metered

| Quantity (August 2026) | Value | Source |
|---|---|---|
| Thermostat call time | 70.41 h, 31 days | [M] `hvac_daily_2026.csv` |
| Cycles | 173 | [M] |
| Mean min/cycle | 24.4 | [D: 70.41 × 60 / 173] |
| Compressor energy (`sem_ac_energy`) | 180.9 kWh | [M] `energy_daily_master.csv` |
| Compressor energy per call-hour | 2.57 kW | [D: 180.9 / 70.41] |
| Compressor kWh per BDL CDD | 0.688 | [D: 180.9 / 263] |
| Air-handler circuit (`sem_furnace_energy`) | 82.8 kWh | [M]; includes fan-only/standby |
| Cooling-attributable blower | ≈ 45.2 kWh | [D: 0.250 × 180.9; blower fit n=128 h] |
| Whole home (SEM) | 550.7 kWh | [M] |

The compressor draw per call-hour (2.57 kW [D]) matches July (2.62 kW [D]). The September report gives the season fit, and the conflict with the 4.9 kW figure in `SYSTEM_SPECIFICATIONS.md` stays open.

---

## Recommendations

### Monitoring Priorities
1. **Within-season decline in runtime per CDD.** It appears in both years [D]. Any single-month controller comparison must be read against it. The September season review uses a daily regression for that reason.
2. **E080 energy baseline.** August is the first E080 month: 28.2 kWh [M]. Compare September on the same thresholds before drawing any efficiency conclusion.

### Pending / Data Hygiene
- The `monthly_summary.csv` DHW-units defect and the 2025 cooling-zone swap carry over from the July report. Correction is pending Bill's confirmation and goes in a separate commit.
- `data/daily_temperature.csv` still ends 2026-02-28, so V-HVAC-7 HALT is pre-existing.

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-08
archive_slot: august
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/*.csv rows appended, this report)

DATA ENTERED / VALIDATED (August 2026)
  HDD65:        0.0 proxy    (BDL 0)
  CDD65:        214.3 proxy  (BDL 263)
  Furnace_Hrs:  0.0          -> Heating Intensity N/A
  Cool_Hrs:     70.41 daily / 70.3 HA accumulator  [2F; 173 cycles]
  Gas_CCF:      8            Gas_Cost: 36.27   (read 08-12)
  DHW_CCF:      5.59         DHW_Op_Hrs: 8    DHW_Recirc_Hrs: 12
  Elec_kWh:     724          Elec_Cost: 175.22 (read 08-11; eff rate $0.2420/kWh)
  SEM:          compressor 180.9 / blower 82.8 / whole 550.7 kWh; dehumidifier 28.2 kWh (Kasa, E080)

VALIDATION
  Daily->monthly: 31/31 rows; 70.41 h vs accumulator 70.3 h.
  V1 range check:     PASS - Elec 724 vs trailing-3 mean 594 (+21.9% [D: 724 / ((311+505+966)/3) - 1]).
                      FLAG(expected) - Gas 8 vs trailing-3 mean 23.0 (-65.2% [D]): summer DHW floor.
  V2 direction check: N/A - no heating load.
  V3 prior data:      PRESENT - August 2025 gas/elec/DHW (therms, converted) and Resideo daily runtime.

METRICS (YoY, BDL basis)
  Cooling intensity:  21.9 -> 16.1 min/CDD  [single month, untested]
  Gas:                16 -> 8 CCF; DHW 10.83 -> 5.59 CCF (recirc 38 -> 12 h)
  Electric:           880 -> 724 kWh; $248.31 -> $175.22 (identical bill windows, 252 vs 246 CDD)

FLAGS
  Runtime/CDD fell Jul->Aug in both years - seasonal confound for single-month comparisons.
  Dehumidifier unit swap (Santa Fe -> Aprilaire E080, first cycle 08-05).

COMMIT MESSAGE: see September report (Jul-Sep committed together).
README UPDATE NEEDED: YES - done with the September update (v1.7.0).
```

---

*Sources: `hvac_daily_2026.csv`, `hvac_monthly.csv`, ACIS BDL daily/monthly degree days, SEM-Meter per-circuit energy (`energy_daily_master.csv`), Kasa dehumidifier energy, Navien archive, HA gas/electric bill archives, and the 2025 Resideo export (`2025 Resideo Thermostat Data.xlsx`).*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + American Standard Silver 14 AC + Navien NPE-240S2 tankless DHW. Two-zone forced air, 2,440 sq. ft., East Hampton CT. Thermostats: Ecobee Smart Enhanced (2026) vs Honeywell T6 Pro (2025).*
