# Changelog

All notable changes to the Residential HVAC Performance Baseline project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.1] - 2026-01-11

### Added
- Complete GitHub repository structure with README, documentation, and specifications
- METHODOLOGY.md with detailed billing-aligned calculation procedures
- DATA_SUMMARY.md for quick reference tables and metrics
- SYSTEM_SPECIFICATIONS.md with comprehensive equipment documentation
- CONTRIBUTING.md to guide community contributions
- LICENSE (MIT) for open-source sharing
- .gitignore for data protection

### Changed
- Refined DHW consumption methodology to billing-aligned approach (188 CCF vs. 220.8 CCF Navien meter reading)
- Improved statistical validation with 4-year coefficient of variation analysis (CV < 8%)
- Enhanced causal analysis of 2024→2025 efficiency variance (+19% heating intensity)
- Clarified electricity residual category (1,126 kWh + 294 kWh modeled = 1,420 kWh total moisture control)
- Added furnace runtime reconciliation (831 burner hours vs. 400 blower hours explanation)

### Fixed
- Resolved ambiguity in dehumidifier load attribution
- Corrected dehumidifier optimization savings estimate ($105 vs. previous $130)
- Added fireplace efficiency specification (65-70%) and fuel quantification (51-55 CCF)

---

## [1.2.0] - 2025-12-15

### Added
- Preliminary 2025 data integration
- Three-year comparative analysis (2022-2024)
- Enhanced HDD correlation methodology

### Changed
- Updated heating intensity baseline to 95.5 CCF/1k HDD (from 80.3 in 2024)
- Revised site EUI to 41.7 kBTU/ft²-yr

---

## [1.1.0] - 2024-01-10

### Added
- Two-year performance tracking (2022-2023)
- Initial weather normalization using KBDL HDD data
- Baseline electricity decomposition methodology

### Changed
- Refined UA calculation to include fireplace contribution
- Improved balance point estimation (59°F resolved)

---

## [1.0.0] - 2023-01-15

### Added
- Initial baseline established from 2022 data
- Building UA calculation (480 BTU/hr-°F)
- Equipment specifications documentation
- First-year performance metrics:
  - Heating Intensity: 89.8 CCF/1k HDD
  - Site EUI: 42.1 kBTU/ft²-yr
  - Total Electricity: 6,824 kWh

### Methodology
- Standard monthly allocation approach (later revised to billing-aligned in v1.2.1)
- Basic HDD normalization
- Equipment runtime tracking via Honeywell Lyric thermostat

---

## Version Numbering

**Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Fundamental methodology changes that affect year-over-year comparability
- **MINOR:** Annual data updates, new analysis sections, significant documentation enhancements
- **PATCH:** Clarifications, corrections, minor documentation improvements

---

## Future Versions (Planned)

### [1.3.0] - Expected January 2027
- 5-year comprehensive review (2022-2026)
- Integration of circuit-level energy monitoring data (if implemented)
- Dehumidifier dew point control optimization results
- Fireplace efficiency calibration with real-time measurements

### [2.0.0] - TBD (Major Equipment Replacement)
- Expected upon first major HVAC component replacement
- Will establish new baseline with updated equipment specifications
- Methodology may evolve to accommodate smart monitoring systems

---

## Links

- **Latest Release:** [v1.2.1](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/releases/tag/v1.2.1)
- **All Releases:** [Releases Page](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/releases)
- **Issues:** [Issue Tracker](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/issues)

---

**Maintained by:** [@wkcollis1-eng](https://github.com/wkcollis1-eng)
