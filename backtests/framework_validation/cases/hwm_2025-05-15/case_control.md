# 00 Freeze Case — HWM 2025-05-15

## 1. Case Identity

- Ticker: HWM
- Company: Howmet Aerospace Inc.
- Exchange / share class: NYSE common stock (single class). Successor to Arconic Inc.; the
  aerospace business retained after the April 1, 2020 spin-off of Arconic Corp.
- Pipeline version: **lean-6module-v1.1**
- Weights version: **none** (qualitative reasoning per `WEIGHTING_HARNESS.md` + `METHODOLOGY.md`)
- Case type: P1 Lean Case
- Runner scope: as-of 2025-05-15 only (BLIND)
- Scorer scope: outcome evidence after locked decision only (`outcome_score.md`, written later by the Scorer)

## 2. Time Boundary

- **As-of date: 2025-05-15**
- Price date: 2025-05-15 close (last settled trading day on or before as-of; a Thursday, full trading day)
- As-of price: **$161.29** (2025-05-15 close), re-derived two independent ways (see `freshness.json`)
- As-of market cap: **~$65.2B** ($161.29 × ~404M shares outstanding at 3/31/25)
- Shares outstanding: ~404M (common, 3/31/25); ~407M diluted weighted average Q1'25
- Currency: USD

## 3. Decision Question

Would the lean six-module pipeline, using **only information public on or before 2025-05-15**, have
identified HWM as a high-quality aerospace-supply compounder deserving at least a starter position —
or judged that the price (a fresh 52-week high after a strong Q1 reaction, ~47x forward earnings) had
already discounted the up-cycle, warranting a WATCH / no-chase?

Expected output (locked in `decision_card.json` before any scoring):

- New-money decision: REJECT / WATCH / STARTER / CORE
- Existing-position decision: EXIT / TRIM / HOLD / ADD
- Suggested initial + max size, buy-below, starter/add/trim zones
- Binding constraint, kill criteria, `runner_dissent`

## 4. Allowed Evidence (public on or before 2025-05-15)

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| SEC filings | filed ≤ 2025-05-15 | FY2024 10-K (filed 2025-02-13); Q1 2025 10-Q (filed ~2025-05-02) |
| Company releases | published ≤ 2025-05-15 | Q4/FY2024 results (2025-02-13); **Q1 2025 results (2025-05-01)** |
| Earnings call transcripts | dated ≤ 2025-05-15 | through the Q1 2025 call (2025-05-01) |
| Historical price / market cap / share count | dated ≤ 2025-05-15 | 2025-05-15 close and prior only |
| Dated news / market narrative | published ≤ 2025-05-15 | narrative context only, not core proof |
| Industry / peer context | published ≤ 2025-05-15 | Boeing/Airbus build rates, deliveries, air-traffic, engine-spares demand |
| Local notes / KOL / video | topic leads / sentiment only | never core proof |

## 5. Forbidden Evidence Before Locked Verdict

- **Q2 2025 results and any 2025-H2 / FY2025 actuals** (reported after cutoff).
- Any 2025-H2 or 2026 quarterly result, guidance update, contract, buyback, dividend, or product update.
- Any stock price, market cap, or performance after 2025-05-15 (the stock is ~$280 in mid-2026 — FORBIDDEN).
- Any later analyst action, rating, price target, or index event dated after 2025-05-15.
- Any outcome-aware wording ("it later rallied", "as we now know", "the up-cycle played out", "the stock went to $X").
- The **`companies/hwm/` LIVE 2026 dossier** and any 2026 HWM analysis in this repo — they contain the
  outcome and post-as-of data; **the Runner must not read them.**

## 6. Freeze Checklist

- [x] As-of date fixed (2025-05-15).
- [x] Price date fixed (2025-05-15 close; exact price Runner-confirmed = $161.29).
- [x] Allowed evidence listed.
- [x] Forbidden evidence listed.
- [x] Runner output separated from scorer output.
- [x] Outcome scoring isolated in `outcome_score.md` (written only after verdict locked + audited CLEAN).

## 7. Roles

- **Runner** (blind agent): produces the P1 Lean Case files; locks `decision_card.json`; does not score.
- **Lookahead Auditor** (checker agent): verifies every source date ≤ 2025-05-15 and no outcome-aware
  language → `lookahead_audit.md` = CLEAN or LEAK. A LEAK voids the case.
- **Scorer** (orchestrator, post-lock): writes `outcome_score.md` comparing the locked verdict to the
  actual outcome.
