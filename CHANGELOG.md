# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.5.0] - 2026-03-16

### Added

- **`data/monthly_summary.csv`** — Derived monthly metrics table (15 rows, Jan 2025–Mar 2026)
  - Columns: Month, HDD65, Gas_CCF, DHW_CCF, Space_Heat_CCF, Heating_Intensity_CCF_1kHDD,
    Gas_Cost, Gas_CPP, Elec_kWh, Elec_Cost, Heat_1F_Hrs, Heat_2F_Hrs, Heat_Total_Hrs,
    Cool_1F_Hrs, Cool_2F_Hrs, Cool_Total_Hrs, Runtime_Per_HDD_Min, Zone_Balance_1F_Pct,
    DHW_Op_Hrs, DHW_Recirc_Hrs
  - Derived from all five source CSVs — single-file reference for validation and reporting
  - Heating_Intensity suppressed for months with HDD ≤ 100 (summer months)

- **`scripts/validate_month.py`** — Pre-commit monthly validation script
  - Implements V-HVAC-1 through V-HVAC-8 from CLAUDE.md
  - Checks: runtime/HDD ±2σ, heating efficiency ±15%, UA proxy ±5%, HDD vs normal,
    zone balance 45–55%, DHW YoY ≤ +5%, daily row count = days-in-month, runtime 2 rows/month
  - HALT-level failures block commit; FLAG-level require confirmation; exits 0/1 accordingly
  - Usage: `python3 scripts/validate_month.py [YYYY-MM-DD]`

- **`UPDATES.md`** — Consolidated monthly update log (replaces individual month files)
  - Newest month prepended to top; structured MoM/YoY tables per month
  - Contains January 2026, February 2026, and March 2026 updates

- **`CLAUDE.md`** — Machine-optimized session context for Claude Code
  - Canonical constants, CSV schemas, prohibited actions, monthly update procedure
  - References engineering-monthly-update skill
  - Includes sentinel comments in README for targeted metric updates

### Changed

- **`README.md`**
  - Added `<!-- METRICS_START -->` / `<!-- METRICS_END -->` sentinels around Key Findings block
  - Added `<!-- HIGHLIGHTS_START -->` / `<!-- HIGHLIGHTS_END -->` sentinels around monthly highlights
  - Updated directory listing to include new files; removed individual month file references
  - Monthly analysis link updated to `UPDATES.md`

### Notes

- `JANUARY_2026_UPDATE.md` and `FEBRUARY_2026_UPDATE.md` retained for backwards compatibility
  and GitHub Pages SEO; content now also available in `UPDATES.md`
- `monthly_summary.csv` is a derived file — do not edit manually; regenerate from source CSVs
  if source data changes

---

## [1.4.0] - 2026-03-01

### Added

- **February 2026 Data Integration**
  - Extended all datasets through February 28, 2026 (50 months total)
  - Added daily temperature data for February 2026 (28 days)
  - Added HVAC runtime data (158 heating hours)
  - Added DHW Navien monitoring (14.14 CCF)
  - Weather data sourced from timeanddate.com for Chester, CT (06424)

- **New Analysis Document**
  - `FEBRUARY_2026_UPDATE.md` - Complete MoM, YoY, and seasonal analysis
  - Early February cold snap analysis (Feb 7-9, 2026)
  - 2025-2026 heating season cumulative summary
  - DHW optimization continued validation

### Changed

- **Data Files Updated**
  - `daily_temperature.csv` - Added 28 February records
  - `monthly_hvac_runtime.csv` - Added Feb 2026 (1F: 72h, 2F: 86h)
  - `monthly_dhw_navien.csv` - Added Feb 2026 (14.14 CCF, 11 hrs, 28 recirc hrs)

### Validated

- **DHW Optimization Continues to Hold**
  - February 2026: 14.14 CCF vs 18.12 CCF Feb 2025 (-22.0%)
  - Recirculation hours: 28 vs 53 (-47.2%)
  - Cumulative Jan-Feb savings: 9.05 CCF (~$14.50)
  - On track for projected $77/year savings

- **System Performance**
  - Runtime efficiency: 8.8 min/HDD (19% better than 10.9 baseline)
  - Zone balance: 54.4% (within 50±5% target)
  - Heating intensity: 149.4 CCF/1kHDD (billing artifacts, runtime confirms health)

---

## [1.3.2] - 2026-02-02

### Added

- **January 2026 Data Integration**
  - Extended all datasets through January 31, 2026 (49 months total)
  - Added daily temperature data for January 2026 (31 days)
  - Added HVAC runtime data (220 heating hours)
  - Added DHW Navien monitoring (17.76 CCF)
  - Added utility billing data (168 CCF gas, 515 kWh electricity)

- **DHW Recirculation Optimization Documentation**
  - Schedule change: 24 hr/day → 15 hr/day (off 9 PM - 6 AM)
  - Measured impact: -22.2% DHW gas consumption
  - Key finding: 59% of DHW gas was recirculation standby (vs 23% factory estimate)
  - Projected annual savings: ~$77/year

- **New Analysis Document**
  - `JANUARY_2026_UPDATE.md` - Complete MoM, YoY, and 13-month analysis
  - Cold snap analysis (January 24-31, 2026)
  - Zone balance performance under extreme conditions
  - DHW optimization case study

- **Month-over-Month Metrics**
  - 13-month rolling comparisons for all utilities
  - Seasonal trend analysis
  - Zone balance tracking by month
  - Space heat vs DHW decomposition using Navien data

### Changed

- **Heating Intensity Baseline Corrected**
  - Old: 95.5 CCF/1kHDD (using estimated DHW)
  - New: 90.3 CCF/1kHDD (using Navien-metered DHW)
  - Reason: Navien monitoring shows actual DHW ~221 CCF/year vs 188 CCF estimate

- **Investigation Thresholds Updated**
  - Heating intensity warning: >99 CCF/1kHDD (was >105)
  - Added separate thresholds for space heating and DHW
  - Added note on using runtime efficiency for real-time validation

- **DATA_SUMMARY.md** updated to v1.3.2
  - Added DHW optimization section
  - Corrected baseline heating intensity
  - Added space heat vs DHW decomposition tables

- **README.md** updated to v1.3.2
  - Added DHW optimization highlight
  - Corrected key findings with Navien-metered values
  - Updated investigation thresholds

### Validated

- **Baseline Integrity Confirmed**
  - Heating intensity: 122.1 vs 121.8 CCF/1kHDD (+0.2% YoY)
  - Space heating: +8.7% tracks HDD +8.5% (perfect weather correlation)
  - Runtime efficiency: 10.7 min/HDD (vs 10.9 baseline)
  - Zone balance: 53.2% (within 50±5% target)
  - No equipment degradation indicators

---

## [1.2.1] - 2026-01-11

### Added

- Fully billing-aligned methodology implementation
- Four-year statistical validation (CV < 8%)
- Real-time monitoring integration (Home Assistant)
- REALTIME_MONITORING_2026.md documentation

### Changed

- DHW baseline adjusted to billing-aligned value (188 CCF vs 268 CCF)
- Heating intensity recalculated with precise billing periods
- Updated all annual summary tables

### Fixed

- Billing period misalignment in 2024 data
- DHW/space heating separation methodology

---

## [1.2.0] - 2025-12-15

### Added

- Preliminary 2025 annual data
- Dehumidifier load modeling (294 kWh identified, 1,126 kWh residual)
- Energy monitoring ROI analysis

### Changed

- Refined electricity decomposition methodology
- Updated investigation thresholds for 2026

---

## [1.1.0] - 2024-01-15

### Added

- Two-year dataset (2022-2023)
- Refined HDD correlation methodology
- Balance point determination (59°F)

### Changed

- Updated baseline metrics with 2023 data
- Improved regression analysis for DHW separation

---

## [1.0.0] - 2023-01-20

### Added

- Initial baseline established from 2022 data
- Core documentation structure
- Equipment specifications
- Methodology documentation

---

## Data Files Updated in v1.4.0

| File | Previous End | Current End | Records Added |
|------|--------------|-------------|---------------|
| daily_temperature.csv | 2026-01-31 | 2026-02-28 | 28 days |
| monthly_hvac_runtime.csv | 2026-01 | 2026-02 | 2 records (zones) |
| monthly_dhw_navien.csv | 2026-01 | 2026-02 | 1 record |
| monthly_gas_scg.csv | 2026-01 | 2026-02 | Pending utility bill |
| monthly_electricity_eversource.csv | 2026-01 | 2026-02 | Pending utility bill |

---

## Key Metrics Comparison

| Version | Data Period | Heating Intensity | Site EUI | CV |
|---------|-------------|-------------------|----------|-----|
| v1.0.0 | 2022 | 89.8 | 42.1 | — |
| v1.1.0 | 2022-2023 | 90.3 | 41.5 | 5.1% |
| v1.2.0 | 2022-2024 | 86.9 | 40.4 | 6.2% |
| v1.2.1 | 2022-2025 | 89.1 | 40.8 | 7.0% |
| v1.3.2 | 2022-2026* | 89.1 | 40.8 | 7.0% |
| **v1.4.0** | **2022-2026*** | **89.1** | **40.8** | **7.0%** |

*Through February 2026; annual metrics unchanged until full year complete

---

## Upcoming (Planned)

### [1.5.0] - Expected April 2026

- Post-winter 2025-2026 season summary
- March 2026 data integration
- Complete heating season analysis
- Dehumidifier season ramp-up validation

### [2.0.0] - Expected January 2027

- Five-year comprehensive baseline review
- Statistical analysis update with full 2026 data
- Potential methodology refinements
- Equipment lifecycle review (5-year checkpoint)
