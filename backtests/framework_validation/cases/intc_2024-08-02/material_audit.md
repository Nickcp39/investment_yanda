# Material Pack Lookahead Audit - INTC 2024-08-02

Independent checker pass (different agent than the collector). As-of date: 2024-08-02.
Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

## 0. Audit Verdict

- **Verdict: CLEAN.**
- No load-bearing post-cutoff fact is used; no decision/thesis/valuation verdict is present.
- The pack contains substantial forward-looking content (Q3 2024 guidance, 2025 opex targets, 2026 reductions, 2027 foundry break-even, 18A products "to launch in 2025"). These are all statements MADE in the Aug 1 2024 release / call (forward guidance and management targets knowable as-of), not realized post-cutoff outcomes — correctly admissible.

## 1. Source Date Check

WEB-VERIFIED: S001 (Q2 2024 release, 2024-08-01 — SEC EDGAR 8-K `000005086324000122`; revenue $12.8B, $(0.38) GAAP EPS, dividend suspension Q4'24, >15% headcount cut all confirmed as Aug 1 disclosures); S007/S008 (as-of close $21.48 on 2024-08-02, -26% / "worst day in ~50 years" confirmed by CNBC); S011 (AMD Q2 2024 reported 2024-07-30, record data-center + >$1B MI300X confirmed).

| source_id | public_date | <= as_of? | web-verified | issue |
|---|---|---|---|---|
| S001 | 2024-08-01 | yes | yes (SEC URL match) | none |
| S002 | 2024-08-01 | yes | - | none |
| S003 | 2024-01-26 | yes | - | none |
| S004 | 2024-04-02 | yes | - | none |
| S005 | 2024-04-25 | yes | - | none |
| S006 | 2024-08-01 | yes | - | none |
| S007 | 2024-08-02 | yes (= as-of) | yes (price) | none |
| S008 | 2024-08-02 | yes (= as-of) | yes (CNBC URL match) | none |
| S009 | 2024-08-01 | yes | - | none |
| S010 | 2024-08-01 | yes | - | none |
| S011 | 2024-07-30 | yes | yes | none |
| S012 | 2024-04-03 | yes | - | none |

All 12 rows dated on or before the as-of date. 0 source-date issues.

## 2. Claim Traceability

| key claim | source_id | traceable to allowed source? |
|---|---|---|
| Q2'24 rev $12,833M -1% YoY; GAAP EPS $(0.38) | S001, S006 | yes |
| >15% headcount cut; >$10B cost plan | S001, S002, S009, S010 | yes |
| Dividend suspension starting Q4 2024 | S001 | yes |
| Q3'24 guide $12.5-13.5B, GAAP EPS $(0.24) | S001 | yes |
| Foundry Q2 op loss $(2,830)M; FY23 loss $7.0B; break-even ~2027 | S001, S004, S012 | yes |
| H1 OCF $1,069M vs $11,652M gross capex | S001 | yes |
| As-of close $21.48, -26%, ~$91.9B equity | S007 | yes |
| 18A milestones (1.0 PDK Jul 2024; products 2025) | S001, S002 | yes (as management claim) |
| AMD record data-center / >$1B MI300X | S011 | yes (context) |

All load-bearing claims trace to allowed source ids. No dangling references.

## 3. Outcome-Aware Language Check

Grep for hindsight phrasing across all files: **0 matches.** Management forward statements (18A "regain process leadership," Gaudi 3 "2x perf/$ vs H100," 2027 break-even) are explicitly tagged as "management framing / claim, not verified outcome" (raw_extracts S002 use-note; evidence_spine §2). No post-as-of price appears.

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, intc_2024-08-02 row)

| forbidden item | status | where mentioned |
|---|---|---|
| Post-crash price recovery / "later surge" | ABSENT | only the as-of close + trailing daily closes; recovery mentioned only in case_control forbidden list |
| Gelsinger departure (Dec 2024) + new CEO | ABSENT | Gelsinger appears only as the CURRENT (as-of) CEO quoted in the Aug 1 release; no departure/successor anywhere |
| 18A ramp outcome / foundry customer wins | ABSENT | only as-of milestones/targets; "is the 18A ramp credible" is an open question, not an outcome |
| US-government / CHIPS-Act equity stake | ABSENT | not mentioned anywhere |
| Any 2024-H2 / 2025 / 2026 development (realized) | ABSENT | 2025/2026 references are forward guidance/targets stated Aug 1, not realized results |

All high-risk traps absent from the evidence/analysis. The 2025/2026/2027 figures are as-of forward guidance (admissible), not post-cutoff outcomes. Acceptable.

## 5. Evidence Misuse

- No KOL / social / video sources. News (S008/S009/S010) labeled "market-reaction and narrative context only (not core proof)"; magnitude independently corroborated by S007 price data.
- Peer/competitive items (S011) explicitly "context, not core proof of any verdict."
- Management optimistic forward statements clearly quarantined as framing, not fact (evidence_spine §2 "Sentiment/Narrative Only," §3 "treat timeline as management claim").

## 6. Materials-Only Check

Grep for decision/valuation verdict tokens: **0 matches.** evidence_spine §2 states explicitly "framing only — NOT a decision," §5 "No decision, sizing, or valuation has been recorded." The turnaround-vs-structural-decline tension is assembled but not adjudicated. No decision/thesis/valuation/decision_card content present.

## 7. Decision

The pack is **CLEAN** and test-ready. Forward guidance is correctly admitted as as-of knowable; no post-cutoff fact, no leadership-change leak, no decision present.

---

## 8. Addendum — `operator_background.md` added (2026-06-18)

- **Added:** `operator_background.md` (founder/operator dossier — Gelsinger / Zinsner / Yeary / Holthaus + board), with 9 new operator sources **O01–O09** appended to `sources_used.csv`. All O01–O09 are public_date ≤ 2024-08-02 (oldest O09 book 2008; newest dated event used = Jan 2023 chair appointment). Materials only — no decision, no valuation, no size.
- **Self-audit verdict: CLEAN.** Per-case forbidden registry re-checked and all ABSENT — notably the **Gelsinger Dec-2024 departure** (he appears only as the as-of sitting CEO) and the **Lip-Bu Tan board resignation of Aug 19 2024**, which was specifically caught as POST-as-of and excluded (Tan appears only as a sitting director as-of). No post-crash price, no 18A/foundry outcome, no CHIPS equity stake, no outcome-aware language. Public bios/interview used as character-pattern/governance-context tier only, never as EVIDENCE-tier hard claims.
