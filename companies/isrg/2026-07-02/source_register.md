# ISRG Source Register

As-of: 2026-07-02 | Run: 2026-07-04

Tier: A1 = primary (SEC/official release/transcript) · A2 = official IR/exec page · B1 = reputable financial data · B2 = reputable media/aggregator · C = commentary/sentiment

| source_id | title | public_date | url_or_path | tier | used_for |
|---|---|---|---|---|---|
| ISRG-Q1-2026-PR | Intuitive Q1 2026 earnings release (8-K ex-99.1 / IR) | 2026-04-21 | https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000029/q126ex-991earningsrelease.htm | A1 | Q1 revenue, procedures, placements, non-GAAP EPS/GM, FY26 guidance |
| ISRG-10Q-Q1-2026 | Intuitive Q1 2026 10-Q (via StockTitan mirror) | 2026-04-21 | https://www.stocktitan.net/sec-filings/ISRG/10-q-intuitive-surgical-inc-quarterly-earnings-report-a75820ad0806.html | A1/B2 | Revenue split (I&A/Systems/Service), GAAP EPS, GM, cash+investments, shares, R&D |
| ISRG-Q4-2025-PR | Intuitive Preliminary Q4 & FY2025 results | 2026-01-13 | https://isrg.intuitive.com/news-releases/news-release-details/intuitive-announces-preliminary-fourth-quarter-and-full-year-5/ | A1 | FY2025 revenue split, year-end installed base (11,106), FY25 placements (1,721; 870 dV5) |
| ISRG-Q3-2025-PR | Intuitive Q3 2025 earnings release (8-K) | 2025-10-16 | https://www.sec.gov/Archives/edgar/data/0001035267/000103526725000206/q325ex-991earningsrelease.htm | A1 | Ion installed base (954 @ Q3'25), da Vinci installed base (10,763 @ Q3'25) |
| ISRG-SA-FINANCIALS | stockanalysis ISRG financials | 2026-07-02 | https://stockanalysis.com/stocks/isrg/financials/ | B1 | 5-year trend (revenue, margins, EPS, FCF), TTM figures |
| ISRG-SA-STATS | stockanalysis ISRG overview/statistics | 2026-07-02 | https://stockanalysis.com/stocks/isrg/ | B1 | Price, mcap, shares, 52wk band, P/E, EPS, revenue |
| YAHOO-ISRG-PRICE | Yahoo Finance chart API (ISRG) | 2026-07-02 | https://query1.finance.yahoo.com/v8/finance/chart/ISRG | B1 | As-of price $426.01, price path (re-fetched by freshness gate) |
| GOOGLE-ISRG-PRICE | Google Finance (ISRG:NASDAQ) | 2026-07-02 | https://www.google.com/finance/quote/ISRG:NASDAQ | B1 | Price cross-check $426.01, prev close $402.38, day range |
| ISRG-CEO-TRANSITION | Intuitive CEO transition effective July 1, 2025 (Dave Rosa) | 2025-05-15 | https://investor.intuitivesurgical.com/news-releases/news-release-details/intuitive-announces-ceo-transition-effective-july-1-2025/ | A1 | Dave Rosa -> CEO; Guthart -> Exec Chair; Rosa's builder background (SP, Ion) |
| ISRG-GUTHART-BIO | Gary Guthart executive bio (Intuitive) | 2026-01-01 | https://www.intuitive.com/en-us/about-us/company/leadership/gary-guthart | A2 | Guthart life-arc: SRI, Caltech PhD, Berkeley BS, 1996 first eng team, CEO 2010-25 |
| MDT-HUGO-FDA | Medtronic Hugo RAS FDA clearance for urology | 2025-12-03 | https://news.medtronic.com/2025-12-03-Medtronic-announces-FDA-clearance-of-Hugo-TM-robotic-assisted-surgery-system-for-urologic-surgical-procedures | A1 | Competitor: Hugo US urology clearance; Expand URO endpoints; ~230k US procedures |
| JNJ-OTTAVA-FDA | J&J submits Ottava to FDA (De Novo) | 2026-01-07 | https://www.jnj.com/media-center/press-releases/johnson-johnson-submits-ottava-robotic-surgical-system-to-the-u-s-food-and-drug-administration | A1 | Competitor: Ottava De Novo submission (general surgery, upper abdomen); FORTE endpoints |
| ISRG-QUIVER-JUL2 | QuiverQuant: ISRG gains ahead of mid-July earnings | 2026-07-02 | https://www.quiverquant.com/news/Intuitive+Surgical+Gains+as+Investors+Appear+to+Position+for+Mid-July+Earnings | B2 | July-2 pop = pre-earnings positioning (no hard catalyst); Q2 date 2026-07-16 |
| ISRG-FOOL-DECLINE | Motley Fool: ISRG down 28%, Wall Street thesis | 2026-07-03 | https://www.fool.com/investing/2026/07/03/intuitive-surgical-is-down-28-and-wall-street-is/ | B2 | De-rate drivers (instrument-life fears, Goldman rebuttal, 2020 Extended-Use precedent) |
| ISRG-SECTOR-NOTE | Lab US-healthcare sector map (internal) | 2026-06 | sectors/us-healthcare/行业结构与机会分析.md | C | Context: ISRG characterized as surgical-robotics near-monopoly, 15-20% growth |

## Evidence mix vs P1 minimum

- SEC filings / official releases: 5 (Q1-PR, 10-Q, Q4/FY25-PR, Q3-PR, CEO-transition) — meets P1.
- Earnings/management commentary: 1 (Q1 release + guidance) — meets P1.
- Historical price / market cap: 3 (Yahoo, stockanalysis, Google Finance) — exceeds P1.
- Reputable financial data / aggregator: 2 (stockanalysis x2) — meets P1.
- Competitor primary (FDA/company): 2 (Medtronic Hugo, J&J Ottava) — competition leg is primary-sourced.
- Sentiment/commentary: QuiverQuant, Motley Fool, GuruFocus — leads/context only, not load-bearing.

## Source-discipline notes

- Every load-bearing Q1 2026 and FY2025 number is primary (10-Q / earnings release), cross-checked vs stockanalysis where possible.
- Price is triple-sourced (Yahoo + stockanalysis + Google Finance), all $426.01, 0% delta — re-fetched by verify_freshness.py.
- OPEN (O1): direct SEC EDGAR full-text 10-Q returned HTTP 403 to the fetcher this pass; used the StockTitan 10-Q mirror + the SEC-hosted 8-K release text surfaced via search. Numbers corroborated across >=2 sources where load-bearing.
- OPEN (O2): non-GAAP owner-earnings bridge not fully reconstructed (GAAP diluted EPS $2.28 vs non-GAAP $2.50 gap is stock-comp + amortization + one-offs; used both).
- FY2025 EPS/FCF/margins are stockanalysis (B1) standardized; revenue split + installed base are primary (A1).
