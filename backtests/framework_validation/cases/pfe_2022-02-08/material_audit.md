# Material Pack Lookahead Audit - PFE 2022-02-08

Independent checker pass (different agent than the collector). As-of date: 2022-02-08.
Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

## 0. Audit Verdict

- **Verdict: CLEAN.**
- No load-bearing post-cutoff fact is used; no decision/thesis/valuation verdict is present.
- The known trap (FY2021 10-K filed 2022-02-24, AFTER as-of) is correctly EXCLUDED; the share count comes from the Q3 2021 10-Q (S011) instead. Checker confirms the 10-K is not used.
- Watch-item (not a leak): the "$25 billion" figure throughout the pack is management's 2030 business-development revenue AMBITION stated on the Feb 8 call, NOT the forbidden post-as-of "fall in the stock toward ~$25." The two are distinct; the stock-price $25 appears only in the case_control forbidden list.

## 1. Source Date Check

WEB-VERIFIED: S001 (Q4/FY2021 release, 2022-02-08 — SEC EDGAR 8-K `000007800322000003`; FY21 rev $81.3B, 2022 guide $98-102B, Comirnaty ~$32B / Paxlovid ~$22B all confirmed as Feb 8 disclosures); S008 (Paxlovid EUA 2021-12-22, first oral antiviral — FDA confirmed); S005/S006 (as-of reaction: guide below ~$108.6B consensus, stock down ~4%).

| source_id | public_date | <= as_of? | web-verified | issue |
|---|---|---|---|---|
| S001 | 2022-02-08 | yes (= as-of) | yes (SEC URL match) | none |
| S002 | 2022-02-08 | yes (= as-of) | yes (mirror of S001) | none |
| S003 | 2022-02-08 | yes (= as-of) | - | none |
| S004 | 2022-02-08 | yes (= as-of) | - | none |
| S005 | 2022-02-08 | yes (= as-of) | yes | none |
| S006 | 2022-02-08 | yes (= as-of) | - | none |
| S007 | 2021-11-23 | yes | - | none |
| S008 | 2021-12-22 | yes | yes (FDA EUA date) | none |
| S009 | 2021-11-05 | yes | - | none |
| S010 | 2021-12-10 | yes | - | none |
| S011 | 2021-11-12 | yes | - | none |
| S012 | 2022-02-08 | yes (= as-of) | yes (price) | none |

All 12 rows dated on or before the as-of date. 0 source-date issues. FY2021 10-K (2022-02-24) correctly NOT in the source list.

## 2. Claim Traceability

| key claim | source_id | traceable to allowed source? |
|---|---|---|
| Q4 rev $23.838B +105%; FY21 $81.288B +95% | S001, S002, S005, S006 | yes |
| FY21 adj EPS $4.42 (GAAP $3.85) | S001, S002, S005 | yes |
| 2022 guide rev $98-102B, adj EPS $6.35-6.55 | S001, S002, S005, S006 | yes |
| 2022 ~$32B Comirnaty + ~$22B Paxlovid | S001, S002, S005, S006 | yes |
| Ex-COVID FY21 grew 6% operationally | S001, S002 | yes |
| Comirnaty $36.781B = ~45% of revenue | S004 | yes |
| As-of close $51.70; ~5.613B shares -> ~$290B | S011, S012 | yes |
| ~8x forward guide; ~3.1% yield | S001, S010, S012 | yes (arithmetic) |
| Paxlovid EUA 2021-12-22; EPIC-HR 89% | S008, S009 | yes |
| Guide below ~$108.6B consensus; stock -4% | S005, S006 | yes |

All load-bearing claims trace to allowed source ids. No dangling references.

## 3. Outcome-Aware Language Check

Grep for hindsight phrasing across all files: **0 matches.** Forward items (2022 guidance, ">=$25B 2030 BD revenue," "6% non-COVID CAGR to 2025," "120M Paxlovid courses," analyst "Paxlovid seasonal from 2023") are as-of guidance/ambitions/analyst-opinion, explicitly tagged as framing. No post-as-of price appears.

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, pfe_2022-02-08 row)

| forbidden item | status | where mentioned |
|---|---|---|
| 2022-24 COVID-revenue collapse | ABSENT | only the as-of 2022 guidance; "collapse" only in case_control forbidden list |
| Seagen acquisition (2023) | ABSENT | "Seagen" appears only in case_control forbidden list + evidence_spine self-check |
| Later guidance cuts | ABSENT | only the original Feb 8 2022 guide is used |
| The fall to ~$25 (stock) | ABSENT | only as-of close $51.70 + trailing days; the stock-$25 only in forbidden list (distinct from the $25B BD ambition) |
| Post-date patent-cliff realization | ABSENT | LOE is treated as general as-of industry knowledge (open question), no realized outcome |

All high-risk traps absent from the evidence/analysis; mentions exist solely inside the case_control forbidden list / evidence_spine self-check. The pervasive "$25B" is the BD ambition (a Feb 8 management statement), not the forbidden stock price. Acceptable.

## 5. Evidence Misuse

- No KOL / social / video sources. Same-day reaction coverage (S005/S006) used for the consensus number and price reaction, labeled "narrative, not core proof."
- S007 ("$100 billion pharma goliath," SVB Leerink) is a pre-as-of analyst opinion, explicitly "media/analyst framing... not proof of durability."
- Management endemicity / BD / 6%-CAGR statements are quarantined as "company optimistic framing / leads, not verified outcomes" (raw_extracts S003 use-note; evidence_spine §2). The EPIC-HR 89% figure is correctly labeled company-reported.

## 6. Materials-Only Check

Grep for decision/valuation verdict tokens: **0 matches.** Optical multiples are "collector arithmetic... neutral, no judgment." case_control §4 and evidence_spine §6 confirm "no buy/sell verdict, no context label, no valuation conclusion." The cheap-vs-peak question is posed but left to the future runner. No decision/thesis/valuation/decision_card content present.

## 7. Decision

The pack is **CLEAN** and test-ready. The post-as-of 10-K trap is correctly handled; the "$25B" ambition is not the forbidden stock-price trap; no post-cutoff fact and no decision present.

---

## Addendum — operator_background.md added (2026-06-18)

`operator_background.md` added (Bourla / D'Amelio / Dolsten operator dossier; formation-first life-arcs, per-person dark-arcs, team fracture inversion, life-arc grade 3/5; 10 dated operator sources O01-O12). Collector self-audit verdict: **CLEAN** — all operator sources public_date ≤ 2022-02-08; the FY2021 comp (2022 proxy/10-K, post-as-of), *Moonshot* (Mar 2022) and its reviews, and the 2022 Genesis Prize *award* are deliberately EXCLUDED, with pre-as-of equivalents (FY2020 ~$21M pay per the 2021 proxy; Jan-2020 combined Chair+CEO; 2021 Oxfam/People's Vaccine profiteering data) used instead; no outcome-aware language; no decision/size/valuation. The COVID-windfall capital-allocation tension is posed and left to the future blind test.

---

## Independent Checker Pass (2026-06-19)

**Second independent agent** (not the collector, not the first checker). Scope extended to include `operator_background.md` and `material_audit.md`. As-of date 2022-02-08. Method: 6-point LOOKAHEAD_CHECKER.md checklist + the pfe_2022-02-08 forbidden-registry row, each item verified ABSENT; highest-risk dates web-verified against authoritative primaries (SEC submissions API, BusinessWire, FDA, Yahoo chart API).

### Verdict: **CLEAN** (no leak — pack is test-ready; blind run may proceed)

- 0 load-bearing post-cutoff facts. 0 decision/thesis/valuation content. The known trap (FY2021 10-K filed **2022-02-24**, 16 days after as-of) is correctly EXCLUDED; share count comes from the Q3 2021 10-Q (S011).
- The pervasive **"$25B"** is management's *2030 BD-revenue ambition* (S003), NOT the forbidden post-as-of *stock fall toward ~$25*; the two are distinct and correctly separated. Confirmed again on this pass.

### 1. Source-date check (web-verified high-risk rows)

| item | claimed date | independently verified | source of truth | result |
|---|---|---|---|---|
| **FY2021 10-K (the trap)** | filed 2022-02-24 (post-as-of → OUT) | **filingDate 2022-02-24, reportDate 2021-12-31, accession 0000078003-22-000027** | SEC submissions API (`data.sec.gov/submissions/CIK0000078003.json`) | **CONFIRMED post-as-of; correctly NOT in `sources_used.csv`** |
| S001 Q4/FY2021 release | 2022-02-08 | release dated 2022-02-08; FY2021 revenue $81.3B confirmed | BusinessWire `20220208005226`; Zacks/cbonds/citybiz mirrors | CONFIRMED = as-of |
| S008 Paxlovid EUA | 2021-12-22 | first oral antiviral EUA 2021-12-22 | FDA (re-confirmed; matches prior pass) | CONFIRMED ≤ as-of |
| S012 as-of price | $51.70 close 2022-02-08 | $51.70 close; prior day $53.21 (≈ -4% post-earnings, consistent with S006) | local Yahoo chart API CSV `asof_2022-02-08_pfe_quotes.csv` + prior web-verify | CONFIRMED ≤ as-of |
| O11 Bourla pay | FY2020 ~$21M (2021 proxy) | pre-as-of figure used; FY2021 ~$24.3M (2022 proxy/10-K) explicitly EXCLUDED | operator self-check | CONFIRMED ≤ as-of |

All 12 case sources + 12 operator sources (O01-O12) carry `public_date ≤ 2022-02-08`. 0 source-date issues. Note: SEC EDGAR HTML and several news mirrors block scripted fetch (403/timeout) — consistent with the collector's stated reason for using the BioSpace mirror (S002); figures cross-checked across independent same-day mirrors instead.

### 2. Claim traceability — all load-bearing claims (C001-C017 in evidence_spine, operator scorecard) trace to an allowed in-window `source_id` / `O-id`. No dangling references. **PASS.**

### 3. Outcome-aware language — grep for hindsight phrasing across ALL six files (incl. operator_background + this audit): **0 matches in any evidence/analysis body.** Every hit sits inside a forbidden-list, an explicit-exclusion self-check, or an ABSENT table. Forward items (2022 guidance, ≥$25B 2030 BD, 6% non-COVID CAGR to 2025, 120M Paxlovid courses, "Paxlovid seasonal from 2023") are tagged as as-of guidance / ambition / analyst-opinion. No post-as-of price appears. **PASS.**

### 4. Post-cutoff fact intrusion (forbidden registry — pfe_2022-02-08 row)

| forbidden item | status | note |
|---|---|---|
| 2022-24 COVID-revenue collapse | **ABSENT** | only the as-of 2022 guide present |
| Seagen acquisition (2023) + later M&A | **ABSENT** | appears only in forbidden list / self-checks; the as-of record carries only *prospective* BD ambition |
| Later guidance cuts/revisions | **ABSENT** | only the original Feb-8 guide used |
| Fall in the stock toward ~$25 | **ABSENT** | only as-of $51.70 + trailing days; "$25" in-pack = the BD ambition, not the price |
| Post-date patent-cliff realization | **ABSENT** | LOE treated as general as-of industry knowledge (open question), no realized outcome |
| (operator) FY2021 comp / *Moonshot* / Genesis Prize *award* | **ABSENT** | deliberately excluded; pre-as-of equivalents used |

### 5. Evidence misuse — no KOL/social/video as core proof. Same-day reaction coverage (S005/S006) labeled "narrative, not core proof." Management endemicity / BD / 6%-CAGR statements quarantined as optimistic framing; EPIC-HR 89% labeled company-reported. Operator self-narrated origin color (O10 firing-squad quote, O04 "financial returns" quote, O08 immigrant framing) explicitly down-weighted vs unchooseable facts. **PASS.**

### 6. Materials-only — 0 decision/valuation-verdict tokens in the evidence/analysis. Optical multiples flagged "collector arithmetic… neutral, no judgment." Operator grade is an explicit "neutral collector estimate, not a decision." The cheap-vs-peak question is posed, deferred to the blind run. **PASS.**

**Decision:** pack is **CLEAN** and test-ready; no load-bearing post-as-of fact; no decision present. Blind Step-2 run authorized.
