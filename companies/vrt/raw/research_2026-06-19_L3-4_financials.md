# VRT Research Run — Layer 3/4: Financials, Orders/Backlog Series & the Q1'26 Withholding

- Run date: 2026-06-19
- Method: decomposition of the deep buy-side pack (As of 2026-06-19, price $333.05); primary anchors = VRT Q1 2026 release/8-K (2026-04-22, S1), Q1 2026 call transcript (S2), Q4/FY2025 release (~2026-02-11, S3), 2026 Investor Conference deck (2026-05-19, S4). Secondary: stockanalysis.com (S6).
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Claims here are NOT yet promoted to facts. Every figure must pass through `../claim_ledger.csv` (source ID + status + confidence) before use in `facts.md`, analysis, or memo.
- Mapped claims: C001–C015, C027 (orders-withholding flag), C032

---

# Vertiv Holdings (NYSE: VRT) — Financial Base, Orders/Backlog Series & Disclosure Flag

*As-of 2026-06-19. Latest reported period: Q1 2026 (reported Apr 22 2026). US domestic filer (10-K / 10-Q / 8-K). Non-GAAP figures ("adjusted") are management-defined; flagged where they diverge from GAAP. All figures USD.*

---

## 1. FY2025 ACTUALS (audited base)

| Metric | FY2025 | Read | claim_id |
|---|---:|---|---|
| Net sales | **$10,229.9M** | organic **+26%** — broad-based, AI-led | C001 |
| Adjusted operating margin | **20.4%** | up from high-teens; real expansion, not mix noise | C002 |
| Adjusted free cash flow | **$1,887.4M** | ~18.4% of sales — strong conversion for a hardware-heavy model | C003 |
| Backlog (year-end) | **$15.0B (+109% YoY)** | the headline visibility metric; converts ~12–18 months, cancellable | C004 |
| Net cash | **~$0.76B** | balance-sheet optionality (M&A + buybacks) | C028 |

**One-line read:** FY2025 is a top-tier, *accelerating* industrial result — high-20s organic growth, ~20% adjusted operating margin, ~$1.9B adjusted FCF, and a backlog that more than doubled. This is the opposite of a low-quality cyclical: margins expanded *while* the company grew fast.

---

## 2. THE ORDERS / BACKLOG SERIES (the demand gauge — and where it goes dark)

This is the single most decision-relevant series for VRT, because orders / book-to-bill is the **near-real-time** read on whether the AI-capex wave is still accelerating. The series accelerated hard through Q4'25 — and then the headline was withheld in Q1'26.

| Period | Organic orders | Book-to-bill | Backlog | Source |
|---|---|---|---|---|
| Q3 2025 | **+60%** | (not isolated) | — | S3 (C006) |
| Q4 2025 | **+252%** | **~2.9x** | **$15.0B (+109% YoY)** | S3 (C005) |
| TTM (through Q4'25) | **+81%** | — | — | S3 (C005) |
| **Q1 2026** | **WITHHELD** | **WITHHELD** | **WITHHELD** | S1/S2 (C012) |

**🚩 The withholding (binding gap).** After a blow-out Q4 (organic orders +252%, book-to-bill ~2.9x, backlog +109%), Vertiv **stopped disclosing the headline quarterly orders / book-to-bill / backlog figures in Q1 2026.** Management offered only qualitative comfort: orders are "up YoY" for FY26, and the backlog is "elongated" (i.e., longer-dated conversion). (C012, C013)

- The **fact** of non-disclosure is HIGH confidence (it is simply absent from the Q1'26 release and the call gave words, not numbers).
- The **underlying Q1'26 orders number is UNVERIFIABLE** from public sources — it cannot be promoted to `facts.md` as a value.
- **Why it matters:** this is the cleanest gauge for kill-criterion (a) (book-to-bill <1.0 for >1 quarter). Removing it *degrades the signal needed to underwrite the kill* on a name with no contracted floor and the highest capex-beta in the basket. After a +252% quarter, silence is itself a *soft negative* — the "backlog silence" risk (S8). It is surfaced consistently in `../claim_ledger.csv` (C012), `../inversion_map.md`, `../monitor.md`, and `../research_status.md`.

> Interpretive caution (avoid over-reading): "elongated backlog" can be benign — large hyperscaler campus orders are inherently lumpy and longer-dated, and a company lapping +252% will mechanically show decelerating *growth* even on strong absolute orders. The issue is not that orders are necessarily weak; it is that **we can no longer see them**, so we cannot *verify* the kill either way. Loss of signal ≠ proof of weakness, but on a no-floor / highest-beta name it is the wrong number to lose.

---

## 3. Q1 2026 ACTUALS (the quarter that beat on P&L but went dark on orders)

| Metric | Q1 2026 | YoY | Read | claim_id |
|---|---:|---|---|---|
| Net sales | **$2,650M** | **+30% total / +23% organic** | total includes FX/M&A; organic is the cleaner read | C007 |
| — Americas organic | — | **+44%** | the engine; AI-capex-geared region | C008 |
| — EMEA organic | — | **−29%** | **not immune** — a real regional air-pocket | C008 |
| — APAC organic | — | **+12%** | steady | C008 |
| Adjusted operating margin | **20.8%** | **+430bps** | beat its own guide by **~180bps** | C009 |
| Adjusted EPS | **$1.17** | **+83%** | | C010 |
| Adjusted FCF | **$653M** | **+147%** | FCF growth outpacing earnings | C011 |

**Two things to hold together from Q1'26:**
1. **P&L beat is real and ahead of plan** — margin +430bps, beating its own guide by ~180bps; EPS +83%; FCF +147%. Execution quality is top-tier.
2. **EMEA organic −29%** is a genuine demand-breadth crack — VRT is *not* uniformly immune; the strength is concentrated in the Americas (+44%). This matters for the inversion case (regional air-pockets exist even mid-super-cycle).

---

## 4. RAISED FY26 GUIDANCE (at Q1'26)

| Metric | FY26 guide | Note | claim_id |
|---|---|---|---|
| Net sales | **$13.5–14.0B** | implies organic +29–31% | C014 |
| Organic growth | **+29–31%** | acceleration vs FY25 +26% | C014 |
| Adjusted operating margin | **22.8–23.8%** | +~250–340bps over FY25's 20.4% | C014 |
| Adjusted EPS | **$6.30–6.40** | midpoint ~$6.35 → anchors fwd P/E | C014 |
| Adjusted FCF | **$2.1–2.3B** | midpoint ~$2.2B | C014 |

The FY26E EPS midpoint (~$6.35) is the denominator for the ~48–49x forward P/E in `../valuation.md`.

---

## 5. 2030 TARGETS (May-2026 Investor Conference, S4)

- **Organic revenue CAGR 20–22%** (2025 → 2030E) — raised from the 2024 investor-day 12–14%.
- **Adjusted operating margin 27%** — raised from 25%.

These are the *long-duration* numbers the bull case capitalizes. They are credible (margins are tracking ahead, FY26 already guides to 22.8–23.8% vs the 27% 2030 target — see C032), but they are **targets, not facts**, and they assume the hyperscaler capex slope keeps cooperating into 2027+.

---

## 6. FINANCIAL-QUALITY VERDICT (feeds `../financials/financial_quality.md`)

- **Recurring revenue?** Partly — services (lifecycle) is the higher-margin recurring layer; power + thermal hardware is order-driven (backlog-converted), not annuity. No PTC-style floor, no multi-year take-or-pay. (C016, C023)
- **Margin expansion source?** Genuine operating leverage + mix toward higher-value integrated systems + pricing — *not* an accounting tailwind. Q1'26 beat its own guide by ~180bps. (C009, C032)
- **FCF conversion?** Strong and improving ($1.89B FY25 → $2.2B FY26E mid; Q1'26 FCF +147%). (C003, C011)
- **Balance sheet?** Net cash ~$0.76B → optionality for bolt-on thermal M&A (Thermal Key, dry coolers) + modest buybacks; negligible dividend (~0.07%). (C028)
- **The one quality blemish is not in the numbers — it is the disclosure:** the headline orders/B2B/backlog series went dark in Q1'26 (C012/C027). The accounting is clean and high-quality; the *transparency* degraded.

---

## 7. COULD NOT VERIFY / OPEN ITEMS

- **Q1'26 orders / book-to-bill / backlog** — withheld by the company; UNVERIFIABLE from public sources. The single binding gap. Watch Q2'26 (~July 2026) for re-disclosure. (C012)
- **Exact net-cash composition / gross debt vs cash split** — aggregator-sourced "net cash ~$0.76B" (S6); confirm against the 10-Q balance sheet if precision matters.
- **Segment-level (power vs thermal vs services) revenue/margin split** — not isolated in the pack; VRT reports by region + product group in filings; pull the 10-K/10-Q segment note to decompose content-per-rack economics.
- **Multiples (C029)** — aggregator-sourced (S6), intraday; `needs_audit`.

---

**Bottom line for the memo:** VRT's reported economics are top-tier and accelerating — FY25 +26% organic / 20.4% margin / $1.9B FCF, Q1'26 beating its own margin guide by ~180bps, FY26 guide raised, 2030 ceiling raised. The financial *quality* is high. The single blemish is not accounting — it is that the **cleanest forward demand gauge (quarterly orders / book-to-bill) was withdrawn in Q1'26 right after a +252% blow-out**, which is exactly the signal needed to underwrite the kill on the highest-beta, no-floor name in the basket. Verify, don't extrapolate.
