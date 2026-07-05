# TEM Source Register

Last updated: 2026-07-04 (run_date) | as_of: 2026-07-04 | pipeline: lean-6module-v1.1

Tier rules: `../../../sources/source_policy.md`

| source_id | Tier | Source | Public Date | URL / Local Path | Notes |
|---|---|---|---|---|---|
| TEM-10K-FY25 | A1 | Tempus AI, Inc. FY2025 10-K (fiscal year ended 2025-12-31) | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/0001717115/000119312526066961/tem-20251231.htm | CIK 0001717115; full annual report, 6.16MB HTML; SEC direct WebFetch 403'd (2 attempts) — fetched successfully via curl with explicit research User-Agent + `-L` redirect follow; full audited financials, MD&A, risk factors, competitive/reimbursement admission (FMI/Guardant), related-party notes, debt schedule |
| TEM-8K-4Q25-ER | A1 | Tempus AI Q4/FY2025 earnings release (8-K Exhibit 99.1) | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/0001717115/000119312526066931/tem-ex99_1.htm | Primary earnings release; FY2025 revenue $1,271.8M, adj EBITDA -$7.4M, FY2026 initial guidance ($1.59B rev / ~$65M adj EBITDA); fetched via curl fallback (SEC WebFetch 403'd) |
| TEM-10Q-Q1-2026 | A1 | Tempus AI Q1 2026 10-Q (period ended 2026-03-31) | 2026-05-05 | https://www.sec.gov/Archives/edgar/data/0001717115/000119312526206356/tem-20260331.htm | Latest quarter; 2.73MB HTML; condensed balance sheet, statement of operations, cash flow, related-party notes (SB Tempus VIE, Pathos), debt schedule as of 3/31/2026; fetched via curl fallback |
| TEM-WEBSEARCH-PRICE | B2 | Websearch price aggregation (Perplexity Finance / MarketBeat / Yahoo summary) | 2026-07-04 | websearch query "Tempus AI TEM stock price July 2026" | Independent cross-check of frozen as_of_price $60.27; websearch returned $60.04 (0.4% delta, within normal noise); 52wk range $41.73-$104.32 |
| TEM-TRADEPRESS-ASTRAZENECA | B1 | FierceBiotech + Pharmaceutical Technology (AstraZeneca/Pathos data deal) | 2025 (deal announcement) | https://www.fiercebiotech.com/biotech/tempus-ai-line-200m-astrazeneca-pathos-deal-develop-cancer-model | ~$200M deal value; cross-checked across 2 independent trade outlets; not an SEC-primary dollar figure (flagged OPEN for exact contract terms) |
| TEM-TRADEPRESS-GSK-MERCK | B2 | IntuitionLabs pricing analysis (GSK/Merck/Gilead data deals) | 2026 | https://intuitionlabs.ai/articles/tempus-ai-rwd-deals-merck-gilead-pricing | GSK ~$70M upfront, Merck >$100M over term, Gilead "on track" $100M+; single/thin-sourced — OPEN item |
| TEM-SEARCH-LEFKOFSKY | B2 | TechCrunch + Wikipedia + governance/proxy trackers (Lefkofsky background) | various 2024-2025 | https://techcrunch.com/2024/05/30/billionaire-groupon-founder-lefkofsky-is-back-with-another-ipo-ai-healthtech-tempus/ | Founder track record (Groupon, InnerWorkings, Echo Global Logistics, Mediaocean); 30-votes/share Class B structure; ~59.9% combined voting power as of March 2025 disclosure |
| TEM-Q1-2026-EARNINGS-SUMMARY | B1 | Multiple earnings-summary aggregators (Seeking Alpha, Bitget, AllInvestView, 247WallSt) | 2026-05-05 | https://seekingalpha.com/news/4586528-tempus-ai-targets-1_59b-1_6b-revenue-and-about-65m-adjusted-ebitda-in-2026-backed-by-merck | Cross-check confirming FY2026 guidance was REITERATED (not further raised) at Q1 2026 print; cash + marketable securities $643.8M at Q1 2026; ≥3 independent aggregators agree |
| YAHOO-TEM-PRICE | B1 | Yahoo Finance (as_of_price frozen input, per runner brief) | 2026-07-02 | https://finance.yahoo.com/quote/TEM/ | Frozen input: last close ≤2026-07-04 = $60.27 (2026-07-02 session), per runner instruction; cross-checked against independent websearch (TEM-WEBSEARCH-PRICE) |
| TEM-8K-MAY2026-CONVERT | A1 | Tempus AI 8-K: $460M 0.00% Convertible Senior Notes due 2032 (priced/closed) | 2026-05-12 | https://www.sec.gov/Archives/edgar/data/0001717115/000119312526220115/d117982d8k.htm | LIVE post-Q1 event, ~7 weeks before as_of 2026-07-04. Conversion price $69.26 (vs original 2030 Notes' $84.19) — a materially closer dilution overhang given as_of_price $60.27. Net proceeds $441.9M used to retire the senior secured Credit Facilities disclosed in the Q1 2026 10-Q. Located via websearch, cross-checked TradingView + StockTitan against the SEC accession number directly |

---

## Fetch notes (2026-07-04)

- SEC EDGAR direct HTML returned HTTP 403 for the harness's default WebFetch on all 3 primary documents (10-K, 8-K exhibit, 10-Q) — consistent with known SEC user-agent blocking. Per the robustness protocol (max 2 attempts/URL, no retry-loops), immediately fell back to `curl -L -A "research contact@example.com"`, which succeeded on the first follow-up attempt (HTTP 200) for all 3 documents. No stalls; total fallback overhead was 2 extra tool calls.
- All A1 numbers are transcribed directly from the fetched primary-document text (converted to line-numbered plain text for auditability — see `raw/extracts.md` for exact line references).
- Pharma-deal dollar figures (AstraZeneca/Pathos $200M, GSK $70M, Merck/Gilead $100M+) are trade-press sourced, not SEC-primary dollar figures — flagged OPEN in facts.md (O1). Directional confirmation (Total Remaining Contract Value >$1.1B, Net Revenue Retention 126%, 70+ data-agreement customers signed in 2025) IS primary-sourced (TEM-8K-4Q25-ER).
- Price cross-checked across 2 independent sources: frozen input $60.27 (per brief) vs independent websearch $60.04 — 0.4% delta, well within normal single-day noise, and both values sit far from the 52-week band edges (not a low/high-hug per verify_freshness.py T2 tripwire).
- **CIK confirmed: 0001717115** (Tempus AI, Inc.)
- 10-K accession: **000119312526066961** (tem-20251231.htm)
- Q4/FY25 8-K exhibit accession: **000119312526066931** (tem-ex99_1.htm)
- Q1 2026 10-Q accession: **000119312526206356** (tem-20260331.htm)
