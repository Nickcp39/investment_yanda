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

---

## Independent Checker Pass (2026-06-17)

Independent agent (NOT the collector; did not assemble this pack). Ran the 6-point `LOOKAHEAD_CHECKER.md`
over the full pack (`case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`,
`operator_background.md`) + applied the `intc_2021-04-23` forbidden-registry row. Web-verified the
highest-risk / most-recent source dates rather than trusting the CSV's self-reported dates.

### Verdict: CLEAN

The pack uses only information public on or before 2021-04-23, contains no outcome-aware language, and
(material-pack requirement) carries no decision / verdict / position size. Test-ready for the blind Runner.

### 1. Source-Date Check — web-verified high-risk rows

| source_id | claimed date | web-verified | in-window (≤2021-04-23)? | note |
|---|---|---|---|---|
| S001/S002/S006 | 2021-03-23 | **2021-03-23 confirmed** (Intel newsroom / BusinessWire wire 20210323005981 / SEC 8-K accession 0001193125-21-091374) | yes | IDM 2.0 "Intel Unleashed" webcast; $20B Arizona/Ocotillo. |
| S003 | 2021-04-22 | **2021-04-22 confirmed** (Intel IR press release detail/1460; CNBC/AlphaStreet same-day) | yes | Q1'21 earnings reported after close 4/22. |
| S004 | 2021-04-23 | **2021-04-23 confirmed** (EDGAR accession 0000050863-21-000018, 10-Q for qtr ended Mar 27 2021) | yes (= as-of, allowed) | 10-Q filed on the as-of date itself. |
| S005 | 2021-04-22 | **2021-04-22 confirmed** (Motley Fool transcript URL dated 2021/04/22) | yes | Q1'21 call held 4/22. |
| S010 | 2021-03-15 | **2021-03-15 confirmed** (AMD digital launch event; ServeTheHome / Tom's Hardware / WCCFTech) | yes | 3rd Gen EPYC "Milan" 7003 launch. |
| S014 | 2021-01-13 | **2021-01-13 confirmed** (Intel IR detail/1438; BusinessWire 20210113005609); Gelsinger CEO **eff. 2021-02-15 confirmed** | yes | Appointment + effective date both verified. |
| S007–S009 | 2020-07-23/24 | consistent with the well-documented July-2020 7nm-delay disclosure | yes | Dated background, low risk. |

**Critical excluded-source check (forbidden-registry trap):** the **Mercury Research Q1 2021** x86/server
CPU-share report was web-verified to publish **~2021-05-09** (Tom's Hardware "CPU Market Q1 2021" article,
2021-05-09; corroborated by a 2021-05-08 Seeking Alpha instablog). It is **post-as-of (OUT)** and the pack
correctly EXCLUDES it — `raw_extracts.md` S010/S011 explicitly notes the Mercury figure is not used and
why. Confirmed ABSENT as a cited/load-bearing figure. ✓

### 2. Claim Traceability

Every load-bearing claim (C001–C018 in `evidence_spine.md`) traces to an in-window `source_id`. Spot-checked:
Q1 financials → S003/S004; DCG −20% / op-income $1,273M → S003/S004; FY21 $19–20B capex → S003; IDM 2.0 /
$20B Arizona / IFS-Thakur / 7nm Meteor Lake → S001/S002/S005/S006; AMD Milan + pre-as-of ~7.1% server share
→ S010/S011; as-of close $59.24 / ~$239B cap → S013/S004; operator formation/career facts → S014–S023. No
load-bearing claim relies on an unlisted or post-as-of source.

### 3. Outcome-Aware Language

Independent grep over all five files for `later|subsequently|as we (now )?know|went on to|turned out|
rallied|collapsed|plunged|surged`. Matches found are all **non-leaking**: "later" / "long-term" appear only
in (a) timeless operator-formation narrative, (b) forward-looking *as-of* framing ("multi-year investment
phase," "restore process leadership" — attributed as management commentary), and (c) prospective kill-criteria.
No hindsight phrasing tied to a post-as-of event. No post-2021-04-23 price anywhere; the only price beyond
4/23 in `raw_extracts.md` is the 2021-04-26 row, explicitly labelled part of the raw download and not used as
the as-of price.

### 4. Post-Cutoff Fact Intrusion (intc_2021-04-23 forbidden registry — each ABSENT)

| forbidden item | present? |
|---|---|
| Entire post-2021 decline / any post-4/23 price or move | absent |
| 2023 dividend cut | absent |
| Gelsinger departure (Dec 2024) + successor | absent |
| 18A / foundry-customer-win outcomes | absent |
| The fall to ~$20s | absent |
| Mercury Research Q1'21 share report (~2021-05-09) | absent (excluded + flagged) |
| Any post-2021 results (Q2'21+) / 2022+ developments / CHIPS equity | absent |

Note: incidental post-as-of facts surfaced in my own web-verification searches (e.g. the Dec-2024 Gelsinger
retirement; the "stock down 3% after-hours on 4/22" headline). These are NOT in the pack and were NOT used in
this audit or carried forward — flagged here only for transparency.

### 5. Evidence Misuse

No KOL / social / video sources. AMD peer data (S010/S011) used as dated industry context, not as company-
specific proof of an outcome — and the post-as-of Mercury figure was deliberately omitted to avoid a date
leak. Company optimistic framing ("progressing well," ">50 foundry customers," "restore process leadership")
is recorded as management commentary (S005), explicitly not as verified fact. Operator promotional/origin
narrative (S022) is weighted below the unchooseable third-party record per the dossier's own reliability axis.

### 6. No Decision / No Outcome (material-pack requirement)

No buy/sell/hold verdict, no context label, no thesis, no valuation conclusion, no position size in any file.
The decision question is recorded in `case_control.md` and left unanswered; `evidence_spine.md` lists open
questions and interpretation guardrails; `operator_background.md` gives an operator *grade* (team life-arc
3/5) but explicitly defers the decision/size. Confirmed.

### Issue count: 0 load-bearing issues.

1 noted exclusion (post-as-of Mercury Research share data) — correctly omitted and flagged by the collector,
independently re-verified by this checker. Independent verdict concurs with the collector self-audit: **CLEAN**.
Cleared to proceed to the blind Runner (Step 2 below, same agent, staying blind to outcome).
