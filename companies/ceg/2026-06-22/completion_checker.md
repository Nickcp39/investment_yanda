# Completion Checker — CEG (company-level A–F gate)

Last updated: **2026-06-22** · Status: **DECISION_DRAFT** (one live refresh pass; NOT COMPLETE)

Self-check before card lock (the independent Checker re-runs this). Per RUNNER_BRIEF §"完成自检".

## Honest status label

`NOT_STARTED → SCAFFOLD → P0_PASS_1 → P1_PARTIAL → DECISION_DRAFT → COMPLETE`

→ **DECISION_DRAFT.** All six modules have refreshed artifacts; the verdict is locked and capped by completeness; four gaps (audit §4) keep it below COMPLETE. The wording throughout says "live refresh / decision draft," never "full research complete."

## A–F gate (✓ = pass; see `audit.md` for detail)

| Gate | Status | Notes |
|---|---|---|
| A. Scope & definition | ✓ | as_of=2026-06-22 frozen; thesis gate + stop conditions pre-written |
| B. Evidence (M1) | ✓ | source_register (14), claim_ledger (30), facts, raw/, freshness.json; secondary PPA price excluded |
| C. 11-stage coverage | ✓ | all 8 analysis modules + IC panel present |
| D. Model & math | ✓ | scenario model arithmetic auditable; implied expectations from current price |
| E. Open questions | ✓ | classified blocking/monitoring/non-blocking; blockers cap verdict |
| F. Audit & consistency | ✓ | numbers reconcile (T5 PASS); card schema stamped |
| **Freshness (mechanical)** | ✓ | `verify_freshness.py` exit 0, status PASS |

## The 5 self-check questions (RUNNER_BRIEF)

1. **What is the current status label?** DECISION_DRAFT (info ~76).
2. **Which gates are not yet passed?** None of A–F fail; but CORE-blocking gaps G1 (combined FCF / SEC 10-K second-confirm) and G2 (no NEW premium PPA) remain open → ceiling STARTER.
3. **What evidence would raise it to COMPLETE/CORE?** Clean combined-entity FCF (primary), a NEW premium-nuclear PPA priced, and deleverage confirmed at ~2.0x.
4. **Any stale files with a different status?** No — all 2026-06-22 files carry the DECISION_DRAFT / STARTER read; the seed (`companies/ceg/`) is left untouched as the prior.
5. **Does the wording match the true status?** Yes — STARTER / DECISION_DRAFT / "live refresh," not "complete."

## Verdict-ceiling check

- Completeness ~76 → ceiling STARTER. Card = STARTER. **Not exceeded.** ✓
- Durability ceiling (cyclical merchant + gas dilution) independently caps below CORE. ✓
- Margin of safety exists → M6 does not cap below completeness. ✓

## Result: **CARD MAY LOCK at STARTER / DECISION_DRAFT.**
