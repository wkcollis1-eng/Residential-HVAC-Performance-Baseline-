# Data Summary: Quick Reference Tables

**Version:** 1.2.1  
**Period:** 2022-2025 (4 years)  
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut

---

## Performance Summary (2025 Baseline)

| Metric | Value | Unit | Benchmark |
|--------|-------|------|-----------|
| **Site Energy Use Intensity (EUI)** | 41.7 | kBTU/ft²-yr | Regional Avg: ~62 kBTU/ft²-yr |
| **Heating Intensity** | 95.5 | CCF/1k HDD | Regional Avg: 145 CCF/1k HDD |
| **Building UA** | 480 | BTU/hr-°F | IECC 2021: 610-725 BTU/hr-°F |
| **Heating Balance Point** | 59 | °F | Typical: 55-62°F |
| **Annual Electricity** | 6,730 | kWh | National Avg (2-person): 8,500 kWh |
| **Annual Natural Gas** | 787 | CCF | — |
| **Total Energy Cost** | $2,946 | $ | Electricity: $1,946 / Gas: $1,000 |

---

## Four-Year Historical Performance

### Annual Energy Consumption

| Year | HDD65 | Total Gas (CCF) | Space Heat (CCF) | DHW (CCF) | Electricity (kWh) |
|------|-------|-----------------|------------------|-----------|-------------------|
| 2022 | 6,092 | 815 | 547 | 268 | 6,824 |
| 2023 | 5,465 | 764 | 496 | 268 | 6,591 |
| 2024 | 5,305 | 694 | 426 | 268 | 6,543 |
| 2025 | 6,270 | 787 | 599 | 188* | 6,730 |

*DHW adjusted to billing-aligned methodology (v1.2.1)

### Weather-Normalized Efficiency

| Year | Heating Intensity (CCF/1k HDD) | Site EUI (kBTU/ft²-yr) | % Better Than Regional |
|------|-------------------------------|------------------------|------------------------|
| 2022 | 89.8 | 42.1 | 38% |
| 2023 | 90.8 | 40.8 | 37% |
| 2024 | 80.3 | 38.2 | 45% |
| 2025 | 95.5 | 41.7 | 34% |
| **4-Yr Mean** | **89.1** | **40.8** | **38%** |
| **Std Dev** | **6.2** | **2.1** | — |
| **CV (%)** | **7.0%** | **5.1%** | — |

---

## 2025 Electricity Decomposition

| End Use | Annual kWh | Daily Avg | % of Total | Annual Cost |
|---------|------------|-----------|------------|-------------|
| **Baseload** | 3,532 | 9.7 kWh/day | 52% | $1,021 |
| **Space Cooling** | 1,694 | 4.6 kWh/day* | 25% | $490 |
| **Furnace Blower** | 84 | 0.23 kWh/day* | 1% | $24 |
| **Dehumidifier (Modeled)** | 294 | 0.81 kWh/day* | 5% | $85 |
| **Residual (Unresolved)** | 1,126 | 3.1 kWh/day* | 17% | $326 |
| **Total** | **6,730** | **18.4 kWh/day** | **100%** | **$1,946** |

*Daily average includes zero-load periods (seasonal equipment)

### Seasonal Load Distribution

| Season | Months | Primary Loads | Total kWh | Avg kWh/day |
|--------|--------|---------------|-----------|-------------|
| **Winter** | Dec-Feb | Baseload + Blower | 1,586 | 17.4 |
| **Spring** | Mar-May | Baseload + Dehumidifier ramp-up | 1,652 | 18.0 |
| **Summer** | Jun-Aug | Baseload + AC + Dehumidifier | 2,214 | 24.1 |
| **Fall** | Sep-Nov | Baseload + Dehumidifier ramp-down | 1,278 | 14.0 |

---

## 2025 Natural Gas Decomposition

| End Use | Annual CCF | % of Total | Annual Cost | Efficiency |
|---------|------------|------------|-------------|------------|
| **Space Heating (Furnace)** | 547 | 69.5% | $912 | 96% AFUE |
| **Space Heating (Fireplace)** | 52 | 6.6% | $87 | 65-70% |
| **Domestic Hot Water** | 188 | 23.9% | $313 | 95% AFUE |
| **Total** | **787** | **100%** | **$1,312** | — |

**Note:** Total cost includes delivery charges and fees ($1,000 actual bill vs. $1,312 commodity cost)

---

## Building Thermal Performance

### Envelope Metrics

| Parameter | Value | Unit | Industry Comparison |
|-----------|-------|------|---------------------|
| **Building Load Coefficient (UA)** | 480 | BTU/hr-°F | — |
| **Area-Normalized UA** | 0.197 | BTU/hr-°F-ft² | — |
| **Heating Balance Point** | 59 | °F | Typical: 55-62°F |
| **IECC 2021 Code UA (est.)** | 610-725 | BTU/hr-°F | 21-34% worse |
| **Total Heat Delivered (2025)** | 61.1 | MMBTU | Furnace: 57.5 / Fireplace: 3.6 |

### Heat Loss Breakdown (Estimated)

| Component | Est. % of Total UA | Notes |
|-----------|-------------------|-------|
| **Walls** | 35-40% | Continuous exterior foam insulation |
| **Windows** | 20-25% | U-0.27 to U-0.30 performance |
| **Ceiling/Attic** | 15-20% | R-49 to R-60 blown insulation |
| **Foundation** | 10-15% | Heated basement (R-15 walls) |
| **Air Infiltration** | 10-15% | Estimated <3 ACH50 |

---

## HVAC Equipment Runtime (2025)

| Equipment | Total Runtime | Avg Daily Runtime | Seasonal Window |
|-----------|---------------|-------------------|-----------------|
| **Furnace Burner** | 831 hours | 2.3 hrs/day (heating season) | Nov-Apr |
| **Furnace Blower** | 400 hours* | 1.1 hrs/day (heating season) | Nov-Apr |
| **Air Conditioner** | 346 hours | 1.9 hrs/day (cooling season) | Jun-Sep |
| **Dehumidifier** | ~2,030 hours** | 9.7 hrs/day (humid season) | Apr-Oct |

*Effective full-load hours at 0.21 kW  
**Estimated from 1,420 kWh at 700W = 2,029 hours (~50% duty cycle)

---

## Investigation Thresholds

### Performance Degradation Triggers

| Metric | 2025 Baseline | Warning (+5-10%) | Action (>10%) |
|--------|---------------|------------------|---------------|
| **Heating Intensity** | 95.5 CCF/1k HDD | >100 CCF/1k HDD | >105 CCF/1k HDD |
| **Site EUI** | 41.7 kBTU/ft²-yr | >43.8 kBTU/ft²-yr | >45.9 kBTU/ft²-yr |
| **AC Power Draw** | 4.9 kW | >5.2 kW | >5.4 kW |
| **Furnace Blower Power** | 0.21 kW (210W) | >0.25 kW (250W) | >0.32 kW (320W) |
| **Dehumidifier Season Load** | 1,420 kWh | >1,600 kWh | >1,800 kWh |

### Diagnostic Actions by Threshold

**Warning Threshold (+5-10%):**
- Review recent weather severity (adjust for HDD variance)
- Check thermostat setpoint history
- Inspect air filter condition
- Verify no new occupancy changes

**Action Threshold (>10%):**
- Schedule HVAC contractor diagnostic
- Perform blower door test (envelope integrity)
- Check refrigerant charge (AC)
- Investigate duct leakage
- Review utility billing for errors

---

## Utility Rate Structure (2025)

### Electricity (Eversource)

| Component | Rate | Annual Charge |
|-----------|------|---------------|
| **Energy Supply** | $0.14/kWh | $942 |
| **Delivery** | $0.13/kWh | $875 |
| **Fixed Charges** | $11/month | $132 |
| **Total** | **~$0.29/kWh** | **$1,946** |

### Natural Gas (Southern Connecticut Gas)

| Component | Rate | Annual Charge |
|-----------|------|---------------|
| **Commodity** | $1.05/CCF | $826 |
| **Delivery** | ~$0.22/CCF | $173 |
| **Fixed Charges** | $14/month | $168 |
| **Total** | **~$1.27/CCF** | **$1,167** |

**Note:** Rates are approximate averages; actual bills include variable supply charges and regulatory adjustments

---

## Equipment Replacement Costs (2025 Estimates)

| Component | Replacement Cost | Expected Life | Annual Reserve |
|-----------|------------------|---------------|----------------|
| **Furnace** | $5,500 | 18-22 years | $275/year |
| **Air Conditioner** | $8,000 | 14-18 years | $500/year |
| **A-Coil** | $1,800 | 15-20 years | $105/year |
| **Furnace Blower Motor** | $586 | 12-15 years | $45/year |
| **Dehumidifier** | $1,400 | 10-12 years | $127/year |
| **DHW Heater (Navien)** | $3,200 | 15-20 years | $185/year |
| **Total Annual Reserve** | — | — | **$1,237/year** |

---

## Energy Monitoring Value Analysis

### Mystery Load Resolution Potential

| Category | Annual kWh | Annual Cost | Optimization Potential |
|----------|------------|-------------|------------------------|
| **Identified Dehumidifier** | 294 | $85 | $21 (dew point control) |
| **Unresolved Residual** | 1,126 | $326 | $82-$163 (25-50% reduction) |
| **Total Moisture Control** | 1,420 | $411 | **$103-$184** |

### Equipment Longevity Monitoring Value

| Equipment | Replacement Cost | Monitoring Benefit | Annual Value |
|-----------|------------------|-------------------|--------------|
| **Furnace Blower** | $586 | Early failure detection | $50 (amortized) |
| **Air Conditioner** | $8,000 | Degradation tracking | $100-$200 |
| **Dehumidifier** | $1,400 | Duty cycle optimization | $103/year savings |

### Total Annual ROI

**Monitor Investment:** $400-$600  
**Annual Value:** $253-$534  
**Simple Payback:** 0.75 to 2.4 years

---

## Data Sources

- **Utility Billing:** Eversource Energy, Southern Connecticut Gas Company
- **Weather:** NOAA/NCEI Hartford Bradley International (KBDL), Station USW00014740
- **HVAC Runtime:** Honeywell Lyric T6 Pro thermostat telemetry
- **DHW Monitoring:** Navien NaviLink independent gas meter
- **Analysis Period:** January 1, 2022 - December 31, 2025

---

**Last Updated:** January 11, 2026  
**Data Quality:** Validated against 4-year historical baseline (CV < 8% all major metrics)
