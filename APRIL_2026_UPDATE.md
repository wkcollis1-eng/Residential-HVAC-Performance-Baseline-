# HVAC Performance Update: April 2026

**Version:** 1.6.2
**Date:** June 17, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Heating Intensity computed on **net space-heating gas** (total − Navien DHW),
per the v1.5.1 correction established in the March 2026 report. All intensity figures below,
and the `data/monthly_summary.csv` column, are on this basis.

**Revision 1.6.1 (June 18, 2026):** Official Bradley/KBDL monthly degree days (ACIS/xmACIS2) are now captured (`bdl_degree_days.csv`) and available for April. Heating Intensity is reported **dual-basis** — BDL official (authoritative) and HA proxy. On the official BDL basis, **April net intensity is 111.0 CCF/1k HDD, not 96.8**: the HA proxy logged April ~60 HDD colder than official (472.3 vs 412), which deflated the proxy intensity and produced the apparent “April anomaly.” Conclusions affected are corrected below. (Runtime/HDD figures remain on the proxy basis in this revision; only Heating Intensity and HDD/CDD references are placed on BDL official.) Prior BDL figures in the §HDD note — Feb 1,125 / Mar 709 — were mismapped (1,125 is Jan 2025's total) and are corrected to ACIS values Feb 1,120 / Mar 744.

---

## Executive Summary

April 2026 is the first full month of the spring shoulder season and the first full month
under the **CPH=2 + 30 s fan-delay** thermostat change (effective April 1). The furnace ran 38.4 hours — a
23.2% reduction from April 2025 despite carrying more HDD. On the **official BDL basis, net
heating intensity is 111.0 CCF/1k HDD** (HA proxy: 96.8), about 23% above the annual baseline and
essentially identical to May's 111.1 — an ordinary shoulder-season reading, not the season's
best. The earlier proxy figure (96.8, “below March, bucking shoulder physics”) was largely an
artifact of the proxy over-counting April HDD by ~60 (472.3 vs 412 official); on the authoritative
BDL basis that anomaly disappears. The YoY improvement is real but smaller than the proxy implied
— −15.2% (BDL) vs −24.8% (proxy). DHW savings from the
recirculation optimization widened to −35.7% year-over-year.

**Key April 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas Consumption | 59.0 CCF | −46.8% MoM |
| Weather Severity | 412 HDD65 / 22 CDD65 *(BDL official)* | proxy 472.3 HDD (+60); BDL now captured (ACIS) |
| Net Space-Heating Gas | 45.72 CCF | −52.4% MoM |
| **Heating Intensity** *(net, BDL)* | **111.0 CCF/1k HDD** | −15.2% vs Apr 2025; +22.9% vs baseline (proxy: 96.8) |
| DHW Consumption | 13.28 CCF | −35.7% YoY; recirc optimization |
| HVAC Runtime | 38.4 hours | −23.2% YoY despite +11.9% HDD |
| Runtime / HDD | 4.88 min/HDD | Shoulder-season normal |
| Avg Cycle Length | 8.2 min *(CSV-derived)* | up from 6.6 in March — CPH=2 directional |
| Zone Balance (1F) | 52.3% | Within 50% ± 5% target |
| Electric | 285 kWh / $81.48 | −17.2% kWh YoY |

> **Methodology note:** This report uses net space-heating gas for Heating Intensity, per
> v1.5.1. The repo's `monthly_summary.csv` `Heating_Intensity_CCF_1kHDD` column previously held
> total-gas values (e.g. Apr 2025 = 177.7); it has been recomputed to the net basis (Apr 2025 =
> 128.8) for **all** heating-season rows in the accompanying file. Review before committing —
> this changes every historical intensity value.

**Interpretation:** The durable signal is runtime: 38.4 h is −23.2% YoY on *more* HDD, a
continuation of the March pattern. The intensity picture changes on official weather — at 111.0
(BDL) April is a normal shoulder reading, not the season's lowest, and it matches May (111.1)
rather than sitting anomalously low. The proxy's 96.8 was mostly its cold-HDD bias for April, not
a CPH=2 efficiency leap. CPH=2 may still contribute at the margin; high April solar gain (furnace
runtime ~20% below the degree-day model) remains a real driver of the low *runtime*, independent
of the HDD-source question. The cleaner CPH=2 read still comes from May/June.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HDD Methodology Note](#hdd-methodology-note)
5. [HVAC Runtime Performance](#hvac-runtime-performance)
6. [Recommendations](#recommendations)

---

## Year-over-Year Analysis

### April 2026 vs April 2025

| Metric | April 2025 | April 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 75.0 CCF | 59.0 CCF | −21.3% | Less gas despite more HDD — favorable |
| **DHW (Navien)** | 20.66 CCF | 13.28 CCF | **−35.7%** | Recirc optimization sustained, widening |
| **Space Heating** *(net)* | 54.34 CCF | 45.72 CCF | −15.9% | Real reduction against +11.9% HDD |
| **HDD65 (BDL official)** | 415 | 412 | −0.7% | Near-identical Aprils — minimal weather confound |
| **HDD65 (HA proxy)** | 422.0 | 472.3 | +11.9% | Proxy over-counts Apr 2026 vs BDL |
| **Heating Intensity** *(net, BDL)* | **130.9 CCF/1k HDD** | **111.0 CCF/1k HDD** | **−15.2%** | Real efficiency gain (proxy basis: −24.8%) |
| **HVAC Runtime** | 50.0 hrs | 38.4 hrs | −23.2% | Less runtime despite more HDD |
| **Runtime / HDD** | 7.11 min/HDD | 4.88 min/HDD | −31.4% | Load distribution + CPH=2 |
| **Electric** | 344 kWh / $109.56 | 285 kWh / $81.48 | −17.2% / −25.6% | Lower use + lower effective rate |

**Key Insight:** On the official BDL basis the two Aprils had almost identical weather (415 vs
412 HDD), so the −15.2% intensity improvement is nearly pure efficiency with negligible weather
confound — a cleaner result than the proxy comparison, which had to argue past a spurious +11.9%
HDD swing. April 2026 burned 0.111 CCF/HDD of space heat (BDL) versus 0.131 in April 2025. The
35.7% DHW reduction (an estimated $14–16 monthly offset) continues to soften the total bill. The
gain is real and substantial, if smaller than the −24.8% the proxy implied.

The electric bill fell harder than usage (−25.6% vs −17.2% kWh) because the effective rate also
dropped (~0.319 → 0.286 $/kWh, −10%) — a rate tailwind on top of lower consumption.

---

## Month-over-Month Analysis

### Natural Gas (March 2026 → April 2026)

| Metric | March 2026 | April 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 111.0 | 59.0 | −46.8% |
| Space Heat CCF *(net of DHW)* | 102.26 | 45.72 | −55.3% |
| DHW CCF (Navien) | 8.74 *(vacation)* | 13.28 | +51.9% |
| HDD65 *(BDL official)* | 744 | 412 | −44.6% |
| **Heating Intensity** *(net, BDL)* | **137.4 CCF/1k HDD** | **111.0 CCF/1k HDD** | **−19.2%** |

**Analysis:** On the official BDL basis, net space-heating gas fell 55.3% on a 44.6% HDD
reduction, and net intensity fell from 137.4 (March) to 111.0 (April), a −19.2% step. **Caveat:** March's
137.4 is vacation-inflated (its DHW was suppressed to 8.74 CCF by a 2-week absence, inflating net space heat), so this
raw step overstates the underlying decline — normalized, the Mar→Apr drop is gentler. April lands exactly where May
does (~111) — a flat shoulder-season plateau, not an anomalously efficient April. (The proxy's
larger −22.6% step was inflated by its April HDD over-count.) Solar gain still depresses actual
runtime below the degree-day model. DHW dipped 11.5% MoM, normal for the seasonal transition.

### HVAC Runtime (March 2026 → April 2026)

| Metric | March 2026 | April 2026 | MoM Change |
|---|---|---|---|
| Total Heating Hours *(burner)* | 81.4 | 38.4 | −52.8% |
| Zone Balance (1F%) | 49.6% | 52.3% | +2.7 pts |
| Runtime / HDD | 6.4 | 4.88 | −23.8% |
| Avg Cycle Length *(CSV-derived)* | 6.6 min | 8.2 min | +24.2% |

**Analysis:** Runtime fell roughly in proportion to HDD. The zone balance continued its
shoulder-season shift toward first-floor dominance (49.6% → 52.3%) as the second-floor cathedral
load attenuates with declining ΔT — the same mechanism noted in March, one step further. The
avg cycle-length increase (6.6 → 8.2 min) moves in the direction the CPH=2 change was expected to
produce (target 9–10 min), but see the runtime section for the caveats on this figure.

---

## DHW Performance Update

### Sustained Recirculation Optimization Results

| Metric | April 2025 *(24 hr recirc)* | April 2026 *(15 hr recirc)* | Change |
|---|---|---|---|
| DHW Gas (Navien) | 20.66 CCF | 13.28 CCF | **−35.7%** |
| DHW Operating Hours | — | 11 hrs | — |
| DHW Recirc Hours | — | 32 hrs | — |
| Implied gas per operating hour | — | 1.21 CCF/hr | — |

**Note:** The April YoY DHW reduction (−35.7%) reflects the recirculation schedule change
(off 9 PM – 6 AM). It is **not** comparable to March's apparent −61.1%, which was confounded by a
2-week vacation rather than recirc savings (see the corrected March report). Prior-year April
operating/recirc hours were not captured under the old workflow, so the per-hour comparison
is single-sided this month; both fields are now archived going forward (see Recommendations).

---

## HDD Methodology Note

Official Bradley/KBDL degree days (ACIS/xmACIS2) are now captured monthly (`bdl_degree_days.csv`)
and available for April. Dual-basis comparison, corrected to authoritative ACIS values:

| Month | HA Proxy Archive | BDL Official (ACIS) | Proxy − BDL |
|---|---|---|---|
| February 2026 | 1,062.6 *(daily CSV 1,089.0)* | 1,120 | −57 |
| March 2026 | 767.6 | 744 | +24 |
| April 2026 | **472.3** | **412** | **+60** |

> **Correction:** earlier drafts cited BDL Feb = 1,125 and Mar = 709; those were mismapped (1,125
> is in fact Jan 2025's BDL total). The ACIS values above are authoritative.

The proxy carries no fixed bias — it reads *colder* than BDL in deep winter (Feb −57) but
*over-counts* in the shoulder (Mar +24, Apr +60). April is the largest divergence: 472.3 proxy vs
412 official, +14.6%. That is the whole reason intensity differs by basis (96.8 proxy vs **111.0
BDL**); the **BDL figure is authoritative** and used in the headline. At 111.0, April sits ~23%
above the 90.3 annual baseline — normal shoulder elevation, in line with May's 111.1.

---

## HVAC Runtime Performance

### Baseline Comparison

| Metric | Annual Baseline | April 2026 | Context |
|---|---|---|---|
| Runtime / HDD | 10.9 min/HDD | 4.88 min/HDD | Shoulder-season normal (structurally below annual) |
| Heating Intensity *(net, BDL)* | 90.3 CCF/1k HDD | 111.0 CCF/1k HDD | +22.9% — shoulder-month elevation (proxy: 96.8 / +7.2%) |
| Zone Balance Target | 50% ± 5% | 52.3% | ✓ Within band |

As established in March, comparing a shoulder month's min/HDD against the January–February-weighted
annual baseline overstates "efficiency"; the meaningful comparison is YoY. April 2026's 4.88 vs
April 2025's 7.11 (−31.4%) is the within-month figure (proxy basis), and it is genuinely
favorable; on BDL HDD the same metric is 5.59 vs 7.23 (−22.7%).

### CPH=2 First-Month Impact

April 1 was the CPH=3→2 + 30 s fan-delay change, making April the first full month under the new
cycling regime. From the daily CSV:

| Metric | March (CPH=3) | April (CPH=2) | Direction |
|---|---|---|---|
| Avg cycle length | 6.6 min | 8.2 min | +24% — toward the 9–10 min target |
| Furnace cycles (total) | 738 | 282 | −62% |
| Cycles / day | 23.8 | 9.4 | −60% |

The cycle-length increase is the expected CPH=2 signature and points the right way. **Two
caveats apply.** First, the cycle-count drop (−60%) is mostly demand-driven — April had less than
half March's heating hours — not a clean CPH=2 effect; the count would have fallen regardless.
Second, these figures are derived from the daily CSV (`furnace_runtime_min` / `furnace_cycles`)
and run below the `sensor.hvac_furnace_min_per_cycle_month` value the March report cited (~7.3 min
baseline). The HA monthly cycle sensors are authoritative; pull `sensor.hvac_furnace_cycles_month`
and `sensor.hvac_furnace_min_per_cycle_month` to confirm before drawing a firm CPH=2 conclusion.
The clean test is May, the last full month before the late-May Ecobee swap.

---

## Recommendations

### Monitoring Priorities

1. **CPH=2 confirmation (May):** April's cycle-length lift (6.6 → 8.2 min) is encouraging but
   confounded with mild weather and is CSV-derived. May is the decisive month — confirm with the
   HA monthly cycle sensors and isolate it before the Ecobee thermostats (installed ~May 29)
   change the controller behavior.

2. **Ecobee transition (May onward):** The Honeywell→Ecobee swap on ~May 29 means May is a
   split-controller month and June is the first full Ecobee month. Tag runtime and cycling data
   by controller for the Ecobee-vs-Honeywell baseline comparison; do not blend across the swap.

3. **12-Month Rolling UA Trend:** Unchanged guidance from March — the rolling UA (~540 vs 493
   baseline) will only resolve as Jan–Feb 2026 cycle into the window against Jan–Feb 2025. April
   shoulder data does not move this determination.

4. **Heating Intensity Trajectory:** April's 96.8 (net) is the closest-to-baseline heating-month
   reading of the season and supports the expectation that CPH=2 contributes a few CCF/1k HDD over
   a full season. Re-baseline only after a full 2026–2027 heating season under CPH=2.

5. **DHW per-hour tracking now enabled:** With `DHW_Op_Hrs` / `DHW_Recirc_Hrs` now archived
   (April: 11 / 32), the implied 1.21 CCF/operating-hour becomes a trackable series. Watch whether
   the YoY DHW savings hold or narrow as municipal inlet temperatures rise through summer.

### Pending / Data Hygiene

- **Intensity methodology correction (action required):** `data/monthly_summary.csv` has been
  recomputed to net-basis Heating Intensity for all heating-season rows. Review the diff and
  commit; this aligns the dataset with the v1.5.1 report methodology.
- **Q1 reconciliation (RESOLVED, June 18 2026):** The March DHW discrepancy is resolved in favor of
  the archive — **8.74 CCF**, reflecting a 2-week vacation (the repo's 15.0 was an entry error). February
  gas cost corrected to 274.7. `monthly_summary.csv` and the March report (v1.5.3) are updated; March
  net intensity is now 137.4 BDL / 133.2 proxy, with March flagged as a vacation-atypical month.

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-04
archive_slot: april
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/monthly_summary.csv)

DATA ENTERED
  HDD65:           472.3        (HA proxy → monthly_summary; BDL official 412 in bdl_degree_days.csv)
  Gas_CCF:         59.0          Gas_Cost: 117.77
  DHW_CCF:         13.2810       (13.7727 Thm × 0.9643)
  Elec_kWh:        285.0         Elec_Cost: 81.48
  Heat_Total_Hrs:  38.4 (burner; 1F 20.1 / 2F 18.3 by Resideo 23:21 split)
  DHW_Op_Hrs:      11.0          DHW_Recirc_Hrs: 32.0

VALIDATION
  V1 range check:     FLAG — Gas −61% / Elec −34% vs trailing-3-mo avg; seasonal shoulder
                      transition (expected), confirmed in context. PASS in seasonal terms.
  V2 direction check: PASS — gas and runtime fell with HDD; intensity favorable, not anomalous.
  V-HVAC-2 (±15% of 90.3): BDL basis 111.0 = +22.9% — shoulder-season elevation (expected, matches May +23%); proxy 96.8 = +7.2%.
  V3 prior data:      PRESENT.

METRICS (before → after / YoY)
  Heating Intensity (net, BDL):  130.9 → 111.0 CCF/1k HDD  (−15.2% YoY)  [proxy: 128.8 → 96.8, −24.8%]
  HVAC Runtime:             50.0 → 38.4 hrs          (−23.2% YoY, on +11.9% HDD)
  DHW:                      20.66 → 13.28 CCF        (−35.7% YoY)
  Runtime/HDD:              7.11 → 4.88 min/HDD       (−31.4% YoY)

FLAGS
  Intensity methodology corrected to net basis (v1.5.1) across full column — review before commit.
  CPH=2 first-month signal confounded with mild April + CSV-derived cycle metrics.

COMMIT MESSAGE (ready to use)
  git commit -m "2026.04: Add April HVAC data — 111.0 CCF/1k HDD (net, BDL official); proxy 96.8; intensity column to net basis; add BDL degree-day basis"

README UPDATE NEEDED: NO — UA within prior documented range; no new record; methodology note already in report.
```

---

*Report generated using Home Assistant archived billing data, Navien tankless telemetry,
Resideo thermostat zone runtime, HA history_stats sensors, and daily HDD tracking via Hartford
weather proxy.*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + Navien NPE-240S2 tankless DHW.
Two-zone forced air, 2,440 sq. ft., East Hampton CT.*
