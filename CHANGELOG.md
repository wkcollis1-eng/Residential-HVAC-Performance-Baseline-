# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- **July-September 2026 monthly reports (2026-10-15)** - `JULY_2026_UPDATE.md` (1.8.2),
  `AUGUST_2026_UPDATE.md` (1.8.3) and `SEPTEMBER_2026_UPDATE.md` (1.9.0). Degree days are ACIS
  Bradley (BDL) HDD65/CDD65 throughout; the HA proxy is secondary. September adds the 2025
  Honeywell T6 Pro vs 2026 Ecobee cooling-season review (June-September): daily-fit runtime
  slope 25.96 -> 19.91 min/CDD, difference -6.05, 95% CI [-11.06, -1.37], p ~ 0.010 [D,
  week-block bootstrap, B=5000]; season ratio 25.54 -> 22.52 min/CDD, p ~ 0.29, not significant
  [D]. Not attributed to the thermostat: year and controller are confounded, and the 2025
  setpoints, system mode and 2F vent position are unrecorded. README 1.7.0 and UPDATES.md carry
  the summaries.

- **Data rows for slots 2026-07..09** - appended only; CRLF; prior bytes verified unchanged.
  - `monthly_gas_scg.csv` 13 / 8 / 8 CCF; `monthly_electricity_eversource.csv` 966 / 724 /
    474 kWh ($210.69 / $175.22 / $118.05); `monthly_dhw_navien.csv` 8.39 / 5.59 / 8.39 CCF [M,
    HA archives].
  - `monthly_hvac_runtime.csv` cooling 121.6 / 70.3 / 20.8 h, from the HA monthly accumulator
    (`hvac_monthly.csv`, the source of truth). July's 121.6 h includes Jul 4-5 (grid outage),
    which have no daily rows; the reports' July runtime per CDD uses the 29 logged days
    (113.61 h / 256 CDD [D]).
  - `monthly_summary.csv` three rows. The HDD65 column stays the HA proxy for continuity;
    Space_Heat = Gas - DHW even when negative (September -0.39 CCF, as in the 2025-09 row).

- **First measured cooling energy** - SEM AC circuit, compressor 332.8 / 180.9 / 50.6 kWh
  Jul / Aug / Sep [M]; 0.925 kWh/CDD over Jul-Sep [D: 564.3 / 610].

- **Metrics** - 12-month electricity 6,468 -> 6,004 kWh (Oct 2025-Sep 2026 bills [D]); 12-month
  site EUI 41.8 -> 41.7 kBTU/ft2-yr [D: (784 x 103.7 + 6,004 x 3.412) / 2,440]; DHW Jan-Sep
  156.63 -> 101.01 CCF, -35.5% [D: 101.01 / 156.63 - 1, both years in CCF].

- **Bill's 2026-10-15 answers recorded** - `SEPTEMBER_2026_UPDATE.md`, `README.md`, `UPDATES.md`
  and `SYSTEM_SPECIFICATIONS.md` carry dated notes; published text is not rewritten. Summer vents
  were all 100% open, so vent position is not a summer confound. The only base-load changes were
  the DHW recirculation and the office computer's overnight shutdown and sleep modes; how the drop
  splits between them is unmeasured. No 2025 cycle data exists, so 2025 runtime per cycle is closed
  as unmeasurable. The condenser is model 4A7A4048L1000AA. Still open: 2025 vs 2026 setpoints and
  schedules, the September 2025 system mode, and RLA / voltage.

### Fixed

- **DHW therms stored as CCF (2026-10-15, Bill: "fix old data")** - `monthly_dhw_navien.csv`
  2024-10..2026-01 (16 cells) and `monthly_summary.csv` DHW_CCF 2025-01..2026-01 (13 cells) held the
  Navien export's Thm values (each an integer m³ × 0.36245). They are now CCF = Thm × 0.9643, 4 dp.
  2025-06 (16.723) passes neither the therm nor the CCF test and was converted as Thm, its source
  column. Space_Heat_CCF and Heating_Intensity_CCF_1kHDD were recomputed with the formulas that
  reproduce every existing cell (Gas - DHW to 2 dp; / HDD65 x 1000 to 1 dp, blank under 100 HDD).
  2025 meter total 220.8 Thm = 212.9 CCF [D]. `validate_month.py` V-HVAC-6 now compares CCF with
  CCF: -44.2% / -48.4% / -44.2% for Jul / Aug / Sep 2026 [D], as the reports state.

- **2025 zone swap (2026-10-15)** - `monthly_summary.csv` had Cool_1F/Cool_2F swapped for 2025-06..09
  and Heat_1F/Heat_2F swapped for 2025-10..11; `monthly_hvac_runtime.csv` had the same months' row
  pairs in 2F, 1F order. Both now match the Resideo export's monthly sheet floor by floor for all
  twelve 2025 months, and its daily sums agree. Zone_Balance_1F_Pct Oct / Nov 2025: 69.7 / 62.1 ->
  30.3 / 37.9 [D], the values `JANUARY_2026_UPDATE.md` already published. Totals and runtime/HDD are
  unchanged. `UPDATES.md` carried 69.7 / 62.1 and gets a dated correction note.

- **Bill CSV month labels (2026-10-15)** - the 50 unquoted rows of `monthly_electricity_eversource.csv`
  and `monthly_gas_scg.csv` are relabelled to the month of their read / bill date, taken from the
  Resideo workbook's Monthly Utilities sheet with every value asserted equal. That is the convention
  the quoted 2026-02+ rows and `monthly_summary.csv` already use. Electricity: 50 labels moved one
  month later. Gas: 46 moved; the 2023-01, 2023-07, 2024-01 and 2024-09 bills already carried their
  bill month, which had left duplicate labels there. Both files now run 2021-12..2026-09, 58 unique
  contiguous months, and match the summary's Gas_CCF / Elec_kWh for all 21 shared months [M]. No
  value changed. `validate_month.py` keys gas by this label, so its gas lookups are now slot-aligned
  and 2026-01 V-HVAC-2/3 run (they WARNed "missing gas"). Its all-months counts went WARN 22 -> 19,
  FLAG 18 -> 21, PASS 119 and HALT 8 unchanged [M, run before and after this commit]; Known issues
  says why the 2025 shoulder months moved.

- **`daily_temperature.csv` onto BDL, extended to 2026-09-30 (2026-10-15, Bill: "fix ... daily
  temps")** - the 2025 rows already equal ACIS BDL (364 of 364 [M]). The 57 Jan / Feb 2026 rows
  whose outdoor cells came from another source (25 had a mean that was not (High + Low) / 2) now
  carry BDL values: HDD65 Jan 1,229.9 -> 1,270.0, Feb 1,089.0 -> 1,126.5 [D]. 2025-02-24, absent
  from the Resideo export, is inserted with BDL temperatures and blank runtime. 2026-03-01..09-30
  (214 rows) are appended: BDL temperatures; runtime hours = (runtime + cool_runtime minutes) / 60
  from Home Assistant `hvac_daily_2026.csv`, the rule that reproduces 31 of the 31 existing rows it
  covers [M]; blank on the 9 days HA has no row (2026-05-16..22, 07-04, 07-05). The file is now 638
  contiguous days; 366 of the 423 existing lines are byte-identical and the other 57 changed only
  in outdoor cells. `validate_month.py` now exits 0: HALT 8 -> 0, PASS 119 -> 126, WARN 19 -> 14,
  FLAG 21 -> 27 [M]. The new FLAGs are Mar-May 2026 checks running for the first time
  (V-HVAC-2 Mar-May, the billing artifact under Known issues; V-HVAC-1 and -3 Mar; V-HVAC-5 May).

### Known issues (flagged, not corrected - each needs Bill's approval and a separate commit)

- **The 2026-10-10 baseline uses the therm figure as CCF.** 566.2 CCF = 787 - 220.8, and 220.8 is
  therms. In CCF the 2025 space heat is 574.1 [D: 787 - 212.9], heating intensity 102.0 CCF/1k HDD65
  [D: 574.1 / 5.629] vs 100.6, and UA 593 [D, METHODOLOGY formula] vs 585. `BASELINE_REPORT.md`,
  `METHODOLOGY.md`, `DATA_SUMMARY.md`, `SYSTEM_SPECIFICATIONS.md`, `validate_month.py`
  (BASELINE_EFFICIENCY) and the Home Assistant helpers still carry 566.2 / 100.6 / 585. Rebasing
  is Bill's call; nothing was changed.

- Compressor draw is 2.725 +/- 0.020 kW per call-hour [D, n=90 days, R2 0.995]. That conflicts
  with "Measured Power Draw: 4.9 kW" in `SYSTEM_SPECIFICATIONS.md`, and so with the 1,694 kWh
  2025 cooling baseline in `BASELINE_REPORT.md`. Both stay unchanged until the condenser
  nameplate is read. *2026-10-15:* Bill supplied the model, 4A7A4048L1000AA (s/n 21014S4Y3F),
  which matches the spec file, but no RLA or voltage. The repo has no measurement record for
  4.9 kW (`BASELINE_REPORT.md` calls it "at rated conditions"); `SYSTEM_SPECIFICATIONS.md` now
  carries a dated note. Still open.
- `monthly_summary.csv` 2026-02 Heat_1F/Heat_2F (72 / 86 h) split furnace runtime (158.2 h), while
  the daily zone sums are 86.4 / 99.2 h [M, `daily_temperature.csv`]; other months hold zone hours.
  2026-03 Zone_Balance_1F_Pct reads 49.6 where 40 / 81.4 gives 49.1 [D]. Not changed.
- `validate_month.py` V-HVAC-2/3 divide one bill (mid-month to mid-month) by calendar-month HDD65,
  so in shoulder months the verdict follows the label convention, not the house. After the bill
  CSV relabel, 2025 V-HVAC-2 went PASS -> FLAG for Feb-Apr and FLAG -> PASS for Dec; V-HVAC-3 went
  FLAG -> PASS or WARN for Mar-May and PASS or WARN -> FLAG for Oct-Dec [M, validate_month output
  before and after]. HDD65 summed over each billing period from the ACIS daily series would remove
  the artifact. Not changed.
- HDD65 has three bases in `data/`. ACIS BDL publishes daily HDD65 rounded to whole degree-days,
  and its monthly sums are the reference the reports and the 5,629 baseline use.
  `daily_temperature.csv` holds 65 - (High + Low) / 2 unrounded from the same BDL highs and lows, so
  its sums run 0-8 HDD a month above ACIS, 5,696 vs 5,629 for 2025 [D]. `monthly_summary.csv`
  HDD65 is the unrounded daily sum for 2025 (2025-02 939.5 omits the then-missing 2025-02-24),
  the replaced non-BDL daily rows for 2026-01 / 02 (1,229.9 / 1,089.0 vs BDL 1,263 / 1,120), and
  neither for 2026-03..09 (e.g. Apr 472.3 vs BDL 412) [D]. Its Heating_Intensity and
  Runtime_Per_HDD follow. Rebasing that column to ACIS monthly is Bill's call; not changed.

### Changed

- **Baselines rebased to ACIS Bradley 2025 (2026-10-10)** - Heating intensity 90.3 -> 100.6 CCF/1k HDD65,
  UA 480 (493 corrected) -> 585 BTU/hr-°F, HDD59/HDD65 ratio 0.844 -> 0.751, 2025 HDD65 6,270 (NOAA) ->
  5,629 (ACIS BDL [M]). Intensity keeps the Navien-corrected 566.2 CCF, so only its degree-day source
  changed; UA also moves from the billing-aligned 599 CCF to 566.2. README, DATA_SUMMARY and
  CLAUDE_Monthly_Report carry the new values; BASELINE_REPORT and METHODOLOGY keep their as-published
  figures, with dated rebase notes and the derivation. `Scripts/validate_month.py` V-HVAC-2 checks
  against 100.6; V-HVAC-3 keeps its own 480 (a different formula). The margin under the 2021 IECC
  code-minimum UA becomes 4-19% [D], from 21-34%.

- **`SYSTEM_SPECIFICATIONS.md`** - Basement dehumidifier is now the Aprilaire E080 (in service 2026-08),
  free-standing, condensate to a pump shared with the Navien. Rated and measured figures carry
  provenance tags; water removed is not measured. The Santa Fe Classic section is kept as the
  retired unit, with the outcome of its proposed dew-point control. Lifecycle row updated;
  document version 1.2.2.

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
