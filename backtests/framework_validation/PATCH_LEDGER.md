# Patch Ledger — staged framework changes (pending validation)

Status rule (`PROTOCOL.md §9` + `WEIGHTING_HARNESS.md §8/§9`): **a single case creates a HYPOTHESIS,
not a mandate.** Proposed changes accumulate here with a mechanism reason + *pre-registered, falsifiable
predictions*, and flip to **ACTIVE** only after the gate is met (≥8 cases scored, or ≥3 cases showing the
same failure pattern, each with a mechanism reason). **Nothing here changes live Runner behavior until its
`Status:` flips to ACTIVE.** This file is how we avoid tuning to one realization.

| id | title | opened | status | activation gate |
|---|---|---|---|---|
| P1 | Governance/control discount: within-band + operator-conditioned, counted once | 2026-06-19 | **PROPOSED (inactive)** | META + DIS confirm the predictions below |

---

## P1 — Governance/control discount: within-band, operator-conditioned, counted once

- **Status:** PROPOSED — **INACTIVE**. Live Runner behavior UNCHANGED.
- **Opened:** 2026-06-19
- **Motivating case:** `googl_2024-06-14` — WINNER **+116% t.r. vs SPY +42%**; score **PASS, size-distance 1**.
  The *only* deduction: ceiling capped at **12% (Confirmed)** vs the **15–25% (Core)** the winner earned.
- **Class of fault:** the **durability-ceiling logic** — *not* the M2/M3/M4 conviction weights (those +1s were honest at as-of).

### Symptom
A **4/5-operator, growing-pool, net-cash franchise** — a name `METHODOLOGY.md §2` itself lists as a Core
holding — was demoted a **full tier** (Core → Confirmed) by the founder-control/governance discount. That
discount was the **one as-of risk that proved value-irrelevant**: the control bloc *backed* the exact capex
that re-rated the stock 2.1×, while raising the dividend and buying back $45.7B.

### Two mechanism faults (both fixable without lengthening the pipeline)
1. **Triple-count (a DELETE, not a new module).** The single "founder control" risk was penalized in **three**
   places at once — **M3** (durability pulled +2→+1), **M5** (listed in the −1 risk set), and the **durability
   ceiling** (12% cap). No rule enforces *"one risk, one module."*
2. **Wrong functional form (a MODIFY of how the discount enters).** The discount acts as a **tier demotion**
   and is applied **largely independent of operator grade**. Governance-control risk and operator quality are
   the *same axis*; a high operator grade should **largely neutralize** the control fear, not sit beside it.

### Proposed rule (refines the qualitative ceiling logic in `METHODOLOGY.md §2`)
- **Single-count rule.** Each risk is scored in **exactly one** module. The durability ceiling *reads* the
  operator/governance grade but does **not** re-penalize a control risk already expressed in M3 or M5.
- **Within-band, operator-conditioned discount.** A governance/control discount lowers the ceiling **within**
  the band the name otherwise earns, **scaled by operator life-arc grade**:
  - operator **≥4/5** → discount is *small*: shave Core-high → Core-low (e.g. 25% → ~15%); **do NOT exit Core**.
  - operator **3–3.5/5** → discount may pull **Core → Confirmed** (one tier).
  - operator **≤2.5/5** → discount may demote **>1 tier** and/or stack with M5 (control becomes a real kill-risk).

### Pre-registered, falsifiable predictions (this is the anti-overfit test — write it BEFORE running the cases)
- **META `2022-11-10`** (founder-control **3/5**, winner): under P1 sizes **≥ Confirmed-high** (vs ~Confirmed
  under current logic). If P1 does **not** raise META's size → **WEAKEN** P1.
- **DIS `2021-11-11`** (operator **2.5/5**, trap): under P1 stays **≤ Confirmed / WATCH** and is **not** upsized.
  If P1 **upsizes DIS** → **REFUTE** P1 (it would just be an overfit ceiling-bump).
- **Global guard:** P1 must **not** improve winner-capture at the cost of trap precision (`WEIGHTING_HARNESS.md §9`).

### Rejected alternative
**Blanket-raise the `quality_compounder` ceiling weight** → REJECTED. A scalar bump would upsize *weak-operator*
founder-controlled names (the DIS-type trap), breaking trap precision. The discount must be **conditional on
operator grade**, not a constant.

### Activation
Flip `Status:` to **ACTIVE** (and record before/after tuning + holdout error per `WEIGHTING_HARNESS.md §8`)
only after META + DIS — ideally + one more founder-control case — confirm the predictions. **Until then:
Runner behavior is unchanged; GOOGL's locked decision and score stand as-is.**
