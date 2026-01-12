# Comprehensive Analysis of Residential Energy Performance and HVAC System Integration

**A Diagnostic Baseline Report for the Connecticut Climate Zone**

**Version:** 1.2.1  
**Date:** January 2026  
**Author:** William K. Collis  
**Property Location:** Central Connecticut, Climate Zone 5A

---

## Executive Summary

The establishment of a definitive energy performance baseline for a high-efficiency residential structure requires a multi-faceted evaluation of mechanical equipment, architectural geometry, and behavioral variables. For this property, a 2,440 sq. ft. two-story Colonial constructed in 2021 and located in Climate Zone 5A (Central Connecticut), a four-year longitudinal study from January 2022 through December 2025 has provided a robust dataset to quantify the efficiency of the installed systems.

For a two-occupant household, the observed electricity baseload of 9.7 kWh/day and Domestic Hot Water (DHW) consumption of 0.533 CCF/day are consistent with national post-2020 residential benchmarks for high-efficiency homes. This analysis integrates verified utility consumption, high-resolution HVAC runtime logs, and internal DHW monitoring to establish a revised baseline as of January 2026. This revision (v1.2.1) adopts a **Fully Billing-Aligned methodology** to reconcile asynchronous utility data with calendar-year performance.

**Key Performance Indicators (2025 Baseline):**
- **Site Energy Use Intensity (EUI):** 41.7 kBTU/ft²-yr
- **Heating Intensity:** 95.5 CCF/1,000 HDD (33% better than regional average)
- **Building Load Coefficient (UA):** 480 BTU/hr-°F (21-34% superior to 2021 IECC code-minimum)
- **Annual Electricity Consumption:** 6,730 kWh
- **Performance Stability:** CV < 7% across all major metrics (4-year average)

---

## Table of Contents

1. [Mechanical Systems Infrastructure](#mechanical-systems-infrastructure)
2. [Year-Over-Year Performance Analysis](#year-over-year-performance-analysis)
3. [Electricity Load Decomposition](#electricity-load-decomposition)
4. [Thermodynamic Envelope Analysis](#thermodynamic-envelope-analysis)
5. [Domestic Hot Water Performance](#domestic-hot-water-performance)
6. [System Integrity & Maintenance](#system-integrity-and-maintenance)
7. [Energy Monitoring ROI Analysis](#energy-monitoring-roi-analysis)
8. [Baseline Summary Metrics](#baseline-summary-metrics)

---

## Mechanical Systems Infrastructure and Technical Specifications

The property utilizes a sophisticated integration of high-efficiency mechanical systems, prioritizing condensing technology and commercial-grade moisture control.

### Primary Heating and Cooling Equipment

**Heating System:**
- **Model:** American Standard Silver 95 series (S9X1C100U5PSBA)
- **Type:** Single-stage condensing gas furnace
- **Efficiency:** 95-96% AFUE
- **Input Capacity:** 100,000 BTU/hr
- **Blower:** 1 hp constant-torque ECM (Electronically Commutated Motor) with Vortica™ II design
- **Operational Characteristic:** Full modulation not available; delivers 100% capacity on all heating calls

**Cooling System:**
- **Model:** American Standard Silver 14 (4A7A4048L1000AA)
- **Type:** Split-system air conditioner
- **Capacity:** 48,000 BTU/hr (4-ton)
- **Efficiency:** 14 SEER
- **Compressor:** Single-stage Duration™ scroll compressor
- **Indoor Coil:** American Standard 4TXCC005 all-aluminum cased A-coil
- **Expansion Device:** Thermostatic expansion valve (TXV) for precise refrigerant regulation

**Supplemental Heating:**
- **Type:** Natural gas direct-vent fireplace (living room)
- **Efficiency:** 65-70% steady-state (manufacturer specification)
- **2025 Delivered Heat:** 3.6 MMBTU
- **2025 Fuel Input:** 5.1-5.5 MMBTU (51-55 CCF, included in space heating total)

### Specialized Moisture Control System

**Basement Dehumidifier:**
- **Model:** Santa Fe Classic
- **Capacity:** 110 pints per day moisture removal
- **Power Draw:** 700W (6.4A) during active compression
- **Energy Factor:** 3.0 L/kWh (exceeds Energy Star requirements)
- **Operational Season:** April through October (basement temps >60°F)
- **Control Strategy:** Fixed 45% RH setpoint (equivalent to 43°F dew point at 65°F basement temperature)

### Domestic Hot Water (DHW) System

**Water Heater:**
- **Type:** Navien NPE-series condensing tankless
- **Efficiency:** 95%+ AFUE
- **Monitoring:** Independent gas meter (NaviLink system)
- **Recirculation:** Active system with estimated 23% standby losses (per Navien factory guidance)

---

## Year-Over-Year Weather-Normalized Efficiency Analysis (2022-2025)

The correction of historical consumption against meteorological data from Hartford Bradley International Airport (KBDL) identifies the home's heating efficiency signature. 

### Terminology

- **Heating Degree Days (HDD):** Cumulative degrees that average daily temperature falls below 65°F
- **CCF:** Hundred cubic feet of natural gas (1 CCF ≈ 100,000 BTU)
- **Heating Intensity:** CCF consumed per 1,000 HDD (efficiency metric normalized for weather severity)

### Four-Year Performance Summary

| Performance Metric | 2022 | 2023 | 2024 | 2025 |
|--------------------|------|------|------|------|
| Annual HDD65 (KBDL) | 6,092 | 5,465 | 5,305 | 6,270 |
| Total Natural Gas (CCF) | 815 | 764 | 694 | 787 |
| Space Heating Gas (CCF) | 547 | 496 | 426 | 599 |
| DHW Gas (CCF) | 268 | 268 | 268 | 188* |
| Heating Intensity (CCF/1k HDD) | 89.8 | 90.8 | 80.3 | 95.5 |

*2025 DHW value reflects billing-aligned methodology (see Domestic Hot Water section)

### Statistical Validation

| Metric | 2025 Value | 4-Year Mean | Std Dev | CV (%) |
|--------|------------|-------------|---------|--------|
| Heating Intensity (CCF/1k HDD) | 95.5 | 89.1 | 6.2 | 7.0% |
| Annual Site EUI (kBTU/ft²-yr) | 41.7 | 40.8 | 2.1 | 5.1% |

The coefficient of variation (CV) below 8% for all major metrics confirms exceptional baseline stability.

### Causal Analysis of 2024–2025 Variance

While 2025 remained **33% more efficient than the regional average** (145 CCF/1k HDD per EIA Connecticut residential data), the normalized heating intensity rose from 80.3 to 95.5 CCF/1k HDD (+19%). This shift indicates that the 18% increase in weather severity in 2025 was accompanied by a non-linear efficiency loss.

**Diagnostic Findings:**

1. **Diminishing Internal Gain Leverage:** In the extremely mild 2024 winter (5,305 HDD), "free" heat from occupants, appliances, and solar gains covered a larger percentage of the total heating load. In the severe 2025 winter (6,270 HDD), these fixed internal gains became proportionally less significant.

2. **Setpoint Stability:** High-resolution thermostat logs from late 2025 show increased whole-house setpoint consistency, potentially reducing periods where the home benefited from fireplace-driven "passive" zoning (warmer living areas allowing lower setpoints in bedrooms).

3. **Balance Point Effects:** At the home's 59°F heating balance point, mild shoulder seasons (like 2024) maximize furnace efficiency by operating only during periods of high load factor. Severe winters force operation during marginal outdoor conditions where cycling losses increase.

---

## Electricity Load Decomposition (2025)

The electricity load has been audited at the billing-period level to isolate seasonal HVAC contributions and identify unresolved consumption categories.

### Billing-Aligned Decomposition

| End Use Category | Annual Consumption (kWh) | Annual Cost ($) | % of Total |
|------------------|--------------------------|-----------------|------------|
| Baseload (9.7 kWh/day) | 3,532 | $1,021 | 52% |
| Space Cooling (AC @ 4.9 kW) | 1,694 | $490 | 25% |
| Furnace Blower (@ 0.21 kW)* | 84 | $24 | 1% |
| Santa Fe Dehum (Modeled) | 294 | $85 | 5% |
| Residual (Seasonal Variance)† | 1,126 | $326 | 17% |
| **Total Billed Electricity** | **6,730** | **$1,946** | **100%** |

### Technical Accounting Notes

**Furnace Blower Runtime (*):**
The 84 kWh allocation at 0.21 kW draw implies approximately 400 effective full-load hours. However, the 831 hours of cumulative furnace runtime reflects total burner call time derived from high-resolution thermostat logs, which capture all heating cycles including short cycling and shoulder-season calls. 

**Explanation of Discrepancy:** The ECM blower operates at variable speeds:
- **High-fire heating mode:** ~0.21 kW (400 hours tracked)
- **Low-speed circulation mode:** ~0.10 kW (potentially embedded in Residual)
- **Intermittent fan-only calls:** Not captured in this allocation

This suggests either (a) the blower frequently operates at reduced speed taps, or (b) a portion of its circulation energy is embedded within the Residual category.

**Dehumidifier Load Attribution (†):**
The 1,126 kWh Residual occurs almost exclusively during the April–October window. When combined with the modeled 294 kWh baseline, the **total seasonal moisture control is estimated at 1,420 kWh**. This magnitude is strongly consistent with a 700W commercial dehumidifier running at approximately 50% duty cycle during humid months.

### Baseload Composition

The 9.7 kWh/day (3,532 kWh annual) baseload represents:
- Refrigeration (kitchen + garage units)
- Electronics and computing (home office, networking equipment)
- Lighting (LED throughout)
- Miscellaneous plug loads
- DHW electric circulation pump

For a two-occupant household, this aligns with national benchmarks for high-efficiency homes (8-12 kWh/day typical range).

### Space Cooling Performance

The 1,694 kWh cooling load was verified through billing-period isolation during summer months (June-September). Key findings:

- **Average Power Draw:** 4.9 kW (4-ton unit at rated conditions)
- **Estimated Runtime:** 346 hours (summer 2025)
- **Performance:** Consistent with manufacturer specifications for 14 SEER split system
- **Verification Method:** Regression analysis of kWh against cooling degree days

---

## Thermodynamic Envelope Analysis

The building's thermal integrity is quantified by the **Building Load Coefficient (UA value)**, which represents the rate of heat loss per degree of temperature difference between indoors and outdoors.

### UA Calculation Methodology

The UA value is derived from:
1. **Delivered Heat:** 57.5 MMBTU (furnace) + 3.6 MMBTU (fireplace) = 61.1 MMBTU total
2. **Temperature Differential:** 6,270 HDD65 baseline → 5,294 HDD59 (adjusted for 59°F balance point)
3. **Heat Loss Rate:** UA = 61.1 MMBTU ÷ (24 hr/day × 5,294 HDD) = 480 BTU/hr-°F

### Envelope Performance Metrics

| Metric | Value | Industry Comparison |
|--------|-------|---------------------|
| Building Load Coefficient (UA) | 480 BTU/hr-°F | — |
| Area-Normalized UA | 0.197 BTU/hr-°F-ft² | — |
| Heating Balance Point | 59°F | 55-62°F typical for high-efficiency homes |
| IECC 2021 Code-Minimum UA | 610-725 BTU/hr-°F | 21-34% worse than measured |

**Performance Interpretation:** The UA of 480 BTU/hr-°F indicates a very tight thermal envelope. This is achieved through:
- Continuous exterior foam insulation (R-5 to R-10 depending on wall section)
- High-performance windows (U-0.27 to U-0.30)
- Comprehensive air sealing (estimated <3 ACH50 based on performance)
- Insulated attic plane (R-49 to R-60 blown fiberglass)

**Architectural Challenge:** The 14-foot cathedral ceiling in the main living area creates potential for vertical stratification, which could theoretically increase the effective UA. The measured performance suggests this effect is well-controlled through proper return air placement and circulation strategies.

### Balance Point Resolution

The 59°F balance point indicates that the home requires no heating when outdoor temperatures exceed 59°F, as internal gains from occupants, appliances, and solar exposure meet the total heat loss. This is consistent with:
- High envelope integrity (low UA)
- Moderate internal gains (two occupants, typical appliance usage)
- South-facing window orientation (passive solar contribution)

---

## Domestic Hot Water (DHW) Performance Analysis

For 2025, DHW gas consumption was calibrated from low-HDD billing cycles at a rate of 0.533 CCF/day, yielding an annual aligned total of 188 CCF (23.9% of total gas consumption).

### Reconciliation of Meter Variance

| Data Source | Annual CCF | Method |
|-------------|-----------|--------|
| Navien Independent Meter | 220.8 | Direct metering via NaviLink |
| Billing-Aligned Calculation | 188.0 | Regression from low-HDD periods |
| **Variance** | **32.8 CCF (15%)** | **Unresolved measurement gap** |

**Explanation of Discrepancy:**

The 32.8 CCF variance is an unresolved measurement gap that likely accumulates during winter billing periods when increased recirculation standby losses (estimated at 23% of total DHW per Navien NPE-series factory guidance) are difficult to isolate from the primary space heating load.

**Contributing Factors:**
1. **Inlet Water Temperature:** Winter inlet water temperatures (~45°F) require higher burner input than summer (~65°F), potentially affecting meter calibration accuracy
2. **Recirculation Standby Loss:** The active recirculation pump maintains hot water in distribution lines, creating thermal losses that are metered as DHW but may partially contribute to space heating via incidental pipe radiation
3. **Billing Period Misalignment:** The Navien meter records calendar-year consumption while utility billing follows offset meter read dates

**Baseline Decision:** The billing-aligned 188 CCF figure is utilized for Energy Use Intensity (EUI) consistency to prevent "double-counting" during heating months. This represents a conservative lower bound for actual DHW consumption.

### DHW Performance Context

For a two-occupant household:
- **Daily Usage:** 0.533 CCF/day (53.3 gallons equivalent at 70°F temperature rise)
- **Annual Cost:** ~$350 (gas) + ~$50 (electric recirculation pump)
- **Efficiency:** 95%+ AFUE via condensing technology
- **Benchmark:** Aligns with national average of 50-65 gallons/day for high-efficiency households

---

## System Integrity and Long-Term Maintenance Insights

### Furnace Blower Performance and Static Pressure

**Equipment Context:**
- **Motor Type:** Constant-torque ECM (Electronically Commutated Motor)
- **Rated Power:** 1 hp (746W maximum)
- **Measured Baseline:** 0.21 kW (210W) during typical heating operation
- **Replacement Cost:** $586 (motor assembly only)

**Operational Concern:**

Occupant modifications—specifically closing 2nd-floor vents by approximately 50%—increase system back-pressure. Constant-torque ECMs respond to increased static pressure by **increasing wattage draw** to maintain target CFM. 

**Diagnostic Value of Monitoring:**

Monitoring the blower's real-time wattage provides an early-warning system for excessive static pressure:
- **Baseline:** 210W (current operation)
- **Concern Threshold:** >300W (indicates >50% increase in back-pressure)
- **Critical Threshold:** >400W (risk of premature motor failure)

**Recommendation:** Whole-house energy monitoring with dedicated furnace circuit tracking can detect gradual motor degradation before catastrophic failure, justifying the monitor cost solely through motor replacement risk mitigation ($586 replacement vs. ~$400 monitoring investment).

### Dehumidifier Operational Optimization

**Current Operation:**
- **Setpoint:** 45% RH (fixed humidity control)
- **Basement Conditions:** 65°F average temperature
- **Equivalent Dew Point:** 43°F
- **Estimated Annual Consumption:** 1,420 kWh (~$410)

**Proposed Optimization:**

Transitioning from fixed RH control to **dew point control** at 52°F target (approximately 63% RH at 65°F) using a Shelly H&T sensor and smart plug:

**Expected Outcomes:**
- **Duty Cycle Reduction:** ~25% (based on psychrometric modeling)
- **Energy Savings:** ~355 kWh/year
- **Cost Savings:** ~$105/year
- **Implementation Cost:** ~$50 (Shelly H&T + Plug)
- **Simple Payback:** 5.7 months

**Technical Justification:** 

At 65°F basement temperature, a 45% RH setpoint (43°F dew point) provides no additional moisture protection compared to a 52°F dew point (63% RH) for mold prevention or comfort. The lower setpoint only increases compressor runtime without commensurate benefit. Dew point control eliminates this inefficiency while maintaining equivalent moisture protection across seasonal temperature variations.

### Air Conditioner Longevity Tracking

**Equipment:** American Standard Silver 14 (4-ton, 14 SEER)  
**Baseline Power Draw:** 4.9 kW  
**Operational History:** 2022-2025 (4 cooling seasons)

**Degradation Indicators to Monitor:**
1. **Power Draw Increase:** >10% rise above 4.9 kW baseline suggests compressor wear or refrigerant loss
2. **Runtime Efficiency:** Decreasing cooling per kWh indicates declining SEER performance
3. **Short Cycling:** Increasing start/stop cycles suggest control or refrigerant issues

**Monitoring Value:** Continuous power monitoring can detect gradual efficiency losses years before catastrophic failure, enabling proactive maintenance (refrigerant recharge, coil cleaning) rather than emergency replacement.

---

## Energy Monitoring ROI Analysis

A whole-house energy monitor is uniquely suited to verify the "Residual" electricity load identified in the v1.2.1 audit and provide ongoing system health diagnostics.

### Primary Value Propositions

#### 1. Mystery Load Resolution ($326/year potential)

**Objective:** Quantify the 1,126 kWh Residual load

**Hypothesis:** Majority attributable to unmeasured dehumidifier operation beyond modeled baseline

**Monitoring Strategy:**
- Dedicated CT clamp on Santa Fe Classic breaker
- April-October seasonal tracking
- Compare measured vs. modeled (294 kWh) baseline

**Value:** If Residual is confirmed as dehumidifier-only, optimization strategies (dew point control, setpoint adjustment) can target full $326/year reduction. If other phantom loads are discovered, enables targeted elimination.

#### 2. ECM Blower Safety Monitoring

**Objective:** Prevent premature $586 motor failure

**Method:** Track furnace blower circuit wattage in real-time

**Thresholds:**
- **Baseline:** 210W (current operation)
- **Warning:** >300W (investigate vent closures/filter)
- **Critical:** >400W (excessive static pressure, motor strain)

**Value:** Early detection of static pressure issues prevents catastrophic motor failure. Monitor cost (~$400) justified by single failure prevention.

#### 3. AC Performance Verification

**Objective:** Detect efficiency degradation before failure

**Method:** Monitor 4-ton AC unit power draw and runtime

**Baseline:** 4.9 kW steady-state

**Degradation Indicators:**
- **Power Draw:** >10% increase (refrigerant loss, compressor wear)
- **Runtime Efficiency:** Decreasing cooling per kWh consumed
- **Cycling Behavior:** Increasing short-cycle frequency

**Value:** Proactive maintenance extends system life and prevents emergency replacement. Typical SEER degradation: 1-2% per year if uncorrected.

### ROI Summary

| Value Stream | Annual Value | One-Time Value | Confidence |
|--------------|--------------|----------------|------------|
| Mystery Load Resolution | $0-$326 | — | Medium |
| Blower Failure Prevention | $50 (amortized) | $586 | High |
| AC Longevity Extension | $75-$150 | $8,000+ (replacement) | Medium |
| Baseline Verification | — | Documentation value | High |
| **Total Annual Value** | **$125-$526** | **$8,586+** | — |

**Monitor Investment:** $400-$600 (Fusion Energy 16-CT or equivalent)  
**Simple Payback:** 1.1 to 4.8 years (depending on mystery load findings)

---

## Baseline Summary Metrics

### Operational Thresholds (2025 Baseline)

| Metric | Aligned Baseline (2025) | Investigation Threshold | Action Trigger |
|--------|-------------------------|-------------------------|----------------|
| Annual Site EUI | 41.7 kBTU/ft²-yr | ±5% (39.6-43.8) | ±10% |
| Heating Intensity | 95.5 CCF/1k HDD | +10% (>105 CCF/1k HDD) | +15% |
| Moisture Control Load | ~1,420 kWh/season | >1,800 kWh | >2,000 kWh |
| Cooling Intensity | 4.9 kW draw | ±10% (4.4-5.4 kW) | ±15% |
| Furnace Blower Power | 210W (0.21 kW) | >300W | >400W |

### Four-Year Performance Stability

The coefficient of variation (CV) below 8% for all major metrics provides high confidence in this baseline for evaluating future modifications:

- **Heating Intensity:** CV = 7.0% (excellent stability across varying weather)
- **Site EUI:** CV = 5.1% (exceptional consistency)
- **Electricity Baseload:** CV < 3% (2022-2025 average: 9.6 kWh/day)

**Interpretation:** Any future deviation beyond investigation thresholds indicates either:
1. Equipment degradation (requires diagnostic/maintenance)
2. Occupant behavior change (document for future baseline adjustment)
3. Envelope compromise (investigate air sealing, insulation)

---

## Appendices

### A. Glossary of Technical Terms

- **AFUE (Annual Fuel Utilization Efficiency):** Percentage of fuel energy converted to useful heat over a full heating season
- **CCF (Hundred Cubic Feet):** Unit of natural gas measurement; 1 CCF ≈ 100,000 BTU (varies by gas composition)
- **CV (Coefficient of Variation):** Standard deviation divided by mean, expressed as percentage; measures relative variability
- **ECM (Electronically Commutated Motor):** Variable-speed DC motor with integrated controls for efficiency
- **EUI (Energy Use Intensity):** Total energy consumption per square foot of conditioned space per year
- **HDD (Heating Degree Days):** Cumulative degrees that average daily temperature falls below 65°F (or other base temperature)
- **SEER (Seasonal Energy Efficiency Ratio):** Cooling output (BTU) divided by electrical input (Wh) over typical cooling season
- **TXV (Thermostatic Expansion Valve):** Refrigerant metering device that maintains optimal superheat
- **UA Value (Building Load Coefficient):** Rate of heat loss per degree temperature difference (BTU/hr-°F)

### B. Data Sources and References

1. **Weather Data:** NOAA National Centers for Environmental Information, Hartford Bradley International Airport (KBDL), Station ID: USW00014740
2. **Utility Data:** Eversource Energy (electricity), Southern Connecticut Gas Company (natural gas)
3. **Equipment Specifications:** American Standard HVAC technical documentation, Navien NPE-series installation manuals
4. **Regional Benchmarks:** U.S. Energy Information Administration (EIA), Connecticut residential energy consumption survey data
5. **IECC Code Requirements:** International Energy Conservation Code (IECC) 2021, Climate Zone 5A specifications

### C. Revision History

- **v1.0.0 (January 2023):** Initial baseline established from 2022 data
- **v1.1.0 (January 2024):** Two-year update with refined HDD correlation methodology
- **v1.2.0 (December 2025):** Three-year update with preliminary 2025 data
- **v1.2.1 (January 2026):** Current version with fully billing-aligned 2025 data and 4-year statistical validation

---

**Document Status:** Active baseline (v1.2.1)  
**Next Update:** January 2027 (5-year comprehensive review)  
**Prepared by:** William K. Collis, P.E. (pending)  
**Date:** January 11, 2026
