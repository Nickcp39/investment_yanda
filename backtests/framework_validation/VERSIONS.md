# Pipeline & Weights Version Registry

**Single source of truth** for `pipeline_version` and `weights_version`. Every case run MUST stamp the
**current active ids** (below) onto BOTH:
1. its `decision_card.json` — at **lock time** (provenance on the decision itself), and
2. its `results.csv` row — at **score time** (and the two MUST match).

> **Guarantee rule (provenance):** a run whose `pipeline_version` + `weights_version` are not recorded on its card **is
> void / non-comparable** and must be re-stamped or re-run. Versions are how we keep cases comparable as the
> pipeline evolves — never compare two cases without first checking they ran under the same ids (or noting they didn't).
>
> **Guarantee rule (freshness, v1.1):** a run without a committed `freshness_check.json` (`status==PASS`) from
> `scripts/verify_freshness.py` is **void / non-comparable** — same standing as a missing version stamp. LIVE data
> (price, market cap, 52-week band, shares, plus export-control / litigation / guidance) is re-verified against
> **≥2 independent sources every run**; a date-only "looks current" check is not sufficient (this is what INC-001
> defeated). Control/integrity guarantees like this one go **ACTIVE on commit** — they are NOT `PATCH_LEDGER.md`
> weighting hypotheses and do NOT wait for the 8-case gate.

---

## Current ACTIVE — stamp these on every NEW run

| field | value |
|---|---|
| `pipeline_version` | **`lean-6module-v1.1`** |
| `weights_version` | **`none`** (no numeric weights file yet; Runner reasons qualitatively per `WEIGHTING_HARNESS.md` + `METHODOLOGY.md`) |

> **v1.1 (2026-06-21)** adds ONE thing to v1: a **mandatory mechanical data-freshness gate** (`scripts/verify_freshness.py`
> + per-dossier `freshness.json` manifest + LIVE/FILED decay axis in `sources/source_policy.md`). Runner conviction/weighting
> logic is UNCHANGED. The 13 v1 blind cases are **not** re-run (see "don't retro-restamp"); v1.1 applies to NEW runs + the
> NVDA 2026-06-20 pilot. Motivated by **INC-001** (`INCIDENTS.md`).

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
| `lean-6module-v1` | `none` | 2026-06-17 → 2026-06-21 | the redesigned **blind 6-module sequential** run (`TEST_PLAN.md`) | **all 13 blind cases** (the 10-case validated set + `mu`/`nbis`/`sndk` re-run from v0 on 2026-06-19) |
| **`lean-6module-v1.1`** | **`none`** | 2026-06-21 → present | v1 **+ mandatory mechanical freshness gate** (`verify_freshness.py` + `freshness.json` + LIVE/FILED axis); conviction logic unchanged | NVDA `2026-06-20` (corrected pilot); all NEW runs from 2026-06-21 |

> Legacy `v0` cases keep their own id — **do not retro-restamp them to v1.** They ran under a genuinely
> different pipeline; the id difference is correct, not drift to be "fixed."

---

## Pending bumps (NOT active — gated in `PATCH_LEDGER.md`)

| patch | would become | trigger |
|---|---|---|
| **P1** — governance discount: within-band, operator-conditioned, counted once | `pipeline_version` → **`lean-6module-v1.2`** | P1 validated (META + DIS) and flipped to ACTIVE |

> **Note:** P1 originally targeted `v1.1`, but `v1.1` was taken by the 2026-06-21 freshness gate (a control fix that
> activated first). P1 now targets **`v1.2`**. This is fine: control/integrity fixes and weighting patches share the
> same minor-version number line, allocated in activation order.

When P1 activates: bump the **Current ACTIVE** block to `lean-6module-v1.2`, add a History row, and from that
point new runs stamp `v1.2`. Cases already scored under `v1` / `v1.1` are **not** re-run — they stand as the baseline
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
- **2026-06-21** — **`lean-6module-v1.1`**: activated the mandatory mechanical **data-freshness gate**
  (`scripts/verify_freshness.py` + per-dossier `freshness.json` + LIVE/FILED decay axis in `sources/source_policy.md`;
  `CHECKER.md §4` hardened from a human checkbox to a script that must exit 0). A **control/integrity fix → ACTIVE on
  commit** (not a `PATCH_LEDGER.md` weighting hypothesis; no 8-case gate). Motivated by **INC-001**: `companies/nvda/`
  (as_of 2026-06-19) used $145.48 (≈ the 52-week low $142.03) as the current price; real close $210.69 — a 45% error
  that flipped base 5y IRR +13%→+4.8% and verdict STARTER→WATCH while the Checker stamped CLEAN. Corrected run lives at
  `companies/nvda/2026-06-20/` (passes the gate); the flawed run is preserved at `companies/nvda/2026-06-19/` (BLOCKs the
  gate) as the error sample. The 13 v1 cases are **not** re-run. **Note:** v1.1 is taken by this freshness gate, so the
  pending **P1** governance patch, when it activates, now targets **`v1.2`** (see Pending bumps).
- **2026-06-21** — **freshness gate extended to all 13 backtest cases + the 6 remaining live dossiers** (still v1.1).
  Added `verify_freshness.py --mode backtest` (nominal price = `raw_close × post-as_of split factor`, recovering
  pre-split prices: NVDA 2023-05-25 ×10 = $379.80, AAPL 2016 ×4 = $90.34) and a **T7 no-lookahead** tripwire (every
  source `public_date ≤ as_of`). **All 13 backtest cases reconcile to the penny and PASS**; T7 caught one real
  post-as_of source (S013) in `amzn_2023-02-03`, now removed. The **live sweep** found only NVDA's price was wrong —
  aapl/amzn/googl/meta/msft/tsla prices were all correct (MSFT's STARTER stands; NVDA is WATCH), with 3 stale
  qualitative items corrected (GOOGL/META legal, MSFT OpenAI). No decision-card numbers, verdicts, or outcome scores
  changed; the 13 v1 case decisions stand.
