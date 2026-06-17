# 00 Freeze Case - SNDK 2025-06-16

## 1. Case Identity

- Ticker: SNDK
- Company: Sandisk Corporation
- Exchange / share class: Nasdaq common stock
- Pipeline version: lean_six_module_v0
- Case type: P1 Lean Case
- Runner scope: as-of 2025-06-16 only
- Scorer scope: outcome evidence after locked decision only

## 2. Time Boundary

- As-of date: 2025-06-16
- Price date: 2025-06-16 close
- As-of price: $44.21
- Shares outstanding used for market cap: 145 million
- Approximate as-of equity value: $6.41 billion
- Currency: USD

## 3. Decision Question

Would the 2025 pipeline have dismissed Sandisk as a messy, newly spun-off NAND cyclical, or would it have identified an asymmetric spin-off / AI-storage-cycle inflection that deserved at least a small starter position?

Expected output:

- New money decision: REJECT / WATCH / STARTER / CORE
- Existing position decision: EXIT / TRIM / HOLD / ADD
- Position size and monitor plan

## 4. Allowed Evidence

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| Company releases | Public on or before 2025-06-16 | Sandisk and Western Digital official releases are allowed. |
| SEC filings | Filed on or before 2025-06-16 | SNDK Q3 FY2025 10-Q and secondary offering filings are allowed. |
| Trading / corporate action data | Dated on or before 2025-06-16 | Nasdaq spin-off notice and 2025-06-16 close are allowed. |
| Industry context | Published on or before 2025-06-16 | TrendForce 2025-05-26 NAND / enterprise SSD note is allowed. |
| News / commentary | Public on or before 2025-06-16 | Use only as narrative context, not core proof. |

## 5. Forbidden Evidence Before Locked Verdict

- Fiscal Q4 2025 results, fiscal 2025 10-K, and any later filings or releases.
- Later Sandisk financial results, customer agreements, buybacks, index additions, analyst upgrades, and later NAND pricing.
- Any stock performance after 2025-06-16.
- Any wording that implies the runner already knows Sandisk became a large winner.

## 6. Freeze Checklist

- [x] As-of date fixed.
- [x] Price input fixed.
- [x] Allowed evidence listed.
- [x] Forbidden evidence listed.
- [x] Runner output separated from scorer output.
- [x] Outcome scoring isolated in `outcome_score.md`.
