# US-Japan Yield Curve vs S&P 500

This folder collects the charts and data generated for the US/Japan yield
comparison work on 2026-06-18.

## Main Figures

- `figures/us_japan_yield_gap_lines_vs_sp500_12m_return_1976_2026.png`
  - Long-run line chart from 1976 to 2026.
  - Blue line: US-Japan yield gap.
  - Black line: S&P 500 trailing 12-month price return.

- `figures/us_japan_yield_gap_lines_vs_sp500_drawdown_1976_2026.png`
  - Long-run line chart from 1976 to 2026.
  - Blue line: US-Japan yield gap.
  - Black line: S&P 500 drawdown from prior high.

- `figures/us_japan_10y2y_monthly_true_1976_2026.png`
  - Strict monthly 2Y/10Y comparison for the US and Japan.

- `figures/us_japan_10y2y_daily_true_2020_2026.png`
  - Strict daily 2Y/10Y comparison from 2020 onward.

- `figures/us_japan_long_short_proxy_1960_2026.png`
  - Long-short proxy context back toward 1960.
  - This is not a strict 10Y-2Y chart.

## Data

- `data/us_japan_yield_gap_bars_vs_sp500_monthly_1976_2026.csv`
  - Monthly combined dataset used for long-run charts.

- `data/us_japan_yield_gaps_vs_sp500_recent.csv`
  - Daily recent dataset used for 2020 onward charts.

## Archive

Earlier chart variants are kept in `figures/archive/` so the project root stays
clean without deleting exploratory work.

## Sources

- FRED: US Treasury yield series and S&P 500 recent data.
- Japan Ministry of Finance: JGB yield curve data.
- ECB: Japan 10Y benchmark yield.
- DataHub/Shiller: long-run S&P 500 monthly price history.
