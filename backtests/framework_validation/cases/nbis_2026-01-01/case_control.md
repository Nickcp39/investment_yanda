# 00 Freeze Case — NBIS 2026-01-01

## 1. Case Identity

- Ticker: NBIS
- Company: Nebius Group N.V.
- Exchange / share class: Nasdaq common stock (Class A); ex-Yandex N.V., Amsterdam-domiciled
- Pipeline version: lean_six_module_v0
- Case type: P1 Lean Case
- Runner scope: as-of 2026-01-01 only (BLIND)
- Scorer scope: outcome evidence after locked decision only (`outcome_score.md`)

## 2. Time Boundary

- **As-of date: 2026-01-01**
- Price date: 2025-12-31 close (last trading day on or before as-of)
- As-of price: **to be confirmed by Runner** from historical data (2025-12-31 close)
- Shares outstanding: Runner to use latest figure disclosed on or before as-of (≈ Q3 2025 reporting)
- Currency: USD

## 3. Decision Question

Would the lean six-module pipeline, using **only information public on or before 2026-01-01**, have identified NBIS as an asymmetric AI-infrastructure opportunity deserving at least a starter position — or dismissed it as an over-valued / over-concentrated neocloud?

Expected output (locked in `decision_card.json` before any scoring):

- New-money decision: REJECT / WATCH / STARTER / CORE
- Existing-position decision: EXIT / TRIM / HOLD / ADD
- Suggested initial + max size, buy-below, starter/add/trim zones
- Binding constraint, kill criteria, `runner_dissent`

## 4. Allowed Evidence (public on or before 2026-01-01)

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| SEC filings | filed ≤ 2026-01-01 | FY2024 20-F; any 6-K furnished through 2025 |
| Company releases / shareholder letters | published ≤ 2026-01-01 | incl. Q1/Q2/Q3 2025 results (Q3 reported ~2025-11-11) |
| Earnings call transcripts | dated ≤ 2026-01-01 | through the Q3 2025 call |
| Contract / partnership announcements | announced ≤ 2026-01-01 | e.g. Microsoft deal (2025-09-08); verify any Meta announcement date before use |
| Historical price / market cap / share count | dated ≤ 2026-01-01 | 2025-12-31 close and prior only |
| Dated news / market narrative | published ≤ 2026-01-01 | narrative context only, not core proof |
| Industry / peer context | published ≤ 2026-01-01 | neocloud / GPU / power context |
| Local notes / KOL / video | topic leads / sentiment only | never core proof |

## 5. Forbidden Evidence Before Locked Verdict

- **Q4 2025 / full-year 2025 results and the FY2025 20-F** (reported/filed in 2026 — AFTER cutoff).
- Any 2026 quarterly result, guidance, financing, contract, partnership, product update, or index event.
- Any stock price, market cap, or performance after 2025-12-31.
- Any later analyst action, guru/institutional action, or news dated after 2026-01-01.
- Any outcome-aware wording (e.g. "it later rallied", "as we now know", "the stock went to $X").
- The existing `companies/nbis/` research folder and `companies/nbis.md` — they contain post-cutoff data and outcome; **the Runner must not read them.**

## 6. Freeze Checklist

- [x] As-of date fixed (2026-01-01).
- [x] Price date fixed (2025-12-31 close; exact price Runner-confirmed).
- [x] Allowed evidence listed.
- [x] Forbidden evidence listed.
- [x] Runner output separated from scorer output.
- [x] Outcome scoring isolated in `outcome_score.md` (written only after verdict locked + audited CLEAN).

## 7. Roles

- **Runner** (blind agent): produces the P1 Lean Case files; locks `decision_card.json`; does not score.
- **Lookahead Auditor** (checker agent): verifies every source date ≤ 2026-01-01 and no outcome-aware language → `lookahead_audit.md` = CLEAN or LEAK. A LEAK voids the case.
- **Scorer** (orchestrator, post-lock): writes `outcome_score.md` comparing the locked verdict to the actual outcome and to the full-information memo (`companies/nbis/memo-v1.md`).
