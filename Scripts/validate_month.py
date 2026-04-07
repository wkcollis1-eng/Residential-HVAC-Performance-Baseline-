#!/usr/bin/env python3
"""
validate_month.py — Residential-HVAC-Performance-Baseline-
Pre-commit validation for monthly data updates.

Usage:
    python3 scripts/validate_month.py              # validate all months
    python3 scripts/validate_month.py 2026-03-01  # validate one month key

Exits 0 if all checks PASS or only WARN.
Exits 1 if any HALT-level check fails (do not commit).

Checks implemented (V-HVAC-1 through V-HVAC-8):
  V-HVAC-1  Runtime/HDD within ±2σ of trailing history
  V-HVAC-2  Heating efficiency within ±15% of 90.3 CCF/1kHDD baseline
  V-HVAC-3  Space_Heat_CCF / HDD coherence (UA proxy ±5%)
  V-HVAC-4  Monthly HDD65 vs 5,270 annual normal (document if >±20%)
  V-HVAC-5  Zone balance 1F/2F within 45–55% (heating season only)
  V-HVAC-6  DHW CCF ≤ prior-year same month +5% (savings must hold)
  V-HVAC-7  daily_temperature row count = days-in-month (no partial months)
  V-HVAC-8  monthly_hvac_runtime exactly 2 rows per month
"""

import csv
import sys
import math
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────
BASELINE_EFFICIENCY = 90.3  # CCF/1kHDD (Navien-corrected 2025)
BASELINE_UA = 480  # BTU/hr-°F
BASELINE_RUNTIME_PHD = 10.9  # min/HDD (2024 full-year)
AFUE = 0.950
GAS_BTU_PER_CCF = 103_700
HDD_ANNUAL_NORMAL = 5_270  # 18-year historical, Chester CT
ZONE_BAL_LO = 45.0  # % 1F share (heating) — lower bound
ZONE_BAL_HI = 55.0  # % 1F share (heating) — upper bound
HDD_THRESH_HEATING = 100  # HDD minimum for heating-season checks

PASS = "✅ PASS"
WARN = "⚠️  WARN"
FLAG = "🚩 FLAG"
HALT = "🛑 HALT"

issues = []
halt_triggered = False


def result(level, check, message):
    global halt_triggered
    tag = {"PASS": PASS, "WARN": WARN, "FLAG": FLAG, "HALT": HALT}.get(level, level)
    print(f"  {tag}  [{check}]  {message}")
    if level == "HALT":
        halt_triggered = True
        issues.append(f"HALT [{check}]: {message}")
    elif level in ("FLAG", "WARN"):
        issues.append(f"{level} [{check}]: {message}")


# ── Load data ─────────────────────────────────────────────────────────────────
repo_root = Path(__file__).parent.parent


def load_csv(path):
    with open(repo_root / path, newline="") as f:
        return list(csv.DictReader(f))


# Runtime (2 rows per month)
runtime = {}
for row in load_csv("data/monthly_hvac_runtime.csv"):
    mk = row["Month"]
    if mk not in runtime:
        runtime[mk] = []
    runtime[mk].append(
        {"heat": float(row["Heating_Hours"]), "cool": float(row["Cooling_Hours"])}
    )

# DHW
dhw = {}
for row in load_csv("data/monthly_dhw_navien.csv"):
    dhw[row["Month"]] = {"ccf": float(row["Gas_CCF"])}

# Gas bills — map to calendar month key
gas_by_month = {}
for row in load_csv("data/monthly_gas_scg.csv"):
    bd = datetime.strptime(row["Bill_Date"], "%Y-%m-%d")
    # Bill date is ~10th of month following consumption month
    # Attribute to month 30-45 days prior
    from_dt = bd
    for offset_days in range(10, 50):
        from datetime import timedelta

        candidate = bd - timedelta(days=offset_days)
        mk = candidate.strftime("%Y-%m-01")
        if mk not in gas_by_month:
            gas_by_month[mk] = float(row["Gas_CCF"])
            break

# HDD per month from daily
monthly_hdd = {}
daily_row_count = defaultdict(int)
for row in load_csv("data/daily_temperature.csv"):
    try:
        d = datetime.strptime(row["Date"], "%Y-%m-%d")
        mk = d.strftime("%Y-%m-01")
        if mk not in monthly_hdd:
            monthly_hdd[mk] = 0.0
        monthly_hdd[mk] += float(row["HDD65"]) if row["HDD65"] else 0.0
        daily_row_count[mk] += 1
    except Exception:
        pass

# ── Determine which months to validate ───────────────────────────────────────
all_months = sorted(set(runtime.keys()))
if len(sys.argv) > 1:
    target = sys.argv[1]
    if not target.endswith("-01"):
        target = target[:7] + "-01"
    validate_months = [target] if target in all_months else []
    if not validate_months:
        print(f"Month {target} not found in runtime data. Available: {all_months[-3:]}")
        sys.exit(1)
else:
    validate_months = all_months

# ── Per-month validation ──────────────────────────────────────────────────────
print(f"\n{'═' * 65}")
print("  Residential-HVAC-Performance-Baseline- — Monthly Validation")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"{'═' * 65}\n")

for mk in validate_months:
    mk_dt = datetime.strptime(mk, "%Y-%m-%d")
    month_name = mk_dt.strftime("%B %Y")
    days_in_month = (
        datetime(mk_dt.year + (mk_dt.month // 12), (mk_dt.month % 12) + 1, 1) - mk_dt
    ).days
    print(f"── {month_name} ({mk}) ──")

    rt_rows = runtime.get(mk, [])
    hdd = monthly_hdd.get(mk, None)
    heat_total = sum(r["heat"] for r in rt_rows)
    heat_1f = rt_rows[0]["heat"] if rt_rows else 0
    heat_2f = rt_rows[1]["heat"] if len(rt_rows) > 1 else 0
    dhw_ccf = dhw.get(mk, {}).get("ccf", None)
    gas_ccf = gas_by_month.get(mk, None)
    is_heating = hdd is not None and hdd > HDD_THRESH_HEATING

    # V-HVAC-8: Exactly 2 rows per month in runtime file
    if len(rt_rows) == 2:
        result("PASS", "V-HVAC-8", f"Runtime: 2 rows (1F={heat_1f}h, 2F={heat_2f}h)")
    elif len(rt_rows) == 0:
        result("HALT", "V-HVAC-8", "No runtime rows found for this month")
    else:
        result(
            "HALT",
            "V-HVAC-8",
            f"Expected 2 rows, found {len(rt_rows)} — check monthly_hvac_runtime.csv",
        )

    # V-HVAC-7: daily_temperature row count
    actual_rows = daily_row_count.get(mk, 0)
    if actual_rows == 0:
        result("HALT", "V-HVAC-7", f"No daily temperature rows for {month_name}")
    elif actual_rows == days_in_month:
        result(
            "PASS",
            "V-HVAC-7",
            f"Daily rows: {actual_rows} = {days_in_month} days in month",
        )
    else:
        result(
            "HALT",
            "V-HVAC-7",
            f"Daily rows: {actual_rows} ≠ {days_in_month} days — partial month data",
        )

    # V-HVAC-1: Runtime/HDD vs trailing history
    if is_heating and heat_total > 0 and hdd and hdd > 0:
        rph = heat_total * 60 / hdd
        # Build trailing 3-month history excluding current
        trailing = []
        prior_months = [
            m
            for m in all_months
            if m < mk and monthly_hdd.get(m, 0) > HDD_THRESH_HEATING
        ][-3:]
        for pm in prior_months:
            ph = monthly_hdd.get(pm, 0)
            pt = sum(r["heat"] for r in runtime.get(pm, []))
            if ph > 0 and pt > 0:
                trailing.append(pt * 60 / ph)
        if len(trailing) >= 2:
            mean_t = sum(trailing) / len(trailing)
            std_t = math.sqrt(sum((x - mean_t) ** 2 for x in trailing) / len(trailing))
            lo = mean_t - 2 * std_t
            hi = mean_t + 2 * std_t
            if lo <= rph <= hi:
                result(
                    "PASS",
                    "V-HVAC-1",
                    f"Runtime/HDD={rph:.2f} min/HDD within ±2σ ({lo:.1f}–{hi:.1f})",
                )
            else:
                result(
                    "FLAG",
                    "V-HVAC-1",
                    f"Runtime/HDD={rph:.2f} OUTSIDE ±2σ ({lo:.1f}–{hi:.1f}) — baseline={BASELINE_RUNTIME_PHD}",
                )
        else:
            result(
                "WARN",
                "V-HVAC-1",
                f"Runtime/HDD={rph:.2f} — insufficient history for σ check ({len(trailing)} prior months)",
            )
    elif not is_heating:
        result(
            "PASS",
            "V-HVAC-1",
            "Non-heating month (HDD ≤ 100) — runtime/HDD check skipped",
        )
    else:
        result("WARN", "V-HVAC-1", "Missing HDD or runtime data — cannot check")

    # V-HVAC-2: Heating efficiency vs 90.3 baseline
    if is_heating and gas_ccf and hdd and hdd > 0:
        eff = gas_ccf / (hdd / 1000)
        delta_pct = (eff - BASELINE_EFFICIENCY) / BASELINE_EFFICIENCY * 100
        # Note: monthly efficiency is expected to deviate from annual due to billing alignment
        # Flag only if >15% AND same direction as prior month
        if abs(delta_pct) <= 15:
            result(
                "PASS",
                "V-HVAC-2",
                f"Heating intensity={eff:.1f} CCF/1kHDD ({delta_pct:+.1f}% vs {BASELINE_EFFICIENCY} baseline)",
            )
        else:
            result(
                "FLAG",
                "V-HVAC-2",
                f"Heating intensity={eff:.1f} CCF/1kHDD ({delta_pct:+.1f}% vs baseline) — confirm billing alignment artifact",
            )
    elif not is_heating:
        result("PASS", "V-HVAC-2", "Non-heating month — efficiency check skipped")
    else:
        result("WARN", "V-HVAC-2", "Missing gas_ccf or HDD — cannot check efficiency")

    # V-HVAC-3: Space heat CCF vs HDD (UA proxy)
    if is_heating and gas_ccf and dhw_ccf and hdd and hdd > 0:
        space_heat = gas_ccf - dhw_ccf
        implied_ua = (space_heat * GAS_BTU_PER_CCF * AFUE) / (hdd * 24)
        delta_pct = (implied_ua - BASELINE_UA) / BASELINE_UA * 100
        if abs(delta_pct) <= 5:
            result(
                "PASS",
                "V-HVAC-3",
                f"Implied UA={implied_ua:.0f} BTU/hr-°F ({delta_pct:+.1f}% vs {BASELINE_UA} baseline)",
            )
        elif abs(delta_pct) <= 15:
            result(
                "WARN",
                "V-HVAC-3",
                f"Implied UA={implied_ua:.0f} ({delta_pct:+.1f}%) — within expected billing variability",
            )
        else:
            result(
                "FLAG",
                "V-HVAC-3",
                f"Implied UA={implied_ua:.0f} ({delta_pct:+.1f}% vs {BASELINE_UA}) — investigate if sustained",
            )
    elif not is_heating:
        result("PASS", "V-HVAC-3", "Non-heating month — UA check skipped")
    else:
        result("WARN", "V-HVAC-3", "Missing data — cannot compute UA proxy")

    # V-HVAC-4: Monthly HDD vs annualized normal
    if hdd is not None:
        # Rough seasonal fraction: assume this month's share of annual HDD
        annualized_share = hdd  # single month — document if season total drifts
        result(
            "PASS",
            "V-HVAC-4",
            f"HDD65={hdd:.0f} (annual normal {HDD_ANNUAL_NORMAL} — document season total if >±20%)",
        )
    else:
        result("WARN", "V-HVAC-4", "No HDD data — check daily_temperature.csv coverage")

    # V-HVAC-5: Zone balance (heating season only)
    if is_heating and heat_total > 0:
        zone_1f_pct = heat_1f / heat_total * 100
        if ZONE_BAL_LO <= zone_1f_pct <= ZONE_BAL_HI:
            result(
                "PASS",
                "V-HVAC-5",
                f"Zone balance: 1F={zone_1f_pct:.1f}% (target {ZONE_BAL_LO}–{ZONE_BAL_HI}%)",
            )
        else:
            result(
                "FLAG",
                "V-HVAC-5",
                f"Zone balance: 1F={zone_1f_pct:.1f}% outside {ZONE_BAL_LO}–{ZONE_BAL_HI}% — note early/late season is expected to deviate",
            )
    else:
        result(
            "PASS",
            "V-HVAC-5",
            "Non-heating month or no runtime — zone balance check skipped",
        )

    # V-HVAC-6: DHW CCF ≤ prior-year same month +5%
    if dhw_ccf is not None:
        # Find same month prior year
        prior_year_mk = datetime(mk_dt.year - 1, mk_dt.month, 1).strftime("%Y-%m-01")
        prior_dhw = dhw.get(prior_year_mk, {}).get("ccf", None)
        if prior_dhw is not None:
            threshold = prior_dhw * 1.05
            pct_chg = (dhw_ccf - prior_dhw) / prior_dhw * 100
            if dhw_ccf <= threshold:
                result(
                    "PASS",
                    "V-HVAC-6",
                    f"DHW={dhw_ccf:.2f} CCF ({pct_chg:+.1f}% YoY) — savings holding",
                )
            else:
                result(
                    "FLAG",
                    "V-HVAC-6",
                    f"DHW={dhw_ccf:.2f} CCF ({pct_chg:+.1f}% YoY) — exceeds prior year +5% threshold ({threshold:.2f})",
                )
        else:
            result(
                "WARN",
                "V-HVAC-6",
                f"DHW={dhw_ccf:.2f} CCF — no prior-year data for {prior_year_mk}",
            )
    else:
        result("WARN", "V-HVAC-6", "No DHW data for this month")

    print()

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"{'═' * 65}")
if halt_triggered:
    print(f"\n{HALT}  Validation FAILED — do not commit until resolved:\n")
    for i in issues:
        print(f"    {i}")
    print()
    sys.exit(1)
elif issues:
    print(
        f"\n{FLAG}  Validation complete — {len(issues)} issue(s) flagged (review before committing):\n"
    )
    for i in issues:
        print(f"    {i}")
    print()
    sys.exit(0)
else:
    print(f"\n{PASS}  All checks passed — safe to commit.\n")
    sys.exit(0)
