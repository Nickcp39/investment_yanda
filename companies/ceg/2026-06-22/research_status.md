# CEG Research Status

Last updated: **2026-06-22**

Company: Constellation Energy Corporation
Ticker: CEG (Nasdaq; spun from Exelon 2022)
Batch: **mempower4 LIVE (as_of 2026-06-22)** — AI-datacenter power/cooling leg (with VRT); seeded from the 2026-06-19 dossier (`companies/ceg/`)

## Honest status label: **DECISION_DRAFT**

This is **one live refresh pass on an existing seed dossier**, not a COMPLETE multi-pass research cycle. Per the RUNNER_BRIEF honesty rule: one parallel pass = `DECISION_DRAFT` (~55–75%), and the verdict ceiling = completeness. Do **not** read this as "full research complete."

- Info-completeness: **~76/100** → caps verdict at **STARTER**.
- Freshness gate: **PASS** (`freshness_check.json`, exit 0; 3 price sources within 1%).

## Decision question

1. (LEAD — bottleneck) Is CEG's existing nuclear fleet a **durable scarcity rent** (carbon-free baseload you can't build new, sold to datacenters at premium PTC-floored PPAs), or is the AI-power premium fully priced and hostage to the FERC co-location switch?
2. (DECISION) Live fresh-initiation verdict at today's price (holder owns 0 shares).
3. (KILL) What breaks the scarcity-rent thesis?

## LEAD answer

**The scarcity rent is durable and NOT FERC-hostage.** The −33% de-rate (from the $412.70 high) is mostly multiple normalization (>35x → ~24x) + Calpine digestion. The two scariest pre-registered kills (FERC, PTC) are empirically resolved favorably; demand is accelerating (+77%). The live risks are **execution** (Calpine deleverage — now meaningfully de-risked, see below) and a **flagship whose upside is already sold to MSFT** — so the equity re-rate hinges on the next premium PPA.

## What the 2026-06-22 refresh changed vs the seed

| Field | Seed (06-19) | Live (06-22) | Significance |
|---|---|---|---|
| Price | $274.06 | **$277.64** | +1.3%; verdict unchanged |
| Post-Calpine leverage | ~3.8x (disputed estimate) | **~$21.3B net debt / ~2.25x pro-forma (10-Q primary)** | **Material de-risk of kill (c)** |
| LS Power divestiture | signed | **completed (cash in)** | deleverage part-proven |
| New PPA | none | **CyrusOne 380 MW (gas)** | partial — not premium nuclear |
| Calpine consideration | $26.6B headline | **$21,835M (10-Q)** | clarified (primary) |

**Net:** the refresh modestly **strengthens** the thesis (balance sheet less stressed than feared) but does **not** change the verdict — the binding constraint (capped flagship + no new premium PPA + completeness ceiling) is unchanged.

## Verdict: **STARTER · info ~76/100 (caps at STARTER) · HOLD for existing**

Primary IC read order: `decision_card.md` → `memo-v1.md` → `facts.md` → `bottleneck_map.md` + `moat_map.md` → `inversion_map.md` → `valuation.md` → `monitor.md`.

## Block tracker — Blocks 1–9 refreshed (v2, live)

| Block | Artifact(s) | Status | Date |
|---|---|---|---|
| 1. Evidence foundation | `source_register.md`, `claim_ledger.csv` (30), `facts.md`, `freshness.json`, `raw/` | ✅ refreshed | 2026-06-22 |
| 2. Financial quality | `financials/financial_quality.md` | ✅ refreshed (primary leverage) | 2026-06-22 |
| 3. Business model | `business_model.md` | ✅ refreshed | 2026-06-22 |
| 4. Industry / value chain | `value_chain_map.md` | ✅ refreshed | 2026-06-22 |
| 5. Moat / bottleneck (LEAD) | `moat_map.md`, `bottleneck_map.md` | ✅ refreshed | 2026-06-22 |
| 6. Operator | `operator_underwriting.md` | ✅ refreshed | 2026-06-22 |
| 7. Inversion | `inversion_map.md` | ✅ refreshed | 2026-06-22 |
| 8. Valuation + IC panel | `valuation.md`, `model/scenario_model.csv`, `ic_panel.md` | ✅ refreshed | 2026-06-22 |
| 9. Decision / monitor | `memo-v1.md`, `monitor.md`, `decision_card.json/.md` | ✅ locked | 2026-06-22 |
| 10. Postmortem | `postmortem.md` | ⏳ stub — fill at review | — |

## Kill-criteria status (the 5 pre-registered)

| Kill | Status (2026-06-22) |
|---|---|
| (a) FERC blocks co-location | **DEFUSED** — 5-0 enabling order 2025-12-18; Crane front-of-meter |
| (b) Power → PTC floor | LIVE but FLOORED (~$25/MWh to 2032; 2027 open ~$34/MWh) |
| (c) Calpine dilutive/over-levered | **PARTIAL but DE-RISKED** — ~2.25x pro-forma (not 3.8x); LS Power cash in; purity 90%→58% |
| (d) PTC repealed | NOT TRIGGERED — survived OBBBA |
| (e) Shared switch: capex slope | **ACCELERATING +77%** to ~$725B — not firing (single-factor tie with NBIS/VRT) |

## Open Questions (do not block STARTER; needed for CORE)

- [ ] Microsoft PPA price (undisclosed; secondary $100–115/MWh unconfirmed) — sizes Crane economics + how capped the flagship is.
- [ ] Year-by-year hedge ratios (undisclosed) — near-term power-price sensitivity.
- [ ] Any NEW premium-nuclear hyperscaler PPA (none; CyrusOne is gas) — the single biggest re-rate catalyst.
- [ ] SEC 10-K (FY2025) headline + combined-entity FCF — second primary confirmation before CORE.
- [ ] CFO / full board roster + Dominguez comp structure (per the proxy).

## Pollution checks

- [x] No KOL as fact. Secondary $100–115/MWh PPA estimates explicitly held OUT of facts as unconfirmed commentary.
- [x] Fact / interpretation / assumption separated; claim_ledger graded.
- [x] Key numbers carry a source_id (claim_ledger 30 rows + facts tagged S#).
- [x] Every thesis variable has a kill condition (`monitor.md` + `inversion_map.md`).
- [x] Memo does not run ahead of evidence (STARTER, info ~76 caps it).
- [x] Freshness gate PASS; price via Yahoo chart API + 2 cross-checks; single-value-of-truth holds.
- [x] Status label is honest (DECISION_DRAFT, not COMPLETE).
