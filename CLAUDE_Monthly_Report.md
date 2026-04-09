# CLAUDE_Monthly_Report.md
# Monthly HVAC Performance Report — Claude Code Prompt
# Version: 1.0  |  Property: 2,440 sq ft Colonial, East Hampton CT (06424), Climate Zone 5A
# Usage: Place in repo root. Run: claude "Follow CLAUDE_Monthly_Report.md to write the [Month] [Year] report"

---

## TASK

Write the monthly HVAC performance report for **[MONTH] [YEAR]**. Produce the
following outputs **in this order**:

1. Standalone report → `reports/[YYYY-MM]_hvac_report.md`
2. Prepend newest entry → `UPDATES.md`
3. Update metrics → `README.md` (§10 defines exactly what changes)
4. Append computed row → `data/monthly_summary.csv` (§8)

Read ALL of the following before writing a single line:
1. This file (complete)
2. `README.md` (current — identify every block that must be updated)
3. `METHODOLOGY.md` (billing-aligned calculation rules)
4. `SYSTEM_SPECIFICATIONS.md` (hardware constants)
5. `data/monthly_gas_scg.csv` (gas bills through reporting month)
6. `data/monthly_dhw_navien.csv` (Navien meter through reporting month)
7. `data/monthly_hvac_runtime.csv` (thermostat runtime through reporting month)
8. `data/daily_temperature.csv` (daily HDD/CDD through reporting month)
9. `data/monthly_summary.csv` (all prior computed metrics — use for YoY and MoM)
10. `UPDATES.md` (read the prior month's entry to verify MoM continuity)

**Do not begin writing until all files are read and all inputs in §3 are computed.**

---

## §1 — SYSTEM CONSTANTS (never derive from data — read from SYSTEM_SPECIFICATIONS.md)

Cross-check these against `SYSTEM_SPECIFICATIONS.md` before every use:

| Constant | Value | Source |
|---|---|---|
| Furnace input rate | 60,556 BTU/hr | Manufacturer submittal |
| AFUE | 0.95 | Manufacturer submittal |
| Furnace output rate | 57,528 BTU/hr | = input × AFUE |
| BTU per CCF | 103,700 BTU/CCF | SCG spec |
| Balance point ratio (HDD59/HDD65) | 0.844 | Calibrated from 4-yr dataset |
| Fireplace annual heat | 3.6 MMBTU/yr | Estimated; embedded in baseline |
| Floor area | 2,440 sq ft | As-built |
| Annual HDD65 normal | 5,270 HDD | 18-year CT climate average |
| Efficiency baseline | 90.3 CCF/1k HDD | 2022–2024 calibrated baseline |
| UA baseline | 493 BTU/hr-°F | Derived from 4-yr dataset |
| EUI baseline | 41.7 kBTU/ft²-yr | 2022–2024 calibrated baseline |
| Blower ECM draw | 0.21 kW | Measured |
| AC condenser draw | 4.9 kW | Nameplate |

**CRITICAL — wrong defaults that appear in other analyses and must never be used:**
- ❌ Furnace input = 100,000 BTU/hr (wrong — that is not this system)
- ❌ AFUE = 0.96 (wrong — submittal-verified value is 0.95)
- ❌ DHW ratio = fixed 28.1% of total gas (wrong — use Navien meter actuals)

---

## §2 — HDD DATA HIERARCHY

Use HDD in this priority order. Document which source is used in the report.

1. **Daily CSV sum** (`data/daily_temperature.csv` — sum `HDD65` for the month):
   This uses (high + low) / 2 method, aligns with prior Resideo export methodology.
   **Preferred for runtime/HDD calculation** (same source as runtime data).

2. **HA proxy archive** (if daily CSV not yet updated):
   Documented 2.3% annual undercount vs BDL, with monthly variation. Use if daily
   CSV is unavailable; note the source.

3. **BDL official** (NOAA KBDL station, Hartford Bradley):
   Most authoritative. Use for cross-checking. If gap > 5% vs daily CSV, document it.

**Known proxy directional errors to flag when present:**
- Jan/Feb: HA proxy typically undercounts (HA < BDL)
- March shoulder season: HA proxy can overcount (HA > BDL)
- Document actual gap when BDL monthly figure is available

---

## §3 — REQUIRED CALCULATIONS (compute all before writing)

Perform every calculation shown. Show the formula inline in your scratch work,
then use the result in the report. Do not round intermediate values — only round
final reported figures.

### 3A. Gas Load Decomposition

```
net_heat_ccf   = total_gas_ccf - dhw_navien_ccf
dhw_pct        = dhw_navien_ccf / total_gas_ccf × 100
```

**DHW source:** Always use Navien meter (`monthly_dhw_navien.csv`), never a
fixed ratio. If Navien data is missing for the month, state "DHW pending —
intensity not calculable this month" and do not publish an intensity figure.

### 3B. Heating Intensity

```
heating_intensity = (net_heat_ccf / hdd65_month) × 1000    [CCF/1k HDD]
```

⚠️ **COMMON ERROR — never use total gas in this formula.** The numerator is
`net_heat_ccf` (after Navien DHW subtracted). Using total gas inflates the
result by ~20–25% and produces a fundamentally different metric. Every
prior-month entry in `monthly_summary.csv` uses net heating gas — verify
your numerator matches before comparing.

### 3C. Rolling 12-Month Efficiency

```
trailing_gas_12m  = sum of net_heat_ccf for trailing 12 calendar months
trailing_hdd_12m  = sum of hdd65_month for same 12 months
efficiency_12m    = (trailing_gas_12m / trailing_hdd_12m) × 1000    [CCF/1k HDD]
```

This is the primary long-term performance metric. Update monthly.

### 3D. Building UA (monthly estimate — use cautiously Nov–Mar only)

```
ua_monthly = (net_heat_ccf × 103700 × 0.95) / (hdd65_month × 0.844 × 24)
```

⚠️ UA is only statistically reliable when ΔT is large (mean outdoor temp
< 40°F, typically Dec–Feb). Do not interpret UA as "envelope health" for
months with mean outdoor > 45°F. The rolling 12-month UA (from HA archives)
is more reliable than any single month estimate.

Add fireplace correction only in annual/12-month UA calculation:
```
ua_12m = (net_heat_ccf_12m × 103700 × 0.95 + 3,600,000) / (hdd_12m × 0.844 × 24)
```
The 3.6 MMBTU fireplace contribution is an annual estimate embedded in the
baseline — do not prorate it by month for monthly UA estimates.

### 3E. Runtime per HDD

```
runtime_per_hdd = (furnace_hours × 60) / hdd65_month    [min/HDD]
```

Use furnace heating hours only (not zone-summed, not cooling).
Use the **same HDD source** as 3B. Mixing sources produces spurious ratios.

### 3F. YoY and MoM Deltas

```
yoy_pct = (current_value / same_month_prior_year_value - 1) × 100
mom_pct = (current_value / prior_month_value - 1) × 100
```

Always compute delta from the **same metric** computed the **same way**.
If prior year used net heating gas, current month must also use net heating gas.
If prior year's figure in `monthly_summary.csv` was computed incorrectly,
note the discrepancy rather than propagating the error.

### 3G. Site EUI (monthly contribution, report annually only)

```
monthly_eui_contribution = (gas_ccf × 103.7 + elec_kwh × 3.412) / 2440
```

Report rolling 12-month EUI as trailing sum. Do not report a single month's
EUI in isolation — it has no meaning without annualization.

### 3H. DHW Performance

```
dhw_per_operating_hour = dhw_navien_ccf / dhw_operating_hours
```

Track this ratio monthly. Changes indicate Navien efficiency change or
recirc schedule change. The 2025 recirc optimization (off 9 PM – 6 AM)
reduced this from ~1.87 CCF/hr to ~1.25 CCF/hr — that baseline is
established; future changes from ~1.25 indicate new operational changes.

---

## §4 — SHOULDER SEASON RULES (March–May, September–October)

These rules apply whenever the monthly mean outdoor temperature exceeds 45°F.

**Do not write these things in shoulder-season months:**
- ❌ "Exceptional efficiency" when runtime/HDD is low
- ❌ "[X]% better than baseline" comparing a shoulder month to the annual baseline
- ❌ "No envelope issues detected" based on mild-month data
- ❌ Heating intensity comparison where one month is peak-heating and one is shoulder

**Required shoulder-season framing:**
- Runtime/HDD is structurally lower in mild months because each HDD represents
  a smaller temperature deficit. The annual baseline of 10.9 min/HDD is dominated
  by cold months; comparing March against it is not meaningful.
- Heating intensity (CCF/1k HDD) is structurally higher in shoulder months
  because furnace startup overhead is amortized over fewer HDD per firing event.
- The correct comparison for shoulder months is same-month prior year, not the
  annual baseline.
- UA estimates derived from shoulder-season months have low signal-to-noise and
  should not be used to draw envelope conclusions.

**When runtime/HDD drops below annual baseline (typical shoulder months):**
Write: "Runtime/HDD of [X] min/HDD is within the normal shoulder-season range.
For context, March [prior year] was [Y] min/HDD."
Do NOT write: "[X] min/HDD is [Z]% better than the [10.9] baseline."

---

## §5 — NARRATIVE VOICE AND CONSISTENCY RULES

### 5A. Tone and Authority Level

- Write in engineering third-person. No "I," no "we" referring to the author.
- Use hedged language only where genuine uncertainty exists:
  - "The data suggests..." — use when a finding has confounders
  - "The [metric] indicates..." — use when directly derived from measurement
  - "This is consistent with..." — use when confirming expected seasonal behavior
- Do not editorialize with positive framing unsupported by the numbers.
  If intensity went up, say it went up. Do not reframe deterioration as stable.

### 5B. Headline Findings — Rules

The Executive Summary bullet list must contain:
1. Total gas CCF — factual, always present
2. Weather (HDD65) — factual, always present
3. Net space heating gas — always present if Navien data available
4. Heating intensity (corrected formula) — always present if Navien available
5. DHW CCF — always present
6. Furnace runtime and runtime/HDD — always present for heating months
7. A closing interpretation sentence — must distinguish between seasonal
   patterns and genuine anomalies

### 5C. Comparing to Baseline — Rules

The baseline (90.3 CCF/1k HDD) is a **full-heating-season annual average**
calibrated from 2022–2024. It is only valid for comparison against:
- Rolling 12-month efficiency
- Full-year annual efficiency
- Individual months in the peak heating season (Dec, Jan, Feb) where ΔT is high

**Never compare an individual shoulder-season month's intensity against 90.3.**
Instead compare it to: same month prior year, or trailing 12-month figure.

### 5D. Describing Changes

| Situation | Correct language | Incorrect language |
|---|---|---|
| Metric improved vs prior year | "decreased [X]% YoY" | "exceptional," "outstanding" |
| Metric worsened vs prior year | "increased [X]% YoY — [explanation]" | Omit or reframe positively |
| Metric within 2% of prior | "consistent with prior year" | "stable" without checking |
| Shoulder metric vs annual | "within normal shoulder-season range" | "[X]% better than baseline" |
| Gap vs annual baseline | "[X] CCF/1k HDD above the [90.3] baseline" | "tightly clustered" without numbers |

### 5E. Causal Claims — Rules

Before stating a cause, verify it is supported by the available data:

- **DHW savings from recirc optimization:** ✓ Claim this when YoY DHW hours
  are equal and CCF is lower. ✗ Do not claim if operating hours also changed.

- **Weather-driven changes:** ✓ Claim when HDD change is proportional to
  gas change. ✗ Do not claim weather explains everything when intensity
  (normalized by HDD) also changed.

- **Modulation / efficiency mode:** ✗ This system uses a single-stage furnace
  (60,556 BTU/hr, no modulation). Never describe changes in CCF/runtime-hour as
  "modulation benefit." The furnace runs at full fire or off — always.

- **Envelope health:** ✓ Only assess from rolling 12-month UA.
  ✗ Never assess from a single month, especially shoulder months.

---

## §6 — REPORT TEMPLATE

Use this exact structure. Do not add or remove sections without reason.

```markdown
# HVAC Performance Update: [Month] [Year]

**Version:** [X.Y.Z]
**Date:** [actual date written]
**Property:** 2,440 sq. ft. Colonial, Climate Zone 5A, Central Connecticut

---

## Executive Summary

[2–3 sentence context: season, notable weather, one-line system status]

**Key [Month] [Year] Findings:**

| Metric | Value | Context |
|---|---|---|
| Total Gas Consumption | [X] CCF | [±%] MoM / [±%] YoY |
| Weather Severity | [X] HDD65 | [source]; BDL official = [Y] if available |
| Net Space Heating Gas | [X] CCF | = Total − Navien DHW |
| Heating Intensity | [X] CCF/1k HDD | [±%] vs [Month] [prior year] |
| DHW Consumption | [X] CCF | [±%] YoY |
| HVAC Runtime | [X] hrs at [Y] min/HDD | [context — see §5D rules] |
| [If cooling month] AC Runtime | [X] hrs | [CDD, runtime/CDD if available] |

**Interpretation:** [2–3 sentences. Distinguish seasonal from anomalous.
If peak heating month: compare intensity to 90.3 baseline and note deviation.
If shoulder month: compare to same-month prior year only.]

[If any v1.5.0-type corrections are present, include a correction note here.]

---

## Year-over-Year Analysis

### [Month] [Year] vs [Month] [Prior Year]

| Metric | [Month Prior] | [Month Current] | YoY Change | Interpretation |
|---|---|---|---|---|
| Total Gas | X CCF | X CCF | ±% | ... |
| DHW (Navien) | X CCF | X CCF | ±% | ... |
| **Space Heating** | **X CCF** | **X CCF** | **±%** | **net of DHW** |
| HDD65 | X | X | ±% | [source noted] |
| **Heating Intensity** | **X CCF/1k HDD** | **X CCF/1k HDD** | **±%** | net heating / HDD |
| HVAC Runtime | X hrs | X hrs | ±% | ... |
| Runtime / HDD | X min/HDD | X min/HDD | ±% | [seasonal context if applicable] |

[Paragraph: explain YoY drivers. Separate weather effect (HDD change) from
efficiency effect (intensity change). If intensity worsened despite favorable
weather, say so explicitly.]

---

## Month-over-Month Analysis

### Natural Gas ([Prior Month] → [Current Month])

| Metric | [Prior Month] | [Current Month] | MoM Change |
|---|---|---|---|
| Total CCF | X | X | ±% |
| Space Heat CCF *(net of DHW)* | X | X | ±% |
| DHW CCF (Navien) | X | X | ±% |
| HDD65 | X | X | ±% |
| Heating Intensity *(corrected)* | X CCF/1k HDD | X CCF/1k HDD | ±% |

[Paragraph: brief MoM commentary. Note if seasonal transition is the driver.]

### HVAC Runtime ([Prior Month] → [Current Month])

| Metric | [Prior Month] | [Current Month] | MoM Change |
|---|---|---|---|
| Total Heating Hours | X | X | ±% |
| Zone Balance (1F%) | X% | X% | Δ pts |
| min/HDD | X | X | ±% |

[Paragraph: runtime context. If shoulder season, apply §4 framing.]

---

## DHW Performance Update

### Navien Tankless — Monthly Metrics

| Metric | [Prior Year Same Month] | [Current Month] | Change |
|---|---|---|---|
| DHW Gas (Navien) | X CCF | X CCF | ±% |
| DHW Operating Hours | X hrs | X hrs | ±% |
| Recirculation Hours | X hrs | X hrs | ±% |
| Gas per Operating Hour | X CCF/hr | X CCF/hr | ±% |

[Paragraph: explain any changes. The established post-optimization baseline
is ~1.25 CCF/hr. Changes from this indicate new operational changes or
seasonal inlet temperature effects.]

---

## HDD Source Note

[Only include if gap between sources > 3% or if sources disagree in direction.
Otherwise omit this section.]

| Month | Daily CSV | HA Proxy | BDL Official |
|---|---|---|---|
| [Month] | X | X | X |

[1–2 sentences explaining which source is used and why.]

---

## HVAC Runtime Performance

### Baseline Comparison

| Metric | Annual Baseline | [Current Month] | Context |
|---|---|---|---|
| Runtime / HDD | 10.9 min/HDD | X min/HDD | [peak/shoulder note] |
| Heating Intensity | 90.3 CCF/1k HDD | X CCF/1k HDD | [peak/shoulder note] |
| Zone Balance Target | 50% ± 5% | X% | ✓/⚠ |

[If peak heating month: "The [X] CCF/1k HDD represents [±Y] CCF/1k HDD
vs the 90.3 baseline ([±Z]%). [Sentence on rolling 12-month context.]"]

[If shoulder month: Use §4 framing. Do NOT compare to 90.3 baseline.]

---

## Rolling 12-Month Summary

| Metric | Value | vs Baseline | Trend |
|---|---|---|---|
| Heating Efficiency | [X] CCF/1k HDD | +[Y] CCF/1k HDD ([Z]%) | [↑↓→] |
| Building UA (12M) | [X] BTU/hr-°F | +[Y] BTU/hr-°F ([Z]%) | [↑↓→] |
| Site EUI | [X] kBTU/ft²-yr | +[Y]% | [↑↓→] |
| Trailing 12M HDD | [X] | vs [5,270] normal | [±Z]% |

[2–3 sentences: status of each metric vs baseline. This is where envelope
and efficiency concerns are discussed — not in the monthly sections above.]

---

## Recommendations

### Monitoring Priorities

[3–5 items. Each must be:
- Specific (name the sensor or metric to watch)
- Actionable (what to do if threshold is crossed)
- Tied to something observed in this month's data]

### Pending Data

[List any bills, meter readings, or CSV updates not yet available.
Include expected timing and which CSVs/archives to update when received.]

---

*[Footer: data sources used, system specs one-liner, report version]*
```

---

## §7 — VALIDATION CHECKLIST

Run mentally before finalizing. If any item fails, fix before writing report.

**Arithmetic:**
- [ ] Heating intensity uses `net_heat_ccf` (not `total_gas_ccf`) in numerator
- [ ] `net_heat_ccf = total_gas_ccf − dhw_navien_ccf` (Navien meter, not estimated)
- [ ] `runtime_per_hdd` uses furnace heating hours (not zone sum) and same HDD source as intensity
- [ ] All YoY and MoM deltas computed from equivalent metrics (same formula both years)
- [ ] No intermediate rounding — final values rounded to 1 decimal for CCF/1k HDD, 0.1h for runtime

**System constants:**
- [ ] Furnace input = 60,556 BTU/hr (not 100,000)
- [ ] AFUE = 0.95 (not 0.96)
- [ ] Fireplace not prorated monthly in UA calculation

**Seasonal framing:**
- [ ] If mean outdoor temp > 45°F: §4 rules applied throughout
- [ ] No individual month compared against 90.3 CCF/1k HDD baseline unless Dec/Jan/Feb
- [ ] Runtime/HDD not called "exceptional" for shoulder months

**Narrative:**
- [ ] No modulation claims (single-stage system)
- [ ] DHW savings claimed only where operating hours are equal YoY
- [ ] Envelope health discussed only via rolling 12-month UA
- [ ] Positive framing not applied to worsening metrics

**Data integrity:**
- [ ] HDD source documented
- [ ] Any gap > 3% between HDD sources flagged
- [ ] `monthly_summary.csv` updated with this month's computed values before publishing
- [ ] `README.md` all five update zones correct and internally consistent (see §10)

---

## §8 — MONTHLY SUMMARY CSV UPDATE

After writing the report, append one row to `data/monthly_summary.csv`:

```
YYYY-MM, total_gas_ccf, dhw_ccf, net_heat_ccf, hdd65, heating_intensity,
furnace_hours, runtime_per_hdd, zone_bal_1f_pct, elec_kwh,
efficiency_12m, ua_12m, hdd_source
```

Where `hdd_source` is one of: `daily_csv`, `ha_proxy`, `bdl_official`.

This row is the authoritative record for next month's YoY comparisons.
Do not modify prior rows unless a documented correction is being applied
(in which case increment the report version and note in UPDATES.md).

---

## §9 — KNOWN ISSUES AND STANDING CORRECTIONS

Document any standing issues here so they are not re-discovered monthly:

**HDD proxy systematic bias:**
The HA proxy (Hartford weather API via Open-Meteo) undercounts annual HDD by ~2.3%
vs BDL official. Monthly bias varies — March tends to overcount, Jan/Feb undercount.
This inflates CCF/1k HDD by ~0.8–1.0 CCF/1k HDD on an annual basis.
The efficiency baseline (90.3) was established using the same proxy, so the bias
partially cancels in year-over-year comparisons but does not cancel fully due to
seasonal variation in the proxy error.

**DHW vs billing-aligned calculation variance:**
The Navien independent meter reads ~15% higher than the billing-aligned DHW estimate.
Always use the Navien meter reading as the authoritative DHW figure.
The billing-aligned estimate is documented in METHODOLOGY.md but is not used in reports.

**Fireplace gas attribution:**
Fireplace gas is included in total utility bills but is not separately metered.
The 3.6 MMBTU/yr (52 CCF/yr at 0.5 CCF/hr × ~100 hrs) estimate is embedded in the
historical baseline. If fireplace usage changes materially year-over-year, a portion
of the intensity change reflects this attribution uncertainty, not system performance.
Do not claim fireplace use "explains" the efficiency gap without quantifying it
through the heat-substitution model (each CCF burned in the fireplace at ~70% efficiency
saves only 0.737 CCF of furnace gas — it does not add 1:1 to measured intensity).

**March 2026 report correction (v1.5.0 → v1.5.1):**
The original report used total gas in the heating intensity numerator.
Corrected values: intensity 125.1 (not 144.4), YoY direction +4.1% (not −5.3%).
`monthly_summary.csv` row for 2026-03 should reflect corrected figures.

---

## §10 — README.md UPDATE

The `README.md` has five distinct zones that must be updated every month.
Locate each zone by its HTML comment markers and replace the content between them.
**Never remove the comment markers themselves** — they are used by CI and badge tooling.

---

### Zone 1 — `METRICS_START` / `METRICS_END`

Update the "Key Findings" badge block. All six lines must reflect the current
trailing 12-month figures, not the just-completed month in isolation.

```markdown
<!-- METRICS_START -->
**Key Findings (Updated [Month] [Year]):**
- **Site EUI (12-mo rolling):** [X] kBTU/ft²-yr ([Y]% better than regional average)
- **Baseline Site EUI:** 41.7 kBTU/ft²-yr — current [+/-Z%] due to [weather/season context]
- **Heating Intensity:** [X] CCF/1k HDD (12-month rolling; corrected with Navien DHW metering)
- **Envelope UA:** [X] BTU/hr-°F ([Y]% [superior/above] baseline)
- **12-mo Electricity:** [X] kWh ([Y]% below average for home size)
- **DHW Optimization:** [X]% sustained YoY from recirculation schedule change (~$[Y]/year savings)
<!-- METRICS_END -->
```

**Calculation rules for each line:**

| Field | Formula | Notes |
|---|---|---|
| Site EUI | trailing 12M gas (CCF × 103.7) + elec (kWh × 3.412) / 2440 | From §3G |
| % better than regional | (regional_avg − site_eui) / regional_avg × 100 | Regional avg = 60.6 kBTU/ft²-yr for CT climate zone 5A |
| Baseline EUI delta | (current_eui / 41.7 − 1) × 100 | Use signed result; write "better" if negative, "above" if positive |
| Heating Intensity | 12-month rolling from §3C | Must match `efficiency_12m` in monthly_summary.csv |
| UA | 12-month rolling from §3D | From HA archives; note if above/below 493 baseline |
| 12-mo electricity | sum of trailing 12 monthly kWh | From monthly_electricity_eversource.csv |
| DHW % savings | (current_12m_dhw / prior_12m_dhw − 1) × 100 | Compare same 12M window, not just current month |
| DHW $/yr savings | dhw_ccf_saved × gas_effective_rate × 12 / months_with_data | Annualized from observed savings rate |

**Framing rules:**
- If EUI is above baseline, write "current [+X%] above baseline due to [cause]" — do not write "current +X% due to colder winter" when efficiency (not weather) is the driver
- If UA is above 493, write "above baseline" not "superior"
- The regional comparison (% better than average) is based on CT residential EUI of ~60 kBTU/ft²-yr for this building type; update only if the source benchmark changes

---

### Zone 2 — `HIGHLIGHTS_START` / `HIGHLIGHTS_END`

Replace the entire highlights block with the current month's summary table
and key insights. Structure:

```markdown
<!-- HIGHLIGHTS_START -->
## 🆕 [Month] [Year] Update Highlights

[1–2 sentence weather/season context for this specific month.]

| Metric | [Month] [Prior Year] | [Month] [Current Year] | YoY Change | Status |
|---|---|---|---|---|
| Total Gas | X CCF | X CCF | ±% | ✅/⚠️ [reason] |
| Space Heating | X CCF | X CCF | ±% | ✅/⚠️ [reason] |
| DHW (Navien) | X CCF | X CCF | ±% | ✅/⚠️ [reason] |
| Weather Severity | X HDD | X HDD | ±% | ✅/⚠️ |
| HVAC Runtime | X hrs | X hrs ([Y] min/HDD) | ±% | ✅/⚠️ |

**Key Insights:**
1. [Most important finding — quantified]
2. [Second finding — quantified]
3. [Season cumulative if in heating season: "Season totals: X hrs across Y HDD (Oct–[Month])"]

### DHW Recirculation Optimization (Ongoing)

**Cumulative Savings ([date range]):** [X] CCF (~$[Y])
**On Track For:** ~$[Z]/year projected annual savings
**Schedule:** 15 hr/day (off 9 PM - 6 AM) — [any comfort issues or "no comfort issues reported"]

See [UPDATES.md](UPDATES.md) for complete monthly analysis.
<!-- HIGHLIGHTS_END -->
```

**Status icon rules:**
- ✅ = metric moved in the expected direction or within ±5% of expectation
- ⚠️ = metric moved in unexpected direction, or exceeded ±15% of expectation
- Never use ✅ for a metric that worsened without qualification

**Space Heating field:** Always use net heating gas (total minus Navien DHW),
not total gas. Label the column header "Space Heating" not "Total Gas."

**min/HDD in runtime row:** Use the §3E formula. Apply §4 shoulder-season
framing in the status field if applicable — do not call it "Excellent" when
mean outdoor temp was > 45°F.

**DHW cumulative savings:** Compute as `sum(prior_year_dhw − current_year_dhw)`
for all months in 2026 with data, then convert to dollars at current gas rate.
If savings are not calculable (missing prior-year Navien data), state "pending
prior-year Navien data for [month]."

---

### Zone 3 — Five-Year Performance Table

Locate the `## 📊 Five-Year Performance Summary` section. Update the
**current year column** (`2026 YTD`) only. Prior years are locked.

```markdown
| Metric | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
|---|---|---|---|---|---|
| Annual Gas (CCF) | 815 | 764 | 694 | 787 | [sum Jan–current month]* |
| Annual Elec (kWh) | 6,824 | 6,591 | 6,543 | 6,730 | [sum Jan–current month]* |
| Heating Intensity | 89.8 | 90.8 | 80.3 | 95.5 | [YTD intensity if ≥4 months, else —]* |
| Site EUI | 42.1 | 40.8 | 38.2 | 41.7 | — |
```

**Rules:**
- The asterisk footnote must state `*[Month range] [Year] only (partial year)` — update the month range
- YTD Heating Intensity: only publish if ≥ 4 months of heating data exist;
  otherwise leave as `—`. When present, use `(sum net_heat_ccf YTD) / (sum hdd YTD) × 1000`
- Site EUI: only publish for complete calendar years; leave `—` for current year
- Never update prior-year columns — if a prior year needs correction, document
  in §9 of this file and version-bump the README

---

### Zone 4 — Version Badge and Recent Updates

Update the version badge at the top of the README:

```markdown
[![Version](https://img.shields.io/badge/Version-[X.Y.Z]-blue.svg)](...)
```

Version increment rules:
- **Patch** (x.x.**Z**): routine monthly data addition, no methodology changes
- **Minor** (x.**Y**.0): new sensor added, new metric introduced, HA config change
- **Major** (**X**.0.0): baseline recalibration, methodology overhaul

Update the `## 📬 Recent Updates` section — prepend the new version entry,
keep the two prior entries, remove the oldest:

```markdown
### v[X.Y.Z] ([Month] [Year])
- Added [Month] [Year] data and analysis
- Extended dataset to [N] months
- [1–2 bullet points: notable findings from this month, quantified]
- [If applicable: system changes, methodology updates]
```

The `**Next Update:**` line at the bottom of the README must also be updated:
```
**Next Update:** [Next Month] [Year] ([context — e.g., "post-winter summary" if April])
```

---

### Zone 5 — Header Metadata

Update these two lines at the bottom of the README:

```markdown
**Version:** [X.Y.Z] ([Month] [Year])
**Status:** Active Baseline — [N] months of validated data
```

Where N = total months of data from Jan 2022 through current reporting month.
Current count: 51 months through February 2026. Increment by 1 each month.

---

### README Consistency Check

Before committing, verify these are internally consistent:

- [ ] Version badge ↔ `## 📬 Recent Updates` entry ↔ footer `**Version:**`
- [ ] METRICS_START Site EUI ↔ Five-Year Table (2025 row EUI)
- [ ] HIGHLIGHTS_START YoY table ↔ UPDATES.md prior-month entry numbers
- [ ] Dataset month count (N) ↔ actual span from Jan 2022 to current month
- [ ] "Next Update" month is the calendar month after the reporting month
- [ ] No README section references a figure that contradicts `monthly_summary.csv`
