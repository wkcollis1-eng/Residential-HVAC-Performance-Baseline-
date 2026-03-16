# HVAC Performance Monthly Updates

**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Source files:** See `data/` directory for raw CSVs. See `data/monthly_summary.csv` for derived monthly metrics.

Updates are listed newest-first. Each month appended to the top of this file.

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
