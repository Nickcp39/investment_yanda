# Incidents Ledger — control/integrity failures + their fixes

This is the standing log of **control/integrity incidents** (a wrong/stale INPUT slipped a gate), kept
**separate from** [`PATCH_LEDGER.md`](PATCH_LEDGER.md) (which stages *weighting/judgment* hypotheses behind an
8-case gate). The distinction matters:

- **Weighting patch (PATCH_LEDGER):** "should this risk move conviction more/less?" — tune-prone, so it waits
  for ≥8 cases or ≥3 same-pattern failures before going ACTIVE. Changing it tunes outcomes to one realization.
- **Control/integrity fix (INCIDENTS, this file):** "a wrong *input* passed a gate." — NOT tune-prone; the
  failure mode is logically certain to recur if unfixed. These go **ACTIVE on commit** (same standing as the
  `VERSIONS.md` provenance guarantee rule). One case is enough; you do not need 8 wrong prices to know that a
  single-source + date-only check can be fooled.

---

## INC-001 — NVDA stale price passed a CLEAN gate (2026-06-21)

**Status:** FIXED → `lean-6module-v1.1` ACTIVE on commit.

### Symptom
`companies/nvda/` (as_of 2026-06-19) shipped current price **$145.48** — which is approximately the **52-week
LOW ($142.03)**. The real last close was **$210.69** (Yahoo + stockanalysis + websearch all agree). The runner
had grabbed an *extreme of the price series* (the min) instead of the *last close ≤ as_of*.

### Impact (verdict-flipping)
The price is the literal denominator of the IRR (`model/scenario_model.csv`: `IRR = (per_share_year5/price_now)^(1/5)-1`):

| metric | shipped ($145.48) | true ($210.69) |
|---|---|---|
| market cap | $3.55T | $5.14T |
| forward P/E | ~19x | ~28x |
| starting OE yield | 5.1% | 3.5% |
| **base 5y IRR** | **+13%** | **+4.8%** (< 8% hurdle) |
| distance off 52wk high | −38% | −11% |
| **new-money verdict** | **STARTER ("price-friendly", #1 in the batch)** | **WATCH (no margin of safety)** |

A 45% price error flipped the verdict AND corrupted the *qualitative* narrative ("near 52-week low", "low-price
buyback", "bearish sentiment, market pricing a top" — all false at $210.69, which is near the highs).

### Root causes
1. **Freshness gate was a human checkbox.** `CHECKER.md §4` asked the Checker to confirm "no obviously stale
   number is treated as current." For NVDA the Checker only verified the price's *date* (≤ as_of) and that the
   (wrong) value was *internally consistent* across 6 files — it never re-fetched the *value*. (For GOOGL the
   same Checker *did* re-pull 3 Yahoo closes — so execution was inconsistent because it was judgment, not a
   mandatory mechanical step.)
2. **Single source + date-only.** Price came from one source (S006 Yahoo, tier B1), "verified" by its date label.
3. **tier ≠ decay-rate.** The China export-control status was tier A2 (primary) but LIVE (fast-decaying); the
   system conflated "primary source = trusted = no recheck" with freshness, so a stale "China permanent loss"
   framing also rode through (the USG had reinstated an H200 license in 2026-02).
4. **No date-keyed folders.** Flat `companies/<ticker>/` means a re-run silently overwrites; two as_of runs
   cannot coexist.

### Fix (lean-6module-v1 → v1.1, control fix, ACTIVE on commit)
- **`scripts/verify_freshness.py`** — mechanical gate: independently re-fetches the last close ≤ as_of (reusing
  `scripts/market_data_download.py:fetch_yahoo`), cross-checks the card value vs ≥2 independent sources, runs
  structural tripwires (incl. **T2 "current ≈ 52wk low/high"** — which fires on exactly this case), and **exits
  non-zero to BLOCK**. A dossier cannot be CLEAN without a committed `freshness_check.json` (`status==PASS`).
- **`freshness.json`** per-dossier manifest — every LIVE datum with ≥2 independent sources.
- **LIVE/FILED decay axis** added to `sources/source_policy.md` (orthogonal to the A1–E1 tier axis).
- **`CHECKER.md §4`** hardened: soft checkbox → mandatory `verify_freshness.py` PASS; Checker may not override.
- **`PROTOCOL.md §4`** + **`VERSIONS.md`**: freshness guarantee rule (no PASS = void/non-comparable).
- **Date-keyed folders**: `companies/<ticker>/<as_of>/`.

### Verification (reproducible)
```
python scripts/verify_freshness.py --dossier companies/nvda/2026-06-19   # -> BLOCK, exit 1 (price 145.48 vs ~210.69; T2 low-hug)
python scripts/verify_freshness.py --dossier companies/nvda/2026-06-20   # -> PASS,  exit 0 (3 sources agree; T1-T5 green)
```
- `companies/nvda/2026-06-19/` — the flawed run, **preserved as the error sample** (its `freshness_check.json` BLOCKs).
- `companies/nvda/2026-06-20/` — the corrected run (price $210.69, verdict WATCH, China = recoverable H200 optionality).

### Follow-through (completed 2026-06-21)
- **Live 6-dossier sweep — DONE.** aapl/amzn/googl/meta/msft/tsla re-verified against ≥2 real sources, migrated to
  date-keyed folders, each with `freshness.json` + a committed PASS. **Price result: only NVDA was wrong; the other
  6 prices were all correct (0.0% delta across 3 sources).** The single-source method happened to grab the right
  last close for them — the gate now removes the "happened to." **3 had STALE LIVE-qualitative items, corrected:**
  GOOGL (DOJ search remedy *finalized 2025-09 — keeps Chrome*, not the structural-divestiture tail the dossier
  implied), META (Boasberg *2025-11 ruled NOT a monopoly*, no IG/WhatsApp spin-off; the dossier said "no recent
  ruling"), MSFT (Microsoft–OpenAI relationship *restructured 2026-04-27*, treated as an unexamined black box).
  **Headline resolved: only MSFT is a STARTER** (price correct, +MOS, base 10y IRR ~9.5%); NVDA, the prior #1, is WATCH.
- **Backtest 13-case retrofit — DONE.** `verify_freshness.py` gained **`--mode backtest`** (nominal =
  `raw_close × cumulative split factor`, recovering pre-split prices: NVDA 2023-05-25 $37.98×10 = $379.80, AAPL 2016
  $22.58×4 = $90.34) + **T7 no-lookahead** (every source `public_date ≤ as_of`). All 13 reconcile to the penny; all
  PASS. **T7 caught a real leak:** `amzn_2023-02-03` carried a post-as_of source (S013 dated 2023-02-09 > as_of
  2023-02-03) — a narrative-only/fenced row the case's own `material_audit.md` had flagged for removal; now removed.
  The two ~0.78% deltas (googl/meta) are StatMuse-vs-Yahoo close-source differences, sub-1%, reconciling to card mcap.
  No decision-card numbers, verdicts, or outcome scores changed.
