# Log-Linear Trend Channel — SPY / QQQ

## SPY — through 2026-06-18, **$746.74**

| window | n | trend CAGR | current vs trend | σ | verdict |
|---|---:|---:|---:|---:|---|
| full | 4140 | 13.6% | +12.1% | +1.55 | 偏热 hot (+1..+2σ) |
| 10y | 2514 | 14.1% | +10.5% | +1.26 | 偏热 hot (+1..+2σ) |
| 5y | 1256 | 14.4% | +9.8% | +1.01 | 偏热 hot (+1..+2σ) |

**Speed:** trailing-1y growth +26.7% vs full-history CAGR 13.6% -> 超速 accelerating

## QQQ — through 2026-06-18, **$740.62**

| window | n | trend CAGR | current vs trend | σ | verdict |
|---|---:|---:|---:|---:|---|
| full | 4140 | 18.7% | +16.4% | +1.52 | 偏热 hot (+1..+2σ) |
| 10y | 2514 | 19.3% | +14.2% | +1.12 | 偏热 hot (+1..+2σ) |
| 5y | 1256 | 17.6% | +19.4% | +1.32 | 偏热 hot (+1..+2σ) |

**Speed:** trailing-1y growth +40.7% vs full-history CAGR 18.7% -> 超速 accelerating

---

Caveat: the 2010→ window is an almost-uninterrupted bull (post-GFC + ZIRP + AI),
so the full-history trend slope is steep and 'fair value' is biased high.
Read the 10y/5y rows as sensitivity. This is a temperature/mean-reversion gauge,
not a timing signal; the trend itself can re-rate.

Built by `scripts/log_trend_channel.py` from `macro/market_panel/data/`. Data through 2026-06-18.