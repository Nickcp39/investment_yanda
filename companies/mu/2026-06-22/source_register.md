# MU Source Register — as_of 2026-06-22 (LIVE)

Tier key: A1 = primary (SEC / official IR) · B = reputable secondary (data aggregators, major media) · C = commentary/sell-side · D = social/KOL (lead only).

| source_id | name | public_date | url / path | tier |
|---|---|---|---|---|
| S1 | Micron Q2 FY2026 earnings press release (8-K EX-99.1, quarter ended 2026-02-26) | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000004/a2026q2ex991-pressrelease.htm | A1 |
| S2 | Micron 10-Q FY2026 Q2 (period 2026-02-26) | 2026-03 | https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000006/mu-20260226.htm | A1 |
| S3 | Micron Q2 FY2026 prepared remarks (IR static file) | 2026-03-18 | https://investors.micron.com/static-files/e089f8c0-065d-47b8-9d02-bfa863cdb357 | A1 |
| S4 | stockanalysis.com — MU quote / statistics / financials (price, mcap, P/E, P/B, EV, cash, debt, 52wk band, 6-yr financial history) | 2026-06-22 | https://stockanalysis.com/stocks/mu/ | B |
| S5 | Yahoo Finance chart API — MU daily price series, 52wk band (price source of truth for freshness gate) | 2026-06-22 | https://query1.finance.yahoo.com/v8/finance/chart/MU | B |
| S6 | StockTitan — Micron to report fiscal Q3 2026 results on June 24, 2026 (earnings date) | 2026-06 | https://www.stocktitan.net/news/MU/micron-technology-to-report-fiscal-third-quarter-results-on-june-24-22gcrbths4gp.html | B |
| S7 | GuruFocus — "Micron Set to Release Q3 Earnings Amid Price Surge" (consensus, price, YTD) | 2026-06 | https://www.gurufocus.com/news/8924495/ | C |
| S8 | TradingKey / IND Money — Micron Q3 earnings preview (consensus est., HBM context) | 2026-06 | https://www.tradingkey.com/analysis/stocks/us-stocks/261975340-mu-q3-earnings-preview-june-2026-tradingkey | C |
| S9 | Astute Group — "SK hynix holds 62% of HBM, Micron overtakes Samsung; 2026 battle pivots to HBM4" (market share) | 2025/2026 | https://www.astutegroup.com/news/general/sk-hynix-holds-62-of-hbm-micron-overtakes-samsung-2026-battle-pivots-to-hbm4/ | C |
| S10 | TrendForce — HBM4 share projections; Samsung mid-20%, demand growth 2026/2027 | 2025-11 to 2026-02 | https://www.trendforce.com/ | B |
| S11 | Seeking Alpha (multiple) — bear cases: "Melt-Up Looks Late Cycle; Don't Chase"; "Market Share Is My Biggest Concern"; "Three Significant Risks" | 2026 | https://seekingalpha.com/symbol/MU | C |
| S12 | Blocks & Files — "Micron's massive memory money making machine" (Q2 FY26 BU detail, DRAM record $18.8B) | 2026-03-19 | https://www.blocksandfiles.com/ai-ml/2026/03/19/microns-massive-memory-money-making-machine/ | C |
| S13 | MarketBeat / consensus — MU analyst price-target distribution, avg target ~$965 | 2026-06 | https://www.marketbeat.com/stocks/NASDAQ/MU/forecast/ | C |
| O01 | Wikipedia — Sanjay Mehrotra (formation/biography) | <= 2025 | https://en.wikipedia.org/wiki/Sanjay_Mehrotra | C |
| O02 | Computer History Museum — Sanjay Mehrotra oral history | 2019 | https://www.computerhistory.org/collections/catalog/102740456 | B |
| O03 | Micron IR — Mark Murphy CFO appointment + bio | 2022-04-18 | https://investors.micron.com/news-releases/news-release-details/micron-appoints-mark-murphy-executive-vice-president-and-chief | A1 |
| O04 | Micron — leadership page (Sadana, Bhatia) | 2026-06-22 | https://www.micron.com/about/company/leadership | A1 |
| O05 | Micron — Scott DeBoer leadership bio (CTPO) | 2026-06-22 | https://www.micron.com/about/company/leadership/scott-deboer | A1 |
| M1 | Repo macro file — 2026Q2 memory supercycle research | 2026-05-06 | macro/2026Q2_memory_supercycle_research.md | (internal) |
| M2 | Repo macro file — 2026Q1 hyperscaler capex check (demand-durability signals) | 2026-05-06 | macro/2026Q1_hyperscaler_capex_check.md | (internal) |
| P0 | Prior backtest case (THESIS PRIOR ONLY — frozen at 2025-03-21, not current facts) | as_of 2025-03-21 | backtests/framework_validation/cases/mu_2025-03-21/ | (prior) |

## Notes on tiering / discipline

- **Price/market-cap/52wk band**: S5 (Yahoo) is the freshness source of truth, cross-checked by S4 (stockanalysis) + S7 (gurufocus). All within tolerance.
- **Reported financials (Q2 FY2026)**: S1/S2/S3 primary. Every load-bearing financial number traces to S1 (the 8-K press release) verified by direct SEC fetch.
- **Forward guidance**: S1 (issued by management) — labeled as guidance, NOT a result. Q3 actual reports 2026-06-24 (post-as_of).
- **HBM market share / competitive**: S9/S10 secondary — used as INTERPRETATION/context, never as a hard EVIDENCE claim supporting a buy.
- **Bear cases (S11)**: commentary tier — used to stress-test the thesis (M5), not as proof.
- **KOL/social**: none promoted to facts.md.
