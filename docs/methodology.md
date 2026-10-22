# Methodology

How the rows in this dataset are collected, what each field means in trade-law terms, how the data are checked, and the references that define the terms. Read this before citing a number.

## 1. What a row is

### Duties (`data/duties.csv`)

One row is one rate for one respondent (or the all-others or country-wide row) under one instrument at one stage of one case. Antidumping (AD) and countervailing duty (CVD) rates are never added together in a row; a reader who wants the stack adds the rows, because that is what Customs does at the border (both are ad valorem on the entered value).

- **Stage.** `preliminary` and `final` are Commerce determinations; `order` is the notice that makes the duties permanent after the ITC's affirmative injury vote; `amended final` corrects ministerial errors; `review` is an administrative review (not yet tracked); `tariff` is used for Section 201 and 301 rows, which are not AD/CVD but sit in the same stack; `scope` is reserved for scope rulings.
- **determination_date** is the date on the "Dated:" line of the Federal Register notice (the signature date). Commerce often announces a determination the next day and the notice publishes a few days later; both go in `notes`. The independent check of 21 October 2026 found the first release had used the announcement date for the Solar IV finals, which is why the convention is written down here.
- **effective_date** is the date the notice says cash deposits apply from (usually the publication date).
- **Cash deposit vs assessment.** The rate in the notice is the cash deposit of estimated duties collected at entry. The final amount owed on those entries is set later in an administrative review, requested in the order's anniversary month, and can be higher, lower or the same; CBP then bills or refunds with interest. The dataset records the published rate and flags adjusted cash deposit rates (for example India's AD cash deposit of 107.17% against a 123.04% margin, adjusted for export subsidies) in `notes`. Source: CBP, AD/CVD FAQ.
- **Critical circumstances.** When affirmative, duties reach back 90 days before the preliminary determination. Recorded in `notes` per row because it differs by company.

### Factories (`data/factories.csv`)

One row is one facility at one manufacturing stage, so an integrated plant has several rows. `capacity_value` is the nameplate the company or a public tracker states, in the unit given; it is not output. `status` is the most recent public status with the date of the document that states it in `status_date`. Announced capacity is recorded as announced, and a cancellation, pause or closure is a new status on the same row with its own source, so the row history is visible in the git log.

## 2. Where the numbers come from

Primary sources, in order of preference:

1. Federal Register notices (via federalregister.gov and govinfo.gov), which carry the rate tables. The updater queries the Federal Register API for the term "crystalline silicon photovoltaic" and reads every new document.
2. Commerce Enforcement and Compliance fact sheets, which summarise determinations on the day of announcement, used until the notice publishes.
3. USITC news releases and reports for injury votes and critical-circumstances findings.
4. For factories: company press releases and investor pages first, then state economic development announcements, then the public trackers (SEIA and Wood Mackenzie Solar Market Insight, Solar Power World's manufacturer list, E2 Clean Economy Works, Atlas Public Policy Clean Economy Tracker), then reputable trade press. A row sourced only to a secondary aggregator is flagged in `notes` and queued for re-sourcing.

A row without a public URL is not accepted; `scripts/validate.py` enforces it.

## 3. How the data are checked

- Every commit runs `scripts/validate.py` (columns, allowed values, dates, numeric fields, source URL present).
- Each release gets an independent verification pass by a reader who did not build the rows, working only from the cited sources and reporting MATCH, MISMATCH or UNVERIFIED per row. The first pass (21 October 2026) checked 58 duty rows and 28 facility rows: every rate, company name and cash-deposit figure matched the notices; the mismatches were a date convention (fixed and defined above), two wrong AFA labels on Laos rows (fixed), two respondent counts (fixed) and nine factory rows with details not supported by the cited document (corrected or blanked). The report is kept in `docs/verification/`.
- Figures that could not be verified are left blank with a note rather than estimated.

## 4. Known limits

- Administrative review rates for the 2012, 2015 and 2025 orders are not yet tracked; the current cash deposit rate for a given Chinese or Southeast Asian exporter can differ from the order rate shown here.
- Scope and circumvention rulings (including the August 2023 circumvention finding covering Cambodia, Malaysia, Thailand and Vietnam) are not yet rows.
- The IEEPA and reciprocal tariff layers and the Section 232 action on polysilicon are not included.
- Capacity rows for several battery plants carry blank capacity because the cited document does not restate it.

## 5. References

Process and law:

- U.S. Department of Commerce, International Trade Administration. *U.S. Antidumping and Countervailing Duties.* https://www.trade.gov/us-antidumping-and-countervailing-duties
- U.S. International Trade Commission. *Understanding Antidumping and Countervailing Duty Investigations.* https://www.usitc.gov/press_room/usad.htm
- U.S. International Trade Commission. *Antidumping and Countervailing Duty Handbook.* https://www.usitc.gov/trade_remedy/adcvd_handbook.htm
- U.S. Customs and Border Protection. *AD/CVD Frequently Asked Questions* (cash deposits vs assessment). https://www.cbp.gov/trade/priority-issues/adcvd/antidumping-and-countervailing-duties-adcvd-frequently-asked-questions
- Congressional Research Service. *Circumvention Inquiry into Solar Imports*, IN11946 (2023). https://crsreports.congress.gov/product/details?prodcode=IN11946
- Congressional Research Service. *Solar Photovoltaics (PV): Status and Issues for Congress*, R48280 (2024). https://www.everycrsreport.com/reports/R48280.html
- Congressional Research Service. *Shining a Light on the Solar Trade*, LSB10066 (2018), on the Section 201 safeguard. https://www.everycrsreport.com/reports/LSB10066.html
- U.S. Department of Energy. *Overview of Trade and Policy Measures for U.S. Solar Manufacturing* (2025). https://www.energy.gov/eere/solar/overview-trade-and-policy-measures-us-solar-manufacturing
- Office of the Federal Register. *REST API documentation.* https://www.federalregister.gov/developers/documentation/api/v1

What the duties did (peer-reviewed and working papers):

- Wang, W. and Houde, S. (2026). The Incidence of the US-China Solar Trade War. *Journal of the Association of Environmental and Resource Economists* 13(1). https://doi.org/10.1086/736763
- Gerarden, T. D., Bollinger, B. K., Gillingham, K. and Xu, D. (2025). Strategic Avoidance and the Welfare Impacts of U.S. Solar Panel Tariffs. NBER Working Paper 34401. https://www.nber.org/papers/w34401
- Nguyen, L. et al. (2019). The US solar panel anti-dumping duties versus uniform tariff. *Energy Policy* 125. https://doi.org/10.1016/j.enpol.2018.11.048
- Kuang, Y.-X. et al. (2018). Who Benefits from Antidumping and Countervailing? *Emerging Markets Finance and Trade*. https://doi.org/10.1080/1540496x.2018.1515735
- Sharma, A. et al. (2022). Do clean energy trade duties generate employment benefits? *Renewable and Sustainable Energy Reviews* 157. https://doi.org/10.1016/j.rser.2022.112104
- Hughes, L. and Meckling, J. (2017). The politics of renewable energy trade: The US-China solar dispute. *Energy Policy* 105. https://doi.org/10.1016/j.enpol.2017.02.044
- Dehghanimadvar, M. et al. (2024). Quantifying the costs of diversifying silicon PV module assembly with local economic policies. *Joule* 8(4). https://doi.org/10.1016/j.joule.2024.02.006
- Smith, B. L. et al. (2021). Solar PV Manufacturing Expansions in the United States, 2017-2019. NREL. https://doi.org/10.2172/1775099
- Levinson, A. (2024) and Pancotti, E. and Tucker, T. N. (2024). Point/Counterpoint on clean-energy tariffs. *Journal of Policy Analysis and Management*. https://doi.org/10.1002/pam.22658 and https://doi.org/10.1002/pam.22653

Capacity, cost and policy benchmarks:

- U.S. Department of Energy (2022). *Solar Photovoltaics Supply Chain Deep Dive Assessment.* https://www.energy.gov/eere/solar/solar-photovoltaics-supply-chain-review-report
- Woodhouse, M., Smith, B., Ramdas, A. and Margolis, R. (2019). Crystalline Silicon PV Module Manufacturing Costs and Sustainable Pricing: 1H 2018 Benchmark. NREL/TP-6A20-72134. https://doi.org/10.2172/1495719
- Powell, D. M. et al. (2015). The capital intensity of photovoltaics manufacturing. *Energy and Environmental Science* 8. https://doi.org/10.1039/c5ee01509j
- U.S. Treasury and IRS (2024). Advanced Manufacturing Production Credit; Final Rule, 89 FR 85798. https://www.govinfo.gov/content/pkg/FR-2024-10-28/pdf/2024-24840.pdf
- SEIA and Wood Mackenzie. *U.S. Solar Market Insight* (quarterly). https://www.seia.org/research-resources/us-solar-market-insight
- E2. *Clean Economy Works* project tracker. https://e2.org/clean-economy-works/
- Atlas Public Policy. *Clean Economy Tracker.* https://atlaspolicy.com/clean-economy-tracker/
- Lawrence Berkeley National Laboratory (2026). *Queued Up: 2026 Edition.* https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf
