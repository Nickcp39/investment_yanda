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

---

## 8. Addendum — operator_background.md (added 2026-06-18)

`operator_background.md` (founder/operator dossier; people line, no decision) ADDED. Self-audit verdict: **CLEAN-WITH-NOTES**.
- New operator-source namespace OPxx (OP01–OP14); every OPxx `public_date ≤ 2023-05-25`. Primary governance from the DEF 14A filed **2023-05-08** (board roster, 13 dir / 12 independent, independent Lead Director Stephen Neal, Huang ~3.77% beneficial ownership, one-share-one-vote / no dual class). FY2023 10-K (2023-02-24, = S004) reused for talent/risk facts.
- Formation facts (births, family, Oneida Baptist Institute, Denny's, OSU/Stanford, UF/Santa Clara/RPI, HP/Sun/AMD/LSI/TI/Microsoft/Cisco) are timeless and each cited to biography/institutional tier (explicitly character-pattern tier, NOT EVIDENCE-tier).
- Anti-narrative rule satisfied: every person (Huang, Kress, Malachowsky, Priem) carries a required dark-arc. Team life-arc grade 4/5.
- **Sources affirmatively EXCLUDED for post-dating as-of** (verified, kept out): Globes "Trillion dollar woman" Kress profile (2023-07-23); Forbes/Tom's Hardware Priem "$70B / off-grid" profile (2023-11); 2024+ "60 direct reports / no 1-on-1s" interview quotes (flat-org used only as a pre-as-of structural LEAD, OP14); Melissa Lora board appointment (2023-07-24); Mark Stevens becoming board chair (2024); all post-as-of accolades ("world's best CEO").
- Outcome-aware language scan: no "later / went on to / as we now know"; no post-as-of price/market-cap; crucible events referenced are all ≤1997. NO decision / thesis / size present (correct for material pack).
- Notes (non-load-bearing): Kress family/childhood formation is a documented public GAP (left empty, not invented); pre-as-of capital-allocation track record is under-documented here and flagged as a GAP for the financial modules; birth-city minor source variance for Huang (Tainan/Taipei) noted in-file.
- Recommend the same INDEPENDENT checker pass cover this file's OPxx date-integrity.

---

## Independent Checker Pass (2026-06-19)

Run by an INDEPENDENT checker (not the collector) per `LOOKAHEAD_CHECKER.md`. Scope: the full material pack (`case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`, `operator_background.md`) + the `nvda_2023-05-25` forbidden-registry row. As-of: **2023-05-25**. Highest-risk source dates were web-verified independently (not trusting the CSV's self-reported dates).

### IC.0 Verdict

- **Verdict: CLEAN-WITH-NOTES.**
- No post-cutoff data on any load-bearing fact; no outcome-aware language; no decision / thesis / size present (correct for a material pack). The pack is test-ready for the blind Runner.
- The collector's own CLEAN-WITH-NOTES verdict is **confirmed**; the three notes are all non-load-bearing and already handled in-pack. One additional minor note added (IC.5, S007 intraday range not independently reproduced — non-load-bearing).

### IC.1 Independent web-verification of highest-risk source dates

| item | claimed in pack | independently verified | result |
|---|---|---|---|
| Q1 FY2024 10-Q (the +1-day trap) | filed 2023-05-26, EXCLUDED (not in CSV) | EDGAR accession **0001045810-23-000093**, period 2023-04-30, **filing date 2023-05-26** (confirmed via search; accession `...093` is numerically AFTER the 8-K's `...087`, independently proving it was filed later) | CONFIRMED EXCLUDED — correct |
| Q1 FY2024 earnings 8-K (S001/S002/S003) | filed 2023-05-24 (after close) | EDGAR accession **0001045810-23-000087**, cover `nvda-20230524.htm`, exhibits `q1fy24pr.htm` + `q1fy24cfocommentary.htm`, all Q1 FY2024 | CONFIRMED ≤ as-of — allowed |
| As-of price / move (S007, S008, S009) | pre-split $379.80; ~+24% single-day to record close; ~$0.94T | CNBC 2023-05-25 corroborates ~24% rally to all-time-high close, after-hours ~30% jump, market value "on track" near ~$975B / approaching $1T; consensus refs ($6.52B Q1 rev, $0.92 adj EPS, $11B Q2 guide) corroborated | CONFIRMED — price + magnitude consistent with locked figure |
| Prior record high context (S014-adjacent) | record close (implies prior peak) | prior record high Nov 2021 (~$333 close) per dated news — consistent, no contradiction with as-of | CONFIRMED — no leak |
| FY2023 10-K (S004) / FY2023 release (S005) | 2023-02-24 / 2023-02-22 | routine prior-year filings, dates well-established; no risk | accepted — allowed |
| Operator DEF 14A (OP01) | filed 2023-05-08 | proxy filed weeks before as-of; governance facts (13 dir/12 indep, Lead Director, ~3.77% Huang, one-share-one-vote) are as-of-appropriate | accepted — allowed |

Note on method: SEC `browse-edgar`, `data.sec.gov/submissions`, and direct `Archives/.../*.htm` all returned HTTP 403 to the fetch service this pass; dates were instead confirmed via EDGAR document URLs surfaced in search (which embed the accession + period-of-report slug) plus dated third-party news. The accession-number ordering (8-K `...087` < 10-Q `...093`) is itself dispositive that the 10-Q post-dates the 8-K, independent of any reported calendar date.

### IC.2 Source-date check (all rows)

Every row in `sources_used.csv` (S001–S014) carries `public_date ≤ 2023-05-25`; re-verified the collector's table — **no source post-dates the as-of**. The one source dated exactly on as-of and most exposed (S007 price lock, S009/S011/S012 same-day news) are all 2023-05-25 and permitted. The operator namespace OP01–OP14 all carry `public_date ≤ 2023-05-25` (the four affirmatively-excluded post-as-of operator sources — Globes 2023-07-23, Forbes/Tom's 2023-11, 2024 flat-org quotes, Lora 2023-07-24, Stevens-chair 2024 — are kept OUT and only referenced as exclusions). PASS.

### IC.3 Claim traceability

All load-bearing facts (C001–C020) trace to allowed source_ids; spot-checked the anchor figures (Q1 rev $7.192B → S001/S002; Data Center $4.284B → S001/S002; Q2 $11B guide → S001/S002; GAAP/non-GAAP EPS $0.82/$1.09 → S001; shares 2.47B → S004; price/cap → S007). News-reported consensus (C018) and ~160% YTD (C020) are correctly graded **medium** and flagged news-reported, not primary. PASS.

### IC.4 Outcome-aware language

Independent scan of all five files for "later / subsequently / as we now know / went on to / rallied to / turned out / became / eventually." **None present** as hindsight phrasing. The only post-as-of EVENT named is the June-2024 10:1 split, used solely as the stated mechanical reason the split-adjusted series is un-adjusted ×10 to the pre-split basis — a disclosed convention, not a "what happened next" development, and non-load-bearing (the pre-split price is corroborated by same-day 2023-05-25 news independent of any split knowledge). Operator crucible events are all ≤1997. PASS.

### IC.5 Post-cutoff fact intrusion — `nvda_2023-05-25` forbidden registry (each ABSENT)

| registry trap | present? |
|---|---|
| Any NVDA price after 2023-05-25 | ABSENT |
| The 10:1 split (Jun 2024) framed as an event/outcome | ABSENT (used only as price-series un-adjust convention; pre-split convention enforced) |
| The run to $1T → $3T (any later market-cap milestone) | ABSENT (only the dated 2023-05-25 "approaching ~$1T" framing) |
| FY2024 / FY2025 results, Q2 FY24+ guidance/filings | ABSENT |
| Blackwell (or any post-Hopper roadmap beyond as-of) | ABSENT (only H100/Grace/Grace Hopper/Ada — all ≤ as-of) |
| Any post-print rally beyond 2023-05-25 | ABSENT |
| Q1 FY24 10-Q filed 2023-05-26 (+1 day) used as a source | ABSENT (explicitly excluded; IC.1 re-confirmed the +1-day date) |
| Later AMD MI300X launch specifics (Dec 2023) / later CoWoS-HBM expansions | ABSENT (only CES-2023 MI300 pre-as-of disclosure, S013) |
| Any "became a winner" / outcome framing | ABSENT |

Additional minor note (non-load-bearing): the S007 intraday pre-split range (~$366.30 low / ~$394.80 high / ~$385.20 open) was not independently reproduced this pass; the as-of CLOSE ($379.80 pre-split) and the move magnitude ARE corroborated by dated news, so this does not affect any load-bearing fact.

### IC.6 Evidence misuse

No social/KOL/video source used. News (S008–S012, S014) is dated narrative/corroboration, not core proof. Management's optimistic framing (generative-AI surge, "procured substantially higher supply for 2H," "visibility out a few quarters," trillion-dollar installed-base TAM) is explicitly labeled management commentary in S006/C007/C008 (C008 graded medium), NOT stated as verified fact. AMD MI300 recorded neutrally with no competitive-outcome claim. Operator formation facts correctly tiered as character-pattern (NOT EVIDENCE-tier), each cited. PASS.

### IC.7 Decision / outcome presence (material-pack gate)

NO buy/sell/hold verdict; NO `decision_card.md` / `.json` present at audit time; NO thesis, position size, or buy-below price. The decision question in `case_control.md` §3 is explicitly marked "DO NOT ANSWER THIS ROUND." Valuation appears only as neutral arithmetic (~$0.94T cap; trailing GAAP P/E ~198x; non-GAAP ~124x from primary EPS) with the forward P/E recorded as a GAP, not estimated. PASS.

### IC.8 Decision

**CLEAN-WITH-NOTES — test-ready.** The pack is free of load-bearing lookahead; the +1-day 10-Q trap is correctly and verifiably excluded; price and magnitude are corroborated by dated same-day news without using any split-era knowledge; operator dossier date-integrity holds. Notes (10-Q +1-day exclusion, pre-split un-adjust convention, news-graded consensus, un-reproduced S007 intraday range) are all non-load-bearing. The independent checker authorizes the blind Runner to proceed (Step 2).
