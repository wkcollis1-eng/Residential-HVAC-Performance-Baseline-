# Residential HVAC Performance Baseline

**A Four-Year Longitudinal Study of High-Efficiency Residential Energy Systems in Climate Zone 5A**

[![DOI](https://img.shields.io/badge/Version-1.2.1-blue.svg)](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository documents a comprehensive energy performance baseline for a 2,440 sq. ft. high-efficiency residential structure in Central Connecticut (Climate Zone 5A). The analysis integrates four years of verified utility data (2022-2025), high-resolution HVAC runtime telemetry, and independent domestic hot water monitoring to establish diagnostic performance thresholds.

**Key Findings:**
- **Site EUI:** 41.7 kBTU/ft²-yr (33% better than regional average)
- **Heating Intensity:** 95.5 CCF/1k HDD (CV: 7.0% over 4 years)
- **Envelope UA:** 480 BTU/hr-°F (21-34% superior to 2021 IECC code-minimum)
- **Annual Electricity:** 6,730 kWh ($1,946)

## Repository Structure

```
├── BASELINE_REPORT.md          # Complete technical analysis
├── DATA_SUMMARY.md              # Quick-reference metrics and tables
├── METHODOLOGY.md               # Billing-aligned calculation methodology
├── SYSTEM_SPECIFICATIONS.md     # Equipment technical specifications
└── data/                        # Supporting datasets (if applicable)
```

## Purpose

This baseline serves multiple objectives:

1. **Anomaly Detection:** Establish investigation thresholds for future performance deviations
2. **Energy Monitoring ROI:** Quantify value proposition for circuit-level monitoring ($326 unresolved residual load)
3. **Contractor Communication:** Provide verifiable baseline for HVAC maintenance and upgrades
4. **Research Reference:** Document real-world performance of 2021-vintage high-efficiency systems

## Property Context

| Attribute | Specification |
|-----------|---------------|
| Location | Central Connecticut, Climate Zone 5A |
| Construction | 2021, Two-story Colonial |
| Conditioned Area | 2,440 sq. ft. |
| Occupancy | 2 residents |
| Primary Heating | American Standard Silver 95 (96% AFUE) condensing gas furnace |
| Primary Cooling | American Standard Silver 14 (4-ton, 14 SEER) split system |
| Moisture Control | Santa Fe Classic dehumidifier (110 PPD, 700W) |
| DHW | Navien NPE-series condensing tankless |

## Data Sources

- **Utility Billing:** Eversource (electricity), Southern Connecticut Gas (natural gas)
- **Weather:** Hartford Bradley International Airport (KBDL) NOAA data
- **HVAC Telemetry:** Honeywell Lyric T6 Pro thermostat runtime logs
- **DHW Monitoring:** Navien NaviLink independent gas meter
- **Analysis Period:** January 2022 - December 2025 (48 months)

## Methodology Highlights

This analysis employs a **Fully Billing-Aligned** approach that reconciles asynchronous utility meter read dates with calendar-year weather normalization. Key innovations include:

- HDD-neutral band optimization to resolve heating balance point (59°F)
- Billing-period electricity decomposition to isolate seasonal HVAC loads
- Multi-source heat accounting (furnace + fireplace) for UA derivation
- Statistical validation via 4-year coefficient of variation analysis

See [METHODOLOGY.md](METHODOLOGY.md) for complete calculation procedures.

## Key Performance Metrics

### Four-Year Statistical Summary

| Metric | 2025 Value | 4-Year Mean | Std Dev | CV (%) |
|--------|------------|-------------|---------|--------|
| Heating Intensity (CCF/1k HDD) | 95.5 | 89.1 | 6.2 | 7.0% |
| Annual Site EUI (kBTU/ft²-yr) | 41.7 | 40.8 | 2.1 | 5.1% |

### 2025 Baseline Thresholds

| Metric | Baseline Value | Investigation Threshold |
|--------|----------------|-------------------------|
| Annual Site EUI | 41.7 kBTU/ft²-yr | ±5% |
| Heating Intensity | 95.5 CCF/1k HDD | +10% |
| Moisture Control Load | ~1,420 kWh/season | >1,800 kWh |
| AC Power Draw | 4.9 kW | ±10% |

## Applications

### Current
- Justification for whole-house energy monitor investment (Fusion Solar 16-CT system)
- Diagnostic baseline for HVAC contractor communications
- Performance verification for high-efficiency equipment

### Future
- Template for residential energy auditing best practices
- Case study for Climate Zone 5A new construction performance
- Longitudinal tracking of equipment degradation curves

## Citation

If you use this methodology or data in your work, please cite:

```
Collis, W. K. (2026). Residential HVAC Performance Baseline: A Four-Year 
Longitudinal Study in Climate Zone 5A. GitHub Repository. 
https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-
```

## Contributing

This is a living baseline document. Contributions that improve methodology transparency, add supplementary analysis, or provide comparative datasets are welcome. See issues for current discussion topics.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contact

Technical questions and collaboration inquiries:
- **GitHub Issues:** [Open an issue](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/issues)
- **Repository Owner:** [@wkcollis1-eng](https://github.com/wkcollis1-eng)

---

**Version:** 1.2.1 (January 2026)  
**Status:** Active Baseline - Ongoing monitoring through 2026
