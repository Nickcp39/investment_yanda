# Material Audit (Self-Applied Lookahead Checker) - INTC 2021-04-23

Self-applied LOOKAHEAD_CHECKER.md, 6-point checklist + INTC forbidden registry. This is a material pack
(evidence only); the gate additionally requires NO decision/outcome present.

## 0. Audit Verdict

- Verdict: CLEAN.
- As-of date: 2021-04-23.
- Pack type: material pack (collector round). No decision files exist in this folder by design.
- Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.
- Note: an independent checker pass (different agent) is still recommended per the protocol; this is the
  collector's self-audit.

## 1. Source Date Check (every source public_date <= 2021-04-23)

| source_id | public_date | allowed? | note |
|---|---|---|---|
| S001 | 2021-03-23 | yes | IDM 2.0 release; web-confirmed date. |
| S002 | 2021-03-23 | yes | 8-K filed 2021-03-23 (EDGAR accession 0001193125-21-091374). |
| S003 | 2021-04-22 | yes | Q1'21 earnings release / 8-K ex-99.1. |
| S004 | 2021-04-23 | yes | 10-Q filed 2021-04-23 (EDGAR accession 0000050863-21-000018) = as-of date, allowed. |
| S005 | 2021-04-22 | yes | Q1'21 call held 2021-04-22; transcript. |
| S006 | 2021-03-23 | yes | BusinessWire wire copy of IDM 2.0. |
| S007 | 2020-07-23 | yes | 7nm-delay coverage. |
| S008 | 2020-07-24 | yes | 7nm-delay coverage. |
| S009 | 2020-07-23 | yes | 7nm-delay coverage. |
| S010 | 2021-03-15 | yes | AMD Milan launch coverage. |
| S011 | 2020-03-06 | yes | Pre-as-of AMD server-share context. |
| S012 | 2021-04-23 | yes | Trade-press Q1'21 framing = as-of date, allowed. |
| S013 | 2021-04-23 | yes | Price series; as-of close locked from this series. |

High-risk rows web-checked: S004/S012/S013 (the as-of-dated rows) and the most recent strategy rows
(S001/S003/S005). The Mercury Research Q1 2021 share report was web-verified to publish ~2021-05-09 and
was therefore EXCLUDED, not cited.

## 2. Claim Traceability

| claim | source_id | traceable? |
|---|---|---|
| Q1'21 revenue / EPS / gross margin | S003, S004 | yes |
| DCG revenue -20% and op income $1,273M | S003, S004 | yes |
| DCG / CCG segment drivers (digestion, ASP/mix) | S004, S005 | yes |
| Notebook record volume + 23% ASP decline | S003, S004 | yes |
| FY2021 guidance incl. $19-20B capex | S003 | yes |
| Dividend paid / buyback / dividend-growth commitment | S003, S004, S005 | yes |
| Balance sheet, shares outstanding | S004 | yes |
| IDM 2.0 three pillars, $20B Arizona, IFS, 7nm Meteor Lake | S001, S002, S005, S006 | yes |
| July 2020 7nm delay context | S007, S008, S009 | yes |
| AMD Milan launch + pre-as-of server share | S010, S011 | yes |
| As-of close $59.24 and ~$239B market cap | S013, S004 | yes |

No load-bearing claim relies on an unlisted or post-as-of source.

## 3. Outcome-Aware Language Check

- Scanned all four files for hindsight phrasing: "later", "subsequently", "as we now know", "went on to",
  "turned out", "rallied/collapsed to". None present.
- No post-2021-04-23 price appears. Only the 2021-04-19 -> 2021-04-26 window is used, and only the
  2021-04-23 close is treated as the as-of price. The single 2021-04-26 row in the price table is part of
  the raw downloaded series for transparency and is explicitly labeled; it is not used as the as-of price
  and carries no outcome interpretation.
- Forward-looking statements are confined to the company's own as-of guidance/commentary (FY2021 guide,
  IDM 2.0 plans) and are attributed as such.

## 4. Post-Cutoff Fact Intrusion (INTC forbidden registry for this case)

Per the strict-blind contrast constraint, each must be ABSENT — verified absent:

| forbidden item | present? |
|---|---|
| Any Intel result/filing/guidance after 2021-04-23 (Q2'21+) | absent |
| Any INTC price/move after 2021-04-23 | absent |
| Mercury Research Q1 2021 CPU-share report (~2021-05-09) | absent (deliberately excluded; noted) |
| Any 18A / later-node ramp, foundry customer wins post-as-of | absent |
| Any CHIPS Act / US-government equity, later dividend action | absent |
| Any knowledge of later Intel/Gelsinger/IFS developments | absent |
| Any 2021-H2 / 2022+ development | absent |

## 5. Evidence Misuse

- No KOL / social / video sources used.
- Peer/competition data (AMD) is used as industry context, not as company-specific proof of an outcome;
  the post-as-of Mercury Research figure was excluded specifically to avoid a date leak.
- Company optimistic framing ("progressing well", "restore process leadership", ">50 foundry customers")
  is recorded as management commentary in S005, explicitly not as verified fact.
- Trade-press framing (S012) is labeled context-only.

## 6. No Decision / No Outcome (material-pack requirement)

- No buy/sell/hold verdict, no context label, no thesis, no valuation conclusion, no position size in any file.
- The decision question is recorded in `case_control.md` and left unanswered.
- `evidence_spine.md` lists open questions and explicit interpretation guardrails rather than conclusions.

## 7. Decision

The INTC 2021-04-23 material pack is CLEAN and is test-ready for a future blind Runner pass.

### Issue count: 0 load-bearing issues. (1 noted exclusion: post-as-of Mercury Research share data correctly omitted.)

## 8. Addendum — operator_background.md added (2021-04-23 as-of)

- `operator_background.md` (founder/operator dossier per `companies/_operator_underwriting_template.md`) was
  ADDED to this pack. It underwrites the people line (Gelsinger CEO, Davis CFO, Ishrak Chair; Swan as outgoing
  context), formation-first with a required dark-arc per person, team-level + fracture inversion, and a team
  life-arc grade of 3/5. Operator-specific sources S014–S023 (9 added; 6 dated ≤ as-of, 3 timeless-formation
  profiles) extend `sources_used.csv`; S001/S004/S005/S007–S009 reused.
- Self-audit (LOOKAHEAD_CHECKER, 6-point + INTC forbidden registry) re-run over the new file: every operator
  source is public_date ≤ 2021-04-23 (or a timeless formation fact, cited); the central read is that Gelsinger
  had been CEO only ~10 weeks, so he is underwritten on his PRIOR record (Intel 1979–2009, EMC, VMware) with
  near-zero Intel-CEO results — that thinness is stated as the finding, not hidden. Grep scan found NO
  hindsight phrasing tied to post-as-of events, NO post-2021-04-23 year/price, NO 18A / foundry-customer-win /
  CHIPS-equity / Gelsinger-departure intrusion, and NO buy/sell/hold verdict or position size. ("later" appears
  only in timeless formation narrative; "exit" only for pre-as-of CEO departures and a forward kill-criterion.)
- **Self-audit verdict for operator_background.md: CLEAN** (0 load-bearing issues). Pack remains test-ready;
  an independent checker pass is still recommended per protocol.
