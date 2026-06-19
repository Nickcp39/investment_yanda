# Market + Macro Indicator Panel

Reusable daily panel of market & macro indicators. Built by
[`scripts/market_data_download.py`](../../scripts/market_data_download.py).

Last built: 2026-06-19 · range 2010-01-01 → today · **16 series**.

## Files

- **`market_panel.xlsx`** — the workbook to open:
  - `metadata` — catalog of every series (label, source, ticker/id, unit, date range, n_obs).
  - `daily` — all series aligned on date (wide), 2010→today.
  - `us_japan_yield_gap` — US/JP 2Y+10Y yields, term spreads, and the **US-JP 10Y differential (`DIFF_10Y`)**, merged from `../us_japan_yield_curve_sp500/`.
- **`data/<LABEL>.csv`** — one tidy `date,value` CSV per series (for programmatic use / diffing).

## What's in it

| Group | Series |
|---|---|
| Equity indices | SPY, QQQ, IWM, SOXX |
| Commodities | GOLD (`GC=F`), WTI (`CL=F`), BRENT (`BZ=F`) |
| Crypto | BTC |
| FX / dollar | DXY, USDJPY |
| US rates | US5Y_FVX, US10Y_TNX, US30Y_TYX |
| Credit (proxy) | HYG, LQD |
| Spreads / 美日利差 | `us_japan_yield_gap` sheet → `DIFF_10Y`, `US_10Y2Y`, etc. |

## Sources

- **Yahoo Finance v8 chart API** — all 15 price/rate series (live, works here). Prices are dividend-adjusted closes.
- **Local merge** — US-Japan yield data reused from `../us_japan_yield_curve_sp500/data/` (daily since 2020; monthly back to 1976 lives in that folder).
- **FRED** — *blocked in this environment* (returns empty / times out, same as Stooq). The script keeps best-effort FRED entries (longer-history 2Y, term spread, true HY OAS credit spread); run from an open network — or add a FRED API key — to fill them in.

## Gotchas (read before analyzing)

- **Rate indices are already in percent** (no scaling). `^TNX`/`^FVX`/`^TYX` = the yield directly (e.g. `4.49` = **4.49%**) — verified against history: 10Y = 0.50% at the 2020 COVID low, 4.99% at the 2023 peak.
- **BTC trades weekends.** The `daily` sheet is an outer join, so weekend rows have BTC/commodity values but `NaN` for SPY/QQQ etc. Filter to SPY's calendar (or `.dropna(subset=['SPY'])`) for a TradFi-only view.
- **Credit = ETF proxies.** HYG/LQD are *prices* (risk-on/off proxies), not true option-adjusted spreads. The real HY OAS is the FRED `SPREAD_HY_OAS` series (blocked here).

## Re-run / extend

```bash
# refresh to today (default start 2010-01-01)
.venv/Scripts/python.exe scripts/market_data_download.py

# custom range
.venv/Scripts/python.exe scripts/market_data_download.py --start 2014-01-01 --end 2026-06-19
```

To add an indicator: add one row to the `YAHOO` (or `FRED`) dict at the top of the script and re-run — output overwrites idempotently.
