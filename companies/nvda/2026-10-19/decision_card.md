# NVDA Decision Card — as_of 2026-10-16 close, run 2026-10-19 (SELLOFF RERUN + 10-Q READ)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-10-19
**batch** nbis_nvda_selloff_rerun_2026-10-19 · **status** DECISION_DRAFT · **completeness** ~70%
**refresh_of** `companies/nvda/2026-09-05` · **context_label** `price_inside_band_top_10q_explains_the_cash_gap_but_does_not_close_it_receivables_now_the_variable`

> as_of is the **2026-10-16 Friday close**. Run made Monday 2026-10-19 during the session (NVDA ~$216–218
> intraday at fetch time); the in-progress session is never used as as_of_price.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **214.13** (2026-10-16 close; Yahoo + stockanalysis history, delta 0.00%) |
| market cap | **~$5.196T** (24,264M diluted × 214.13) |
| vs prior card ($230.36, 2026-09-04) | **−7.0%** |
| distance from 52-week high $243.37 (intraday 2026-10-06) | **−12.0%** |
| business_verdict | **exceptional** (unchanged) |
| **new_money_verdict** | **WATCH (0%)** — **price is inside the band for the first time; STEP 1 of the trigger is half-closed** |
| existing_position_verdict | **HOLD** |
| suggested initial / max size | **0% / 3–5% once STEP 1 closes** |
| **buy_below** | **BAND $148.30 – $222.44 UNCHANGED** — price is **3.7% below the top** |
| binding_constraint | **OWNER-EARNINGS QUALITY**: the 10-Q shows operating cash flow at 40% of net income, and names the reason (receivables); price is no longer the constraint |

## Six-module signals (net +2; prior +3)

| Module | Role | 07-10 | 09-05 | **10-19** | One line |
|---|---|---:|---:|---:|---|
| M1 Evidence Spine | confidence | +2 | +1 | **+2** | The Q2 FY27 10-Q (filed 08-26) was read via SEC XBRL + document: the open items of 09-05 are now **answered**, not inferred |
| M2 Theme / Mechanism | context | +2 | +2 | **+1** | Q3 guide ~$108B stands; Hugging Face $11.9B acquisition (8-K 09-03). But the demand narrative took two public hits: a report that OpenAI's annualised revenue runs ~$20B below what it signalled (CNBC 10-08, secondary) and hyperscaler/neocloud capex-delay talk; H200 $400M excess-inventory charge (secondary) |
| M3 Profit Pool / Durability | conviction | +2 | +2 | **+2** | 75.0% GM held; Q3 guided 74.0%; ~$99B buyback authorisation |
| M4 Financial Reality | warning | +2 | 0 | **−1** | **The changed leg, now on evidence.** 10-Q: Q2 OCF $24.08B vs NI $59.69B (40%). Bridge: −$7.77B non-cash equity gains, **−$22.4B receivables build (AR $40.7B → $63.1B in one quarter; five customers ≥10% of AR)**, −$5.8B inventory (to $31.6B), −$5.5B prepaid. Payment terms of **90 days to one year** offered to investment-grade customers on large builds. Supply/capacity commitments **$279B (from $119B a quarter earlier)** |
| M5 Inversion / Trap | risk | −1 | −1 | **−2** | New trap leg: NVDA is now a **vendor-financier** of its customers (receivables + $42.8B marketable equity book incl. CoreWeave/Nebius stakes + $3.3B equity-method infrastructure financiers) while the neocloud credit stack reprices (CoreWeave bonds ~79c). Q3 will mark the equity book down (CoreWeave −56% from high, Nebius −45%) |
| M6 Price / Position | price | −1 | −1 | **0** | Inside the band: base 5y IRR **+8.8%** at $214.13 clears the 8% hurdle on the accounting-OE basis; cash-haircut basis still ≈ 0%. Forward P/E ~17.9x (stockanalysis) |

## The finding that matters: STEP 1 is answered, half-favourably

The 09-05 card made entry conditional on the 10-Q closing the owner-earnings bridge in two parts.

1. **GAAP > non-GAAP inversion = investment gains?** **Confirmed.** Gains from equity securities, net: **$7,771M in Q2**, $23,707M in H1 (10-Q cash-flow reconciliation). Non-operating, non-cash.
2. **OCF converges toward non-GAAP net income?** **Not confirmed.** OCF did not converge; the 10-Q says why: receivables (+$22.4B), inventory (+$5.8B), prepaids (+$5.5B). H1 OCF $74.4B vs H1 NI $118.0B (63%); Q1 alone was 86%, Q2 alone 40%.

So the gap is **working capital, not margin** — which is the better of the two structural readings — but the working capital is **extended credit to customers** in the exact quarter the market began doubting customers' credit. The card does not treat this as closed.

## Price band (unchanged inputs; re-priced)

| Basis | OE start | 8%-neutral entry | 5y IRR at 214.13 |
|---|---:|---:|---:|
| Accounting OE (Q2 annualised ~$215.5B; Q3 guide ~$241B) | $225B | **$222.44** | **+8.8%** |
| Cash-haircut OE (toward demonstrated FCF ~$85B annualised) | $150B | **$148.30** | **+0.4%** |

**214.13 is inside the band.** On the accounting basis the hurdle is cleared for the first time in this complex; on the cash basis it is not. The band collapses to a point only when the Q3 FY27 cash-flow statement says which basis is right.

## WATCH → STARTER trigger (re-sequenced, same logic)

**STEP 1 (re-specified):** Q3 FY27 (expected ~2026-11-18, unconfirmed) shows **(a)** quarterly OCF ≥ ~70% of GAAP net income **or** receivables growing no faster than revenue (AR/quarterly revenue back toward ~0.45 from 0.66), **and (b)** no allowance or write-down against the ≥10%-of-AR customers. **STEP 2:** with STEP 1 met and price ≤ $222.44, open a **3–5% STARTER** (T0 cap $500 applies).
**If instead** Q3 shows AR still rising faster than revenue or any reserve against a large customer → anchor at the cash-haircut basis ($148) and stay WATCH.

## Kill criteria

K1 Q3 revenue misses ~$108B or DC declines sequentially or GM < 65% · K2 custom-silicon share erosion (escalation only) · K3 inventory write-down ($4.5B H20 precedent; $400M H200 charge reported in Q2 — secondary; inventory $31.6B, commitments $279B) · K4 price above band with no OE upgrade — **no longer triggered** · K5 10-Q shows OCF/NI gap structural — **partially: AR-driven, one quarter; re-test at Q3** · K6 Huang key-man · **K7 NEW: customer-credit leg** — any ≥10%-of-AR customer in distress, or NVDA extending further financing (equity, guarantees, terms) to keep orders flowing; the SB Energy / OpenAI-affiliated guarantees (capped $105B) sit in this leg.

## runner_dissent

The dissent says the obvious thing: the five receivables customers are almost certainly hyperscalers and Oracle, not neoclouds; 90-day-to-one-year terms on $100B of quarterly shipments are a commercial choice by a company with $57B of cash and securities, not distress; the stock is at a 17.9x forward multiple with 75% gross margins; base IRR clears the hurdle at this price; and the card's own words were "the first STARTER candidate this book has had in this complex". The discipline answer is that the 09-05 card put the cash-flow statement ahead of the entry on purpose, the statement came and did not close the gap, and the names on the receivables ledger are not disclosed. Four weeks to the Q3 print is a bounded cost. The runner would rather be four weeks late than size on a cash conversion the filing does not yet show.
