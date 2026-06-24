# HWM Source Register

As-of: 2026-06-22 | Run: 2026-06-23

Tier: A1 = primary (SEC/official release/transcript) · A2 = official IR/exec page · B1 = reputable financial data · B2 = reputable media/aggregator · C = commentary/sentiment

| source_id | title | public_date | url_or_path | tier | used_for |
|---|---|---|---|---|---|
| HWM-Q1-2026-PR | Howmet Q1 2026 Results (PRNewswire press release) | 2026-05-07 | https://www.prnewswire.com/news-releases/howmet-aerospace-reports-first-quarter-2026-results-302764843.html | A1 | Q1 results, segments, end markets, guidance, balance sheet, buyback, M&A |
| HWM-Q1-2026-HOWMET | Howmet Q1 2026 Results (company IR page) | 2026-05-07 | https://www.howmet.com/financial-release/2026-05-07/howmet-aerospace-reports-first-quarter-2026-results/ | A2 | Cross-check release; CEO commentary (spares, Iranian-conflict note) |
| HWM-Q1-2026-8K | Howmet Q1 2026 8-K (StockTitan summary) | 2026-05-07 | https://www.stocktitan.net/sec-filings/HWM/8-k-howmet-aerospace-inc-reports-material-event-21557e1d5549.html | B2 | Guidance cross-check; spares figure (secondary, OPEN) |
| HWM-10Q-Q1-2026 | Howmet Q1 2026 10-Q (StockTitan) | 2026-05-07 | https://www.stocktitan.net/sec-filings/HWM/10-q-howmet-aerospace-inc-quarterly-earnings-report-76452e33be62.html | A1/B2 | Shares outstanding (cover 400,713,557 @ 2026-03-24) |
| HWM-SA-FINANCIALS | stockanalysis HWM financials | 2026-06-23 | https://stockanalysis.com/stocks/hwm/financials/ | B1 | 10-year trend, TTM FCF/EPS |
| HWM-SA-STATS | stockanalysis HWM overview/statistics | 2026-06-23 | https://stockanalysis.com/stocks/hwm/ | B1 | Price, mcap, shares, 52wk, P/E, EPS |
| YAHOO-HWM-PRICE | Yahoo Finance chart API (HWM) | 2026-06-22 | https://query1.finance.yahoo.com/v8/finance/chart/HWM | B1 | As-of price $280.36, 52wk band (re-fetched by gate) |
| HWM-PLANT-BIO | John C. Plant executive bio | 2026-01-01 | https://www.howmet.com/executive-leadership/john-plant/ | A2 | Operator life-arc, career history |
| HWM-CAPALLOC | Howmet dividend / capital allocation | 2026-05-07 | https://www.prnewswire.com/news-releases/howmet-aerospace-board-approves-common-stock-dividend-302751663.html | A1 | Dividend +20%, buyback authorization |
| HWM-FITCH-UPGRADE | Fitch upgrade to A- (via company/news) | 2026-02-13 | https://www.howmet.com/ | B2 | Credit rating, balance-sheet quality |

## Evidence mix vs P1 minimum

- SEC filings / official releases: 4 (PR, IR page, 8-K, 10-Q) — meets P1.
- Earnings/management commentary: 1 (release + CEO quotes) — meets P1.
- Historical price / market cap: 2 (Yahoo, stockanalysis) — meets P1.
- Reputable financial data / aggregator: 2 (stockanalysis ×2) — meets P1.
- Sentiment/commentary: noted as leads only (SimplyWallSt, Kalkine) — not load-bearing.

## Source-discipline notes

- Spares figure ($520M/+36%/23%) is B2/commentary-derived only -> flagged OPEN (O1); release confirms spares qualitatively.
- No direct SEC EDGAR full-text extraction this pass (used release + 10-Q summary + aggregators) -> OPEN (O2). Numbers all corroborated across >=2 sources where load-bearing.
