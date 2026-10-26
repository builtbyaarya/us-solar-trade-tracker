# Changelog

## 2026-10-23
- `docs/index.html` rebuilt for industry readers: one headline landed cost per origin with a plain verdict against US-assembled, the duty stack readable layer by layer with hover and tap explanations (what the layer is, the rate, the source and date), an "Import or buy US-assembled?" comparison, and a one-page print summary. The map now zooms smoothly to the Southeast Asia cluster with labels that do not overlap. No change to any number, table, filter, link or source; `data/` untouched.

## 2026-10-22
- New "Landed cost" tab: what a TOPCon module costs per watt at a US port by origin (public spot price, derived ocean freight, then AD, CVD, Section 301, the forced-labour Section 301 and, from 4 Dec 2026, the Section 232 tariff and the $0.38/W minimum import price), on a map with an editable breakdown. Inputs and every source are in `data/landed_cost_inputs.json`; AD and CVD come from this tracker's own rows.
- Page split into three tabs (Overview, Duty rates, Factories) with a shorter intro; system font (San Francisco on Apple devices), Archivo embedded as the fallback.
- Studio look for `docs/index.html`: light grey background, white cards, pill labels, graphite and amber bars, matching the game.
- Redesigned `docs/index.html` to match the Solar Factory game: flat deep background, one amber accent, Archivo embedded in the file (nothing loads from Google Fonts), a small wafer-stack mark in the header linking to the game, and a fuller footer (data as is, no tracking, CC BY 4.0 data and MIT code, corrections link). No change to any number, table, filter or link.

## 2026-10-21
- First release: 222 duty-rate rows (Solar I to IV, Section 201, Section 301) and 66 facility rows, every row sourced.
- Solar IV (India, Indonesia, Laos): final determinations of 11 Sep 2026 and the ITC vote of 14 Oct 2026 are in; the AD/CVD order notices are placeholders until Commerce publishes them (expected early Nov 2026).
