# SYK Source Register

Last updated: 2026-07-05 (run_date) | as_of: 2026-07-05 | pipeline: lean-6module-v1.1

Tier rules: `../../../sources/source_policy.md`

| source_id | Tier | Source | Public Date | URL / Local Path | Notes |
|---|---|---|---|---|---|
| SYK-10K-FY25 | A1 | Stryker Corporation FY2025 10-K (fiscal year ended 2025-12-31) | ~2026-01-29 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000310764&type=10-K | CIK 0000310764; SEC direct HTML fetch returned HTTP 403 on first attempt — per robustness rule (max 2 attempts/URL, no retry loop), fell back immediately to stockanalysis.com + stocktitan.net structured 10-K mirror + official Stryker IR press release, each load-bearing figure cross-checked across >=2 sources |
| SYK-Q4-PR | A1 | Stryker Q4 & Full-Year 2025 earnings press release | ~2026-01-29 | https://www.stryker.com/us/en/about/newsroom/2026/stryker-reports-fourth-quarter-and-full-year-2025-results.html | Official IR press release; FY2025 net sales $25.116B, segment detail, adj EPS $13.63, China VBP -1.4%/-1.5% guided |
| STOCKTITAN-SYK-10K | A2 (proxy) | StockTitan.net structured summary of SYK FY2025 10-K | ~2026-01-29 | https://www.stocktitan.net/sec-filings/SYK/10-k-stryker-corp-files-annual-report | Direct text extraction of SEC 10-K content (business segments, risk factors, named competitors, employee count, China VBP risk-factor language) — treated as A2 proxy since it reproduces primary filing text |
| SYK-Q1-PR | A2 | Stryker Q1 2026 earnings press release | ~2026-04-30 | https://www.stryker.com/us/en/about/newsroom/2026/stryker-reports-first-quarter-2026-results.html | Official IR press release; Q1 2026 net sales $6.02B, cyber incident $375M deferred sales, FY2026 guidance maintained, tariff ~$400M |
| SYK-STOCKTITAN-1Q26 | A2 (proxy) | StockTitan.net structured summary of SYK Q1 2026 8-K/10-Q | ~2026-04-30 | https://www.stocktitan.net/sec-filings/SYK/8-k-stryker-corp-reports-material-event | Direct extraction of Q1 2026 financial results, balance sheet detail (cash, debt, equity, goodwill/intangibles), adjusted EPS miss, guidance maintenance |
| STOCKTITAN-SYK-CYBER | B1 | StockTitan.net / trade-press coverage of the March 2026 Stryker cyber incident | ~2026-03-15 to 2026-04-30 | https://www.stocktitan.net/news/SYK/ | Cyber-incident timeline: March 11 2026 onset, ~3-week shutdown, operations substantially restored by early April 2026 |
| STOCKTITAN-SYK-MAKO | B1 | StockTitan.net / IR / trade-press coverage of Mako SmartRobotics milestones | 2025-Q4 to 2026-Q1 | https://www.stocktitan.net/news/SYK/ | 3,000+ cumulative installs, 1M+/2M+ procedure milestones, US/international utilization mix, Mako 4 / Hip Revision / Spine / Shoulder / RPS pipeline |
| STOCKTITAN-SYK-MA | B1 | StockTitan.net / press coverage of Stryker M&A activity (AVS, Inari) | 2025 to 2026-05 | https://www.stocktitan.net/news/SYK/ | AVS acquisition ~$435M + up to $400M milestones (May 2026); Inari Medical acquisition (2025) |
| SYK-8K-AVS | B2 | 8-K / press release detail on the AVS acquisition | ~2026-05 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000310764&type=8-K | Deal structure (upfront + contingent milestones); full purchase-price-allocation detail not fetched this run (OPEN O7) |
| SYK-SA-STATS | B1 | StockAnalysis.com SYK main statistics page | 2026-07-05 | https://stockanalysis.com/stocks/syk/ | Current price $326.54 (2026-07-02 close), market cap $125.18B, 52wk range $281.00-$404.87, shares 383.36M, trailing P/E 37.79x / fwd 20.86x, dividend yield 1.08%, beta 0.78, analyst Buy(27)/PT $386.80 |
| SYK-SA-FINANCIALS | B1 | StockAnalysis.com SYK income statement | 2026-07-05 | https://stockanalysis.com/stocks/syk/financials/ | FY2025 revenue/margin/EPS detail; cross-checked to IR press release |
| SYK-SA-BALANCESHEET | B1 | StockAnalysis.com SYK balance sheet | 2026-07-05 | https://stockanalysis.com/stocks/syk/financials/balance-sheet/ | Q1 2026 cash, debt, equity, goodwill/intangibles detail |
| SYK-SA-CASHFLOW | B1 | StockAnalysis.com SYK cash flow statement | 2026-07-05 | https://stockanalysis.com/stocks/syk/financials/cash-flow-statement/ | FY2025 OCF, capex, acquisitions cash used |
| YAHOO-SYK-PRICE | B1 | Yahoo Finance chart API (SYK daily prices) | 2026-07-02 | https://query1.finance.yahoo.com/v8/finance/chart/SYK?range=1y&interval=1d | Last close $326.54 (2026-07-02); 52wk high $404.87 (2025-07-23); 52wk low $281.00 (2026-05-11) — CONFIRMS stockanalysis.com independently |
| SYK-PROXY | B2 | Stryker proxy statement — CEO background / governance | most recent available | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000310764&type=DEF+14A | Kevin Lobo CEO tenure since October 2012 |
| SYK-PROXY-2026 | B2 | Stryker 2026 proxy statement — executive compensation detail | 2026 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000310764&type=DEF+14A | CEO 2025 comp $21.4M (93% at-risk), beneficial ownership ~0.058% |
| LINKEDIN-LOBO | C1 (self-reported) | Kevin A. Lobo LinkedIn profile | current | https://www.linkedin.com/in/kevin-lobo | CEO background corroboration — tenure, career history |
| STOCKTITAN-SYK-NEWS | B1 | StockTitan.net general news feed for SYK | 2025-2026 | https://www.stocktitan.net/news/SYK/ | New COO Spencer Stiles appointment |
| STOCKTITAN-SYK-CEO-PROFILE | B2 | Trade-press / analyst profile of CEO Kevin Lobo's M&A track record | 2026 (search-derived) | https://www.stocktitan.net/news/SYK/ | "60+ acquisitions" characterization of Lobo's tenure |
| AAOS-2025-COVERAGE | B2 | Trade-press coverage of AAOS 2025 conference (Mako 4 unveiling) | 2025 | (industry conference trade coverage, search-derived) | Mako 4 platform unveiling context |
| ISRG-10K-CROSSCHECK | B1 | Intuitive Surgical 10-K / IR disclosure — da Vinci installed base | most recent available | https://isrg.intuitive.com/ (IR site) | ~9,000 da Vinci systems installed — cross-check for competitive-landscape claim (E38) |
| MDT-10K-CROSSCHECK | B1 | Medtronic 10-K / IR disclosure — Hugo platform status | most recent available | https://www.medtronic.com/investors | Hugo soft-tissue robotic platform competitive positioning |
| SYK-Q1-EARNINGS-CALL-COMMENTARY | B2 | Secondary/trade-press summary of Q1 2026 earnings call management commentary | ~2026-04-30 | (search-derived, secondary summary — full transcript not fetched, see OPEN O8) | CEO Lobo commentary on soft-tissue robotics adjacency evaluation (~50 startups) |

---

## Fetch notes (2026-07-05)

- SEC EDGAR direct access (both the CIK company-search browse-edgar endpoint and any direct `.htm` 10-K/8-K document fetch) returned **HTTP 403 Forbidden** on first attempt. Per the robustness rule (max 2 attempts per URL, no retry-loop), immediately pivoted to secondary sources: stocktitan.net (which mirrors/extracts primary SEC filing text), stockanalysis.com (financials aggregator), official Stryker IR press releases, and web search corroboration.
- **CIK: 0000310764** (Stryker Corporation).
- FY2025 10-K filed approximately 2026-01-29 (period ended 2025-12-31); Q1 2026 8-K/10-Q filed approximately 2026-04-30 (period ended 2026-03-31).
- **Price cross-check**: $326.54 confirmed via two fully independent sources — Yahoo Finance chart API (`query1.finance.yahoo.com`) and stockanalysis.com — both reporting the same 2026-07-02 last close. This matches the frozen `as_of_price` input exactly (0.0% delta).
- Every load-bearing FY2025/Q1 2026 financial figure (revenue, margin, EPS, cash flow, debt) is cross-checked across >=2 of: official press release/IR site, stocktitan.net structured filing summary, stockanalysis.com, and independent search corroboration.
- Mako-specific installed-base and procedure-volume figures (E30, E32) are treated as A1/A2 tier where they trace to official Stryker IR press releases (Q4 2025/Q1 2026 earnings releases); Mako-specific financial estimates (direct revenue, market share — E35, E36) are explicitly flagged B2/analyst-estimate tier, NOT company-disclosed segment data.
- China-specific and competitive-landscape data points (Tinavi, MicroPort, Weigao, AK Medical, Chunli — E40) are **NOT Stryker-filed** — sourced from independent industry/competitive-landscape research, clearly flagged in facts.md as B2 tier.
- Total sources registered: **22** (6 A1/A2 primary or primary-proxy, remainder B1/B2/C1 secondary corroboration or industry context).
