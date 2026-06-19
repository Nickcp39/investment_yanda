# CEG Research Run — Layer 9: Valuation + Market

- Run date: 2026-06-19
- Method: decomposition of the Block-1 evidence pack, grounded in `../source_register.md` (S9 market data; S3 guidance; S7 PTC floor). Prices as of 2026-06-19.
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Promoted to `../claim_ledger.csv` (C027–C028) and feeds `../valuation.md` + `../model/`.

---

## BOTTOM LINE

At **$274.06**, CEG trades at **~24x fwd P/E, ~15x EV/EBITDA, ~1.2% FCF yield** — a **premium to merchant peers** (VST ~16x, TLN ~17–18x, NRG ~18x) that is **compressed from >35x at the $413 high (−34%).** The premium is justified by scale + nuclear CF + AI-PPA optionality + the §45U floor, but it is **fair, not cheap.** Street targets cluster **$300–390 (median ~$370)**. The asymmetry from $274 is the best of the three-name batch: ~−20% bear / ~+20–25% base / ~+50% bull.

---

## Current setup [S9]

| Item | Value | claim_id |
|---|---|---|
| Share price | **$274.06** (2026-06-19) | C027 |
| Market cap | ~$98B | C027 |
| Enterprise value | ~$120B | C027 |
| Fwd P/E | **~24x** | C027 |
| EV/EBITDA | ~15x | C027 |
| FCF yield | ~1.2% | C027 |
| 52-wk high | $413 (de-rate −34%) | C027 |

## Peer comp [S9]

| Name | Fwd P/E | Note |
|---|---|---|
| **CEG** | **~24x** | Premium; scale + nuclear CF + AI-PPA optionality + PTC floor |
| VST (Vistra) | ~16x | Merchant peer |
| TLN (Talen) | ~17–18x | Merchant peer; the original BTM/AWS co-location case |
| NRG | ~18x | Merchant peer |

- CEG's ~24x is a **~6–8 turn premium** to the peer set. The bull defends it on the un-buildable nuclear moat + the contracted AI-PPA annuity; the bear says ~17x is the right merchant multiple → $200–230.

## Analyst targets [S9]

- Range **$300–390**, median **~$370**:
  - Mizuho **$300**, KeyBanc **$321**, Barclays **$358**, UBS **$388**.
- Even the low Street target ($300) is **above** the current $274 — i.e., the sell-side sees the de-rate as overshooting.

## Scenarios (EPS × multiple → price)

Anchored on FY2026 guide ($11–12 adj EPS, C009) and the ~24x base multiple, flexed by Crane (2027) + Calpine accretion + new-PPA optionality. See `../model/scenario_model.csv`.

| Scenario | Path | EPS basis | Multiple | Value |
|---|---|---|---|---|
| **Bear** | Calpine deleverage stalls, no new AI PPA, power softens | ~$11.5 base | ~17x (merchant) | **~$200–230** |
| **Base** | Crane delivers 2027, Calpine accretes, 1–2 new PPAs | ~$12.5 fwd | ~24–25x | **~$300–340** |
| **Bull** | Multiple premium PPAs + uprates + 2nd restart, leverage→2x | ~$14+ fwd | ~30x | **~$400+** |

- **Asymmetry from $274:** bear ~−20% / base ~+20–25% / bull ~+50%. Best risk/reward of GEV/VRT/CEG.
- **Floor logic:** the §45U PTC (~$25/MWh to 2032) backstops the *power-price* downside; the bear is a *multiple* compression (24x→17x) on an intact franchise, not an earnings collapse. That makes the bear shallow relative to the bull.

## Why not a pure owner-earnings DCF
- Trailing FCF (~$1.3B) is modest and pre-Calpine; combined-entity FCF is not cleanly reported yet; hedge ratios are undisclosed. So the defensible anchor is **forward EPS × a multiple bracketed by peers (16–18x) and the franchise premium (24–30x)**, cross-checked against Street targets — not a 10-yr DCF on noisy trailing cash.

---

## COULD NOT VERIFY
1. Post-Calpine combined EBITDA/FCF (await Q1'26 10-Q) → EV/EBITDA and FCF yield are estimates. (C011)
2. Microsoft PPA price → cannot value the Crane annuity precisely. (C013)
3. Multiples (C027/C028) are aggregator-sourced (stockanalysis.com), intraday-ish; treat as ±.

## Key sources
- S9 — stockanalysis.com (CEG/VST/peer multiples), 2026-06 — stockanalysis.com/stocks/ceg/
- S3 — CEG 2026 Outlook deck (guide), 2026-03-31
- S7 — §45U PTC floor, 2025-07

**Net for thesis:** ~24x is a fair price for a durable moat with the scariest tails cut — a *quality-at-fair-price pullback*, not deep value. The asymmetry is favorable (shallow floored bear / solid base / strong bull) and the whole Street sees $300+. That supports a **STARTER**, with adds on a new PPA or weakness to $230–250.
