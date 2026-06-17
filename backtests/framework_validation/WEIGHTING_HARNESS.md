# Lean Pipeline Weighting & Tuning Harness

Status: `DESIGN - NOT YET RUN`
Updated: 2026-06-16

This file defines how the lean six-module pipeline learns from historical cases.
It replaces the older 10-layer weighting idea.

---

## 0. Disease We Are Fixing

The old framework tended to:

- reward cheapness and information completeness too much;
- punish early asymmetric winners with `WATCH / 0%`;
- treat uncertainty as a veto instead of a position-size haircut;
- miss bottleneck winners when classic valuation looked uncomfortable;
- walk toward value traps when trailing earnings looked cheap;
- collapse new-money and existing-position decisions into one verdict.

The fix is not "add more research". The fix is to aggregate fewer, cleaner
signals into position size.

---

## 1. Module Signal Schema

Each module emits one signal:

```json
{
  "module": "M3 Profit Pool / Durability",
  "role": "context | conviction | risk | price | confidence",
  "signal": 0,
  "confidence": "low | med | high",
  "finding": "",
  "drivers": ["source_id"]
}
```

Signal scale:

```text
+2 strong positive
+1 mild positive
 0 neutral
-1 warning
-2 strong warning / veto candidate
```

---

## 2. Module Roles

| Module | Default Role | What It Should Control |
|---|---|---|
| M1 Evidence Spine | confidence | Size haircut, band width, source risk. |
| M2 Theme / Mechanism Thesis | context + conviction | Whether this is a real opportunity, dislocation, or bottleneck. |
| M3 Profit Pool / Durability | conviction | Whether the company captures and keeps the economics. |
| M4 Financial Reality | conviction or warning | Whether accounting confirms, distorts, or refutes the thesis. |
| M5 Inversion / Trap Test | risk or veto | Permanent loss, structural decline, false cheapness. |
| M6 Price / Position / Monitor | price + output | Buy-below, starter/add/trim zones, position delta. |

Important: M1 confidence does not mechanically cap verdict. It changes size and
required monitoring. This prevents "more research created more questions, so we
downgraded a winner to 0%" behavior.

---

## 3. Aggregation Model

```text
context = M2.context_label

conviction_raw =
  W[context].M2 * signal[M2] +
  W[context].M3 * signal[M3] +
  W[context].M4 * signal[M4]

risk_penalty =
  W[context].M5 * abs(min(signal[M5], 0))

if hard_veto(context, M5, M4):
  target_size = 0
else:
  conviction = conviction_raw - risk_penalty
  price_modifier = price_function(context, M6)
  confidence_haircut = confidence_function(M1)
  target_size = size_function(context, conviction, price_modifier, confidence_haircut)
```

The verdict is derived from target size:

| Target Size | New-Money Verdict |
|---:|---|
| 0% | `REJECT` or `WATCH` |
| 0.25%-1% | `WATCH / tracking` or very small `STARTER` |
| 1%-3% | `STARTER` |
| 3%-6% | medium position |
| 6%+ | `CORE`, only for rare high-confidence compounders |

Existing-position action:

```text
position_delta = target_size - current_position
```

This creates `ADD`, `HOLD`, `TRIM`, or `EXIT` without needing a separate
framework.

---

## 4. Context Gates

| Context | Price Role | Risk/Veto Rule | Positive Weight Emphasis |
|---|---|---|---|
| `quality_compounder` | modulator, not automatic veto | veto only if thesis durability breaks | M2, M3, M4 |
| `exceptional_bottleneck` | structured-entry modulator | valuation rarely hard veto; downside controls size | M2, M3, M4 |
| `cyclical_inflection` | use normalized mid-cycle economics | veto if balance sheet cannot survive cycle | M2, M4, M5 |
| `spinoff_forced_seller` | use normalized post-spin economics | veto if separation economics fail | M1, M2, M4 |
| `turnaround` | price matters heavily | veto if survival or execution path fails | M4, M5 |
| `structural_decline_trap` | mostly irrelevant after veto | M5 hard veto can set size to 0 | M5, M4 |
| `false_cheap_value_trap` | low multiple is not MOS | M4/M5 can veto trailing earnings | M4, M5 |
| `yield_or_balance_sheet_trap` | dividend yield not MOS | debt/capex/dividend fragility can veto | M4, M5 |

---

## 5. Starter Rules

The new design must allow small ownership when the setup is asymmetric.

`STARTER` can be justified even with incomplete evidence when all are true:

- M2 identifies a real dislocation, bottleneck, or forced update;
- M3 or M4 supports the mechanism;
- M5 does not show permanent impairment or balance-sheet death;
- M6 shows survivable downside at small size;
- M1 confidence is at least enough to know what would falsify the thesis.

This rule is specifically meant to catch cases like SNDK 2025 or NVDA 2023
where a classic full-MOS process may be too slow.

---

## 6. Trap Veto Rules

Hard veto can fire when:

- M3 shows profit-pool loss or moat erosion;
- M4 shows normalized earnings are far below trailing earnings;
- M4 shows capex, debt, dilution, or working-capital needs absorb owner earnings;
- M5 shows structural decline, permanent impairment, or management incentives
  that can destroy value;
- M6 shows downside is not survivable at even a small position.

This rule is meant to catch INTC, PYPL, DIS, PFE, yield traps, and false-low-P/E
stocks.

---

## 7. Scoring Fields

Each scored case writes one row to `results.csv`:

```text
pipeline_version,
weights_version,
case_id,
context_label,
mechanical_label,
target_size,
predicted_new_money_verdict,
predicted_existing_position_verdict,
correct_size_band,
size_distance_error,
veto_fired,
veto_expected,
dominant_module,
dominant_module_expected,
reasoning_score,
failure_tags,
notes
```

Failure tags:

```text
theme_missed
mechanism_missed
bottleneck_underweighted
profit_pool_misidentified
financial_reality_underweighted
trailing_accounting_trap
inversion_veto_missed
valuation_overweighted
valuation_underweighted
confidence_used_as_veto
too_small_missed_asymmetry
too_large_for_uncertainty
no_add_rule
no_trim_rule
hold_winner_failed
hindsight_leak
```

---

## 8. Weight Versioning

Use:

```text
weights/W_v<n>.json
CHANGELOG.md
results.csv
```

Each weight change must record:

```text
Change:
Mechanism reason:
Cases that motivated it:
Tuning error before:
Tuning error after:
Holdout error before:
Holdout error after:
Rejected alternatives:
```

Do not change weights after one case. A single case can create a hypothesis; it
cannot justify a framework patch by itself.

---

## 9. Anti-Overfitting Rules

- Early rounds are mechanism-guided calibration, not machine learning.
- Keep a holdout set.
- Do not tune every module independently with fewer than six cases per context.
- A change that only improves error but has no investment logic is rejected.
- A process that catches winners by buying every story is worse than the old
  process; trap precision must improve at the same time.
