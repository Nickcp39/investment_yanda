# GEV Research Run — Layer 3/4: Financials & Accounting + One-Off Reconciliation

- Run date: 2026-06-19
- Method: decomposition of the deep buy-side evidence pack; primary figures cross-confirmed against GEV Q1'26 earnings call (S3) and Dec 2025 investor update (S4) via WebFetch 2026-06-19. FY2025 10-K (S1) and Q1'26 10-Q (S2) are the primary anchors.
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Claims here are NOT yet promoted to facts. Every figure must pass through `../claim_ledger.csv` (source ID + status + confidence) before use in `../facts.md`, analysis, or memo.

---

## 0. THE HEADLINE PROBLEM (read this first)

GE Vernova's trailing/headline GAAP numbers are **heavily distorted by three one-offs** that all flatter the same period. A screener will show TTM net income ~$9.4B and EV/EBITDA ~85x; both are wrong as a read on earning power. The three distortions:

| # | One-off | Period | Size | Effect | Source |
|---|---|---|---:|---|---|
| 1 | **Tax valuation-allowance release** | FY2025 | ~$2.9B | Inflates FY2025 net income ($4.9B) — non-operating, non-cash | [PRIMARY] S1 |
| 2 | **M&A gains (Prolec remeasurement + Proficy sale)** | Q1'26 | ~$4.5B | Inflates Q1'26 net income ($4.745B) — primarily the Prolec buy-in remeasurement, **excluded from adjusted EBITDA** | [PRIMARY] S3 / S2 |
| 3 | **Working-capital / contract-liability inflow** | Q1'26 | ~$5.3B benefit (contract-liability line ~+$5.6B) | Flatters Q1'26 FCF ($4.8B) — customer reservation deposits, deferred-revenue timing, **not earned profit** | [PRIMARY] S3 / S2 |

> **Net:** TTM net income ~$9.4B double-counts (1)+(2). The clean reads are (a) **FY2025 operating income $1.39B**, (b) **2026 guide adjusted EBITDA margin 12–14%** (≈ $5.7–6.4B on $44.5–45.5B revenue), and (c) **FCF normalized below the $4.8B Q1 print** once advance-payment timing is stripped. Use the forward, adjusted figures — not trailing GAAP.

---

## 1. FY2025 ACTUALS (first clean full year post-spin)

[PRIMARY] S1 (FY2025 10-K, gev-20251231, filed Feb 2026):
- **Revenue $38.07B, +9% YoY.**
- **Operating income $1.39B**, up ~$0.9B YoY — the cleanest profitability read for FY2025.
- **Net income $4.9B** — **includes a ~$2.9B tax valuation-allowance release** (non-operating). Strip it: net income attributable to operations is ~$2.0B-ish, and even that carries other below-the-line noise. **Do not read $4.9B as operating earning power.**
- **Free cash flow $3.7B**, >2x FY2024's $1.7B. This is a *genuine* improvement (down-payment-rich Power orders + Electrification growth) and is cleaner than net income, though it too benefits from advance-payment timing at the margin.

Segment direction (FY2025 → trajectory): Power and Electrification margins inflecting up; Wind still loss-making. Detail in §3.

## 2. Q1'26 ACTUALS (the most one-off-laden quarter)

[PRIMARY] S2 (Q1'26 10-Q, gev-20260331) + S3 (call, 2026-04-22):
- **Revenue $9.34B, +16% YoY.**
- **Net income $4.745B** — but **~$4.5B is M&A gains** (call: *"we recognized $4.5 billion of gains from M&A transactions, primarily resulting from the acquisition of Prolec, which were excluded from adjusted EBITDA"*), **plus a ~$0.33–0.6B Proficy divestiture gain**. (Pack split it ~$4.0B Prolec + $0.33B Proficy; reconciled here to the call's $4.5B M&A total + Proficy.) **Operating/earned Q1 net income is a small fraction of $4.745B.**
- **Q1 FCF $4.8B** — **flattered by a ~$5.3B working-capital benefit** (call: *"working capital was a $5.3 billion cash benefit"* from higher Power down-payments + Electrification orders; the contract-liability line specifically ~+$5.6B). These are **customer advances on turbine reservations** — they are a powerful *demand* signal but are **deferred revenue, not earned profit**. Normalized Q1 FCF is materially below $4.8B.
- **Cash $10.17B**; **gross debt/EBITDA <1x** — investment-grade, ample liquidity.

## 3. SEGMENT FINANCIAL QUALITY

[PRIMARY] S3. The economics that matter sit at the segment level (group GAAP is one-off noise):

**Q1'26 segment EBITDA margins:**
| Segment | Q1'26 margin | YoY change | Read |
|---|---:|---|---|
| **Power** | **16.3%** | +~500 bps | Inflecting hard; the gas-turbine + services engine |
| **Electrification** | **17.8%** | +590 bps | Short-cycle, capacity-constrained, rising fast |
| **Wind** | **−$382M EBITDA loss** | worse (vs −$146M Q1'25) | Dilutive; loss *widened* |

**2026 guide (segment):** Power 17–19%, Electrification 18–20%, **Wind ~$400M EBIT loss for the year**.
**2028 targets:** Power **22%**, Electrification **22%**, Wind **6%** (on *declining* Wind revenue); **company-wide ~20% EBITDA on ~$52B revenue** [PRIMARY] S4.

> Power + Electrification carry the company. Wind is a structural drag whose *best* outcome management underwrites is "small profit on a shrinking business" by 2028. The margin ramp (16% → 22% Power/Electrification) is the core of the base-case value — and is partly *cyclical pricing* (see L5-6 raw), not purely structural.

## 4. 2026 GUIDANCE (raised) — the clean forward anchor

[PRIMARY] S3, confirmed by WebFetch 2026-06-19:
- **Revenue $44.5–45.5B**
- **Adjusted EBITDA margin 12–14%** → implied **adj EBITDA ≈ $5.7–6.4B**
- **FCF $6.5–7.5B** (note: FCF benefits from continued advance payments → normalized run-rate lower)

These forward, *adjusted* figures — not trailing GAAP — are what the valuation must use. See `../financials/financial_quality.md` and `../valuation.md`.

## 5. BALANCE SHEET & CAPITAL ALLOCATION (cash side)

[PRIMARY] S1/S4/S5:
- Cash $10.17B (Q1'26); gross debt/EBITDA <1x.
- Funded the **$5.275B Prolec buy-in (Feb 2026, ~half cash / half debt)** and a **$10B 2025–28 capex/R&D program** while maintaining IG and returning ≥⅓ of cash to shareholders (~$3.6B in 2025; dividend doubled to $2.00/yr; buyback $6B→$10B, $3.3B spent by Dec 3 2025). Capital-allocation detail in L7-8 raw + `../operator_underwriting.md`.

---

## Analyst comments (NOT facts — flag for module write-up)

- The **single most important accounting message** for GEV is the one-off reconciliation. Any analyst who anchors on trailing net income or screener EV/EBITDA will badly misjudge the multiple. Carry this through `financials/`, `valuation.md`, `model/`.
- **Open gap:** a clean *normalized-FCF* bridge that strips the advance-payment timing is not yet built from disclosure — flagged as a gap in `../facts.md` and `../research_status.md`.
- The FCF *quality* question (how much of $6.5–7.5B 2026 FCF is advance-payment timing vs earned) is the key unknown for the valuation's FCF multiple.
