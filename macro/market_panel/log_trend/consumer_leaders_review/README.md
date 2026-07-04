# Consumer Leaders Rolling Log-Trend Review

Review universe: KO, PEP, PG, WMT, COST, MCD, CL, KMB, JNJ, PM.
Source: Yahoo Finance chart API adjusted close. This is a review artifact, not a promoted indicator yet.

Built through 2026-06-24.

## Latest

| ticker | name | price | vs 5Y | 5Y CAGR | vs 10Y | 10Y CAGR |
|---|---|---:|---:|---:|---:|---:|
| JNJ | Johnson & Johnson | $240.68 | +30.8% | 6.3% | +27.3% | 7.4% |
| KO | Coca-Cola | $81.07 | +10.7% | 8.9% | +10.3% | 9.3% |
| PM | Philip Morris | $179.01 | +7.8% | 20.6% | +35.6% | 10.6% |
| CL | Colgate-Palmolive | $92.64 | +2.0% | 6.2% | +3.9% | 5.4% |
| WMT | Walmart | $119.66 | +1.7% | 27.8% | +19.1% | 18.2% |
| PEP | PepsiCo | $142.90 | -3.9% | -0.1% | -19.2% | 8.1% |
| PG | Procter & Gamble | $152.89 | -4.3% | 4.4% | -17.2% | 11.0% |
| KMB | Kimberly-Clark | $107.27 | -6.6% | 0.1% | -14.4% | 3.6% |
| MCD | McDonald's | $275.29 | -12.5% | 7.7% | -21.1% | 12.4% |
| COST | Costco | $963.87 | -13.3% | 23.2% | -16.4% | 25.4% |

## 1Y/2Y/3Y Annualized Return If Price Reverts To Trend

| ticker | trend | 1Y | 2Y ann. | 3Y ann. |
|---|---|---:|---:|---:|
| KO | rolling 5y | -1.6% | +3.5% | +5.3% |
| KO | rolling 10y | -0.9% | +4.0% | +5.8% |
| PEP | rolling 5y | +4.0% | +1.9% | +1.2% |
| PEP | rolling 10y | +33.8% | +20.3% | +16.1% |
| PG | rolling 5y | +9.1% | +6.8% | +6.0% |
| PG | rolling 10y | +34.1% | +22.0% | +18.2% |
| WMT | rolling 5y | +25.7% | +26.8% | +27.1% |
| WMT | rolling 10y | -0.7% | +8.4% | +11.6% |
| COST | rolling 5y | +42.2% | +32.4% | +29.2% |
| COST | rolling 10y | +50.0% | +37.1% | +33.1% |
| MCD | rolling 5y | +23.1% | +15.2% | +12.6% |
| MCD | rolling 10y | +42.5% | +26.5% | +21.6% |
| CL | rolling 5y | +4.1% | +5.1% | +5.5% |
| CL | rolling 10y | +1.4% | +3.4% | +4.1% |
| KMB | rolling 5y | +7.2% | +3.6% | +2.4% |
| KMB | rolling 10y | +21.0% | +12.0% | +9.1% |
| JNJ | rolling 5y | -18.7% | -7.1% | -2.8% |
| JNJ | rolling 10y | -15.6% | -4.8% | -0.9% |
| PM | rolling 5y | +11.9% | +16.2% | +17.6% |
| PM | rolling 10y | -18.5% | -5.0% | -0.1% |

## Files

- `consumer_leaders_rolling_dashboard.png`
- `<TICKER>_rolling_log_trend.png`
- `<TICKER>_rolling_log_trend.csv`
- `consumer_leaders_latest.csv`
- `consumer_leaders_reversion_scenarios.csv`