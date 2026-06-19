# Material Audit (self-applied Lookahead Checker) - AMZN 2023-02-03

Pack type: MATERIAL PACK (evidence only). Self-applied by the collector. An
independent checker pass is still recommended per LOOKAHEAD_CHECKER.md (the
independence is the point); this is the collector's honest self-audit.

## 0. Audit Verdict

- Verdict: **CLEAN-WITH-NOTES**
- One-line: Materials only, no decision/thesis/size present; all load-bearing facts trace to sources public <= 2023-02-03; one cited row (S013) has a public_date after the as-of date but is fenced to a non-load-bearing narrative-direction use only.
- As-of date: 2023-02-03
- Files audited: case_control.md, sources_used.csv, raw_extracts.md, evidence_spine.md

## 1. Source Date Check

| source_id | public_date | <= as-of? | issue |
|---|---|---|---|
| S001 | 2023-02-02 | yes | none (earnings release, after-close 2023-02-02) |
| S002 | 2023-02-02 | yes | none (same release - income statement table) |
| S003 | 2023-02-02 | yes | none (same release - segment table) |
| S004 | 2023-02-02 | yes | none (same release - balance sheet / cash flow) |
| S005 | 2023-02-02 | yes | none (same release - supplemental metrics) |
| S006 | 2023-02-03 | yes | none (FY2022 10-K filed on the as-of date itself; verified on EDGAR: CIK 0001018724, accession 0001018724-23-000004) |
| S007 | 2023-02-02 | yes | none (Q4'22 earnings call held 2023-02-02) |
| S008 | 2023-02-03 | yes | none (as-of close; series ends 2023-02-06 in source but only <=2023-02-03 data is used as as-of; the 2023-02-06 row appears in the raw series for completeness and is NOT used as an as-of fact) |
| S009 | 2023-01-04 | yes | none |
| S010 | 2023-01-05 | yes | none |
| S011 | 2023-02-02 | yes | none |
| S012 | 2023-02-02 | yes | none |
| S013 | 2023-02-09 | **NO** | **FLAGGED.** Public_date is 6 days after the as-of date. Mitigation: S013 is used only as a narrative lead for the *direction* of the post-print stock reaction (rally halted), which is independently confirmed by the verified Feb 3 close in S008. No price, market-cap, YTD, or any other quantitative fact from S013 is used. The article's quoted price ($244.65) and market cap ($2.6T) are explicitly excluded as a later-period, non-comparable level. Recommend a future independent checker either (a) accept the fenced narrative-only use or (b) drop S013 entirely; the pack does not depend on it. |
| S014 | 2023-01-24 | yes | none |
| S015 | 2023-02-02 | yes | none |

Highest-risk row web-verified: S008 (price). As-of close 2023-02-03 = $103.39 confirmed on two independent Yahoo Finance hosts (query1 and query2), internally consistent with surrounding sessions (prior close 2023-02-02 = $112.91). VERIFIED.

## 2. Claim Traceability

| claim group | claim_ids | source_id(s) | traceable? |
|---|---|---|---|
| Q4/FY revenue & growth | C001, C002 | S001, S002, S012 | yes |
| AWS revenue, deceleration, margin | C003-C006, C018, C019 | S001, S003, S005, S007, S011 | yes |
| Segment operating losses (NA / Intl) | C007, C008, C009 | S001, S002, S003 | yes |
| Q4 charges composition | C010 | S001, S007 | yes |
| Net loss & Rivian | C011, C012 | S001, S002, S007 | yes |
| Cash flow / capex / FCF | C013, C014 | S001, S004, S005 | yes |
| Headcount reductions | C015 | S005, S009, S010 | yes |
| Q1'23 guidance | C016 | S001 | yes |
| As-of price & market cap | C017 | S008 (+ shares from S004) | yes |
| Balance sheet | C021 | S004 | yes |
| Peer cloud context | C022 | S014, S015 | yes |

All load-bearing claims trace to a source public <= 2023-02-03. No load-bearing claim depends on S013.

## 3. Outcome-Aware Language Check

- Scanned case_control.md, raw_extracts.md, evidence_spine.md for hindsight phrasing ("later", "subsequently", "as we now know", "went on to", "rebounded/collapsed to") and post-as-of prices.
- Result: none found in load-bearing text. Where the post-split context is mentioned, it is framed defensively (an explicit instruction NOT to use later non-comparable prices), not as an outcome.
- No price after 2023-02-03 is asserted as fact. The S008 raw series lists a 2023-02-06 row for completeness but it is explicitly marked as not used as an as-of fact.

## 4. Post-Cutoff Fact Intrusion (AMZN forbidden registry)

AMZN is not in the original LOOKAHEAD_CHECKER per-case registry table; applying the standard
forbidden-trap discipline for this as-of date. Each item checked ABSENT:

| forbidden item | absent? |
|---|---|
| Q1 2023 (and later) Amazon results / FY2023 10-K | absent |
| The additional ~9,000 role reductions announced March 2023 | absent |
| Any AMZN price after 2023-02-03 / the 2023 recovery / later split-adjusted levels | absent (S013's later price explicitly excluded) |
| Later AWS re-acceleration or generative-AI narrative | absent |
| Later capex cuts, later operating-margin recovery, later Rivian marks | absent |
| Any 2023-H2 / 2024+ development | absent |

## 5. Evidence Misuse Check

- No social / KOL / video source used; no source used as core proof beyond its tier.
- Peer filings (S014 MSFT, S015 GOOGL) used as industry/cloud-cycle context, not as proof of any AMZN-specific outcome.
- Management's optimistic framing (S001 CEO quote, S007 "long-term trends still there") is recorded explicitly as management view, not as verified fact (noted in raw_extracts and evidence_spine).
- S013 fenced to narrative-direction lead only (see row in section 1).

## 6. No Decision / No Outcome (material-pack gate)

- The pack contains NO buy/sell/hold verdict, NO decision_card, NO thesis_mechanism, NO valuation target, and NO position size.
- The decision question is recorded in case_control.md section 3 and explicitly marked DEFERRED / not answered.
- evidence_spine.md section 2 includes a boundary note stating the trough-vs-structural question is "NOT resolved here."
- Extracts are neutral. PASS.

## 7. Decision

The material pack is **CLEAN-WITH-NOTES** and is material-collection-complete. The single
note is S013's post-as-of public_date, mitigated by fencing it to a non-load-bearing use
and excluding its quantitative figures. Recommended action for the independent checker:
accept the fenced use or drop S013; the pack's integrity does not depend on it. No LEAK.

---

## 8. Addendum — operator_background.md added (2023-02-03 as-of)

`operator_background.md` (founder/operator dossier per `companies/_operator_underwriting_template.md`)
was added to this case on the as-of frame. It underwrites the people line — Jeff Bezos (founder /
Executive Chairman), Andy Jassy (CEO since 2021-07-05, AWS-builder), Brian Olsavsky (CFO since 2015) —
formation-first per person, compressed adult track ≤ as-of, required dark-arc per person, team-level
cohesion/key-man/culture/succession, fracture inversion, and a team life-arc grade (4/5). It uses 8
operator sources (O1–O8 + O5-comp) plus financial facts already in the pack (S001/S003/S004/S007/S009);
it adds NO decision, thesis, or size.

Self-applied Lookahead Checker on operator_background.md:
- **Source-date check:** all operator sources have public_date <= 2023-02-03 (formation facts are
  timeless/encyclopedic; the 1997 + 2020 shareholder letters and the 2021 succession coverage are
  pre-as-of). The Jassy father-anecdote (O5) is self-narrated at a 2022 event and is explicitly
  fenced to lowest-tier self-narrative.
- **Outcome-aware language:** none. The one "later" occurrence is in a forward-looking *kill-criteria*
  clause ("to test on later evidence — NOT evaluated here"), not hindsight about a known outcome.
- **Post-cutoff intrusion:** ABSENT. Explicitly excluded as leaks and recorded in the dossier's source
  appendix: any 2024+ "do the Leadership Principles survive Jassy" commentary, Bloomberg's 2026
  Jassy/AI profile, the 2026 re-reporting of the father anecdote and its quoted multi-trillion market
  cap, Jacklyn Gise's 2025 death, Olsavsky's 2024 CMU-board / 2025 CFO-of-the-Year, and any post-2022
  revenue figure (e.g. the $638B 2024 number some bios carry).
- **Evidence misuse:** Wikipedia used as a cited cross-check of primary facts (formation), not as core
  proof of an outcome; management/self-narrative framing flagged as such; no KOL/social/video used as
  proof.
- **No decision / no outcome:** the dossier contains NO buy/sell/hold, NO size, NO valuation; the
  open people-tension (does a founder-authored culture transmit to the first non-founder CEO) is
  recorded as an open question, not resolved.

**Addendum verdict: CLEAN-WITH-NOTES** — the only note is O5's self-narrated father anecdote, fenced
to lowest-tier framing and not load-bearing. No LEAK. (An independent checker pass remains recommended
per LOOKAHEAD_CHECKER.md — the independence is the point.)

---

## Independent Checker Pass (2026-06-19)

Performed by an **independent checker** (NOT the collector) per `LOOKAHEAD_CHECKER.md`. Inputs: this
case's six material files + the framework docs. The 6-point checklist and the `amzn_2023-02-03`
per-case forbidden-registry row were run from scratch; the two highest-risk dates (as-of price; the
FY2022 10-K filing date) were re-verified against independent public sources.

### Verdict: **CLEAN-WITH-NOTES** — material-pack-complete, no LEAK.

One-line: independent re-run reproduces the collector's verdict. All load-bearing facts trace to
sources public ≤ 2023-02-03; the only note is S013 (public_date 2023-02-09), fenced to a
non-load-bearing narrative-direction use with its quantitative figures excluded. Pack does not depend
on it. No decision/thesis/size present. Safe to proceed to the blind run.

### 1. Source-date check (independent)

| source_id | claimed public_date | ≤ as-of? | independent check |
|---|---|---|---|
| S001–S005 | 2023-02-02 | yes | Q4'22 earnings release issued after-close 2023-02-02 — confirmed (CNBC/IR coverage same date). |
| S006 (FY2022 10-K) | 2023-02-03 | yes | **Web-verified on SEC EDGAR submissions API:** accession `0001018724-23-000004`, **filingDate 2023-02-03**, reportDate 2022-12-31, acceptanceDateTime 2023-02-02T18:27:34Z. Filed on the as-of date itself (after-hours submission 2023-02-02 → EDGAR stamps next-business-day filing date 2023-02-03). Within bounds either reading. Accession matches the pack exactly. |
| S007 | 2023-02-02 | yes | Q4'22 call held 2023-02-02 — confirmed. |
| S008 (price) | 2023-02-03 | yes | **Web-verified independently (StatMuse):** AMZN close 2023-02-03 = **$103.39** (−1.8% on the day). Matches the pack's Yahoo-sourced figure exactly. Independent confirmation on a non-Yahoo source. |
| S009 / S010 | 2023-01-04 / 2023-01-05 | yes | ~18,000-role-reduction announcement dated early Jan 2023 — established, well before as-of. |
| S011 / S012 | 2023-02-02 | yes | Print-day coverage. |
| S013 | **2023-02-09** | **NO** | **FLAGGED (concur with collector).** 6 days after as-of. Used only as a narrative-direction lead ("rally halted"), independently corroborated by the verified Feb-3 close decline (S008). Its quoted $244.65 price and $2.6T market cap are explicitly excluded as a later, non-comparable (also pre-/post-split-confused) level. Independent recommendation: **accept the fenced narrative-only use** — pack integrity does not depend on S013. |
| S014 / S015 | 2023-01-24 / 2023-02-02 | yes | MSFT Q2 FY23 (2023-01-24) and Alphabet/Google Cloud Q4'22 (2023-02-02) — peer/cloud-cycle context, both ≤ as-of. |
| O1–O8, O5-comp | ≤ 2022 / formation-timeless | yes | Operator sources: shareholder letters (1997/2020), 2015 & 2021 succession coverage, encyclopedic formation facts. O5 (2022 father anecdote) fenced as lowest-tier self-narrative. None post-as-of. |

Highest-risk rows independently web-verified: **S008 price ($103.39 ✓ via StatMuse)** and **S006 10-K filingDate (2023-02-03 ✓ via SEC EDGAR, accession matches)**. Both confirm the pack.

### 2. Claim traceability (independent)

Spot-checked the load-bearing claim groups (C001–C022) against `sources_used.csv`. Every load-bearing
claim traces to a source public ≤ 2023-02-03 (revenue/AWS/segment/charges/Rivian/cash-flow/headcount/
guidance/price/balance-sheet/peer). **No load-bearing claim depends on S013.** Traceable: PASS.

### 3. Outcome-aware language (independent regex sweep)

Independently grepped all six files for hindsight markers (`later|subsequently|as we (now )?know|went on
to|rebounded|rallied|recover(y)?|re-?accel|surge|collapsed to|eventually|ended up`) and post-as-of
price/date tokens (`180|244|$15x–$24x|march 2023|q1'23 result|fy2023|2024|2025|2026|9,000`).

- Every hit lands in **defensive exclusion text** (case_control §5 forbidden list; this audit's forbidden
  registry; operator_background's explicit "EXCLUDED as post-as-of" block) or in **forward-looking
  kill-criteria** ("to test on later evidence — NOT evaluated here").
- No hit asserts a known post-as-of outcome in load-bearing text. The "$1.9–2.3B / 12,000 / Q1 2023"
  tokens are **Alphabet/MSFT peer charges** (S014/S015, ≤ as-of), not AMZN outcomes. The "$120s
  guidance" is the forward Q1'23 guidance *range issued 2023-02-02* (allowed — what management said, not a
  realized result). The "$638B / 2026 Bloomberg profile / 2024-2025 events" tokens appear **only inside
  exclusion lists** confirming absence.
- No post-2023-02-03 price asserted as fact. Outcome-aware language: **NONE in load-bearing text.** PASS.

### 4. Post-cutoff fact intrusion — `amzn_2023-02-03` forbidden registry row (each ABSENT)

| forbidden item (registry row) | absent? | check |
|---|---|---|
| The 2023 recovery to $180+ | **absent** | No post-2023-02-03 price in any load-bearing text; S013's $244.65 explicitly excluded. |
| AWS re-acceleration | **absent** | Only the *deceleration* path (37%→33%→28%→20% ex-FX; "mid-teens" into Jan) is recorded; no later re-accel/gen-AI narrative. |
| The March-2023 additional ~9,000 layoffs | **absent** | Appears only in the case_control/audit exclusion lists; not used as a fact. |
| Q1'23 results (late Apr 2023) | **absent** | Only the *forward Q1'23 guidance* (issued 2023-02-02) is present; no actual Q1'23 result. |
| FY2023+ results | **absent** | No FY2023 10-K or later filing referenced as fact. |
| The Rivian-mark recovery | **absent** | Only the FY22 −$12.7B / Q4 −$2.3B Rivian valuation *loss* is recorded; no later mark recovery. |

### 5. Evidence misuse (independent)

- No KOL/social/video source used as core proof. Peer filings (S014 MSFT, S015 GOOGL) used as
  industry/cloud-cycle context only, not as proof of any AMZN-specific outcome.
- Management's optimistic framing (S001 CEO quote; S007 "long-term trends still there") is explicitly
  recorded as *management view*, not verified fact — confirmed in raw_extracts and evidence_spine.
- Wikipedia (O1/O3/O6) used as a cited cross-check of *formation* facts, not as outcome proof; O5
  father-anecdote fenced as lowest-tier self-narrative. S013 fenced to narrative-direction only. PASS.

### 6. No decision / no outcome (material-pack gate)

- No `decision_card`, no buy/sell/hold verdict, no thesis_mechanism, no valuation target, no position
  size anywhere in the six files. The decision question is recorded in case_control §3 and explicitly
  marked **DEFERRED**; evidence_spine §2 carries the boundary note that the trough-vs-structural question
  is "NOT resolved here"; operator_background ends with open questions, not a verdict. PASS.

### Independent Decision

The pack is **CLEAN-WITH-NOTES** and material-collection-complete. The single note (S013 post-as-of
public_date) is mitigated by fencing to a non-load-bearing use and excluding its figures; pack integrity
does not depend on it. The two highest-risk facts were re-verified on independent sources and both match
the pack. **No LEAK on any load-bearing fact.** Cleared to proceed to the blind 6-module run.
