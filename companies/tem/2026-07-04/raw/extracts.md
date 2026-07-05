# TEM Raw Primary Extracts

as_of: 2026-07-04 | Fetched: 2026-07-04

## Fetch method note (robustness)
SEC EDGAR blocks the harness's default WebFetch user-agent (403 Forbidden) on both attempts via the standard tool. Per the robustness protocol (max 2 attempts/URL, no retry-loops), fell back immediately to `curl` with an explicit research User-Agent + `-L` redirect-following, which succeeded (HTTP 200) on the first follow-up attempt for all 3 primary documents below. This is a documented fallback, not a stall.

## Primary documents fetched (full text converted to line-based .txt for grep, in scratchpad — not committed; key figures transcribed into facts.md / claim_ledger.csv)

1. **TEM 10-K FY2025** (period ended Dec 31, 2025; filed 2026-02-24)
   URL: https://www.sec.gov/Archives/edgar/data/0001717115/000119312526066961/tem-20251231.htm
   Size: 6.16 MB HTML / 5,769 lines converted text
   Contains: full FY2025 audited financials, MD&A, risk factors, competitive position discussion (FMI/Guardant reimbursement admission), cash flow statement detail, debt schedule (Convertible Notes conversion terms), related-party notes (SB Tempus, Pathos), share count as of Feb 20, 2026.

2. **TEM 8-K Q4/FY2025 Earnings Release Exhibit 99.1** (filed ~2026-02-24, same period)
   URL: https://www.sec.gov/Archives/edgar/data/0001717115/000119312526066931/tem-ex99_1.htm
   Size: 1.61 MB HTML / 1,817 lines converted text
   Contains: Q4 2025 + FY2025 revenue/EBITDA/net-loss highlights, segment detail (Diagnostics vs Data and applications), FY2026 initial guidance ($1.59B revenue / ~$65M adj EBITDA).

3. **TEM 10-Q Q1 2026** (period ended March 31, 2026; filed 2026-05-05)
   URL: https://www.sec.gov/Archives/edgar/data/0001717115/000119312526206356/tem-20260331.htm
   Size: 2.73 MB HTML / 2,494 lines converted text
   Contains: Q1 2026 condensed balance sheet, statements of operations, cash flow statement, segment revenue, related-party note detail (SB Tempus VIE, Pathos Master Agreement), stock-based compensation, debt schedule as of 3/31/2026, competitive/reimbursement risk-factor language.

## Secondary/cross-check sources (WebSearch, not fetched in full — used for price cross-check, pharma-deal sizing, governance background)
- Yahoo Finance / Perplexity Finance / MarketBeat aggregation (price, 52wk range) — websearch 2026-07-04
- FierceBiotech, Pharmaceutical Technology (AstraZeneca/Pathos $200M deal) — websearch 2026-07-04
- IntuitionLabs pricing analysis (GSK/Merck/Gilead deal sizing) — websearch 2026-07-04, single/thin-sourced, flagged OPEN
- TechCrunch, Wikipedia (Eric Lefkofsky background/track record) — websearch 2026-07-04
- Governance/proxy tracker (Class B voting power %, 30-votes-per-share structure) — websearch 2026-07-04
- Multiple earnings-summary aggregators (Bitget, AllInvestView, 247WallSt, Seeking Alpha) confirming Q1 2026 guidance reiteration — websearch 2026-07-04

## Key line-item locations (for audit trail — line numbers in converted scratchpad .txt files)
- 10-K balance sheet (cash $604.787M, YE2025): line 2088-2092
- 10-K cash flow summary table (OCF/investing/financing FY2025 vs FY2024): line 1962-1994
- 10-K total revenue/net loss/adj-EBITDA one-liner (FY2025/24/23 three-year comp): line 1427
- 10-K accumulated deficit "$2.4 billion" explicit statement: line 1923
- 10-K convertible notes conversion price $84.19: line 1937
- 10-K FMI/Guardant reimbursement-gap admission: line 483
- 10-Q balance sheet (Q1 2026 vs YE2025 comparative): line 110-281
- 10-Q statement of operations (Q1 2026 vs Q1 2025 comparative): line 284-399
- 10-Q cash flow statement (OCF $(73,277)K / investing $(10,067)K / financing $(271)K): line 490-618
- 10-Q related-party notes (SB Tempus VIE $81.7M, Pathos $25.0M related-party asset, IP License Agreement ¥7.5B): line 1370-1378
- 8-K FY2025/Q4 highlights + FY2026 guidance ($1.59B / ~$65M adj EBITDA): line 10-31, 94
