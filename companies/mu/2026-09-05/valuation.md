# MU Valuation (M6) — as_of 2026-09-05

**as_of_price 1016.59** · market cap $1.149T (1,130M shares) · EV $1.12T · **-19.0% off the 52-week high**
of $1,255.00 · prior card 2026-07-10 was $979.30, so **+3.8%**.
Model: `model/scenario_model.csv`.

## The band is CARRIED, unchanged, and that is a deliberate decision
Micron has not reported since the prior card. Q4 FY2026 lands **2026-09-30**, after this as_of. There is
no company-specific evidence on which to move the valuation. Re-rating an entry price on sector sentiment
and peer read-across is precisely the error this pipeline exists to prevent.

| Scenario | Normalized EPS | Exit P/E | Fair value | Price / fair |
|---|---:|---:|---:|---:|
| Bear — mid-cycle reversion | $11 | 15x | $165 | 6.16x |
| **Base — HBM lifts the floor** | **$22** | **20x** | **$440** | **2.31x** |
| Bull — semi-secular re-rate | $38 | 25x | $950 | 1.07x |

## The price moved the WRONG way against the band
| | 2026-07-10 | 2026-09-05 |
|---|---:|---:|
| Price / base fair | 2.23x | **2.31x** |
| Price / bull fair | 1.03x | **1.07x** |

In July the stock sat roughly **at** the honest bull case. It is now **above** it. The +3.8% move made the
setup slightly worse, not better.

## The forward-multiple trap, stated plainly
Forward P/E is **7.07x**. Trailing is **22.94x**. Memory stocks print their lowest multiples on peak EPS —
that is what a cyclical top looks like from the inside. Micron's own record: **FY2022 EPS $7.75 became
FY2023 EPS of −$5.34**, a 169% swing peak to trough. Against TTM EPS of $44.31, the market at 1016.59 is
implicitly paying for normalized EPS of roughly **$85 at 12x** — about **11x** the FY2022 prior-peak EPS.

## Calibrating "it has already fallen a lot"
Micron's own major drawdowns since 2006: −89.7%, −73.8%, −50.6%, −48.4%, −54.0%. **Median −54.0%.**
The current drawdown is **-19.0% off the 52-week high**; the deepest point this cycle was −39.1% on
2026-07-29, since retraced. By this stock's own history a 19% drawdown has never marked a cycle low.

## Buy-below UNCHANGED at $650
Price needs to fall a further **36.1%** to reach it. 2026-09-30 is the date that earns any change to this
number — in either direction. See `decision_card.json → runner_dissent` for the case that the base band
may now be too harsh, and why it is flagged rather than quietly adjusted.
