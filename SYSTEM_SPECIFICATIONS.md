# System Specifications: HVAC and Energy Equipment

**Property:** 2,440 sq. ft. Two-Story Colonial  
**Location:** Central Connecticut, Climate Zone 5A  
**Construction Year:** 2021  
**Last Updated:** January 2026

---

## Primary Heating System

### Furnace

**Manufacturer:** American Standard  
**Model:** Silver 95 Series (S9X1C100U5PSBA)  
**Type:** Single-stage condensing gas furnace

**Performance Specifications:**
- **AFUE (Marketing):** "up to 96%" (series marketing claim)
- **AFUE (Submittal-Verified):** 95.0% (per S9X1C100U-SUB-1D-EN; used in all calculations)
- **Input Capacity:** 100,000 BTU/hr (nameplate)
- **Output Capacity:** 95,000 BTU/hr (at 95% AFUE)
- **Effective Heating Rate:** 60,556 BTU/hr (empirical; accounts for cycling losses, duct losses, and part-load operation)
- **Modulation:** Single-stage (no modulation)
- **Fuel:** Natural gas
- **BTU/CCF:** 103,700 (pipeline natural gas energy content; used in all calculations)

**Blower Specifications:**
- **Motor Type:** 1 hp constant-torque ECM (Electronically Commutated Motor)
- **Design:** Vortica™ II airflow optimization
- **Rated Power:** 746W maximum
- **Measured Power Draw:** 210W (0.21 kW) during typical heating operation
- **Speed Control:** Multi-tap (heat/cool/circulation modes)
- **Replacement Cost:** $586 (motor assembly, parts + labor)

**Operational Characteristics:**
- **Ignition:** Hot surface igniter
- **Combustion Air:** Direct-vent sealed combustion
- **Exhaust:** PVC (condensing)
- **Condensate Management:** Drain to floor drain via trap

**Installation Details:**
- **Location:** Basement mechanical room
- **Ductwork:** Sheet metal trunk with flex branches
- **Filter Size:** 20×25×5 MERV 11 media filter
- **Filter Replacement:** Every 6-9 months

**2025 Performance:**
- **Runtime:** 831 burner hours
- **Fuel Consumption:** 547 CCF (furnace only, excludes fireplace)
- **Delivered Heat:** 57.5 MMBTU (96% AFUE)

---

## Primary Cooling System

### Air Conditioner (Outdoor Unit)

**Manufacturer:** American Standard  
**Model:** Silver 14 Series (4A7A4048L1000AA)  
**Type:** Split-system central air conditioner

**Performance Specifications:**
- **Capacity:** 48,000 BTU/hr (4 tons)
- **SEER:** 14
- **Compressor Type:** Single-stage Duration™ scroll compressor
- **Refrigerant:** R-410A
- **Voltage:** 240V single-phase
- **Measured Power Draw:** 4.9 kW steady-state

**Installation Details:**
- **Location:** North side of house (shaded)
- **Line Set:** Insulated copper, 25 ft run
- **Disconnect:** 60A fused disconnect
- **Pad:** Composite concrete pad

**2025 Performance:**
- **Runtime:** 346 hours (cooling season)
- **Electricity Consumption:** 1,694 kWh
- **Average Outdoor Temperature (runtime):** ~82°F

### Indoor Coil (Evaporator)

**Manufacturer:** American Standard  
**Model:** 4TXCC005  
**Type:** Cased A-coil (all-aluminum)

**Specifications:**
- **Expansion Device:** Thermostatic Expansion Valve (TXV)
- **Drain Pan:** Primary + secondary (safety switch)
- **Installation:** Upflow configuration in furnace plenum

**TXV Advantages:**
- Precise superheat control across varying conditions
- Maintains consistent 4.9 kW power draw
- Prevents refrigerant flooding during low-load operation

---

## Supplemental Heating

### Gas Fireplace

**Type:** Direct-vent sealed combustion (natural gas)  
**Location:** Living room (main floor)

**Performance:**
- **Efficiency:** 65-70% steady-state (manufacturer specification)
- **2025 Fuel Input:** 51-55 CCF (~5.1-5.5 MMBTU)
- **2025 Delivered Heat:** 3.6 MMBTU
- **Usage Pattern:** Supplemental zone heating, aesthetic

**Installation:**
- **Venting:** Direct to exterior (sealed combustion)
- **Control:** Manual on/off with thermostat modulation
- **Safety:** Oxygen depletion sensor, flame sensor

---

## Moisture Control

### Basement Dehumidifier

**Manufacturer:** Santa Fe  
**Model:** Classic  
**Type:** Whole-basement commercial-grade dehumidifier

**Performance Specifications:**
- **Capacity:** 110 pints per day (AHAM rated)
- **Coverage:** Up to 2,200 sq. ft.
- **Operating Range:** 40-95°F ambient
- **Power Draw:** 700W (6.4A @ 115V) during compressor operation
- **Energy Factor:** 3.0 L/kWh (exceeds Energy Star 2.0 L/kWh requirement)

**Control and Monitoring:**
- **Current Setpoint:** 45% RH (fixed humidity control)
- **Measured Basement Conditions:** 65°F average temperature
- **Equivalent Dew Point:** 43°F
- **Operational Season:** April through October (basement temps >60°F)

**Installation:**
- **Location:** Basement utility room
- **Drainage:** Gravity drain to floor drain
- **Ducting:** None (free-standing unit)
- **Circuit:** Dedicated 15A circuit

**2025 Performance:**
- **Estimated Runtime:** 2,030 hours (~50% duty cycle during season)
- **Electricity Consumption:** ~1,420 kWh (294 kWh modeled + 1,126 kWh residual)
- **Annual Cost:** ~$411

**Optimization Potential:**
- **Proposed Strategy:** Dew point control at 52°F (vs. current 45% RH / 43°F dew point)
- **Expected Savings:** ~$105/year (25% duty cycle reduction)
- **Implementation:** Shelly H&T sensor + smart plug automation

---

## Domestic Hot Water (DHW)

### Tankless Water Heater

**Manufacturer:** Navien  
**Model:** NPE-series condensing tankless  
**Type:** On-demand / instantaneous water heater

**Performance Specifications:**
- **Efficiency:** 95%+ AFUE (condensing technology)
- **Fuel:** Natural gas
- **Temperature Rise:** 45°F inlet → 120°F outlet (typical)
- **Flow Rate:** 5-7 GPM at 45°F rise
- **Modulation:** 15:1 turndown ratio

**Recirculation System:**
- **Type:** Integrated pump with return line
- **Schedule:** Programmable timer
- **Standby Loss:** ~23% of total DHW consumption (per Navien factory guidance)

**Monitoring:**
- **NaviLink System:** Independent gas meter for DHW-only consumption
- **2025 Navien Meter Reading:** 220.8 CCF
- **2025 Billing-Aligned Value:** 188 CCF (used for EUI consistency)
- **Variance:** 15% (32.8 CCF unresolved measurement gap)

**Installation:**
- **Location:** Basement utility room
- **Venting:** PVC condensing exhaust (sealed combustion)
- **Electrical:** 120V for controls and recirculation pump

**2025 Performance:**
- **Daily Consumption:** 0.533 CCF/day (billing-aligned baseline)
- **Annual Consumption:** 188-221 CCF (depending on measurement method)
- **Annual Cost:** $313 (billing-aligned) to $368 (Navien meter)

---

## Thermostat and Controls

### Zone Configuration

**Configuration:** 2-zone (1F/2F) with independent schedule control
**Damper System:** Motorized zone dampers in trunk ductwork
**Control Logic:** Either thermostat call activates furnace; zone dampers direct airflow

### Thermostats (2 units)

**Manufacturer:** Honeywell
**Model:** Lyric T6 Pro WiFi Programmable
**Type:** Digital programmable with remote monitoring

**Zone Assignments:**
- **1st Floor (1F):** Living areas, kitchen, main level
- **2nd Floor (2F):** Bedrooms, upper level

**Capabilities:**
- **Connectivity:** WiFi-enabled, cloud logging
- **Data Logging:** High-resolution runtime telemetry per zone
- **Smart Features:** Geofencing, adaptive scheduling

**2025 Configuration:**
- **Heating Setpoint:** 68-70°F (occupied), 65°F (sleep)
- **Cooling Setpoint:** 74-76°F
- **Fan Mode:** Auto (no continuous circulation)
- **Schedule:** Independent programmable schedules per zone

**2025 Performance:**
- **Zone Balance:** 53.2% to 2F (slight 2F bias due to cathedral ceiling heat loss)
- **Chaining Index:** 1.38 (moderate zone coordination)
- **Zone Overlap:** 19% concurrent operation

**Data Exports:**
- **Furnace Runtime:** 831 burner hours (2025)
- **Temperature Logs:** 15-minute intervals per zone
- **Equipment Cycling:** Start/stop timestamps per zone

---

## Ductwork and Air Distribution

### Duct System

**Configuration:** Conventional trunk-and-branch

**Materials:**
- **Main Trunk:** Sheet metal (basement)
- **Branches:** Flex duct (R-6 insulation)
- **Registers:** Standard steel (adjustable dampers)

**Return Air:**
- **1st Floor:** Central return (living room)
- **2nd Floor:** Central return (hallway)
- **Basement:** No dedicated return (door undercut provides air path)

---

## Building Envelope

### Wall Construction

**Type:** 2×6 advanced framing with exterior continuous insulation

**Assembly (exterior to interior):**
1. Vinyl siding
2. Continuous insulation board (R-5 to R-10)
3. Sheathing (OSB)
4. 2×6 studs with batt cavity insulation (R-20 to R-21)
5. Vapor barrier
6. Drywall

**Estimated R-Value:** R-25 to R-31 effective

### Ceiling/Attic

**Insulation:** Blown-in fiberglass insulation  
**R-Value:** R-49 to R-60  
**Ventilation:** Ridge and soffit vents (passive)

**Cathedral Ceiling (Living Room):**
- **Height:** 14 feet
- **Insulation:** Batt insulation (R-30 to R-38)
- **Challenge:** Potential stratification (monitored via setpoint stability)

### Windows

**Type:** Vinyl-framed double-pane with low-E coating  
**U-Factor:** 0.27 to 0.30  
**SHGC:** 0.25 to 0.30  
**Orientation:** Majority south-facing (passive solar benefit)

### Foundation/Basement

**Type:** Poured concrete with interior insulation  
**Wall Insulation:** R-15 (2" rigid insulation board or equivalent)  
**Floor:** Concrete slab (uninsulated)  
**Condition:** Conditioned space (included in 2,440 sq. ft. total)

### Air Sealing

**Estimated Leakage:** <3 ACH50 (based on performance modeling)  
**No Blower Door Test Available:** Estimate derived from UA calculation

---

## Electrical Service

**Main Panel:** 200A service  
**Voltage:** 120/240V split-phase  
**Major 240V Loads:**
- Air conditioner (4-ton)
- Electric dryer
- Range (240V but gas cooktop)

**Monitoring Preparation:**
- **Planned System:** Fusion Energy 16-CT or equivalent
- **Target Circuits:**
  - Furnace (blower monitoring)
  - Air conditioner (efficiency tracking)
  - Dehumidifier (mystery load resolution)
  - DHW recirculation pump (standby loss quantification)

---

## Property Characteristics

**Total Conditioned Area:** 2,440 sq. ft.

**Floor Plan:**
- **Basement:** 800 sq. ft. (finished, conditioned)
- **1st Floor:** 1,220 sq. ft. (living areas, kitchen)
- **2nd Floor:** 420 sq. ft. (bedrooms)

**Occupancy:** 2 residents (full-time)

**Orientation:** Long axis east-west (optimal for passive solar)

**Lot:** Suburban, moderate tree cover (north/west shade for AC unit)

---

## Maintenance Schedule

### Quarterly

- Inspect furnace filter (replace if dirty)
- Clean dehumidifier filter
- Check condensate drains (furnace, AC, dehumidifier)

### Annually

- Professional HVAC inspection (spring)
- Clean AC outdoor coil (pre-season)
- Verify refrigerant charge
- Inspect ductwork for leaks
- Test CO/smoke detectors

### As Needed

- Replace furnace filter (every 6-9 months for MERV 13)
- Clean AC condensate drain
- Inspect fireplace (annual sweep recommended)

---

## Replacement Lifecycle Planning

| Component | Install Date | Expected Life | Replacement Due | Est. Cost |
|-----------|-------------|---------------|-----------------|-----------|
| Furnace | 2021 | 18-22 years | 2039-2043 | $5,500 |
| Air Conditioner | 2021 | 14-18 years | 2035-2039 | $8,000 |
| A-Coil | 2021 | 15-20 years | 2036-2041 | $1,800 |
| Dehumidifier | ~2018-2020 | 10-12 years | 2028-2032 | $1,400 |
| DHW Heater | 2021 | 15-20 years | 2036-2041 | $3,200 |
| Blower Motor | 2021 | 12-15 years | 2033-2036 | $586 |

**Total Annual Reserve:** $1,237/year (based on expected lifecycles)

---

**Document Version:** 1.2.1  
**Last Equipment Survey:** January 2026  
**Next Scheduled Update:** January 2027 (or upon equipment replacement)
