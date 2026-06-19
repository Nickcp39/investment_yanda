# Valuation / Margin Of Safety — CEG

Last updated: 2026-06-19 · Price **$274.06**

Source base: market data (S9), guidance (S3), §45U floor (S7). Numbers are forward adj-EPS × multiple triangulation + peer/Street cross-check — **not** an owner-earnings DCF (combined-entity FCF not cleanly reported post-Calpine; hedge ratios undisclosed — see `financials/financial_quality.md`). Multiples are aggregator-sourced (stockanalysis.com), treat as ±.

## Current Setup

| Item | Value | claim_id |
|---|---|---|
| Share price | **$274.06** (2026-06-19) | C027 |
| Market cap | ~$98B | C027 |
| Enterprise value | ~$120B | C027 |
| Fwd P/E | **~24x** | C027 |
| EV/EBITDA | ~15x | C027 |
| FCF yield | ~1.2% | C027 |
| 52-wk high | $413 → de-rate **−34%** | C027 |

## Why not an owner-earnings DCF

Trailing FCF (~$1.3B FY2025) is modest, **standalone**, and pre-Calpine; the combined-entity FCF is not cleanly reported yet (the +64% Q1'26 revenue is an acquisition artifact); and hedge ratios are undisclosed. A 10-yr DCF would be false precision. The defensible anchor is **forward adjusted-operating-EPS × a terminal multiple**, bracketed by merchant peers and the franchise premium, cross-checked against Street targets. That triangulation *is* the valuation conclusion.

## Multiples + peer comp

| Name | Fwd P/E | Note |
|---|---:|---|
| **CEG** | **~24x** | Premium: scale + nuclear CF + AI-PPA optionality + §45U floor |
| VST (Vistra) | ~16x | Merchant peer |
| TLN (Talen) | ~17–18x | Merchant peer (original BTM/AWS co-location case) |
| NRG | ~18x | Merchant peer |

CEG's ~24x is a **~6–8 turn premium** to the merchant set, **compressed from >35x at the $413 high.** The bull defends the premium on the un-buildable nuclear moat + the contracted, PTC-floored PPA annuity; the bear says ~17x is the right merchant multiple.

## Analyst targets

Range **$300–390**, median **~$370**: Mizuho $300, KeyBanc $321, Barclays $358, UBS $388. **Even the lowest Street target ($300) sits above the current $274** — the sell-side reads the de-rate as overshooting. (C028)

## Scenarios (adj-EPS × terminal P/E)

See `model/scenario_model.csv` (implied prices reconciled to these ranges).

| Scenario | Path | EPS × multiple | Value | vs $274 |
|---|---|---|---|---|
| **Bear** | Calpine deleverage stalls, no new AI PPA, power softens toward floor, multiple → merchant ~17–18x | ~12.0 × ~18x | **~$200–230** | ~−20% |
| **Base** | Crane delivers 2027, Calpine accretes + deleverages, 1–2 new PPAs, premium ~24–25x holds | ~13.0 × ~25x | **~$300–340** | ~+20–25% |
| **Bull** | Multiple premium PPAs + uprates + 2nd restart, leverage → 2x, ~30x | ~13.8 × ~30x | **~$400+** | ~+50% |

**Asymmetry from $274: ~−20% bear / ~+20–25% base / ~+50% bull — the best risk/reward of the GEV/VRT/CEG batch.**

## The floor logic (why the bear is shallow)

The **§45U PTC (~$25/MWh to 2032)** backstops the power-price downside; 2027 open nuclear is priced **~$34/MWh**, above the floor. (C019, C026) So the bear is a **multiple compression (24x → 17–18x) on an *intact* franchise**, not an earnings collapse. That makes the downside bounded and shallow relative to the bull — a legislated margin of safety that most merchant generators lack.

## Margin Of Safety

| Required return | Buy below | Hold / starter | Trim/Avoid above |
|---|---|---|---|
| ~10–12%/yr (durable moat, PTC-floored, but post-Calpine leverage + capped flagship) | ≈ **<$230–250** (bear-ish multiple, moat intact → back up the truck) | **~$250–300** (STARTER; the current $274 sits here) | ≳ **$370+** (Street median; reassess vs froth) |

**At $274 the stock is a *quality-at-fair-price pullback*, not deep value.** The −34% restored a margin of safety **vs its own froth**, not vs absolute value (~24x > 16–18x peers). The skew is favorable (shallow floored bear, solid base, strong bull) and the whole Street sees $300+. This supports a **STARTER** now, scaling on (a) a confirmed *new* hyperscaler PPA, or (b) weakness toward $230–250.

## Valuation discipline notes

- A genuinely durable moat can still be only a *fair* forward investment at ~24x — pay for it as a starter, not a layup.
- Do not let a 30x bull multiple rescue the present; ~24x already embeds a premium.
- Post-Calpine leverage and combined FCF are **estimates** pending the Q1'26 10-Q — the multiples carry a ± until then. (C011)
- The single biggest upside swing is the **next PPA price** (Crane's is locked to MSFT and undisclosed). (C013)

→ Position implication is in `memo-v1.md` (STARTER + sizing); triggers in `monitor.md`.
