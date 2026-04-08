# HVAC Performance Update: March 2026

**Version:** 1.5.0
**Date:** April 1, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut

---

## Executive Summary

March 2026 represents the transition into the spring shoulder season. As outdoor temperatures rose, heating demand decreased significantly. The system demonstrated exceptional efficiency, with runtime per HDD dropping to 6.4 min/HDD—well below the established 10.9 min/HDD baseline. Domestic Hot Water (DHW) savings from the recirculation optimization continue to be realized, with a substantial year-over-year reduction in gas consumption.

**Key March 2026 Findings:**
- **Total Gas Consumption:** 111.0 CCF (Decrease of 36.6% MoM)
- **Weather Severity:** 767.6 HDD65 (Decrease of 29.5% MoM)
- **Space Heating:** 96.0 CCF (Decrease of 40.3% MoM)
- **Heating Intensity:** 144.4 CCF/1kHDD (Slightly lower than March 2025)
- **DHW Consumption:** 15.0 CCF (-33.2% YoY)
- **HVAC Runtime:** 81.4 hours at 6.4 min/HDD (Exceptional efficiency)

**Interpretation:** The reduction in space heating (40.3%) outpaced the decrease in HDD (29.5%), leading to an improved heating intensity. The runtime efficiency of 6.4 min/HDD is approximately 41% better than the baseline, which is typical for the shoulder season as the system operates at a smaller delta-T.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HVAC Runtime Performance](#hvac-runtime-performance)
5. [Recommendations](#recommendations)

---

## Year-over-Year Analysis

### March 2026 vs March 2025

| Metric | March 2025 | March 2026 | YoY Change | Interpretation |
|--------|------------|------------|------------|----------------|
| **Total Gas** | 106.0 CCF | 111.0 CCF | +4.7% | Weather + DHW offset |
| **DHW (Navien)** | 22.47 CCF | 15.00 CCF | **-33.2%** | Recirc optimization |
| **Space Heating** | 83.53 CCF | 96.00 CCF | +14.9% | Weather-driven |
| **HDD65** | 695.5 | 767.6 | **+10.3%** | Warmer than Feb, colder than Mar '25 |
| **Heating Intensity** | 152.4 | 144.4 | -5.3% | Efficient tracking |
| **HVAC Runtime** | 96.0 hrs | 81.4 hrs | -15.2% | Better efficiency |
| **Runtime Efficiency** | 8.28 min/HDD | 6.4 min/HDD | -22.7% | Exceptional |

**Key Insight:** While total gas usage is slightly up, this is primarily due to a 10.3% increase in HDD compared to last March. The 33.2% reduction in DHW consumption continues to provide a significant buffer, allowing the overall energy footprint to remain stable despite the colder-than-average March weather.

---

## Month-over-Month Analysis

### Natural Gas (February 2026 $\rightarrow$ March 2026)

| Metric | February 2026 | March 2026 | MoM Change |
|--------|---------------|------------|------------|
| Total CCF | 175.0 | 111.0 | -36.6% |
| Space Heat CCF | 160.9 | 96.0 | -40.3% |
| DHW CCF (Navien) | 14.14 | 15.00 | +5.7% |
| HDD65 | 1,089.0 | 767.6 | -29.5% |

**Analysis:** The sharp decline in space heating usage aligns with the seasonal transition. The slight increase in DHW consumption is typical for March as users often increase hot water usage during the transition from winter.

### HVAC Runtime (February 2026 $\rightarrow$ March 2026)

| Metric | February 2026 | March 2026 | MoM Change |
|--------|---------------|------------|------------|
| Total Heating Hours | 158.0 | 81.4 | -48.5% |
| Zone Balance (1F%) | 45.6% | 49.6% | +4.0 pts |
| min/HDD | 8.7 | 6.4 | -26.4% |

**Analysis:** Runtime decreased significantly. The zone balance has moved closer to the ideal 50% target, indicating very stable heat distribution as the load on the system decreases.

---

## DHW Performance Update

### Sustained Recirculation Optimization Results
The recirculation schedule change (off 9 PM - 6 AM) continues to deliver strong results:

| Metric | March 2025 (24hr) | March 2026 (15hr) | Change |
|--------|-------------------|-------------------|--------|
| DHW Gas (Navien) | 22.47 CCF | 15.00 CCF | **-33.2%** |
| DHW Operating Hours | 12 hrs | 12 hrs | 0% |

**Note:** With identical operating hours between the two years, the 33.2% reduction in gas is purely an operational gain from the recirculation schedule optimization.

---

## HVAC Runtime Performance

### Baseline Comparison

| Metric | Baseline | March 2026 | Status |
|--------|----------|------------|--------|
| Runtime Efficiency | 10.9 min/HDD | 6.4 min/HDD | 41% better |
| Zone Balance Target | 50% $\pm$ 5% | 49.6% | $\checkmark$ Optimal |

**Analysis:** The system is performing exceptionally well. The runtime efficiency of 6.4 min/HDD is significantly below the annual baseline, reflecting the increased efficiency of the system during lower-load shoulder season conditions.

---

## Recommendations

### Monitoring Priorities
1. **Spring Transition:** Monitor the "Runtime per HDD" metric as it continues to decline. We expect a further drop until the heating system is fully deactivated.
2. **DHW Inlet Temperature:** Track if the DHW savings percentage changes as the incoming municipal water temperature rises during the spring, which typically reduces the energy required for initial heating.
3. **Cooling Season Prep:** Begin monitoring for the first cooling cycles (CDD tracking) to establish the 2026 cooling baseline.

### Pending Data
- **Utility Bills:** March 2026 gas and electric bills pending (expected mid-April).
- Will update `monthly_gas_scg.csv` and `monthly_electricity_eversource.csv` upon receipt.
