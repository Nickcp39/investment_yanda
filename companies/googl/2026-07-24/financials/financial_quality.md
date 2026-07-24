# GOOGL Financial Quality / Accounting Reconstruction (M4) — Q2 2026 REFRESH

Last updated: 2026-07-24 · Module M4 Financial Reality · role: warning
Signal: **−2** (was −1 at 2026-06-19) · confidence: high

> All figures traced to `claim_ledger.csv` (primary A1) / `raw/q2_2026_primary_extracts.md`. Owner-earnings bridge in `model/owner_earnings_bridge.csv`.

---

## 0. Module verdict (one line)

**The prior dossier WARNED that revenue was growing while FCF stalled because capex was eating it. In Q2 2026 that warning MATERIALIZED: free cash flow went NEGATIVE (−$5.9B), TTM FCF fell to $53.3B (−20% YoY), capex hit a record $44.9B (115% of quarterly OCF), buybacks stayed at zero while the share count rose, and long-term debt doubled — all while GAAP net income printed +298% on a $99B non-cash equity gain. Accounting is not fraudulent; but the gap between reported earnings and owner earnings is now EXTREME, and the cash reality deteriorated. Signal worsens −1 → −2.**

---

## 1. Accounting → economics: the net-income mirage got bigger

Q2 net income $112,193M (+298%), diluted EPS $9.11 (+294%). **$99.0B of pre-tax "other income" is a non-cash unrealized gain on equity securities** (non-marketable securities jumped $68.7B → $131.5B on the balance sheet). It raised tax/NI/EPS by $21.9B / $77.1B / **$6.26** respectively. Strip it and clean diluted EPS ≈ **$2.85**. The clean growth read remains **operating income +30%**. This is the SAME distortion as Q1'26 (a $36.9B equity gain), now ~2.7x larger. [GOOG.A1.2026Q2.007/.008/.019]

**The market saw through it:** revenue and EPS beat consensus, yet the stock fell ~7%. Investors priced the negative FCF and the raised capex guide — a real-world validation of "owner earnings > reported net income."

## 2. Owner-earnings bridge (TTM through Q2'26) — built off OPERATING income

Full line-by-line in `model/owner_earnings_bridge.csv`. Because net income is dominated by the equity gain, the honest base is operating income (fully primary):

| Item | TTM (through Q2'26) | Note |
|---|---:|---|
| Operating income | $147,628M | FY25 129,039 − H1'25 61,877 + H1'26 80,466 (primary-derived) |
| − Normalized tax @ ~16% | −$23,620M | Alphabet structural rate; GAAP rate distorted by the equity-gain tax |
| + Normalized net interest/investment income | +$1,500M | excludes ALL equity-security gains |
| = Normalized operating earnings | **~$125,508M** | |
| + D&A | +$26,000M | TTM depreciation of P&E (H1'26 actual $13,586M, annualizing ~$27B and rising) + small amort |
| − SBC (real cost) | −$30,294M | TTM; buybacks paused so dilution is NAKED |
| − Maintenance capex — GROWTH read (= D&A) | −$26,000M | implies ~$106B of $132.4B TTM capex is optional growth |
| **= Owner earnings (growth read)** | **~$95B** | |
| − Maintenance capex — DEFENSIVE read (~50% capex) | −$66,201M | half the AI capex is required to hold the moat |
| **= Owner earnings (defensive read)** | **~$55B** | |

**TTM owner-earnings range ≈ $55B (defensive) – $95B (growth), midpoint ~$75B.** vs reported net income $244B TTM → reported overstates owner earnings ~2.6–4.4x.

**The harsh cash cross-check:** TTM FCF $53.3B − TTM SBC $30.3B = **~$23B of cash owner earnings after real dilution cost** — a ~0.6% yield on a $3.885T market cap. The negative-FCF quarter is what exposes this floor. (Note: owner-earnings midpoint $75B is HIGHER than the prior $51–82B range because operating income grew +30%; but the CASH read fell — the growth read now requires believing $106B of annual capex is discretionary, which the negative FCF and the RAISED $205B guide argue against.)

## 3. Red-flag check (Buffett §2/§8) — more lights on than in June

| Red flag | June 2026 | Q2 2026 | Evidence |
|---|---|---|---|
| Revenue up but owner-earnings/share stalls | 🔴 | **🔴 worse** | FCF/share $6.06 (FY25) → $5.32 (Q1'26 TTM) → **$4.36 (Q2'26 TTM)**, −28% from peak, while share count RISES |
| Capex faster than durable revenue | 🔴 (strongest) | **🔴 firing** | capex TTM $132.4B; **Q2 capex/OCF 115%**, TTM 71.3% (>70%); guide RAISED to $195–205B, 2027 higher |
| Free cash flow | 🟡 stalled | **🔴 NEGATIVE** | Q2 FCF −$5.9B; TTM $53.3B (−20% YoY) |
| Buybacks vs dilution | 🔴 paused | **🔴 still paused, dilution naked** | repurchases $0; shares 12,088M → 12,230M; +$49.6B equity + preferred issued |
| Net income inflated by one-offs | 🔴 ($36.9B) | **🔴 bigger ($99.0B)** | equity-securities gain = $6.26 of $9.11 EPS |
| Leverage / capital-structure shift | 🟡 | **🟡→🔴 escalating** | LT debt $46.5B → **$98.2B** (~doubled); external funding now core to the capex plan |

**Not fraud, not a survival risk** (liquidity is enormous: $242B cash+marketable). But every light that mattered is now brighter, and the FCF light turned red.

## 4. What genuinely IMPROVED (steelman the growth read)

Intellectual honesty requires flagging the bull-side evidence, which is real:
- **Cloud is converting capex to high-margin revenue:** Cloud op margin 20.7% → **35.6%**, op income tripled to $8.8B, backlog **$513.9B (+$54B QoQ)**. This is the "incremental ROIC holds" disconfirming evidence the June bear case needed.
- **Operating income +30%** and consolidated margin 34% — the operating engine is compounding, not breaking.
- **Search resilient (+17%)** with AI features additive to query growth — the F1 "AI erodes search monetization" leg is not showing up.

So the negative FCF is, on the bull read, a *choice* to invest into proven demand, not a symptom of a broken business. The problem is that this read is not yet confirmable (TPU/cloud revenue mostly lands 2027) and it is contradicted by the cash statement today.

## 5. Signal rationale: why −2 (not −1)

The June −1 was "warning, not veto." The rule the lab runs on: when the *specific bear mechanism you flagged materializes*, the signal must worsen. K-B (the capex black hole) has now substantially fired — FCF negative, TTM capex/OCF >70%, FCF/share −28%, dilution naked, debt doubled. That is a −2 on *financial reality* independent of price (M6 handles price). It is not −2-as-veto (no bankruptcy risk; and Cloud offers a genuine growth-read offset), so the business verdict stays "good" and the M5 trap stays a valuation/capex trap, not a death spiral. But M4 must register that the thing we said to watch for happened.

## OPEN (owner-earnings uncertainty sources — unchanged and now more binding)
- Maintenance vs growth capex split (the $40B swing in the OE range).
- Disclosed capex hurdle rate / incremental ROIC (K-C: still absent).
- FY2025 depreciation absolute value (used H1'26 actual $13.586B to anchor TTM ~$26B; verify vs 10-K).
- Timing of the FCF inflection the bull case requires (post-2027).
