# Material Audit (self-applied LOOKAHEAD_CHECKER) - META 2022-11-10

> Self-audit by the collector. An independent checker pass is still recommended
> (the framework requires checker independence). This is the collector's own
> 6-point self-application.

## 0. Audit Verdict

- Verdict: CLEAN-WITH-NOTES.
- As-of date: 2022-11-10.
- Files audited: case_control.md, sources_used.csv, raw_extracts.md, evidence_spine.md.
- Notes are non-load-bearing (source-precision and one unsourced valuation component), itemized below. No post-cutoff fact and no decision are present.

## 1. Source-Date Check

Every sources_used.csv row has public_date <= 2022-11-10. Highest-risk / most-recent rows web-checked:

| source_id | public_date | allowed? | issue |
|---|---|---|---|
| S001 | 2022-10-26 | yes | none (Q3'22 release) |
| S002 | 2022-10-27 | yes | none (10-Q filed 2022-10-27; SEC index confirms) |
| S003 | 2022-11-09 | yes | none (8-K Exhibit 99.1, dated Nov 9 2022; verified on SEC EDGAR) |
| S004 | 2022-10-26 | yes | none (Q3'22 call same day as release) |
| S005 | 2022-11-10 | yes | none (as-of price; the date IS the as-of date) |
| S006 | 2022-10-27 | yes | none (reaction-day article) |
| S007 | 2022-10-27 | yes | none (analyst round-up; actions dated ~Oct 27) |
| S008 | 2022-10-20 | yes | none (Snap Q3 print) |
| S009 | 2022-10-25 | yes | none (Alphabet Q3 print) |
| S010 | 2022-11-09 | yes | none (layoff-day news) |
| S011 | 2022-11-10 | yes | none (as-of-day macro context) |

No source dated after 2022-11-10.

## 2. Claim Traceability

| claim | source_id | traceable? |
|---|---|---|
| Q3'22 revenue -4% YoY; ad revenue; impressions +17% / price-per-ad -18% | S001 / S002 | yes |
| FoA op income $9,336M; RL loss $(3,672)M; RL revenue $285M | S001 / S002 | yes |
| Costs +19%; op income $5,664M; margin 20% vs 36%; net income $4,395M; EPS $1.64 | S001 / S002 | yes |
| DAP 2.93B / MAP 3.71B / FB DAU 1.98B / MAU 2.96B | S001 | yes |
| 2022 & 2023 capex + total-expense guidance | S001 | yes |
| Buybacks $6.55B Q3 / $17.78B authorized; 9-mo $21,093M | S001 / S002 | yes |
| Cash+securities $41.78B; LT debt $9,922M; equity $124,094M | S001 / S002 | yes |
| Nov 9 ~13% / 11,000+ layoff; hiring freeze; cost discipline | S003 / S010 | yes |
| As-of close $111.00; market cap ~$294.3B; net cash ~$31.9B; EV ~$262.5B | S005 / S002 | yes |
| Oct 27 -24% to $97.94; Q4 guide $30-32.5B | S006 | yes |
| Analyst PT cuts (MS $205->$105, etc.) | S007 | yes |
| Peer ad slowdown (Snap +6%, Alphabet +6% / $13.91B NI) | S008 / S009 | yes |
| Transcript: 2023 expenses flat / RL losses to grow (paraphrase) | S004 | yes (paraphrase — see Note A) |

All load-bearing claims trace to an allowed source_id.

## 3. Outcome-Aware Language Check

- No hindsight phrasing ("later", "subsequently", "as we now know", "went on to", "turned out", "rallied/collapsed to") used as fact.
- No post-as-of price appears. The only forward-leaning lines are management's own dated statements (S003) and are explicitly labeled "management framing," not fact.
- The as-of close ($111.00) is above the Oct 27 trough ($97.94); this is explained by the dated, on-or-before-as-of Nov 9 layoff news and Nov 10 CPI rally (S011), not by any future knowledge.

## 4. Post-Cutoff Fact Intrusion (per-case forbidden registry for META)

Each item checked ABSENT:

| forbidden item (post 2022-11-10) | present? |
|---|---|
| Q4 2022 results / FY2022 10-K | ABSENT |
| 2023 "Year of Efficiency" announcement/framing | ABSENT |
| Second (March 2023) ~10,000-job layoff round | ABSENT |
| Later capex/expense revisions, later buybacks, 2024 dividend initiation | ABSENT |
| Any META price after 2022-11-10 / the 2023+ recovery | ABSENT |
| Later analyst upgrades / later DAU-ad metrics | ABSENT |
| Any "turned out / as we now know" outcome framing | ABSENT |

(Note: the registry in LOOKAHEAD_CHECKER.md does not yet include a META row; this audit applies the analogous META-specific traps. Recommend extending the registry — see section 7.)

## 5. Evidence Misuse Check

- No KOL / social / video sources used. All sources are filings, official releases, market data, or reputable dated news/peer earnings.
- Company optimistic framing (S003 "deeply underestimated," "most profitable ever built"; S004 paraphrase) is recorded as framing, NOT stated as verified fact.
- Peer data (S008, S009) is used as industry context, not as Meta-specific proof.
- Analyst PT cuts (S007) are used as sentiment, not core proof.

## 6. No Decision / No Outcome (material-pack gate)

- No buy/sell/hold verdict, no context label, no thesis, no position size, no buy-below, no decision_card present in any file.
- The decision question is recorded in case_control.md and explicitly deferred.
- Valuation figures (P/E, EV, FCF, market cap) are presented as neutral arithmetic data inputs, NOT as a valuation judgment or recommendation.

## 7. Notes (non-load-bearing; safe to proceed)

- Note A (source precision): S004 (earnings-call transcript) was retrieved as paraphrase, not verbatim quotes. Its claims (2023 expenses roughly flat; RL losses to grow) are cross-consistent with S001 guidance and S003, and are graded medium confidence. They are not load-bearing for any required fact. A future pass could re-extract verbatim from the official transcript PDF if higher precision is needed.
- Note B (valuation component): the trailing-P/E arithmetic uses an FY2021 diluted-EPS figure ($13.77) that is NOT independently cited in sources_used.csv. The trailing P/E (~10.6x) is therefore labeled "approximate" in raw_extracts.md and flagged as open question #5 in evidence_spine.md. The market cap, net cash, and EV do NOT depend on this and are fully sourced (price S005 x shares S002).
- Note C (registry): LOOKAHEAD_CHECKER.md should be extended with a META 2022-11-10 row (forbid anything after 2022-11-10; traps as in section 4).

## 8. Decision

The material pack is CLEAN-WITH-NOTES and is recommended as test-ready after the two minor notes (A, B) are acknowledged. An independent checker pass remains advisable per framework policy.

## 9. Addendum — operator_background.md added (2022-11-10 as-of)

- 2022-11-10: Added `operator_background.md` (founder/operator dossier per `_operator_underwriting_template.md`) plus operator sources **S012–S019** in `sources_used.csv`. Self-audit verdict: **CLEAN-WITH-NOTES** — every operator source has public_date <= 2022-11-10 (proxy 2022-04-22 [S012], Sandberg departure 2022-06-01 [S016], CFO transition announce 2022-07-27 / effective 2022-11-01 [S015], FTC order 2019-07-24 [S017], Haugen testimony 2021-10-05 [S018], biographies S013/S014/S019 2022-10); no post-as-of events, no outcome-aware language, no decision/size; 8 dedicated operator sources (>= the 3–6 minimum); governance/control-risk dimension covered from the primary 2022 DEF 14A (Zuckerberg 56.9% voting power, "controlled company"). One open note: Susan Li's pre-Harvard formation facts are not reliably documented in dated sources <= as-of and are logged as a gap rather than guessed.

---

## Independent Checker Pass (2026-06-19)

> Performed by an INDEPENDENT checker (not the collector). Scope: all six material-pack files
> (case_control.md, sources_used.csv, raw_extracts.md, evidence_spine.md, operator_background.md,
> material_audit.md) against the 6-point LOOKAHEAD_CHECKER.md checklist + the `meta_2022-11-10`
> forbidden-registry row (now present in LOOKAHEAD_CHECKER.md, line 37). High-risk dates web-verified.

### Verdict: **CLEAN** (test-ready)

No load-bearing post-cutoff fact, no outcome-aware language, no decision/thesis/size present. The
collector's two prior notes (A: transcript paraphrase; B: unsourced FY2021 EPS component used only for an
explicitly-"approximate" trailing P/E) are confirmed **non-load-bearing** — neither alters the as-of
integrity of the pack — so this independent pass grades **CLEAN** (the collector's self-grade was the more
conservative CLEAN-WITH-NOTES; both are "safe to proceed").

### 1. Source-date check — all rows public_date <= 2022-11-10 (high-risk rows web-verified)

| source_id | claimed date | independent verification | allowed? |
|---|---|---|---|
| S001 Q3'22 release | 2022-10-26 | Web-confirmed: Meta reported Q3'22 on **2022-10-26**, revenue ~$27.7B, EPS $1.64 (matches pack). | yes |
| S003 Nov 9 layoff (8-K Ex.99.1) | 2022-11-09 | Web-confirmed: Zuckerberg "13% / >11,000" message dated **2022-11-09**; severance "16 weeks + 2/yr, no cap" + 6-mo healthcare matches S003 verbatim. | yes |
| S005 as-of close | 2022-11-10 | Web-confirmed via StatMuse: META close **$111.00** on 2022-11-10 (date IS the as-of date). | yes |
| S002 10-Q | 2022-10-27 | Filed on/before as-of (collector verified on EDGAR; date 1 day after Q3 release, plausible). | yes |
| S004 Q3 call | 2022-10-26 | Same day as release. | yes |
| S006 reaction | 2022-10-27 | Reaction-day article. | yes |
| S007 analyst PT round-up | 2022-10-27 | Dated ~Oct 27. | yes |
| S008 Snap Q3 | 2022-10-20 | Snap Q3 print. | yes |
| S009 Alphabet Q3 | 2022-10-25 | Alphabet Q3 print. | yes |
| S010 layoff news | 2022-11-09 | Layoff-day news. | yes |
| S011 CPI day | 2022-11-10 | As-of-day macro context. | yes |
| S012 DEF 14A | 2022-04-22 | 2022 proxy. | yes |
| S013 Sandberg bio | 2022-10-15 | Formation facts (timeless), dated cite. | yes |
| S014 Bosworth bio | 2022-10-20 | Formation facts (timeless), dated cite. | yes |
| S015 CFO transition | 2022-07-27 | Wehner→CSO / Li→CFO eff. 2022-11-01 (effective date IS on-or-before as-of; pre-announced = known). | yes |
| S016 Sandberg departure | 2022-06-01 | Announced 2022-06-01, official 2022-08-01. | yes |
| S017 FTC $5B order | 2019-07-24 | Dark-arc anchor. | yes |
| S018 Haugen testimony | 2021-10-05 | Dark-arc anchor. | yes |
| S019 Zuckerberg bio | 2022-10-15 | Formation facts (timeless), dated cite. | yes |

No source dated after 2022-11-10. **Note on web search:** general web results surfaced post-as-of events
(2023 layoff round, recovery) — these were used ONLY to confirm the forbidden traps exist in reality and
must stay excluded; NONE were imported into the pack or this audit.

### 2. Claim traceability — every load-bearing claim traces to an allowed source_id

Re-checked evidence_spine.md claims C001–C019 and operator_background People-Map / Scorecard claims: all
trace to S001–S019. The two anchor financials (Q3 print, Nov 9 layoff) and the $111.00 price/market-cap
chain (S005 × S002 share count) are fully sourced. PASS.

### 3. Outcome-aware language check — ABSENT

No "later / subsequently / as we now know / went on to / turned out / rallied / recovered" used as fact.
The only forward-leaning lines are Zuckerberg's own dated statements (S003, e.g. "deeply underestimated,"
"more efficient cost structure than we outlined to investors recently") and the S004 transcript paraphrase,
each explicitly labeled **management framing**, not verified fact. The as-of $111.00 sitting above the
Oct 27 $97.94 trough is explained by the dated Nov 9 layoff + Nov 10 CPI rally (S011) — not hindsight.

### 4. Post-cutoff fact intrusion — `meta_2022-11-10` forbidden registry row, each ABSENT

| forbidden item (per LOOKAHEAD_CHECKER.md row, after 2022-11-10) | present in pack? |
|---|---|
| 2023 "Year of Efficiency" (Feb 2023) framing/announcement | ABSENT |
| Recovery to $300 → $400+ | ABSENT |
| FY2022 full-year results (reported Feb 2023) | ABSENT |
| 2023+ results | ABSENT |
| Later Reality Labs losses (post-as-of quarters) | ABSENT |
| The later AI-capex pivot | ABSENT |
| Second (March 2023) ~10,000-job layoff round | ABSENT |
| 2024 dividend initiation / later buybacks / later DAU-ad metrics | ABSENT |
| Any post-2022-11-10 META price | ABSENT |

The registry now contains the `meta_2022-11-10` row (collector's prior Note C is resolved — the row exists
in LOOKAHEAD_CHECKER.md). PASS.

### 5. Evidence misuse check — PASS

No KOL / social / video sources. All sources are SEC filings, official releases, market data, reputable
dated news, peer earnings, or biography-tier (used only for timeless formation facts, never EVIDENCE-tier
hard claims). Management optimism (S003/S004) recorded as framing. Peer data (S008/S009) used as industry
context, not Meta-specific proof. Analyst PTs (S007) used as sentiment.

### 6. No decision / no outcome (material-pack gate) — PASS

No buy/sell/hold verdict, no context label, no thesis, no position size, no buy-below, no decision_card in
any of the six files. The decision question is recorded in case_control.md and explicitly deferred. All
valuation figures (P/E ~10.6x [marked approximate], EV ~$262.5B, ~$31.9B net cash, FCF proxy) are presented
as neutral arithmetic inputs.

### Checker decision

**CLEAN — no LEAK. The blind Runner (Step 2) may proceed on this pack.**
