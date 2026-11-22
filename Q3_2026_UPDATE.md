# HVAC Performance Update: Q3 2026 vs Q3 2025 + Nine-Month Summary

**Version:** 1.11.0
**Date:** November 22, 2026 (1.10.0: November 13, 2026)
**Revision 1.11.0:** Bill, 2026-11-22: the 2025 trip was in mid-August 2025, about 8 days, not 10–12 days in September as 1.10.0 had it. The exact days, and whether the water heater was off, are not known. Every figure that depended on the trip's dates is recomputed (advisory 2, executive summary, §1.3, §1.4, §4.2–§4.4, §4.6, §5, §7). The 1.10.0 figures stay in the tables, marked superseded, and are listed in §6. The trip's exact days are used for the arithmetic only and are not published.
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Quarterly report in place of the October monthly update. Q3 means July–September. Bills are attributed by **slot month** (`data/monthly_summary.csv`, bill-date month). SEM-Meter and SDR radio-meter figures are **calendar months**. Degree days are ACIS Bradley (BDL) HDD65/CDD65. Daily degree days are built from `data/daily_temperature.csv` by rounding each daily mean half-up and then subtracting from 65. That reproduces the ACIS monthly sums in all 21 months from January 2025 to September 2026 [D, 0 of 21 mismatched]. Tags: [M] measured, [S] spec, [D] derived (formula shown), [I] inferred (falsifier stated).

> **Data-integrity advisory (read first):**
> 1. **Mixed basis.** Gas and electricity are bill slots. DHW is calendar-month Navien readings. SEM and SDR are calendar months. Non-DHW gas (total gas − DHW) therefore mixes two bases and can go negative, as in September 2026 (−0.39 CCF).
> 2. **An 11-day absence in mid-August 2026.** Bill, 2026-11-13: the house was empty for part of the September gas slot, with the water heater off and no cooking. The meters show it directly. On the 9 full days the microwave, both counter circuits and the computer outlet read 0, whole-home use was 6.1–11.3 kWh/day, and the Navien plug held at its 0.203 kWh/day standby [M]. The AC ran on 2 of those 9 days, one cycle each [M]. With the partial days either side, 11 days are affected: 4 in the Jul 15–Aug 11 electric window and 7 in the Aug 12–Sep 10 window. They are dropped from the daily AC fits (§4), and their effect on the bills is estimated in §1.3 and §1.4. 2025 had one too: a trip of about 8 days in mid-August 2025 (Bill, 2026-11-22, correcting the September dates of 2026-11-13). Its exact days are not known, so the 2025 AC fits drop a 12-day span that covers every day such a trip could have fallen on (§4.3), and its effect on the 2025 bills is modelled in §1.3. Both absences fall mostly in the Aug 12–Sep 10 electric window. The September gas bill, which the 2026 absence explains, is resolved in §3.2.
> 3. **One summer per controller.** 2025 ran a Honeywell T6 Pro and 2026 an Ecobee. Year and controller are fully confounded. The AC results describe *the two summers*; they are not a causal estimate of the thermostat effect (§4.6).
> 4. **The 2026 daily AC rows miss Jul 4–5** (grid outage), days that carried 29 CDD [D]. The daily fits use the 90 days that have rows. The bill-slot table uses the HA accumulator's July total (121.6 h).
> 5. **SDR full months.** The radio meters start 2026-08-21, so **September is the only full SDR month in Q3**. The 11 August days are left out of all SDR totals, and October belongs to Q4.
> 6. **The H1 overview's DHW and space-heat figures are superseded.** They summed raw cells, several of which held therms, before the 2026-10-15 correction. In consistent CCF, H1 DHW was 115.73 → 78.64 CCF and H1 space heat 441.27 → 490.36 CCF [D, `monthly_summary.csv` as corrected].

---

## Executive Summary

- **Weather.** Q3 2026 had 610 CDD against 596 in Q3 2025 [M], +14 CDD (+2.35% [D: 610 / 596 − 1]). The daily CDD distributions cannot be told apart (Mann-Whitney p = 0.76, KS D = 0.120, p = 0.53, n = 92 / 92 days). The heat fell in different months: July 2025 ran 360 CDD against 285, and August 2026 ran 263 against 170 [M].
- **Electricity.** 2,164 kWh in 2026 against 2,628 in 2025 [M]: −464 kWh, −17.66% [D: 2164 / 2628 − 1]. The bill window was the same 92 days in both years (Jun 11–Sep 10), at 739 vs 717 CDD [D]. Cost fell from $737.75 to $503.96 (−31.69% [D]); volume accounts for $130.26 of the drop and the lower rate for $103.53 [D, §1.1]. Use was 4.80, 5.57 and 4.83 kWh/day lower in the three windows [D]. The 2026 absence (advisory 2) accounts for an estimated 197.4 kWh of the 464 [D: 82.7 + 114.7, §1.3]. Without it, the drop is 2.90 kWh/day, not 5.04 [D]. The mid-August 2025 trip lowered the 2025 side by an estimated 101–168 kWh, depending on its exact days [I, §1.3]. With both put back, Q3 use was 4.00–4.73 kWh/day lower, and the three windows 4.80, 2.62–3.39 and 4.38–6.09 kWh/day lower [I]. With n = 3 windows no test has power. The nine-month paired test (§5) is p = 0.026 as measured, p = 0.060 with only the 2026 absence adjusted, and p = 0.031–0.035 with both [I].
- **Gas.** 29 CCF against 44 [M] (−34.09% [D: 29 / 44 − 1]) and $117.59 against $139.82 [M]. DHW was 22.37 against 40.89 CCF (−45.29% [D: 22.37 / 40.89 − 1]). It was lower in all 3 months [D], and recirculation ran 46 h against 143 [M]. The 2026 absence removed an estimated 2.5–3.1 CCF of that DHW and 3.1–3.8 CCF of total gas [D, §1.4]. The 2025 trip lowered 2025 DHW as well: August 2025 read 10.83 CCF against 15.03 in both July and September [M], a shortfall of about 9 days' use at the July–September rate [D, §1.4]. With both put back, Q3 DHW is about 24.9–25.5 CCF in 2026 against 44.3–45.3 in 2025 [I, §1.4], so the drop is no smaller. The furnace ran 0 h in both quarters [M].
- **AC: a lower 2026 slope, borderline in Q3 and clear over June–September, with no change in total runtime per CDD.** Without the 11 absent days of 2026, and without the 12-day mid-August 2025 span the 2025 trip could have covered, the slopes are 22.95 min/CDD in 2026 and 25.76 in 2025 [D, OLS, n = 79 / 80 days]. The difference, −2.81 min/CDD, has a 95% CI of [−6.30, +0.21], p ≈ 0.063 [D, week-block bootstrap, B = 5000]. For five 8-day placements of the trip inside that span it is −2.83 to −3.26, p 0.033–0.062, and 4 of the 5 are below 0.05 [D, §4.3]. In Q3 the result therefore depends on the trip's exact days, which are not known. Over June–September it does not: the slope difference is −4.32 [−7.69, −1.13], p ≈ 0.006, and −4.35 to −4.54 (p 0.003–0.004) for the five placements [D, §4.6 item 6]. The quarter-ratio difference is +0.26, p ≈ 0.92, and the season ratio −0.75, p ≈ 0.71 [D]: total runtime per CDD did not differ. A lower slope at the same ratio is a change of shape, not of total. 2026 ran on more mild days: at 1–4 CDD on 14 of 15 days against 6 of 19 (Fisher exact p = 0.0004 [D]; 0.0003–0.0004 for the placements), mostly at low runtime, and slightly fewer hours per day in every band from 5 CDD up (§4.4). 1.10.0 reported no detectable change (−1.10 min/CDD, p ≈ 0.54). That rested on September 2025 dates that Bill has since corrected, and it is superseded (§4.3).
- **SEM-Meter, Jul–Sep 2026.** The whole home used 1,903.86 kWh [M]. The AC compressor took 564.27 kWh, 29.6% of that [D: 564.27 / 1903.86]. The air handler took 244.60 kWh and the dehumidifier 184.11 [M], 72% of the dehumidifier's in July, before it was replaced [D: 131.93 / 184.11]. There is no 2025 SEM data, so no circuit has a year-over-year figure.
- **SDR radio meters, September 2026.** The utility electric meter read 437.31 kWh and the SEM 439.10, so the SEM reads +0.41% high [D: 439.10 / 437.31 − 1]. The daily figure is +0.39%, sd 0.18, n = 30 days. Gas was 10.54 CCF; less the Navien's 8.39 CCF, non-DHW gas was about 2.1 CCF [D]. That replaces the bill-basis −0.39. Water was 2,641.1 gal, 88.0 gal/day [M].
- **Nine months (Jan–Sep).** Electricity was 4,558 against 5,284 kWh (−13.74% [D]; paired monthly t = −2.72, p = 0.026, n = 9; Wilcoxon p = 0.055). Adjusted for the 2026 absence alone the drop is 528.7 kWh, t = −2.19, p = 0.060 [D, §5.1]. Adjusted for the mid-August 2025 trip as well it is 630–697 kWh, t = −2.53 to −2.62, p = 0.031–0.035, Wilcoxon p = 0.055 [I, §5.1]. Gas was 598 against 601 CCF (paired p = 0.93, n = 9) on 12.83% more HDD [D: 3869 / 3429 − 1]. DHW was 101.01 against 156.63 CCF (−35.51% [D]), lower in 9 of 9 months (t = −6.74, p = 0.0001). Heating intensity Jan–May was unchanged: 128.93 vs 129.67 CCF per 1,000 HDD, regression difference +0.24 ± 7.71, p = 0.98, n = 10 months [D].

---

## 1. Q3 2026 vs Q3 2025 — bills

### 1.1 Quarter totals

| Metric | Q3 2025 | Q3 2026 | Change |
|---|---|---|---|
| HDD65 (BDL) | 58 [M] | 87 [M] | +29 [D] |
| CDD65 (BDL) | 596 [M] | 610 [M] | +14, +2.35% [D] |
| Total gas | 44 CCF [M] | 29 CCF [M] | −15 CCF, −34.09% [D] |
| Gas cost | $139.82 [M] | $117.59 [M] | −$22.23, −15.90% [D] |
| Gas all-in price | $3.1777/CCF [D] | $4.0548/CCF [D] | [I] fixed charges spread over less gas; falsifier: the bills' customer-charge lines |
| DHW (Navien) | 40.89 CCF [M] | 22.37 CCF [M] | −18.52 CCF, −45.29% [D] |
| Non-DHW gas | 3.11 CCF [D] | 6.63 CCF [D] | mixed basis (advisory 1); furnace off |
| DHW operating / recirculation hours | 24 / 143 [M] | 29 / 46 [M] | recirculation −97 h [D] |
| Furnace runtime | 0 h [M] | 0 h [M] | |
| Electricity | 2,628 kWh [M] | 2,164 kWh [M] | −464 kWh, −17.66% [D] |
| Electric cost | $737.75 [M] | $503.96 [M] | −$233.79, −31.69% [D] |
| Electric all-in rate | $0.2807/kWh [D] | $0.2329/kWh [D] | −17.0% [D: 0.2329 / 0.2807 − 1] |
| Cooling runtime (slot) | 240 h [M] | 212.7 h [M] | −27.3 h [D] |

**Electric cost split.** At the 2025 rate, 2026's 2,164 kWh would have cost $607.49 [D: 2164 × 737.75 / 2628]. Of the $233.79 drop, $130.26 is volume [D: 737.75 − 607.49] and $103.53 is rate [D: 607.49 − 503.96].

### 1.2 By month

| Slot month | CDD 2025 / 2026 | Electricity, kWh | Gas, CCF | DHW, CCF | Cooling runtime, h (slot) |
|---|---|---|---|---|---|
| July | 360 / 285 [M] | 1,129 / 966 [M] | 17 / 13 [M] | 15.03 / 8.39 [M] | 172 / 121.6 [M] |
| August | 170 / 263 [M] | 880 / 724 [M] | 16 / 8 [M] | 10.83 / 5.59 [M] | 62 / 70.3 [M] |
| September | 66 / 62 [M] | 619 / 474 [M] | 11 / 8 [M] | 15.03 / 8.39 [M] | 6 / 20.8 [M] |

Electric slot months are bill windows, not calendar months: the July slot is the bill read 07-14, covering Jun 11–Jul 14. CDD in this table are calendar months. The window CDD are in §1.3. DHW is the calendar-month Navien reading, so the absence (advisory 2) is entirely in the August 2026 DHW figure.

### 1.3 Electricity over identical bill windows

| Window | Days | 2025 kWh | 2026 kWh | 2025 CDD | 2026 CDD | 2025 kWh/day | 2026 kWh/day | Drop, kWh/day |
|---|---|---|---|---|---|---|---|---|
| Jun 11–Jul 14 | 34 | 1,129 [M] | 966 [M] | 339 [D] | 318 [D] | 33.21 [D] | 28.41 [D] | 4.80 [D] |
| Jul 15–Aug 11 | 28 | 880 [M] | 724 [M] | 252 [D] | 246 [D] | 31.43 [D] | 25.86 [D] | 5.57 [D] |
| Aug 12–Sep 10 | 30 | 619 [M] | 474 [M] | 126 [D] | 175 [D] | 20.63 [D] | 15.80 [D] | 4.83 [D] |
| **Q3 bills** | **92** | **2,628** [M] | **2,164** [M] | **717** [D] | **739** [D] | 28.57 [D] | 23.52 [D] | **5.04** [D: 464 / 92] |

**The absence.** The 11 absent days (advisory 2) fall in the second and third windows. To estimate what they would have used, fit SEM whole-home use on CDD over the 81 occupied days of Q3 2026: 14.12 kWh/day + 1.315 kWh/CDD, residual sd 5.61 kWh/day [D]. On that fit, the absence saved 82.7 kWh in the second window and 114.7 kWh in the third [D: fitted − measured SEM on the absent days]. The estimate assumes the absent days would have run like occupied days at the same CDD. Its uncertainty is roughly ±11 and ±15 kWh [D: 5.61 × √4; 5.61 × √7]. It leaves 2025 as measured; the 2025 trip is modelled below the table.

| Window | CDD difference, 2026 − 2025 | Measured drop, kWh/day | 2026 absence adjusted, kWh/day | 2026 absence and 2025 trip adjusted, kWh/day |
|---|---|---|---|---|
| Jun 11–Jul 14 | −21 [D] | 4.80 [D] | 4.80 [D] (no absent days) | 4.80 [D] (no absent days) |
| Jul 15–Aug 11 | −6 [D] | 5.57 [D] | 2.62 [D: (156 − 82.7) / 28] | 2.62–3.39 [I] |
| Aug 12–Sep 10 | +49 [D] | 4.83 [D] | 1.01 [D: (145 − 114.7) / 30] | 4.38–6.09 [I] |
| **Q3 bills** | +22 [D] | **5.04** [D] | **2.90** [D: (464 − 82.7 − 114.7) / 92] | **4.00–4.73** [I: (464 − 197.4 + 101 to 168) / 92] |

**The third window.** Measured, the third window was 49 CDD warmer in 2026 and still used 4.83 kWh/day less, which looked like a base-load change rather than a cooling one. 1.10.0 adjusted it for the 2026 absence alone, found it 1.01 kWh/day lower, and read the adjusted drops as shrinking as 2026 got warmer relative to 2025. The 2025 trip is in that window too. With it adjusted, the three drops are 4.80, 2.62–3.39 and 4.38–6.09 kWh/day [I], in no order by CDD difference, so that reading is withdrawn. With n = 3 windows neither reading has a test, and the data neither show nor exclude a cooling share [D].

**The 2025 trip.** 2025 has no daily electricity data, so the trip's effect can only be modelled. Take the 2026 occupied-day fit above, less the 2026 empty-house mean of 8.37 kWh/day [D: (289.4 − 197.4) / 11, fitted and adjusted totals for the 11 days]. On that model an empty day saves 5.75 kWh + 1.315 kWh per CDD [D: 14.12 − 8.37]. Applied to 8 empty days at each of five placements around Bill's dates (2026-11-22), the trip lowered 2025 use by 101–168 kWh, ±16 kWh for any one placement [I: 5.61 × √8; a 2026 fit applied to 2025 days; falsifier: the utility's daily usage for August 2025, if it still holds it]. Nearly all of it falls in the Aug 12–Sep 10 window, the rest in Jul 15–Aug 11. The model treats all 8 days as wholly empty, so if the first and last days were partly occupied the figures are lower. 1.10.0 placed the trip in September and gave the third window up to 3.38 kWh/day and Q3 up to 3.67. Those figures are superseded.

Bill names two changes: the DHW recirculation (2026-10-15) and the office computer. The computer now shuts down overnight with sleep modes on, a change that began in January 2026 (2026-11-13). Against the adjusted drop, 2.90 kWh/day for the 2026 absence alone and 4.00–4.73 with the 2025 trip as well [I]:

- **Recirculation.** The Navien-and-pump Kasa plug used 24.54 kWh in Jul–Sep 2026 [M], 0.27 kWh/day [D: 24.54 / 92]. For recirculation alone to explain the adjusted drop, that plug would have had to draw 3.17 kWh/day in 2025 [D: 2.90 + 0.27], about 12 times its 2026 draw [D: 3.17 / 0.267], or 4.27–5.00 kWh/day, 16–19 times, with the trip adjusted [I: 4.00 to 4.73 + 0.27]. Recirculation ran 3.1 times as many hours in 2025 [D: 143 / 46], so recirculation is probably a small share [I; falsifier: a 2025 reading of that plug].
- **Office computer.** The computer outlet used 78.02 kWh in Q3 2026 [M], 0.85 kWh/day [D: 78.02 / 92]. Explaining the adjusted drop alone would take 3.75 kWh/day in 2025 [D: 2.90 + 0.85], about 156 W around the clock [D: 3.75 / 24], or 4.85–5.58 kWh/day, 202–233 W, with the trip adjusted [I]. That draw is unmeasured.
- **Timing.** Both changes were in place before May. The nine-month series shows no drop in January–April and a drop from the May 2026 slot onward (§5.2), so neither change explains when the drop began. Bill knows of no other change around April–May 2026 (2026-11-13), so the timing is unexplained (§5.2).

### 1.4 Gas windows

The 2025 Q3 gas bills cover meter reads 06-13 → 09-12: 92 days, 0.4783 CCF/day [D: 44 / 92]. The 2026 bills cover statement dates 06-10 → 09-15: 95 days, 0.3053 CCF/day [D: 29 / 95]. The 09-15 bill's meter read was an actual read on 09-14 (Bill, 2026-11-13).

**The absence** removed an estimated 307–375 ft³ (3.1–3.8 CCF) of 2026 gas [D: 9–11 days × 34.1 ft³/day]. The rate is the SDR mean over the 24 full occupied days of Aug 22–Sep 14 [D]. Nearly all of the removed gas is DHW. On occupied days the Navien used 0.28 CCF/day in both August and September [D: 5.59 / 20; 8.39 / 30], so the absence took about 2.5–3.1 CCF of DHW [D: 9–11 days × 0.28]. With it put back, Q3 2026 DHW would be about 24.9–25.5 CCF [D: 22.37 + 2.5 to 3.1], still far below 2025's 40.89 [M].

**The 2025 trip** falls inside the 2025 Q3 gas bills and inside the calendar-August 2025 DHW reading. August 2025 DHW was 10.83 CCF, against 15.03 in both July and September [M]. At the July–September rate of 0.4928 CCF/day [D: 30.06 / 61], a full August would be 15.28 CCF, so August was about 4.45 CCF short, about 9 days' use [D: 15.28 − 10.83; 4.45 / 0.4928]. That fits near-zero DHW on the trip days, whether or not the heater was off [I; falsifier: the Navien's daily history for August 2025, if it holds one]. Put back for 7–9 days, Q3 2025 DHW would be about 44.3–45.3 CCF [D: 40.89 + 3.45 to 4.44], against 24.9–25.5 for 2026. Both quarters held an absence, so the measured comparison was already close to like-for-like, and the DHW drop is about 19–20 CCF adjusted against 18.52 measured [D]. 2025 gas is understated by at least the same DHW share.

---

## 2. SEM-Meter — July–September 2026 (calendar months)

The SEM-Meter was installed 2026-06-28 [M], so July, August and September are its first three full months. July has 739 of 744 hours [M]. The 5 missing hours fall on Jul 5, in the grid outage, and any use in them is unrecorded. There is no 2025 circuit data.

### 2.1 Circuits

| Circuit | Jul kWh | Aug kWh | Sep kWh | Q3 kWh | Share of whole home |
|---|---|---|---|---|---|
| **Whole home** | 914.02 [M] | 550.74 [M] | 439.10 [M] | **1,903.86** [D] | — |
| AC compressor | 332.78 [M] | 180.87 [M] | 50.62 [M] | 564.27 [D] | 29.6% [D: 564.27 / 1903.86] |
| Air handler (`sem_furnace`) | 123.07 [M] | 82.84 [M] | 38.69 [M] | 244.60 [D] | 12.8% [D: 244.60 / 1903.86] |
| Fridge | 69.60 [M] | 62.27 [M] | 59.26 [M] | 191.13 [D] | 10.0% [D] |
| Bedroom / office | 61.63 [M] | 50.46 [M] | 69.85 [M] | 181.94 [D] | 9.6% [D] |
| Dryer | 51.97 [M] | 38.25 [M] | 62.22 [M] | 152.44 [D] | 8.0% [D] |
| Family room | 25.39 [M] | 19.01 [M] | 24.65 [M] | 69.05 [D] | 3.6% [D] |
| Master suite | 14.52 [M] | 12.33 [M] | 12.76 [M] | 39.61 [D] | 2.1% [D] |
| Counter 1 | 12.38 [M] | 5.36 [M] | 10.82 [M] | 28.55 [D] | 1.5% [D] |
| Counter 2 | 9.35 [M] | 6.46 [M] | 7.74 [M] | 23.56 [D] | 1.2% [D] |
| Dishwasher / disposal | 8.78 [M] | 5.14 [M] | 9.27 [M] | 23.18 [D] | 1.2% [D] |
| Microwave | 5.22 [M] | 3.48 [M] | 7.15 [M] | 15.85 [D] | 0.8% [D] |
| Washer | 3.76 [M] | 3.41 [M] | 5.49 [M] | 12.66 [D] | 0.7% [D] |
| Dining / kitchen lights | 2.85 [M] | 2.35 [M] | 4.11 [M] | 9.31 [D] | 0.5% [D] |
| Laundry / bedroom | 2.31 [M] | 2.40 [M] | 0.87 [M] | 5.58 [D] | 0.3% [D] |
| Garage | 1.31 [M] | 0.71 [M] | 0.93 [M] | 2.94 [D] | 0.2% [D] |
| **Branch-circuit sum** | 724.91 [D] | 475.34 [D] | 364.42 [D] | 1,564.67 [D] | 82.2% [D] |
| **Unmetered remainder** | 189.11 [D] | 75.40 [D] | 74.68 [D] | 339.19 [D] | 17.8% [D] |
| … dehumidifier (Kasa) | 131.93 [M] | 28.22 [M] | 23.96 [M] | 184.11 [D] | 9.7% [D] |
| … Navien + recirculation pump (Kasa) | 7.88 [M] | 8.01 [M] | 8.65 [M] | 24.54 [D] | 1.3% [D] |
| … router (Kasa) | 8.09 [M] | 8.26 [M] | 8.07 [M] | 24.42 [D] | 1.3% [D] |
| … true residual | 41.21 [D] | 30.91 [D] | 34.00 [D] | 106.12 [D] | 5.6% [D] |

The true residual averages 48.2 W [D: 106.12 kWh / 2,203 h]. The computer outlet (78.02 kWh) and the two TV plugs (20.85 and 46.99 kWh) [M] sit on branch circuits, so they are inside the branch sum, not added to it.

**Cooling system.** Compressor plus air handler came to 808.87 kWh [D], 42.5% of the whole home [D: 808.87 / 1903.86]. The air-handler figure includes any fan-only running.

**Compressor per CDD** (from the September report): July 1.168, August 0.688 and September 0.816 kWh/CDD; Q3 **0.925 kWh/CDD** [D: 564.27 / 610]. The draw is 2.725 ± 0.020 kW per hour of thermostat call [D, daily OLS, n = 90 days, R² 0.995].

**Dehumidifier.** It was replaced in August with an Aprilaire E080, and its use fell from 131.93 kWh in July to 28.22 and 23.96 [M]. 2025 dehumidifier use was not metered. Moisture removal therefore differs between the two summers (§4.6).

### 2.2 SEM against the utility meter

| Comparison | SEM kWh | Utility kWh | SEM vs utility |
|---|---|---|---|
| Bill window Jul 15–Aug 11 | 705.2 [M] | 724 (bill) [M] | −2.6% [D: 705.2 / 724 − 1] |
| Bill window Aug 12–Sep 10 | 485.7 [M] | 474 (bill) [M] | +2.5% [D: 485.7 / 474 − 1] |
| September, calendar | 439.10 [M] | 437.31 (SDR) [M] | **+0.41%** [D: 439.10 / 437.31 − 1] |
| September, daily | — | — | +0.39%, sd 0.18, range 0.04 to 0.67%, n = 30 days [D] |
| Sep 11–Oct 8 | 353.7 [M] | 352.4 (SDR) / 362 (bill) [M] | +0.37% vs SDR [D: 353.7 / 352.4 − 1] |

Against the utility meter's own radio, the SEM reads 0.4% high, steadily: the range is under 0.7% on every one of 30 days [D]. Against the bills it is off by ±2.5% with the sign changing. The Sep 11–Oct 8 window separates the two explanations. There the SEM and SDR agree within 1.3 kWh, while the bill differs by 9.6 kWh, less than one day's use (12.6 kWh/day [D: 352.4 / 28]). So the bill-window gaps come from read timing at the window edges, not from the SEM [I; falsifier: utility read timestamps showing reads at midnight].

---

## 3. SDR radio meters — September 2026

The rtlamr2mqtt readings started 2026-08-21. They are hourly deltas of each meter's own counter, so a month total is a counter difference and gaps in decoding within the month do not bias it [D].

| Meter | September 2026 | Daily mean | Daily sd | Daily range | Note |
|---|---|---|---|---|---|
| Electric | 437.31 kWh [M] | 14.58 kWh [D: 437.31 / 30] | — | — | SEM +0.41% [D] |
| Gas | 1,054 ft³ = 10.54 CCF [M] | 35.1 ft³ [D] | 9.8 ft³ [D] | 20–68 ft³ [M] | no zero days in 30 [M] |
| Water | 2,641.1 gal [M] | 88.0 gal [D] | 35.7 gal [D] | 46.4–195.6 gal [M] | first full month; no comparator |

### 3.1 Gas closure on a calendar month

| | CCF |
|---|---|
| SDR gas, September | 10.54 [M] |
| Navien DHW, September (24 m³) | 8.39 [M] (repo conversion) / 8.48 [D: 24 × 35.3147 / 100] |
| **Non-DHW gas** (range, fireplace; furnace 0 h) | **2.15 / 2.06** [D: 10.54 − 8.39; 10.54 − 8.48] |
| Navien whole-m³ quantisation | ±0.18 [D: 0.5 × 35.3147 / 100] |

On the same calendar month, non-DHW gas comes out positive, about **2.1 ± 0.2 CCF** [D]. The −0.39 CCF in the September bill slot is a window artifact, as the September report said. DHW was 80% of September gas [D: 8.39 / 10.54 = 0.796; 8.48 / 10.54 = 0.804].

### 3.2 The September gas bill — resolved

From Aug 21 to Sep 15 the SDR shows 862 ft³ (8.62 CCF) [M, 26 days, Aug 21 partial]. The bill reports 8 CCF for the 34-day slot ending 09-15 [M]. If the 8 unmeasured days had used gas at the usual rate, the slot would hold about 11 CCF [D: 862 + 8 × 34.1 ≈ 1,135 ft³], too much for quantisation to explain. Bill, 2026-11-13: the read was an actual read on Sep 14, and the house was empty with the water heater off for part of the slot (advisory 2). The pieces now fit:

| Part of the slot | ft³ |
|---|---|
| Absent days (water heater off, no cooking, furnace off; Navien plug at standby [M]) | ≈ 0 |
| Return to the SDR's first reading, about 2–3 days, unmeasured | 68–102 [D: × 34.1 ft³/day] |
| SDR Aug 21–Sep 13 / through Sep 14 (time of the read unknown) | 788 / 834 [M] |
| **Estimated slot total** | **856–936** [D] |
| What a bill of 8 CCF can mean | 700–900 [D: two whole-CCF register reads, so true use lies within ±1 CCF of 8; every bill in the repo is whole CCF, n = 21 [M]] |

The two ranges overlap, so the bill closes against the SDR to within about one day's gas [D: 936 − 900 = 36 ft³, against 34.1 ft³/day]. The Q3 2026 gas total stays at the billed 29 CCF.

---

## 4. Air conditioning — Q3 2026 vs Q3 2025

**Sources:** 2025 runtime is daily per-floor Resideo run hours (`2025 Resideo Thermostat Data.xlsx`, sheet "Daily Temp Resideo Data"). 2026 runtime is `hvac_daily_2026.csv`, from HA `binary_sensor.hvac_ac_running` (either zone calling for cooling). The basis matches the June–September season review in `SEPTEMBER_2026_UPDATE.md`, and the method reproduces that review's figures exactly [D].

### 4.1 CDD vs last year

| Period | 2025 CDD | 2026 CDD | Difference |
|---|---|---|---|
| June (context) | 198 [M] | 190 [M] | −8 [D] |
| July | 360 [M] | 285 [M] | −75 [D] |
| August | 170 [M] | 263 [M] | +93 [D] |
| September | 66 [M] | 62 [M] | −4 [D] |
| **Q3** | **596** [M] | **610** [M] | **+14, +2.35%** [D] |
| June–September | 794 [M] | 800 [M] | +6 [D] |
| January–September | 837 [M] | 881 [M] | +44, +5.26% [D] |

**Q3 daily distribution:**

| | Q3 2025 | Q3 2026 |
|---|---|---|
| Days with CDD > 0 | 71 of 92 [D] | 72 of 92 [D] |
| Days ≥ 10 CDD | 28 [D] | 26 [D] |
| Days ≥ 15 CDD | 12 [D] | 9 [D] |
| Highest daily CDD | 19 [D] | 23 [D] |
| Mean CDD per day | 6.48 [D] | 6.63 [D] |
| Days with a high ≥ 90 °F | 15 [M] | 10 [M] |
| Highest daily high | 96 °F [M] | 100 °F [M] |

The two quarters cannot be told apart day by day: Mann-Whitney p = 0.758, Kolmogorov-Smirnov D = 0.120, p = 0.529, n = 92 / 92 [D]. Q3 2025 had more hot days (12 vs 9 at ≥ 15 CDD), and Q3 2026 had the hottest single day (23 CDD, 100 °F). The difference lies in timing: 2025 front-loaded its heat into July, and 2026 spread it over July and August.

### 4.2 Runtime by month

| Month | 2025 runtime | 2025 run days | 2025 min/CDD | 2026 runtime | 2026 run days | 2026 min/CDD |
|---|---|---|---|---|---|---|
| July | 171.20 h [M] | 31 of 31 [M] | 28.5 [D: 171.20 × 60 / 360] | 113.61 h, 29 days [M] | 29 of 29 [M] | 26.6 [D: × 60 / 256] |
| August | 62.07 h [M] | 16 of 31 [M] | 21.9 [D: × 60 / 170] | 70.41 h [M] | 23 of 31 [M] | 16.1 [D: × 60 / 263] |
| September | 5.58 h [M] | 3 of 30 [M] | 5.1 [D: × 60 / 66] | 20.82 h [M] | 16 of 30 [M] | 20.1 [D: × 60 / 62] |
| **Q3** | **238.85 h** [M] | 50 of 92 [M] | **24.05** [D: × 60 / 596] | **204.84 h, 90 days** [M] | 68 of 90 [M] | **21.15** [D: × 60 / 581] |

The 2026 July divisor, 256 CDD, leaves out the 29 CDD of the two missing days [D: 285 − 29]. With the HA accumulator's July (121.6 h), Q3 2026 is 212.83 h over 610 CDD, **20.93 min/CDD** [D: 212.83 × 60 / 610]. First-floor cooling was 1.58 h of the 238.85 in 2025 [M] and 0.0 h in Q3 2026 [M]; the second floor carries the cooling.

Without the 11 absent days, Q3 2026 is 198.51 h over 479 CDD, **24.87 min/CDD** [D: 198.51 × 60 / 479], against 24.05 in 2025. Without the 12-day mid-August 2025 span the 2025 trip could have covered, 2025 is **24.60 min/CDD** [D], and 24.50–25.03 for the five 8-day placements inside it [D]. 1.10.0 dropped 23 September days instead and gave 25.49 (superseded).

**Run days.** The AC ran on 68 of 90 days in 2026 and 50 of 92 in 2025 (Fisher exact p = 0.0032 [D]). Without the absence it ran on 64 of 79 (p = 0.0003 [D]). Without the 2025 trip span as well, 2025 ran on 44 of 80 (p = 0.0006 [D]; 0.0001–0.0013 for the five placements). Of the 42 days in Q3 2025 with no AC, 6 were in that span and 27 in September 2025, when the AC ran on 3 of 30 days (§4.6 item 2) [D]. 1.10.0 dropped 23 September days, which held 20 of the 42, and found no significant difference (p = 0.087); that is superseded. August 2026 includes the absence: on its 20 occupied days the AC ran on 19 [M].

### 4.3 Daily regression: runtime = a + b × CDD

| | Q3 2025, mid-August trip span excluded | Q3 2026, absence excluded | Q3 2025, September span excluded (1.10.0, superseded) | Q3 2025, all days (superseded) | Q3 2026, all days (superseded) |
|---|---|---|---|---|---|
| Days fitted | 80 [D] | 79 [M] | 69 [D] | 92 [M] | 90 [M] |
| Intercept a | −0.121 ± 0.217 h/day [D] | +0.194 ± 0.134 h/day [D] | +0.192 ± 0.336 h/day [D] | −0.094 ± 0.235 h/day [D] | +0.137 ± 0.219 h/day [D] |
| Slope b | 0.4293 ± 0.0254 h/CDD = **25.76 min/CDD** [D] | 0.3825 ± 0.0163 h/CDD = **22.95 min/CDD** [D] | 0.4008 ± 0.0339 h/CDD = 24.05 min/CDD [D] | 0.4152 ± 0.0268 h/CDD = 24.91 min/CDD [D] | 0.3313 ± 0.0260 h/CDD = 19.88 min/CDD [D] |
| R² | 0.785 [D] | 0.877 [D] | 0.676 [D] | 0.727 [D] | 0.649 [D] |
| Lag-1 autocorrelation of residuals | 0.38 [D] | 0.21 [D] | 0.42 [D] | 0.42 [D] | 0.57 [D] |
| CDD range fitted | 0–19 [D] | 0–23 [D] | 0–19 [D] | 0–19 [D] | 0–23 [D] |
| Fitted runtime at 5 / 10 / 15 CDD | 2.03 / 4.17 / 6.32 h [D] | 2.11 / 4.02 / 5.93 h [D] | 2.20 / 4.20 / 6.20 h [D] | 1.98 / 4.06 / 6.13 h [D] | 1.79 / 3.45 / 5.11 h [D] |

The 11 absent days carried 102 CDD and only 6.33 h of runtime [D], so they pulled the all-days slope down. Dropping them raises the 2026 R² from 0.649 to 0.877 and cuts the residual autocorrelation from 0.57 to 0.21 [D]. The residuals are still autocorrelated, so ordinary OLS standard errors are too small, and the tests below use week blocks for that reason. The 2025 trip did the same to 2025 on a smaller scale: dropping the mid-August span moves the 2025 slope from 24.91 to 25.76 min/CDD and its R² from 0.727 to 0.785 [D]. The span is 12 days because the trip's exact days are not known: it covers every day an 8-day trip within 2 days of Bill's dates could have fallen on, so it also drops about 4 occupied days. The five 8-day placements inside it give 2025 slopes of 25.77–26.21 min/CDD [D, n = 84 each].

| Test | Point estimate | 95% CI | p | Method |
|---|---|---|---|---|
| **Slope difference, 2026 − 2025, both absences excluded** | **−2.81 min/CDD** [D] | [−6.30, +0.21] | ≈ 0.063 | week-block bootstrap, blocks anchored Jul 1 (13 in 2025, 13 in 2026), B = 5000, seed 20261113 |
| **Quarter-ratio difference, both excluded** | +0.26 min/CDD [D] | [−4.14, +7.52] | ≈ 0.92 | same bootstrap |
| Pooled model, year × CDD interaction, both excluded | −0.0468 ± 0.0306 h/CDD [D] | — | 0.13 (t = −1.53, dof 155) | OLS, ignores autocorrelation |
| **Slope difference, five 8-day trip placements inside the span** | **−2.83 to −3.26 min/CDD** [D] | — | **0.033–0.062** (4 of 5 below 0.05) | same bootstrap, one run per placement, 13–14 blocks in 2025 |
| Quarter-ratio difference, same placements | −0.17 to +0.36 min/CDD [D] | — | 0.90–0.99 | same bootstrap |
| Pooled interaction, same placements | −0.0471 to −0.0544 h/CDD [D] | — | 0.07–0.12 | OLS |
| Slope difference, September 2025 span excluded (1.10.0, superseded) | −1.10 min/CDD [D] | [−5.36, +3.04] | ≈ 0.54 | same bootstrap, 12 blocks in 2025 |
| Quarter-ratio difference, September span (1.10.0, superseded) | −0.63 min/CDD [D] | [−4.71, +4.53] | ≈ 0.78 | same bootstrap |
| Pooled interaction, September span (1.10.0, superseded) | −0.0183 ± 0.0368 h/CDD [D] | — | 0.62 (t = −0.50, dof 144) | OLS |
| Slope / ratio difference, three 10–12-day September placements (1.10.0, superseded) | −1.37 to −1.96 / −0.28 to +0.44 min/CDD [D] | — | 0.26–0.39 / 0.82–0.97 | same bootstrap |
| Slope difference, 2026 absence only excluded (superseded) | −1.96 min/CDD [D] | [−5.63, +1.10] | ≈ 0.21 | as above, 14 blocks in 2025 |
| Quarter-ratio difference, 2026 absence only excluded (superseded) | +0.82 min/CDD [D] | [−3.43, +7.23] | ≈ 0.73 | same bootstrap |
| Pooled interaction, 2026 absence only excluded (superseded) | −0.0327 ± 0.0334 h/CDD [D] | — | 0.33 (t = −0.98, dof 167) | OLS |
| Slope difference, all days (superseded) | −5.03 min/CDD [D] | [−10.65, −0.34] | ≈ 0.030 | as above, 14 blocks per year |
| Quarter-ratio difference, all days (superseded) | −2.89 min/CDD [D] | [−9.05, +4.48] | ≈ 0.42 | same bootstrap |
| Pooled interaction, all days (superseded) | −0.0839 ± 0.0376 h/CDD [D] | — | 0.027 (t = −2.23, dof 178) | OLS |

**With both absences excluded, the 2026 slope is about 3 min/CDD lower, at the edge of significance in Q3, and the quarter ratio does not differ.** The slope difference has p ≈ 0.063 for the 12-day span and 0.033–0.062 for the five placements [D], so whether it clears 0.05 depends on the trip's exact days, which are not known. The quarter ratio does not differ for any of them (p 0.90–0.99) [D]. Over June–September the slope difference is significant for every exclusion tested (§4.6 item 6). The all-days slope difference (p ≈ 0.030) came from the 11 absent days, when the AC was mostly off at 4–16 CDD.

**Correction (2026-11-22, R13).** 1.10.0 dropped 23 September 2025 days for a trip it placed there on the 2026-11-13 account. It concluded that Q3 2026 and Q3 2025 "cannot be told apart on runtime per CDD", and that "the trip's exact dates do not change this result". The trip was in mid-August (Bill, 2026-11-22). The robustness check varied the trip's days only inside September, so it could not test the month, and the second claim was wider than the check behind it. With September 2025 back in as occupied days, the slope difference is borderline in Q3 and significant over the season. The 1.10.0 rows stay in the tables above, marked superseded.

**Correction (2026-11-13, R13).** An unpublished draft of this report gave the all-days result as the finding: "on the hotter days, Q3 2026 used significantly less runtime per CDD". It stays in the tables above, marked superseded.

Seven Q3 2025 days had no AC at 5 CDD or more [M]; Q3 2026 without the absence has none. One of the seven falls in the mid-August 2025 trip span. Bill names no other absence (2026-11-13, 2026-11-22), so the other six stay in the fits as occupied days. The fits cover 0–23 CDD/day, and no figure here applies outside that range.

### 4.4 Runtime by CDD band

| Daily CDD | 2025 all days (run days) | 2025 all mean h/day | 2025 trip span excluded, days (run days) | 2025 excl. mean h/day | 2026 absence excluded, days (run days) | 2026 excl. mean h/day | 2026 all days (run days) | 2026 all mean h/day |
|---|---|---|---|---|---|---|---|---|
| 0 | 21 (1) [D] | 0.01 [D] | 18 (1) [D] | 0.01 [D] | 20 (6) [D] | 0.11 [D] | 20 (6) [D] | 0.11 [D] |
| 1–4 | 21 (6) [D] | 0.69 [D] | 19 (6) [D] | 0.76 [D] | 15 (14) [D] | 1.53 [D] | 17 (14) [D] | 1.35 [D] |
| 5–9 | 22 (16) [D] | 2.85 [D] | 22 (16) [D] | 2.85 [D] | 25 (25) [D] | 2.75 [D] | 29 (26) [D] | 2.42 [D] |
| 10–14 | 16 (16) [D] | 5.01 [D] | 11 (11) [D] | 4.88 [D] | 12 (12) [D] | 4.44 [D] | 16 (14) [D] | 3.57 [D] |
| ≥ 15 | 12 (11) [D] | 6.79 [D] | 10 (10) [D] | 7.45 [D] | 7 (7) [D] | 7.33 [D] | 8 (8) [D] | 6.55 [D] |

The comparison uses the excluded columns of both years; the 2025 span is the 12-day mid-August span. On mild days the 2026 system ran far more often. On 1–4 CDD days it ran on 14 of 15 days, against 6 of 19 in 2025 (Fisher exact p = 0.0004 [D]; 0.0003–0.0004 for the five placements). On 0 CDD days it ran on 6 of 20 against 1 of 18 (p = 0.09 [D]). On 5–9 CDD days it ran on all 25, against 16 of 22 (p = 0.007 [D]). From 10 CDD up, both years ran on every day (19 of 19 against 21 of 21, p = 1.0 [D]). Hours per day now have a direction: 2026 was lower in all three bands from 5 CDD up (2.75 against 2.85, 4.44 against 4.88, 7.33 against 7.45 h/day) and higher at 0 and 1–4 CDD [D]. That is the lower slope of §4.3 seen band by band. The band differences in hours are small and untested.

These band tests were chosen after the bands were drawn, so treat them as descriptive. The 1–4 CDD result survives a Bonferroni correction for the five bands [D: 0.0004 × 5 = 0.002], and so does the 5–9 CDD result [D: 0.007 × 5 = 0.035]. The all-days columns (p = 0.0013 at 1–4 CDD) are kept for comparison with the unpublished draft. 1.10.0 used a September span instead: 9 (0), 14 (6), 18 (14), 16 (16) and 12 (11) days (run days) by band, giving p = 0.0052 at 1–4 CDD, 0.14 at 0 CDD and 0.025 at 5–9 CDD (superseded).

### 4.5 2026 cycles and compressor energy

| Month | Cycles | Min per cycle | Cycles per day |
|---|---|---|---|
| July (29 days) | 236 [M] | 28.9 [D: 113.61 × 60 / 236] | 8.14 [D] |
| August | 173 [M] | 24.4 [D: 70.41 × 60 / 173] | 5.58 [D] |
| September | 68 [M] | 18.4 [D: 20.82 × 60 / 68] | 2.27 [D] |
| **Q3 (90 days)** | **477** [M] | 25.8 [D: 204.84 × 60 / 477] | 5.30 [D] |

August and the Q3 row include the 11-day absence, when the AC ran 12 cycles in total [D: 173 − 161], most of them on the two partial days. Without the absence, August is 161 cycles over 20 days, 8.05 per day and 23.9 min per cycle [D]. Q3 is 465 cycles over 79 days, 5.89 per day and 25.6 min per cycle [D: 465 / 79; 198.51 × 60 / 465].

There are no 2025 cycle counts (Bill, 2026-10-15: no such data exists), so there is no comparison.

**Compressor energy, Q3 2026:** 564.27 kWh, 0.925 kWh/CDD [D: 564.27 / 610] (§2.1). Both figures include the absence days. **2025 was not metered.** A 2025 figure can only be built as runtime × an assumed draw, which is runtime per CDD again in other units. At the 2026 draw of 2.725 kW, Q3 2025 would be 650.9 kWh, 1.09 kWh/CDD [I: 238.85 × 2.725; / 596; falsifier: any measured 2025 draw that differs from 2026's]. The conflict between 2.725 kW and the 4.9 kW in `SYSTEM_SPECIFICATIONS.md` is still open (September report §Compressor draw).

### 4.6 Confounds and limits (R11)

1. **One summer per controller.** Year and thermostat are fully confounded, with n = 1 summer each.
2. **Settings.** Bill, 2026-10-15: the 2F setpoints and schedules were the same in both summers, cooling was not switched off in September 2025, and all vents were 100% open in summer. That removes those as confounds. It does not make the comparison a controlled one. With no trip in it, September 2025 is unexplained again: the AC ran on 3 of 30 days (5.58 h at 66 CDD), against 16 of 30 in September 2026 (20.82 h at 62 CDD) [M]. 1.10.0 put that gap down to the trip.
3. **Ecobee minimum compressor runtime** was raised from 10 to 15 min on 2026-06-07 (`JUNE_2026_UPDATE.md`). That affects cycle length and mild-day runtime, which is where 2026 ran more.
4. **Weather beyond CDD.** BDL is an airport station, not the site, and CDD65 does not capture humidity (latent load), solar gain or wind. The linear fits leave 21% (2025, trip span excluded) and 12% (2026, absence excluded) of daily variance unexplained [D: 1 − 0.785; 1 − 0.877].
5. **Moisture removal changed.** The dehumidifier was replaced in August 2026, and its 2025 operation was not metered (§2.1).
6. **Not independent of the season review, and hit by the same absences.** Q3 is 182 of the 242 days in the June–September review [D: 92 + 90 of 122 + 120], and both absences fall in both. Excluding both, the Q3 slope difference is −2.81 min/CDD (p ≈ 0.063) and the season difference is −4.32 [−7.69, −1.13] (p ≈ 0.006) [D: same bootstrap, blocks anchored Jun 1, seed 20261015; 2025 n = 110 days at 26.69 min/CDD, 2026 n = 109 at 22.37]. For the five trip placements the season difference is −4.35 to −4.54 (p 0.003–0.004) [D]. The season ratio does not differ: −0.75 (p ≈ 0.71), and −0.68 to −0.96 for the placements (p 0.61–0.75) [D]. The pooled interaction is −0.0720 ± 0.0266 h/CDD (t = −2.70, dof 215 [D, OLS, autocorrelation ignored]). On 1–4 CDD days 2026 ran on 20 of 22 days against 12 of 27 (Fisher exact p = 0.0008 [D]). 1.10.0, with the September span, gave −2.99 (p ≈ 0.12), and −3.14 to −3.55 (p 0.075–0.097) for its placements; those are superseded. Excluding the 2026 absence alone, it was −3.59 (p ≈ 0.052). The Q3 and season tests are not independent, so the second does not confirm the first.
7. **Occupancy.** A day with nobody home is not comparable to an occupied day. This report drops the 2026 absence, which the circuit meters show, and the span the 2025 trip could have covered, from Bill's account (2026-11-13, corrected 2026-11-22). 2025 has no circuit-level metering, so the trip's days cannot be read from the data, and the AC exclusion is wider than the trip. 1.10.0's exclusion was in the wrong month.
8. **Not established:** that the Ecobee saves energy over a season; any 2025 cycle behaviour; any 2025 compressor energy.

---

## 5. Nine-month summary — January–September 2026 vs 2025

### 5.1 Totals and paired tests

The paired tests compare slot months, n = 9 pairs, two-sided.

| Metric | Jan–Sep 2025 | Jan–Sep 2026 | Change | Paired monthly test (n = 9) |
|---|---|---|---|---|
| HDD65 (BDL) | 3,429 [M] | 3,869 [M] | +440, +12.83% [D] | — |
| CDD65 (BDL) | 837 [M] | 881 [M] | +44, +5.26% [D] | — |
| Total gas | 601 CCF [M] | 598 CCF [M] | −3 CCF, −0.50% [D] | mean −0.33 CCF/month, t = −0.09, p = 0.93; Wilcoxon p = 0.82 |
| Gas cost | $1,091.50 [M] | $1,096.28 [M] | +$4.78, +0.44% [D] | t = 0.12, p = 0.91 |
| Gas all-in price | $1.8161/CCF [D] | $1.8332/CCF [D] | | |
| DHW (Navien) | 156.63 CCF [M] | 101.01 CCF [M] | −55.62 CCF, −35.51% [D] | mean −6.18 CCF/month, t = −6.74, p = 0.0001; Wilcoxon p = 0.0039; lower in 9 of 9 |
| Space heat (gas − DHW) | 444.38 CCF [D] | 496.99 CCF [D] | +52.61 CCF, +11.84% [D] | — |
| Electricity | 5,284 kWh [M] | 4,558 kWh [M] | −726 kWh, −13.74% [D] | mean −80.7 kWh/month, t = −2.72, p = 0.026; Wilcoxon p = 0.055 |
| Electricity, 2026 absence adjusted | 5,284 kWh [M] | 4,755.4 kWh [D: 4,558 + 197.4] | −528.7 kWh [D] | mean −58.7 kWh/month, t = −2.19, p = 0.060; Wilcoxon p = 0.098 [D] |
| Electricity, 2026 absence and 2025 trip adjusted | 5,385–5,452 kWh [I: 5,284 + 101 to 168] | 4,755.4 kWh [D] | −630 to −697 kWh [I] | mean −70.0 to −77.4 kWh/month, t = −2.53 to −2.62, p = 0.031–0.035; Wilcoxon p = 0.055 [I] |
| Electric cost | $1,552.44 [M] | $1,137.71 [M] | −$414.73, −26.71% [D] | mean −$46.08/month, t = −3.98, p = 0.0041; Wilcoxon p = 0.0078 |
| Electric all-in rate | $0.2938/kWh [D] | $0.2496/kWh [D] | | |
| Heating runtime | 489 h [M] | 521.8 h [M] | +32.8 h, +6.71% [D] | basis change in May (below) |
| Cooling runtime (slot) | 340 h [M] | 317.9 h [M] | −22.1 h [D] | — |
| DHW operating hours | 83 [M] | 97 [M] | +14 [D] | — |
| DHW recirculation hours | 487 [M] | 275 [M] | −212 h, −43.53% [D] | — |

**Gas.** Total gas held level on 12.83% more HDD [D]. The DHW saving (−55.62 CCF) offset nearly all of the extra space heating (+52.61 CCF) [D]. Heating efficiency did not change:

- Jan–May space-heat intensity was 129.67 CCF per 1,000 HDD in 2025 and 128.93 in 2026 [D: 434.40 / 3.350; 484.89 / 3.761]. Paired monthly t = −0.57, p = 0.60 (n = 5).
- Regressing monthly space heat on HDD through the origin gives 129.98 CCF per 1,000 HDD, with a 2026 difference of +0.24 ± 7.71 (t = 0.03, p = 0.976, n = 10 months, df 8) [D].
- Total gas per 1,000 HDD over Jan–May was 159.40 in 2025 and 146.77 in 2026 [D: 534 / 3.350; 552 / 3.761]. Of the 12.63 difference, 11.89 is DHW and 0.74 is space heat [D: (99.61 / 3.350 − 67.11 / 3.761); 129.67 − 128.93].

**Heating runtime.** Runtime per HDD over Jan–May was 8.758 min in 2025 and 8.324 in 2026 [D]. May 2026 runtime (Resideo, overlap-inclusive) and May 2025 runtime (burner hours) are on different bases (H1 overview §6), so this figure is weaker than the gas intensity.

**Gas, absence-adjusted.** The August 2026 absence removed about 3.1–3.8 CCF (§1.4). Put back, nine-month 2026 gas is about 601–602 CCF against 601 [D: 598 + 3.1 to 3.8]. The mid-August 2025 trip lowered 2025 gas by at least its DHW share, about 3.5–4.4 CCF (§1.4), so with both put back it is about 601–602 against 604–605 [I]. Neither changes the conclusion.

**DHW.** It was lower in every month. The winter vacation fell in a different month each year (H1 overview), so those two monthly pairs are distorted in opposite directions. The nine-month total is not affected, because the trip falls inside the window in both years. The August 2026 absence lowered August 2026 DHW by about 2.5–3.1 CCF (§1.4), so with only that put back the nine-month DHW drop is about 52.5–53.1 CCF rather than 55.62 [D: 55.62 − 3.1 to 2.5]. The mid-August 2025 trip lowered August 2025 DHW by about 3.5–4.4 CCF (§1.4). With both put back the drop is about 56.0–57.6 CCF [I: 55.62 − 3.1 to 2.5 + 3.45 to 4.44]. DHW is lower in 9 of 9 months either way: August 2026 with the absence put back is at most 8.69 CCF, against 10.83 measured for August 2025 [D: 5.59 + 3.1]. The measured 55.62 compares two years that each include a summer trip, so it is close to like-for-like.

**Electricity, absence-adjusted.** The 2026 absence lowered the August and September 2026 slots by about 197.4 kWh (§1.3). Adjusted for it alone, the nine-month drop is 528.7 kWh, t = −2.19, p = 0.060, n = 9 [D]. The mid-August 2025 trip lowered the 2025 September slot (Aug 12–Sep 10), and at the earliest placement the August slot by one day, by 101–168 kWh in all [I, §1.3]. Adjusted for both, the drop is 630–697 kWh: mean −70.0 to −77.4 kWh/month, t = −2.53 to −2.62, p = 0.031–0.035, Wilcoxon p = 0.055 [I: the paired test re-run with the slot differences adjusted at each of the five placements]. On the t-test that is significant at 0.05 for every placement. It rests on a 2026 model applied to 2025 days (falsifier in §1.3). 1.10.0 gave 528.7 kWh as a lower bound, up to about 599.7 kWh, and ran no test for it; that is superseded.

### 5.2 When the electricity drop began

| Slot month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep |
|---|---|---|---|---|---|---|---|---|---|
| 2026 − 2025, kWh | +54 [D] | −43 [D] | +60 [D] | −59 [D] | −153 [D] | −121 [D] | −163 [D] | −156 [D] | −145 [D] |
| 2026 absence adjusted, kWh | +54 [D] | −43 [D] | +60 [D] | −59 [D] | −153 [D] | −121 [D] | −163 [D] | −73.3 [D] | −30.3 [D] |
| 2026 absence and 2025 trip adjusted, kWh | +54 [D] | −43 [D] | +60 [D] | −59 [D] | −153 [D] | −121 [D] | −163 [D] | −73.3 to −94.8 [I] | −131.5 to −182.8 [I] |

The January–April differences average +3.0 kWh/month [D: 12 / 4]. The May–September differences average −147.6 as measured and −108.1 with the 2026 absence adjusted [D: −738 / 5; −540.6 / 5], about 3.6 kWh/day [D: 108.1 / 30.4]. With the 2025 trip adjusted as well they average −128.4 to −141.8, about 4.2–4.7 kWh/day [I: / 30.4]. The split was chosen after looking at the series, so no p-value is given for it. The May 2026 slot is mostly April use and had more cooling than May 2025 (20.2 h against 1.0 h [M]), so the drop there is not reduced cooling.

Neither of the two changes Bill has named explains the timing. The office computer's overnight shutdown and sleep modes began in January 2026 (Bill, 2026-11-13). DHW recirculation hours were already lower in January–May (290 → 199 h [M]). Yet electricity in January–April was not lower. Both changes were in place months before the drop began. An earlier draft of this section inferred that something else changed around April–May 2026, or ran in summer 2025 and not in summer 2026 [I], and named as its falsifier that Bill would know of no such change. Bill knows of none (2026-11-13), so that inference is withdrawn. **The timing of the drop is unexplained.** Of the loads that run mainly in summer, the dehumidifier and the compressor have no 2025 metering (§2.1, §4.5), so the data cannot test them.

---

## 6. Data notes

- **`data/daily_temperature.csv` HDD65 column.** It sums unrounded (mean − 65) and so does not match ACIS: January 2025 1,134.5 vs 1,125; January 2026 1,270.0 vs 1,263; September 2026 88.0 vs 85 [M]. This report rounds each daily mean half-up first, which matches ACIS in all 21 months [D]. The column is unchanged, because a correction needs Bill's approval.
- **H1 overview.** Its DHW (120.0 → 79.3 CCF) and space-heat (437 → 483 CCF) figures predate the 2026-10-15 therms-to-CCF correction. The corrected H1 values are in advisory 6, and the nine-month figures here supersede them.
- **Navien model.** The owner's equipment record gives NPE-240A2 (2026-10-21). Seven monthly reports, March–September, name NPE-240S2. That is left for a separate change.
- **September 2026 gas bill window:** resolved (§3.2). The read was actual, on 09-14, and the absence explains the low bill.
- **Correction (2026-11-13, R13).** An unpublished draft of this report, written before Bill reported the August absence, gave the Q3 AC slope difference as −5.03 min/CDD (p ≈ 0.030). It also read the Q3 electricity drop, 5.04 kWh/day, as base load. Both included the 11 absent days. The corrected figures are in §1.3 and §4.3. The published season review (`SEPTEMBER_2026_UPDATE.md`) and the README's key insights 1 and 2 carry the same exposure, and each now has a dated correction note at the site.
- **Correction (2026-11-22, R13).** 1.10.0 placed the 2025 trip in September, on the 2026-11-13 account. Bill has since corrected it to mid-August (2026-11-22). That supersedes the 23-day September AC exclusion and every Q3 and season result built on it (§4.2–§4.4, §4.6 items 6 and 7). It also supersedes the claim that the AC results do not depend on the trip's dates, the electricity figures given as lower bounds with an upper value for a September trip (§1.3, §5.1, §5.2), and the open question on the trip's dates. The 1.10.0 values stay in the tables, marked superseded. The 2026-11-13 correction notes in `SEPTEMBER_2026_UPDATE.md`, the README and `UPDATES.md` relied on the September dates too, and each now has a 2026-11-22 note at the site.

---

## 7. Open Questions

These are physical or occupancy facts. They come from Bill, not from inference (R14).

**Answered (Bill, 2026-11-13):**

- **September 2026 gas bill:** the meter read was actual, on 09-14. The household was away for about two weeks in that bill slot, with DHW off, no heat and no cooking. The data show 11 absent days in mid-August (advisory 2). This closes §3.2 and changes §1.3 and §4.3.
- **Office computer:** the overnight shutdown and sleep modes began in January 2026 (§5.2).
- **2025 occupancy:** the household was away for 10–12 days in September 2025. The 2025 AC fits drop every day that trip could have covered (§4.3), and the AC results do not depend on its exact dates. *Corrected 2026-11-22 (Bill): the September dates were wrong. The trip was in mid-August 2025 (below), and the second sentence is withdrawn (§4.3).*
- **April–May 2026:** Bill knows of no change then, and of nothing that ran in summer 2025 but not in summer 2026. The timing of the electricity drop is unexplained (§5.2).

**Answered (Bill, 2026-11-22):**

- **Dates of the 2025 trip, and was the water heater off?** (1.10.0 Open Question 1.) Mid-August 2025, about 8 days. Bill does not know the exact days, or whether the water heater was off. The AC fits drop a 12-day span and test five 8-day placements inside it (§4.3), and the electricity model uses the same placements (§1.3). August 2025 DHW fits near-zero use on the trip days either way (§1.4). The days are used for the arithmetic only and are not published.

**Open:** none.

---

*Sources: `data/monthly_summary.csv`, `data/daily_temperature.csv` (BDL daily); ACIS BDL monthly HDD65/CDD65 (StnData, sid BDL); `hvac_daily_2026.csv` (HA, daily AC runtime and cycles); `2025 Resideo Thermostat Data.xlsx` (sheet "Daily Temp Resideo Data"); `energy_daily_master.csv` (SEM-Meter circuits, Kasa plugs, rtlamr2mqtt SDR gas, water and electric); `SEPTEMBER_2026_UPDATE.md` (season review, compressor draw, confounds); `H1_2026_vs_2025_OVERVIEW.md` (vacation months, May runtime basis); Bill (2026-10-15, 2026-11-13: settings, September read, both absences, computer, no April–May change; 2026-11-22: the 2025 trip's month). Bootstrap: week blocks anchored on the first day of the window, B = 5000, seed 20261113 (season review: seed 20261015).*
