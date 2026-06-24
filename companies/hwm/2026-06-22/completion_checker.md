# HWM Completion Checker (company-level A-F gate)

As-of: 2026-06-22 | Run: 2026-06-23 | Status: DECISION_DRAFT

| Gate | Requirement | Status | Note |
|---|---|---|---|
| **A. Freshness** | verify_freshness.py exit 0, status PASS, >=2 price sources, T5 single-value-of-truth | **PASS** | $280.36 re-fetched to the penny; mcap identity 0.00%; T1-T5 pass; 2 T6 WARN (non-blocking) |
| **B. Provenance** | pipeline_version + weights_version + run_date stamped | **PASS** | lean-6module-v1.1 / none / 2026-06-23 |
| **C. Six modules emit signals** | M1-M6 each {signal, confidence, finding, drivers} | **PASS** | M1+1, M2+2, M3+2, M4+2, M5-1, M6-2 |
| **D. Two-axis verdict** | new-money + existing-position | **PASS** | WATCH / HOLD |
| **E. Source discipline** | load-bearing claims dated + tiered; primary>secondary | **PASS w/ OPEN** | spares figure secondary-only (O1); no direct EDGAR (O2) |
| **F. Honesty** | real status label, runner_dissent, OPEN items, no fabricated quotes | **PASS** | DECISION_DRAFT; dissent written; IC voices labeled (lens) |

## Blocking issues

- None for the freshness gate or the verdict. 

## Non-blocking OPEN items (cap completeness, not the price verdict)

- O1 spares precision (secondary), O2 no direct EDGAR full-text, O3 owner-earnings bridge, O4 CAM contribution, O5 Plant succession.

## Checker hand-off

This is the **Runner** output. An independent **Checker** pass (re-derive numbers, re-run freshness, challenge the IRR exit-multiple assumptions, confirm spares vs 10-Q) is the next step to move toward COMPLETE.
