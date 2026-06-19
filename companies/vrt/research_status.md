# VRT Research Status

Last updated: 2026-06-19

Company: Vertiv Holdings Co.

Ticker: VRT (NYSE)

Decision question:
1. (LEAD — bottleneck) Is VRT's datacenter power + thermal content a **durable, share-gaining toll booth** (rising $-content per AI rack as density forces liquid cooling), or a **high-beta capex-cycle play** that de-rates the moment the hyperscaler capex slope rolls? Does VRT own the bottleneck or merely supply into it?
2. (DECISION) At today's price ($333.05), BUY / NO-BUY / WATCH, and at what price/evidence each becomes right.
3. (KILL) What breaks the content-growth thesis?

Current stage: **✅ Full pipeline (Blocks 1–9) complete (v1).** Evidence base + 9 analysis blocks + memo + monitor all written. Remaining = a few primary cross-checks (see Open Questions) and forward quarterly monitoring.

Verdict: **WATCH** (edge **STARTER** on pullback / clean orders re-disclosure) · info-completeness **72/100** · rank **#3 of 3** (with [[CEG]], [[GEV]]). LEAD answer: **both true — a real, share-gaining *integration* toll booth that rides the capex cycle with no shock-absorber; which framing dominates depends on the hyperscaler capex slope.** See `memo-v1.md`, `bottleneck_map.md`.

**Binding gap:** **verified current Q1'26 orders / book-to-bill / backlog — WITHHELD by the company.** The single cleanest demand gauge went dark exactly when it matters; surfaced consistently in `claim_ledger.csv` (C012), `inversion_map.md`, `monitor.md`.

---

## Block Checklist — 1–9 done

| Block | Question | Artifact | Status | Date |
|---|---|---|---|---|
| 1. Direction | Why now / hypothesis | `step0_plan.md` | ✅ done | 2026-06-19 |
| 2. Evidence | What is true? | `source_register.md` (9 sources), `claim_ledger.csv` (33 claims), `facts.md` | ✅ done | 2026-06-19 |
| 3. Financial quality | Real economics? | `financials/financial_quality.md`, `model/` (assumptions + scenario.csv) | ✅ done | 2026-06-19 |
| 4. Business model | How it makes money | `business_model.md` | ✅ done | 2026-06-19 |
| 5. Industry / value chain | Where is profit captured? | `value_chain_map.md` | ✅ done | 2026-06-19 |
| 6. Moat / bottleneck (LEAD) | Toll booth vs cycle | `moat_map.md`, `bottleneck_map.md` | ✅ done | 2026-06-19 |
| 7. Operator | Management / capital allocation | `operator_underwriting.md` | ✅ done | 2026-06-19 |
| 8. Inversion | How it fails | `inversion_map.md` | ✅ done | 2026-06-19 |
| 9. Valuation | Priced for permanent compounding? | `valuation.md`, `model/scenario_model.csv` | ✅ done | 2026-06-19 |
| 10. Decision / monitor | BUY/NO-BUY/WATCH + monitor | `memo-v1.md`, `monitor.md` | ✅ done (postmortem pending outcome) | 2026-06-19 |

---

## Raw research log (Block 2 evidence base)

| Raw file | Mapped layer | Topic |
|---|---|---|
| `raw/research_2026-06-19_L3-4_financials.md` | L3/4 | FY25 + Q1'26 financials, orders/backlog series, the Q1'26 orders/B2B withholding |
| `raw/research_2026-06-19_L4_business_model_value_chain.md` | L4 | product stack, value-chain position, NVIDIA integration stack |
| `raw/research_2026-06-19_L5-6_moat_bottleneck.md` | L5/6 | moat/bottleneck, liquid-cooling share, NVIDIA design, competition |
| `raw/research_2026-06-19_L7-8_operator_inversion.md` | L7/8 | operator (Albertazzi), inversion paths, the "backlog silence" flag |
| `raw/research_2026-06-19_L9_valuation_market.md` | L9 | valuation multiples, scenarios, Street targets |

---

## Open Questions (primary cross-checks — do not block the conclusion, but close next pass)

- [ ] **Q1'26 orders / book-to-bill / backlog** — withheld by the company (last hard print: Q4'25 organic orders +252% / B2B ~2.9x / backlog $15.0B). **The binding gap.** Watch Q2'26 (~July 2026). (C012)
- [ ] **Segment split** (power vs thermal vs services revenue/margin) — pull from 10-K/10-Q to decompose content-per-rack economics. (C016)
- [ ] **Multiples & Street target** — aggregator-sourced (S6, `needs_audit`); confirm against the 10-Q balance sheet + a clean consensus feed. (C029, C031)
- [ ] **Net-cash composition** — confirm gross cash vs debt split against the 10-Q. (C028)

## Pollution Checks

- [x] No KOL as fact (no video sources in this case; S6/S7/S8/S9 are B2 independent/press, used for market data + industry context only).
- [x] Fact / interpretation / assumption separated (raw digests flagged UNAUDITED; `claim_ledger` status-graded; forecasts in `model/` labeled assumptions).
- [x] Key numbers carry a source id (33-claim ledger; `facts.md` all cite [S#]).
- [x] Every thesis variable has a kill condition (`monitor.md` + `inversion_map.md`); the binding gap (C012) is surfaced in all four downstream files.
- [x] Memo does not run ahead of evidence (verdict WATCH, gated by valuation + the withheld orders/B2B; does not extrapolate one strong quarter into a permanent moat).

## Consistency with pre-written files

- `step0_plan.md`, `facts.md`, `memo-v1.md` were written first and are **preserved unchanged**; this status + all Block files are consistent with them (same verdict WATCH, same binding gap, same kill-criteria status A→YELLOW / B,C,D→GREEN).
