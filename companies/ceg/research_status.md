# CEG Research Status

Last updated: 2026-06-19

Company: Constellation Energy Corporation
Ticker: CEG (Nasdaq; spun from Exelon 2022)
Batch: AI-electricity bottleneck — power/grid generation layer (1 of 3, with [[GEV]], [[VRT]])

Decision question:
1. (LEAD — bottleneck) Is CEG's existing nuclear fleet a **durable scarcity rent** (carbon-free baseload you can't build new, sold to datacenters at premium PTC-floored PPAs), or is the AI-power premium fully priced and hostage to the FERC co-location switch?
2. (DECISION) Live fresh-initiation BUY / NO-BUY / WATCH at today's price (holder owns 0 shares).
3. (KILL) What breaks the scarcity-rent thesis?

Current stage: **✅ Blocks 1–9 first-run complete (v1).** Evidence base + 9 analysis layers + memo + monitor all written. Remaining = a few primary-confirm items (see Open Questions) and forward quarterly monitoring.

Verdict: **STARTER · info-completeness 76/100 (caps at STARTER) · rank #1 of 3.** Entry ref $274.06.
LEAD answer: **the scarcity rent is durable and NOT FERC-hostage; the −34% de-rate is mostly multiple normalization (>35x → ~24x) + Calpine digestion.** See `bottleneck_map.md` / `memo-v1.md`.

Primary IC read order: `memo-v1.md` → `facts.md` → `bottleneck_map.md` + `moat_map.md` → `inversion_map.md` → `valuation.md` → `monitor.md`.

---

## Block tracker — Blocks 1–9 done

| Block | Question | Artifact(s) | Status | Date |
|---|---|---|---|---|
| 1. Evidence foundation | What is true? | `source_register.md` (S1–S12), `claim_ledger.csv` (28), `facts.md`, `raw/` (6 blocks) | ✅ done | 2026-06-19 |
| 2. Financial quality | Real economics (FCF, PTC floor, leverage)? | `financials/financial_quality.md` | ✅ done | 2026-06-19 |
| 3. Business model | Merchant + hyperscaler PPAs? | `business_model.md` | ✅ done | 2026-06-19 |
| 4. Industry / value chain | Where is profit captured? | `value_chain_map.md` | ✅ done | 2026-06-19 |
| 5. Moat / bottleneck (LEAD) | Durable scarcity rent vs FERC exposure | `moat_map.md`, `bottleneck_map.md` | ✅ done | 2026-06-19 |
| 6. Operator | Capital allocation; Calpine integration | `operator_underwriting.md` | ✅ done | 2026-06-19 |
| 7. Inversion | The 5 kills (FERC/price/Calpine/PTC/shared-switch) | `inversion_map.md` | ✅ done | 2026-06-19 |
| 8. Valuation | Premium already priced? | `valuation.md`, `model/scenario_model.csv` | ✅ done | 2026-06-19 |
| 9. Decision / monitor | BUY/NO-BUY/WATCH + triggers | `memo-v1.md`, `monitor.md` | ✅ done | 2026-06-19 |
| 10. Postmortem | (after outcome) | `postmortem.md` | ⏳ stub — fill at review | — |

---

## Kill-criteria status (the 5 pre-registered)

| Kill | Status |
|---|---|
| (a) FERC blocks co-location | **DEFUSED** — 5-0 enabling order 2025-12-18; Crane front-of-meter |
| (b) Power → PTC floor | LIVE but FLOORED (~$25/MWh to 2032; 2027 open ~$34/MWh) |
| (c) Calpine dilutive/over-levered/re-carbonizes | **PARTIAL TRIGGER** — purity 90%→58%; leverage→3.8x |
| (d) PTC repealed | NOT TRIGGERED — survived OBBBA |
| (e) Shared switch: hyperscaler capex slope | **ACCELERATING +77%** to ~$725B — not firing |

→ 3 defused, 1 floored, 1 partial. The thesis dies only on **Calpine execution + no new PPA**.

---

## Open Questions (primary-confirm items — do not block the verdict, finish next pass)

- [ ] **Post-Calpine net-debt/EBITDA** — ~3.8x estimated; confirm at Q2'26 10-Q. (C011)
- [ ] **Microsoft PPA price** — undisclosed by CEG; sizes Crane economics + how capped the flagship upside is. (C013)
- [ ] **Year-by-year hedge ratios** — undisclosed; needed for near-term power-price sensitivity.
- [ ] **Any new post-Meta hyperscaler PPA** — none confirmed; the single biggest re-rate catalyst.
- [ ] **S1 (FY2025) / S2 (Q1'26) headline figures via primary URL** — releases returned HTTP 404/410 on automated re-fetch 2026-06-19; carried at pack confidence; re-confirm vs SEC 10-K / 10-Q.
- [ ] CFO / full board roster + Dominguez comp structure (per the proxy).

## Pollution Checks

- [x] No KOL as fact (no video/C-tier sources used for any number).
- [x] Fact / interpretation / assumption separated ([PRIMARY]/[SECONDARY] in raw; claim_ledger status graded verified/partial/unverified/needs_audit).
- [x] Key numbers carry a source_id (claim_ledger 28 rows + facts all tagged S#).
- [x] Every thesis variable has a kill condition (`monitor.md` + `inversion_map.md`).
- [x] Memo does not run ahead of evidence (STARTER, info 76/100 caps it; rests on bottleneck + inversion + valuation).
- [x] Decision unchanged from the locked verdict (STARTER / 76 / #1 of 3); model implied prices reconciled to memo ranges.

## Relationship to existing files

- `step0_plan.md`, `facts.md`, `memo-v1.md` were **already written** and are **preserved unchanged** (facts.md lightly extendable but verdict/numbers held). Everything in this footprint agrees with them.
- This `companies/ceg/` set = the full 10-layer pipeline footprint, decomposed from the Block-1 evidence pack, mirroring `_company_research_template/` structure and `nbis/` depth.
