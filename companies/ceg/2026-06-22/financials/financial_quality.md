# Financial Quality — CEG

Last updated: **2026-06-22**

Source base: FY2025 release (S1), Q1'26 8-K (S2), Q1'26 **10-Q** (S13), §45U statute (S7). Facts: `../facts.md` / `../claim_ledger.csv`.

## One-line read

A genuinely high-quality, cash-generative merchant generator — ~32 GW nuclear at ~95% capacity factor and near-zero marginal cost, beating its own adjusted-EPS guide quarter after quarter — whose financials are clean and whose **downside is legislatively floored** (§45U PTC ~$25/MWh to 2032). The two complications the seed flagged are now **resolved or milder**: (1) post-Calpine leverage, feared at ~3.8x, is **~2.25x pro-forma on the primary 10-Q** (net debt ~$21.3B) with LS Power's $5B cash in; (2) the Q1'26 +64% revenue is an acquisition artifact, not organic. This is much closer to a "clean compounder" than NBIS — the residual risk is integration/execution, not accounting quality.

## Accounting → Economics Bridge

| Item | Reported | Economic interpretation | claim_id |
|---|---:|---|---|
| FY2025 revenue | $25.5B (+8%) | Standalone merchant + retail; real | C001 |
| FY2025 adj operating EPS | $9.39 (beat) | The right franchise read; GAAP $7.40 swings on marks | C002 |
| FY2025 FCF | ~$1.3B | Modest vs ~$100B cap; forward FCF story is contracted PTC-floored PPAs | C003 |
| FY2025 nuclear CF | 94.7% | The engine: ~95% CF, ~$0 fuel → wide inframarginal margin | C004 |
| Q1'26 revenue | $11.12B (+64%) | **Acquisition artifact** (first full Calpine quarter), not organic | C005 |
| Q1'26 adj EPS | $2.74 (beat $2.59) | Continues the beat pattern; GAAP $4.49; Calpine ~+$2/share FY26 | C006 |
| Q1'26 nuclear CF | 92.3% | Seasonally lower (refueling); discipline intact | C007 |
| **Net debt — Q1'26 10-Q** | **~$21.3B** (LT $16,994M + ST $5,102M − cash $800M) | **PRIMARY** — resolves the seed's ~$21.6B estimate | C011r |
| **Pro-forma leverage** | **~2.25x** (mgmt, forward-EBITDA) | $3.4B debt-reduction plan to 2027 toward ~2.0x | C011r |
| Buyback | $5.0B auth | Per-share discipline; retirer | C008 |
| Dividend | $1.71 (~0.6%), ≥10% growth | Growing, well-covered | facts.md |

**Owner-earnings read:** unlike NBIS (negative owner earnings), CEG's owner earnings are **positive and growing** — the franchise throws off cash, returns it (buyback + dividend), funds Crane (~$1.6B, $1.0B DOE loan), *and* deleverages. The constraint is not "does it earn money" but "how fast does Calpine debt come down" — and that constraint is **easing** (LS Power cash in, ~2.25x pro-forma).

## Quality Questions

- **Is revenue recurring / contracted?** Increasingly so — base merchant volume is partially hedged forward; the new layer is long-dated PPAs (Crane→MSFT 20-yr, Meta→Clinton, CyrusOne gas). (C013, C021, C030)
- **Does growth require rising capital intensity?** **No — the opposite of NBIS.** The core fleet exists; Crane is a ~$1.6B restart (largely DOE-funded), not a greenfield. (C018)
- **Are margins real?** Yes — ~95% CF on ~$0-fuel nuclear, set by the gas-marginal clearing price, floored by §45U. (C020, C026)
- **Is SBC / dilution a concern?** The dilution event was the **Calpine equity issuance (~50M shares / $17.6B)** — a discrete, accretion-justified raise, not chronic SBC. (C014)
- **Buybacks?** Yes — $5.0B authorization. A retirer. (C008)
- **Is reported FCF overstating owner earnings?** No structural inflation flagged. The caveat: ~$1.3B is **standalone**; combined-entity FCF is not yet cleanly reported.

## Watch items (this is a clean book)

1. **Post-Calpine leverage ~2.25x pro-forma (10-Q net debt ~$21.3B).** The path to ~2.0x by 2027 is still partly a forecast, but the largest step (LS Power $5B) is **done**. Confirm the trajectory at each 10-Q. **Much less of a red flag than at 2026-06-19.** (C011r, C024)
2. **Q1'26 +64% revenue is acquisition-driven** — not organic.
3. **Hedge ratios undisclosed** → near-term EPS sensitivity to power curves not precisely modelable.
4. **GAAP vs adj-EPS gap** swings on commodity marks — use adj operating EPS for the franchise.
5. **Combined-entity FCF** not cleanly reported — second primary confirmation warranted before CORE.

## So what

The economics are **already high-quality** — positive, growing owner earnings; a structurally wide, PTC-floored margin; per-share discipline. The financial *story* is therefore not "will it earn" but **"will Calpine deleverage on plan"** — and this pass shows it is on plan (LS Power cash in, ~2.25x pro-forma). The honest residual caution is that combined-entity FCF is still partly estimated. Modeled in `../model/`.
