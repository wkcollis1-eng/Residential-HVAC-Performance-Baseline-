# H1 Overview: January–June 2026 vs 2025

**Version:** 1.0.0
**Date:** July 7, 2026
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, East Hampton CT
**Sources:** the six monthly reports (`JANUARY`–`MAY_2026_UPDATE.md` + the June 2026 report), `data/monthly_summary.csv`, and authoritative Bradley/KBDL degree days (`bdl_degree_days.csv`, ACIS).
**Basis note:** All figures use the **report basis** — net space-heating gas for intensity, **BDL official** degree days, and **bill-date-month** attribution for electric/gas (see §6; two repo CSVs use different conventions and are not mixed in here).

---

## Executive Summary

The first half of 2026 was **materially colder than 2025** — +12.2% heating degree-days (3,782 vs 3,371 BDL) — yet the house consumed **essentially the same total gas** (+2.2%) and **less electricity** (−9.9% kWh). That combination is the headline: on a colder half-year, the envelope-plus-equipment performed at or slightly better than 2025, and the DHW recirculation program did the heavy lifting that kept the gas bill flat.

Three durable findings, and two things that are *not* signals:

1. **Heating efficiency held on colder weather.** Aggregate net heating intensity was **127.7 CCF/1k HDD vs 129.6 in 2025 (−1.5%)**. Space-heating gas rose +10.5% and heating runtime +6.7%, both *less* than the +12.2% HDD increase — the furnace tracked weather, it did not degrade.
2. **The DHW recirc program is the standout.** DHW gas fell **−33.9% H1** (120.0 → 79.3 CCF) on a **−33.4% cut in recirculation hours** (344→229). Each year's H1 includes the household's normal recurring 1–2 week winter vacation, so the aggregate is a fair comparison. This offset the weather-driven space-heat increase almost exactly, which is *why* total gas stayed flat.
3. **Electricity fell −9.9% kWh — but −22.2% in dollars.** Usage dropped 2,656 → 2,394 kWh; the bill dropped $814.69 → $633.75. The extra came from a **−13.7% effective-rate decline** ($0.307 → $0.265/kWh), widening to −20.7% by June. Usage fell hardest April–June (−17% to −33%). **Gas cost, by contrast, was flat (+2.8%)** — no rate tailwind (+0.7%/CCF), with the −30% DHW-cost drop offsetting a +13% weather-driven heating-cost rise.

One thing to read carefully: the recurring winter **vacation fell in different months** (Feb 2025 vs Mar 2026), so those two months' individual YoY cells are distorted in opposite directions and are read as a pair, not singly — the vacation is normal recurring load and stays *in* the totals. And the **May heating-runtime jump** is a Resideo-vs-burner-hours basis change, not a real regression.

---

## Master Comparison — H1 2025 vs H1 2026

Gas, DHW, and space-heat in CCF; HDD/CDD are BDL official; intensity is net CCF/1k HDD (BDL); electric in kWh; runtime in heating-hours.

| Month | HDD (BDL) | Gas CCF | DHW CCF | Space-Heat CCF | Net Intensity (BDL) | Electric kWh | Heat Runtime |
|---|--:|--:|--:|--:|--:|--:|--:|
| **Jan** | 1,125 → 1,263 *(+12%)* | 161 → 168 | 22.83 → 17.76 | 138.2 → 150.2 | 122.8 → 119.0 *(−3.1%)* | 461 → 515 *(+12%)* | 198 → 220 |
| **Feb** ✈ | 959 → 1,120 *(+17%)* | 154 → 175 | 18.12 → 13.63 | 135.9 → 161.4 | 141.7 → 144.1 *(+1.7%)* | 447 → 404 *(−10%)* | 138 → 158 |
| **Mar** ✈ | 687 → 744 *(+8%)* | 106 → 111 | 22.47 → 8.74 | 83.5 → 96.0 | 121.6 → 137.4 *(+13%)* | 314 → 374 *(+19%)* | 96 → 81 |
| **Apr** | 415 → 412 *(−1%)* | 75 → 59 | 20.66 → 13.28 | 54.3 → 45.7 | 128.8 → 111.0 *(−15%)* | 344 → 285 *(−17%)* | 50 → 38 |
| **May** | 164 → 222 *(+35%)* | 38 → 39 | 19.21 → 14.33 | 18.8 → 24.7 | 114.6 → 111.1 *(−3.1%)* | 464 → 311 *(−33%)* | 7 → 24 † |
| **Jun** | 21 → 21 *(flat)* | 23 → 17 | 16.72 → 11.53 | 6.3 → 5.5 | N/A *(no heating)* | 626 → 505 *(−19%)* | 0 → 0 |
| **H1 total** | **3,371 → 3,782 (+12.2%)** | **557 → 569 (+2.2%)** | **120.0 → 79.3 (−33.9%)** | **437 → 483 (+10.5%)** | **129.6 → 127.7 (−1.5%)** | **2,656 → 2,394 (−9.9%)** | **489 → 522 (+6.7%)** |

✈ The recurring 1–2 week vacation landed in **Feb 2025** (DHW op-hours halved to 6) but **Mar 2026** (DHW −36%). Because the trip is in a different month each year, the individual **Feb** and **Mar** YoY cells are distorted in opposite directions and should be read as a *pair*, not singly — the H1 aggregate absorbs one trip per year and is the comparable unit. Vacation months are *included* (they are normal, recurring load), not excluded. † May heating runtime crosses a measurement-basis change and is not YoY-comparable.

---

## 1. Heating — colder weather, efficiency held

H1 2026 ran **+12.2% HDD** over 2025 (a colder Jan/Feb and a much colder May). Against that, space-heating gas rose only **+10.5%** and heating runtime **+6.7%** — both below the weather increase. The clean way to see it is aggregate net intensity: **129.6 → 127.7 CCF/1k HDD, −1.5%**. Per month on the authoritative BDL basis, intensity was flat-to-improved (Jan −3.1%, Feb +1.7% within baseline CV, Apr −15.2%, May −3.1%) — with one caveat: the net-intensity method has a known upward bias in the **vacation month**, because low vacation-DHW means less is subtracted from total gas, inflating the apparent space-heat share. That bias shows up in Mar 2026 (+13%) and would show in Feb 2025 the same way; it moves with the trip. The aggregate is unaffected (each year carries one vacation), and for any single vacation month the robust read is total-gas-per-HDD, which had March 2026 at −3.3% YoY. The furnace is performing on-baseline; the higher absolute gas is weather, not degradation.

One open item carried from the winter reports: the 12-month rolling UA calculation showed a ~9.5% elevation, but the reports are explicit that **March alone can't confirm whether that's persistent** — it needs the Jan–Feb 2027 heating season to cycle through the window. H1 2026 does not resolve it either way.

## 2. DHW — the recirculation program is the win

The deliberate recirc-schedule reduction (started mid-January, 24→15 hr/day, then tuned monthly) is the strongest efficiency result of the half-year. DHW gas fell **−33.9% H1** (120.0 → 79.3 CCF), tracking a **−33.4% cut in recirc hours** (344 → 229). This figure **includes the household's normal recurring 1–2 week winter vacation** in each year — the right way to handle a routine event. The wrinkle is timing: the trip fell in **Feb 2025** (DHW op-hours halved to 6) but **Mar 2026** (DHW −36%), so the individual Feb and Mar cells are pulled in opposite directions (Feb YoY understates the recirc effect because 2025-Feb was itself vacation-low; Mar overstates it at −61% because 2026-Mar was the low one). Read Feb+Mar as a block (40.6 → 22.4 CCF) or, better, use the H1 aggregate, which carries exactly one trip per year. The January report's standby-loss analysis found ~59% of DHW gas was recirculation standby — well above Navien's 23% factory estimate — which is why cutting recirc hours pays back so directly. This −40.7 CCF of DHW savings is what absorbed the +46 CCF weather-driven space-heat increase and kept total gas flat.

> **To confirm (Bill):** the DHW signals place the 2025 trip in February and the 2026 trip in March, but the March 2026 **DHW op-hours still read 12** (normal), which is inconsistent with a 2-week absence — the op-hours archive may not have captured that month. Confirming the actual 2025/2026 vacation dates (and whether the thermostat is set back while away) would let me annotate the month pairing exactly and decide whether vacation space-heat needs its own small adjustment.

## 3. Total gas — flat on a colder half, in both volume and dollars

Total gas was **+2.2%** (557 → 569 CCF) on **+12.2% HDD**. Decomposed: space heat +46 CCF (weather) minus DHW −40.7 CCF (recirc program) ≈ net +12 CCF. The house burned almost the same gas it did in a warmer 2025 — the efficiency gain is real and it lives in DHW.

The cost side (now from the authoritative HA gas archive) tells the same story in dollars, and this is the direct contrast to electricity:

| Gas H1 | 2025 | 2026 | YoY |
|---|--:|--:|--:|
| **Total cost** | $951.68 | $978.69 | **+2.8%** |
| — Heating cost | $727.42 | $822.48 | **+13.1%** |
| — DHW cost | $224.26 | $156.21 | **−30.3%** |
| Effective rate | $1.709/CCF | $1.720/CCF | **+0.7%** |

Total gas cost was **essentially flat (+2.8%)** because a **+13.1% heating-cost increase** (colder weather, tracking space-heat CCF +12.1%) was almost entirely offset by a **−30.3% DHW-cost drop** (the recirc program — ~$68 saved, absorbing ~72% of the +$95 weather-driven heating increase). Unlike electricity, gas had **no rate tailwind**: the effective rate rose +0.7% ($1.709 → $1.720/CCF). So the electric bill fell 22% on both lower usage *and* a −14% rate, while the gas bill held flat on flat rates with the DHW program doing all the offsetting work.

> **Cost-split method:** heating and DHW costs are a **derived allocation** — the gas bill is not metered by end use, so each month's blended $/CCF (fixed charge included) is apportioned by volume (DHW share = DHW CCF ÷ total CCF). DHW and heating therefore carry the same effective rate by construction; the split reflects *volume*, not a separate DHW tariff. Gas costs are now fully archive-verified: 2026 H1 from the HA `gas_archive_*` entities, 2025 H1 from `monthly_summary.csv` (whose 2025-H2 values match the archive exactly, corroborating the vintage). The lone stale cell — Feb 2026 gas cost $248.00 in the committed CSV — is superseded here by the archive's **$274.70**.

## 4. Electricity — down, with a rate tailwind

Electric use fell **−9.9% kWh H1** (2,656 → 2,394). The pattern is seasonal: Jan +12% and Mar +19% (winter blower runtime on colder months), then April–June down hard (−17%, −33%, −19%). May and June are the standouts — May 2025 had essentially no AC to mask anything, so the −153 kWh sits in base load and the dehumidifier, not cooling.

On cost, the full H1 picture (now reconciled to the authoritative HA `electric_archive_*` values) is a **−22.2% drop** ($814.69 → $633.75) — larger than the −9.9% usage drop because the **effective rate fell −13.7%** ($0.3067 → $0.2647/kWh). Per month: Jan −2.8%, Feb −20.1%, Mar +3.1%, Apr −25.6%, May −41.7%, Jun −36.0%. The rate tailwind is modest early (−10% to −13.5% Jan–May) and jumps in June (−20.7%, the summer supply-rate reset) — so the headline "big rate drop" is really a June effect, not a flat H1 one.

| Electric H1 | 2025 | 2026 | YoY |
|---|--:|--:|--:|
| kWh | 2,656 | 2,394 | **−9.9%** |
| Cost | $814.69 | $633.75 | **−22.2%** |
| Effective rate | $0.3067 | $0.2647 | **−13.7%** |

## 5. Cooling — onset, not yet a YoY story

Cooling came online at the end of H1: ~1 hr (May 2025) → 20.2 hr (May 2026) → 84.6 hr (June 2026). This is the first season under the Ecobee controller with SEM-Meter instrumentation arriving late June, so H1 establishes the *baseline* rather than a YoY comparison. The June report's first Ecobee-vs-Honeywell read (26.7 vs 30.0 min/CDD BDL, −11%) is a single data point; July is the first fully-metered cooling month.

## 6. Data integrity & caveats — read before quoting

These are the reasons specific figures above are flagged, and where the committed CSVs disagree:

- **Three stale cost cells in `monthly_summary.csv` — corrected from the HA archives.** Electric: **Feb 2026 = $111.48** (CSV $139.48) and **Mar 2026 = $103.92** (CSV $100.84). Gas: **Feb 2026 = $274.70** (CSV $248.00 — identical to Feb 2025, and the April/May reports claim this was fixed but the committed CSV still shows $248.00). All other 2026 cost cells and every kWh/CCF cell match their archives. **Action:** repair `Elec_Cost` (2026-02, 2026-03) and `Gas_Cost` (2026-02) in the committed CSV; the report-vs-CSV sync gap on the gas cell is worth a look in the monthly-update workflow.
- **Two electric attribution bases in the repo.** `monthly_summary.csv` uses **bill-date-month**; `monthly_electricity_eversource.csv` uses **consumption-month** — they differ by exactly one month (e.g., summary 2025-06 = 626 kWh = the 6/10 bill; eversource 2025-06 = 1,129 = the 7/14 bill). This overview uses the summary/report (bill-date) basis throughout for internal consistency. Do not mix the two files.
- **Gas file month-offset.** `monthly_gas_scg.csv` is shifted one month from `monthly_summary.csv` (scg 2025-01 = 154 = summary 2025-02). Same attribution issue; the reports use the summary basis.
- **Vacation is recurring load — included, not excluded.** The household routinely takes a 1–2 week vacation in the Feb–Apr window each year, so it is treated as normal load and kept in all totals. The only complication is timing: the DHW signals place it in **Feb 2025** (op-hours 6) and **Mar 2026** (DHW −36%), so those two months' individual YoY cells are distorted in opposite directions and are read as a pair. The H1 aggregate carries one trip per year and is the correct comparison unit. *(Open: March 2026 DHW op-hours read 12, inconsistent with a 2-week absence — see §2 confirm-note.)*
- **May heating-runtime basis change.** May 2026 runtime (24 h, Resideo overlap-inclusive) vs May 2025 (7 h, burner hours) are different bases — not a regression, not YoY-comparable.
- **HDD proxy vs BDL.** All intensity figures here use BDL official (ACIS). The HA `outdoor_temp_live` proxy over-counts in shoulder months (Mar/Apr) and under-counts in others; the reports standardized on BDL from the June-18 dual-basis revision.

---

## Bottom Line

On a **12% colder** half-year, the house held total gas flat (+2.2%), cut electricity **−9.9% kWh / −22.2% in dollars**, and kept heating efficiency steady (−1.5% intensity). The single biggest lever was the **DHW recirculation program** (−34% DHW on −33% recirc hours), which offset the weather-driven heating increase almost exactly. The efficiency picture is genuine. The recurring winter vacation is kept in the totals (it fell in Feb 2025 vs Mar 2026, so those months are read as a pair); the May runtime jump is a basis change, not a regression; and the one data-repair item is two wrong `Elec_Cost` cells (2026-02, 2026-03) in `monthly_summary.csv`, now corrected from the HA archive.

*Weather: Bradley/KBDL (ACIS/xmACIS2, base 65°F). Metrics reconciled from the committed monthly reports and `monthly_summary.csv`; source discrepancies flagged in §6.*
