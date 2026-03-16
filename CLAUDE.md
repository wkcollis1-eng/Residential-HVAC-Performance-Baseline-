# CLAUDE.md — Residential-HVAC-Performance-Baseline-

**Repo:** wkcollis1-eng/Residential-HVAC-Performance-Baseline-
**Type:** Longitudinal residential energy performance study — data + documentation
**Period:** January 2022 – present (monthly cadence)
**Skill reference:** For monthly data updates, load `/mnt/skills/user/engineering-monthly-update/SKILL.md` before proceeding.

---

## REPO PURPOSE

Five-year longitudinal study of a 2,440 sq. ft. 2021 Colonial in Central Connecticut (IECC Climate Zone 5A). Integrates utility billing, HVAC runtime telemetry, and DHW metering into a billing-aligned performance baseline. Primary outputs: diagnostic thresholds, efficiency trends, peer-reviewed-quality documentation.

---

## ARCHITECTURE

```
data/                         ← SOURCE OF TRUTH — CSV datasets
  monthly_gas_scg.csv         bill date, billing days, CCF, charges, $/CCF
  monthly_electricity_eversource.csv   read date, kWh, days, charges, $/kWh
  monthly_dhw_navien.csv      month, Gas_CCF, DHW_Operating_Hours, Recirculation_Hours
  monthly_hvac_runtime.csv    month, Cooling_Hours, Heating_Hours  [2 rows/month = 1F + 2F]
  daily_temperature.csv       date, high, low, mean, HDD65, CDD65, 1F_runtime, 2F_runtime

homeassistant/packages/
  hvac_baseline.yaml          HA package — YAML-linted in CI; edit carefully

docs/images/                  chart PNGs referenced in markdown
images/                       dashboard screenshot PNGs

README.md                     header metrics updated each month — see UPDATE TARGETS
CHANGELOG.md                  semver per-release log
DATA_SUMMARY.md               quick-reference tables — update when new month added
METHODOLOGY.md                stable — edit only for methodology changes
UPDATES.md                    consolidated monthly update log — newest month prepended to top
{MONTH}_YYYY_UPDATE.md        legacy per-month files (retained for SEO/GitHub Pages — do not delete)
```

---

## CANONICAL CONSTANTS (never recalculate without cause)

```
Building UA:              480 BTU/hr-°F  (note: 493 in some HA sensors — baseline report uses 480)
Heating efficiency:       90.3 CCF/1kHDD  (Navien-corrected 2025 baseline)
Site EUI baseline:        41.7 kBTU/ft²-yr
Annual gas:               ~787 CCF  (566 heating + 221 DHW)
Annual electricity:       6,730 kWh
DHW ratio:                ~28% of total gas
HVAC runtime baseline:    10.9 min/HDD (2024 full-year)
Zone balance target:      50% ±5% (1F vs 2F split)
HDD65 annual normal:      5,270 HDD (18-year historical, Chester CT 06424)
Gas energy content:       103,700 BTU/CCF
AFUE:                     95.0%
DHW schedule:             15 hr/day active (off 9 PM – 6 AM) — locked, no changes without note
Navien conversion:        CCF = Therms × 0.9643
```

---

## DATA FILE FORMATS

### monthly_gas_scg.csv
```
Bill_Date,Billing_Days,Gas_CCF,Usage_Per_Day,Total_Charges,Cost_Per_CCF
YYYY-MM-DD,NN,NNN,N.NNN,NNN.NN,N.NNN
```
- One row per bill. Bill date = end of billing period.
- `Usage_Per_Day` = Gas_CCF / Billing_Days
- `Cost_Per_CCF` = Total_Charges / Gas_CCF

### monthly_electricity_eversource.csv
```
Read_Date,Usage_kWh,Days,Usage_Per_Day,Charge,Cost_Per_kWh
YYYY-MM-DD,NNN,NN,NN.NNN,NNN.NN,N.NNN
```
- One row per bill.

### monthly_dhw_navien.csv
```
Month,Gas_CCF,DHW_Operating_Hours,Recirculation_Hours
YYYY-MM-DD,NN.NNNN,NN,NN
```
- One row per calendar month. Month field = first of month.
- Values already in CCF (converted from Navien Therms reading before entry).

### monthly_hvac_runtime.csv
```
Month,Cooling_Hours,Heating_Hours
YYYY-MM-DD,NNN,NNN
YYYY-MM-DD,NNN,NNN   ← second row = same month, different zone
```
- **TWO rows per month** — first row = 1F (first floor), second row = 2F (second floor).
- Do not collapse to one row. Zone separation is intentional.

### daily_temperature.csv
- One row per calendar day.
- Columns include: date, high, low, mean, HDD65, CDD65, 1F_runtime_min, 2F_runtime_min.
- Source: timeanddate.com Chester CT (06424).
- Add all days for the month in one append — never partial months.

---

## MONTHLY UPDATE PROCEDURE

**Always load the engineering-monthly-update skill first:**
`/mnt/skills/user/engineering-monthly-update/SKILL.md`

The skill governs validation rules, unit handling, halt conditions, and commit format.
This section provides repo-specific addenda only.

### Step 0 — Validate before starting
```bash
python3 scripts/validate_month.py YYYY-MM-01
```
Run first. HALT failures must be resolved before any data entry. WARN/FLAG require confirmation.

### Files to update each month (in order)
```
1. data/daily_temperature.csv         append N rows (all days in month)
2. data/monthly_hvac_runtime.csv      append 2 rows (1F + 2F)
3. data/monthly_dhw_navien.csv        append 1 row (Navien CCF for the month)
4. data/monthly_gas_scg.csv           append 1 row when bill arrives (~10th)
5. data/monthly_electricity_eversource.csv  append 1 row when bill arrives (~10th)
6. {MONTH}_YYYY_UPDATE.md             create new monthly analysis doc
7. DATA_SUMMARY.md                    update performance table header row
8. README.md                          update KEY METRICS in header (see below)
9. CHANGELOG.md                       add release entry
```

### README.md update targets (update these fields every month)
```
- Data period badge:   "Data-2022-YYYY" → current year
- Overview:            "NN months of verified utility data (January 2022 – Month YYYY)"
- Key Findings block:  Site EUI, Heating Intensity, Envelope UA, 12-mo Electricity, DHW note
- Update Highlights:   ## 🆕 [Month] YYYY Update Highlights  (table + key insights)
- DHW cumulative:      cumulative savings YTD in CCF and dollars
```

### Monthly analysis entry (UPDATES.md)
Prepend a new section to the top of UPDATES.md (below the header, above the prior month). Include:
- MoM comparison table (vs. prior month)
- YoY comparison table (vs. same month prior year)
- Seasonal cumulative totals (Oct–present for heating season)
- DHW optimization section (CCF saved, running YTD total)
- Key efficiency metrics (runtime/HDD, zone balance %)
- Weather context (HDD vs normal, notable events)

### CHANGELOG.md versioning convention
```
Major:  methodology change
Minor:  new month of data added  → bump minor (e.g. 1.3.2 → 1.4.0)
Patch:  corrections/fixes        → bump patch (e.g. 1.4.0 → 1.4.1)
```

---

## VALIDATION RULES (repo-specific — supplement skill V1–V5)

```
V-HVAC-1: runtime/HDD within ±2σ of 7-day rolling bounds from HA alerts
V-HVAC-2: heating efficiency within ±15% of 90.3 CCF/1kHDD baseline
V-HVAC-3: UA recalculation — flag if >±5% from 480 BTU/hr-°F
V-HVAC-4: HDD65 vs 5,270 annual normal — document deviation ≥20%, don't alarm
V-HVAC-5: Zone balance — flag if 1F/2F split outside 45-55% (cooling season: 2F expected dominant)
V-HVAC-6: DHW CCF — flag if >+5% vs prior year same month (schedule change savings must hold)
V-HVAC-7: daily_temperature rows — count must equal days-in-month; no partial months
V-HVAC-8: monthly_hvac_runtime — exactly 2 rows per month; verify month date matches
```

---

## BILLING ALIGNMENT (critical methodology constraint)

Utility bills span ~30-day periods ending ~10th of month — they do NOT align with calendar months.
The billing-aligned methodology pro-rates consumption to actual meter-read-date periods.
See METHODOLOGY.md for full decomposition procedure.

**Key rules:**
- Never assign a bill directly to a calendar month by bill date
- `Bill_Date` in monthly_gas_scg.csv = END of billing period
- Weather-normalize using HDD for the actual billing period span, not the calendar month
- Billing misalignment creates ~15-day phase shift — document, never suppress

---

## COMMIT PATTERN

```bash
git commit -m "YYYY.MM: Add [Month YYYY] HVAC performance data — [key metric]"
# Example:
git commit -m "2026.03: Add March 2026 HVAC performance data — 9.1 min/HDD runtime"
```

One logical change per commit. Never bundle data entry + config changes.

---

## CI/CD — GITHUB ACTIONS (.github/workflows/validate.yml)

Four jobs run on every push to main:
```
markdown-lint      markdownlint-cli2 (cosmetic rules disabled — see .markdownlint.json)
yaml-lint          yamllint on homeassistant/ (relaxed, no line-length limit)
link-check         lychee link checker (non-fatal — fail: false)
validate-ha-package  pyyaml syntax check on homeassistant/packages/hvac_baseline.yaml
```

Before committing any .md or .yaml change, verify it will pass lint.
Markdown rules disabled: MD004, MD012, MD022, MD031, MD032, MD034, MD036, MD040, MD013, MD033, MD041, MD060.
MD024 enabled with `siblings_only: true` — duplicate headings allowed at different nesting levels.

---

## DERIVED METRICS (calculate after each monthly data entry)

After updating source CSVs, regenerate monthly_summary.csv:
```bash
# Re-run the same logic as the original generation script, or update the last row manually.
# monthly_summary.csv is a cache — never edit directly; derive from source CSVs.
```


```
runtime_per_hdd       = monthly_heating_hours × 60 / monthly_HDD65
zone_balance_pct      = 1F_heating_hours / (1F + 2F heating hours) × 100
dhw_yoy_savings_ccf   = same_month_prior_year_dhw - current_month_dhw
dhw_savings_ytd_ccf   = sum of monthly savings Jan–present
dhw_savings_ytd_$     = dhw_savings_ytd_ccf × current $/CCF
heating_intensity      = gas_ccf_billing_period / (HDD65_billing_period / 1000)
```

Report before → after for all rolling metrics after each update.

---

## PROHIBITED ACTIONS

```
NEVER alter historical data rows in any CSV without explicit user instruction + documented reason
NEVER assign a gas/electric bill to a calendar month ignoring billing period dates
NEVER collapse monthly_hvac_runtime to 1 row/month — 2 rows required (1F + 2F)
NEVER store Therms in dhw_navien.csv — always convert to CCF first (× 0.9643)
NEVER change AFUE from 95.0% — manufacturer-confirmed
NEVER update UA constant without recalculation evidence from new dataset
NEVER add partial-month rows to daily_temperature.csv
NEVER manually edit monthly_summary.csv — it is derived from source CSVs; regenerate instead
NEVER commit unvalidated data — run V-HVAC-1 through V-HVAC-8 first
```

---

## BASELINE REFERENCE — FLAG THRESHOLDS

| Metric | Baseline | Flag if |
|--------|----------|---------|
| Heating efficiency | 90.3 CCF/1kHDD | >±15% |
| Runtime/HDD | 10.9 min/HDD | >±2σ rolling |
| UA | 480 BTU/hr-°F | >±5% |
| Zone balance (heating) | 50% ±5% | <45% or >55% |
| DHW monthly | prior-year same month | >+5% YoY increase |
| Annual electricity | 6,730 kWh | >±25% |
| HDD annual | 5,270 | document if >±20% |

---

## OUTPUT FORMAT FOR MONTHLY SESSIONS

Use this structure in every monthly update response:

```
MONTH: YYYY-MM
FILES UPDATED: [list with row counts]

DATA ENTERED
  [field]: [value] [unit]

VALIDATION
  V-HVAC-1 through V-HVAC-8: PASS | FLAG — [detail]

METRICS (before → after)
  runtime/HDD:    N.N → N.N min/HDD
  zone balance:   NN% → NN%
  DHW YoY:        +/-NN% vs [month] 2025

COMMIT MESSAGE
  git commit -m "YYYY.MM: Add [Month YYYY] HVAC data — [key metric]"

README UPDATE: YES/NO — [fields changed]
CHANGELOG VERSION: N.N.N → N.N.N
```
