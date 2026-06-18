# Material Pack Lookahead Audit - PYPL 2021-07-29

Independent checker pass (different agent than the collector). As-of date: 2021-07-29.
Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

## 0. Audit Verdict

- **Verdict: CLEAN.**
- No load-bearing post-cutoff fact is used; no decision/thesis/valuation verdict is present.
- High-risk timing trap checked: the Block (Square)-Afterpay acquisition was announced **2021-08-01**, three days AFTER the as-of date (web-verified). It is correctly listed as forbidden and is ABSENT from the runner files. "Afterpay" appears only as a generic BNPL competitor name in the dated landscape source (S009, 2021-07-28) and in the case_control forbidden line about the acquisition — the deal itself is not used.

## 1. Source Date Check

WEB-VERIFIED: S001 (Q2 2021 release, 2021-07-28 — SEC EDGAR 8-K `000163391721000146`; rev $6.24B, TPV $311B +40%, -8% after-hours, eBay drag all confirmed); S004/S005 (consensus $1.12 EPS / $6.27B rev, ~8% drop, as-of close $283.17 gap-down from $301.98); Block-Afterpay announce date 2021-08-01 (post-as-of — confirmed forbidden and absent).

| source_id | public_date | <= as_of? | web-verified | issue |
|---|---|---|---|---|
| S001 | 2021-07-28 | yes | yes (SEC URL match) | none |
| S002 | 2021-07-28 | yes | - | none |
| S003 | 2021-07-28 | yes | - | none |
| S004 | 2021-07-28 | yes | yes | none |
| S005 | 2021-07-29 | yes (= as-of) | yes (price) | none |
| S006 | 2021-04-20 | yes | - | none |
| S007 | 2021-02-11 | yes | - | none |
| S008 | 2021-05-06 | yes | - | none |
| S009 | 2021-07-28 | yes | - | none |

All 9 rows dated on or before the as-of date. 0 source-date issues. (Note on S003: some transcript hosts timestamp the call publication 2021-07-29; the call itself was held 2021-07-28 — still on/before as-of. evidence_spine §4 already flags this.)

## 2. Claim Traceability

| key claim | source_id | traceable to allowed source? |
|---|---|---|
| Q2'21 rev $6.24B +19%; TPV $311B +40% | S001, S002 | yes |
| 403M active accounts; NNAs 11.4M (down from 21.3M) | S001 | yes |
| GAAP EPS $1.00 (-23%); non-GAAP $1.15 (+8%) | S001, S002 | yes |
| eBay 4% of TPV (from 9%), volume -37% | S001 | yes |
| eBay drag ~7pt FY (~$0.85 EPS); ~8.5pt Q3; ~100% done by Q3 | S003 | yes |
| Ex-eBay rev ~+32%, volume ~+48% | S003 | yes (mgmt, medium) |
| Venmo ~$58B TPV +58%; revenue ~+70% | S001, S003 | yes |
| FY21 guide rev ~$25.75B, non-GAAP EPS ~$4.70 | S001 | yes |
| As-of close $283.17; ~$332.7B on 1,175M shares | S005, S002 | yes |
| Feb 2021 ID targets (750M accts, >$50B rev by 2025) | S007 | yes (as stated target) |
| Square Q1'21 GP $964M (+79%); Cash App +171% | S008 | yes (peer context) |

All load-bearing claims trace to allowed source ids. No dangling references.

## 3. Outcome-Aware Language Check

Grep for hindsight phrasing across all files: **0 matches.** Forward items (FY21/Q3 guidance, Feb 2021 investor-day 2025 targets) are as-of guidance/targets, explicitly tagged "company targets/aspirations, not realized results." The deceleration is framed from as-of data (NNA drop, Q3 guide), not from knowledge of a later de-rate. No post-as-of price appears.

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, pypl_2021-07-29 row)

| forbidden item | status | where mentioned |
|---|---|---|
| Pinterest acquisition rumor (Oct 2021) | ABSENT | only in case_control forbidden list |
| 2022 guidance cuts / user-growth deceleration | ABSENT | only as-of FY21/Q3'21 guidance; later cuts only in forbidden list |
| The stock collapse / de-rate | ABSENT | only as-of close + as-of-era path; "de-rated" only in case_control forbidden list |
| Alex Chriss CEO (Sep 2023) | ABSENT | Schulman is the CURRENT (as-of) CEO; "Chriss" only in forbidden list |
| The 2026 ~$43 price | ABSENT | not mentioned anywhere |
| Block-Afterpay deal (announced 2021-08-01, post-as-of) | ABSENT | only "Afterpay" as a generic competitor (S009, dated 2021-07-28) + the forbidden-list line about the acquisition |
| Amazon-Venmo checkout (Nov 8 2021) | ABSENT | only in case_control forbidden list |

All high-risk traps absent from the evidence/analysis; mentions exist solely inside the case_control forbidden list, or (for Afterpay) as a legitimately-dated competitor name. Acceptable.

## 5. Evidence Misuse

- No KOL / social / video sources. CNBC (S004) used for the consensus comparison and immediate reaction.
- Peer Square data (S008) and the BNPL landscape (S009) are explicitly "context, not core proof" / "peer context."
- Management framing ("essential service," "best performance in our history," ex-eBay ~32% growth, 2025 super-app targets) is quarantined as "framing/aspiration, not verified outcomes" (raw_extracts S003 use-note; evidence_spine §2 "Sentiment/Narrative Only"). The ex-eBay growth claim is assigned medium confidence as a management figure.

## 6. Materials-Only Check

Grep for decision/valuation verdict tokens (decision_card / REJECT / STARTER / BUY / SELL / price target / fair value / conviction): **0 matches.** The REJECT/WATCH/STARTER/CORE wording exists only inside the case_control "Decision Question" describing the FUTURE blind-test output ("NOT produced this round"), not as an actual verdict. evidence_spine is labeled "Materials-only... does NOT contain a buy/sell verdict, thesis, valuation conclusion, or position size"; M1 signal explicitly 0. No decision/thesis/valuation/decision_card content present.

## 7. Decision

The pack is **CLEAN** and test-ready. The Block-Afterpay timing trap (post-as-of by 3 days) is correctly excluded; no post-cutoff fact, no leadership-change leak, no decision present.
