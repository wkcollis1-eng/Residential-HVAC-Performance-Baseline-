# HVAC Performance Update: May 2026

**Version:** 1.7.2
**Date:** June 17, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut
**Methodology:** Heating Intensity on **net space-heating gas** (total − Navien DHW), per v1.5.1.

**Revision 1.7.1 (June 18, 2026):** Official Bradley/KBDL degree days (ACIS) now incorporated (`bdl_degree_days.csv`). Heating Intensity is dual-basis. On the official BDL basis May net intensity is **111.1 CCF/1k HDD** (proxy 114.2) and is **flat with April's 111.0** — the proxy's apparent April→May +18% “mild-month” rise was an artifact of the proxy over-counting April HDD. Conclusions corrected below; runtime/HDD remains proxy-basis.

> **Data-integrity advisory (read first):** May 2026 carries three caveats that affect the
> runtime data — an HA outage (May 16–22), a thermostat swap (Honeywell → Ecobee, ~May 29), and a
> cooling-instrumentation gap. Billing, DHW, and HDD figures are full-month and clean; **runtime,
> zone, and CDD figures are flagged throughout.** See §5 and FLAGS.

---

## Executive Summary

May 2026 is the season-transition month: residual heating tailing off, cooling season opening,
and the controller changing hands mid-month. It was a month of weather extremes — a cold early
half (216 HDD, +26.7% YoY) followed by a hot late half that drove the first meaningful cooling of
the year (20.2 hours vs 1.0 last May). The clean signals are favorable on the bills: gas was
essentially flat YoY (+2.6%), DHW savings held at −25.4%, and electricity fell 33%. Net heating
intensity is 111.1 CCF/1k HDD on the official BDL basis (proxy 114.2), essentially **flat with
April's 111.0** — not a rise. The proxy's April→May jump (96.8 → 114.2) was an artifact of the
proxy over-counting April HDD; on official weather both months read the same shoulder-season ~111,
~23% above baseline. The runtime story
is real but its precision is limited this month by the outage and the controller swap.

**Key May 2026 Findings:**

| Metric | Value | Note |
|---|---|---|
| Total Gas Consumption | 39.0 CCF | +2.6% YoY; −33.9% MoM |
| Weather Severity | 222 HDD65 / 57 CDD65 *(BDL official)* | proxy 216.0 HDD; BDL now captured (ACIS) |
| Net Space-Heating Gas | 24.67 CCF | mild-month regime |
| **Heating Intensity** *(net, BDL)* | **111.1 CCF/1k HDD** | −3.1% YoY; flat with April (proxy: 114.2 / +3.6%) |
| DHW Consumption | 14.33 CCF | −25.4% YoY; savings narrowing as predicted |
| HVAC Heating Runtime | 24.0 hrs *(Resideo basis)* | overlap-inclusive; burner-equiv ~20.9 |
| **Cooling Runtime** | **20.2 hrs** | first of 2026; 17 Honeywell + 3.2 Ecobee |
| Electric | 311 kWh / $82.66 | −33.0% kWh / −41.7% $ YoY |
| Zone Balance (1F) | 33.3% *(Resideo basis)* | not comparable to burner-basis months |

> **Methodology / basis note:** Intensity is net-basis per v1.5.1. May heating runtime and the
> 8/16 zone split come from Resideo thermostat logs (the HA burner accumulator lost May 16–22),
> which count overlapping zone calls twice — so `Heat_Total` (24.0) sits ~15% above the
> burner-equivalent (~20.9) used in other months. Cooling (20.2 h) is Resideo + Ecobee combined.

**Interpretation:** Bill-side, May is a quiet, favorable month: flat gas on a colder May, DHW
savings intact, and a large electric drop. The electric −33% lands almost entirely in the
weather-independent base load and the dehumidifier (no AC in May 2025 to explain it away);
isolating which would need the Shelly plug series. The heating intensity “rising from April (96.8
→ 114.2)” was a proxy artifact — on official BDL weather April and May are both ~111, flat — so
there is no mild-month step to explain and certainly no degradation. The month's real news is operational: cooling season
is open and the controller transition is underway, both of which set up June as the first clean
read on the new Ecobee regime.

---

## Table of Contents
1. [Year-over-Year Analysis](#year-over-year-analysis)
2. [Month-over-Month Analysis](#month-over-month-analysis)
3. [DHW Performance Update](#dhw-performance-update)
4. [HDD & Cooling Methodology Note](#hdd--cooling-methodology-note)
5. [HVAC Runtime Performance](#hvac-runtime-performance)
6. [Recommendations](#recommendations)

---

## Year-over-Year Analysis

### May 2026 vs May 2025

| Metric | May 2025 | May 2026 | YoY Change | Interpretation |
|---|---|---|---|---|
| **Total Gas** | 38.0 CCF | 39.0 CCF | +2.6% | Flat, on a colder May |
| **DHW (Navien)** | 19.21 CCF | 14.33 CCF | **−25.4%** | Recirc savings, narrowing (see §3) |
| **Space Heating** *(net)* | 18.79 CCF | 24.67 CCF | +31.3% | More heating — colder early May |
| **HDD65 (BDL official)** | 164 | 222 | +35.4% | Colder May 2026 (official) |
| **HDD65 (HA proxy)** | 170.5 | 216.0 | +26.7% | Proxy under-counts May 2026 vs BDL |
| **Heating Intensity** *(net, BDL)* | **114.6 CCF/1k HDD** | **111.1 CCF/1k HDD** | **−3.1%** | Flat (proxy basis: +3.6%) |
| **Electric** | 464 kWh / $141.84 | 311 kWh / $82.66 | **−33.0% / −41.7%** | Large drop — base load + dehumidifier |
| **Cooling Runtime** | 1.0 hr | 20.2 hrs | — | First real cooling of 2026 |
| HVAC Heating Runtime | 7.0 hrs | 24.0 hrs *(Resideo)* | *see note* | Basis change — not directly comparable |
| Zone Balance (1F) | 57.1% *(burner)* | 33.3% *(Resideo)* | *not comparable* | Different basis |

**Key Insight:** The trustworthy comparisons all point mild-and-favorable: gas flat, DHW down a
quarter, intensity flat, and a one-third cut in electricity. The electric drop is the standout —
and notable because May 2025 had essentially no AC (1 cooling hour) to mask anything, so the
−153 kWh sits in base load and the dehumidifier, not cooling. The remaining rows carry warnings:
heating runtime jumped 7 → 24 h, but May 2026 was both colder *and* measured on the
overlap-inclusive Resideo basis, while May 2025 used burner hours off a tiny 7-hour baseline — so
that comparison is not clean and should not be quoted as a runtime regression. Zone balance is
likewise on two different bases and not comparable this month.

---

## Month-over-Month Analysis

### Natural Gas (April 2026 → May 2026)

| Metric | April 2026 | May 2026 | MoM Change |
|---|---|---|---|
| Total CCF | 59.0 | 39.0 | −33.9% |
| Space Heat CCF *(net of DHW)* | 45.72 | 24.67 | −46.0% |
| DHW CCF (Navien) | 13.28 | 14.33 | +7.9% |
| HDD65 *(BDL official)* | 412 | 222 | −46.1% |
| **Heating Intensity** *(net, BDL)* | **111.0 CCF/1k HDD** | **111.1 CCF/1k HDD** | **+0.1% (flat)** |

**Analysis:** Space-heating gas fell 46% as HDD dropped. On the HA proxy this lifted intensity
+18% (the classic mild-month signature); on the **official BDL basis intensity is flat — 111.0
(April) → 111.1 (May)** — because BDL did not over-count April the way the proxy did. The proxy's
+18% step was therefore mostly its own April HDD error, not physics; either way April's 96.8 was a
weather/HDD-source artifact, not a sustained CPH=2 gain. DHW ticked up 7.9% MoM, normal as the
recirculation loop works a touch harder against cooler morning starts early in the month.

### Electric & Cooling (April 2026 → May 2026)

| Metric | April 2026 | May 2026 | MoM Change |
|---|---|---|---|
| Electric | 285 kWh | 311 kWh | +9.1% |
| Cooling Runtime | 0.0 hrs | 20.2 hrs | season open |

**Analysis:** Electricity rose 9% MoM as the dehumidifier and first AC cycles came online — modest,
and consistent with a late-month-only cooling load. June will show the first full cooling-season
electric step.

---

## DHW Performance Update

### Recirculation Optimization — Savings Narrowing as Predicted

| Metric | May 2025 *(24 hr recirc)* | May 2026 *(15 hr recirc)* | Change |
|---|---|---|---|
| DHW Gas (Navien) | 19.21 CCF | 14.33 CCF | **−25.4%** |
| DHW Operating Hours | 10 hrs | 12 hrs | +20% |
| DHW Recirc Hours | 58 hrs | 35 hrs | −39.7% |
| Implied gas per operating hour | 1.92 CCF/hr | 1.19 CCF/hr | −38.0% |

**Note:** The YoY DHW reduction stepped down from −35.7% (April) to −25.4% (May). This is the
inlet-temperature effect the March report anticipated: as the municipal supply warms through
spring, the per-gallon energy demand falls for *both* years, compressing the percentage gap that
the recirc schedule change created. The per-operating-hour figure (−38%) shows the underlying
efficiency gain is intact; the headline percentage simply narrows seasonally. Recirc hours fell
to 35 (from 58), confirming the 9 PM–6 AM off-schedule is holding.

---

## HDD & Cooling Methodology Note

**Heating (HDD):** Official BDL (ACIS) records **222 HDD / 57 CDD** for May; the HA proxy logged
216.0 HDD (−6, a −2.7% under-count). Net intensity is **111.1 on the BDL basis** (114.2 proxy).
Unlike April, the two bases nearly agree this month, so the basis choice barely moves the May
reading.

**Cooling (CDD / runtime):** This is the weak spot of the month. The HA cooling accumulator logged
only ~3.8 CDD and 3.2 cooling hours, because the cooling instrumentation came online late and the
May 16–22 outage swallowed a warm stretch. The **reliable** cooling figure is the thermostat
runtime: 20.2 hours total (17 h Honeywell through ~May 28, 3.2 h Ecobee from ~May 29). Use the
Resideo/Ecobee runtime, not the HA CDD, as the May cooling metric. CDD-based cooling intensity
should not be computed for May; begin clean CDD tracking in June.

---

## HVAC Runtime Performance

### Heating — basis caveat

May heating runtime (24.0 h) and the 1F/2F split (8 / 16) come from Resideo thermostat logs
because the HA burner accumulator was incomplete after the May 16–22 outage (it read 11.8 h,
which is below the physical floor set by the 16-hour 2F call, so it is provably short). Resideo
counts overlapping zone calls twice, so this `Heat_Total` runs ~15% above the burner-equivalent
(~20.9 h) used in every other month. **Consequences:**

- `Runtime_Per_HDD_Min` (6.67) and `Zone_Balance_1F_Pct` (33.3%) are on the Resideo basis and are
  not directly comparable to prior burner-basis months. Do not trend the May zone balance against
  April's 52.3%.
- The whole-month figure is best read qualitatively: light residual heating, tapering through the
  month, with the second floor calling more than the first in the cold early days.

### Cooling — season open across a controller change

Cooling came online for 2026: 20.2 hours, all on the second floor, spanning the thermostat swap
(17 h Honeywell + 3.2 h Ecobee). This is the start of the Ecobee-vs-Honeywell baseline period —
keep the split tagged by controller. The first *full* Ecobee cooling month is June.

### Cycling / CPH=2 — deferred to June

A clean CPH=2 cycle read is not possible for May: the outage removed a week of daily data and the
Ecobee swap changed the controller late in the month. The April directional signal (cycle length
6.6 → 8.2 min) stands as the last clean CPH=3→2 datapoint. Resume cycle analysis with June, the
first uninterrupted full month under the Ecobee controller, using the HA monthly cycle sensors.

---

## Recommendations

### Monitoring Priorities

1. **June = first clean Ecobee month.** Treat it as the reset point for cycle/CPH analysis and the
   anchor for the Ecobee-vs-Honeywell comparison. Tag all runtime by controller; do not blend
   across the late-May swap.

2. **Fix cooling instrumentation before peak season.** May exposed that HA logged only 3.2 of 20.2
   actual cooling hours and ~3.8 CDD. Verify the cooling accumulators and CDD capture are firing
   correctly (this ties into the `csv_manager`/capture review) so June cooling intensity is
   trustworthy.

3. **Dehumidifier / base-load attribution.** The −33% electric YoY lives in base load + the
   dehumidifier. Pull the Shelly plug series to split it — this is the same data that would close
   the long-standing base-load-vs-moisture question in the load decomposition.

4. **DHW inlet-temperature watch.** The YoY DHW savings narrowed (−35.7% → −25.4%) exactly as the
   inlet-warming hypothesis predicted. Track whether it continues to compress through summer; the
   per-operating-hour figure (−38%) is the cleaner efficiency indicator to follow.

5. **12-Month Rolling UA.** Unchanged — shoulder/cooling months don't move the determination; the
   read comes with Jan–Feb 2026 cycling into the window.

### Pending / Data Hygiene

- **May 16–22 backfill (if recoverable):** If HA's recorder retained furnace runtime through the
  outage, recompute the complete May burner total and replace the Resideo-basis heating runtime
  with a burner-basis figure (removing the §5 caveat). If HA was down, the Resideo basis stands as
  flagged.
- **Intensity methodology correction:** carry the net-basis `monthly_summary.csv` correction from
  the April update into the same commit.
- **Q1 reconciliation (RESOLVED, June 18 2026):** March DHW resolved to the archive value **8.74 CCF**
  (2-week vacation; repo's 15.0 was an entry error) and February gas cost corrected to 274.7. `monthly_summary.csv`
  and the March report (v1.5.3) are updated; March net intensity is now 137.4 BDL / 133.2 proxy (vacation-atypical).

---

## Monthly Update Record (skill OUTPUT FORMAT)

```
target_month: 2026-05
archive_slot: may
Repo(s) updated: Residential-HVAC-Performance-Baseline- (data/monthly_summary.csv)

DATA ENTERED
  HDD65:           216.0        (HA proxy → monthly_summary; BDL official 222 / CDD 57 in bdl_degree_days.csv)
  Gas_CCF:         39.0          Gas_Cost: 85.79
  DHW_CCF:         14.3296       (14.8601 Thm × 0.9643)
  Elec_kWh:        311.0         Elec_Cost: 82.66
  Heat_Total_Hrs:  24.0  [Resideo basis — 1F 8.0 / 2F 16.0; burner-equiv ~20.9]
  Cool_Total_Hrs:  20.2  [2F; 17 Honeywell + 3.2 Ecobee]
  DHW_Op_Hrs:      12.0          DHW_Recirc_Hrs: 35.0

VALIDATION
  V1 range check:     FLAG — Gas −73% / Elec −20% vs trailing-3-mo avg; seasonal (expected). PASS in context.
  V2 direction check: PASS — gas/HDD consistent; intensity in mild-month band, not anomalous.
  V-HVAC-2 (±15% of 90.3): net intensity 111.1 BDL (+23.0%) / 114.2 proxy (+26.5%) — shoulder-season elevation, expected; matches April.
  V3 prior data:      PRESENT.

METRICS (YoY)
  Heating Intensity (net, BDL):  114.6 → 111.1 CCF/1k HDD  (−3.1%)  [proxy: 110.2 → 114.2, +3.6%]
  DHW:                      19.21 → 14.33 CCF         (−25.4%)
  Electric:                 464 → 311 kWh             (−33.0%)
  Gas:                      38.0 → 39.0 CCF           (+2.6%)
  Cooling runtime:          1.0 → 20.2 hrs            (season open)

FLAGS
  HA outage May 16–22 → heating runtime/zone on Resideo (overlap-incl) basis, not burner.
  Controller swap ~May 29 (Honeywell→Ecobee) → split-controller month; CPH/cycle analysis deferred to June.
  Cooling logging incomplete (HA 3.2 h / 3.8 CDD vs 20.2 h actual) → use thermostat runtime, not CDD.
  Runtime/zone YoY not comparable (basis change + small 2025 baseline).

COMMIT MESSAGE (ready to use)
  git commit -m "2026.05: Add May HVAC data — 111.1 CCF/1k HDD (net, BDL official); proxy 114.2; runtime Resideo-basis (HA outage); cooling season open 20.2 h"

README UPDATE NEEDED: NO — within prior documented ranges; data-integrity notes captured in report.
```

---

*Report generated using Home Assistant archived billing data, Navien tankless telemetry,
Resideo + Ecobee thermostat runtime, HA history_stats sensors, and daily HDD tracking via Hartford
weather proxy.*
*System: single-stage gas furnace (60,556 BTU/hr, 0.95 AFUE) + Navien NPE-240S2 tankless DHW.
Two-zone forced air, 2,440 sq. ft., East Hampton CT. Thermostats: Honeywell Lyric T6 Pro →
Ecobee Smart Enhanced (~May 29, 2026).*
