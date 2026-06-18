# 00 Freeze Case - PYPL 2021-07-29

## 1. Case Identity

- Ticker: PYPL
- Company: PayPal Holdings, Inc.
- Exchange / share class: Nasdaq common stock (NASDAQ: PYPL)
- Pipeline version: lean_six_module_v0
- Case type: P1 Lean Case
- Runner scope: as-of 2021-07-29 only
- Scorer scope: outcome evidence after locked decision only

## 2. Time Boundary

- As-of date: 2021-07-29
- Price date: 2021-07-29 close
- As-of price: $283.17 (Yahoo regular-market close; adj close $280.74)
- Shares outstanding used for market cap: 1,175 million (common shares outstanding at 2021-06-30 per Q2 2021 10-Q)
- Approximate as-of equity value: ~$332.7 billion
- Currency: USD

## 3. Decision Question

Would the pipeline have treated PayPal at a near-all-time-high valuation as a durable digital-payments compounder worth owning, or flagged it as an expensive, decelerating-growth name facing an eBay-migration revenue drag and rising competition (i.e., a de-rating trap)?

Expected output (future blind test, NOT produced this round):

- New money decision: REJECT / WATCH / STARTER / CORE
- Existing position decision: EXIT / TRIM / HOLD / ADD
- Position size and monitor plan

## 4. Allowed Evidence

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| Company releases | Public on or before 2021-07-29 | PayPal Q2 2021 earnings release (Jul 28 2021), Feb 11 2021 Investor Day targets, Apr 20 2021 Venmo crypto release are allowed. |
| SEC filings | Filed on or before 2021-07-29 | PYPL Q2 2021 10-Q (period ended 2021-06-30) and the Q2 2021 8-K earnings exhibit are allowed. |
| Earnings call | Held on 2021-07-28 | Q2 2021 earnings call (CEO Dan Schulman, CFO John Rainey) is allowed. |
| Trading / market data | Dated on or before 2021-07-29 | 2021-07-29 close and the as-of-era price path (incl. Jul 26 2021 ATH) are allowed. |
| Industry / peer context | Published on or before 2021-07-29 | Square Q1 2021 results (May 6 2021) and dated BNPL-competition context are allowed. |
| News / commentary | Public on or before 2021-07-29 | Use only as narrative context, not core proof. |

## 5. Forbidden Evidence Before Locked Verdict

- Q3 2021 results (Nov 2021) and any later filings, releases, or guidance.
- The Pinterest acquisition rumor (Oct 2021) and the Amazon-Venmo checkout deal (announced Nov 8 2021).
- The Block (Square)-Afterpay acquisition (announced Aug 1-2 2021) and any other post-as-of M&A.
- Any 2022+ guidance cuts, user-growth deceleration, the abandonment of the 750M-account target, or later management/strategy changes.
- Alex Chriss as CEO (2023) or any later leadership change.
- Any stock performance after 2021-07-29 (no "later fell/collapsed", no 2022-2026 prices).
- Any wording that implies the runner already knows PayPal de-rated.

## 6. Freeze Checklist

- [x] As-of date fixed.
- [x] Price input fixed (2021-07-29 close $283.17; saved to backtests/data/asof_2021-07-29_pypl_quotes.csv).
- [x] Allowed evidence listed.
- [x] Forbidden evidence listed.
- [x] Runner output separated from scorer output.
- [x] Materials-only pack: no decision file written this round.
