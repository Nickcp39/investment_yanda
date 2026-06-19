# Material Pack Lookahead Audit - AAPL 2016-05-12

Independent checker pass (different agent than the collector). As-of date: 2016-05-12.
Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

## 0. Audit Verdict

- **Verdict: CLEAN-WITH-NOTES.**
- No load-bearing post-cutoff fact is used; no decision/thesis/valuation verdict is present.
- One cosmetic note: `evidence_spine.md` §3 (the iPhone-cycle tension row) references a source id "S014" that does not exist in `sources_used.csv` (the CSV ends at S013). The underlying claim (iPhone SE demand > supply; switchers) is the same one captured as load-bearing fact C014, which is correctly cited to S006/S007 (both valid, allowed sources). So this is a dangling-reference typo in a non-load-bearing row, not a fact pulled from a missing/post-cutoff document. Recommend renumbering "S014" -> "S007" before the blind test. Not a leak.

## 1. Source Date Check

WEB-VERIFIED (independent of CSV self-report): S003 (Q2 FY16 release, 2016-04-26 — SEC EDGAR 8-K `000119312516556520`, $250B program / $50.6B rev confirmed); S011 (Icahn exit, 2016-04-28 — CNBC/Bloomberg/CNN confirmed); S008/S009 (as-of close $90.34 / sub-$90 first since 2014 confirmed by contemporaneous coverage).

| source_id | public_date | <= as_of? | web-verified | issue |
|---|---|---|---|---|
| S001 | 2015-10-28 | yes | - | none |
| S002 | 2016-01-26 | yes | - | none |
| S003 | 2016-04-26 | yes | yes (SEC URL match) | none |
| S004 | 2016-04-26 | yes | yes (same 8-K) | none |
| S005 | 2016-04-27 | yes | - | none |
| S006 | 2016-04-26 | yes | - | none |
| S007 | 2016-03-21 | yes | - | none |
| S008 | 2016-05-12 | yes (= as-of) | yes (price) | none |
| S009 | 2016-05-12 | yes (= as-of) | yes | none |
| S010 | 2016-04-26 | yes | - | none |
| S011 | 2016-04-28 | yes | yes (CNBC URL match) | none |
| S012 | 2016-04-27 | yes | - | none |
| S013 | 2016-04-27 | yes | - | none |

All 13 rows dated on or before the as-of date. 0 source-date issues. No source defined after as-of (note: the only "S014" is a typo'd cross-reference, not a source).

## 2. Claim Traceability

| key claim | source_id | traceable to allowed source? |
|---|---|---|
| First revenue decline in 13 yrs; Q2 rev $50.557B -13% | S003, S004, S010 | yes |
| First-ever YoY iPhone unit decline (51.2M, -16%) | S004, S006, S010 | yes |
| Services +20%, Other +30% only growing lines | S004, S006 | yes |
| Net cash ~$153B; $232.9B cash+securities | S005 | yes |
| Capital-return program expanded to $250B | S003 | yes |
| As-of close $90.34; ~$494.9B cap | S008, S009 | yes |
| Smartphone market shrank -3% Q1'16 | S012, S013 | yes |
| iPhone SE demand > supply / switchers (C014) | S006, S007 | yes |
| Icahn exited on China risk | S011 | yes |

Note: the §3 tension-log "S014" reference resolves to S006/S007 (see Verdict). No claim traces to an undefined or post-cutoff source.

## 3. Outcome-Aware Language Check

Grep for hindsight phrasing (later / subsequently / went on to / as we now know / rallied / collapsed / rebounded / eventually) across all files: **0 matches.** Forward-looking items are framed as as-of management guidance/targets (e.g., $250B program "by end of March 2018"), not as known outcomes. No post-as-of price appears.

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, aapl_2016-05-12 row)

| forbidden item | status | where mentioned |
|---|---|---|
| Berkshire's Apple stake (Q1'16 13F filed ~2016-05-16) | ABSENT from analysis | only in case_control forbidden list + S011/evidence_spine guardrail notes explicitly excluding it |
| AirPods (Sep 2016) | ABSENT | only in case_control forbidden list / evidence_spine self-check |
| iPhone 7 and later | ABSENT | only in forbidden list / self-check |
| Services-boom narrative on post-as-of results | ABSENT | Services framing rests on Q2 FY16 (+20%) only |
| FY2016 H2+ results | ABSENT | latest data is Q2 FY16 (ended 2016-03-26) + as-of price |
| Multi-year price appreciation | ABSENT | only the as-of close and trailing daily quotes |

All high-risk traps are absent from the evidence/analysis; mentions exist solely inside labeled forbidden-list / guardrail lines. Acceptable.

## 5. Evidence Misuse

- No KOL / social / video sources. News (S009, S010, S011) and the Icahn item are labeled "sentiment/lead, not core proof."
- Industry data (S012/S013) used as market-maturity context, not as proof Apple must decline.
- Management framing (Services annuity, India +56%, "China more stable than common view") is explicitly tagged as company optimism to be tested, not verified fact (evidence_spine §2 "Sentiment/Narrative Only").

## 6. Materials-Only Check

Grep for decision/valuation verdict tokens (decision_card / REJECT / STARTER / BUY / SELL / price target / fair value / conviction): **0 matches.** Valuation arithmetic (trailing P/E ~10x, EV/earnings ~6.7x) is explicitly labeled "neutral, NOT a judgment." All interpretation is left open for the future runner. No decision/thesis/valuation/decision_card content present.

## 7. Decision

The pack is **CLEAN-WITH-NOTES** and test-ready after the trivial "S014"->"S007" reference fix in evidence_spine.md §3. No leak; the noted item is cosmetic and non-load-bearing.

## 8. Addendum — operator_background.md added (2016-05-12 as-of)

- **`operator_background.md` added** (formation-first founder/operator dossier per `companies/_operator_underwriting_template.md`): core team = Tim Cook (CEO), Jony Ive (CDO/design soul), Jeff Williams (COO), Luca Maestri (CFO), under the Steve Jobs (d.2011) legacy. Per-person formation→adult-track→dark-arc; team-level cohesion/key-man/culture-DNA/succession; fracture inversion; team life-arc grade 4/5; scorecard 28/40 (neutral, materials only — NO decision/size).
- **Operator sources:** 14 dated/timeless operator sources (O001–O014) added in the file's own source table, reliability-tiered (unchooseable facts > third-party early-career > self-narrative); cross-referenced to in-case S003/S004/S005/S006/S011.
- **Self-audit verdict: CLEAN.** Track-record/governance rows all `public_date ≤ 2016-05-12` (Jobs resignation 2011-08-24, 2012 Maps/Forstall, 2013–14 capital-return + 7:1 split, 2014 shareholder stance, Ive CDO 2015, Williams COO 2015-12-17). Formation facts are timeless/unchooseable and legitimately cited per the formation rule. No outcome-aware language, no post-as-of price, Berkshire 13F ABSENT (Icahn used + explicitly distinguished), AirPods/iPhone 7+/Services-boom/FY2016-H2+ ABSENT. Independent checker pass still recommended (LOOKAHEAD_CHECKER requires a different agent than the collector).
