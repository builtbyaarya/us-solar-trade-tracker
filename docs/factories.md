# US manufacturing capacity: the picture behind `data/factories.csv`

_Last checked: 2026-10-21. Every figure below has its source next to it; the CSV rows carry their own._

- Module capacity: SEIA/Wood Mackenzie Q3 2026 SMI (published 10 Sep 2026) puts US nameplate module capacity at roughly 66 GWdc, with only ~1 GWdc added in Q2 2026. Solar Power World's Aug 25 2026 manufacturer list sums to ~72 GW of claimed current module capacity (it counts nameplate from company claims, so it runs higher than SEIA). Source: https://seia.org/?p=17820 and https://www.solarpowerworldonline.com/wp-content/uploads/2026/08/0825.pdf
- Cell capacity: SEIA's Q3 2026 release does not state a cell figure. From the dataset, operating US silicon cell capacity is about 10 GW (Qcells 3.3, ES Foundry 3.0, Canadian Solar 2.1, Suniva 1.0, plus Silfab's 1 GW still under construction), with ~15 GW more under construction or announced (Boviet 3.0, T1 2.1 then +3.2, Talon 4.8, Mission/OCI 2.0, Nextnova 2.0, Suniva Laurens 4.5, Toyo 1.5, Convalt 3.6). First Solar's CdTe lines (~14 GW nameplate in 2026, 17.7 GW in 2027) are integrated and not counted as "cell" here.
- Upstream: wafer/ingot is still thin. Qcells Cartersville 3.3 GW ingot/wafer was listed as under construction in Aug 2026; Corning's Michigan wafer plant is ramping with no public capacity; NorSun Tulsa (5 GW) has no confirmed FID or construction since Dec 2024. Polysilicon is Hemlock (~20,000 t), Wacker TN (~20,000 t) and Highland Materials TN (20,000 t, 2027); REC Silicon Moses Lake closed Jan 2025.
- Trade/policy: the 6 Aug 2026 proclamation sets a 15% tariff plus minimum import prices on polysilicon, ingots, wafers, cells and modules from 4 Dec 2026 (per SEIA Q3 2026). OBBBA (Jul 2025) phased out the 45X/48E incentives that underpinned many 2023-24 announcements; the slowdown shows in SEIA's ~1 GW/quarter module adds.
- Cancellations: E2's Clean Economy Works tracker (manufacturing through Jun 2026) counts 72 cancellations, closures or downsizes in 2026 so far ($26.5B, 13.3 GW, 76,150 jobs) and, since Jan 2025, $35.4B of cancelled manufacturing investment and 52,533 manufacturing jobs across 214 combined project cancellations ($84.3B). Source: https://e2.org/reports/clean-economy-works-june-may-2026-2/ . Canary Media reported >$22B cancelled in H1 2025 alone: https://www.canarymedia.com/newsletters/clean-energy-cancellations-top-22-billion
- Notable factory losses in the dataset: Meyer Burger Goodyear AZ (1.4 GW, closed Jun 2025), Ebon Solar NM ($942M cell plant, cancelled May 2026), Freyr GA ($2.5B, Feb 2025), Kore Power AZ (12 GWh, Feb 2025), AESC SC ($1.6B, paused Jun 2025), Gotion MI (terminated), Toledo Solar (closed Jul 2024), REC Silicon (closed Jan 2025).
- Battery picture: the big EV cell JVs are being restructured toward LFP stationary storage. LGES started LFP ESS production at Lansing MI (ex-Ultium, >35 GWh) in Aug 2026; Ultium Spring Hill TN is retooling to LFP; BlueOval SK is being dissolved (Ford keeps Kentucky, SK On keeps the 45 GWh Tennessee plant, which had layoffs in Mar 2026); Panasonic Kansas (30 GWh) pushed back its full-capacity date; LGES Arizona targeted H1 2026 mass production (not reconfirmed).
- Data-quality flags: rows sourced only to the SPW list have status_date 2026-08-25 and no investment or jobs; Toyota NC, Ford Marshall MI, Ultium Spring Hill and Gotion MI were left out until a company or state release can be cited; capacity left blank wherever no source states it (Meyer Burger CO, Toledo Solar, REC Silicon, Corning wafer, LGES AZ, BlueOval KY, HL-GA, AESC, Gotion IL, Freyr, Form Energy, ENTEK, Toyota, Ford MI).

## Known gaps (not yet in the CSV; add with a company or state source)
Enphase (contract manufacturing via Flex in SC/TX/WI), Elin Energy, SolarCycle Cedartown GA (solar glass; no matching stage), Tesla Megafactory Waller County TX and Tesla/Hanwha supply, LGES Holland MI, Ultium Warren OH, Samsung SDI/Stellantis Kokomo IN, AESC Bowling Green KY, American Battery Factory Tucson AZ, Hemlock Clarksville TN polysilicon expansion.

## Pages the updater re-checks (also in `docs/watchlist.txt`)
- https://seia.org/research-resources/solar-market-insight-report-q3-2026 (and the next quarterly SMI; manufacturing section)
- https://seia.org/initiative-topic/manufacturing/ (SEIA manufacturing news and Supply Chain Dashboard)
- https://e2.org/reports/ (Clean Economy Works monthly memo; manufacturing appendix lists each cancellation)
- https://www.canarymedia.com/articles/clean-energy-manufacturing (Canary Media manufacturing desk)
- https://atlaspolicy.com/clean-economy-tracker/ (Atlas Public Policy Clean Economy Tracker)
- https://www.solarpowerworldonline.com/tag/manufacturing/ (SPW; its US manufacturer list is refreshed in print issues; latest: Aug 2026 PDF above)
- https://pv-magazine-usa.com/category/manufacturing/ (pv magazine USA manufacturing)
- https://www.utilitydive.com/topic/solar/ and https://www.manufacturingdive.com/topic/energy/ (Utility Dive / Manufacturing Dive)
- https://electrek.co/guides/solar-power/ and https://electrek.co/guides/batteries/ (Electrek)
- https://investor.firstsolar.com/news/default.aspx (First Solar press releases)
- https://www.hanwha.com/newsroom/news/press-releases.do (Qcells / Hanwha)
- https://ir.t1energy.com/news-events/press-releases (T1 Energy)
- https://news.lgensol.com/ (LG Energy Solution newsroom)
- https://www.dallasfed.org/research/energy (Dallas Fed US gigafactory tracker referenced by 2026 trackers)
