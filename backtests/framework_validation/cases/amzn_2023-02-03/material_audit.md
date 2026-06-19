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
