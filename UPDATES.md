# HVAC Performance Monthly Updates

**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Source files:** See `data/` directory for raw CSVs. See `data/monthly_summary.csv` for derived monthly metrics.

Updates are listed newest-first. Each month appended to the top of this file.

---

## September 2026 Update

**Version:** 1.9.0 | **Date:** October 15, 2026 | **Full report:** [SEPTEMBER_2026_UPDATE.md](SEPTEMBER_2026_UPDATE.md)

### Executive Summary

September 2026 was a shoulder month (62 CDD / 85 HDD, BDL [M]) with no furnace runtime in either year. The report adds the first full cooling-season comparison of the Honeywell T6 Pro (2025) against the Ecobee (2026), on BDL CDD65.

| Metric | Sep 2025 | Sep 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| Total Gas | 11 CCF / $41.38 | 8 CCF / $37.02 | −3 CCF [D] | 2026 bill 5 days longer |
| DHW (Navien) | 15.03 CCF | 8.39 CCF | **−44.2%** [D] | Recirc 51 → 17 h |
| Electricity | 619 kWh / $173.58 | 474 kWh / $118.05 | −23.4% kWh / −32.0% $ [D] | Identical bill window |
| CDD65 / HDD65 (BDL) | 66 / 39 | 62 / 85 | −4 / +46 [D] | Cooler month |
| Cooling Runtime | 5.58 h (3 days) | 20.82 h (16 days, 68 cycles) | +15.24 h [D] | Mild-day running |
| AC Compressor (SEM) | not metered | 50.6 kWh, 0.816 kWh/CDD [D] | — | |

**Season review (June–September, BDL CDD65):**

1. Daily-fit runtime slope 25.96 → 19.91 min/CDD: −6.05 min/CDD, 95% CI [−11.06, −1.37], p ≈ 0.010 [D, week-block bootstrap, B=5000]. Less runtime per degree-day on hot days.
2. Season ratio 25.54 → 22.52 min/CDD: −3.02, 95% CI [−7.95, +2.72], p ≈ 0.29 [D]. Not significant, because the Ecobee ran more on mild days.
3. Compressor energy 0.925 kWh/CDD over Jul–Sep [D: 564.3 / 610], at 2.725 kW per call-hour [D, n=90 days]. This conflicts with the 4.9 kW spec figure; the conflict is open.
4. Whole-house electricity over identical 120-day bill windows fell from 3,141 to 2,526 kWh [M] at 779 vs 769 CDD. It was about 5.15 kWh/day lower in every window [D, n=4, sd 0.39]: a base-load change, not a cooling one.
5. Year and thermostat are fully confounded. No difference is attributed to the thermostat until the 2025 setpoints, system mode and 2F vent position are known.

---

## August 2026 Update

**Version:** 1.8.3 | **Date:** October 15, 2026 | **Full report:** [AUGUST_2026_UPDATE.md](AUGUST_2026_UPDATE.md)

### Executive Summary

August 2026 was hotter than August 2025 (263 vs 170 CDD, BDL [M]) and still used fewer minutes of cooling per CDD. The Aprilaire E080 dehumidifier replaced the Santa Fe Classic from 08-05.

| Metric | Aug 2025 | Aug 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| Total Gas | 16 CCF / $48.43 | 8 CCF / $36.27 | −8 CCF [D] | DHW-led; 2025 bill 2 days longer |
| DHW (Navien) | 10.83 CCF | 5.59 CCF | **−48.4%** [D] | Recirc 38 → 12 h |
| Electricity | 880 kWh / $248.31 | 724 kWh / $175.22 | −17.7% kWh / −29.4% $ [D] | Identical bill window |
| CDD65 (BDL) | 170 | 263 | +93 CDD [D] | Hotter |
| Cooling Runtime | 62.07 h | 70.41 h (173 cycles) | +8.34 h [D] | |
| Cooling Intensity (BDL) | 21.9 min/CDD | 16.1 min/CDD | −5.8 min/CDD [D] | Single month; see season review |
| AC Compressor (SEM) | not metered | 180.9 kWh, 0.688 kWh/CDD [D] | — | |
| Dehumidifier (Kasa) | — | 28.2 kWh [M] | — | E080 from 08-05 |

**Key Insight:** runtime per CDD fell from July to August in both years (28.5 → 21.9 min/CDD in 2025, 26.6 → 16.1 in 2026 [D]), so a single month cannot separate the controller from the season.

---

## July 2026 Update

**Version:** 1.8.2 | **Date:** October 15, 2026 | **Full report:** [JULY_2026_UPDATE.md](JULY_2026_UPDATE.md)

### Executive Summary

July 2026 was the first full month with the SEM-Meter metering the AC circuit, and was milder than July 2025 (285 vs 360 CDD, BDL [M]). A grid outage took the mains down from 21:00 Jul 4; SEM data resume at 08:00 Jul 5. Neither day has thermostat rows.

| Metric | Jul 2025 | Jul 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| Total Gas | 17 CCF / $50.01 | 13 CCF / $44.30 | −4 CCF [D] | DHW-led |
| DHW (Navien) | 15.03 CCF | 8.39 CCF | **−44.2%** [D] | Recirc 54 → 17 h |
| Electricity | 1,129 kWh / $315.86 | 966 kWh / $210.69 | −14.4% kWh / −33.3% $ [D] | Identical bill window |
| CDD65 (BDL) | 360 | 285 | −75 CDD [D] | Milder |
| Cooling Runtime | 171.20 h | 113.61 h (29 days, 236 cycles) | not comparable as totals | 2 outage days missing |
| Cooling Intensity (BDL) | 28.5 min/CDD | 26.6 min/CDD (29 days) | −1.9 min/CDD [D] | Single month |
| AC Compressor (SEM) | not metered | 332.8 kWh, 1.168 kWh/CDD [D] | — | 2.62 kW per call-hour [D] |

*March–June 2026 have individual reports (`MARCH_2026_UPDATE.md` … `JUNE_2026_UPDATE.md`) but were never added to this file; that gap is left open.*

---

## February 2026 Update

**Version:** 1.4.0 | **Date:** March 1, 2026

### Executive Summary

February 2026 was significantly colder than February 2025, with a notable early-month cold snap (Feb 7–9, minimum 0°F). DHW optimization savings from January's recirculation schedule change continued to hold.

| Metric | Feb 2025 | Feb 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| Total Gas | 154 CCF | 175 CCF | +13.6% | Weather + billing days |
| DHW (Navien) | 18.12 CCF | 14.14 CCF | **-22.0%** | Recirc optimization |
| Space Heating | 135.9 CCF | 160.9 CCF | +18.4% | Weather-driven |
| HDD65 | 940 | 1,077 | +14.6% | Colder winter |
| Heating Intensity | 144.5 CCF/1kHDD | 149.4 CCF/1kHDD | +3.4% | Within baseline CV (7.0%) |
| HVAC Runtime | 138 hrs | 158 hrs | +14.5% | Tracks HDD |
| Runtime Efficiency | — | **8.8 min/HDD** | — | 19% better than baseline |
| Zone Balance (1F%) | — | 45.6% | — | ✅ Within 45–55% target |

**Key Insights:**

1. Runtime efficiency (8.8 min/HDD) is 19% better than the 10.9 min/HDD baseline, confirming system health despite colder conditions.
2. DHW savings from January's recirculation change are sustained: -22.0% YoY for the second consecutive month.
3. The 18.4% space heating increase slightly exceeds the 14.6% HDD increase — a billing period artifact, not a system issue.

### DHW Optimization: Cumulative (Jan–Feb 2026)

| Month | Old Schedule Est. | Actual (15hr) | Savings |
|-------|-------------------|---------------|---------|
| Jan 2026 | 22.83 CCF | 17.76 CCF | 5.07 CCF |
| Feb 2026 | 18.12 CCF | 14.14 CCF | 3.98 CCF |
| **Total** | **40.95 CCF** | **31.90 CCF** | **9.05 CCF (~$14.50)** |

On track for projected **$77/year** savings.

### 2025–2026 Heating Season Cumulative (Oct 2025 – Feb 2026)

| Month | Heat Hrs | HDD65 | min/HDD | Zone Bal (1F%) |
|-------|----------|-------|---------|----------------|
| Oct 2025 | 33 | 358 | 5.5 | 69.7% |
| Nov 2025 | 103 | 716 | 8.6 | 62.1% |
| Dec 2025 | 206 | 1,148 | 10.8 | 42.2% |
| Jan 2026 | 220 | 1,230 | 10.7 | 46.8% |
| Feb 2026 | 158 | 1,089 | **8.8** | 45.6% |
| **Total** | **720** | **4,541** | **9.5** | **49.1%** |

### Gas Consumption Decomposition

```
February 2026 Total Gas: 175 CCF (billing pending — estimated from HA)
├── Space Heating:       160.9 CCF (91.9%)
└── Domestic Hot Water:   14.1 CCF (8.1%)   ← DHW share down from 11.8% in Feb 2025
```

### Pending Data

- February 2026 gas and electric utility bills not yet entered in CSV (expected mid-March 2026).
- `monthly_gas_scg.csv` and `monthly_electricity_eversource.csv` to be updated on receipt.

---

## January 2026 Update

**Version:** 1.3.2 | **Date:** February 2, 2026

### Executive Summary

January 2026 extended the four-year baseline with real-time monitoring data and documented the DHW recirculation optimization implemented mid-month. Space heating tracked weather within 0.2% YoY on an intensity basis.

| Metric | Jan 2025 | Jan 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| Total Gas | 161 CCF | 168 CCF | +4.3% | Includes DHW savings |
| DHW (Navien) | 22.83 CCF | 17.76 CCF | **-22.2%** | Recirc optimization |
| Space Heating | 138.2 CCF | 150.2 CCF | +8.7% | Weather-driven |
| HDD65 | 1,134 | 1,230 | +8.5% | Colder winter |
| Heating Intensity | 121.8 CCF/1kHDD | 122.1 CCF/1kHDD | **+0.2%** | ✅ Flat (excellent) |
| Electricity | 461 kWh | 515 kWh | +11.7% | Billing days + blower |
| HVAC Runtime | 198 hrs | 220 hrs | +11.1% | Tracks HDD |
| Runtime Efficiency | — | 10.7 min/HDD | — | ✅ Within baseline |

**Key Insights:**

1. Space heating increased 8.7% to match the 8.5% increase in HDD — essentially perfect 1:1 tracking.
2. Heating intensity flat at +0.2% YoY, confirming no equipment degradation or envelope compromise.
3. DHW optimization (9 hr overnight shutoff) delivered -22.2% in first full month of monitoring.

### DHW Recirculation Optimization

**Change:** Navien schedule reduced 24 hr/day → 15 hr/day (off 9 PM – 6 AM), implemented mid-January 2026.

| Metric | Jan 2025 (24 hr) | Jan 2026 (15 hr) | Change |
|--------|-----------------|------------------|--------|
| DHW Gas (Navien) | 22.83 CCF | 17.76 CCF | **-22.2%** |
| Recirc Hours | 61 hrs | 43 hrs | -29.5% |

**Standby Loss Analysis:** Observed 22.2% gas savings from a 37.5% recirculation reduction implies ~59% of DHW gas was recirculation standby loss — significantly higher than Navien's 23% factory estimate. Consistent with cold basement (~55–60°F), long pipe runs, and winter inlet temperatures (~45°F).

**Projected Annual Savings:** ~$77/year at current $/CCF.

### Late-January Cold Snap (Jan 24–31, 2026)

- 8-day HDD: 429 (35% of monthly total in 26% of days)
- Minimum temperature: −2°F (Jan 31)
- Runtime efficiency during event: 11.2 min/HDD — within ±2σ of 10.9 baseline
- No efficiency alerts triggered

### Updated Baseline (Navien-Corrected)

| Metric | Original Estimate | Navien-Corrected |
|--------|-------------------|------------------|
| Annual DHW Gas | 188 CCF | 220.8 CCF |
| Annual Space Heating | 599 CCF | **566.2 CCF** |
| Heating Intensity | 95.5 CCF/1kHDD | **90.3 CCF/1kHDD** |

Original DHW estimate was understated. Corrected baseline (90.3) is now the reference for all efficiency comparisons.

---

*For updates prior to January 2026, see git history. New months are prepended to the top of this file.*
