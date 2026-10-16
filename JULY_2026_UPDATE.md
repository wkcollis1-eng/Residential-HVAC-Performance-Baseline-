# HVAC Performance Update: July 2026

**Version:** 1.8.2
**Date:** October 15, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Cooling-season report. Heating Intensity is **not computed** (no furnace runtime). Degree days are **ACIS Hartford-Bradley (KBDL) HDD65/CDD65** throughout; the HA `outdoor_temp_live` proxy is shown as secondary only. Figures carry provenance tags: [M] measured, [S] spec, [D] derived (formula shown), [I] inferred (with its falsifying observation).

> **Data-integrity advisory (read first):** July 2026 is the **first full month with the SEM-Meter metering the AC circuit**, so cooling *energy* is now measured rather than runtime-derived. Four caveats apply:
> 1. **Grid outage Jul 4–5.** SEM mains read 0 from 21:00 Jul 4 through 02:59 Jul 5, and 03:00–07:59 Jul 5 is absent from the hourly export [M, `www/energy/energy_2026-07-0{4,5}.csv`]. The AC did not run during the outage. It did run outside it: the compressor drew 21.384 kWh on Jul 4 before 21:00 and 13.478 kWh on Jul 5 from 08:00 [M, SEM hourly]. HA wrote **no daily runtime rows for Jul 4 or Jul 5** [M, `hvac_daily_2026.csv`, 29 of 31 days]. July runtime-per-CDD is therefore computed on the **29 days with rows** (113.61 h over 256 BDL CDD). The HA monthly accumulator (121.6 h [M]) is shown for reference but cannot be reconciled for those two days.
> 2. **Heating Intensity is N/A.** Furnace runtime was 0.0 h [M]; 2 BDL HDD [M] cannot carry a CCF/1k-HDD figure.
> 3. **Mixed measurement basis.** Runtime, cycles, CDD, and SEM/Kasa energy are calendar-month. Gas and electric are bill-slot values: the electric bill read 07-14 covers Jun 11–Jul 14 (34 days), and the gas bill read 07-15 covers about Jun 13–Jul 15 [M, bill-date helpers]. Navien DHW is calendar-month. Net gas (total − DHW) therefore mixes bases and is reported with that flag.
> 4. **2025 DHW was logged in therms.** The 2025 comparators here are converted: 15.585 Thm × 0.9643 = 15.03 CCF [D]. The `monthly_summary.csv` 2025 cell (15.585) is in therms, not CCF; this is a standing defect, see Pending.

---

## Executive Summary

July 2026 was the hottest month of the summer: 285 BDL CDD [M], with a BDL mean of 73.9 °F [M]. It was still milder than July 2025, which had 360 CDD and a 76.3 °F mean [M]. Cooling ran **113.61 h over 236 cycles on the 29 logged days** [M], at a mean **28.9 min/cycle** [D: 113.61 × 60 / 236]. Cooling intensity was **26.6 min/CDD** against **28.5 in July 2025** [D]. The two figures are close, and a single month carries no significance test; the September report tests the full season. Gas fell to 13 CCF and electricity to 966 kWh / $210.69 on the bill. DHW was the largest gas term and fell to 8.39 CCF against 15.03 CCF in July 2025, with recirculation hours down from 54 to 17 [M]. July is also the first full SEM month. The compressor drew **332.8 kWh**, about **2.6 kW per hour of thermostat call** [D].

**Key July 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas | 13 CCF / $44.30 [M] | bill read 07-15; no heating |
| DHW (Navien) | 8.39 CCF [M] | 24 m³ Navien reading; op 10 h / recirc 17 h [M] |
| Net Gas (cooking + standby) | 4.61 CCF [D: 13 − 8.39] | mixed basis (bill-slot gas − calendar DHW); at the 1-CCF bill resolution |
| Weather Severity | 2 HDD65 / 285 CDD65 *(BDL)* [M] | HA proxy: 2.4 HDD / 253.3 CDD [M] |
| **Heating Intensity** | **N/A** | furnace 0.0 h [M] |
| **Cooling Runtime** | **113.61 h** *(29 days, 2F)* [M] | HA accumulator 121.6 h incl. Jul 4–5 [M] |
| **Cooling Intensity** *(BDL)* | **26.6 min/CDD** [D: 113.61 × 60 / 256] | full-month accumulator basis: 25.6 [D: 121.6 × 60 / 285] |
| Cycles | 236 [M] | 28.9 min/cycle [D]; 8.14 cycles/day [D: 236 / 29] |
| AC compressor (SEM) | 332.8 kWh [M] | 1.168 kWh/BDL CDD [D: 332.8 / 285] |
| Electric | 966 kWh / $210.69 [M] | bill read 07-14, Jun 11–Jul 14 |
| Dehumidifier (Kasa) | 131.9 kWh [M] | prior unit, RH-band 49%/46% control |
| Mean Outdoor Temp | 73.3 °F (HA) / 73.9 °F (BDL) [M] | |

**Interpretation:** July is a cooling-and-moisture month. Gas is at its summer floor and DHW-dominated. Cooling intensity on the BDL basis is close to July 2025, and July alone cannot separate controller from weather. July 2025 was hotter (+75 CDD [D: 360 − 285]), and runtime per CDD varies across a season. The season-level comparison, with a significance test, is in the September report. The SEM data is the new information this month. Compressor energy per call-hour is about 2.6 kW. That is roughly half the "4.9 kW measured" in `SYSTEM_SPECIFICATIONS.md`, a conflict flagged below and not resolved here.

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

### July 2026 vs July 2025

| Metric | July 2025 | July 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 17 CCF / $50.01 [M] | 13 CCF / $44.30 [M] | −4 CCF / −$5.71 [D] | DHW-led |
| **DHW (Navien)** | 15.03 CCF *(9 op / 54 recirc h)* [D: 15.585 Thm × 0.9643] | 8.39 CCF *(10 op / 17 recirc h)* [M] | −6.64 CCF, −44.2% [D: 8.39 / 15.03 − 1] | recirc hours 54 → 17 [M] |
| **Electric** | 1,129 kWh / $315.86 [M] | 966 kWh / $210.69 [M] | −14.4% kWh / −33.3% $ [D: 966 / 1129 − 1; 210.69 / 315.86 − 1] | identical bill windows (Jun 11–Jul 14 both years) |
| **Effective rate** | $0.2798/kWh [D] | $0.2181/kWh [D] | −22.0% [D: 0.2181 / 0.2798 − 1] | all-in bill rate |
| **HDD65 (BDL)** | 0 [M] | 2 [M] | — | no heating either year |
| **CDD65 (BDL)** | 360 [M] | 285 [M] | −75 CDD, −20.8% [D: 285 / 360 − 1] | milder July 2026 |
| **Cooling Runtime** | 171.20 h *(Honeywell; 2F 169.62 / 1F 1.58)* [M, Resideo daily] | 113.61 h *(Ecobee; 29 d, 2F)* [M] | not comparable as totals | 2026 is missing 2 days |
| **Cooling Intensity** *(BDL)* | **28.5 min/CDD** [D: 171.20 × 60 / 360] | **26.6 min/CDD** [D: 113.61 × 60 / 256] | −1.9 min/CDD [D] | single month, untested: see Sep season review |
| **Heating Intensity** | N/A | N/A | — | no heating |

**Gas decomposition:** Net gas (total − DHW) is 1.97 CCF in July 2025 [D: 17 − 15.03] and 4.61 CCF in July 2026 [D: 13 − 8.39]. Neither figure is resolvable. The gas bill is integer CCF covering about Jun 13–Jul 15, and DHW is the calendar month, so the subtraction mixes two windows. The DHW drop (−6.64 CCF [D]) is larger than the total-gas drop (−4 CCF [D]), so the residual moved the other way by an amount within that basis error.

**Key Insight (electric):** The electric bill windows are identical in both years: reads on 06-10 and 07-14, 34 days [M, Resideo "Monthly Utilities" for 2025, HA bill-date helper for 2026]. Over that window BDL CDD was 339 in 2025 and 318 in 2026 [D, sum of ACIS daily CDD65]. Whole-house use was 33.21 vs 28.41 kWh/day [D: 1129 / 34; 966 / 34]. A cooling-only explanation is tested across all four summer windows in the September report; it does not hold.

> **Caveat on the cooling YoY:** Both runtimes are thermostat **call** time. The 2025 figure is Resideo's daily per-floor run time. The 2026 figure is `binary_sensor.hvac_ac_running` (either zone's `climate.*` `hvac_action == cooling`, via the local `homekit_controller` integration) through `history_stats`. 1F cooling is negligible in both years (1.58 h in July 2025, 0.0 h in July 2026 [M]), so summing floors (2025) versus "either zone" (2026) differs by at most 1.58 h [D].

---

## Month-over-Month Analysis

### Natural Gas (June 2026 → July 2026)

| Metric | June 2026 | July 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 17 [M] | 13 [M] | −4 CCF [D] |
| DHW CCF (Navien) | 11.53 [M] | 8.39 [M] | −27.2% [D: 8.39 / 11.53 − 1] |
| Net Gas *(mixed basis)* | 5.47 [D] | 4.61 [D] | at bill resolution |
| HDD65 *(BDL)* | 21 [M] | 2 [M] | — |

**Analysis:** Gas fell to the summer floor. DHW fell 3.14 CCF [D] as recirculation hours dropped from 30 to 17 [M] and summer inlet water warmed. Operating hours were 10 in both months [M].

### Electric & Cooling (June 2026 → July 2026)

| Metric | June 2026 | July 2026 | MoM Change |
|---|---|---|---|
| Electric *(bill slot)* | 505 kWh / $114.74 [M] | 966 kWh / $210.69 [M] | +461 kWh [D] |
| CDD65 *(BDL)* | 190 [M] | 285 [M] | +95 CDD [D] |
| Cooling Runtime | 84.60 h *(30 d)* [M] | 113.61 h *(29 d)* [M] | +29.0 h [D] |
| Cooling Intensity *(BDL)* | 26.7 min/CDD [D] | 26.6 min/CDD [D] | flat |
| Cycles / min per cycle | 194 / 26.2 [M / D] | 236 / 28.9 [M / D] | longer cycles on hotter days |
| Dehumidifier *(Kasa)* | 134.7 kWh [M] | 131.9 kWh [M] | −2.8 kWh [D] |

**Analysis:** Cooling intensity held at about 26.6–26.7 min/CDD across a +95 CDD step [D]. The electric bill nearly doubled because its window (Jun 11–Jul 14) captured the start of peak cooling. Cycle length rises with load. Across the 2026 season, minutes per cycle increase by 1.285 ± 0.189 min per CDD [D: OLS, n=94 cooling days, p=1.1e-9]. July's longer cycles are consistent with its hotter days.

---

## DHW Performance Update

| Metric | July 2025 | July 2026 | Change |
|---|---|---|---|
| DHW Gas (Navien) | 15.03 CCF [D: 15.585 Thm × 0.9643] | 8.39 CCF [M] | −44.2% [D] |
| DHW Operating Hours | 9 h [M] | 10 h [M] | +1 h |
| DHW Recirc Hours | 54 h [M] | 17 h [M] | −37 h |
| Gas per operating hour | 1.67 CCF/h [D: 15.03 / 9] | 0.84 CCF/h [D: 8.39 / 10] | operating hours are integer-quantized |

**Note:** DHW fell while operating hours rose by one, and recirculation hours fell by 37. Per template §5E, a recirc-savings claim needs equal operating hours, and these are not equal (9 vs 10). The DHW drop is therefore reported as *consistent with* the recirculation reduction, not proven by it. Resolution caveat: the Navien reports whole m³, so each monthly figure carries ±0.5 m³ ≈ ±0.17 CCF [D: 0.5 × 0.36245 × 0.9643]. That is why July and September 2026 read identically (24 m³ each), as did July and September 2025 (43 m³ each) [D: 15.585 / 0.36245 = 43.0].

---

## HDD & Cooling Methodology Note

**Reference:** ACIS station BDL (Hartford-Bradley), daily HDD65/CDD65 [M, `reports/bdl_degree_days.csv`, monthly; daily pull matches the monthly sums exactly for May–Oct of both years]. July 2026: 2 HDD / 285 CDD. The HA proxy logged 2.4 HDD / 253.3 CDD [M], which under-counts CDD by 31.7 [D: 285 − 253.3]. BDL is the primary basis for every per-CDD figure in this report. For July runtime-per-CDD, the denominator is BDL CDD **summed over the 29 days that have runtime rows** (256 [D]), so numerator and denominator cover the same days.

---

## Cooling Runtime Performance

### Cooling — first full SEM month

| Quantity (July 2026) | Value | Source |
|---|---|---|
| Thermostat call time | 113.61 h, 29 days | [M] `hvac_daily_2026.csv` |
| Cycles | 236 | [M] |
| Compressor energy (`sem_ac_energy`) | 332.8 kWh full month; 297.9 kWh on the 29 matched days | [M] `energy_daily_master.csv` |
| Compressor energy per call-hour | 2.62 kW | [D: 297.9 / 113.61] |
| Compressor kWh per BDL CDD | 1.168 (full month) / 1.164 (matched days) | [D: 332.8 / 285; 297.9 / 256] |
| Air-handler circuit (`sem_furnace_energy`) | 123.1 kWh | [M]; includes fan-only/standby, not cooling alone |
| Cooling-attributable blower | ≈ 83.2 kWh | [D: 0.250 × 332.8, blower fit from the SEM 11-day analysis, n=128 h] |
| Whole home (SEM) | 914.0 kWh | [M]; compressor = 36.4% [D: 332.8 / 914.0] |

**Compressor draw conflict.** Across Jul–Sep 2026, daily compressor kWh regresses on daily call-hours at **2.725 ± 0.020 kW, R² 0.995** [D: OLS, n=90 days]. Call time is therefore a faithful proxy for compressor operation, and the compressor draws about 2.7 kW while running. `SYSTEM_SPECIFICATIONS.md` lists "Measured Power Draw: 4.9 kW steady-state", and the report template lists 4.9 kW as nameplate. The SEM circuit closes against whole-home within 4.5% (July true residual 41.2 of 914.0 kWh [D]), so an AC CT reading half the true value would have left a residual near 330 kWh [D]. No cause is inferred here. The nameplate and the basis of the 4.9 kW figure are open questions for Bill (see the September report).

**Dehumidifier:** 131.9 kWh [M], the last full month of the prior unit. The Aprilaire E080 entered service in August 2026 (first logged compressor cycle 2026-08-05 [M, `SYSTEM_SPECIFICATIONS.md`]).

---

## Recommendations

### Monitoring Priorities
1. **Season-level thermostat comparison.** It is in the September report (daily regression on BDL CDD, n=242 days, with a week-block bootstrap). No single-month conclusion is drawn here.
2. **Resolve the 4.9 kW figure.** It sets the 2025 cooling-energy baseline (346 h × 4.9 kW = 1,694 kWh in `BASELINE_REPORT.md`).

### Pending / Data Hygiene
- **Jul 4–5 runtime rows** are missing from `hvac_daily_2026.csv`. SEM shows compressor energy on both days outside the outage window. The EOD row writer did not record either day; the cause is not established.
- **`monthly_summary.csv` DHW units:** the 2024-10 through 2026-01 cells hold Navien therms, not CCF. The 2025 Cool_1F/Cool_2F columns are swapped relative to the Resideo export (2F carried 97/170/62/6 h). Both corrections wait for Bill's confirmation and go in a separate commit.
- **`data/daily_temperature.csv` ends 2026-02-28.** `validate_month.py` V-HVAC-7 HALTs for every month since March (pre-existing; the June row also HALTs).

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-07
archive_slot: july
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/*.csv rows appended, this report)

DATA ENTERED / VALIDATED (July 2026)
  HDD65:        2.4 proxy    (BDL 2)
  CDD65:        253.3 proxy  (BDL 285)
  Furnace_Hrs:  0.0          -> Heating Intensity N/A
  Cool_Hrs:     121.6 HA accumulator; 113.61 on 29 daily rows (Jul 4-5 no rows)  [2F; 236 cycles on 29 d]
  Gas_CCF:      13           Gas_Cost: 44.30   (read 07-15)
  DHW_CCF:      8.39         DHW_Op_Hrs: 10   DHW_Recirc_Hrs: 17
  Elec_kWh:     966          Elec_Cost: 210.69 (read 07-14; eff rate $0.2181/kWh)
  SEM:          compressor 332.8 / blower 123.1 / whole 914.0 kWh; dehumidifier 131.9 kWh (Kasa)

VALIDATION
  Daily->monthly: 29/31 rows; 113.61 h vs accumulator 121.6 h - 8.0 h attributed to Jul 4-5 by the accumulator, unverifiable.
  V1 range check:     FLAG(expected) - Elec 966 vs trailing-3 mean 367 (+163% [D: 966 / ((285+311+505)/3) - 1]): bill window caught peak cooling onset.
                      FLAG(expected) - Gas 13 vs trailing-3 mean 38.3 (-66.1% [D: 13 / ((59+39+17)/3) - 1]): heating ended in May; summer DHW floor.
  V2 direction check: N/A - no heating load.
  V3 prior data:      PRESENT - July 2025 gas/elec/DHW (therms, converted) and Resideo daily runtime.

METRICS (YoY, BDL basis)
  Cooling intensity:  28.5 -> 26.6 min/CDD  [single month, untested]
  Gas:                17 -> 13 CCF; DHW 15.03 -> 8.39 CCF (recirc 54 -> 17 h)
  Electric:           1,129 -> 966 kWh; $315.86 -> $210.69 (identical bill windows)

FLAGS
  Jul 4-5 grid outage: no HA daily rows; AC ran outside the outage window (SEM 21.384 / 13.478 kWh).
  SEM compressor 2.62 kW/call-h vs SYSTEM_SPECIFICATIONS 4.9 kW - unresolved.
  monthly_summary.csv DHW therms-as-CCF (2024-10..2026-01) and 2025 cooling zone swap - correction pending.

COMMIT MESSAGE: see September report (Jul-Sep committed together).
README UPDATE NEEDED: YES - done with the September update (v1.7.0).
```

---

*Sources: `hvac_daily_2026.csv`, `hvac_monthly.csv`, ACIS BDL daily/monthly degree days, SEM-Meter per-circuit energy (`energy_daily_master.csv`, hourly `energy_2026-07-0{4,5}.csv`), Kasa dehumidifier energy, Navien archive, HA gas/electric bill archives, and the 2025 Resideo export (`2025 Resideo Thermostat Data.xlsx`: daily runtime, Navien log, Eversource/CNG bills).*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + American Standard Silver 14 AC + Navien NPE-240S2 tankless DHW. Two-zone forced air, 2,440 sq. ft., East Hampton CT. Thermostats: Ecobee Smart Enhanced (2026) vs Honeywell T6 Pro (2025).*
