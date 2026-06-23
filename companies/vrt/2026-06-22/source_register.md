# Source Register — VRT (as_of 2026-06-22)

Tier scale: primary (A1/A2 — SEC filing / official release / transcript / IC deck) > secondary (B1/B2 — aggregator / industry / press) > commentary > social. KOL/social = lead or sentiment only; never EVIDENCE, never directly supports BUY.

| ID | Source | Public date | Link / path | Tier | Used for |
|---|---|---|---|---|---|
| S1 | VRT Q1 2026 earnings release / 8-K (Ex-99.1) | 2026-04-22 | https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026379/q12026exhibit991vrt04222026.htm | primary (A2) | Q1'26 revenue/margin/EPS/FCF; raised FY26 guide; fact of orders/B2B non-disclosure |
| S2 | VRT Q1 2026 earnings call transcript | 2026-04-22 | VRT IR / transcript aggregators | primary (A2) | "orders up YoY / backlog elongated" qualitative; 800V DC timing; ~75% hyperscaler mix commentary |
| S3 | VRT Q4/FY2025 earnings release / 8-K | 2026-02-11 | https://www.sec.gov/Archives/edgar/data/0001674101/000167410126000006/exhibit991vrt02112026.htm | primary (A2) | FY25 sales/margin/FCF; backlog $15.0B; Q4 orders +252% / B2B 2.9x (last hard print) |
| S4 | VRT 2026 Investor Conference deck (Greenville) | 2026-05-19 | VRT IR | primary (A2) | 2030 targets (20–22% CAGR / 27% margin), raised vs 2024 investor day |
| S5 | Vertiv × NVIDIA GB200 NVL72 reference design | 2024 | Vertiv / NVIDIA | primary (A2) | reference-design authority; 7MW power+cooling architecture; density specs |
| S6 | stockanalysis.com + Yahoo chart API + wallstreetzen | 2026-06-22 | https://stockanalysis.com/stocks/vrt/ ; https://query1.finance.yahoo.com/v8/finance/chart/VRT ; https://www.wallstreetzen.com/stocks/us/nyse/vrt | secondary (B2) | LIVE price/mcap/52wk/shares/multiples/Street target (needs_audit on multiples) |
| S7 | MarketsandMarkets liquid-cooling share | 2025–26 | MarketsandMarkets | secondary (B2) | ~11.3% share; DTC +26% CAGR; component commoditization |
| S8 | "Backlog Silence" analysis (Seeking Alpha) | 2026 | Seeking Alpha | secondary (B2) | third-party flag that the orders withdrawal was noticed — used only to support the *qualitative* "discretionary withdrawal = soft negative" read, NOT as an orders number |
| S9 | Big-4 hyperscaler capex aggregation | 2026 | press / hyperscaler calls | secondary (B2) | shared-switch macro: ~$700–725B 2026 (+62–77%) |
| S10 | Vertiv PR — ThermoKey acquisition completed | 2026-06-12 | https://www.prnewswire.com/news-releases/vertiv-completes-acquisition-of-thermokey-expanding-heat-rejection-portfolio-for-ai-data-centers-302798971.html | primary (A2) | NEW: bolt-on thermal M&A closed (EMEA heat-rejection) |
| S11 | VRT 8-K — quarterly dividend declaration | 2026-06-03 | https://www.sec.gov/Archives/edgar/data/0001674101/000162828026040031/exhibit991vrt-q22026divide.htm | primary (A2) | NEW: $0.0625/qtr dividend |

## Discipline notes

- **Latest hard quarter = Q1'26** (S1/S2, reported 2026-04-22). Q2'26 earnings = **2026-07-29** (not yet public at as_of). No 10-Q line-item pull beyond the release; segment split and net-cash composition remain open.
- **S6 multiples carry `needs_audit`** — aggregator-sourced; the LIVE price/mcap/52wk fields are cross-checked ≥2 sources in `freshness.json` and re-verified by `verify_freshness.py`. The valuation *multiples* (fwd P/E, EV/EBITDA) are not yet tied to a one-hand 10-Q balance sheet, but the conclusion direction (priced for perfection) is robust at any basis.
- **Zero C-tier pollution:** no KOL/video sources. S8 (Seeking Alpha, B2) used only to corroborate a disclosure *behavior*, never to supply the withheld orders number.
