# Fixed-salary DCA + dry-powder dip-buying — where's the balance?

Fixed salary **$100,000/yr**; un-deployed cash earns **4%**; dip trigger = price **≤ PIT −1σ** (real-time, no look-ahead).

## ^GSPC — 1985-01-01→2026-06-22  ($100,000/yr salary, total in $4.16M, cash@4%)

| strategy | final wealth | IRR | avg cash drag |
|---|---:|---:|---:|
| Pure DCA (base=1.0) | $40,486,615 | 9.0% | 0% |
| Pure dip (base=0, dump on -1σ) | $33,523,104 | 8.3% | 4% |

### Balance sweep (deploy 100% dry powder on ≤ −1σ; vary the always-in base)

| base (always-in) | dry-powder for dips | final wealth | IRR | avg cash drag |
|---:|---:|---:|---:|---:|
| 0.00 | 1.00 | $33,523,104 | 8.3% | 4% |
| 0.25 | 0.75 | $35,263,982 | 8.5% | 3% |
| 0.50 | 0.50 | $37,004,859 | 8.7% | 2% |
| 0.60 | 0.40 | $37,701,210 | 8.7% | 1% |
| 0.70 | 0.30 | $38,397,562 | 8.8% | 1% |
| 0.80 | 0.20 | $39,093,913 | 8.9% | 1% |
| 0.90 | 0.10 | $39,790,264 | 8.9% | 0% |
| 0.95 | 0.05 | $40,138,439 | 8.9% | 0% |
| 1.00 | 0.00 | $40,486,615 | 9.0% | 0% |

**Balance point: base ≈ 1.00** (always-invest 100% of salary, keep 0% as dry powder for −1σ dips) → **$40,486,615, IRR 9.0%**.

## ^IXIC — 1985-01-01→2026-06-22  ($100,000/yr salary, total in $4.16M, cash@4%)

| strategy | final wealth | IRR | avg cash drag |
|---|---:|---:|---:|
| Pure DCA (base=1.0) | $88,911,722 | 11.7% | 0% |
| Pure dip (base=0, dump on -1σ) | $48,419,734 | 9.6% | 22% |

### Balance sweep (deploy 100% dry powder on ≤ −1σ; vary the always-in base)

| base (always-in) | dry-powder for dips | final wealth | IRR | avg cash drag |
|---:|---:|---:|---:|---:|
| 0.00 | 1.00 | $48,419,734 | 9.6% | 22% |
| 0.25 | 0.75 | $58,542,731 | 10.3% | 12% |
| 0.50 | 0.50 | $68,665,728 | 10.8% | 6% |
| 0.60 | 0.40 | $72,714,926 | 11.0% | 5% |
| 0.70 | 0.30 | $76,764,125 | 11.2% | 3% |
| 0.80 | 0.20 | $80,813,324 | 11.4% | 2% |
| 0.90 | 0.10 | $84,862,523 | 11.5% | 1% |
| 0.95 | 0.05 | $86,887,122 | 11.6% | 0% |
| 1.00 | 0.00 | $88,911,722 | 11.7% | 0% |

**Balance point: base ≈ 1.00** (always-invest 100% of salary, keep 0% as dry powder for −1σ dips) → **$88,911,722, IRR 11.7%**.

---
## Honest caveats
- The balance point is **fit in-sample** on a 41-yr US bull (1985→). It is the wrong number for a flat market (Nikkei 1990→ would punish dry-powder hoarding for 30 yrs).
- Cash rate held flat at 4%; real T-bills ranged ~0–8% over the window.
- Price indices (ex-dividends): absolute wealth understates ~1.5–2%/yr; the cross-strategy comparison is unaffected.

Built by `scripts/log_trend_dca_balance.py`.