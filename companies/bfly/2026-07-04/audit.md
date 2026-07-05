# BFLY Audit (Stage 7 · Quality Gate)

Last updated: 2026-07-04 · auditing this cold-start dossier's completeness, internal consistency, and verdict ceiling

## 1. Completeness Assessment

| Dimension | Status | Notes |
|---|---|---|
| Primary evidence base | Strong | 8 primary SEC filings (10-K FY2025, 10-Q Q1 2026, 6 material 8-Ks) + 2 independent live price/market-data pulls (Yahoo, stockanalysis, 0.0% delta) + 1 successful background competitive-research pass; ~80 claims in the ledger, nearly all load-bearing numbers tagged A1 |
| Financial model | Strong | 3-year P&L trend + normalized bridge (E&O charge, SBC, litigation accruals separated) + cash-flow/runway analysis + dilution history + 3-scenario 5y IRR grid using EV/Revenue exit method (the correct framework for a pre-EBITDA-profitability company) |
| 8 analysis modules | Complete | business_model / value_chain / moat / bottleneck / operator / inversion / financial_quality / valuation all present and internally cross-referenced |
| Gaps | See below | Full DEF 14A exec-comp/beneficial-ownership detail (O3 in facts.md), FY2022-and-earlier point-in-time share counts (O4), Clarius's underlying probe architecture (bottleneck_map.md OPEN item), identity of the ~11%-revenue single customer (O1), next-earnings-date not yet company-confirmed (O6) |

**Completeness estimate: ~75-80%** for a small-cap first-pass dossier -- proportionally strong for a $2B-cap name given the depth of primary-source extraction (8 SEC filings fully read, not just aggregated data). This is comparable to, or slightly better than, this pipeline's GOOGL pilot-day effort, though naturally short of a name that would receive multiple research days.

## 2. Hard-Rule Ceiling Check

- "Missing modules caps verdict": all 8 analysis modules present -> **does not trigger**.
- "Insufficient sourcing caps verdict at INFO-GAP/WATCH": load-bearing numbers are well-sourced (A1), but the verdict ceiling here is **not primarily a sourcing-completeness problem** -- it is a **substantive evidentiary finding**: the evidence itself (once gathered) shows (a) no price-side margin of safety, (b) an unresolved moat-durability question, and (c) a real governance-concentration risk. This is a different ceiling mechanism from a name where the cap is "we didn't gather enough evidence yet."
- **Verdict ceiling = WATCH**, and the source of that ceiling is a genuine finding, not an evidence gap: valuation.md shows base-case and even bull-case IRR below the 8% hurdle; moat_map.md shows a 3-5 year technical lead rather than a structural moat; operator_underwriting.md shows a 71%-controlled governance structure with a disclosed portfolio-wide litigation pattern.

## 3. Source of the Ceiling (comparison across this pipeline's recent cases)

- **GOOGL case**: ceiling = WATCH, driven by **price alone** (negative margin of safety at an otherwise strong, well-understood business).
- **MSFT case**: ceiling = STARTER, driven by **research completeness** (~65%, two information gaps) -- price itself had a POSITIVE margin of safety.
- **BFLY case (this dossier)**: ceiling = WATCH, driven by a **compound, substantive finding across three independent dimensions** -- valuation (no margin of safety, base case -15.3% IRR), moat durability (real but narrow/eroding), and governance (extreme concentration with a disclosed litigation pattern). Unlike MSFT, this is not primarily an evidence-completeness problem (completeness is reasonably good at ~75-80%); unlike GOOGL, it is not a single-dimension problem either. **This is the most "genuinely uncertain business, not just mispriced" case in the recent batch** -- the underlying company is smaller, younger (5 years post-SPAC), and has a shorter demonstrated track record than either mega-cap comparable, so even strong evidence-gathering cannot manufacture a longer performance history than exists.

## 4. Internal Consistency Check

- Module signals are consistent with facts.md throughout; the "fabless, no manufacturing chokepoint" finding appears consistently in moat_map.md, bottleneck_map.md, and value_chain_map.md without contradiction.
- as_of_price $7.68 appears identically across facts.md, valuation.md, model/scenario_model.csv, decision_card.md, decision_card.json, and brief-v1.html (verified via verify_freshness.py T5 tripwire).
- Market cap ($2,009.4M / ~$2.01B) and shares outstanding (261.64M) are consistent across all files.
- 52-week high ($9.69, 2026-06-29) and low ($1.32, 2025-08-08) are consistent across facts.md, source_register.md, valuation.md, decision_card.json, and freshness.json.
- No stale files claiming a different status exist (cold-start, no prior version of this dossier).
- One judgment call flagged for transparency: the task brief's own framing mentioned a "spike to ~$8.90 on 2026-06-18" and a "~7.2x multiple needed" figure; this dossier's own independently-gathered evidence (facts.md E3, sourced from 2 independent price pulls) establishes the intraday high as $9.69 on 2026-06-29 (the 06-18 move reached an intraday $8.94 before continuing higher over the following days), and this Runner's own valuation model arrives at a required multiple of ~7.5x (aggressive-bull sensitivity) to ~6.7x (at 30% growth) for an 8% hurdle -- both numbers are close to, and consistent with, the brief's framing, with the small differences fully attributable to slightly different growth-path/exit-year conventions, not a factual disagreement. The dossier uses its own independently-verified/computed numbers throughout rather than the brief's shorthand figures.

## 5. Inquiry Points for the IC Panel

1. **Valuation**: base-case and bull-case (5.0x exit) 5-year IRR both fall below an 8% hurdle at the current $7.68 -- does the panel agree this alone should prevent a new-money STARTER regardless of business quality?
2. **Moat durability**: is a 3-5 year technical lead (patents + accumulated data, no manufacturing chokepoint) sufficient for any position size, or does it require the price to compensate more heavily than it currently does?
3. **Governance concentration**: does Rothberg's ~71% voting control (no sunset until 2028) combined with a disclosed same-founder litigation pattern (Quantum-Si) constitute an independent cap on size, separate from the valuation and moat questions?
4. **Genuine improvement vs. proof**: the gross-margin trend and first positive operating-cash-flow quarter are real -- does the panel weight this enough to justify a small monitoring position (e.g. 1-2%) rather than 0%, or does the compound constraint argue for 0% until more evidence accumulates?
5. **Embedded-licensing concentration**: the critique round in ic_panel.md flagged that the margin improvement is substantially attributable to ONE large licensing relationship (Midjourney) rather than broad-based hardware cost improvement -- does this change the panel's read on repeatability?

## 6. Completeness Conclusion

**~75-80% · ceiling = WATCH (a genuine, substantive finding across valuation + moat + governance, not primarily an evidence-completeness gap).** The path to a higher completeness grade (and potentially a higher verdict, though not automatically) runs through: (a) 2-3 more quarters of demonstrated profitability trajectory; (b) independent resolution of Clarius's probe architecture (does it validate or undercut the "chip is the key unlock" thesis); (c) Butterfly Embedded partner-conversion data beyond Midjourney; (d) full DEF 14A executive-compensation and beneficial-ownership detail. None of these are blocking for a small-cap WATCH-tier verdict today, but all would sharpen the next review.
