# BSX Filing Calendar (via SEC data.sec.gov submissions API — CIK 0000885725)

Fetched: 2026-07-05. SEC EDGAR direct HTML document fetch returned HTTP 403 on both attempted URLs (cgi-bin/browse-edgar company search AND direct .htm 10-K/10-Q document); per robustness rule (max 2 attempts/URL, no retry-loop), immediately pivoted to: (a) the SEC's own `data.sec.gov/submissions/CIK{10-digit}.json` API, which DID succeed (200) and gave the authoritative filing calendar/accession numbers below, and (b) stocktitan.net structured filing mirrors + official company press releases + search-corroborated trade press for financial line-item extraction.

Company: **BOSTON SCIENTIFIC CORP** | CIK: **0000885725** | Ticker: BSX (NYSE) | SIC 3841 (Surgical & Medical Instruments & Apparatus) | FYE: Dec-31

## Relevant recent filings (form, filing date, accession, primary doc, items)

| Form | Filed | Accession | Primary Doc | Items | Relevance |
|---|---|---|---|---|---|
| 10-K | 2026-02-17 | 0000885725-26-000010 | bsx-20251231.htm | — | FY2025 annual report |
| 8-K | 2026-02-04 | 0000885725-26-000006 | q42025earningsrelease.htm | 2.02, 9.01 | Q4/FY2025 earnings — Event 1 gap-down trigger (facts.md E7) |
| 8-K | 2026-02-05 | 0000885725-26-000008 | — | 5.02 | Officer/director change |
| 8-K | 2026-02-23 | 0000885725-26-000013 | bsx-20260218.htm | 5.02, 7.01, 8.01, 9.01 | — |
| 8-K | 2026-02-26 | 0000885725-26-000017 | bsx-20260226.htm | 1.01, 1.02, 2.03, 9.01 | Credit facility / debt (likely Penumbra-financing-related) |
| DEF 14A | 2026-03-18 | 0000885725-26-000025 | bsx-20260318.htm | — | Proxy statement (CEO comp, board, insider ownership) |
| 8-K | 2026-03-30 | 0000885725-26-000029 | bsx-20260328.htm | 8.01, 9.01 | Conference-call announcement (Q1 2026 call scheduling) — coincides with a price gap but is NOT itself the earnings event |
| 8-K | 2026-04-22 | 0000885725-26-000031 | bsx-20260422.htm | 2.02, 9.01 | Q1 2026 earnings — Event 2 (first guidance cut, facts.md E7) |
| 10-Q | 2026-05-01 | 0000885725-26-000033 | bsx-20260331.htm | — | Q1 2026 quarterly report |
| 8-K | 2026-05-05 | 0000885725-26-000036 | bsx-20260430.htm | 5.03, 5.07, 9.01 | Annual meeting results / bylaw amendment |
| 8-K | 2026-05-18 | 0000885725-26-000041 | bsx-20260518.htm | 8.01, 9.01 | $2B accelerated share repurchase agreement |
| 8-K | 2026-05-18 | 0000885725-26-000042 | bsx-20260518.htm | 8.01, 9.01 | MiRus LLC strategic investment |
| — | 2026-05-27 | (Bernstein conf. presentation — not a standalone 8-K earnings release found) | — | — | Event 3 — SECOND guidance cut (facts.md E7), stock -10.3% to -12.5% |
| 8-K | 2026-01-15 | 0000947871-26-000037 | ss5822815_8k.htm | 1.01, 9.01 | Penumbra merger agreement announcement ($14.5B EV) |

## Price-gap-to-filing reconciliation

- **2026-02-04 gap (-17.6%)**: matches 8-K 2.02 filed same day — Q4/FY2025 earnings + initial (later-cut-twice) FY2026 guidance. CONFIRMED.
- **2026-03-30 gap (-9.0%, from Mar 27 close)**: the only same-week filing is the 8-K dated 2026-03-30 (items 8.01/9.01, "conference call announcement" per stocktitan news feed headline "Boston Scientific announces conference call discussing first quarter 2026 results" + an FDA clearance news item same day) — this is NOT an earnings/guidance event itself. Most likely explanation (not fully confirmed this run): broader medtech-sector or macro move, OR anticipatory positioning ahead of the pending Q1 earnings date, OR a reaction to the CHAMPION-AF WATCHMAN FLX study data released 2026-03-28 (2 days prior) — the study met all endpoints (positive), so this would NOT explain a decline; alternatively could be profit-taking/de-risking ahead of the securities class-action lead-plaintiff deadline (2026-05-04) news cycle heating up, or a sector-wide de-rating. FLAGGED AS UNRESOLVED — see facts.md O-series; does not change the overall three-event narrative materially since the largest, most decisive gaps (Feb 4, May 27) are fully confirmed.
- **2026-05-27 gap (-10.3% to -12.5%)**: matches the Bernstein 42nd Annual Strategic Decisions Conference presentation (no standalone 8-K found under this CIK for that exact date, consistent with conference remarks not always triggering a same-day 8-K unless material new guidance is issued in writing — the guidance cut was communicated verbally/via presentation per multiple corroborating news sources). CONFIRMED via ≥3 independent secondary sources (Motley Fool, Tradingpedia, Stocktwits, CoinCentral).
