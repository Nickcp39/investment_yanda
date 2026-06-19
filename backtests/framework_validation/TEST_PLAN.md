# Blind Backtest — Sequential Test Plan

Status: `READY TO RUN` · Created 2026-06-17 · pipeline_version `lean-6module-v1` · weights_version `none` (no `W_v1.json` yet — Runner reasons qualitatively per `WEIGHTING_HARNESS.md`; this first pass establishes BASELINE behavior, not tuned weights).

## Rule: ONE case at a time

Run each case fully (checker → runner → scorer) and report before starting the next. No parallel fan-out. This keeps it controlled, resumable, and lets a failure pattern stop the run before it spreads.

## Per-case pipeline — 3 independent agents (independence is the whole point)

```
[1] Independent Checker  →  [2] Blind Runner  →  [3] Scorer
   (≠ collector)             (≠ checker, blind)    (sees outcome)
```

**[1] Independent Checker** — a DIFFERENT agent than the one that collected the pack. Runs `LOOKAHEAD_CHECKER.md` (6-point checklist + the per-case forbidden registry) over the pack. Verdict `CLEAN / CLEAN-WITH-NOTES / LEAK`. A `LEAK` halts the case (fix or void) — do NOT run the Runner on a leaked pack. Writes/updates `material_audit.md`.

**[2] Blind Runner** — fresh, blind. Inputs it may read: the case folder's `case_control.md` + the 5–6 material files (incl. `operator_background.md`) + `PROTOCOL.md` + `COMPANY_MATERIAL_TEMPLATE.md` + `WEIGHTING_HARNESS.md` + `METHODOLOGY.md` (for the position ladder + durability ceiling). MUST NOT read: `companies/<ticker>/` (full-info), `CASE_INDEX.md` (has the winner/trap hint), any outcome. Produces `decision_card.json` + `decision_card.md`, locks them, writes `runner_dissent` if the mechanical result feels wrong. No outcome, no score.
- The `operator_background.md` team-grade feeds the **durability ceiling** (METHODOLOGY): high-grade founder/long-arc team can raise the size ceiling; a 2.5/5 fracture lowers it / forces a governance discount.

**[3] Scorer** — sees post-as-of data. Computes the REALIZED outcome itself (as-of price → +12 / +24 / +36 mo and to-today, vs SPY and SOXX/peer), classifies winner/trap, then grades the locked decision per `PROTOCOL.md` §6 + `METHODOLOGY.md` §7 (size-distance + reasoning + the rule that a winner sized only as a tiny STARTER LOSES points — "right direction, too small" is not full marks). Writes `outcome_score.md` and appends one row to `results.csv`.

**Provenance gate (both Checker & Scorer enforce it).** The Checker confirms the card stamps
`pipeline_version` / `weights_version` per [`VERSIONS.md`](VERSIONS.md); the Scorer copies those ids
**verbatim** into the `results.csv` row (never invents them) and confirms they match the active registry.
An unstamped or mismatched card **halts the case** until fixed — this is what guarantees every case is
traceable to the exact pipeline version that produced it.

## Blindness / sealed outcomes

- Checker & Runner never see the outcome. **Sealed outcomes are NOT stored in case folders.** The Scorer reconstructs the realized outcome from post-as-of market data at scoring time.
- The orchestrator holds the expected winner/trap label only to sanity-check the Scorer; it is passed to the Scorer, never to the Runner.

## Order (sequential)

| # | case | why this slot |
|---|---|---|
| 1 | `googl_2024-06-14` | the motivating case — does the redesign give a real position instead of `WATCH / 0%`? |
| 2 | `intc_2021-04-23` | trap, near a top |
| 3 | `intc_2024-08-02` | winner, near a bottom — the **same-company discrimination pair** with #2 |
| 4 | `nvda_2023-05-25` | exceptional_bottleneck winner (founder team 4/5) |
| 5 | `meta_2022-11-10` | turnaround winner (founder-control discount 3/5) |
| 6 | `amzn_2023-02-03` | cyclical/quality winner |
| 7 | `aapl_2016-05-12` | quality compounder mispriced as ex-growth |
| 8 | `pfe_2022-02-08` | false-cheap peak-earnings trap |
| 9 | `pypl_2021-07-29` | expensive decelerating-growth trap |
| 10 | `dis_2021-11-11` | structural-decline trap (operator fracture 2.5/5) |

(Order adjustable. `mu_2025-03-21` was already self-run; re-run cleanly here only if desired.)

## Scoreboard — `results.csv`

One row per scored case (schema = `WEIGHTING_HARNESS.md` §7):
`pipeline_version, weights_version, case_id, context_label, mechanical_label, target_size, predicted_new_money_verdict, predicted_existing_position_verdict, correct_size_band, size_distance_error, veto_fired, veto_expected, dominant_module, dominant_module_expected, reasoning_score, failure_tags, notes`

## After each case (report + checkpoint)

1. Report: the blind decision (verdict + size + binding constraint) → then the realized outcome + score.
2. Update `results.csv` + the status tracker below.
3. Proceed to the next case, or pause.

## Stop conditions

- A `LEAK` halts that case until fixed.
- **Do not tune weights mid-run.** If a failure pattern repeats across ≥3 cases, pause and discuss a framework patch (per the anti-overfitting rule) — a single case is a hypothesis, not a mandate.

## Status tracker

| # | case | checker | runner | scorer | result |
|---|---|---|---|---|---|
| 1 | googl_2024-06-14 | CLEAN | STARTER 4% / max 12% / HOLD | PASS · size-dist 1 · sound | ✅ WINNER +116% (back-loaded); old WATCH/0% disease fixed |
| 2 | intc_2021-04-23 | CLEAN | WATCH / 0% / TRIM | PASS · size-dist 0 · sound | ✅ TRAP correctly avoided (M5 led) |
| 3 | intc_2024-08-02 | CLEAN | WATCH / 0% / TRIM | FAIL · size-dist 3 · shallow | ❌ WINNER +445% MISSED — same trap frame as 2021 |
| 4 | nvda_2023-05-25 | CLEAN | STARTER 3% / max 12% | PASS · size-dist 1 · sound | ✅ WINNER +446%; too-small at the 12% ceiling |
| 5 | meta_2022-11-10 | CLEAN | STARTER 3.5% / max 9% | PASS · size-dist 1 · sound | ✅ WINNER +465%; ceiling capped by founder-control discount (P1) |
| 6 | amzn_2023-02-03 | CLEAN | STARTER 4% / max 12% | PASS · size-dist 0 · sound | ✅ WINNER +138%; mirror-correct of INTC-2024 |
| 7 | aapl_2016-05-12 | CLEAN | STARTER 4% / max 11% | PASS · size-dist 1 · sound | ✅ WINNER +1318%; be braver at the ceiling |
| 8 | pfe_2022-02-08 | — | — | — | |
| 9 | pypl_2021-07-29 | — | — | — | |
| 10 | dis_2021-11-11 | — | — | — | |
