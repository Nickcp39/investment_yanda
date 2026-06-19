# Material Pack Lookahead Audit - DIS 2021-11-11

Independent checker pass (different agent than the collector). As-of date: 2021-11-11.
Files audited: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

## 0. Audit Verdict

- **Verdict: CLEAN.**
- No load-bearing post-cutoff fact is used; no decision/thesis/valuation verdict is present.
- The known trap (FY2021 10-K filed 2021-11-24, AFTER as-of) is correctly EXCLUDED, with balance-sheet detail taken from the 2021-11-10 release instead. Checker confirms the 10-K is not used.

## 1. Source Date Check

WEB-VERIFIED: S001 (Q4 & FY2021 release, 2021-11-10 — SEC EDGAR 8-K `000174448921000214`; 118.1M Disney+, $18.53B rev, $0.37 EPS, -5% afterhours all confirmed); S005 (consensus $18.79B / $0.51 EPS / ~125-126M subs confirmed by Hollywood Reporter + CNBC); S009 (as-of close $162.11, down ~7% first full session after earnings).

| source_id | public_date | <= as_of? | web-verified | issue |
|---|---|---|---|---|
| S001 | 2021-11-10 | yes | yes (SEC URL match) | none |
| S002 | 2021-11-10 | yes | - | none |
| S003 | 2021-11-10 | yes | yes | none |
| S004 | 2021-11-10 | yes | - | none |
| S005 | 2021-11-10 | yes | yes | none |
| S006 | 2021-11-10 | yes | - | none |
| S007 | 2021-08-12 | yes | - | none |
| S008 | 2021-08-12 | yes | - | none |
| S009 | 2021-11-11 | yes (= as-of) | yes (price) | none |

All 9 rows dated on or before the as-of date. 0 source-date issues. FY2021 10-K (2021-11-24) correctly NOT in the source list.

## 2. Claim Traceability

| key claim | source_id | traceable to allowed source? |
|---|---|---|
| Q4 rev $18,534M +26%; FY21 $67,418M | S001 | yes |
| Disney+ 118.1M (+60% YoY); only ~2.1M net adds | S001, S004 | yes |
| Q3 FY21 Disney+ 116M (+12% QoQ) -> deceleration | S007, S008 | yes |
| Disney+ ARPU -9% to $4.12 (Hotstar mix) | S001, S005 | yes |
| Q4 DTC op loss widened to -$630M; FY21 -$1,679M | S001 | yes |
| Q4 DPEP rev $5,450M (+99%), OI $640M | S001 | yes |
| Cash $15,959M; borrowings ~$54.4B | S001 | yes |
| 230-260M Disney+ FY2024 target reiterated | S002, S003 | yes (mgmt) |
| As-of close $162.11 (down ~7%); ~$289B cap | S001, S009 | yes |
| Consensus $18.79B / $0.51 / ~126M subs | S003, S004, S005 | yes (press-reported, medium conf) |

All load-bearing claims trace to allowed source ids. No dangling references.

## 3. Outcome-Aware Language Check

Grep for hindsight phrasing across all files: **0 matches.** Management's forward statements (FY2022 reacceleration "in the third and fourth quarters," >160 countries by FY23, FY2024 subscriber + profitability target) are as-of guidance/targets from the 2021-11-10 call, explicitly tagged "mgmt framing." No post-as-of price appears.

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, dis_2021-11-11 row)

| forbidden item | status | where mentioned |
|---|---|---|
| 2022 stock decline | ABSENT | only the as-of close + trailing-52-week range; later decline only in case_control forbidden list |
| Chapek ouster / Iger return (Nov 2022) | ABSENT | Chapek appears only as the CURRENT (as-of) CEO; "Iger" appears only in case_control forbidden list |
| Widening DTC losses 2022-23 | ABSENT | only FY2021 / Q4 FY21 DTC figures used |
| Price hikes / password-sharing crackdown | ABSENT | only in case_control forbidden list |
| FY2022+ results | ABSENT | latest data is Q4/FY2021 (ended 2021-10-02) + as-of price |

All high-risk traps absent from the evidence/analysis; mentions exist solely inside the case_control forbidden list / evidence_spine self-check. Acceptable.

## 5. Evidence Misuse

- No KOL / social / video sources. Same-day trade press (S003-S006) used for the as-of market reaction and for consensus numbers (not in the company filing); evidence_spine §4 assigns these medium confidence as "press-reported analyst numbers, not company disclosures."
- S007/S008 (prior-quarter baseline) are primary-corroborated trade press establishing the deceleration trajectory.
- Management "non-linear growth / dam will break on content" framing and the FY2024 target are explicitly "company optimistic framing; treated as commentary, not verified fact" (evidence_spine §2).

## 6. Materials-Only Check

Grep for decision/valuation verdict tokens: **0 matches.** Naive multiples (~71x ex-items EPS, ~146x GAAP) are explicitly "stated as raw arithmetic for the record only; not a valuation judgment." evidence_spine §5 confirms "No buy/sell decision, thesis, or valuation verdict is present (material pack only)." No decision/thesis/valuation/decision_card content present.

## 7. Decision

The pack is **CLEAN** and test-ready. The post-as-of 10-K trap is correctly handled; no post-cutoff fact, no personnel-change leak, no decision present.

## 8. Addendum — operator_background.md added (2021-11-11 as-of)

- **Added:** `operator_background.md` (founder/operator dossier per `_operator_underwriting_template.md`): core team = Chapek (CEO), Iger (departing Exec Chairman), McCarthy (CFO), + Kareem Daniel (DMED) as the powered-but-loyalist 4th. Formation-first per person, required dark-arc per person, team-level succession/culture read, fracture inversion, durability grade. Team life-arc grade **2.5 (~2–3)**, governance discount required. 6 dated operator sources (O1–O6), all `public_date <= 2021-11-11` (Variety 2020-02-25 & 2016-05; TheWrap 2021-07-13; THR 2021-10-06; WDWNT 2021-05; Disney 8-K/transcript 2021-11-10).
- **Self-audit (LOOKAHEAD_CHECKER):** **CLEAN.** Forbidden registry items all ABSENT as facts — Chapek ouster/Iger return (Nov 2022), Kareem Daniel exit, McCarthy step-down (2023), Susan Arnold's chairman naming (announced 2021-12-01, post-as-of), 2022 stock decline, FY2022+ results appear ONLY inside the explicit "post-as-of EXCLUDED" notice. The Iger↔Chapek power-sharing collapse and the DMED creative-vs-business friction are pre-as-of facts (sourced to O3 2021-07-13 and O4 2021-10-06), not hindsight. Iger's end-2021 departure and the CEO/chairman role separation were public as of as-of; the *named* board-chair successor was withheld as post-as-of. No decision/size/thesis present (people-side risk flags only). Reliability axis applied: unchooseable facts > third-party early-career > self-narrative (Iger's 2019 memoir explicitly discounted). **Verdict: CLEAN.**

---

## Independent Checker Pass (2026-06-19)

Second, **fully independent** checker (different agent than collector and than the §0–§8 auditor).
Scope: `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`,
`operator_background.md`, plus this file. Ran the 6-point `LOOKAHEAD_CHECKER.md` checklist + the
`dis_2021-11-11` forbidden-registry row. High-risk dates web-verified independently (not trusting the
CSV self-report).

### Verdict: **CLEAN** — test-ready. No load-bearing post-cutoff fact; no decision/thesis/valuation in the pack.

The single most dangerous trap (the FY2021 **10-K filed 2021-11-24**, 13 days AFTER as-of) is correctly
EXCLUDED; balance-sheet detail is taken from the 2021-11-10 release (8-K Ex-99.1) instead. **Independently
web-confirmed** the 10-K filing date below.

### A. Web-verification of high-risk / load-bearing dates (independent)

| item | pack's claim | independent web check | result |
|---|---|---|---|
| Q4 & FY2021 earnings release | 2021-11-10, 8-K Ex-99.1; Disney+ 118.1M, $18.53B rev, $0.37 ex-items EPS | Confirmed: release dated 2021-11-10; 118.1M, +2.1M net adds, $0.09 GAAP / $0.37 ex-items EPS | ✅ ≤ as-of |
| **FY2021 10-K (the trap)** | **filed 2021-11-24 → EXCLUDED** | **Confirmed: accession 0001744489-21-000220 filed Wed 2021-11-24 4:34pm ET (Fintel + Last10K)** | ✅ **post-as-of, correctly out** |
| As-of price | $162.11 close 2021-11-11, down ~7% from $174.45 (Nov 10) | Confirmed against local `asof_2021-11-11_dis_quotes.csv` (162.11; prior close 174.45; ~62M vol) | ✅ = as-of |
| Consensus | ~$18.79B rev / ~$0.51 EPS / ~125–126M subs (all missed) | Confirmed: ~125M subs expected vs 118.1M actual (press-reported, medium conf — correct tag) | ✅ ≤ as-of |
| O3 TheWrap (Kareem Daniel / DMED) | 2021-07-13 | Confirmed article exists, contemporaneous; describes Oct-2020 DMED reorg friction as a then-current fact | ✅ ≤ as-of |
| O4 THR (Iger long exit / Chapek) | 2021-10-06 | Confirmed; Iger's plan to run creative "until end of 2021," power-sharing tension, all pre-as-of | ✅ ≤ as-of |
| O5 Genie+ at $15/day | 2021-05 (WDWNT); launched fall 2021 | Confirmed: Genie+/Lightning Lane launched WDW **2021-10-19** at $15/ticket/park/day — pre-as-of | ✅ ≤ as-of |
| Susan Arnold board-chair naming | **announced 2021-12-01 → EXCLUDED, successor withheld** | Confirmed announced **2021-12-01** (effective 2021-12-31) — POST as-of; operator file withholds the name | ✅ **post-as-of, correctly out** |

### B. Six-point checklist

1. **Source-date check** — all 9 `sources_used.csv` rows + all 6 operator rows (O1–O6) dated ≤ 2021-11-11. 0 violations. The two boundary items (10-K, Arnold) are both post-as-of and both correctly excluded.
2. **Claim traceability** — every load-bearing fact (C001–C020) traces to an allowed `source_id`; operator claims trace to O1–O6. No dangling refs.
3. **Outcome-aware language** — no hindsight phrasing; no post-as-of price. Management's forward statements (FY2022 H2 reacceleration, >160 countries by FY23, 230–260M / profitability by FY2024) are tagged as as-of *mgmt framing/optimistic*, not verified fact.
4. **Post-cutoff fact intrusion (forbidden row)** — 2022 stock decline · Chapek ouster / Iger return (Nov 2022) · widening DTC losses 2022-23 · price hikes / password-sharing crackdown · FY2022+ results → **each ABSENT** as a fact; appears only inside explicit "post-as-of EXCLUDED" notices.
5. **Evidence misuse** — no KOL/social/video as core proof. Same-day trade press used for as-of reaction + consensus (medium conf, correctly flagged). Company optimistic framing not asserted as fact.
6. **Materials-only** — no `decision_card`, no buy/sell verdict, no thesis, no valuation conclusion. Naive multiples (~71× ex-items, ~146× GAAP) are explicitly "raw arithmetic … not a valuation judgment."

### C. Operator-file note (load-bearing for the future M3)

The `operator_background.md` succession/culture read (Iger↔Chapek fracture, DMED creative-vs-business
friction, loyalist-heavy inner circle, team grade **2.5/5**) is built **entirely from pre-as-of sources**
(O3 2021-07-13, O4 2021-10-06, O5 2021-05). The most tempting leak — using Iger's Nov-2022 *return* or the
Arnold name to color the people read — is NOT present. The fracture is diagnosed from facts knowable on
2021-11-11 (power-sharing collapse already reported; Iger's end-2021 exit already public). This is legitimate,
not hindsight.

### D. No load-bearing fact failed → proceed to Step 2 (blind run).
