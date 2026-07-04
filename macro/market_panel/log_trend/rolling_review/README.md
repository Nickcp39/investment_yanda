# Rolling Log-Trend Review

This is the review version of the trend-line indicator. Each date uses only
the previous 5Y or 10Y of prices, fits `ln(price)=a+b*time`, then converts
the fitted value back into real price space with `exp(a+b*time)`.

This makes the trend line itself bend when the regime changes.

## Latest

| ticker | price | rolling 5Y trend | vs 5Y | 5Y trend CAGR | rolling 10Y trend | vs 10Y | 10Y trend CAGR |
|---|---:|---:|---:|---:|---:|---:|---:|
| GOOGL | $346.13 | $256.94 | +34.7% | 22.2% | $252.21 | +37.2% | 21.4% |
| GOOG | $346.08 | $257.78 | +34.3% | 22.1% | $255.61 | +35.4% | 21.8% |
| QQQ | $713.65 | $622.20 | +14.7% | 17.7% | $649.34 | +9.9% | 19.3% |
| TSLA | $381.61 | $339.74 | +12.3% | 9.8% | $666.40 | -42.7% | 48.4% |
| AAPL | $294.30 | $267.63 | +10.0% | 15.1% | $349.57 | -15.8% | 28.8% |
| AMZN | $234.11 | $229.53 | +2.0% | 14.4% | $258.96 | -9.6% | 17.6% |
| NVDA | $200.04 | $257.49 | -22.3% | 82.3% | $192.70 | +3.8% | 62.0% |
| MSFT | $373.94 | $491.97 | -24.0% | 14.8% | $629.56 | -40.6% | 26.7% |
| META | $562.20 | $760.56 | -26.1% | 34.1% | $577.76 | -2.7% | 17.6% |

## Reversion Math

If price returns to the current rolling trend line after H years, the return is:

`future_trend = trend_today * (1 + trend_cagr)^H`

`return = future_trend / price_today - 1`

| ticker | trend | 1Y revert | 2Y revert ann. | 3Y revert ann. |
|---|---|---:|---:|---:|
| QQQ | rolling 5y | +2.6% | +9.9% | +12.5% |
| QQQ | rolling 10y | +8.5% | +13.8% | +15.6% |
| GOOG | rolling 5y | -9.1% | +5.3% | +10.6% |
| GOOG | rolling 10y | -10.1% | +4.7% | +10.1% |
| MSFT | rolling 5y | +51.0% | +31.7% | +25.8% |
| MSFT | rolling 10y | +113.2% | +64.3% | +50.7% |

## Files

- `rolling_log_trend_focus_dashboard.png` - recent 5Y review dashboard.
- `<TICKER>_rolling_log_trend.png` - full chart with rolling 5Y/10Y trend and deviation.
- `<TICKER>_rolling_log_trend.csv` - daily rolling trend values.
- `rolling_log_trend_latest.csv` - current readings.
- `rolling_log_trend_reversion_scenarios.csv` - 1Y/2Y/3Y trend-reversion return math.