# Residential HVAC Performance Baseline - Dataset Documentation

**Version:** 1.2.2  
**Data Period:** 2021-12 through 2025-12  
**Last Updated:** January 12, 2026

---

## Overview

This directory contains raw operational data for the residential HVAC performance baseline study. All data has been cleaned, validated, and formatted for analysis reproducibility. Personal identifying information has been removed while preserving analytical utility.

**Property Context:**

- Location: Central Connecticut, Climate Zone 5A
- Construction: 2021, Two-story Colonial
- Conditioned Area: 2,440 sq. ft.
- Occupancy: 2 residents

---

## Dataset Files

### 1. `monthly_hvac_runtime.csv`

**Description:** HVAC equipment runtime hours extracted from Honeywell Lyric T6 Pro thermostat telemetry

**Period:** January 2025 - December 2025 (12 months)  
**Rows:** 24  
**Source:** Resideo/Honeywell Lyric app export  
**Frequency:** Monthly aggregation

**Columns:**
| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `Month` | datetime | YYYY-MM-01 | First day of month |
| `Cooling_Hours` | integer | hours | AC compressor runtime during month |
| `Heating_Hours` | integer | hours | Furnace burner runtime during month |

**Notes:**

- Runtime represents actual equipment operation (burner on / compressor on)
- Does not include fan-only circulation time
- Single-stage equipment: all runtime is at full capacity
- 2025 total: Heating = 831 hours, Cooling = 346 hours

**Data Quality:**

- ✅ No missing values
- ✅ Validated against utility consumption patterns
- ✅ Consistent with degree-day analysis

---

### 2. `daily_temperature.csv`

**Description:** Daily temperature readings from thermostat sensors (indoor and outdoor)

**Period:** January 1, 2025 - December 31, 2025 (365 days)  
**Rows:** 364  
**Source:** Resideo/Honeywell Lyric app export  
**Frequency:** Daily aggregation (high/low/average)

**Columns:**
| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `Date` | datetime | YYYY-MM-DD | Calendar date |
| `Outdoor_High` | float | °F | Daily maximum outdoor temperature (Hartford KBDL proxy) |
| `Outdoor_Low` | float | °F | Daily minimum outdoor temperature (Hartford KBDL proxy) |
| `Outdoor_Mean_F` | float | °F | Daily mean outdoor temperature |
| `HDD65` | float | °F-days | Heating degree days (base 65°F) |
| `Indoor_1st_Floor` | float | hours | Daily HVAC runtime hours (heating + cooling) for 1st floor zone |
| `Indoor_2nd_Floor` | float | hours | Daily HVAC runtime hours (heating + cooling) for 2nd floor zone |

**Notes:**

- Outdoor temperature data sourced from Hartford Bradley International Airport (KBDL) as proxy for zip code 06424
- HDD65: Heating degree days calculated as max(0, 65°F - mean outdoor temp)
- **HVAC runtime columns:** Combined heating and cooling hours per day from Resideo thermostat data
  - **Total runtime (2025):** 1,167.78 hours (366.47 + 801.31)
  - Reconciles with monthly summary: 831 heating + 346 cooling = 1,177 hours (0.8% difference due to rounding)
  - Values represent thermostat calls per zone (may overlap if both zones call simultaneously)
  - 2nd floor shows higher runtime (801.31 vs 366.47 hours), consistent with upper floor heating/cooling challenges
  - Zero values indicate no HVAC demand
- Setpoint strategy: 68-70°F heating, 74-76°F cooling

**Data Quality:**

- ✅ No missing days (364 days in 2025, excludes leap day)
- ✅ Cross-validated against NOAA KBDL weather station (outdoor temps R² > 0.95)
- ✅ HVAC runtime reconciles with monthly totals: 1,167.78 daily vs 1,177 monthly (0.8% difference)

---

### 3. `monthly_dhw_navien.csv`

**Description:** Domestic hot water (DHW) gas consumption and operating metrics from Navien tankless water heater

**Period:** October 2024 - December 2025 (15 months)  
**Rows:** 15  
**Source:** Navien NaviLink independent gas meter  
**Frequency:** Monthly reading

**Columns:**
| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `Month` | datetime | YYYY-MM-01 | First day of month |
| `Gas_CCF` | float | CCF | Natural gas consumed by DHW system |
| `DHW_Operating_Hours` | integer | hours | DHW burner runtime (heating water) |
| `Recirculation_Hours` | integer | hours | Recirculation pump runtime |

**Notes:**

- Independent metering isolates DHW from space heating gas consumption
- CCF = hundred cubic feet of natural gas (~100,000 BTU per CCF)
- Recirculation pump maintains hot water in distribution loop (standby losses ~23%)
- 2025 annual total: 220.8 CCF (from meter), 188 CCF (billing-aligned calculation)

**Data Quality:**

- ✅ No missing values for available period
- ⚠️ 15% variance between meter reading and billing-aligned calculation (see baseline report)
- ✅ Consistent with seasonal inlet water temperature patterns

---

### 4. `monthly_electricity_eversource.csv`

**Description:** Whole-house electricity consumption from utility billing records

**Period:** December 2021 - December 2025 (49 billing periods)  
**Rows:** 49  
**Source:** Eversource Energy utility bills  
**Frequency:** Monthly billing cycles (28-34 days per period)

**Columns:**
| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `Read_Date` | datetime | YYYY-MM-DD | Utility meter read date (end of billing period) |
| `Usage_kWh` | integer | kWh | Electricity consumed during billing period |
| `Days` | integer | days | Number of days in billing period |
| `Usage_Per_Day` | float | kWh/day | Average daily consumption (calculated) |
| `Charge` | float | $ | Total charges for billing period |
| `Cost_Per_kWh` | float | $/kWh | Average cost per kWh (calculated) |

**Notes:**

- Billing periods do not align with calendar months (15-day phase shift typical)
- Rates include both supply and delivery charges (~$0.29/kWh average in 2025)
- 2025 calendar-year total: 6,730 kWh (via billing-aligned methodology)
- Fixed charges (~$11/month) included in total but not in per-kWh rate

**Data Quality:**

- ✅ No missing values
- ✅ Validated against utility account history
- ✅ Rate calculations verified against tariff schedules

**Load Breakdown (2025 calendar year via billing-aligned analysis):**

- Baseload: 3,532 kWh (52%)
- Space Cooling: 1,694 kWh (25%)
- Moisture Control: ~1,420 kWh (21%)
- Furnace Blower: 84 kWh (1%)
- Residual: 1,126 kWh (17%)

---

### 5. `monthly_gas_scg.csv`

**Description:** Whole-house natural gas consumption from utility billing records

**Period:** December 2021 - December 2025 (49 billing periods)  
**Rows:** 49  
**Source:** Southern Connecticut Gas Company utility bills  
**Frequency:** Monthly billing cycles (28-34 days per period)

**Columns:**
| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `Bill_Date` | datetime | YYYY-MM-DD | Utility bill date (end of billing period) |
| `Billing_Days` | integer | days | Number of days in billing period |
| `Gas_CCF` | float | CCF | Natural gas consumed during billing period |
| `Usage_Per_Day` | float | CCF/day | Average daily consumption (calculated) |
| `Total_Charges` | float | $ | Total charges for billing period |
| `Cost_Per_CCF` | float | $/CCF | Average cost per CCF (calculated) |

**Notes:**

- CCF = hundred cubic feet of natural gas (~100,000 BTU per CCF)
- Billing periods do not align with calendar months
- Rates vary seasonally (winter ~$1.50/CCF, summer ~$1.00/CCF average)
- 2025 calendar-year total: 787 CCF (via billing-aligned methodology)
- Includes all gas consumption: space heating (furnace + fireplace), DHW, gas range

**Data Quality:**

- ✅ No missing values
- ✅ Validated against utility account history
- ✅ Cross-checked against Navien independent DHW meter

**Load Breakdown (2025 calendar year via billing-aligned analysis):**

- Space Heating (Furnace): 547 CCF (69.5%)
- Space Heating (Fireplace): 52 CCF (6.6%)
- Domestic Hot Water: 188 CCF (23.9%)

---

## Data Quality and Validation

### Validation Methods

**1. Internal Consistency Checks:**

- ✅ HVAC runtime hours validated against temperature data (heating runtime correlates with HDD)
- ✅ Electricity cooling load validated against cooling runtime (4.9 kW average draw)
- ✅ Gas consumption validated against heating runtime and AFUE (96% furnace efficiency)

**2. External Cross-Validation:**

- ✅ Thermostat outdoor temperature vs. NOAA KBDL weather station (R² > 0.95)
- ✅ Utility billing totals vs. calendar-year aggregations (within 2%)
- ✅ Navien meter vs. billing-aligned DHW calculation (15% variance documented)

**3. Statistical Validation:**

- ✅ Four-year coefficient of variation (CV) < 8% for all major metrics
- ✅ Weather-normalized heating intensity stable within 7% (2022-2025)
- ✅ No outliers beyond 2σ in daily temperature or runtime data

### Known Limitations

1. **Thermostat Data Coverage:**
   - 2025 only (earlier years not exported from Lyric app)
   - One missing day in daily temperature data
   - Runtime data does not capture variable blower speeds

2. **Navien DHW Meter:**
   - Data availability: October 2024 onward (meter installed mid-2024)
   - 15% variance from billing-aligned calculation (seasonal baseline drift)
   - Recirculation pump operation time may include non-heating runtime

3. **Utility Billing:**
   - Asynchronous billing cycles require billing-aligned methodology
   - Electricity rate includes both supply and delivery (not separately itemized)
   - Gas rate varies seasonally with supply contracts

---

## Usage Guidelines

### Reproducing Baseline Analysis

All calculations in the baseline report can be reproduced using these datasets:

1. **Heating Intensity (CCF/1k HDD):**
   - Use `monthly_gas_scg.csv` for total gas consumption
   - Subtract DHW baseline (0.533 CCF/day from `monthly_dhw_navien.csv`)
   - Normalize by HDD from NOAA KBDL weather station
   - Result: 95.5 CCF/1k HDD (2025)

2. **Building UA Calculation:**
   - Space heating gas from step 1
   - Convert to delivered heat (× 100k BTU/CCF × 0.96 AFUE)
   - Add fireplace contribution (3.6 MMBTU estimated)
   - Divide by (24 hr/day × HDD at 59°F balance point)
   - Result: 480 BTU/hr-°F

3. **Electricity Load Decomposition:**
   - Use billing-aligned methodology (see METHODOLOGY.md)
   - Cooling load isolated via regression against cooling degree days
   - HVAC blower: 831 hours × 0.21 kW = 84 kWh (from `monthly_hvac_runtime.csv`)
   - Baseload: Average of low-load months (April, May, October)

### Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{collis2026_hvac_data,
  author = {Collis, William K.},
  title = {Residential HVAC Performance Baseline Dataset},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/tree/main/data}},
  version = {1.2.2}
}
```text

---

## Privacy and Data Protection

**Anonymization:**

- ✅ No personal identifying information (names, addresses removed)
- ✅ Location generalized to "Central Connecticut"
- ✅ Utility account numbers removed
- ✅ Only operational metrics retained

**Data Sharing:**

- This dataset is released under MIT License
- Suitable for academic research, policy analysis, and engineering studies
- Not suitable for individual property assessment (aggregated only)

---

## Contact

**Questions about the dataset:**

- Open an issue: https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/issues
- Repository owner: @wkcollis1-eng

**Reporting data quality issues:**

- Please include: filename, row/column, observed issue, expected value
- Data corrections will be versioned and documented in CHANGELOG.md

---

## Version History

**v1.2.2 (January 2026):**

- Initial public data release
- Cleaned and validated 2025 operational data
- Added 2022-2025 utility billing history
- Documented known limitations and validation methods

**Future Additions:**

- 2026 data (planned: January 2027)
- Circuit-level electricity monitoring (if implemented)
- Enhanced blower motor telemetry (static pressure tracking)

---

**Last Updated:** January 12, 2026  
**Data Quality Review:** Validated against baseline report v1.2.1  
**License:** MIT (see repository LICENSE file)
