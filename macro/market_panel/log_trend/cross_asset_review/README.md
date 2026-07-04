# SPY and Gold Rolling Log-Trend Review

Source series:

- `SPY`: Yahoo Finance adjusted close, dividend-adjusted.
- `GOLD`: Yahoo Finance `GC=F` gold futures series from `macro/market_panel/data/GOLD.csv`.

## Latest

| ticker | date | price | rolling 5Y trend | vs 5Y | 5Y CAGR | rolling 10Y trend | vs 10Y | 10Y CAGR |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| SPY | 2026-06-23 | 733.58 | 682.38 | +7.5% | 14.5% | 677.33 | +8.3% | 14.1% |
| GOLD | 2026-06-24 | 4,001.00 | 4,058.33 | -1.4% | 23.3% | 3,311.48 | +20.8% | 12.3% |

## Reversion Math

| ticker | trend | 1Y | 2Y ann. | 3Y ann. |
|---|---|---:|---:|---:|
| SPY | rolling 5y | +6.5% | +10.4% | +11.7% |
| SPY | rolling 10y | +5.3% | +9.6% | +11.1% |
| GOLD | rolling 5y | +25.0% | +24.2% | +23.9% |
| GOLD | rolling 10y | -7.0% | +2.2% | +5.5% |

## Files

- `spy_gold_rolling_dashboard.png`
- `SPY_rolling_log_trend.png`
- `GOLD_rolling_log_trend.png`
- `spy_gold_latest.csv`
- `spy_gold_reversion_scenarios.csv`