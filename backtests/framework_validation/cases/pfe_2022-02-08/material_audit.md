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
