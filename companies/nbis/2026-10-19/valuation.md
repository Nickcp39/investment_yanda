# NBIS Valuation (M6) — as_of 2026-10-16, run 2026-10-19

**as_of_price 165.47** · market cap $45.36B (274.10M shares) · **−44.8% off the 52-week high** of $299.86
· baseline `../2026-09-05/` ($226.39) → **−26.9%**. Model: `model/scenario_model.csv`.

## The band did not move. The price moved into it.

| | |
|---|---|
| buy-below band | **$150 – $180** (unchanged across 07-10 → 08-12 → 09-05 → 10-19) |
| price vs band | **INSIDE**: 8.1% below the $180 STARTER gate, 10.3% above the $150 floor |
| no-chase zone | ≥ $250 — 34% above price |
| max size | ≤ 4% (card) · **T0 real-money cap $500** (`trading-desk/risk_limits.md`) |

## EV after the converts — two bases, because the cash has not been spent yet

The $5.75B converts closed 2026-08-24. Pro-forma on the Q2 balance sheet (no Q3 burn):

| Basis | Cash | Debt counted | EV | EV / ARR $3.0B (Jun) | EV / exit-26 ARR $8.0B mid |
|---|---:|---:|---:|---:|---:|
| **A — pro-forma post-converts** | $9.10B cash+restricted + $5.68B net proceeds = $14.78B | $775M ABF + $5.75B new converts + ~$0.2B residual 2029/2031 notes ≈ $6.73B | **$37.3B** | **12.4x** | **4.7x** |
| B — prior-card method (ignores the converts on both sides) | $8.0B | $775M ABF | $38.1B | 12.7x | 4.8x |

Both bases land at roughly the same EV because the converts added cash and debt one-for-one. What changes
EV from here is **burn**: at the Q2 run-rate (~$5.7B capex/quarter against ~$2.3B OCF) each quarter adds
roughly $3–3.5B of net debt until revenue catches up. The residual 2029/2031 principal after the $800M
exchange is **not confirmed in this run** (original 2025 issuance believed ~$1.0B total; marked unverified).

| Scenario | exit-2026 ARR | EV (basis A) | EV/ARR |
|---|---:|---:|---:|
| guide low | $7.0B | $37.3B | 5.3x |
| guide mid | $8.0B | $37.3B | 4.7x |
| guide high | $9.0B | $37.3B | 4.1x |
| current (Jun-26) | $3.0B | $37.3B | 12.4x |

## Why M6 moves to +1 and the verdict does not

At 09-05 the shape was "defensible on exit ARR, expensive on current ARR, and the whole difference is a
six-month ramp that has not happened". At $165 the multiple on the *un-happened* ramp is 4.7x instead of
6.85x, and on current ARR 12.4x instead of 18.3x. That is a real change in price and is scored as such.

The verdict is gated on evidence, not price: the STARTER trigger has two conditions and the second —
active MW disclosed — has now been open for four quarters. The pipeline rule (`discipline.md` §3.1) is that
verdict ≥ STARTER is required before a buy, and verdict stays WATCH while the proof metric is absent.

## What the converts say about the company's own view of price
The company set the equity reference at **$223.90** and sold conversion rights at **$313–325** eight weeks
before the stock traded at $165. Either the market is wrong by a third or the company's August pricing was
the top of its own range. The card does not pick; it notes that the conversion prices are now 90–96% above
spot, so the notes will behave as **debt**, not as equity, for the foreseeable future — which is precisely the
K-G branch.

`capital_cycle`: `applicable yes · stage mid-late · supply_barrier low · caution PEAK-lean` — unchanged.
The peer-credit episode is what a capital-cycle peak looks like from the financing side.

## Down-side arithmetic the owner should see
| From $165.47 to | Move |
|---|---|
| band floor $150 | −9.3% |
| 52-week low $73.52 | −55.6% |
| convert conversion price $313.46 | +89.4% |
| 09-05 price $226.39 | +36.8% |
