# QA Material Audit (self-applied Lookahead Checker) - NVDA 2023-05-25

Self-applied per `LOOKAHEAD_CHECKER.md`. This is a material pack (evidence only); the gate also requires NO decision / NO outcome present. An independent checker pass is still recommended (the collector auditing itself is a first pass, not the final independent gate).

## 0. Audit Verdict

- Verdict: CLEAN-WITH-NOTES.
- As-of date: 2023-05-25.
- Reason for "with notes" (all non-load-bearing, already handled in-pack):
  1. The Q1 FY2024 10-Q was filed 2023-05-26 (one day AFTER as-of) and is therefore EXCLUDED; the same quarterly numbers are sourced from the 2023-05-24 earnings 8-K (S001/S002/S003), which is allowed. Documented in `case_control.md` §5.
  2. The price was locked from a split-adjusted series and un-adjusted x10 to the PRE-split basis (10:1 split occurred 2024-06-07, after as-of). This un-adjustment uses only a knowable split ratio; the split is NOT used as a post-as-of narrative event. Documented in `case_control.md` §2 and S007.
  3. Two consensus figures (Q1 ~$6.52B; Q2 ~$7.2B) and the ~160% YTD figure are news-reported (S008/S011/S014), graded medium, and used as dated context only.
- Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.
- Decision files: NONE present (correct for a material pack).

## 1. Source Date Check

| source_id | public_date | allowed? | issue |
|---|---|---|---|
| S001 | 2023-05-24 | yes | none (8-K EX-99.1; <= as-of) |
| S002 | 2023-05-24 | yes | none (8-K EX-99.2; <= as-of) |
| S003 | 2023-05-24 | yes | none (8-K cover; <= as-of) |
| S004 | 2023-02-24 | yes | none (FY2023 10-K) |
| S005 | 2023-02-22 | yes | none (FY2023 results release) |
| S006 | 2023-05-24 | yes | none (Q1 FY24 call, held 2023-05-24) |
| S007 | 2023-05-25 | yes | as-of close itself; series un-adjusted to pre-split |
| S008 | 2023-05-24 | yes | none (CNBC after-hours) |
| S009 | 2023-05-25 | yes | none (CNBC record close, as-of day) |
| S010 | 2023-05-24 | yes | none (Reuters/Investing.com) |
| S011 | 2023-05-25 | yes | none (CNN, as-of day) |
| S012 | 2023-05-25 | yes | none (Washington Post, as-of day) |
| S013 | 2023-01-05 | yes | none (AMD MI300 CES 2023, pre-as-of) |
| S014 | 2023-05-25 | yes | none (dated YTD chart context) |

Highest-risk rows web-checked: the 10-Q (confirmed filed 2023-05-26 via SEC submissions index -> correctly EXCLUDED, not in CSV); the earnings 8-K (confirmed filed 2023-05-24); the price (locked from series + corroborated by 2023-05-25 dated news). No source in the CSV post-dates the as-of.

## 2. Claim Traceability

| claim | source_id | traceable? |
|---|---|---|
| Q1 FY24 revenue / Data Center / Gaming | S001, S002 | yes |
| GAAP & non-GAAP margin and EPS | S001, S002 | yes |
| Q2 FY24 $11B revenue guide + margin guide | S001, S002 | yes |
| Generative-AI demand attribution + supply for 2H | S002, S006 | yes |
| FY2023 full-year baseline (Data Center ramp, R&D, EPS) | S004, S005 | yes |
| Shares outstanding 2.47B (pre-split) | S004 | yes |
| Balance sheet / supply obligations | S001, S002 | yes |
| As-of close $379.80 pre-split + ~$0.94T cap | S007 | yes |
| Single-day surge magnitude / consensus beats | S008, S009, S011 | yes (news, graded medium) |
| AMD MI300 competitive disclosure | S013 | yes |

All load-bearing facts trace to an allowed source_id.

## 3. Outcome-Aware Language Check

- Scanned `case_control.md`, `raw_extracts.md`, `evidence_spine.md` for "later / subsequently / as we now know / went on to / rallied to / turned out / became." No such hindsight phrasing present.
- No post-as-of price appears. The only later EVENT referenced is the June-2024 10:1 split, and only as the mechanical reason the price series is un-adjusted (a stated convention), not as a development that "happened next." This is non-load-bearing and disclosed.
- No FY2024 H2+, no Q2 FY24 actuals, no later market-cap milestone, no later AMD MI300X launch specifics.

## 4. Post-Cutoff Fact Intrusion (derived NVDA forbidden registry)

The `LOOKAHEAD_CHECKER.md` registry does not yet have an NVDA row; the following were derived from this case's anchor and each verified ABSENT:

| trap to exclude | present? |
|---|---|
| Any NVDA price after 2023-05-25 | ABSENT |
| Q1 FY2024 10-Q (filed 2023-05-26, +1 day) used as a source | ABSENT (explicitly excluded) |
| Q2 FY2024 (or later) results / guidance / filings | ABSENT |
| The 10:1 split framed as a later event/outcome | ABSENT (used only as price-series un-adjust convention) |
| Later AI / data-center revenue milestones | ABSENT |
| Later market-cap milestones ($1T crossing, multi-trillion) | ABSENT (only the as-of "approaching ~$1T" framing, dated 2023-05-25) |
| AMD MI300X launch detail (Dec 2023) / later CoWoS expansions | ABSENT (only CES-2023 pre-as-of disclosure used) |
| Any "became a winner" framing | ABSENT |

## 5. Evidence Misuse Check

- No social / KOL / video source used; news is dated narrative/corroboration, not core proof.
- Management's optimistic framing (generative-AI surge, supply/visibility, trillion-dollar TAM) is explicitly labeled as management commentary in S006/C007/C008, NOT stated as verified fact.
- Consensus and YTD figures from news are graded medium and flagged as news-reported, not primary.
- AMD MI300 is recorded neutrally as a disclosed competitive product, with no claim about competitive outcome.

## 6. Decision / Outcome Presence Check (material-pack gate)

- NO buy/sell/hold verdict anywhere.
- NO `decision_card.md` / `.json`, NO thesis file, NO position size, NO buy-below price.
- The decision question is recorded in `case_control.md` §3 explicitly marked "DO NOT ANSWER THIS ROUND."
- Valuation appears only as neutral arithmetic (market cap, trailing P/E from primary EPS), not as a judgment.

## 7. Decision

The material pack is CLEAN-WITH-NOTES and is test-ready. The notes (10-Q +1-day exclusion, pre-split un-adjust convention, news-graded consensus) are documented and non-load-bearing. Recommend an INDEPENDENT checker pass before the future blind Runner locks any decision, and recommend adding an NVDA row to the `LOOKAHEAD_CHECKER.md` per-case forbidden registry using §4 above.
