#!/usr/bin/env python3
"""Build derived files from the two CSVs:
  data/tracker.json      everything in one JSON (used by the Solar Factory game and by anyone who wants it)
  README.md              the summary tables between the <!-- summary:start --> and <!-- summary:end --> markers
Run from the repository root after editing a CSV:  python3 scripts/validate.py && python3 scripts/build.py"""
import csv, json, re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def rows(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def latest_by_group(duties):
    """For each case_group, country, company and duty_type keep the most advanced stage (order > final > preliminary)."""
    rank = {"preliminary": 1, "final": 2, "amended final": 3, "order": 4, "review": 5, "tariff": 2, "scope": 0}
    best = {}
    for d in duties:
        if not d["rate_pct"]:
            continue  # placeholders (e.g. an order not yet published) never outrank a real rate
        k = (d["case_group"], d["country"], d["company"], d["duty_type"])
        r = (rank.get(d["rate_stage"], 0), d["effective_date"] or "", d["determination_date"] or "")
        if k not in best or r > best[k][0]:
            best[k] = (r, d)
    return [v[1] for v in best.values()]


def md_table(headers, lines):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(str(c) for c in line) + " |" for line in lines]
    return "\n".join(out)


def main():
    duties = rows("duties.csv")
    facts = rows("factories.csv")
    today = date.today().isoformat()

    # ---- JSON ----
    out = {
        "generated": today,
        "license": "CC BY 4.0 (data), MIT (code)",
        "source": "https://github.com/builtbyaarya/us-solar-trade-tracker",
        "disclaimer": "Not legal or trade advice. Verify every figure against its source_url before use.",
        "duties": duties,
        "factories": facts,
    }
    # summary used by the game: all-others rate per country per duty type, latest stage
    summary = defaultdict(dict)
    for d in latest_by_group(duties):
        if d["company"].lower().startswith("all other") or "wide" in d["company"].lower():
            v = num(d["rate_pct"])
            if v is not None:
                key = d["duty_type"]
                cur = summary[d["country"]].get(key)
                if cur is None or v > cur:
                    summary[d["country"]][key] = v
    out["all_others_by_country"] = dict(summary)
    cap = defaultdict(float)
    for f in facts:
        v = num(f["capacity_value"])
        if v is not None and f["status"] in ("operating", "expanding", "ramping", "commissioning"):
            cap[f["stage"]] += v
    out["operating_capacity_by_stage"] = dict(cap)
    (DATA / "tracker.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ---- README tables ----
    groups = defaultdict(list)
    for d in latest_by_group(duties):
        groups[d["case_group"]].append(d)
    parts = [f"_Summary generated {today} from the CSVs; the CSVs are the source of truth._\n"]
    parts.append("### Duty rates (latest stage on file, all-others and country-wide rows)\n")
    lines = []
    for g in sorted(groups):
        for d in sorted(groups[g], key=lambda x: (x["country"], x["duty_type"])):
            c = d["company"].lower()
            if c.startswith("all other") or "wide" in c or d["duty_type"] in ("Section 201", "Section 301"):
                rate = d["rate_pct"] + "%" if d["rate_pct"] else "see notes"
                lines.append([g, d["country"], d["duty_type"], d["company"], rate, d["rate_stage"],
                              d["determination_date"] or "", f"[source]({d['source_url']})"])
    parts.append(md_table(["Case", "Country", "Type", "Row", "Rate", "Stage", "Date", "Source"], lines))
    parts.append("\n### US manufacturing capacity by stage (sum of facility nameplates on file)\n")
    agg = defaultdict(lambda: defaultdict(float))
    for f in facts:
        v = num(f["capacity_value"])
        if v is not None:
            agg[f"{f['stage']} ({f['capacity_unit']})"][f["status"]] += v
    lines = []
    for st in sorted(agg):
        cells = agg[st]
        lines.append([st, f"{cells.get('operating', 0) + cells.get('expanding', 0) + cells.get('ramping', 0):.1f}",
                      f"{cells.get('under_construction', 0) + cells.get('commissioning', 0):.1f}",
                      f"{cells.get('announced', 0):.1f}", f"{cells.get('cancelled', 0) + cells.get('closed', 0) + cells.get('paused', 0):.1f}"])
    parts.append(md_table(["Stage", "Operating", "Under construction", "Announced", "Cancelled, closed or paused"], lines))
    pending = [d for d in duties if not d["rate_pct"]]
    if pending:
        parts.append(f"\nPending: {len(pending)} placeholder rows with no rate yet (for example AD/CVD orders not yet published); see `notes` in the CSV and `docs/cases.md`.")
    parts.append(f"\nRows: {len(duties)} duty rates, {len(facts)} facilities. Every row carries a public source URL.\n")
    summary_md = "\n".join(parts)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = re.sub(r"<!-- summary:start -->.*?<!-- summary:end -->",
                    "<!-- summary:start -->\n" + summary_md + "\n<!-- summary:end -->", readme, flags=re.S)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"built data/tracker.json and README summary: {len(duties)} duty rows, {len(facts)} facility rows")


if __name__ == "__main__":
    main()
