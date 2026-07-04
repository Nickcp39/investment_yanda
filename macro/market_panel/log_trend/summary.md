# Common Log-Trend Indicators

This folder tracks QQQ, SPY, and large-cap tech against log-linear trend lines.
Use 5Y and 10Y first; use full-history only as background because liquidity and
rate regimes can change the slope.

Built through 2026-07-01 from `macro/market_panel/data/`.

## Latest Snapshot

| ticker | price | vs 5Y trend | 5Y CAGR | vs 10Y trend | 10Y CAGR | vs full | 1Y growth |
|---|---:|---:|---:|---:|---:|---:|---:|
| GOOGL | $361.21 | +38.8% | 22.6% | +42.2% | 21.5% | +45.5% | +105.5% |
| GOOG | $357.89 | +37.1% | 22.5% | +39.0% | 21.8% | +43.3% | +102.3% |
| TSLA | $425.30 | +24.5% | 10.0% | -36.4% | 48.3% | -34.1% | +33.9% |
| QQQ | $725.17 | +15.6% | 18.0% | +11.2% | 19.3% | +13.3% | +32.1% |
| AAPL | $294.38 | +9.5% | 15.1% | -16.0% | 28.7% | -7.6% | +44.1% |
| SPY | $745.76 | +8.7% | 14.6% | +9.7% | 14.1% | +11.3% | +22.0% |
| AMZN | $241.70 | +4.6% | 14.7% | -6.7% | 17.5% | -31.0% | +10.2% |
| META | $612.91 | -20.0% | 34.3% | +5.7% | 17.5% | -11.9% | -16.7% |
| MSFT | $384.28 | -21.7% | 14.6% | -38.9% | 26.5% | -36.4% | -22.1% |
| NVDA | $197.58 | -24.2% | 82.4% | +1.6% | 62.0% | +29.5% | +25.2% |

## Files

- `common_log_trend_dashboard.png` - quick visual dashboard.
- `<TICKER>_log_trend.png` - price plus full/10Y/5Y log trend lines and deviation panel.
- `<TICKER>_channel.csv` - price, trend values, and deviation columns.
- `common_log_trend_summary.csv` - one row per ticker/window.
- `common_log_trend_latest.csv` - one latest row per ticker.

## Method

Fit `ln(price) = a + b * time` with ordinary least squares.
The trend line is `exp(a + b * time)`, and trend CAGR is `exp(b * 365.25) - 1`.

Missing input series: none.