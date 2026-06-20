# Pipeline & Weights Version Registry

**Single source of truth** for `pipeline_version` and `weights_version`. Every case run MUST stamp the
**current active ids** (below) onto BOTH:
1. its `decision_card.json` — at **lock time** (provenance on the decision itself), and
2. its `results.csv` row — at **score time** (and the two MUST match).

> **Guarantee rule:** a run whose `pipeline_version` + `weights_version` are not recorded on its card **is
> void / non-comparable** and must be re-stamped or re-run. Versions are how we keep cases comparable as the
> pipeline evolves — never compare two cases without first checking they ran under the same ids (or noting they didn't).

---

## Current ACTIVE — stamp these on every NEW run

| field | value |
|---|---|
| `pipeline_version` | **`lean-6module-v1`** |
| `weights_version` | **`none`** (no numeric weights file yet; Runner reasons qualitatively per `WEIGHTING_HARNESS.md` + `METHODOLOGY.md`) |

---

## Convention — when does each id bump?

- **`pipeline_version` = `lean-6module-v<MAJOR>[.<MINOR>]`** — the Runner **logic**: the six modules, the
  gates, and the aggregation / durability-ceiling **rules**.
  - **MINOR bump** (`v1` → `v1.1`) = a rule refinement, e.g. activating a `PATCH_LEDGER.md` item.
  - **MAJOR bump** (`v1` → `v2`) = a module add/delete or structural change. *(Adding length is discouraged —
    most changes are modify/delete = minor bumps.)*
- **`weights_version` = `W_v<n>.json` | `none`** — the **numeric weights file only**. Bumps when numbers change.
- A change may bump one or both. **Every bump is recorded in the History table below + cites its motivating cases.**

---

## Registry — id → contents → cases

| `pipeline_version` | `weights_version` | active dates | what it is | cases run under it |
|---|---|---|---|---|
| `lean_six_module_v0` | `W_v0` | 2026-06 (pilot) | first-draft lean **pilot**, *self-run* — NOT the blind sequential protocol | `sndk_2025-06-16`, `nbis_2026-01-01`, `mu_2025-03-21` (self-run) |
| **`lean-6module-v1`** | **`none`** | 2026-06-17 → present | the redesigned **blind 6-module sequential** run (`TEST_PLAN.md`) | **all 13 blind cases** (the 10-case validated set + `mu`/`nbis`/`sndk` re-run from v0 on 2026-06-19) |

> Legacy `v0` cases keep their own id — **do not retro-restamp them to v1.** They ran under a genuinely
> different pipeline; the id difference is correct, not drift to be "fixed."

---

## Pending bumps (NOT active — gated in `PATCH_LEDGER.md`)

| patch | would become | trigger |
|---|---|---|
| **P1** — governance discount: within-band, operator-conditioned, counted once | `pipeline_version` → **`lean-6module-v1.1`** | P1 validated (META + DIS) and flipped to ACTIVE |

When P1 activates: bump the **Current ACTIVE** block to `lean-6module-v1.1`, add a History row, and from that
point new runs stamp `v1.1`. Cases already scored under `v1` are **not** re-run — they stand as the `v1` baseline
the patch is measured against.

---

## History / changelog

- **2026-06-17** — `lean-6module-v1` established (blind sequential protocol; weights `none`). Supersedes the
  `lean_six_module_v0` pilot for all NEW cases.
- **2026-06-19** — back-stamped `googl_2024-06-14` (case 1) with `lean-6module-v1` / `none` / run_date 2026-06-19
  (the blind Runner had omitted the provenance fields; `decision_card.json` now carries them). Provenance made
  mandatory in `PROTOCOL.md §4`.
- **2026-06-19** — completed the **v0-pilot backfill**: `sndk` / `nbis` carried `pipeline_version` only and
  `mu` carried none; all three now stamp full `lean_six_module_v0` / `W_v0` / `run_date` (= card creation date).
  Note: `W_v0` and `none` are both **qualitative labels — no numeric weights JSON exists for either era** — they
  only mark pilot (v0) vs blind-sequential (v1). All four run cases are now fully version-stamped.
- **2026-06-19** — back-stamped `intc_2021-04-23` + `intc_2024-08-02` (run before §4 provenance was mandatory)
  with `lean-6module-v1` / `none` / run_date 2026-06-19. **All 13 decision cards now carry version stamps**
  (10 × `lean-6module-v1` blind set, 3 × `lean_six_module_v0` pilot).
- **2026-06-19** — **re-ran `mu` / `nbis` / `sndk` under `lean-6module-v1`** (the 3 v0 pilots). Each: the v0 work
  archived to its own `_v0/` subfolder (**NOT** restamped — honoring the "don't retro-restamp" rule above), then a
  fresh blind run added `operator_background` + an independent checker pass + a v1 `decision_card` + `outcome_score`.
  **All 13 cases now scored under `lean-6module-v1`** in `results.csv` (the v0 cards remain in `_v0/` as the
  superseded baseline). ⚠ `mu` / `nbis` / `sndk` outcomes are **PROVISIONAL** (short as-of windows ~15 / ~5.5 / ~12 mo
  + high recent-date training-leakage risk) — weight them lightly vs the 10-case set.
