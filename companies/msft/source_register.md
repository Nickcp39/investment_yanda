# MSFT Source Register

Last updated: 2026-06-19 (cold-start run; all A1 sources fetched from SEC EDGAR XBRL + primary filings; price from Yahoo chart API)

| source_id | Tier | Source | Date | URL / Local path | Notes |
|---|---|---|---|---|---|
| MSFT-10K-2025 | A1 | Microsoft FY2025 10-K (FY end 2025-06-30) | 2025-07-30 | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm | Primary annual filing |
| MSFT-10K-2024 | A1 | Microsoft FY2024 10-K | 2024-07-30 | https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm | Prior year |
| MSFT-10Q-Q3-2026 | A1 | Microsoft Q3 FY2026 10-Q (qtr end 2026-03-31) | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm | Latest quarterly filing |
| MSFT-Q3-2026-ER | A1 | Microsoft Q3 FY2026 earnings press release / 8-K | 2026-04-29 | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast | Official IR earnings release |
| MSFT-Q3-2026-PERF | A1 | Microsoft Q3 FY2026 IR performance page | 2026-04-29 | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/performance | Official IR segment data |
| MSFT-XBRL-FACTS | A1 | SEC EDGAR XBRL companyconcept API (CIK 0000789019) | retrieved 2026-06-19 | https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/ | 10-yr audited series: revenue, op income, net income, OCF, capex, buybacks, dividends, balance sheet, shares |
| MSFT-PROXY-2025 | A1 | Microsoft 2025 DEF 14A proxy statement | 2025-10-21 | https://www.sec.gov/Archives/edgar/data/789019/000119312525245150/d908201ddef14a.htm | Governance: board, exec comp, voting, shareholder proposals |
| MSFT-8K-2026-06 | A1 | Microsoft 8-K filed 2026-06-05 (event 2026-06-02) | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/789019/000119312526258667/d26760d8k.htm | Recent material event (verify item) |
| YAHOO-MSFT-PRICE | B1 | Yahoo Finance chart API (query2.finance.yahoo.com) | retrieved 2026-06-19 | https://query2.finance.yahoo.com/v8/finance/chart/MSFT?range=1mo&interval=1d | Daily closes; latest close 2026-06-18 $379.40; 52wH $555.45 / 52wL $356.28 |
| MSFT-Q3-COMMENTARY | B2 | Secondary commentary on Q3 FY26 call (Futurum / AlphaStreet / CNBC) | 2026-04-29..30 | https://news.alphastreet.com/microsoft-msft-q3-fy2026-azure-hits-40-growth-as-ai-business-reaches-37-billion-run-rate/ | Azure +40%, AI run-rate $37B, FY26 capex ~$190B guide — used as lead; figures cross-checked to IR/10-Q where possible |

Fetch notes (2026-06-19):
- SEC default WebFetch UA returns HTTP 403; all A1 SEC data retrieved via SEC-compliant User-Agent through the XBRL companyconcept/companyfacts API and primary IR pages.
- Yahoo chart API succeeded via PowerShell Invoke-RestMethod (Git-Bash python stub failed; not a data issue).
- OPEN: full-text 10-Q/10-K segment notes and proxy detail not line-by-line verbatim-extracted this pass (XBRL aggregates + official IR press release used instead). Azure +40% and AI run-rate $37B come from official IR press release (A1) corroborated by secondary; FY26 capex ~$190B guide is from the earnings call (secondary capture, B2) pending verbatim transcript — marked accordingly in facts.md.

Tier rules: `../../sources/source_policy.md`.
