# Valuation / Margin Of Safety — VRT

Last updated: **2026-06-22** (refreshed from 2026-06-19 seed)

Source base: market data (S6, aggregator + Yahoo + wallstreetzen, cross-checked in `freshness.json`), FY26 guide (S1), 2030 targets (S4). All prices as of **2026-06-22**, **volatile**. Engine = **EPS × forward P/E** ladder (VRT is FCF-positive; the swing variable is the forward multiple) — see `model/scenario_model.csv`.

## Current Setup (at $345.05)

| Item | Value | claim_id |
|---|---|---|
| Share price | **$345.05** (06-22 close; was $333.05 06-18) | freshness.json |
| Market cap | **~$132.5B** | C029 |
| Net cash | ~$0.76B | C028 |
| **Enterprise value** | **~$132B** (net cash → EV ≈ mkt cap) | C029 |
| Shares out | 384.11M | freshness.json |
| 52-wk high / low | **$379.94 / $110.06** | C030 |
| Position vs high / low | **−9.2% off high / +213% off low** | C030 |

## Multiples (EV ≈ $132B; FY26E EPS $6.35)

| Multiple | Value | Note | claim_id |
|---|---:|---|---|
| **Forward P/E** | **~50.5x** (stockanalysis) / **~54x** on FY26E $6.35 as-reported | the anchor — richer than the seed's ~48-49x after the rally | C029 |
| Trailing P/E | ~86x | earnings still catching up to price | C029 |
| P/S | ~12.5x | | C029 |
| **PEG** | **~1.6** | fast growth, but not cheap relative to it | C029 |

**Read: priced for perfection — and more so than the seed.** ~50-54x forward earnings on a hardware-heavy industrial is only justified by sustained 20%+ organic growth *and* the margin march to 27% (2030). **The bull case is already in the price** — and after the +3.6% move to $345 there is even less of it left as edge. (C029, C015)

## Why an EPS × P/E ladder (not a DCF)

VRT is **solidly FCF-positive** (~$1.9B FY25 → ~$2.2B FY26E), so — unlike NBIS (negative FCF → EV/forward-sales triangulation) — the defensible engine is **EPS × forward multiple**. The whole bear case is a **de-rate** (50x → 25–30x) on roughly flat EPS: the *multiple* does the work on a high-beta, no-floor capex-cycle name. That is the single most important valuation fact, and it is unchanged by the refresh.

## Scenarios (EPS × P/E → price)

Anchored on near-term EPS × a forward multiple, vs current price **$345.05**. See `model/scenario_model.csv`.

| Scenario | Path | EPS basis | P/E | Value | vs $345.05 |
|---|---|---|---:|---|---:|
| **Bear** | 2027 capex digestion + book-to-bill confirmed <1.0; de-rate ~25–30x on **flat** EPS; **no floor** | ~$6–7 | 25–30x | **~$182** ($170–230) | **−47%** (−33% to −51%) |
| **Base** | In-line FY26 execution; multiple holds ~45–48x | ~$6.35 → FY27 grows | 45–48x | **~$292** ($340–380 if FY27 EPS grown in) | **−15%** (−12% to +10%) |
| **Bull** | FY26 beaten, 2030 27%-margin validated, backlog re-accelerates; ~50x FY27E EPS | FY27E up | ~50x | **~$360** ($430–480 on FY27E) | **+4%** (+25% to +39%) |

\* Bear has **no floor** — the $110.06 52-wk low was ~one year ago. The skew **worsened** with the rally: near-term **base ≈ −15%, bull ≈ +4%, bear ≈ −47%**. Only the *dynamic* base ($340–380, FY27 EPS grown into 45–48x) and the FY27E bull ($430–480) clear current — and both require the orders/B2B gauge to confirm ≥1.0 first.

## The Street (upside now even thinner)

- **Analyst mean target ~$378** (Strong Buy, 27 analysts, high $500, low $260) ≈ **+9.6%** upside. (C031)
- After **+213% off the low**, the Street now sees only ~**+9.6%** to the mean (vs +13% at the seed) — i.e., even more of the bull case is *consensus*, not edge.

## Margin Of Safety

| Required return | Buy below | Hold/Watch | Trim/Avoid above |
|---|---|---|---|
| ~12–15%/yr (high-beta, no floor, priced-for-perfection) | ≈ **<$230–250** (restores MOS; ~bear + cushion; implies ~36–39x fwd) | ~$250–345 | **>~$345** (priced for perfection — at/above now) |

**At $345 the stock sits *above* the "priced for perfection" line** (which the seed put at ~$340). This is not "sell" (no position is held); it is **"no margin of safety for new capital,"** now with a worse skew than the seed. Combined with the still-withheld orders/B2B (binding gap, C012, dark until Q2'26 on 2026-07-29), it caps the actionable lean at **WATCH**. Re-rates toward STARTER on (a) clean orders/B2B re-disclosure ≥1.0 at Q2'26, or (b) a pullback toward ~$230–250.

## Valuation discipline notes

- A great franchise can still be a poor *forward* investment at ~50-54x with **no contracted floor** under a cyclical demand base — the rally to $345 makes this sharper, not softer.
- The forward multiple is doing all the work — do not assume ~50x holds; the base case *requires* it, and that is not conservative.
- Uncertainty is asymmetric and *informational*: the orders/B2B gauge is still withheld (C012), so the bear branch cannot be ruled out nor the bull confirmed until Q2'26 (2026-07-29) re-discloses → required MOS rises, and there is none at $345.
- **Refresh delta:** the +3.6% move did not change the structure — it shrank the upside (Street +13%→+9.6%, near-term bull +8%→+4%) and pushed price above the perfection line. M6 caps first; verdict unchanged at WATCH.

→ Position implication is written in `memo-v1.md` (WATCH; STARTER on pullback / re-disclosure) and `monitor.md` (triggers).
