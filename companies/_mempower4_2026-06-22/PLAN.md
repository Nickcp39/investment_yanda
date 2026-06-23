# mempower4 — Live Batch (as_of 2026-06-22)

Status doc + progress tracker. Mirrors the `_mega7_2026-06-19/` orchestration (PLAN + reused RUNNER_BRIEF + reused CHECKER).

## Scope

4 live full-dossier runs — the AI-buildout supply chain, two legs:
- **Memory/storage:** **MU** (Micron — DRAM/HBM/NAND), **SNDK** (SanDisk — NAND/flash)
- **AI-datacenter power/cooling:** **VRT** (Vertiv — power+thermal), **CEG** (Constellation — nuclear generation / AI PPAs)

## Mode & depth

- **LIVE** (实盘): use ALL current public info as of 2026-06-22 (latest earnings, current price, current management). No as-of freeze, no look-ahead QA.
- **Depth:** full GOOGL-level dossier (same as Mega7 + the existing VRT/CEG dossiers), each locking one `lean-6module-v1` `decision_card.json`.

## Canonical specs (REUSED — do not duplicate)

- **RUNNER_BRIEF** = `companies/_mega7_2026-06-19/RUNNER_BRIEF.md`
- **CHECKER** = `companies/_mega7_2026-06-19/CHECKER.md`
- Plus `PROTOCOL.md` · `COMPANY_MATERIAL_TEMPLATE.md` · `WEIGHTING_HARNESS.md` · `METHODOLOGY.md` · `_operator_underwriting_template.md` · `VERSIONS.md`.

**Deltas for this batch:** `as_of=2026-06-22`; dossier path = `companies/<ticker>/2026-06-22/` (dated subfolder, current convention); **data-freshness gate is the user's explicit priority — mandatory PASS.**

## Per-ticker notes

| ticker | seed | watch |
|---|---|---|
| MU | stub only (`companies/mu/step0_plan.md`) + backtest `mu_2025-03-21` (prior only) | ⚠ fiscal **Q3 2026 earnings ~late June 2026** — get the absolute latest; if just reported, use it; if imminent, note date + use latest available |
| SNDK | backtest `sndk_2025-06-16` (prior only) | NAND cyclical → durability ceiling caps below Core (METHODOLOGY) |
| VRT | **existing full dossier `companies/vrt/` (~2026-06-19)** — SEED from it | refresh ALL live data to 2026-06-22 + re-run freshness gate |
| CEG | **existing full dossier `companies/ceg/` (~2026-06-19)** — SEED from it | refresh ALL live data to 2026-06-22 + re-run freshness gate |

## 3-phase workflow (role isolation: Checker ≠ Runner)

```
Phase 1  Runner ×4 (parallel): build companies/<ticker>/2026-06-22/ full dossier
         + freshness.json (every LIVE field ≥2 sources) → run scripts/verify_freshness.py
         (exit 0 + freshness_check.json status==PASS) → lock decision_card.json
Phase 2  independent Checker ×4: run _mega7 CHECKER.md (confirm freshness_check.json==PASS
         before CLEAN) → companies/<ticker>/2026-06-22/checker_report.md
Phase 3  Synthesis: read 4 cards → attractiveness ranking + single-factor concentration
         → companies/_mempower4_2026-06-22/synthesis.md + dashboard.html
```

## Freshness gate (v1.1 hard门 — the user's requirement)

`python scripts/verify_freshness.py --dossier companies/<ticker>/2026-06-22` must produce `freshness_check.json` with `status==PASS`. No PASS = auto FIX-NEEDED. LIVE data (price/mktcap/52wk/shares/guidance/regulatory) ≥2 independent sources, price via Yahoo chart API cross-checked. (INC-001 lesson: a single mispriced field self-propagates and flips the verdict; manual "looks fresh" is not enough.)

## Honesty / verdict ceiling

One parallel pass = `DECISION_DRAFT` (~55–75%), NOT COMPLETE. Verdict ceiling = completeness (<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER / >80 CORE); for names with no price margin-of-safety, M6 caps before completeness.

## Progress tracker

| ticker | dossier | freshness PASS | decision_card locked | checker | verdict (new / existing) |
|---|---|---|---|---|---|
| MU   | ☑ | ☑ PASS | ☑ | ☐ | WATCH / HOLD (lean TRIM) — $1,184.88 ATH |
| SNDK | ☑ (missing financial_quality/memo/monitor/ic_panel/completion_checker) | ☑ PASS (T6 WARN) | ☑ | ☐ | WATCH / TRIM — $2,288.92 ATH |
| VRT  | ☑ (missing ic_panel/completion_checker) | ☑ PASS (T6 WARN) | ☑ | ☐ | WATCH / HOLD — $345.05 |
| CEG  | ☑ | ☑ PASS | ☑ | ☐ | **STARTER 2%** / HOLD — $277.64 |

> Runners hit a process-exit mid-run (all 4 "failed" notifications) but had already written the dossier + run `verify_freshness.py` → 4/4 freshness PASS, 4/4 decision_card locked. SNDK/VRT are missing a few wrapper files (ic_panel, completion_checker, +SNDK memo/monitor/financial_quality) — decisions are sound but those two aren't yet 100% to Mega7 spec. Phase 2 (independent Checker) + Phase 3 (synthesis) not yet run.

## Synthesis flag (pre-registered)

All 4 are **AI-capex + liquidity** plays (memory demand + datacenter power both ride the same buildout). Stacked on the user's existing NBIS / GOOGL / BTC, adding any of these = **doubling a single factor, not diversifying** (METHODOLOGY §5). Must be called out in synthesis.
