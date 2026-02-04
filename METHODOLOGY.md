# Methodology: Billing-Aligned Energy Performance Analysis

**Version:** 1.2.1
**Last Updated:** January 2026

## Overview

This document describes the **Fully Billing-Aligned** methodology used to reconcile asynchronous utility meter read dates with calendar-year weather normalization and performance tracking. This approach addresses a fundamental challenge in residential energy auditing: utility billing cycles rarely align with calendar months, creating ~15-day phase shifts that corrupt weather-normalized efficiency calculations.

---

## The Billing Misalignment Problem

### Standard Industry Practice (Flawed Approach)

Most residential energy analyses simply assign utility bills to calendar months:

```text
Utility Bill: Dec 15, 2024 → Jan 14, 2025 (846 kWh)
Standard Assignment: "January 2025: 846 kWh"
Problem: Bill includes 16 days of December consumption!
```

**Consequences:**

- Weather normalization uses wrong HDD values (January HDD vs. actual Dec 15-Jan 14 HDD)
- Year-over-year comparisons become meaningless if billing dates shift
- Cannot accurately isolate seasonal HVAC loads

### Billing-Aligned Solution

Our methodology allocates consumption based on **actual meter read dates** and calculates daily rates from adjacent billing periods for pro-ration.

---

## Core Methodology Components

### 1. Billing Period Decomposition

**Process:**

For each utility bill, extract:

- **Meter Read Date (Start):** Previous bill end date
- **Meter Read Date (End):** Current bill end date
- **Consumption:** kWh or CCF for the period
- **Duration:** Days between read dates

**Daily Rate Calculation:**

```text
Daily Rate = Total Consumption ÷ Days in Billing Period
```

**Example:**

```text
Bill Period: Dec 15, 2024 → Jan 14, 2025 (31 days)
Consumption: 846 kWh
Daily Rate: 846 ÷ 31 = 27.3 kWh/day
```

### 2. Calendar Month Allocation

**Process:**

For each calendar month, sum consumption from all overlapping billing periods using pro-rated daily rates:

```text
January 2025 Consumption =
  (Dec 15-31, 2024 bill × 14 days) +
  (Jan 1-14, 2025 from same bill × 14 days) +
  (Jan 15-31, 2025 from next bill × 17 days)
```

**Calculation:**

```text
Jan 2025 = (27.3 kWh/day × 14 days) + (next bill daily rate × 17 days)
```

### 3. Weather Normalization Alignment

**HDD Calculation for Billing Periods:**

Once consumption is allocated to calendar days, match with corresponding HDD values from NOAA daily weather data:

```text
HDD65 for Jan 2025 = Σ(max(0, 65°F - T_avg)) for Jan 1-31
```

**Key Advantage:** HDD values now precisely match consumption periods, enabling accurate calculation of heating intensity:

```text
Heating Intensity = Space Heating CCF ÷ (HDD ÷ 1,000)
```

---

## Space Heating Isolation

### Method 1: Low-HDD Regression (DHW Baseline)

**Objective:** Determine DHW consumption independent of space heating

**Process:**

1. **Select Low-HDD Billing Periods:** April-October when HDD < 200/month
2. **Calculate Daily Gas Consumption:** CCF/day for each low-HDD period
3. **Linear Regression:** Regress daily CCF against daily HDD to find intercept
4. **DHW Baseline:** Y-intercept represents zero-HDD consumption (pure DHW)

**Example:**

```text
Low-HDD Periods (2025):
  Apr: 187 HDD, 1.02 CCF/day
  May: 98 HDD, 0.87 CCF/day
  Jun: 12 HDD, 0.68 CCF/day
  Sep: 45 HDD, 0.71 CCF/day

Regression: Daily CCF = 0.533 + (0.0087 × HDD/day)
DHW Baseline = 0.533 CCF/day
```

**Annual DHW Calculation:**

```text
Annual DHW = 0.533 CCF/day × 365 days = 194.5 CCF
Billing-Aligned Total (2025): 188 CCF (accounts for billing period boundaries)
```

### Method 2: High-HDD Allocation (Space Heating)

**Objective:** Subtract DHW baseline from total gas to isolate space heating

**Process:**

1. **Calculate Monthly DHW:** 0.533 CCF/day × days in month
2. **Subtract from Total Gas:** Space Heating = Total - DHW
3. **Sum Annual Space Heating:** Aggregate across all months

**Example (January 2025):**

```text
Total Gas (Jan 2025): 112 CCF
DHW Baseline: 0.533 × 31 days = 16.5 CCF
Space Heating: 112 - 16.5 = 95.5 CCF
```

---

## Electricity Decomposition

### Baseload Determination

**Method:** Average consumption during minimum-load periods (spring/fall shoulder seasons)

**Process:**

1. **Identify Low-Load Months:** April, May, October (minimal HVAC operation)
2. **Calculate Daily Average:** kWh/day for each month
3. **Baseload Value:** Mean of shoulder-season daily rates

**2025 Calculation:**

```text
April: 11.2 kWh/day
May: 9.8 kWh/day
October: 8.1 kWh/day
Baseload = (11.2 + 9.8 + 8.1) ÷ 3 = 9.7 kWh/day
```

### HVAC Load Isolation

**Cooling Load (Summer):**

```text
Monthly Cooling kWh = Total kWh - (Baseload × days) - Furnace Blower kWh
```

**Heating Season Blower:**

```text
Blower kWh = Furnace Runtime Hours × Blower Power Draw
```

**Example (July 2025):**

```text
Total July kWh: 892 kWh
Baseload: 9.7 × 31 = 301 kWh
Furnace Blower: 0 kWh (no heating)
Cooling: 892 - 301 = 591 kWh
```

### Residual Category

**Definition:** Consumption not attributed to Baseload, AC, or Furnace Blower

**Calculation:**

```text
Residual = Total Annual kWh - Baseload - AC - Blower - Modeled Dehumidifier
```

**Diagnostic Value:** Residual is concentrated in April-October, suggesting unmeasured seasonal load (likely dehumidifier excess beyond modeled baseline).

---

## Building UA Calculation

### Input Parameters

1. **Total Delivered Heat (MMBTU):**
   - Furnace: Space Heating CCF × 100k BTU/CCF × AFUE
   - Fireplace: Independently measured via fuel consumption × efficiency

2. **Heating Degree Days (HDD):** Weather-normalized demand

3. **Balance Point:** Temperature below which heating is required

### Calculation Steps

**Step 1: Calculate Delivered Heat**

```text
Furnace Delivered = 599 CCF × 100k BTU/CCF × 0.96 AFUE = 57.5 MMBTU
Fireplace Delivered = 3.6 MMBTU (measured)
Total Delivered = 57.5 + 3.6 = 61.1 MMBTU
```

**Step 2: Adjust HDD for Balance Point**

```text
HDD65 (2025) = 6,270
Balance Point = 59°F (determined via regression)
HDD59 (2025) = 5,294 (recalculated from daily NOAA data)
```

**Step 3: Calculate UA**

```text
UA = Total Delivered Heat ÷ (24 hr/day × HDD)
UA = 61.1 MMBTU × 1,000,000 BTU/MMBTU ÷ (24 × 5,294)
UA = 61,100,000 ÷ 127,056
UA = 481 BTU/hr-°F ≈ 480 BTU/hr-°F
```

**Step 4: Area Normalization**

```text
UA/ft² = 480 ÷ 2,440 sq ft = 0.197 BTU/hr-°F-ft²
```

### Balance Point Determination

**Method:** HDD Neutral Band Optimization

**Process:**

1. Calculate UA at multiple balance points (55°F, 57°F, 59°F, 61°F, 63°F)
2. Select balance point that minimizes year-over-year UA variance
3. Validate against theoretical expectations (55-62°F typical for high-efficiency homes)

**Result:** 59°F balance point yields most stable UA across 2022-2025 dataset

---

## Statistical Validation

### Coefficient of Variation (CV)

**Definition:**

```text
CV = (Standard Deviation ÷ Mean) × 100%
```

**Application:**

Used to quantify baseline stability across 4-year dataset:

```text
Heating Intensity (CCF/1k HDD):
  Mean = 89.1
  Std Dev = 6.2
  CV = (6.2 ÷ 89.1) × 100% = 7.0%
```

**Interpretation:**

- CV < 5%: Exceptional stability
- CV 5-10%: Good stability
- CV > 10%: Investigate systematic variance

### Regression Analysis

**Applications:**

1. DHW baseline determination (CCF vs. HDD regression)
2. Balance point optimization (UA stability vs. balance point)
3. AC power verification (kWh vs. cooling degree days)

**Standard Metrics Reported:**

- R² (coefficient of determination)
- Slope and intercept with 95% confidence intervals
- Residual analysis for outlier detection

---

## Data Quality Controls

### 1. Billing Period Continuity Check

**Validation:**

```text
End Date (Bill N) = Start Date (Bill N+1) - 1 day
```

**Purpose:** Detect missing billing periods or data entry errors

### 2. Consumption Reasonableness Bounds

**Electricity:**

- Daily baseload: 5-15 kWh/day
- Summer peak: 20-40 kWh/day
- Winter peak: 15-30 kWh/day

**Natural Gas:**

- Daily DHW: 0.4-0.7 CCF/day
- Peak winter: 3-8 CCF/day

**Action:** Flag any billing period outside 2× normal range for manual review

### 3. HDD Cross-Validation

**Method:** Compare NOAA KBDL data against:

- Nearby weather stations (Bradley Field, Tweed-New Haven)
- Home Assistant local temperature sensors
- Expected HDD from historical climate normals

**Tolerance:** ±5% variance acceptable; >5% triggers investigation

---

## Limitations and Uncertainty

### Known Sources of Error

1. **DHW/Space Heating Separation:** ±10-15% uncertainty due to seasonal inlet temperature variation
2. **Fireplace Heat Contribution:** ±5% uncertainty in efficiency assumption (65-70%)
3. **Balance Point Determination:** ±1°F uncertainty in optimal value
4. **Dehumidifier Modeled Load:** ±20% uncertainty (unmetered equipment)

### Confidence Intervals

**Heating Intensity (95% CI):**

```text
2025: 95.5 ± 8.3 CCF/1k HDD
Range: 87.2 to 103.8 CCF/1k HDD
```

**Building UA (95% CI):**

```text
2025: 480 ± 35 BTU/hr-°F
Range: 445 to 515 BTU/hr-°F
```

---

## Software and Tools

### Data Processing Pipeline

1. **Raw Data Extraction:** Utility PDFs → CSV (manual or OCR)
2. **Weather Data:** NOAA API → daily temperature and HDD
3. **Billing Alignment:** Python pandas (custom script)
4. **Regression Analysis:** Python scipy.stats / R
5. **Visualization:** Matplotlib / ggplot2

### Reproducibility

All analysis scripts and raw data CSV files are available in the `/data` directory of this repository (if applicable). Key dependencies:

```python
pandas >= 1.5.0
numpy >= 1.23.0
scipy >= 1.9.0
matplotlib >= 3.6.0
```

---

## Future Enhancements

### Planned Improvements (v1.3.0)

1. **Circuit-Level Monitoring Integration:** Replace modeled dehumidifier load with actual CT measurements
2. **Fireplace Efficiency Calibration:** Install flue gas temperature sensor for real-time efficiency calculation
3. **DHW Recirculation Loss Isolation:** Independent metering of recirculation pump runtime
4. **Multi-Zone Temperature Logging:** Quantify cathedral ceiling stratification effects on UA

---

## References

1. **ASHRAE Fundamentals (2021):** Chapter 19 - Energy Estimating and Modeling Methods
2. **BPI Technical Standards:** Building Performance Institute, Inc. - Standard 2400-S-2013
3. **RESNET Standards:** ANSI/RESNET/ICC 301-2019 (Energy Calculation Methodology)
4. **NOAA Climate Data:** National Centers for Environmental Information (NCEI) API documentation

---

**Document Prepared By:** William K. Collis
**Methodology Review Status:** Validated against 4-year historical dataset (2022-2025)
**Last Calculation Update:** January 11, 2026
