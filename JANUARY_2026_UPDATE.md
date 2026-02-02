# HVAC Performance Update: January 2026

**Version:** 1.3.0  
**Date:** February 2, 2026  
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut

---

## Executive Summary

This update extends the four-year baseline (2022-2025) with January 2026 data, incorporating the real-time monitoring system implemented in early January. The analysis validates baseline performance under extreme cold conditions and documents a successful DHW optimization.

**Key January 2026 Findings:**
- **Total Gas Consumption:** 168 CCF (+4.3% YoY)
- **Weather Severity:** 1,230 HDD65 (+8.5% YoY — significantly colder)
- **Space Heating:** 150.2 CCF (+8.7% YoY — tracks weather perfectly)
- **Heating Intensity:** 122.1 CCF/1kHDD (+0.2% YoY — essentially flat)
- **DHW Optimization:** -22.2% from recirculation schedule change
- **HVAC Runtime:** 220 hours at 10.7 min/HDD (within baseline)

**Interpretation:** Space heating consumption increased 8.7% to match the 8.5% increase in weather severity — essentially perfect 1:1 tracking. The heating intensity is flat YoY (+0.2%), confirming system integrity and validating the 4-year baseline methodology.

---

## Table of Contents

1. [DHW Recirculation Optimization](#dhw-recirculation-optimization)
2. [Corrected Year-over-Year Analysis](#corrected-year-over-year-analysis)
3. [Month-over-Month Analysis](#month-over-month-analysis)
4. [13-Month Rolling Comparison](#13-month-rolling-comparison)
5. [January Cold Snap Analysis](#january-cold-snap-analysis)
6. [HVAC Runtime Performance](#hvac-runtime-performance)
7. [Updated Baseline Metrics](#updated-baseline-metrics)
8. [Recommendations](#recommendations)

---

## DHW Recirculation Optimization

### Change Implemented

**Date:** Mid-January 2026  
**Change:** Navien recirculation schedule reduced from 24 hr/day to 15 hr/day  
**Schedule:** OFF between 9:00 PM and 6:00 AM

### Measured Impact

| Metric | Jan 2025 (24hr) | Jan 2026 (15hr) | Change |
|--------|-----------------|-----------------|--------|
| DHW Gas (Navien) | 22.83 CCF | 17.76 CCF | **-22.2%** |
| Recirc Hours | 61 hrs | 43 hrs | **-29.5%** |
| Daily DHW Rate | 0.74 CCF/day | 0.57 CCF/day | **-23.0%** |

### Implied Standby Loss Analysis

The relationship between recirculation reduction and gas savings reveals the true standby loss fraction:

```
Recirculation time reduction: 37.5% (9 hrs off / 24 hrs)
DHW gas reduction observed:   22.2%

Implied calculation:
  22.2% savings ÷ 37.5% recirc reduction = 59% standby loss fraction
```

**Finding:** Approximately **59% of DHW gas consumption** was attributable to recirculation standby losses — significantly higher than Navien's factory estimate of 23%.

**Explanation:** The elevated standby losses are consistent with:
- Cold basement location (~55-60°F ambient)
- Long pipe runs to fixtures
- Winter inlet water temperatures (~45°F)
- Hot water sitting in uninsulated pipes during recirc-off periods

### Projected Annual Savings

| Scenario | Annual DHW Gas | Annual Cost | vs. Old |
|----------|----------------|-------------|---------|
| Old (24hr recirc) | ~221 CCF | ~$368 | — |
| New (15hr recirc) | ~175 CCF | ~$291 | **-$77/year** |

**ROI:** Immediate — no hardware cost, pure operational optimization.

### Comfort Impact Assessment

The 9-hour overnight shutoff (9 PM - 6 AM) should have minimal comfort impact:
- Low hot water demand period
- First morning draw will have ~30 second delay (acceptable)
- Could reduce to 12hr schedule (6 PM - 6 AM) if no comfort issues observed

---

## Corrected Year-over-Year Analysis

### January 2026 vs January 2025 (Using Navien DHW Data)

| Metric | Jan 2025 | Jan 2026 | YoY Change | Interpretation |
|--------|----------|----------|------------|----------------|
| **Total Gas** | 161 CCF | 168 CCF | +4.3% | Includes DHW savings |
| **DHW (Navien)** | 22.83 CCF | 17.76 CCF | **-22.2%** | Recirc optimization |
| **Space Heating** | 138.17 CCF | 150.24 CCF | **+8.7%** | Weather-driven |
| **HDD65** | 1,134 | 1,230 | **+8.5%** | Colder winter |
| **Heating Intensity** | 121.8 | 122.1 | **+0.2%** | ✅ Flat (excellent) |
| **Electricity** | 461 kWh | 515 kWh | +11.7% | Billing days + blower |
| **HVAC Runtime** | — | 220 hrs | — | 10.7 min/HDD |

**Key Insight:** The 8.7% increase in space heating gas perfectly tracks the 8.5% increase in HDD. The +0.2% heating intensity variance is well within the baseline CV of 7.0%, confirming:
1. No equipment degradation
2. No envelope compromise  
3. Baseline methodology validated

### Gas Consumption Decomposition

```
January 2026 Total Gas: 168.0 CCF
├── Space Heating:      150.2 CCF (89.4%)
└── Domestic Hot Water:  17.8 CCF (10.6%)

January 2025 Total Gas: 161.0 CCF  
├── Space Heating:      138.2 CCF (85.8%)
└── Domestic Hot Water:  22.8 CCF (14.2%)
```

The DHW share dropped from 14.2% to 10.6% of total gas — a direct result of the recirculation optimization.

### Historical January Comparison (5-Year Trend)

| Year | Total CCF | DHW CCF | Space Heat CCF | HDD65 | CCF/1kHDD |
|------|-----------|---------|----------------|-------|-----------|
| 2022 | 141 | ~18* | ~123 | ~1,100 | ~112 |
| 2023 | 133 | ~18* | ~115 | ~985 | ~117 |
| 2024 | 120 | ~18* | ~102 | ~950 | ~107 |
| 2025 | 161 | 22.83 | 138.2 | 1,134 | 121.8 |
| **2026** | **168** | **17.76** | **150.2** | **1,230** | **122.1** |

*DHW estimated for 2022-2024 (Navien monitoring started Oct 2024)

**Trend:** The 2025-2026 heating seasons are the coldest in the dataset. Despite this, heating intensity remains stable at 121-122 CCF/1kHDD, validating long-term system performance.

---

## Month-over-Month Analysis

### Natural Gas (December 2025 → January 2026)

| Metric | Dec 2025 | Jan 2026 | MoM Change |
|--------|----------|----------|------------|
| Total CCF | 110 | 168 | +52.7% |
| Space Heat CCF | 88.3 | 150.2 | +70.2% |
| DHW CCF (Navien) | 21.75 | 17.76 | -18.3% |
| Days in Period | 28 | 34 | +21.4% |
| HDD65 | 1,148 | 1,230 | +7.1% |

**Analysis:** Space heating increased 70% MoM while HDD only increased 7%. This reflects billing period alignment — December bill captures mid-November through mid-December (before the coldest period), while January bill captures the late-January cold snap.

### Electricity (December 2025 → January 2026)

| Metric | Dec 2025 | Jan 2026 | MoM Change |
|--------|----------|----------|------------|
| Total kWh | 454 | 515 | +13.4% |
| Days in Period | 33 | 34 | +3.0% |
| kWh/Day | 13.76 | 15.15 | +10.1% |

**Analysis:** The 10.1% daily increase reflects higher furnace blower runtime (220 vs 206 heating hours).

### HVAC Runtime (December 2025 → January 2026)

| Metric | Dec 2025 | Jan 2026 | MoM Change |
|--------|----------|----------|------------|
| Total Heating Hours | 206 | 220 | +6.8% |
| 1F Zone Hours | 87 | 103 | +18.4% |
| 2F Zone Hours | 119 | 117 | -1.7% |
| Zone Balance (2F%) | 57.8% | 53.2% | -4.6 pts |
| min/HDD | 10.8 | 10.7 | -0.9% |

**Analysis:** The zone balance shift from 57.8% to 53.2% indicates 1F worked harder during colder conditions — consistent with the thermal model showing 1F has 26% higher UA per square foot.

---

## 13-Month Rolling Comparison

### Gas Consumption (Feb 2025 - Jan 2026 vs Feb 2024 - Jan 2025)

| Period | Total CCF | Space Heat | DHW | Avg CCF/Month |
|--------|-----------|------------|-----|---------------|
| Feb 2024 - Jan 2025 | 786 | ~566 | ~220 | 60.5 |
| Feb 2025 - Jan 2026 | 802 | ~588 | ~214 | 61.7 |
| **Change** | **+16 CCF** | **+22 CCF** | **-6 CCF** | **+2.0%** |

**Analysis:** The 13-month rolling gas increased only 2.0% despite a significantly colder winter, thanks to the DHW optimization offsetting some of the heating increase.

### Electricity (Feb 2025 - Jan 2026 vs Feb 2024 - Jan 2025)

| Period | Total kWh | Avg kWh/Month |
|--------|-----------|---------------|
| Feb 2024 - Jan 2025 | 6,631 | 510 |
| Feb 2025 - Jan 2026 | 6,838 | 526 |
| **Change** | **+207 kWh** | **+3.1%** |

---

## January Cold Snap Analysis

### Late January 2026 Arctic Event (Jan 24-31)

The most severe sustained cold in the 5-year dataset:

| Date | Low °F | Mean °F | HDD65 | Total Runtime | min/HDD |
|------|--------|---------|-------|---------------|---------|
| Jan 24 | 2 | 10.2 | 54.8 | 10.5h | 11.5 |
| Jan 25 | 4 | 8.7 | 56.3 | 11.4h | 12.1 |
| Jan 26 | 13 | 16.5 | 48.5 | 9.5h | 11.8 |
| Jan 27 | 6 | 13.0 | 52.0 | 9.0h | 10.4 |
| Jan 28 | 5 | 13.0 | 52.0 | 10.0h | 11.5 |
| Jan 29 | 6 | 12.9 | 52.1 | 8.7h | 10.0 |
| Jan 30 | 1 | 9.2 | 55.8 | 10.2h | 11.0 |
| Jan 31 | -2 | 7.6 | 57.4 | 10.8h | 11.3 |
| **8-Day** | **-2** | **11.4** | **429** | **80.1h** | **11.2** |

**Cold Snap Metrics:**
- **8-Day HDD:** 429 (35% of monthly total in 26% of days)
- **Average Runtime:** 10.0 hours/day (vs 7.1h monthly average)
- **Runtime Efficiency:** 11.2 min/HDD (within ±2σ of 10.9 baseline)
- **Minimum Temperature:** -2°F (January 31)

**Equipment Performance:**
- ✅ No efficiency alerts triggered
- ✅ No recovery rate degradation
- ✅ Runtime stayed within statistical control limits
- ✅ Zone balance remained within 45-55% target

---

## HVAC Runtime Performance

### 2025-2026 Heating Season Summary

| Month | Heat Hours | HDD65 | min/HDD | Zone Balance (2F%) |
|-------|------------|-------|---------|-------------------|
| Oct 2025 | 33 | 358 | 5.5 | 30.3% |
| Nov 2025 | 103 | 716 | 8.6 | 37.9% |
| Dec 2025 | 206 | 1,148 | 10.8 | 57.8% |
| Jan 2026 | 220 | 1,230 | 10.7 | 53.2% |
| **Season Total** | **562** | **3,452** | **9.8** | **48.5%** |

### Baseline Comparison

| Metric | Baseline | Jan 2026 | Status |
|--------|----------|----------|--------|
| Runtime Efficiency | 10.9 min/HDD | 10.7 min/HDD | ✅ 2% better |
| Zone Balance Target | 50% ±5% | 53.2% | ✅ Within range |
| Peak Daily Runtime | 12.5h @ 55+ HDD | 11.4h @ 56 HDD | ✅ Better |

---

## Updated Baseline Metrics

### Corrected 2025 Annual Performance

With Navien DHW metering (Oct 2024 - Dec 2025 data), the 2025 baseline should be recalculated:

| Metric | Original (Est. DHW) | Corrected (Navien DHW) |
|--------|---------------------|------------------------|
| Total Gas | 787 CCF | 787 CCF |
| DHW Gas | 188 CCF (billing-aligned) | 220.8 CCF (Navien sum) |
| Space Heating | 599 CCF | 566.2 CCF |
| Heating Intensity | 95.5 CCF/1kHDD | **90.3 CCF/1kHDD** |

**Note:** The original 188 CCF DHW estimate was lower than the Navien-metered actual of 220.8 CCF. This means the true space heating consumption — and therefore heating intensity — is lower (better) than originally reported.

### Updated Investigation Thresholds

| Metric | Baseline | Warning (+10%) | Action (+15%) | Jan 2026 |
|--------|----------|----------------|---------------|----------|
| Heating Intensity | 90.3 CCF/1kHDD | >99 | >104 | 122.1* |
| Monthly Space Heat (Jan) | 138 CCF | >152 | >159 | 150 ✅ |
| Monthly DHW (Jan) | 22.8 CCF | >25 | >26 | 17.8 ✅ |
| Runtime Efficiency | 10.9 min/HDD | >12.0 | >12.5 | 10.7 ✅ |

*January heating intensity elevated vs annual due to billing period alignment; runtime efficiency confirms system health

---

## Recommendations

### Completed Actions ✅

1. **DHW Recirculation Optimization** — Implemented mid-January
   - 15hr schedule (off 9 PM - 6 AM)
   - Projected savings: ~$77/year
   - No comfort complaints reported

### Monitoring Priorities

1. **Track DHW Savings:** Continue Navien monitoring to verify projected annual savings hold through summer (lower savings expected due to warmer inlet temps)

2. **Consider Further Recirc Reduction:** If no comfort issues, test 12hr schedule (off 6 PM - 6 AM) for additional ~$25/year savings

3. **Document Standby Loss Finding:** The 59% standby loss fraction (vs 23% factory estimate) is significant and worth publishing for other Navien owners

### Documentation Updates

1. **Update baseline DHW assumption** from 188 CCF to 221 CCF (Navien-metered)
2. **Revise heating intensity baseline** from 95.5 to 90.3 CCF/1kHDD
3. **Add DHW optimization case study** to methodology documentation

---

## Appendix: Monthly Data Tables

### Gas Consumption (13 Months with DHW Split)

| Month | Total CCF | DHW (Navien) | Space Heat | HDD | CCF/1kHDD |
|-------|-----------|--------------|------------|-----|-----------|
| Jan 2025 | 161 | 22.83 | 138.2 | 1,134 | 121.8 |
| Feb 2025 | 154 | 18.12 | 135.9 | 940 | 144.5 |
| Mar 2025 | 106 | 22.47 | 83.5 | 696 | 120.0 |
| Apr 2025 | 75 | 20.66 | 54.3 | 422 | 128.8 |
| May 2025 | 38 | 19.21 | 18.8 | 170 | 110.5 |
| Jun 2025 | 23 | 16.72 | 6.3 | 22 | — |
| Jul 2025 | 17 | 15.59 | 1.4 | 0 | — |
| Aug 2025 | 16 | 11.24 | 4.8 | 20 | — |
| Sep 2025 | 11 | 15.59 | -4.6* | 42 | — |
| Oct 2025 | 18 | 17.40 | 0.6 | 358 | — |
| Nov 2025 | 58 | 19.21 | 38.8 | 716 | 54.2 |
| Dec 2025 | 110 | 21.75 | 88.3 | 1,148 | 76.9 |
| **Jan 2026** | **168** | **17.76** | **150.2** | **1,230** | **122.1** |

*Negative value indicates billing period artifacts; DHW exceeded total for this period

### Electricity Consumption (13 Months)

| Month | kWh | kWh/Day | Cost | $/kWh |
|-------|-----|---------|------|-------|
| Jan 2025 | 461 | 14.87 | $143.56 | $0.311 |
| Feb 2025 | 447 | 14.42 | $139.48 | $0.312 |
| Mar 2025 | 314 | 10.83 | $100.84 | $0.321 |
| Apr 2025 | 344 | 12.29 | $109.56 | $0.318 |
| May 2025 | 464 | 14.97 | $141.84 | $0.306 |
| Jun 2025 | 626 | 19.56 | $179.41 | $0.287 |
| Jul 2025 | 1,129 | 33.21 | $315.86 | $0.280 |
| Aug 2025 | 880 | 31.43 | $248.31 | $0.282 |
| Sep 2025 | 619 | 20.63 | $173.58 | $0.280 |
| Oct 2025 | 513 | 18.32 | $138.95 | $0.271 |
| Nov 2025 | 479 | 15.97 | $130.36 | $0.272 |
| Dec 2025 | 454 | 13.76 | $124.09 | $0.273 |
| **Jan 2026** | **515** | **15.15** | **$139.47** | **$0.271** |

---

**Document Version:** 1.3.0  
**Analysis Date:** February 2, 2026  
**Data Coverage:** January 2022 - January 2026 (49 months)  
**Author:** William K. Collis
