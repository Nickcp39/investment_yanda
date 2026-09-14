# NBIS Decision Card — as_of 2026-09-05 (RE-PRICE + SOURCE UPGRADE)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-09-05
**batch** memory_ai_refresh_2026-09-05 · **status** DECISION_DRAFT · **completeness** ~70%
**refresh_of** `companies/nbis/2026-08-12` (Q2'26 EVENT RERUN)
**context_label** `hypergrowth_neocloud_repriced_only_proof_metric_still_open_for_a_fourth_quarter`

> ## ⚠️ BASELINE CORRECTION — read first
> This card was first built against `../2026-07-10/`. **Wrong baseline.** `../2026-08-12/` already existed
> on `origin/main`; the local repo was **29 commits behind** when the batch ran. Caught by `git fetch` +
> `git log HEAD..origin/main` before pushing. **Scope: NBIS only** (no 2026-08 dossier exists for NVDA /
> SNDK / MU / GEV). Logged as **INC-002**.
>
> The first draft also claimed to be **withdrawing a "warming toward STARTER" flag**. That flag was already
> dropped by the 08-12 card. **No credit is claimed for it.**

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **226.39** (2026-09-04 close; 2 sources, delta 0.00%) |
| market cap | ~$62.05B (274.10M shares) |
| vs prior card's real reference close ($254.40, 2026-08-13) | **−11.0%** |
| distance from 52-week high $299.86 | **−24.5%** |
| business_verdict | **good** (unchanged, three cards) |
| **new_money_verdict** | **WATCH (0%)** — third consecutive |
| existing_position_verdict | **HOLD** (the one name the book already holds) |
| suggested initial / max size | **0% / 4%** |
| **buy_below** | **$150–180 UNCHANGED** (three cards) |
| **no_chase_zone** | **≥ $250** (carried from 08-12) — not currently triggered; **breached at $254.40 on 08-13** |
| binding_constraint | **PRICE (26–51% above band) + active MW open a FOURTH quarter** |

## Six-module signals (net −1) — baseline is 08-12, not 07-10

| Module | Role | 07-10 | **08-12** | **09-05** | One line |
|---|---|---:|---:|---:|---|
| M1 Evidence Spine | confidence | 0 | **−1** | **0** | ⭐ **the only leg this run moves** — primary 6-K reached; corroborates the prior card's secondary figures |
| M2 Theme / Mechanism | context | +1 | +1 | **+1** | Contracted 4→5 GW; four Q2 deals >$1B TCV; RPO $33.6B. But connected guidance **not** raised |
| M3 Profit Pool / Durability | conviction | 0 | **+1** | **+1** | Revenue per MW **$20M → $40–50M** on new signings — commoditisation contradicted by transacted price |
| M4 Financial Reality | conviction | −1 | **0** | **0** | adj EBITDA +$236.2M (40.6%) vs −$21.0M PY; cost of revenue 29% → 22.9%. But quarterly FCF ≈ −$3.41B |
| M5 Inversion / Trap | risk | −2 | −2 | **−2** | Commoditisation leg cooled; **leverage leg hot** — non-current liabilities $4.10B → $8.50B in one quarter |
| M6 Price / Position | price | −1 | −1 | **−1** | $226.39 still 26–51% above band; below the ≥$250 no-chase line |

## What this run actually contributes

The 08-12 card carried a source-grade warning: **SEC EDGAR, nebius.com and businesswire were all blocked**
by the environment's egress proxy, so every Q2'26 number was `unverified_secondary` with two unresolved
conflicts. **This run reached the SEC 6-K directly and it corroborates those figures** — revenue $582.3M,
AI cloud $574.9M, adj EBITDA $236.2M, ARR $3.0B, capex ~$5.7B, cash $8.0B, the $775M facility, 5 GW
contracted. **That is worth exactly one module notch (M1 −1 → 0) and nothing more.**

## Conflicts — two carried, one new

- **C110** deferred revenue basis (~$1.2B apart) — **unresolved**, line item not reached.
- **C111** whether Q2 moved to net debt — **unresolved**, and it changes EV by ~12%. Both bases are shown
  in `model/scenario_model.csv` rather than picking the flattering one.
- **C-NEW-ATM** — 08-12 records the ATM as **undrawn**; this run's 6-K read reports **$2.8B / 12.7M shares
  at $223.6 avg**, 12.3M remaining. **NOT resolved in this card's favour** — both could be partly right if
  the issuance postdates the prior card. Therefore **not used to fire K-C**; the prior card's reframing
  toward the debt/leverage branch is adopted instead.

## Kill criteria (carried from 08-12, with status)

**K-A** active MW undisclosed — 🟡 **half-resolved, still open**: ARR *accelerated* $1.92B → $3.0B, but
active MW is absent a **fourth** consecutive quarter · **K-B** anchor risk — 🟢 cooled ($46B base intact +
four >$1B TCV deals) · **K-C** prepayment → dilution — **reframed at 08-12**: the original wording misses
the middle state, **debt**; see C-NEW-ATM · **K-D** rev/MW declining — 🟢 **counter-evidenced, it is rising** ·
**K-E** capex $31–35B without conversion — 🟢 **falsified** ($20–25B, low end) · **K-F** concentration /
ICFR — ⬜ undeterminable · **K-G** 🆕 **leverage branch** (non-current liabilities doubled, first
asset-backed note, $3.75B convertible plan) — 🟡 active monitor · **K-VAL** — 🔴 **standing**.

## WATCH → STARTER trigger (unchanged, three cards)

**(1)** price below ~$180, **AND (2)** active MW actually disclosed. Near-term falsifiable test: ARR
**$3.0B → $7–9B** by year-end (**2.3x–3.0x in six months**); Q3 2026 is the checkpoint. Note FY26 revenue
guidance was only **reaffirmed** at $3.0–3.4B despite the Q2 beat.

## runner_dissent

**An error of my own first.** I built this card against 07-10 when 08-12 already existed on origin, because
the local repo was 29 commits behind and I did not fetch before running the batch. The first draft then
claimed to withdraw a "warming" flag the 08-12 card had already dropped — I was about to take credit for
someone else's judgement. Logged as INC-002.

**Substantively:** the 08-12 card is in several ways **better than this one**. It has RPO, revenue per MW,
cost ratios and the leverage analysis I did not independently reproduce. The one place this run adds value
is source grade. That is one notch, not a verdict.

**And the verdict should not move.** The proof metric has now been absent for **four straight quarters
while the stock compounded** — that is the pattern that should make a buyer *more* patient, not less.
