# DCA below the log-trend band — does it 'always win'?

## ^GSPC — 1985-01-01 → 2026-06-22 (41y)

| strategy | buys % of mo | contributed | final value | multiple | IRR (ann) | lots in profit |
|---|---:|---:|---:|---:|---:|---:|
| S0 DCA always | 100% | $499 | $4860 | 9.74x | 9.0% | 100% |
| S1 <= PIT trend | 42% | $499 | $1509 | 3.02x | 4.7% | 100% |
| S2 <= PIT -1σ | 26% | $499 | $1235 | 2.48x | 3.9% | 100% |
| S3 <= PIT -2σ | 7% | $499 | $755 | 1.51x | 1.9% | 100% |
| S4 always +2x<-1σ | 100% | $629 | $5726 | 9.10x | 9.1% | 100% |
| SX <= FULL -1σ (CHEAT) | 13% | $499 | $1252 | 2.51x | 4.0% | 100% |

## ^IXIC — 1985-01-01 → 2026-06-22 (41y)

| strategy | buys % of mo | contributed | final value | multiple | IRR (ann) | lots in profit |
|---|---:|---:|---:|---:|---:|---:|
| S0 DCA always | 100% | $499 | $10675 | 21.39x | 11.7% | 100% |
| S1 <= PIT trend | 35% | $499 | $2334 | 4.68x | 6.4% | 100% |
| S2 <= PIT -1σ | 21% | $499 | $1842 | 3.69x | 5.5% | 100% |
| S3 <= PIT -2σ | 5% | $499 | $902 | 1.81x | 2.6% | 100% |
| S4 always +2x<-1σ | 100% | $605 | $12124 | 20.04x | 11.8% | 100% |
| SX <= FULL -1σ (CHEAT) | 12% | $499 | $1436 | 2.88x | 4.5% | 100% |

---
## Read this before believing any 稳赢 claim
- **Look-ahead**: `SX (CHEAT)` uses the full-sample trend (knows the future) — it looks great and is **not tradeable**. Compare it to `S2 (<= PIT -1σ)`, the honest real-time version.
- **Cash drag + rarity**: dip-only strategies (S1–S3) sit in cash for years in a melt-up, so on EQUAL contributions they can LOSE to plain DCA (S0) on final value even though each buy is cheaper. `S4 (always + double the dip)` is the realistic way to use the band.
- **Regime/survivorship**: this works because the US index trended up and always recovered. Buying 'below trend' on Japan's Nikkei from 1990, or Nasdaq from 2000, left you underwater for 10–30 years — the index-level version of the value trap.

Built by `scripts/log_trend_dca_backtest.py`. PIT warmup = 120 mo. Price indices (ex-dividends).