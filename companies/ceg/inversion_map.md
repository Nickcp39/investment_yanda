# Inversion / Risk Map — CEG

Last updated: 2026-06-19

Source base: operator/inversion raw (S5, S7, S8), Calpine (S4, S11). "Invert" — how does the bull thesis die? Scores the 5 pre-registered kills from `step0_plan.md`.

## If I Wanted This Company To Fail

| Attack path | Mechanism | Evidence today | Early warning | Permanent damage? |
|---|---|---|---|---|
| **(a) FERC blocks co-location** | regulatory switch caps premium-PPA model | **DEFUSED** — 5-0 enabling order 2025-12-18; Crane front-of-meter (C015, C013) | hostile final PJM co-location definition | Low — was the scariest, now resolved |
| **(b) Power prices → PTC floor** | merchant margin compresses; upside gone | **LIVE but FLOORED** — ~$25/MWh to 2032; 2027 open ~$34/MWh (C019, C026) | open-year curves falling toward ~$25 | Low (floored) — compresses upside, not value |
| **(c) Calpine dilutive / over-levered / re-carbonizes** | leverage + purity drag re-rates whole entity | **PARTIAL TRIGGER** — purity 90%→58%; leverage→3.8x; mitigated by accretion + LS Power $5B (C023, C011, C024) | deleverage stalls; a divestiture slips; accretion under-delivers | **Medium–High** if deleverage stalls |
| **(d) PTC repealed** | downside floor removed | **NOT TRIGGERED** — survived OBBBA intact; FEOC-only (C019) | new legislation targeting §45U | n/a — resolved favorably |
| **(e) Shared switch: hyperscaler capex slope down** | demand leg of the thesis weakens (batch-common) | **ACCELERATING +77%** — ~$725B 2026 (C025) | 2027 capex guide *decelerates* | Medium (batch-wide) — kill not firing |
| **(*) Capped flagship + no new PPA** | Crane upside sold to MSFT; if no new PPA, equity is dead money at ~24x | Crane→MSFT contracted; **no confirmed new post-Meta PPA** (C013) | extended PPA drought + power softening | Medium — the real "quality trap" path |

## Risk Types

| Risk | Short-term volatility | Permanent impairment | Monitoring metric |
|---|---|---|---|
| Regulation / market structure | Med | **Low (a defused)** | PJM co-location definition; FERC compliance |
| Power-price / commodity | High | **Low (b floored)** | open-year power curves vs ~$25 floor |
| Balance sheet / integration | Med–High | **Med–High (c)** | net-debt/EBITDA; deleverage path; divestiture close |
| Demand / AI capex (shared) | High | Med (e) | hyperscaler 2027 capex guide |
| Re-rating / valuation | High | — | new-PPA catalyst; fwd P/E vs peers |
| Management / governance | Low | Low | clean (no super-voting); Calpine execution |

## Kill Criteria status (the 5 pre-registered, scored)

**Of 5 kills, 3 are DEFUSED (a, d, e), 1 is FLOORED (b), 1 is PARTIALLY LIVE (c).** The thesis does not die on the moat. The only genuinely live failure mode is **Calpine execution + no new PPA** — the "quality-at-a-fair-price trap."

- [x] **(a) FERC** → **DEFUSED** (5-0 enabling order; front-of-meter flagship). (C015, C013)
- [~] **(b) Power → floor** → **LIVE but FLOORED** (~$25/MWh to 2032; open priced ~$34). (C026)
- [⚠] **(c) Calpine** → **PARTIAL TRIGGER** (purity 90%→58%; leverage→3.8x; mitigated, not de-risked). (C023, C011, C024)
- [x] **(d) PTC repeal** → **NOT TRIGGERED** (survived OBBBA). (C019)
- [x] **(e) Shared switch** → **ACCELERATING +77%** to ~$725B — kill not firing. (C025)

## The 3 that matter most (ranked)

1. **(c) Calpine execution** — the only CEG-specific live risk: deleverage 3.8x→2.0x stalls, a divestiture slips, or accretion under-delivers. Arithmetic, not narrative. → TRIM trigger.
2. **(*) Capped flagship + no new PPA** — Crane's upside is sold to MSFT; if no *new* AI PPA signs and power softens, the equity is dead money at ~24x even with the moat intact. → the catalyst is the *next* PPA. → gates the UPGRADE.
3. **(a)-residual** — a hostile final PJM co-location *definition* (C016). Low probability after the 5-0 order; CEG's front-of-meter flagship is insulated; mainly an industry-BTM risk. → re-open watch.

## Disconfirming Evidence (what makes the bear case wrong)

- [ ] A **new** (post-Meta) hyperscaler PPA signs and is priced → primary re-rate catalyst; refutes the "capped/no-new-PPA" trap.
- [ ] Calpine deleverage reaches **~2.0x on/ahead of schedule** with LS Power cash in → kill (c) defused.
- [ ] Open-year power curves **hold above the ~$25 floor** through CEG's open years → kill (b) cushion confirmed.
- [ ] FERC's final PJM co-location definition lands **co-location-favorable** → kill (a) fully closed.

## So what

The two scariest tails (FERC, PTC) are empirically cut; demand is accelerating; the moat is durable. The case's failure mode is **narrow and specific** — Calpine execution + a flagship whose upside is already spoken for. That is exactly what the **STARTER** sizing (not back-up-the-truck) and the monitor triggers are built around. See `monitor.md`.
