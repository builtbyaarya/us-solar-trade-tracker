#!/usr/bin/env python3
"""Validate the tracker datasets: required columns, allowed values, every row sourced, dates well formed.
Run from the repository root:  python3 scripts/validate.py
Exit code 1 on any error so it can gate commits and the scheduled update."""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

DUTIES_COLS = ["case_group", "case_number", "country", "company", "duty_type", "rate_pct", "rate_stage",
               "determination_date", "effective_date", "source_title", "source_url", "notes"]
FACT_COLS = ["company", "facility_name", "state", "city", "stage", "capacity_value", "capacity_unit", "status",
             "announced_date", "status_date", "investment_usd_m", "jobs", "source_title", "source_url", "notes"]
DUTY_TYPES = {"AD", "CVD", "Section 201", "Section 301", "IEEPA", "Section 232"}
RATE_STAGES = {"preliminary", "final", "order", "review", "amended final", "tariff", "scope"}
STAGES = {"polysilicon", "ingot", "wafer", "cell", "module", "battery_cell", "battery_module_pack",
          "battery_materials", "ingot_wafer", "cell_module"}
STATUSES = {"announced", "under_construction", "operating", "expanding", "paused", "cancelled", "closed",
            "commissioning", "ramping"}
UNITS = {"GW/yr", "GWh/yr", "metric_tons/yr", "MW/yr", "MWh/yr"}
DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")  # as precise as the source gives: YYYY, YYYY-MM or YYYY-MM-DD
URL = re.compile(r"^https?://\S+$")
STATES = set("AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC PR".split())


def check(path, cols, rules):
    errors = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        if r.fieldnames != cols:
            errors.append(f"{path.name}: columns are {r.fieldnames}, expected {cols}")
            return errors
        for i, row in enumerate(r, 2):
            for e in rules(row):
                errors.append(f"{path.name} line {i}: {e}")
    return errors


def duty_rules(row):
    e = []
    if row["duty_type"] not in DUTY_TYPES:
        e.append(f"duty_type '{row['duty_type']}' not in {sorted(DUTY_TYPES)}")
    if row["rate_stage"] and row["rate_stage"] not in RATE_STAGES:
        e.append(f"rate_stage '{row['rate_stage']}' not allowed")
    if row["rate_pct"]:
        try:
            v = float(row["rate_pct"])
            if v < 0 or v > 5000:  # Cambodia CVD AFA rate in Solar III is 3403.96%
                e.append(f"rate_pct {v} out of range")
        except ValueError:
            e.append(f"rate_pct '{row['rate_pct']}' is not a number")
    for d in ("determination_date", "effective_date"):
        if row[d] and not DATE.match(row[d]):
            e.append(f"{d} '{row[d]}' is not YYYY, YYYY-MM or YYYY-MM-DD")
    if not URL.match(row["source_url"]):
        e.append("source_url missing or not a URL (every row must be sourced)")
    if not row["country"] or not row["company"] or not row["case_group"]:
        e.append("case_group, country and company are required")
    return e


def fact_rules(row):
    e = []
    if row["stage"] not in STAGES:
        e.append(f"stage '{row['stage']}' not in {sorted(STAGES)}")
    if row["status"] not in STATUSES:
        e.append(f"status '{row['status']}' not in {sorted(STATUSES)}")
    if row["state"] and row["state"] not in STATES:
        e.append(f"state '{row['state']}' is not a two-letter US state code")
    if row["capacity_value"]:
        try:
            float(row["capacity_value"])
        except ValueError:
            e.append(f"capacity_value '{row['capacity_value']}' is not a number")
        if row["capacity_unit"] not in UNITS:
            e.append(f"capacity_unit '{row['capacity_unit']}' not in {sorted(UNITS)}")
    for d in ("announced_date", "status_date"):
        if row[d] and not DATE.match(row[d]):
            e.append(f"{d} '{row[d]}' is not YYYY, YYYY-MM or YYYY-MM-DD")
    for n in ("investment_usd_m", "jobs"):
        if row[n]:
            try:
                float(row[n])
            except ValueError:
                e.append(f"{n} '{row[n]}' is not a number")
    if not URL.match(row["source_url"]):
        e.append("source_url missing or not a URL (every row must be sourced)")
    if not row["company"]:
        e.append("company is required")
    return e


def main():
    errors = []
    errors += check(DATA / "duties.csv", DUTIES_COLS, duty_rules)
    errors += check(DATA / "factories.csv", FACT_COLS, fact_rules)
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s)")
        sys.exit(1)
    nd = sum(1 for _ in open(DATA / "duties.csv", encoding="utf-8")) - 1
    nf = sum(1 for _ in open(DATA / "factories.csv", encoding="utf-8")) - 1
    print(f"OK: duties.csv {nd} rows, factories.csv {nf} rows, every row sourced")


if __name__ == "__main__":
    main()
