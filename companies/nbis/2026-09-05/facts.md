# NBIS Facts (M1) — as_of 2026-09-05

**as_of_price 226.39** (close of Friday 2026-09-04, +7.5% on the day). Yahoo and stockanalysis agree
exactly, delta 0.00%.

> ## ⚠️ BASELINE CORRECTION
> This dossier was first built against `../2026-07-10/`. **That was the wrong baseline.**
> `../2026-08-12/` — a **Q2'26 EVENT RERUN** — already existed on `origin/main`, and the local repository
> was **29 commits behind** when this batch was run. Found by `git fetch` + `git log HEAD..origin/main`
> before pushing (commit `a1cc8e5`). Scope: **NBIS only** — verified that no 2026-08 dossier exists for
> NVDA / SNDK / MU / GEV. Logged as **INC-002**. This file is rebuilt against 08-12.

## What this run actually contributes: SOURCE GRADE

The 2026-08-12 card carried an explicit warning: **SEC EDGAR, nebius.com and businesswire were all blocked
by the environment's egress proxy**, so every Q2'26 figure was tagged `unverified_secondary`, and it noted
its own completeness was *lower* than 07-10, not higher.

**This run reached the SEC 6-K exhibit directly.** It **corroborates** the secondary numbers the prior
runner had to rely on:

| Line | 08-12 card (secondary) | This run (SEC 6-K, primary) | Agree? |
|---|---|---|---|
| Q2 revenue | $582.3M | $582.3M | ✅ |
| AI cloud revenue | $575M | $574.9M | ✅ |
| adj EBITDA | $236.2M | $236.2M | ✅ |
| ARR at end-June | $3.0B | $3.0B | ✅ |
| Q2 capex | $5.66B | ~$5.7B | ✅ |
| cash | $8.04B | $8.0B | ✅ |
| senior secured note | $775M @ SOFR+2.50% | $775M @ SOFR+2.50% | ✅ |
| contracted power | 5 GW | 5 GW | ✅ |

**That retires the source-grade penalty (M1 −1 → 0). It does not do more than that.**

## EVIDENCE carried from 2026-08-12 (still the richest read on this quarter)

RPO **$33.6B** (29% recognised within 24 months, 39% in 25–48 months) · four Q2 contracts averaging
**>$1B TCV each** · **revenue per MW rising from >$20M to a $40–50M/MW range on new signings** ·
cost of revenue down to **22.9%** of revenue from 29% · GAAP net loss **−$190.4M**, EPS **−$0.68** ·
Q2 OCF **+$2.25B** but capex **$5.66B** → quarterly FCF ≈ **−$3.41B** · cash and restricted cash **$9.10B** ·
PP&E **$13.05B** (YE2025 $5.55B) · **non-current liabilities $8.50B, doubled in one quarter from $4.10B** ·
FY26 revenue guidance **$3.0–3.4B reaffirmed, not raised**, despite the Q2 beat.

## THE FINDING THAT OUTRANKS ALL OF THE ABOVE

**Active MW is still not disclosed — a FOURTH consecutive quarter** (prior card C114 = OPEN).
The filing gives *contracted* capacity (5 GW) and *connected* guidance (800MW–1GW, **not raised**).
Neither is powered, revenue-producing MW. Three consecutive cards have named this as the proof metric.

## CONFLICTS — carried unresolved, plus one new

- **C110 (unresolved)** — deferred revenue basis: "increase of $3,200.6M to $4,778.1M" vs "current +
  non-current from $1.58B to ~$5.98B". About $1.2B apart. This run did not reach the line item.
- **C111 (unresolved)** — whether Q2 moved NBIS into net debt. Nominal cash $9.10B vs non-current
  liabilities $8.50B implies net cash of about +$0.6B, contradicting sources claiming net debt.
  **This directly affects the EV used in valuation** — both bases are shown in `model/scenario_model.csv`.
- **C-NEW-ATM (new, unresolved)** — the 08-12 card records the ATM as **UNDRAWN**. This run's read of the
  6-K reports **ATM proceeds $2.8B from 12.7M Class A shares at a $223.6 average**, 12.3M remaining.
  **NOT resolved in this card's favour.** Both could be partly right if the issuance postdates the prior
  card, and a $223.6 average is consistent with sales spanning the mid-August spike. Because it is
  unresolved it is **NOT used to fire K-C**; the prior card's reframing toward the debt/leverage branch
  is adopted instead. Must be settled against the primary filing before it influences sizing.

## Price context

| | |
|---|---|
| as_of price | **226.39** |
| prior card's stated price | ~$215–220 (**flagged stale in that card**) |
| actual close 2026-08-13 | **$254.40** (intraday $208.40–262.34) → **−11.0%** to today |
| 52-week range | $63.26 – $299.86 → **−24.5% off the 52-week high** |
| market cap | $62.05B (274.10M shares) |
| no-chase zone (from 08-12) | **≥ $250** — breached at $254.40 on 08-13; **226.39 is not in it** |
