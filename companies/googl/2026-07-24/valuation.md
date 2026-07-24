# GOOGL Valuation / Margin of Safety (M6) — Q2 2026 REFRESH

Last updated: 2026-07-24 · Module M6 Price/Position · role: price + output
Signal: **−2** (unchanged from 2026-06-19) · confidence: high

> Numbers trace to `facts.md` / `claim_ledger.csv` and `model/scenario_model.csv` + `model/owner_earnings_bridge.csv`. Non-filed inputs marked ASSUMPTION. Units USD, billions unless noted.

---

## 0. Module verdict (one line)

**The price fell 14% (to $317.69) but owner-earnings quality fell about as fast (FCF went negative; TTM FCF −20%), so the margin of safety is essentially unchanged: still negative. Base-case 10y IRR improved from −3.0% to −1.0% but is still below zero; only the BULL case (flawless capex conversion) now clears the 8% hurdle, at +8.2%; and on trailing free cash flow the stock is actually MORE expensive than in June (72.9x vs 69.6x). Price still caps the verdict at WATCH.**

## 1. Current setup (price anchor)

At **$317.69** the stock is **−22.2% below the 52-week high** of $408.61 and +69% above the 52-week low of $187.82 (upper-middle of the range — not a low/high grab).

| Item | Value | Source |
|---|---:|---|
| **as_of price (canonical)** | **$317.69** | 2026-07-23 settled close (−7.1% earnings-reaction day); Yahoo + stockanalysis agree, delta 0.0% [S-YHOO-2026-07-23] |
| Shares (A+B+C) | 12,230M | 6/30/26; up from 12,088M (dilution) [GOOG.A1.2026Q2.031] |
| **Market cap** | **~$3,885B ($3.885T)** | = $317.69 × 12,230M; vs $4.46T prior |
| Net cash (marketable) | +$144B | cash+marketable $242.5B − LT debt $98.2B; but ~$70B just raised & earmarked for capex → transitional |
| **Market cap / TTM FCF** | **72.9x** | $3,885B / $53.273B — WORSE than prior 69.6x despite the lower price |
| Base owner-earnings yield | 1.75% | base OE0 $68B / $3,885B (P/OE 57x); vs 1.45% prior |

> The single most important valuation fact this quarter: **price −14%, but TTM FCF −17% (to $53.3B), so mkt-cap/FCF got more expensive.** "Cheaper" on the tape, dearer on cash.

## 2. Owner-earnings base

From `model/owner_earnings_bridge.csv`: TTM owner earnings **~$55B (defensive) – $95B (growth)**, midpoint ~$75B; harsh cash read (TTM FCF − TTM SBC) ~$23B. Scenario starting points: **bear $54B / base $68B / bull $90B** (base nudged up from $65B on +30% operating income and Cloud proof points, but weighted toward the defensive read given negative FCF).

## 3. Three-scenario 10y IRR at $317.69

Structure carried from 2026-06-19 for comparability (same CAGR paths / terminal multiples / payout paths); only OE0, price, and net cash updated. Engine: interim payouts + terminal (OE_y10 × terminal P/OE + $100B conservative net cash), bisection IRR. Full outputs in `model/scenario_model.csv`.

| Scenario | OE0 | rev CAGR | OE CAGR (1–5y/6–10y) | exit P/OE | OE_y10 | **10y IRR @ $317.69** | (was @ $370) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Bear** | $54B | ~6% | 2%/2% | 14x | $66B | **−11.3%** | (−13.1%) |
| **Base** | $68B | ~11% | 9%/7% | 20x | $147B | **−1.0%** | (−3.0%) |
| **Bull** | $90B | ~15% | 14%/10% | 26x | $279B | **+8.2%** | (+5.2%) |

**Read:** every scenario improved ~2–3pp on the lower entry. But **the base case is still negative (−1.0%)** and only the **bull just clears 8% (+8.2%)** — i.e., at today's price you are paying essentially full value for the optimistic "capex converts to high-return growth" case, with no cushion if it doesn't. To earn 10% at $317.69 still requires owner earnings to compound ~20%/yr for a decade.

### Reverse read: what $317.69 implies
- Base-case IRR turns positive (0%) only below **~$288**; clears 8% only below **~$139**; clears 10% only below **~$117**.
- Even the **bull** case falls below 8% above **~$322** — the current price sits right at that edge.

## 4. Margin-of-safety ladder (base path, term 20x)

| Tier | Target IRR | Buy below | vs $317.69 | (prior) |
|---|---:|---:|---:|---:|
| **Avoid above** | (bull <8%) | **> ~$322** | at the line | (~$300) |
| Base breakeven | 0% | ~$288 | −9% | — |
| Min hurdle | 8% | ~$139 | −56% | (~$134) |
| **Starter anchor** | 10% | **~$117** | **−63%** | (~$113) |
| Core / real MoS | 12% | ~$99 | −69% | (~$95) |
| Downside anchor | bear-8% | ~$50 | −84% | (~$48) |

**Buy-below (10% starter anchor) = ~$117**, a modest uptick from ~$113 on the higher operating-income base. Still ~63% below today.

### Is the margin of safety real? No.
- Conservative (bear/base) values remain **below** the price. Base fair value ~$117 (10% discount); bear downside anchor ~$50.
- **Starting cash owner-earnings yield ~0.6% (FCF−SBC) / base OE yield 1.75%** — the moat protects the *business*, not $318 of principal.
- Balance sheet is **levering up and diluting** for capex (LT debt doubled to $98.2B; $49.6B equity + preferred issued; buybacks $0) — it is not protecting the downside.
- All return still depends on the optimistic capex-conversion assumption; per the ceiling rule, "safety from optimistic assumptions → max WATCH."

## 5. Discipline self-check
- ✅ Good business at the wrong price is still a poor investment — the textbook case. The 14% drop did not create a margin of safety because FCF fell in step.
- ✅ Did not rescue the return with aggressive terminals: even bull 26x only gets to +8.2%.
- ✅ Higher uncertainty → larger discount: maintenance/growth capex split still unobservable AND capex just went UP → weight toward the base/bear anchor (~$99–117), not the 8% line.

## 6. Open questions
- [ ] Maintenance vs growth capex split (drives base OE0 and where "fair" sits).
- [ ] Net-cash treatment: used conservative $100B terminal (vs $144B reported) since the raise is capex-earmarked; at $144B the base buy-below is essentially unchanged (~$117).
- [ ] Terminal multiple: if the market permanently re-rates "AI capex compresses FCF conversion," mature multiple could fall to 14–15x (bear anchor), worsening base IRR.
- [ ] The bull case rests on a post-2027 FCF inflection (TPU/cloud revenue) that is not yet observable.
