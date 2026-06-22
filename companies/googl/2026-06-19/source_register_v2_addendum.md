# GOOGL Source Register v2 Addendum

Last updated: 2026-06-16

Purpose: source register for the v2 rerun. This addendum isolates new-pipeline sources from v1-era artifacts until the final audit decides what should be promoted into the main source register.

## Source Quality Rules

| Tier | Use | Limitation |
|---|---|---|
| A1 primary filing | Reported numbers, legal terms, ownership snapshots, capital raise terms | Filing facts can still be stale after the filing date |
| A2 official company transcript | Management causal explanation and guidance language | Management claims are not independently verified operating facts |
| B market data / estimates | Price anchor and consensus expectations | Must be timestamped and not treated as business evidence |
| C secondary commentary | Topic leads and narrative checks | Never promotes to fact without primary source |

## v2 Sources

| source_id | Tier | Source | Date | URL / local path | Used for | Reliability note |
|---|---|---|---|---|---|---|
| GOOG.A1.2026Q1.10Q | A1 | Alphabet Q1 2026 Form 10-Q | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | Paid clicks, CPC, TAC, balance sheet, PPE, debt, share repurchase pause | Best source for quarterly accounting detail |
| GOOG.A1.2026Q1.991 | A1 | Alphabet Q1 2026 Exhibit 99.1 | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm | Revenue, segment income, cash flow, capex, FCF, Cloud backlog headline | Best source for Q1 earnings tables |
| GOOG.A2.CALL2026Q1 | A2 | Alphabet official Q1 2026 earnings-call transcript | 2026-04-29 | https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx | AI Search, capex allocation, Cloud backlog conversion, management ROIC framing | Management commentary; not proof of realized economics |
| GOOGL.FWP.2026.06 | A1 | Alphabet June 2026 free writing prospectus | 2026-06 | https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm | Equity raise purpose and structure | Financing context; not operating performance |
| GOOGL.424B5.2026.06 | A1 | Alphabet June 2026 424B5 prospectus supplement | 2026-06 | https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm | 2026 capex guidance, 2027 capex direction, Berkshire private placement terms | Strong for disclosed terms; capex is guidance |
| BRK.A1.13F.2026Q1 | A1 | Berkshire Hathaway Q1 2026 13F information table | 2026Q1 | https://www.sec.gov/Archives/edgar/data/1067983/000119312526226661/xslForm13F_X02/53405.xml | Berkshire Alphabet quarter-end holding | 13F snapshot; not necessarily Buffett's personal decision |
| HH.A1.13F.2026Q1 | A1 | H&H International Investment Q1 2026 13F information table | 2026Q1 | https://www.sec.gov/Archives/edgar/data/1759760/000175976026000005/xslForm13F_X02/infotable.xml | H&H Alphabet quarter-end holding | 13F snapshot; not Duan Yongping personal real-time trading |
| HH.A1.13F.2025Q4 | A1 | H&H International Investment Q4 2025 13F information table | 2025Q4 | https://www.sec.gov/Archives/edgar/data/1759760/000175976026000001/xslForm13F_X02/infotable.xml | H&H quarter-over-quarter position comparison | Snapshot delta; not exact trade ledger |
| GOOG.LOCAL.P0.SEC | Local raw | P0 SEC Extracts v2 | 2026-06-16 | companies/googl/raw/p0_sec_extracts_v2.md | Parsed tables for Search, Cloud, capex, financing | Derived from A1 sources above; must trace back to URL |
| GOOG.LOCAL.P0.CALL | Local raw | Q1 2026 call extract | 2026-06-16 | companies/googl/raw/q1_2026_call_ai_search.md | Parsed management commentary | Derived from A2 call transcript |

## Sources Not Yet Sufficient

| Source need | Why it matters | Status |
|---|---|---|
| AI Overviews / AI Mode RPM cohort data | Decides whether AI Search is accretive or dilutive | Not disclosed by Alphabet |
| Maintenance versus growth capex split | Decides normalized owner earnings | Not directly disclosed |
| Cloud backlog margin by workload type | Decides whether $460B backlog is high-quality revenue | Not disclosed |
| Numeric capex hurdle rate / payback | Decides capital allocation discipline | Management references frameworks but gives no number |
| Full 10-year normalized owner earnings sequence | Needed for Buffett-style durability test | Being rebuilt by accounting workstream |

