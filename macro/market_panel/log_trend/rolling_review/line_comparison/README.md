# Line Comparison Review

Two comparisons are included:

1. `rolling_vs_fixed_log`: solid lines are rolling 5Y/10Y log trends; dashed lines are
   the latest fixed-window log-straight line converted back into real price.
2. `log_vs_price_straight`: rolling 5Y log trend versus a literal straight line in
   normal price space.

Important: rolling and fixed log lines share the same final value because the final
day uses the same latest 5Y/10Y window. The historical path is what differs.

## Current 5Y Comparison

| ticker | price | rolling 5Y log trend | price-straight 5Y line | vs rolling | vs price-straight |
|---|---:|---:|---:|---:|---:|
| QQQ | $713.65 | $622.20 | $610.13 | +14.7% | +17.0% |
| GOOG | $346.08 | $257.78 | $262.95 | +34.3% | +31.6% |
| MSFT | $373.94 | $491.97 | $480.22 | -24.0% | -22.1% |
| AAPL | $294.30 | $267.63 | $262.47 | +10.0% | +12.1% |
| NVDA | $200.04 | $257.49 | $190.60 | -22.3% | +5.0% |
| AMZN | $234.11 | $229.53 | $228.43 | +2.0% | +2.5% |

## Files

- `<TICKER>_rolling_vs_fixed_log.png`
- `<TICKER>_log_vs_price_straight.png`
- `current_deviation_log_vs_price_line.png`
- `rolling_vs_fixed_log_latest.csv`
- `log_vs_price_straight_latest.csv`