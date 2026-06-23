# VRT Research Status

Last updated: **2026-06-22**

Company: Vertiv Holdings Co. · Ticker: VRT (NYSE) · Batch: **mempower4 (LIVE, as_of 2026-06-22)**

This run **refreshes the 2026-06-19 seed dossier** (`companies/vrt/`) to as_of 2026-06-22 — all LIVE data re-pulled, freshness gate re-run, decision card re-locked.

Decision question:
1. (LEAD — bottleneck) Is VRT's datacenter power + thermal content a **durable, share-gaining toll booth** (rising $-content per AI rack as density forces liquid cooling), or a **high-beta capex-cycle play** that de-rates the moment the hyperscaler capex slope rolls? Does VRT own the bottleneck or merely supply into it?
2. (DECISION) At today's price ($345.05), BUY / NO-BUY / WATCH, and at what price/evidence each becomes right.
3. (KILL) What breaks the content-growth thesis?

Current stage: **DECISION_DRAFT** (one parallel pass, completeness ~70%). Full 6-module pipeline run on refreshed live data; freshness gate **PASS**; decision card **locked**. Honest status: this is a refresh of a thorough seed, not an independent multi-pass build — verdict ceiling held to completeness.

Verdict: **WATCH** (edge **STARTER** on pullback to ~$230–250 / clean Q2'26 orders re-disclosure) · info-completeness **~70/100** · business **good**. LEAD answer: **both true — a real, share-gaining *integration* toll booth that rides the capex cycle with no shock-absorber; which framing dominates depends on the hyperscaler capex slope.** See `memo-v1.md`, `bottleneck_map.md`, `decision_card.json`.

**Binding constraint: PRICE (M6 caps first).** At $345.05 fwd P/E is ~50.5–54x, −9.2% off the ATH, near-term bull +4% / bear −47% (no floor), Street only +9.6% away → no margin of safety, and the +3.6% move from the seed's $333.05 worsened the skew. **Secondary (tightly coupled): orders / book-to-bill / backlog STILL withheld** (C012) — the cleanest demand gauge remains dark, next read Q2'26 (2026-07-29).

---

## Freshness Gate (mempower4 hard门)

- `freshness.json`: every LIVE field (price/mcap/52wk/shares/target + guidance + corporate actions) carries ≥2 independent sources + cross-check delta.
- `python scripts/verify_freshness.py --dossier companies/vrt/2026-06-22` → **exit 0, status==PASS** (`freshness_check.json`).
- Price $345.05 (Yahoo close 06-22) cross-checked vs stockanalysis $344.68 + Yahoo regularMarket $344.87 + independent re-fetch (~$345.15) → all within 1%. Tripwires T1–T5 PASS; T6 WARN only (guidance source 61d old — expected: latest hard quarter is Q1'26, Q2'26 = 2026-07-29 not yet public).

---

## Module Checklist — M1–M6 done

| Module | Role | Artifact | Status | Signal |
|---|---|---|---|---|
| M1 Evidence Spine | confidence | `facts.md`, `source_register.md`, `claim_ledger.csv`, `freshness.json` | ✅ refreshed | +1 |
| M2 Theme / Mechanism | context+conviction | `business_model.md`, `value_chain_map.md` | ✅ refreshed | +2 |
| M3 Profit Pool / Durability | conviction | `moat_map.md`, `bottleneck_map.md`, `operator_underwriting.md` | ✅ refreshed | +1 |
| M4 Financial Reality | conviction | `financials/financial_quality.md`, `model/` | ✅ refreshed | +1 |
| M5 Inversion / Trap | risk | `inversion_map.md` | ✅ refreshed | −1 |
| M6 Price / Position / Monitor | price+output | `valuation.md`, `model/scenario_model.csv`, `monitor.md` | ✅ refreshed | −2 |
| Aggregation | — | `audit.md`, `ic_panel.md`, `memo-v1.md`, `decision_card.json/.md` | ✅ locked | WATCH |

---

## What changed vs the 2026-06-19 seed

| Field | Seed (06-19) | Refresh (06-22) | Effect |
|---|---|---|---|
| Price | $333.05 (06-18 close) | **$345.05** (06-22 close) | +3.6% |
| Market cap | ~$128B | **~$132.5B** | |
| 52-wk high / low | $380 / $110 | **$379.94 / $110.06** | refined |
| Off high / low | −12% / +203% | **−9.2% / +213%** | closer to high |
| Forward P/E | ~48–52x | **~50.5–54x** | richer |
| Street upside | +13% | **~+9.6%** | thinner |
| Latest quarter | Q1'26 | **Q1'26 (unchanged)** | Q2'26 = 2026-07-29 |
| Orders/B2B gap | withheld | **STILL withheld** | binding gap persists |
| New events | — | **ThermoKey closed 06-12; $0.0625/qtr dividend declared** | on-strategy bolt-on + token dividend |
| Verdict | WATCH | **WATCH (unchanged; skew worse)** | M6 caps first |

---

## Open Questions (primary cross-checks — do not block the conclusion)

- [ ] **Orders / book-to-bill / backlog** — still withheld; **the binding gap.** Next read Q2'26 (2026-07-29). (C012)
- [ ] **Segment split** (power/thermal/services) — pull from 10-K/10-Q to decompose content-per-rack economics. (C016)
- [ ] **Multiples & Street target** — aggregator-sourced (S6, `needs_audit`); confirm against the 10-Q + a clean consensus feed. (C029, C031)
- [ ] **Net-cash composition** — confirm gross cash vs debt against the 10-Q. (C028)

## Pollution Checks

- [x] No KOL as fact (no video sources; S6/S7/S8/S9 are B2 independent/press for market data + context only; S8 used only to corroborate a disclosure behavior).
- [x] Fact / interpretation / assumption separated (claim_ledger status-graded; forecasts in `model/` labeled assumptions).
- [x] Key numbers carry a source id; every LIVE field carries ≥2 sources in `freshness.json`.
- [x] Every thesis variable has a kill condition (`monitor.md` + `inversion_map.md`); the binding gap (C012) surfaced across downstream files.
- [x] Memo does not run ahead of evidence (verdict WATCH, gated by valuation + the withheld orders/B2B; one strong quarter not extrapolated into a permanent moat).

## Honesty notes (RUNNER_BRIEF §5)

① Current status = **DECISION_DRAFT** (one parallel refresh pass, ~70% completeness), NOT COMPLETE. ② Gates still open: orders/B2B re-disclosure (Q2'26), 10-Q segment/net-cash, aggregator multiples one-hand audit. ③ Evidence to reach COMPLETE: Q2'26 orders print + 10-Q line items. ④ No stale metadata — all files dated 2026-06-22 and consistent (same verdict, same binding gap, same kill status a→YELLOW / b,c,d→GREEN). ⑤ Wording matches real status throughout. Uncertainty captured in `runner_dissent` + OPEN items.
