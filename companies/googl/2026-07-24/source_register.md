# GOOGL Source Register — Q2 2026 Refresh (as_of 2026-07-24)

| source_id | Tier | Source | Date | URL / path | Notes |
|---|---|---|---|---|---|
| GOOG.A1.2026Q2 | A1 | Alphabet Q2 2026 results, 8-K Exhibit 99.1 | 2026-07-22 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm | PRIMARY earnings release; verbatim extracts in `raw/q2_2026_primary_extracts.md` (retrieved with SEC-compliant UA; default WebFetch UA -> 403) |
| GOOG.A1.2026Q2.10Q | A1 | Alphabet Q2 2026 Form 10-Q | 2026-07-22 | via StockTitan 10-Q summary https://www.stocktitan.net/sec-filings/GOOG/10-q-alphabet-inc-quarterly-earnings-report-8ffb92bbee5d.html | Cloud RPO $513.9B / total RPO $519.5B; H1 OCF/capex confirm |
| INVESTING-CAPEX-GUIDE | B/C | Investing.com — "Alphabet Q2 2026 slides" | 2026-07-22 | https://www.investing.com/news/company-news/alphabet-q2-2026-slides-24-revenue-growth-cloud-surges-despite-capex-93CH-4807148 | FY2026 capex $195-205B; Cloud margin 35.6%; TTM FCF -20%; Q3 third-party-capacity margin note |
| SEEKINGALPHA-CAPEX | C | Seeking Alpha news | 2026-07-22 | https://seekingalpha.com/news/4617114 | Confirms $195-205B capex + third-party-capacity bridge |
| CNBC-Q2 / MLQ / QZ | C | CNBC live blog / MLQ / Quartz | 2026-07-22 | (see WebSearch synthesis) | Corroborate capex raise, revenue $119.8B, Cloud +82% |
| S-YHOO-2026-07-23 | A1(price) | Yahoo Finance v8 chart API | 2026-07-23 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL | 2026-07-23 close $317.69 (last settled close <= as_of 2026-07-24); series also gives 07-22 $342.09, 07-24 ~$319.7 |
| SA-GOOGL-PRICE | B | stockanalysis.com | 2026-07-24 | https://stockanalysis.com/stocks/googl/ | previous close $317.69; 52wk $187.82-$408.61; shares 12.23B; mkt cap ~$3.91T |
| GOOGL-PRIOR-DOSSIER | internal | companies/googl/2026-06-19/ | 2026-06-19 | (repo) | Prior WATCH; signals +1/+2/+1/-1/-1/-2; buy_below ~$113; carries deep moat/value-chain/operator write-ups |

Fetch note (2026-07-24): SEC blocks the default WebFetch UA (HTTP 403); the primary Q2 8-K was retrieved via a compliant SEC User-Agent and parsed from primary HTML. Business-structure sources (10-K, proxy, financing docs) carry forward from the 2026-06-19 register.

Tier rules: `../../../sources/source_policy.md`.
