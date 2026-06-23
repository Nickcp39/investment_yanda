# Valuation / Margin Of Safety — CEG

Last updated: **2026-06-22** · Price **$277.64**

Source base: market data (S9/S15, 2026-06-22), guidance (S2), §45U floor (S7), analyst targets (S16). Numbers are forward adj-EPS × multiple triangulation + peer/Street cross-check — **not** an owner-earnings DCF (combined-entity FCF not cleanly reported post-Calpine; hedge ratios undisclosed — see `financials/financial_quality.md`). Multiples are aggregator-sourced; treat as ±.

## Current Setup (LIVE 2026-06-22)

| Item | Value | claim_id |
|---|---|---|
| Share price | **$277.64** (2026-06-22, Yahoo daily-close ≤ as_of; 3 sources within 0.21%) | C027r |
| Market cap | ~$100.3B (361.19M sh × $277.64) | C027r |
| Enterprise value | ~$120B | C027r |
| Fwd P/E | **~24x** (on FY26 guide midpoint $11.50) | C027r |
| EV/EBITDA | ~15x | C027r |
| FCF yield | ~1.2% (standalone) | C027r |
| 52-wk range | $240.51 – $412.70 → current is **−33% off the high**, +15.4% off the low | C029 |

## Why not an owner-earnings DCF

Trailing FCF (~$1.3B FY2025) is modest, **standalone**, and pre-Calpine; combined-entity FCF is not cleanly reported yet (the +64% Q1'26 revenue is an acquisition artifact); and hedge ratios are undisclosed. A 10-yr DCF would be false precision. The defensible anchor is **forward adjusted-operating-EPS × a terminal multiple**, bracketed by merchant peers and the franchise premium, cross-checked against Street targets.

## Multiples + peer comp

| Name | Fwd P/E | Note |
|---|---:|---|
| **CEG** | **~24x** | Premium: scale + nuclear CF + AI-PPA optionality + §45U floor |
| VST (Vistra) | ~16x | Merchant peer |
| TLN (Talen) | ~17–18x | Merchant peer (original BTM/AWS co-location case) |
| NRG | ~18x | Merchant peer |

CEG's ~24x is a **~6–8 turn premium** to the merchant set, compressed from >35x at the $412.70 high. The bull defends the premium on the un-buildable nuclear moat + the contracted, PTC-floored PPA annuity; the bear says ~17–18x is the right merchant multiple, especially after Calpine's gas dilution (carbon-free 90%→58%).

## Analyst targets (refreshed 2026-06-22)

Range **$296–441**, median **~$360** (23 analysts, consensus "Buy", as of 2026-06-18): low $296, high $441. **Even the lowest Street target ($296) sits above the current $277.64** — the sell-side reads the de-rate as overshooting. (C028r)

## Scenarios (adj-EPS × terminal P/E)

See `model/scenario_model.csv` (implied prices reconciled to these ranges).

| Scenario | Path | EPS × multiple | Value | vs $277.64 |
|---|---|---|---|---|
| **Bear** | Calpine deleverage stalls / re-rates toward merchant, no new premium PPA, power softens toward floor, multiple → ~17–18x | ~12.0 × ~18x | **~$210–230** | ~−20% |
| **Base** | Crane delivers 2027, Calpine accretes + deleverages (~2.0–2.25x), 1–2 new PPAs, premium ~24–25x holds | ~13.0 × ~25x | **~$300–340** | ~+10–22% |
| **Bull** | Multiple premium PPAs + uprates + 2nd restart, leverage → 2x, ~30x | ~13.8 × ~30x | **~$400+** | ~+45% |

**Asymmetry from $277.64: ~−20% bear / ~+10–22% base / ~+45% bull.** The de-risked leverage (now ~2.25x pro-forma, not the seed's 3.8x) modestly firms the base/bear floor vs 2026-06-19.

## The floor logic (why the bear is shallow)

The **§45U PTC (~$25/MWh to 2032)** backstops the power-price downside; 2027 open nuclear is priced **~$34/MWh**, above the floor (C019, C026). So the bear is a **multiple compression (24x → 17–18x) on an *intact* franchise**, not an earnings collapse. The downside is bounded and shallow relative to the bull — a legislated margin of safety most merchant generators lack. The refreshed primary leverage (~$21.3B / ~2.25x) makes the "Calpine over-levers the entity" leg of the bear weaker than the seed assumed.

## Margin Of Safety

| Required return | Buy below | Hold / starter | Trim/Avoid above |
|---|---|---|---|
| ~10–12%/yr (durable moat, PTC-floored, leverage de-risked, but capped flagship + Calpine gas dilution) | ≈ **<$250** (bear-ish ~18–20x multiple, moat intact → scale up) | **~$250–300** (STARTER; the current $277.64 sits here) | ≳ **$370+** (Street median froth) / ≳$414 (>30x) |

**At $277.64 the stock is a *quality-at-fair-price* name with a real-but-thin margin of safety.** The −33% restored a margin of safety **vs its own froth** (>35x→~24x), not vs absolute value (~24x > 16–18x peers). The skew is favorable (shallow floored bear, solid base, strong bull) and the whole Street ($296–441) sits above the price. This supports a **STARTER** now, scaling on (a) a confirmed *new* premium-nuclear PPA, or (b) weakness toward $230–250.

## Valuation discipline notes

- A genuinely durable moat can still be only a *fair* forward investment at ~24x — pay for it as a starter, not a layup.
- Do not let a 30x bull multiple rescue the present; ~24x already embeds a premium, and Calpine's gas mix is a re-rating risk toward a merchant multiple.
- The single biggest upside swing is the **next PPA price** (Crane's is locked to MSFT and undisclosed; the one new deal found — CyrusOne 380 MW — is gas, not premium nuclear). (C013, C030)
- Leverage is no longer the scary number it looked like at 2026-06-19: primary 10-Q net debt ~$21.3B, pro-forma ~2.25x, LS Power cash in. (C011r)

→ Position implication is in `memo-v1.md` (STARTER + sizing); triggers in `monitor.md`.
