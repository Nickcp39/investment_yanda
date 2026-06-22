# GEV Source Register

Last updated: 2026-06-21 (run_date) | as_of: 2026-06-19 | pipeline: lean-6module-v1.1

Tier rules: `../../../sources/source_policy.md`

| source_id | Tier | Source | Public Date | URL / Local Path | Notes |
|---|---|---|---|---|---|
| GEV-8K-4Q25-ER | A1 | GE Vernova Q4 & FY2025 earnings press release (8-K exhibit) | 2026-01-28 | https://www.gevernova.com/sites/default/files/gev_webcast_pressrelease_01282026.pdf | Primary IR; FY2025 revenue $38.1B, OCF $5.0B, FCF $3.7B, tax release $2.9B, backlog $150B; PDF binary — text extracted via gevernova.com/news article |
| GEV-8K-1Q26-ER | A1 | GE Vernova Q1 2026 earnings press release (8-K exhibit, filed 2026-04-22) | 2026-04-22 | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm (403) / stocktitan.net summary | Primary 8-K; Q1'26 revenue $9.34B, FCF $4.8B, backlog $163B, guidance raised; SEC HTML blocked — used stocktitan.net structured summary cross-checked to Motley Fool transcript |
| GEV-10K-FY25 | A1 | GE Vernova FY2025 10-K (fiscal year ended 2025-12-31) | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm | CIK 1996810; full annual report; SEC direct access blocked (403) — numbers cross-verified via stockanalysis.com, press release, and web search corroboration |
| GEV-8K-1Q26-TRANSCRIPT | A2 | GE Vernova Q1 2026 earnings call transcript | 2026-04-22 | https://www.fool.com/earnings/call-transcripts/2026/04/22/ge-vernova-gev-q1-2026-earnings-transcript/ | A2 (primary call; Motley Fool transcript); key quotes: +10–20% GT pricing, 100 GW milestone, BWRX-300 progress, Wind tariff impact |
| GEV-DEC25-INVESTOR-UPDATE | A2 | GE Vernova December 2025 Investor Update (transcript/slides) | 2025-12-09 | https://www.gevernova.com/sites/default/files/gev_webcast_transcript_12092025.pdf | A2; 2028 targets: $52B revenue, 20% EBITDA, $22B+ cumulative FCF, Power/Electrification 22% margins; PDF binary extracted via lastbastion.com summary + gevernova.com press release |
| GEV-DEC25-PR-DIVIDEND | A1 | GE Vernova press release: dividend doubled, buyback raised (8-K) | 2025-12-09 | https://www.gevernova.com/news/press-releases/ge-vernova-raises-multi-year-financial-outlook-doubles-dividend-increases-buyback-authorization | Dividend $1→$2/yr; buyback $6B→$10B |
| GEV-SA-FINANCIALS | B1 | StockAnalysis.com GEV income statement, cash flow, balance sheet | 2026-06-19 | https://stockanalysis.com/stocks/gev/financials/ | Annual I/S + CFO; quarterly Q1 2026; high-quality aggregator cross-checked to press release; used for segment revenue triangulation |
| GEV-SA-STATS | B1 | StockAnalysis.com GEV statistics page | 2026-06-19 | https://stockanalysis.com/stocks/gev/statistics/ | Market cap $298.2B, EV $292.2B, EV/EBITDA trailing 85.6x (distorted), shares 268.72M, net cash $6.0B |
| YAHOO-GEV-PRICE | B1 | Yahoo Finance chart API (GEV daily prices) | 2026-06-19 | https://query1.finance.yahoo.com/v8/finance/chart/GEV?range=1y&interval=1d | Last close $1,109.73 (2026-06-18); 52wk high $1,181.95; 52wk low $479.04; ≥2 sources confirmed |
| GEV-STOCKTITAN-1Q26 | B1 | StockTitan.net SEC filing summary — GEV 1Q 2026 | 2026-04-22 | https://www.stocktitan.net/sec-filings/GEV/8-k-ge-vernova-inc-reports-material-event-365b201cba34.html | Structured summary of Q1 2026 8-K; segment revenue, EBITDA, backlog data; cross-checked vs transcript |
| GEM-GT-MARKETSHARE | B2 | Global Energy Monitor — leading 3 GT manufacturers market share study | 2025 | https://globalenergymonitor.org/research/leading-three-manufacturers-providing-two-thirds-turbines-gas-fired-power-plants-under | GEV+Siemens+Mitsubishi ~two-thirds of plants under construction; GEV 38% Asia share |
| BWRX-ANS-2025 | A2 | ANS Nuclear Newswire — BWRX-300 UK regulatory milestone | 2025-12-16 | https://www.ans.org/news/2025-12-16/article-7621/article-7621/ | Step 2 GDA completed UK; cross-checked vs Q1 2026 transcript |
| GEV-LASTBASTION-DEC25 | B2 | Bastion Fiduciary — GEV December 2025 Investor Day summary | 2026-01-15 | https://lastbastion.com/2026/01/15/ge-vernova-december-2025-investor-day/ | Secondary analysis of investor day targets; used to extract 2028 numbers from PDF; cross-checked to GEV-DEC25-PR-DIVIDEND |

---

## Fetch notes (2026-06-21)

- SEC direct HTML/XBRL (data.sec.gov/submissions, EDGAR archives) returned HTTP 403 for all attempts without User-Agent bypass. SEC XBRL companyfacts API also returned 403.
- All A1/A2 numbers derived from: (1) official GEV press release PDFs (fetched directly — binary; text extracted via page description), (2) stocktitan.net structured SEC filing summaries, (3) gevernova.com IR article text, (4) Motley Fool earnings call transcript.
- Every load-bearing financial number cross-checked across ≥2 of: press release, stockanalysis.com, stocktitan.net, transcript.
- Price ($1,109.73) confirmed: Yahoo chart API + stockanalysis.com (both returned same value for 2026-06-18 close).
- **CIK: 1996810** (confirmed via SEC EDGAR web search result URL structure).
- 10-K accession: **000199681026000015** (gev-20251231.htm confirmed via search).
- Q1 2026 8-K accession: **000199681026000063**.
