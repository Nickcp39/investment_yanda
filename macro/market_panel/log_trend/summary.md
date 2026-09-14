# Common Log-Trend Indicators

This folder tracks QQQ, SPY, and large-cap tech against log-linear trend lines.
Use 5Y and 10Y first; use full-history only as background because liquidity and
rate regimes can change the slope.

Built through 2026-09-11 from `macro/market_panel/data/`.

## Latest Snapshot

| ticker | price | vs 5Y trend | 5Y CAGR | vs 10Y trend | 10Y CAGR | vs full | 1Y growth |
|---|---:|---:|---:|---:|---:|---:|---:|
| AAPL | $332.27 | +16.9% | 16.3% | -8.1% | 28.3% | -0.1% | +47.1% |
| GOOGL | $338.50 | +16.7% | 26.1% | +25.2% | 22.0% | +29.5% | +41.9% |
| GOOG | $335.45 | +15.4% | 26.0% | +22.7% | 22.3% | +27.6% | +40.4% |
| QQQ | $714.88 | +6.3% | 20.0% | +5.6% | 19.3% | +7.6% | +23.7% |
| SPY | $764.29 | +5.6% | 16.0% | +8.7% | 14.2% | +10.7% | +18.5% |
| TSLA | $365.44 | +4.0% | 10.4% | -46.9% | 47.2% | -45.8% | +5.1% |
| AMZN | $256.78 | +3.3% | 17.3% | -2.5% | 17.0% | -28.9% | +11.5% |
| MSFT | $495.63 | -0.9% | 14.7% | -21.8% | 25.7% | -20.3% | -0.1% |
| META | $648.03 | -21.4% | 37.2% | +8.0% | 17.6% | -9.7% | -13.5% |
| NVDA | $218.29 | -24.9% | 83.8% | +2.5% | 61.7% | +29.5% | +23.4% |

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