# HVAC Performance Update: September 2026 + 2025 vs 2026 Cooling-Season Review

**Version:** 1.9.0
**Date:** October 15, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Shoulder-month report (template §4: same-month prior-year comparison only, no comparison with the annual baseline). It adds a **full cooling-season comparison of the Honeywell T6 Pro (2025) and the Ecobee Smart Enhanced (2026)**. Degree days are **ACIS Hartford-Bradley (KBDL) HDD65/CDD65** throughout; the HA `outdoor_temp_live` proxy is shown as secondary only. Figures carry provenance tags: [M] measured, [S] spec, [D] derived (formula shown), [I] inferred (with its falsifying observation).

> **Data-integrity advisory (read first):**
> 1. **Shoulder month.** The BDL mean was 64.0 °F [M], with 85 HDD and 62 CDD [M]. Furnace runtime was 0.0 h [M], so Heating Intensity is N/A. Per template §4, September is compared with September 2025 only.
> 2. **Mixed measurement basis.** The electric bill read 09-10 covers Aug 12–Sep 10 (30 days) in both years [M]. The gas bills differ in length: the 2026 bill read 09-15 covers 34 days and the 2025 bill read 09-12 covers 29 days [M]. DHW is calendar-month, so net gas comes out negative this month (see Gas decomposition).
> 3. **2025 DHW was logged in therms.** The 2025 comparator is converted: 15.585 Thm × 0.9643 = 15.03 CCF [D].
> 4. **The season review compares one summer under each controller.** Year and controller are fully confounded. Its statistical results describe *the two summers*. They are not a causal estimate of the thermostat effect (see §Confounds and limits).

---

## Executive Summary

September 2026 was a typical shoulder month. BDL recorded 62 CDD and 85 HDD [M], against 66 CDD and 39 HDD in September 2025 [M]. The furnace did not run in either year [M]. The AC ran **20.82 h over 68 cycles on 16 days** [M], compared with **5.58 h on 3 days** in September 2025 [M, Resideo daily]. Gas held at 8 CCF and DHW at 8.39 CCF, against 15.03 CCF in September 2025 [M / D]. The electric bill was 474 kWh / $118.05 [M]. Its window was 49 CDD hotter than the same window in 2025 [D: 175 − 126], and use was still 145 kWh lower [D: 619 − 474].

**Season review, June–September, on BDL CDD:**
- **On hot days the Ecobee summer used less runtime per degree-day.** The daily regression slope was 19.91 min/CDD in 2026 and 25.96 in 2025 [D, OLS, n=120 / 122 days]. The difference, **−6.05 min/CDD**, has a week-block bootstrap 95% CI of [−11.06, −1.37], p ≈ 0.010 [D, B=5000].
- **On mild days it ran more.** On days of 1–4 CDD the AC ran on 20 of 24 days in 2026 and 12 of 29 in 2025 [M].
- **The season totals cannot be told apart.** Season runtime per CDD was 22.52 in 2026 and 25.54 in 2025 [D]. The difference, −3.02 min/CDD, has a 95% CI of [−7.95, 2.72], p ≈ 0.29 [D, B=5000].
- **Runtime per cycle** for 2026 averaged 25.9 min [D: 289.44 × 60 / 671] and lengthened by 1.285 ± 0.189 min per CDD [D, n=94 cooling days, p=1.1e-9]. The 2025 export has no cycle counts, so there is no 2025 comparison.
- **Compressor energy** for 2026 was 0.925 kWh per CDD over Jul–Sep [D: 564.3 / 610], drawing 2.725 ± 0.020 kW while called [D, n=90 days, R² 0.995]. 2025 compressor energy was not metered.
- **Whole-house electricity over identical bill windows** was 2,526 kWh in 2026 and 3,141 in 2025 [M]: 120 days each, at 769 vs 779 CDD [D]. It was about 5.15 kWh/day lower in every window regardless of cooling load [D, n=4 windows, sd 0.39]. That is a base-load difference, not a cooling one.

**Key September 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas | 8 CCF / $37.02 [M] | bill read 09-15, 34-day window |
| DHW (Navien) | 8.39 CCF [M] | 24 m³ Navien reading; op 11 h / recirc 17 h [M] |
| Net Gas (cooking + standby) | −0.39 CCF [D: 8 − 8.39] | mixed basis; negative = window mismatch, not a reading error |
| Weather Severity | 85 HDD65 / 62 CDD65 *(BDL)* [M] | HA proxy: 89.9 HDD / 49.8 CDD [M] |
| **Heating Intensity** | **N/A** | furnace 0.0 h [M] |
| **Cooling Runtime** | **20.82 h** *(30 days, 2F)* [M] | HA accumulator 20.8 h [M] |
| **Cooling Intensity** *(BDL)* | **20.1 min/CDD** [D: 20.82 × 60 / 62] | September 2025: 5.1 [D: 5.58 × 60 / 66] |
| Cycles | 68 [M] | 18.4 min/cycle [D: 20.82 × 60 / 68]; 16 cooling days [M] |
| AC compressor (SEM) | 50.6 kWh [M] | 0.816 kWh/BDL CDD [D: 50.6 / 62]; 2.43 kW per call-hour [D: 50.6 / 20.82] |
| Electric | 474 kWh / $118.05 [M] | bill read 09-10, Aug 12–Sep 10 |
| Dehumidifier (Kasa) | 24.0 kWh [M] | Aprilaire E080, second month |
| Mean Outdoor Temp | 63.5 °F (HA) / 64.0 °F (BDL) [M] | |

**Interpretation:** September's cooling result follows the season pattern. The 2026 controller ran on more mild days, and in a month of mostly mild days that turns into higher runtime per CDD than in September 2025. As template §4 requires for shoulder months, nothing here is set against an annual baseline.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HDD & Cooling Methodology Note](#hdd--cooling-methodology-note)
5. [Cooling Runtime Performance](#cooling-runtime-performance)
6. [2025 vs 2026 Cooling-Season Review](#2025-vs-2026-cooling-season-review)
7. [Recommendations](#recommendations)
8. [Open Questions](#open-questions)

---

## Year-over-Year Analysis

### September 2026 vs September 2025

| Metric | September 2025 | September 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 11 CCF / $41.38 [M] | 8 CCF / $37.02 [M] | −3 CCF / −$4.36 [D] | 2026 bill 5 days longer |
| **DHW (Navien)** | 15.03 CCF *(9 op / 51 recirc h)* [D: 15.585 Thm × 0.9643] | 8.39 CCF *(11 op / 17 recirc h)* [M] | −6.64 CCF, −44.2% [D: 8.39 / 15.03 − 1] | recirc hours 51 → 17 [M] |
| **Electric** | 619 kWh / $173.58 [M] | 474 kWh / $118.05 [M] | −23.4% kWh / −32.0% $ [D: 474 / 619 − 1; 118.05 / 173.58 − 1] | identical bill window (Aug 12–Sep 10) |
| **Effective rate** | $0.2804/kWh [D] | $0.2491/kWh [D] | −11.2% [D: 0.2491 / 0.2804 − 1] | all-in bill rate |
| **HDD65 (BDL)** | 39 [M] | 85 [M] | +46 HDD [D] | furnace 0.0 h both years |
| **CDD65 (BDL)** | 66 [M] | 62 [M] | −4 CDD [D] | |
| **Cooling Runtime** | 5.58 h, 3 cooling days *(Honeywell)* [M] | 20.82 h, 16 cooling days *(Ecobee)* [M] | +15.24 h [D] | mild-day running, see season review |
| **Cooling Intensity** *(BDL)* | 5.1 min/CDD [D] | 20.1 min/CDD [D] | +15.0 min/CDD [D] | single month; shoulder month |
| **Heating Intensity** | N/A | N/A | — | no furnace runtime |

**Gas decomposition:** Net gas (total − DHW) is −4.03 CCF for September 2025 [D: 11 − 15.03] and −0.39 CCF for September 2026 [D: 8 − 8.39]. Both negative values come from the windows not lining up. The gas bill covers mid-August to mid-September, and DHW is the calendar month; inlet water temperature is not measured, so the split between the two windows cannot be reconstructed. The `monthly_summary.csv` 2025-09 row holds −4.59 because it subtracts therms (15.585) from CCF. That is the standing units defect.

**Key Insight (electric):** In the identical Aug 12–Sep 10 window, BDL CDD was 126 in 2025 and 175 in 2026 [D]. HDD was 36 and 4 [D]. Use fell anyway, from 20.63 to 15.80 kWh/day [D: 619 / 30; 474 / 30]. A hotter window with lower use is the clearest single sign that the summer electricity drop is not cooling-driven (see the season review, Energy).

---

## Month-over-Month Analysis

### Natural Gas (August 2026 → September 2026)

| Metric | August 2026 | September 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 8 [M] | 8 [M] | 0 [D] |
| DHW CCF (Navien) | 5.59 [M] | 8.39 [M] | +50.1% [D: 8.39 / 5.59 − 1] |
| Net Gas *(mixed basis)* | 2.41 [D] | −0.39 [D] | window mismatch |
| HDD65 *(BDL)* | 0 [M] | 85 [M] | — |

**Analysis:** DHW rose by 2.80 CCF [D]. Operating hours rose from 8 to 11 and recirculation from 12 to 17 [M]. The furnace did not fire despite 85 BDL HDD [M]. Heating setpoints for September are not recorded here, so whether that reflects the setpoint or the building is not established.

### Electric & Cooling (August 2026 → September 2026)

| Metric | August 2026 | September 2026 | MoM Change |
|---|---|---|---|
| Electric *(bill slot)* | 724 kWh / $175.22 [M] | 474 kWh / $118.05 [M] | −34.5% kWh [D: 474 / 724 − 1] |
| CDD65 *(BDL)* | 263 [M] | 62 [M] | −201 CDD [D] |
| Cooling Runtime | 70.41 h [M] | 20.82 h [M] | −49.59 h [D] |
| Cooling Intensity *(BDL)* | 16.1 min/CDD [D] | 20.1 min/CDD [D] | +4.0 min/CDD [D]; mild-day running |
| Cycles / min per cycle | 173 / 24.4 [M / D] | 68 / 18.4 [M / D] | shorter cycles at low load |
| Compressor (SEM) | 180.9 kWh [M] | 50.6 kWh [M] | −130.3 kWh [D] |
| Whole home (SEM) | 550.7 kWh [M] | 439.1 kWh [M] | −111.6 kWh [D] |
| Dehumidifier *(Kasa)* | 28.2 kWh [M] | 24.0 kWh [M] | −4.2 kWh [D] |

**Analysis:** Cooling runtime per CDD rose as load fell. Mild days carry a fixed part of runtime, the fitted intercept of +0.28 h/day in 2026 (see the season review), and that part weighs more when CDD is small. Cycles shortened to 18.4 min [D], matching the 2026 fit of minutes per cycle against CDD.

---

## DHW Performance Update

| Metric | September 2025 | September 2026 | Change |
|---|---|---|---|
| DHW Gas (Navien) | 15.03 CCF [D] | 8.39 CCF [M] | −44.2% [D] |
| DHW Operating Hours | 9 h [M] | 11 h [M] | +2 h |
| DHW Recirc Hours | 51 h [M] | 17 h [M] | −34 h |
| Gas per operating hour | 1.67 CCF/h [D: 15.03 / 9] | 0.76 CCF/h [D: 8.39 / 11] | operating hours are integer-quantized |

**Note:** Operating hours rose, so per §5E the drop is *consistent with* the recirculation reduction, not proven by it. July and September read the same in both years: 24 m³ in 2026 and 43 m³ in 2025. That is Navien whole-m³ quantization at ±0.17 CCF [D: 0.5 × 0.36245 × 0.9643], not a copy error.

**Summer DHW, Jul–Sep:** 22.37 CCF in 2026 against 40.89 CCF in 2025 [D: 8.39 + 5.59 + 8.39; 15.03 + 10.83 + 15.03]. Operating hours were 29 against 24, and recirculation hours 46 against 143 [M].

---

## HDD & Cooling Methodology Note

**Reference:** ACIS BDL daily HDD65/CDD65 [M]. September 2026: 85 HDD / 62 CDD. The HA proxy logged 89.9 HDD / 49.8 CDD [M]. Every per-CDD figure uses BDL. In both years the daily BDL pull reproduces the monthly `reports/bdl_degree_days.csv` sums exactly for May–Oct [D].

---

## Cooling Runtime Performance

| Quantity (September 2026) | Value | Source |
|---|---|---|
| Thermostat call time | 20.82 h, 30 days | [M] `hvac_daily_2026.csv` |
| Cycles / cooling days | 68 / 16 | [M] |
| Mean min/cycle | 18.4 | [D: 20.82 × 60 / 68] |
| Compressor energy (`sem_ac_energy`) | 50.6 kWh | [M] |
| Compressor energy per call-hour | 2.43 kW | [D: 50.6 / 20.82] |
| Compressor kWh per BDL CDD | 0.816 | [D: 50.6 / 62] |
| Air-handler circuit (`sem_furnace_energy`) | 38.7 kWh | [M]; includes fan-only/standby |
| Whole home (SEM) | 439.1 kWh | [M] |

---

## 2025 vs 2026 Cooling-Season Review

### Scope and basis

| Item | 2025 | 2026 |
|---|---|---|
| Thermostat | Honeywell T6 Pro | Ecobee Smart Enhanced (installed ~2026-05-29) |
| Runtime source | Resideo daily per-floor run hours (`2025 Resideo Thermostat Data.xlsx`, sheet "Daily Temp Resideo Data") | HA `binary_sensor.hvac_ac_running` (either zone `hvac_action == cooling`, local `homekit_controller`) via `history_stats`; `hvac_daily_2026.csv` |
| Runtime meaning | thermostat call time | thermostat call time |
| Days | Jun 1–Sep 30, 122 of 122 [M] | Jun 1–Sep 30, 120 of 122 [M]; Jul 4–5 have no rows (grid outage, see July report) |
| 1F share of cooling | 3.36 h of 338.00 [M] | 0.39 h of 289.44 [M] |
| Cycles | not in the export | 671 [M] |
| Compressor energy | not metered | SEM `sem_ac_energy`, from 2026-06-28 [M] |
| Degree days | ACIS BDL daily CDD65 | ACIS BDL daily CDD65 |

Because 1F cooling is under 1% of the total in both years [D: 3.36 / 338.00; 0.39 / 289.44], the 2025 per-floor sum and the 2026 either-zone flag measure the same thing to within 3.36 h per season [D].

### Monthly comparison (BDL basis)

| Month | 2025 CDD | 2025 run h | 2025 min/CDD | 2026 CDD | 2026 run h | 2026 min/CDD | 2026 cycles | 2026 min/cycle | 2026 cycles/day |
|---|---|---|---|---|---|---|---|---|---|
| Jun | 198 [M] | 99.15 [M] | 30.0 [D] | 190 [M] | 84.60 [M] | 26.7 [D] | 194 [M] | 26.2 [D] | 6.47 [D] |
| Jul | 360 [M] | 171.20 [M] | 28.5 [D] | 285 (256 on 29 d) [M] | 113.61 [M] | 26.6 [D: 113.61 × 60 / 256] | 236 [M] | 28.9 [D] | 8.14 [D] |
| Aug | 170 [M] | 62.07 [M] | 21.9 [D] | 263 [M] | 70.41 [M] | 16.1 [D] | 173 [M] | 24.4 [D] | 5.58 [D] |
| Sep | 66 [M] | 5.58 [M] | 5.1 [D] | 62 [M] | 20.82 [M] | 20.1 [D] | 68 [M] | 18.4 [D] | 2.27 [D] |
| **Season** | **794** [M] | **338.00** [M] | **25.54** [D: 338.00 × 60 / 794] | **800** (771 on 120 d) [M] | **289.44** [M] | **22.52** [D: 289.44 × 60 / 771] | **671** [M] | **25.9** [D] | **5.59** [D: 671 / 120] |

Cooling days: 74 of 122 in 2025 and 94 of 120 in 2026 [M]. With the HA July accumulator in place of the 29 daily rows, the 2026 season is 297.43 h over 800 CDD, or 22.31 min/CDD [D: (84.60 + 121.6 + 70.41 + 20.82) × 60 / 800].

### Runtime vs CDD — daily regression

Model: `runtime_h = a + b × CDD_BDL`, one fit per year, on all days Jun 1–Sep 30 (zero-run days included).

| | 2025 (Honeywell) | 2026 (Ecobee) |
|---|---|---|
| n (days) | 122 | 120 |
| Slope b | 0.4327 ± 0.0216 h/CDD = **25.96 min/CDD** [D] | 0.3318 ± 0.0227 h/CDD = **19.91 min/CDD** [D] |
| Intercept a | −0.046 ± 0.192 h/day [D] | +0.280 ± 0.189 h/day [D] |
| R² | 0.770 [D] | 0.643 [D] |
| Lag-1 residual autocorrelation | 0.38 [D] | 0.53 [D] |
| CDD range fitted | 0–22 [M] | 0–23 [M] |

**Significance.** Residuals are serially correlated, so the OLS standard errors are too small. The primary test is therefore a **week-block bootstrap**: 18 week blocks per year resampled with replacement, B=5000, seed 20261015.

| Difference (2026 − 2025) | Point | 95% CI | two-sided p |
|---|---|---|---|
| Slope (min/CDD) | **−6.05** [D] | [−11.06, −1.37] [D] | ≈ 0.010 [D, B=5000] |
| Season ratio (min/CDD) | **−3.02** [D] | [−7.95, +2.72] [D] | ≈ 0.29 [D, B=5000] |

The pooled OLS interaction model agrees in direction. Its slope difference is −0.1009 ± 0.0316 h/CDD, t = −3.19, dof = 238, p = 0.0016 [D]. Its year offset is +0.326 ± 0.270 h/day, p = 0.23 [D]. Because of the autocorrelation, the bootstrap figures are the ones to quote.

**Fitted daily runtime at matched CDD** [D, from the per-year fits; inside the fitted range only]:

| CDD | 2025 | 2026 | Difference |
|---|---|---|---|
| 5 | 2.12 h | 1.94 h | −0.18 h [D] |
| 10 | 4.28 h | 3.60 h | −0.68 h [D] |
| 15 | 6.44 h | 5.26 h | −1.18 h [D] |

**By CDD band (descriptive; the regression above carries the test):**

| BDL CDD band | 2025 days (run days) | 2025 mean h/day | 2026 days (run days) | 2026 mean h/day |
|---|---|---|---|---|
| 0 | 29 (5) [M] | 0.09 [D] | 24 (7) [M] | 0.11 [D] |
| 1–4 | 29 (12) [M] | 0.94 [D] | 24 (20) [M] | 1.45 [D] |
| 5–9 | 26 (20) [M] | 2.89 [D] | 41 (38) [M] | 2.63 [D] |
| 10–14 | 21 (21) [M] | 5.19 [D] | 21 (19) [M] | 3.84 [D] |
| ≥ 15 | 17 (16) [M] | 7.30 [D] | 10 (10) [M] | 6.35 [D] |

**Reading.** The two summers differ in shape, not in total. In 2026 the AC ran on mild days that 2025 mostly skipped: 20 of 24 days at 1–4 CDD, against 12 of 29 [M]. It ran fewer hours on hot days, 3.84 vs 5.19 h/day at 10–14 CDD [D]. The two effects nearly cancel over a season, and the season totals are statistically indistinguishable (p ≈ 0.29 [D]). The weather distribution also differed: 2025 had 17 days of 15 CDD or more and 2026 had 10 [M]. A season-ratio comparison mixes that difference in, and the regression does not.

### Runtime per cycle (2026 only)

The 2025 Resideo export records daily run hours, not cycles. **2025 runtime per cycle is unmeasured**, and no 2025 figure is estimated.

| 2026 cycle metric | Value |
|---|---|
| Season cycles / cooling days | 671 / 94 [M] |
| Season mean min/cycle | 25.9 [D: 289.44 × 60 / 671] |
| Median min/cycle (per cooling day) | 23.1 [D, n=94 days] |
| min/cycle vs CDD | +1.285 ± 0.189 min per CDD, r = 0.58, p = 1.1e-9 [D, OLS, n=94] |
| Cycles per cooling day (median) | 7.5 [D, n=94] |
| Cycles per cooling day vs CDD | +0.452 ± 0.059 per CDD, r = 0.63, p = 1.4e-11 [D, OLS, n=94] |
| Minimum compressor runtime setting | raised from 10 to 15 min on 2026-06-07 (Ecobee setting, per `JUNE_2026_UPDATE.md`) |

On hotter days the Ecobee runs both longer cycles and more of them. At low load, September's 18.4 min/cycle [D] sits near the 15-minute floor set on 2026-06-07.

### Energy — kWh per CDD

**2026 compressor (measured):**

| | Jul | Aug | Sep | Jul–Sep |
|---|---|---|---|---|
| Compressor kWh (SEM) | 332.8 [M] | 180.9 [M] | 50.6 [M] | 564.3 [D] |
| BDL CDD | 285 [M] | 263 [M] | 62 [M] | 610 [D] |
| kWh per CDD | 1.168 [D] | 0.688 [D] | 0.816 [D] | **0.925** [D: 564.3 / 610] |
| kW per call-hour | 2.62 [D] | 2.57 [D] | 2.43 [D] | 2.725 ± 0.020 [D, daily OLS slope, n=90, R² 0.995] |

Daily compressor kWh against daily BDL CDD gives 0.915 ± 0.070 kWh/CDD (intercept −0.02, R² 0.663) [D, OLS, n=90 days]. June is excluded because the SEM-Meter was installed 2026-06-28 [M].

**2025 compressor: not metered.** A 2025 kWh/CDD figure can only be built as runtime × an assumed draw. That makes it runtime per CDD again in different units, so it adds no independent evidence. For completeness: if 2025 drew the 2026 2.725 kW, the 2025 season would be 1.16 kWh per CDD [I: 25.54 / 60 × 2.725; falsifier: a 2025 draw that differs from 2026, e.g. a nameplate or clamp reading not near 2.7 kW].

**Whole-house electricity over identical bill windows** (meter reads on 06-10, 07-14, 08-11, 09-10 and 10-08 in both years [M]):

| Window | Days | 2025 kWh | 2026 kWh | 2025 CDD | 2026 CDD | 2025 kWh/day | 2026 kWh/day | Drop, kWh/day |
|---|---|---|---|---|---|---|---|---|
| Jun 11–Jul 14 | 34 | 1,129 [M] | 966 [M] | 339 [D] | 318 [D] | 33.21 [D] | 28.41 [D] | 4.80 [D] |
| Jul 15–Aug 11 | 28 | 880 [M] | 724 [M] | 252 [D] | 246 [D] | 31.43 [D] | 25.86 [D] | 5.57 [D] |
| Aug 12–Sep 10 | 30 | 619 [M] | 474 [M] | 126 [D] | 175 [D] | 20.63 [D] | 15.80 [D] | 4.83 [D] |
| Sep 11–Oct 8 | 28 | 513 [M] | 362 [M] | 62 [D] | 30 [D] | 18.32 [D] | 12.93 [D] | 5.39 [D] |
| **Total** | **120** | **3,141** [M] | **2,526** [M] | **779** [D] | **769** [D] | 26.18 [D] | 21.05 [D] | 5.15 mean, sd 0.39 [D, n=4] |

Whole-house kWh per CDD over the 120 days was 4.032 in 2025 and 3.285 in 2026 [D: 3141 / 779; 2526 / 769]. That figure carries the base-load difference and **is not a thermostat metric**. The daily drop is nearly constant (sd 0.39 kWh/day across 4 windows [D]). It does not follow the CDD difference: the Aug 12–Sep 10 window was 49 CDD hotter in 2026 and still dropped 4.83 kWh/day. A drop driven by cooling would shrink in that window by about 1.5 kWh/day [D: 49 × 0.915 / 30]. The data therefore point to a change of roughly 215 W in continuous load between the two summers [I: 5.15 / 24; falsifier: identification of loads that ran in summer 2025 and not in 2026, or a cooling-driven drop that varies with ΔCDD once more windows are added]. The cause cannot be found in this data, because 2025 had no circuit-level metering. See Open Questions.

The SEM whole-home total closes against the utility meter over the same windows: 705.2 vs 724, 485.7 vs 474, and 353.7 vs 362 kWh [M]. The SEM circuits are therefore a sound basis for the 2026 figures.

### Compressor draw — conflict with the spec file

The SEM fit gives **2.725 ± 0.020 kW** of compressor draw per hour of thermostat call. The median day is 2.50 kW (p10 2.40, p90 2.70) [D, n=59 days with more than 0.5 h]. `SYSTEM_SPECIFICATIONS.md` lists "Measured Power Draw: 4.9 kW", and template §1 lists 4.9 kW as nameplate. The 2025 cooling-energy baseline in `BASELINE_REPORT.md`, 346 h × 4.9 kW = 1,694 kWh, rests on that figure. At the SEM-measured draw it would be 943 kWh [I: 346 × 2.725; assumes the 2025 draw equals 2026's; falsifier: the condenser nameplate (RLA, voltage) or a 2025 clamp reading near 4.9 kW]. An AC CT reading half the true value is ruled out: the July unmetered residual was 41.2 kWh of 914.0 [D], and a half-reading CT would have left at least 332.8 kWh unaccounted. **No correction is made here.** The 4.9 kW figure and the baseline stay as they are until the nameplate is read (Open Questions).

### Confounds and limits (R11)

1. **One season per controller.** Year and thermostat are fully confounded, with n = 1 summer each. Every difference above describes the two summers, and the thermostat is one candidate cause among the items below.
2. **Setpoints, schedules and system mode are not recorded for 2025.** In September 2025 the AC ran on 3 of 30 days, against 16 of 30 in 2026 [M]. That fits a mode or setpoint difference (for example, cooling switched off) as well as a control difference.
3. **2F supply vents** were closed about 50% on 2026-01-01 [M, Resideo note]. Their position in summer 2026 is unconfirmed. Because 2F carries more than 99% of cooling [D: 1 − 0.39 / 289.44], vent position changes the airflow the 2F zone delivers.
4. **Ecobee minimum compressor runtime** was raised from 10 to 15 min on 2026-06-07 (per `JUNE_2026_UPDATE.md`). This affects cycle length and mild-day runtime.
5. **Weather beyond CDD.** BDL is an airport station, not the site. CDD65 does not carry humidity (latent load), solar gain or wind. The linear model leaves 23% and 36% of daily variance unexplained [D: 1 − 0.770; 1 − 0.643].
6. **Moisture removal changed.** In 2026 the dehumidifier was metered at 134.7 kWh in June, 131.9 in July, 28.2 in August and 24.0 in September [M]. It was replaced in August, and 2025 dehumidifier operation was not metered.
7. **Missing days.** Jul 4–5 2026 are absent, a grid outage with partial-day operation (July report). Neither day affects the regression fits, which use only days with rows.
8. **Extrapolation.** The fits cover 0–23 CDD/day. No figure here applies outside that range.
9. **Not established:** that the Ecobee saves energy over a season; any 2025 cycle behaviour; any 2025 compressor energy.

### Conclusion

On the BDL basis over June–September, the 2026 Ecobee summer used **significantly less runtime per CDD on hot days**: slope difference −6.05 min/CDD, 95% CI [−11.06, −1.37], p ≈ 0.010 [D, week-block bootstrap]. It used **more runtime on mild days**. The season totals do not differ detectably: −3.02 min/CDD, 95% CI [−7.95, +2.72], p ≈ 0.29 [D]. The study design cannot attribute either effect to the thermostat. Answers to the setpoint, vent and system-mode questions would remove the largest alternatives. The whole-house electricity reduction (−615 kWh over identical 120-day windows [D: 3141 − 2526]) is real, but it is a near-constant daily difference unrelated to cooling load, and the thermostat is not credited with it.

---

## Recommendations

### Monitoring Priorities
1. **Record 2F cooling setpoints, schedules and system mode** each summer from 2027 on. Without them, the next comparison has the same confound.
2. **Resolve the compressor draw.** Read the condenser nameplate (model, RLA). Until that is done, neither the 4.9 kW figure nor the 1,694 kWh 2025 baseline can be used for energy claims.
3. **Explain the ~5 kWh/day base-load drop** between summers before attributing electricity savings to any one change.
4. **Heating season.** October brings the first furnace runtime since May. The heating-side Ecobee comparison (runtime/HDD, cycles) starts then, on BDL HDD65.

### Pending / Data Hygiene
- **Historical rows** in `monthly_summary.csv`: DHW therms-as-CCF (2024-10..2026-01) and the 2025 Cool_1F/Cool_2F swap. A correction needs Bill's approval and goes in a separate commit.
- **Month labels in the bill CSVs.** In `monthly_electricity_eversource.csv` and `monthly_gas_scg.csv`, the unquoted rows through 2025-12-01 are labelled by usage month (2025-06-01 = 1,129 kWh, the bill read 2025-07-14). The quoted rows from 2026-02-01 on are labelled by slot month, and there is no 2026-01-01 row. `monthly_summary.csv` uses slot months throughout, and every figure in these reports uses the slot basis. Relabelling needs Bill's approval and belongs in the same separate commit.
- **`data/daily_temperature.csv` ends 2026-02-28.** V-HVAC-7 HALT is pre-existing for every month since March.
- **`UPDATES.md`** has no entries for March–June 2026, which were never prepended. This update adds July–September only.

---

## Open Questions

These are physical facts and settings. They come from Bill, not from inference (R14).
1. **Condenser nameplate:** model, RLA and voltage. What was the "4.9 kW measured" figure in `SYSTEM_SPECIFICATIONS.md` measured with? *Blocks: the 2025 cooling-energy baseline and any 2025 kWh/CDD.*
2. **Summer settings:** were the 2F vents still about 50% closed in summer 2026? Were 2F cooling setpoints and schedules the same in both summers? Was cooling switched off for part of September 2025? *Blocks: attributing the runtime differences to the thermostat.*
3. **Base load:** what ran continuously in summer 2025 and not in 2026 (or the reverse)? It amounts to about 5 kWh/day. *Blocks: attributing the electricity drop.*
4. **2025 cycle data:** is there any source of 2025 cycle counts (Resideo app history, a Honeywell export)? *Blocks: the 2025 runtime-per-cycle comparison.*

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-09
archive_slot: september
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/*.csv rows appended, Jul-Sep reports, README, UPDATES, CHANGELOG)

DATA ENTERED / VALIDATED (September 2026)
  HDD65:        89.9 proxy   (BDL 85)
  CDD65:        49.8 proxy   (BDL 62)
  Furnace_Hrs:  0.0          -> Heating Intensity N/A
  Cool_Hrs:     20.82 daily / 20.8 HA accumulator  [2F; 68 cycles]
  Gas_CCF:      8            Gas_Cost: 37.02   (read 09-15)
  DHW_CCF:      8.39         DHW_Op_Hrs: 11   DHW_Recirc_Hrs: 17
  Elec_kWh:     474          Elec_Cost: 118.05 (read 09-10; eff rate $0.2491/kWh)
  SEM:          compressor 50.6 / blower 38.7 / whole 439.1 kWh; dehumidifier 24.0 kWh (Kasa, E080)

VALIDATION
  Daily->monthly: 30/30 rows; 20.82 h vs accumulator 20.8 h.
  V1 range check:     FLAG(expected) - Elec 474 vs trailing-3 mean 731.7 (-35.2% [D: 474 / ((505+966+724)/3) - 1]): end of cooling season.
                      FLAG(expected) - Gas 8 vs trailing-3 mean 12.7 (-36.8% [D: 8 / ((17+13+8)/3) - 1]): summer DHW floor.
  V2 direction check: N/A - 85 BDL HDD but furnace 0.0 h; heating had not started.
  V3 prior data:      PRESENT - September 2025 gas/elec/DHW (therms, converted) and Resideo daily runtime.

METRICS (YoY, BDL basis)
  Cooling intensity (Sep):    5.1 -> 20.1 min/CDD   [single shoulder month]
  Season slope (Jun-Sep):     25.96 -> 19.91 min/CDD; diff -6.05, 95% CI [-11.06, -1.37], p~0.010 (week-block bootstrap, B=5000)
  Season ratio (Jun-Sep):     25.54 -> 22.52 min/CDD; diff -3.02, 95% CI [-7.95, 2.72], p~0.29 - NOT significant
  Whole-house, identical 120-day windows: 3,141 -> 2,526 kWh at 779 vs 769 CDD; ~5.15 kWh/day lower in every window (n=4, sd 0.39)

FLAGS
  SEM compressor 2.725 kW/call-h vs SYSTEM_SPECIFICATIONS 4.9 kW - unresolved; 2025 1,694 kWh cooling baseline rests on 4.9.
  Year and controller fully confounded - no causal thermostat claim.

COMMIT MESSAGE (ready to use)
  Residential-HVAC-Performance-Baseline-: git commit -m "2026.09: Add Jul-Sep 2026 monthly updates and 2025 vs 2026 AC season review (BDL CDD)"

README UPDATE NEEDED: YES - v1.7.0: METRICS, HIGHLIGHTS, 2026 YTD row, Recent Updates, footer.
```

---

*Sources: `hvac_daily_2026.csv`, `hvac_monthly.csv`, ACIS BDL daily HDD65/CDD65 (StnData, sid BDL), SEM-Meter per-circuit energy (`energy_daily_master.csv`), Kasa dehumidifier energy, Navien archive, HA gas/electric bill archives, and the 2025 Resideo export (`2025 Resideo Thermostat Data.xlsx`: daily per-floor runtime, notes, Eversource/CNG bills, Navien log).*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + American Standard Silver 14 AC + Navien NPE-240S2 tankless DHW. Two-zone forced air, 2,440 sq. ft., East Hampton CT. Thermostats: Ecobee Smart Enhanced (2026) vs Honeywell T6 Pro (2025).*
