# US Solar Trade Tracker

[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-2b6cb0)](data/LICENSE) [![Code: MIT](https://img.shields.io/badge/code-MIT-2b6cb0)](LICENSE) [![validate data](https://github.com/builtbyaarya/us-solar-trade-tracker/actions/workflows/validate.yml/badge.svg)](https://github.com/builtbyaarya/us-solar-trade-tracker/actions/workflows/validate.yml) [![Rows](https://img.shields.io/badge/rows-222%20duty%20rates%20%C2%B7%2066%20facilities-555)](data/)

An open, sourced dataset of two things that decide whether a solar or battery factory in the United States makes sense:

1. **Duty rates** on imported crystalline silicon solar cells and modules: every antidumping (AD) and countervailing duty (CVD) rate by case, country, company, stage and date, with AD and CVD kept separate and every row linked to the Federal Register notice, Commerce fact sheet or ITC document it comes from. Section 201 and 301 tariff layers are included as their own rows so the full stack is visible.
2. **US manufacturing capacity** for solar and batteries by stage (polysilicon, ingot, wafer, cell, module, battery cells and packs) with each facility's announced size, status and status date, including pauses, closures and cancellations.

Maintained by a mechanical engineering student who got tired of rebuilding the same spreadsheet. Updated twice a week by a scheduled job that re-reads the official pages in `docs/watchlist.txt`; nothing is added without a public source.

> **Not legal or trade advice.** Duty rates change through reviews, orders and court remands, and announced capacity is often not built. Verify every number against its `source_url` before you rely on it. See [DISCLAIMER.md](DISCLAIMER.md).

## Files

| Path | What it is |
|---|---|
| `data/duties.csv` | One row per rate: case, country, company, AD or CVD, rate, stage, dates, source |
| `data/factories.csv` | One row per facility and stage: company, location, stage, capacity, status, dates, investment, jobs, source |
| `data/tracker.json` | Both tables plus a per-country "all others" summary and operating capacity by stage, rebuilt by `scripts/build.py` |
| `docs/schema.md` | Column definitions and allowed values |
| `docs/cases.md` | Plain-English timeline of each case and what is still pending |
| `docs/factories.md` | The capacity picture, known gaps and data-quality flags |
| `docs/methodology.md` | What each field means in trade-law terms, how rows are collected and checked, and the references |
| `docs/verification/` | Independent verification reports, one per release |
| `docs/index.html` | A browser explorer for the data: landed cost per watt by origin on a map, the duty stack per country, and the two tables with filters and sorting |
| `data/landed_cost_inputs.json` | Public spot prices, freight, tariff layers and Section 45X amounts used by the landed-cost tab, each with its source and date |
| `docs/watchlist.txt` | The official pages the updater re-checks |
| `scripts/validate.py` | Checks columns, allowed values, dates and that every row has a source |
| `scripts/build.py` | Rebuilds `tracker.json` and the summary tables below |
| `scripts/check_sources.py` | Hashes the watchlist pages; prints `NO CHANGE` when nothing moved |

## Summary

<!-- summary:start -->
_Summary generated 2026-10-21 from the CSVs; the CSVs are the source of truth._

### Duty rates (latest stage on file, all-others and country-wide rows)

| Case | Country | Type | Row | Rate | Stage | Date | Source |
|---|---|---|---|---|---|---|---|
| Section 201 safeguard (2018-2026) | All countries (global safeguard; some developing countries exempt) | Section 201 | All importers | 14.0% | order | 2022-02-04 | [source](https://www.govinfo.gov/link/fr/87/7357) |
| Section 301 (China tech-transfer action) | China | Section 301 | All importers | 50% | final | 2024-09-18 | [source](https://www.govinfo.gov/link/fr/89/76581) |
| Solar I (China 2012) | China | AD | PRC-wide entity | 249.96% | order | 2012-12-03 | [source](https://www.govinfo.gov/link/fr/77/73018) |
| Solar I (China 2012) | China | CVD | All others | 15.24% | order | 2012-12-03 | [source](https://www.govinfo.gov/link/fr/77/73017) |
| Solar II (China/Taiwan 2015) | China | AD | PRC-wide entity | 165.04% | order | 2015-02-10 | [source](https://www.govinfo.gov/content/pkg/FR-2015-02-18/html/2015-03183.htm) |
| Solar II (China/Taiwan 2015) | China | CVD | All others | 38.43% | order | 2015-02-10 | [source](https://www.govinfo.gov/content/pkg/FR-2015-02-18/html/2015-03183.htm) |
| Solar II (China/Taiwan 2015) | Taiwan | AD | All others | 19.5% | order | 2015-02-10 | [source](https://www.govinfo.gov/content/pkg/FR-2015-02-18/html/2015-03179.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Cambodia | AD | All others | 125.37% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11588.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Cambodia | CVD | All others | 534.67% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11589.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Malaysia | AD | All others | 8.59% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11588.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Malaysia | CVD | All others | 34.09% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11589.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Thailand | AD | All others | 111.45% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11588.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Thailand | CVD | All others | 255.39% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11589.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Vietnam | AD | Vietnam-wide entity | 271.28% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11588.htm) |
| Solar III (Cambodia/Malaysia/Thailand/Vietnam 2025) | Vietnam | CVD | All others | 124.57% | order | 2025-06-17 | [source](https://www.govinfo.gov/content/pkg/FR-2025-06-24/html/2025-11589.htm) |
| Solar IV (India/Indonesia/Laos 2026) | India | AD | All others | 123.04% | final | 2026-09-10 | [source](https://www.federalregister.gov/documents/2026/09/16/2026-18945/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-india-final) |
| Solar IV (India/Indonesia/Laos 2026) | India | CVD | All others | 126.09% | final | 2026-09-10 | [source](https://www.federalregister.gov/documents/2026/09/16/2026-18947/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-india-final) |
| Solar IV (India/Indonesia/Laos 2026) | Indonesia | AD | All others | 94.36% | final | 2026-09-10 | [source](https://www.federalregister.gov/documents/2026/09/16/2026-18939/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-indonesia-final) |
| Solar IV (India/Indonesia/Laos 2026) | Indonesia | CVD | All others | 73.2% | final | 2026-09-10 | [source](https://www.federalregister.gov/documents/2026/09/16/2026-18940/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-indonesia-final) |
| Solar IV (India/Indonesia/Laos 2026) | Laos | AD | Laos-wide entity | 65.43% | final | 2026-09-10 | [source](https://www.federalregister.gov/documents/2026/09/16/2026-18941/crystalline-silicon-photovoltaic-cells-whether-or-not-assembled-into-modules-from-the-lao-peoples) |
| Solar IV (India/Indonesia/Laos 2026) | Laos | CVD | All others | 82.03% | final | 2026-09-10 | [source](https://www.govinfo.gov/content/pkg/FR-2026-09-16/html/2026-18942.htm) |

### US manufacturing capacity by stage (sum of facility nameplates on file)

| Stage | Operating | Under construction | Announced | Cancelled, closed or paused |
|---|---|---|---|---|
| battery_cell (GWh/yr) | 95.0 | 45.0 | 100.0 | 31.0 |
| cell (GW/yr) | 9.4 | 14.9 | 9.6 | 2.0 |
| ingot (GW/yr) | 0.0 | 3.3 | 0.0 | 0.0 |
| module (GW/yr) | 61.4 | 0.0 | 7.4 | 1.5 |
| polysilicon (metric_tons/yr) | 40000.0 | 20000.0 | 0.0 | 0.0 |
| wafer (GW/yr) | 0.0 | 3.3 | 5.0 | 0.0 |

Pending: 7 placeholder rows with no rate yet (for example AD/CVD orders not yet published); see `notes` in the CSV and `docs/cases.md`.

Rows: 222 duty rates, 66 facilities. Every row carries a public source URL.

<!-- summary:end -->

## Explore it in a browser

`docs/index.html` is a single page that loads `data/tracker.json`: filter duties by case, country and instrument, see AD and CVD side by side for each country, and sort facilities by stage and status. Served at https://builtbyaarya.github.io/us-solar-trade-tracker/ once the repository is public; locally, run `python3 -m http.server` in the repository root and open `http://localhost:8000/docs/`.

## How to use it

```bash
git clone https://github.com/builtbyaarya/us-solar-trade-tracker
cd us-solar-trade-tracker
python3 scripts/validate.py      # every row checked
python3 scripts/build.py         # rebuild tracker.json and the README tables
```

Load it in Python:

```python
import pandas as pd
duties = pd.read_csv("data/duties.csv")
duties[(duties.case_group.str.startswith("Solar IV")) & (duties.duty_type == "AD")]
```

The same data drives the [Solar Factory game](https://github.com/builtbyaarya/solar-factory-game), where you try to build a US solar or battery factory and survive to 2030.

## Contributing and citing

See [CONTRIBUTING.md](CONTRIBUTING.md). A row without a public `source_url` will not be merged. To cite the dataset, use [CITATION.cff](CITATION.cff) or: *US Solar Trade Tracker (builtbyaarya), version 2026.10.21, CC BY 4.0, github.com/builtbyaarya/us-solar-trade-tracker*.

How the data are collected and checked, and the papers and official references behind the definitions, are in [docs/methodology.md](docs/methodology.md).

## Licence

Code: [MIT](LICENSE). Data (`data/`): [CC BY 4.0](data/LICENSE). Please credit "US Solar Trade Tracker (builtbyaarya), CC BY 4.0".
