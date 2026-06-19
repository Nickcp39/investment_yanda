# Financial Quality — CEG

Last updated: 2026-06-19

Source base: FY2025 release (S1), Q1 2026 8-K (S2), 2026 Outlook deck (S3), §45U statute (S7). Facts: `../facts.md` / `../claim_ledger.csv`.

## One-line read

A genuinely high-quality, cash-generative merchant generator — ~22 GW nuclear at ~95% capacity factor and near-zero marginal cost, beating its own adjusted-EPS guide quarter after quarter — whose financials are clean and whose **downside is legislatively floored** (§45U PTC ~$25/MWh to 2032). The only two things that complicate the read are temporary and well-flagged: (1) **Calpine has levered the balance sheet to ~3.8x** with a credible-but-unproven path to ~2.0x by 2027, and (2) the **Q1'26 +64% revenue is an acquisition artifact**, not organic. This is much closer to a Terry-Smith "clean compounder" than NBIS — the risk is balance-sheet/execution, not accounting quality.

## Accounting → Economics Bridge

| Item | Reported | Economic interpretation | claim_id |
|---|---:|---|---|
| FY2025 revenue | $25.5B (+8%) | Standalone merchant + retail; real | C001 |
| FY2025 adj operating EPS | $9.39 (beat) | The right franchise read; GAAP $7.40 swings on commodity marks | C002 |
| FY2025 GAAP EPS | $7.40 | < adj-EPS due to mark-to-market; not a clean operating read this year | C002 |
| FY2025 FCF | ~$1.3B | Modest vs ~$98B cap; the **forward** FCF story is contracted PTC-floored PPAs | C003 |
| FY2025 nuclear CF | 94.7% | The engine: ~95% CF, ~$0 marginal fuel → wide inframarginal margin | C004 |
| Q1'26 revenue | $11.1B (+64%) | **Acquisition artifact** (first Calpine-consolidated qtr), not organic | C005 |
| Q1'26 adj EPS | $2.74 (beat $2.59) | Continues the beat pattern; GAAP $4.49 (favorable marks this qtr) | C006 |
| Q1'26 nuclear CF | 92.3% | Seasonally lower (refueling); discipline intact | C007 |
| Net debt — standalone YE2025 | ~$5.3B (~0.9x) | Conservative pre-deal | C011 |
| Net debt — post-Calpine | **~$21.6B (~3.8x)** | **ESTIMATED pending Q1'26 10-Q**; the key quality watch | C011 |
| Buyback | $5.0B auth; ~$335M YTD | Per-share discipline; retirer, not just issuer | C008 |
| Dividend | $1.71 (~0.6%), ≥10% growth | Growing, well-covered | facts.md |

**Owner-earnings read:** unlike NBIS (negative owner earnings), CEG's owner earnings are **positive and growing** — the franchise throws off cash, returns it (buyback + dividend), funds Crane (~$1.6B, $1.0B DOE loan), *and* deleverages. The constraint is not "does it earn money" but "how fast does Calpine debt come down."

## Quality Questions

- **Is revenue recurring / contracted?** Increasingly so. Base merchant volume is partially hedged forward; the new layer is **long-dated PPAs** (Crane→MSFT 20-yr, Meta→Clinton) that convert volatility into contracted annuities. Higher quality than pure spot. (C013, C021)
- **Does growth require rising capital intensity?** **No — the opposite of NBIS.** The core nuclear fleet already exists; Crane is a ~$1.6B restart (largely DOE-funded), not a greenfield build. Growth comes from (a) PPA premiums on existing MW, (b) Calpine accretion, (c) uprates/restarts — not a capex treadmill. (C018)
- **Are margins real?** Yes — ~95% CF on ~$0-fuel nuclear is a structurally wide margin set by the gas-marginal clearing price. The §45U PTC floors the bottom of that margin. (C020, C026)
- **Is SBC / dilution a concern?** The dilution event is the **Calpine equity issuance (~50M shares)** — a discrete, disclosed, accretion-justified raise, not chronic SBC dilution. (C014)
- **Buybacks?** Yes — $5.0B authorization, actively repurchasing. A retirer. (C008)
- **Is reported FCF overstating owner earnings?** No structural inflation flagged (no prepayment-OCF trick like NBIS). The caveat is that ~$1.3B is **standalone** and the combined-entity FCF is not yet cleanly reported.

## Watch items (not red flags — this is a clean book)

1. **⚠️ Post-Calpine leverage ~3.8x (estimated).** The deleverage to ~2.0x by 2027 (via ~$5B asset sales — LS Power $5B/4.4 GW signed — + paydown) is a **forecast**. Await the Q1'26 10-Q for the audited combined net-debt/EBITDA. This is the single most important number to confirm. (C011, C024)
2. **Q1'26 +64% revenue is acquisition-driven** — do not read it as organic growth.
3. **Hedge ratios undisclosed** → near-term EPS sensitivity to power curves not precisely modelable.
4. **GAAP vs adj-EPS gap** swings on commodity marks — use adj operating EPS for the franchise.

## So what

The economics are **already high-quality** — positive, growing owner earnings; a structurally wide, PTC-floored margin; per-share discipline. The financial *story* is therefore not "will it earn" but **"will Calpine deleverage on plan."** If it does (LS Power cash in, ~2.0x by 2027), the quality read is clean and the franchise compounds. The honest caution is that the combined-entity numbers are still partly estimated pending the Q1'26 10-Q. Modeled in `../model/`.
