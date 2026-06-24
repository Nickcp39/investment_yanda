# 00 Freeze Case — HWM 2024-05-15

## 1. Case Identity

- Ticker: HWM
- Company: Howmet Aerospace Inc.
- Exchange / share class: NYSE common stock; created April 2020 from the Arconic Inc. separation (Howmet Aerospace vs Arconic Corp.)
- Pipeline version: lean-6module-v1.1
- Case type: P1 Lean Case
- Runner scope: as-of 2024-05-15 only (BLIND)
- Scorer scope: outcome evidence after locked decision only (`outcome_score.md`)

## 2. Time Boundary

- **As-of date: 2024-05-15**
- Price date: 2024-05-15 close (the as-of date is a trading day — Wednesday)
- As-of price: **$82.75** (2024-05-15 close, Yahoo v8; raw close = nominal, no splits since)
- Shares outstanding: 408,169,673 common as of 2024-03-31 (Q1 2024 10-Q); ~412M diluted weighted-average (Q1 2024)
- As-of market cap: **~$33.8B** ($82.75 × 408.17M)
- Currency: USD

## 3. Decision Question

Would the lean six-module pipeline, using **only information public on or before 2024-05-15**, have identified HWM — a richly-priced jet-engine-component leader riding an aerospace aftermarket/spares upturn, sitting at its 52-week high right after a guidance raise — as a quality compounder deserving at least a starter position, or dismissed it as a too-expensive, late-cycle chase?

Expected output (locked in `decision_card.json` before any scoring):

- New-money decision: REJECT / WATCH / STARTER / CORE
- Existing-position decision: EXIT / TRIM / HOLD / ADD
- Suggested initial + max size, buy-below, starter/add/trim zones
- Binding constraint, kill criteria, `runner_dissent`

## 4. Allowed Evidence (public on or before 2024-05-15)

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| SEC filings | filed ≤ 2024-05-15 | FY2023 10-K (filed 2024-02-13); Q1 2024 10-Q (filed ~2024-05-02) |
| Company releases | published ≤ 2024-05-15 | Q4/FY2023 release (2024-02-13); Q1 2024 release (2024-05-02) |
| Earnings call transcripts | dated ≤ 2024-05-15 | through the Q1 2024 call (2024-05-02) |
| Historical price / market cap / share count | dated ≤ 2024-05-15 | 2024-05-15 close and prior only |
| Dated news / market narrative | published ≤ 2024-05-15 | narrative context only, not core proof |
| Aerospace-industry / peer context | published ≤ 2024-05-15 | Boeing/Airbus build rates, GTF/spares, IATA traffic, defense, Class 8 truck — all dated ≤ as-of |
| Local notes / KOL / video | topic leads / sentiment only | never core proof |

## 5. Forbidden Evidence Before Locked Verdict

- **Any HWM quarterly result after Q1 2024** (Q2 2024 onward) and the **FY2024 10-K** (filed 2025) — AFTER cutoff.
- Any 2024 (post-05-15) / 2025 / 2026 guidance, financing, buyback, dividend, or contract event.
- Any stock price, market cap, or performance after 2024-05-15 (HWM trades far higher in mid-2026 — explicitly excluded).
- Any later analyst action, guru/institutional action, index event, or news dated after 2024-05-15.
- Any later aerospace build-rate revision (e.g., later FAA 737-cap changes, later Airbus rate reframes, later Class 8 forecast revisions).
- Any outcome-aware wording (e.g. "it later rallied", "as we now know", "the stock went to $X").
- The **live `companies/hwm/` 2026 dossier** and any 2026 HWM analysis in this repo — they contain post-cutoff data and the outcome; **the Runner must not read them.**

## 6. Freeze Checklist

- [x] As-of date fixed (2024-05-15).
- [x] Price date fixed (2024-05-15 close; price Runner-confirmed = $82.75 from Yahoo v8, two endpoints + committed quote CSV).
- [x] Allowed evidence listed.
- [x] Forbidden evidence listed.
- [x] Runner output separated from scorer output.
- [x] Outcome scoring isolated in `outcome_score.md` (written only after verdict locked + audited CLEAN).

## 7. Roles

- **Runner** (blind agent): produces the P1 Lean Case files; locks `decision_card.json`; does not score.
- **Lookahead Auditor** (checker agent): verifies every source date ≤ 2024-05-15 and no outcome-aware language → `lookahead_audit.md` = CLEAN or LEAK. A LEAK voids the case.
- **Scorer** (orchestrator, post-lock): writes `outcome_score.md` comparing the locked verdict to the actual outcome.
