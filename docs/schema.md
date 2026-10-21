# Schema

## data/duties.csv

| Column | Meaning | Allowed values |
|---|---|---|
| case_group | Short name of the investigation | e.g. `Solar I (China 2012)`, `Solar IV (India/Indonesia/Laos 2026)` |
| case_number | Commerce case number | `A-` (antidumping) or `C-` (countervailing) numbers, blank if none |
| country | Exporting country the rate applies to | text |
| company | Respondent or the catch-all row | company name, `All others`, `China-wide entity`, etc. |
| duty_type | Which instrument | `AD`, `CVD`, `Section 201`, `Section 301`, `IEEPA`, `Section 232` |
| rate_pct | Rate in percent, number only | 0 to 1000, blank if the source gives no number |
| rate_stage | How far the case had got when this rate was published | `preliminary`, `final`, `amended final`, `order`, `review`, `tariff`, `scope` |
| determination_date | Date of the notice or decision | YYYY-MM-DD, or YYYY-MM / YYYY when the source gives no more |
| effective_date | Date the rate applied from (cash deposits), if the notice says | YYYY-MM-DD, or YYYY-MM / YYYY when the source gives no more |
| source_title | Title of the document | text |
| source_url | Link to the document the rate was read from | required |
| notes | Anything a reader needs: critical circumstances, cash deposit vs assessment, review period | text |

Rules: AD and CVD are never summed in one row. A later stage never overwrites an earlier one; add a new row. The "latest" rate for a country is the row with the most advanced stage.

## data/factories.csv

| Column | Meaning | Allowed values |
|---|---|---|
| company | Owner or operator | text |
| facility_name | Plant or site name | text |
| state | Two-letter US state code | `OH`, `GA`, ... |
| city | City or county | text |
| stage | Manufacturing stage | `polysilicon`, `ingot`, `wafer`, `ingot_wafer`, `cell`, `module`, `cell_module`, `battery_cell`, `battery_module_pack`, `battery_materials` |
| capacity_value | Nameplate capacity, number only | blank if not public |
| capacity_unit | Unit of capacity_value | `GW/yr`, `MW/yr`, `GWh/yr`, `MWh/yr`, `metric_tons/yr` |
| status | Most recent public status | `announced`, `under_construction`, `commissioning`, `ramping`, `operating`, `expanding`, `paused`, `cancelled`, `closed` |
| announced_date | Date first announced | YYYY-MM-DD, or YYYY-MM / YYYY when the source gives no more |
| status_date | Date of the source that gives the current status | YYYY-MM-DD, or YYYY-MM / YYYY when the source gives no more |
| investment_usd_m | Announced investment, USD millions | number |
| jobs | Announced jobs | number |
| source_title, source_url | The document the row was read from | source_url required |
| notes | What changed and why, in a few words | text |

One row per facility per stage: a plant that makes cells and modules has two rows.
