# SEM-Meter First 13 Days — Deep Analysis Report

**Repo:** Residential-HVAC-Performance-Baseline-
**Window:** 2026-06-28 through 2026-07-10 (13 days, 307 valid hours of 312 logged)
**Sources:** SEM-Meter 16-CT hourly exports, Kasa plug sensors, Pirate Weather archive (temp/RH/dew point), EIA RECS 2020 (CE3.1 / CE3.1ST), EIA Table 5A (2024), NOAA Climate-at-a-Glance, American Standard submittal S9X1C100U-SUB-1D-EN
**Rate:** $0.29/kWh (matches CT 2024 average of 28.75 c/kWh, EIA Table 5A)
**Status:** v1.5 — full Jul 10 weather received (partial-export bias was -4.9 F); all 11 clean days now in fits (2026-07-11)

---

## 1. Data hygiene

- Daily CSVs contain an embedded `TOTAL_kWh` row — excluded before aggregation.
- **Grid outage contamination (Jul 4-5):** mains CTs read 0.000 from 21:00 Jul 4 through 02:00 Jul 5 (branch CTs remained live on the generator-fed bus, per install reference sec. 4). Hours 03:00-07:00 on Jul 5 are absent from the export. Jul 4-5 whole-home daily totals are undercounts; all base-load and regression work excludes these hours/days.
- Outage forensics from the SEM side: mains dead at 21:00 (~2 h before cliff_imminent at 23:22); generator-fed branch activity 23:00-02:00; fridge logged a 611 Wh recovery hour at 23:00 (compressor + likely defrost after the dead window). Furnace circuit read 0 W throughout the generator window despite essential-list status — reconcile against outage timeline.
- Kasa nesting verified empirically (hourly kasa <= parent circuit, all hours): living-room TV/Sonos within Family Room CT; computer outlet and tv_room within Bedroom/Office CT; dehumidifier, Navien (hwh), and basement router are standalone within the balance channel.

## 2. Totals

| Metric | Value |
|---|---|
| 13-day whole-home | 410.7 kWh ($119.10) |
| Daily average (11 clean days) | 29.1 kWh/day |
| Peak day (Jul 3, 95.5 F max) | 51.7 kWh |
| Minimum day (Jul 7, cool/rainy) | 17.7 kWh |
| Peak hour | 6.1 kW |

## 3. Base load

**Method:** "quiet hours" = valid hours with zero AC, dehumidifier, dryer, washer, dishwasher, microwave, and counter activity (<5 Wh each), n = 51 -- then split by computer-Kasa state, because the computer and tv_room Kasa outlets are scheduled OFF overnight (confirmed in data: 0.0 W hours 00:00-05:00, on ~06:30, off ~23:00).

**True always-on floor: 221 W** (n = 29 computer-off quiet hours, all 00:00-05:00, stable across the full window; hard floor 188 W at fridge off-cycle). Annualized: 221 W x 8,766 h = 1,937 kWh/yr = $562/yr = **29% of annual consumption** (6,730 kWh). Summer-conditions extrapolation; re-derive in winter.
The oft-quoted 285 W quiet-hour mean is a blend: computer-on quiet hours average 346 W whole-home (computer idling ~65 W plus daytime electronics). The 221 W floor is the correct base-load figure; the existing Kasa night schedules are already capturing ~$50-80/yr vs an unmanaged baseline.

Overnight-floor decomposition (221 W):

| Channel | W | Notes |
|---|---|---|
| Fridge | 68 | cycling average, overnight |
| Other (balance) | 54 | router 9 + Navien 7 + **true residual ~38** |
| Furnace | 42.5 | = 14 W IFC/ECM standby + Ecobee fan-circulate (sec. 7) |
| Bedroom/office | 25 | fully decomposed: UPS 18 + ~7 misc (AFCI electronics, 2 smoke detectors, Kasa plug overhead); computer + tv_room Kasa scheduled off overnight |
| Master suite | 18 | |
| Family room | 14 | AV deep standby ~8 W + ~6 W |

**Untracked share of the overnight floor: 24.5% (54 W)** at the CT level; **~17% (~38 W)** after Kasa attribution. The UPS (~18 W at wall, confirmed by breaker-off subtraction 2026-07-11) is on bedroom/office ckt 20, NOT in the balance channel; the 40 W residual is therefore largely unexplained. Plausible knowns (water softener, doorbell, garage opener, bath GFCIs) cover ~10-15 W, leaving ~25 W = ~220 kWh/yr = ~$64/yr unattributed -- the largest remaining dark load in the model.
**Breaker census procedure (closes the residual in ~20 min):** during a quiet hour, with SEM live view up (UPS keeps HA/monitoring alive), flip each balance-channel breaker off 2-3 min and read the whole-home delta: ckt 11 (basement outlets), 14 (dining), baths, garage receptacle. Each delta = that circuit's standby to +/-1-2 W.

**Whole-window coverage validation:** Other = 14.6% of total = dehumidifier 9.0% + router/Navien 1.3% + **true residual 4.3%** — vs install-reference sec. 6 prediction of ~4-5% unresolved. Coverage model validated.

**Benchmark:** NRDC Home Idle Load study (70k homes): average always-on 164 W (~1,300 kWh/yr). Subtracting fridge (68) and furnace circuit (42.5) from the 221 W floor leaves **~110 W of plug/electronics always-on -- well below the study average**, including the monitoring stack. The Kasa night schedules are the mechanism.

## 4. Consumption patterns

- **Cooling = 54.9% of window consumption** (compressor 150.8 + blower dynamic ~40 kWh), tracking the heat arc Jun 28 -> Jul 3 peak -> Jul 6-7 collapse.
- **Blower overhead = 26.8% of compressor energy** (regression: blower_kWh = 0.250 x AC_kWh + 0.023, n=128 AC-active hours).
- **Dehumidifier-AC anticorrelation r = -0.88** (daily, n=9). Natural experiment Jul 6-7: AC ~0, outdoor dew point ~61 F / RH 93-95%, dehumidifier surged to 4.6-6.0 kWh/day — undisplaced vapor-flux load, confirming the substitution mechanism. Note: dew point and AC collinear at r = 0.92 in this window; separating the DP term requires shoulder-season data.
- Post-outage laundry cluster: dryer Jul 5/6/7 = 6.9/5.2/3.7 kWh.
- Zone-call pattern: first-floor stat essentially never initiates cooling (0 calls observed); all measured cooling behavior (blower watts, duty, splits) reflects single-zone second-floor operation. Also explains Ecobee overcool-for-dehumidification never engaging on zone 1.
- "Base + everything else" band stable at 7.3-10.1 kWh/day regardless of weather.

## 5. Weather signature (Pirate Weather, calendar-day means, n=11 clean days, full weather coverage all days)

| Fit | Slope | Intercept | R^2 |
|---|---|---|---|
| Cooling vs Tmean | 1.592 kWh/F-day | -102.0 | 0.942 |
| Cooling vs CDD63.5 | 1.634 kWh/CDD | -1.52 | 0.949 |
| Compressor vs CDD63.5 | 1.303 kWh/CDD | | 0.948 |
| Whole-home vs CDD63.5 | 1.406 kWh/CDD | 15.1 kWh/day | 0.842 |

Stability: slope drifted 1.672 -> 1.658 -> 1.634 (-2.3% total) as days were added, R^2 steady ~0.95, balance point pinned at 64.0-64.1 F throughout. Converged. Methodology note: a partial-day weather export (Jul 10, hours 00-07 only) biased that day's mean -4.9 F and made its cooling appear 30% above the fit line; corrected with the full-day re-pull. Daily means require full-day coverage -- add an n>=90 sample check to the pipeline.
Dew-point decoupling: still blocked (r(dp, AC) = 0.91 across 11 days); shoulder-season data remains the requirement.

- **Balance point: 64.1 F (daily) / 63.6 F (hourly)** — independently confirms the Ecobee-derived 63-63.5 F estimate. Hourly onset: 0% compressor hours below 63 F outdoor; ~80% above 80 F.
- **Net marginal cost: $0.41 per CDD63.5** (whole-home slope x $0.29). Gross cooling $0.47/CDD; the ~14% discount is the dehumidifier duty displaced per cooling kWh (ledger: 1.63 gross - ~0.2 dehum offset = ~1.41 net).
- Consistency check: 1,694 kWh annual cooling / 1.634 = ~1,037 CDD63.5/yr implied (plausible for central CT; recompute directly from the Pirate Weather archive over a full season).
- At 90-96 F the system averaged 2.05 kWh/h cooling at 81% compressor duty — still cycling through a 95.5 F peak: adequate, not excessive, capacity.

## 6. Benchmarks (all verified from source)

| Basis | Cooling kWh/HH-yr | CDD65 | kWh/CDD65 |
|---|---|---|---|
| US all homes (RECS 2020) | 2,055 | 1,503 (2020) | 1.37 |
| US single-family detached | 2,510 | 1,503 | 1.67 |
| Connecticut all homes | 1,062 | 772 (2020) | 1.38 |
| New England all homes | 947 | - | - |
| This house, base-65 | 1,694 (2025) | 676 (CT 2025) | 2.51 |
| **This house, base-63.5** | 1,694 | ~1,013 | **1.67** |

The apparent 1.8x-CT-average intensity at base-65 is an artifact stack: (a) RECS denominators include no-AC homes, window units, apartments; (b) base-65 CDD undercounts exposure for a 63.5 F-balance house by ~50%. Priced at own balance point, intensity equals the US single-family-detached ratio. A low balance point is characteristic of a tight envelope, not poor equipment.

Household totals (EIA Table 5A 2024): CT avg 694.6 kWh/mo @ 28.75 c; US 863.3 kWh/mo @ 16.48 c. This house: 561 kWh/mo = 19% below CT, 35% below US.

## 7. Equipment verification (nameplate closed-loop)

**Condenser:** 4A7A4048L1000AA — American Standard Silver 14, 4-ton, single-stage, R-410A.
**Furnace:** S9X1C100U5PSBAB — 100k input, 95% AFUE, 9-tap constant-torque ECM (1 hp, Vortica II), 5-ton cabinet.
**Coil:** 4TXCC005DS3HCAA (5-ton cased). Installed ~Nov 2021.
**Zoning:** EWC Ultra-Zone NCM-300 panel (VER 2.3), 2 zones active (zone 1 = main floor, zone 2 = upstairs; zone 3 unused), motorized dampers, no evidence of bypass damper in panel wiring (field check pending). SAS supply-air limit and low-temp limit dial (~43 F) provide coil-icing backstop. Operating pattern (Jul 2026): ~99% of cooling calls are second-floor only -- single-zone operation is the normal cooling state, not the exception.

**Operational EER at near-full load: 12.0-12.6** (3.08 kW compressor + ~0.75 kW blower vs 46-48 kBtu/h capacity range; exact AHRI combo cert not retrieved). Family rating: up to 15.5 SEER / 13 EER. **Verdict: on-spec, no fault signature.**

**Blower (RESOLVED against submittal fan table @ 0.5 in. w.c.):**

| Tap | CFM | W | CFM/ton (4T) |
|---|---|---|---|
| 5 | 1,554 | 436 | 389 |
| **6 (design)** | **1,688** | **519** | **422** |
| 7 | 1,853 | 631 | 463 |
| **8 (observed match)** | **2,033** | **782** | **508** |

Measured sustained cooling-mode blower: 732-747 W raw; **~760 W after subtracting the true 14 W standby** -- matching tap 8 at ~0.4-0.5 in. static. Because ~99% of cooling calls are second-floor-only, these measured hours WERE single-zone hours: the system moves ~2,030-2,080 CFM (>500 CFM/ton) through the zone-2 trunk alone without excessive static. Duct capacity is generous; the zoning penalty for a constant-torque ECM is minimal in this system.
**Single-zone worst case at tap 6 (static scales with flow^2):** ~0.3 in. -> ~1,750 CFM = ~437 CFM/ton -- above the 400 CFM/ton icing floor even with zone 1 sealed. NCM-300 SAS + low-temp limit provide the backstop; confirm SAS ON (DIP 7) and limit ~40-45 F. LED2 (SUPPLY AIR LIMIT) lit during a cooling call = air-starved, do not lower tap.
**Tap location:** S9X1 lower blower-compartment door, IFC digital display (MENU/OPTIONS -- no dip switches). Door interlock kills power; hold switch closed to read. Photograph settings before changing.
**Tap 8 -> 6 economics (manufacturer airflow factors, Trane ref 1229687, -17% CFM extrapolated):** blower -215 W (782->519 spec), refrigerant-side power -~83 W, capacity x~0.955 + fan-heat credit -> net ~45.1 kBtu/h. Energy per delivered Btu -5.0% -> ~105 kWh/yr = ~$30/yr; slope 1.63 -> ~1.53 kWh/CDD. Capacity cost concentrated in the ~5-10 hrs/yr of >=98% duty (measured: 5 hrs in the 11-day window, 88-93 F outdoor); expect ~0.5-1.5 F drift on design-day afternoons only. Fully reversible.
**Context that sizes the decision:** system already runs 25-min average cycles with 15-min minimum runtime; indoor RH holds <50%; noise is not a concern. Latent and acoustic side-benefits are therefore ~zero here -- the change is pure kWh harvesting. Verdict: worth doing on the next trip past the furnace, not worth a special trip. Validation: blower plateau ~520 W in SEM minute data; kWh/CDD drift toward ~1.53.

**Furnace-circuit "42 W constant" — RESOLVED (minute data, 2026-07-10):**
Minute resolution shows 14 W true standby + ~131 W blower for ~15 min/hr (0.014 x 45/60 + 0.131 x 15/60 = 0.043 kWh/h, matching every idle hour). 131 W = tap 1 circulate (spec 104-129 W band). **Attribution: Ecobee "fan minimum on time" ~15 min/hr**, introduced with the June 2026 thermostat transition — explaining its absence from the 2025 decomposition.
- True standby: 14 W = 123 kWh/yr = $36/yr (normal, irreducible).
- Circulation: <=287 kWh/yr = <=$83/yr upper bound (heating/cooling calls satisfy the quota in active hours). This is a deliberate comfort/mixing setting, not a defect. Option: 15 -> 5 min/hr retains most mixing benefit, recovers ~$40-55/yr.

## 8. End-use decomposition correction required

The 2025 decomposition allocates "furnace blower: 84 kWh/yr." Measured reality:
- Cooling-season blower: ~450 kWh/yr at current tap (0.25-0.27 x compressor)
- Fan circulation: up to ~287 kWh/yr (new with Ecobee, June 2026)
- IFC/ECM standby: 123 kWh/yr
- Heating-season blower: additional (winter data needed)

Total air-handler electricity ~850+ kWh/yr vs 84 allocated; the balance was absorbed into baseload/residual. Rebalance before the July monthly report.

## 9. Opportunities (no lifestyle impact), ranked

Rule of thumb at $0.29/kWh: **10 W continuous = 87.7 kWh/yr = $25.40/yr.**

| # | Item | Action | Est. saving |
|---|---|---|---|
| 1 | Blower tap 8 -> 6 | IFC setting, reversible; next trip past furnace | ~$30/yr (pure kWh; latent/noise benefits ~zero here) |
| 2 | Ecobee fan circulate 15 -> 5 min/hr | thermostat setting (owner's comfort call) | ~$40-55/yr |
| 3 | Breaker census of ~38 W residual | 20 min, quiet evening | up to ~$64/yr exposure; recoverable share unknown |
| 4 | Fridge health (2.17 kWh/day summer; re-measure in fall) | coil clean, gasket check | ~$20-40/yr speculative |

Removed after data review: computer overnight idle and AV overnight standby -- both already captured by existing Kasa night schedules (overnight AV deep standby is ~8 W, not the 21 W daytime-blended figure).

Realistic total: **~$70-125/yr (3-6%)** with zero comfort or habit change -- an honest downgrade from earlier drafts after confirming the Kasa schedules already harvest the electronics savings. Items 1-2 reduce the cooling slope ~6-9% and were invisible before circuit-level metering.

## 10. Open items

- [ ] Read cooling airflow tap from IFC display; measure temperature split
- [ ] Confirm Ecobee fan min-on-time setting; decide 15/5/0 min/hr
- [ ] Retrieve AHRI combination certificate (exact SEER/EER for 4A7A4048L + 4TXCC005 + S9X1C100U5)
- [ ] Recompute CDD63.5 directly from Pirate Weather archive, full season
- [ ] Rebalance 2025 end-use decomposition (air-handler line)
- [ ] Reconcile furnace-circuit 0 W during generator window vs essential-loads list
- [ ] Pull exact expanded performance table via AHRI ref number (check install invoice/warranty paperwork; comfortsite.com/Resources/Literature/pdf/{AHRI-ref}.HTML)
- [ ] Re-baseline UPS wall draw at ~18 W; pre-log expected +~10 W step when N100 moves onto UPS
- [ ] Winter base-load re-derivation; fridge re-measurement in fall
- [ ] Shoulder-season data to decouple dew point from temperature in dehumidifier model
