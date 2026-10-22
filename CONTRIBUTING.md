# Contributing

Corrections and additions are welcome. The one rule: every number needs a public source.

## Adding or correcting a row

1. Find the primary document: a Federal Register notice (federalregister.gov or govinfo.gov), a Commerce fact sheet, a USITC release, a company press release or a state announcement. Trade press is fine for factory status when nothing primary exists; say so in `notes`.
2. Edit `data/duties.csv` or `data/factories.csv` following `docs/schema.md`. One row per rate or per facility and stage. Never overwrite an earlier stage; add a new row.
3. Run `python3 scripts/validate.py` (it must print OK) and `python3 scripts/build.py` (rebuilds `data/tracker.json` and the README tables).
4. Open a pull request. In the description quote the table or sentence in the source that supports the change, with page or section.

## What gets declined

- A row with no `source_url`, or a URL that does not show the figure.
- AD and CVD combined into one number.
- Estimates, "about", or figures copied from another aggregator without the primary document.
- Anything about a company that is not a public source.

## Reporting an error

Open an issue with the row (case, country, company, duty type or facility name), what you think is wrong, and the document that shows the correct value. Errors in rates are fixed first.

## Code

Scripts are plain Python 3 with no dependencies beyond the standard library, so anyone can run them. Keep it that way.
