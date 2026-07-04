# MELI Source Register

As-of: 2026-07-02 | Run: 2026-07-04

Tier: A1 = primary (SEC/official release/transcript) · A2 = official IR/exec page · B1 = reputable financial data · B2 = reputable media/aggregator · C = commentary/sentiment

| source_id | title | public_date | url_or_path | tier | used_for |
|---|---|---|---|---|---|
| MELI-Q1-2026-REL | MercadoLibre Q1 2026 Letter to Shareholders (8-K Ex 99.1, SEC EDGAR) | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/0001099590/000109959026000014/meli-20260507xex991.htm | A1 | Q1 revenue, margins, GMV/TPV, geography, credit book, NIMAL, NPL, mgmt commentary (fetched directly via urllib) |
| MELI-10Q-Q1-2026 | MercadoLibre Q1 2026 10-Q (StockTitan parse) | 2026-05-08 | https://www.stocktitan.net/sec-filings/MELI/10-q-mercadolibre-inc-quarterly-earnings-report-45532b4fae60.html | A1/B2 | Loans receivable net, allowance, provision expense, shares outstanding, cash |
| MELI-Q4-2025-REL | MercadoLibre Q4/FY2025 results (Businesswire / 8-K) | 2026-02-24 | https://www.businesswire.com/news/home/20260224245400/en/MercadoLibre-Inc.-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results | A1 | FY2025 revenue, Commerce/Fintech split, adjusted FCF, capex, Q4 metrics |
| MELI-FOOL-TRANSCRIPT | MercadoLibre Q1 2026 earnings call transcript | 2026-05-07 | https://www.fool.com/earnings/call-transcripts/2026/05/07/mercadolibre-meli-q1-2026-earnings-transcript/ | B1 | CFO "no margin guidance"; investment-posture commentary |
| MELI-SA-FINANCIALS | stockanalysis MELI financials | 2026-07-04 | https://stockanalysis.com/stocks/meli/financials/ | B1 | 5-year trend, TTM EPS/revenue |
| MELI-SA-STATS | stockanalysis MELI overview/statistics | 2026-07-04 | https://stockanalysis.com/stocks/meli/ | B1 | Price, mcap, shares, 52wk, P/E, P/S |
| YAHOO-MELI-PRICE | Yahoo Finance chart API (MELI) | 2026-07-02 | https://query1.finance.yahoo.com/v8/finance/chart/MELI | B1 | As-of price $1,763.36, 52wk band (re-fetched by gate) |
| GOOGLE-MELI-PRICE | Google Finance MELI | 2026-07-02 | https://www.google.com/finance/quote/MELI:NASDAQ | B1 | Price cross-check ($1,763.36, prev $1,742.19) |
| MELI-LEADERSHIP | MELI leadership transition (newsroom + Bloomberg + BA Times) | 2025-12-09 | https://news.mercadolibre.com/en/mercado-libre-leadership-transition-uruguay | A2/B1 | Galperin -> Exec Chairman 2026-01-01; new CEO Szarfsztejn; team bios |
| MELI-DEF14A-2026 | MercadoLibre 2026 Proxy Statement (DEF 14A) | 2026-04-23 | https://www.sec.gov/Archives/edgar/data/0001099590/000109959026000010/meli-20260423.htm | A1 | Galperin Trust ~7.00% ownership; one-share-one-vote governance; board |
| MELI-Q1-2026-SLIDES | MercadoLibre Q1 2026 slides recap (Investing.com) | 2026-05-08 | https://www.investing.com/news/company-news/mercadolibre-q1-2026-slides-49-revenue-surge-masks-margin-pressure-93CH-4670917 | B2 | Commerce/Fintech split, take rates, portfolio mix (secondary cross-check) |
| MELI-FCF-DEF | MELI adjusted-FCF definition (Q4'25 release + investor recaps) | 2026-02-24 | https://stockanalysis.com/stocks/meli/financials/cash-flow-statement/ | B1/B2 | Adjusted FCF normalization ($1.48B FY25; -$56M Q1'26) |
| SEA-6K-Q1-2026 | Sea Limited Q1 2026 6-K (Shopee GMV, Brazil) | 2026-05 | https://www.sec.gov/Archives/edgar/data/0001703399/000119312526219378/d78490dex991.htm | A1 | Shopee Brazil momentum (competitive stress) |
| NU-Q1-2026 | Nu Holdings Q1 2026 results | 2026-05 | https://international.nubank.com.br/company/nu-holdings-ltd-reports-first-quarter-2026-financial-results/ | A1 | Nubank scale (135M customers) for fintech competition |
| MACRO-ARG | Argentina macro (PIIE / Buenos Aires Herald) | 2026-06 | https://www.piie.com/blogs/realtime-economics/2026/argentinas-fragile-monetary-framework-risks-renewed-volatility | B1 | Argentina inflation/FX/Milei; devaluation tail risk |
| MACRO-BRL | Brazil Selic (Agência Brasil / tradingeconomics) | 2026-06 | https://tradingeconomics.com/brazil/interest-rate | B1 | Selic 14.25% easing cycle (credit-funding tailwind) |

## Evidence mix vs P1 minimum

- SEC filings / official releases: 5 (Q1 Letter [primary, direct fetch], 10-Q, FY25 release, DEF 14A, Sea/Nu comparables) — meets P1.
- Earnings/management commentary: 2 (Letter + call transcript) — meets P1.
- Historical price / market cap: 3 (Yahoo, stockanalysis, Google Finance) — exceeds P1.
- Reputable financial data / aggregator: 2 (stockanalysis ×2) — meets P1.
- Macro/competitive context: multiple (PIIE, tradingeconomics, Sea/Nu filings) — meets P1.
- Sentiment/commentary: TIKR, Motley Fool, Seeking Alpha noted as leads/analysis only.

## Source-discipline notes

- The Q1 2026 Letter (MELI-Q1-2026-REL) was fetched DIRECTLY from SEC EDGAR via urllib (generic web-fetchers get 403), so all Q1 operating metrics, geography, credit book, NIMAL, and the 15-90 day NPL (8.0%) are PRIMARY.
- Commerce/Fintech Q1'26 *segment* dollar split is secondary (slides) — flagged OPEN O2. FY2025 split is corroborated.
- 90+ day NPL not separately in the Letter -> OPEN O1.
- Galperin Trust 7.00% is a strong secondary read of the DEF 14A (SEC 403'd the generic fetcher for the proxy) -> OPEN O4; eyeball p.42 to lock.
- Adjusted FCF is MELI's own defined metric (strips fintech float); the raw aggregator FCF ($10.8B) is explicitly NOT used for valuation.
