# NBIS Research Run — Layer 4 cross-check: Contract Quality / RPO / Backlog

- Run date: 2026-06-18 (redundant cross-check spawned by the business-model agent)
- Method: general-purpose subagent; primary = FY2025 20-F + Q1'26 6-K Exhibit 99.2 (audited/unaudited financial statements) + shareholder letters.
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Promote via `claim_ledger.csv`. This agent's figures come straight from filings and **supersede** looser "backlog" framing elsewhere.
- Subagent id (may expire): a45ec235f76559f1c | tokens: 108,409 | tool_uses: 40

---

## HEADLINE: the "$46B backlog" is not a company figure — use RPO

The word "backlog" does NOT appear in the FY2025 20-F or the shareholder letters. "$46B" is a **media/analyst sum of deal ceilings** (MSFT up to ~$19.4B + 2nd Meta up to ~$27B). NBIS's only formal contracted-revenue metric is **RPO**, which is materially lower because it excludes optional tranches and capacity not yet meeting recognition criteria.

## RPO (formal SEC metric) — [PRIMARY]
- **RPO at Mar 31, 2026 = $33,585.3M.** Recognition: 29% within 24 months (by Mar'28), 39% months 25-48, 32% thereafter. (Q1'26 6-K Ex 99.2)
- **RPO at Dec 31, 2025 = $21,333.0M.** Recognition: 28% within 24 months. (FY2025 20-F)
- RPO rose **+$12.25B QoQ**, driven by the Mar 16 2026 second Meta agreement.
- Gap: headline "$46B" vs SEC RPO $33.6B ≈ $12B+ = optional/not-yet-recognizable portions (notably Meta's $15B sell-or-Meta-buys tranche).

## Deferred revenue (balance sheet) — [PRIMARY]
- **Mar 31, 2026: $4,778.1M** (current $685.6M + non-current $4,092.5M).
- Dec 31, 2025: $1,577.5M (current $275.5M + non-current $1,302.0M); vs $16.3M at Dec'24.
- Q1'26 cash flow: deferred revenue +$3,200.6M in the quarter (~$3.2B new prepayments).

## ARR trajectory — [PRIMARY] (ARR = last month AI-cloud rev ×12)
- Mar 31 2026 = **$1.92B** (+674% YoY, +54% QoQ)
- Dec 31 2025 = $1.25B ("more than doubled from $551M at end Sept")
- Sep 30 2025 = $551M
- Exit-2026 guide $7-9B; FY2026 revenue guide $3.0-3.4B; ~40% adj EBITDA margin.
- Q1'26 group rev $399.0M (+684% YoY, +75% QoQ); AI-cloud rev $389.7M (+841% YoY).

## Microsoft contract — [PRIMARY 20-F]
- Up to ~$17.4B through 2031 (→$19.4B w/ additional services), 5-yr, Vineland NJ; first tranche Nov'25, second Feb'26.
- **Aggregate upfront ≈ $6,958.1M**; remainder invoiced monthly through Oct 2031.

## Meta contracts — [PRIMARY 20-F]
- **First Meta agreement (~Dec 2025): ~$2,880.7M total**, 5-yr, two tranches (Nov'25 + Feb'26), **take-or-pay** — "Meta is obligated to pay the contracted service fees irrespective of actual utilization." (Media rounded to "$3B".)
- **Second Meta agreement (Mar 16 2026): up to ~$27B** = ~$12B dedicated compute (Vera Rubin, delivery from early 2027) + a further Order up to ~$15B where NBIS can sell to other customers; if unsold, Meta must purchase.

## RESOLUTION of the take-or-pay vs terminable dispute (C014/C015)
Both are true and not contradictory — they protect opposite parties:
- **Take-or-pay (customer-side obligation):** customer pays the contracted fee *irrespective of actual utilization* (confirmed for the first Meta agreement, "irrespective of actual utilization"; MSFT economics similar with ~$6.96B upfront). Protects NBIS if the customer under-uses.
- **Delivery obligation (NBIS-side):** if NBIS fails to deliver/meet SLAs, customer has **service-credit / termination rights** (MSFT) and there are liquidated damages for late delivery. Protects the customer if NBIS fails to build/energize on time.
→ Net: revenue is contractually sticky *as long as NBIS delivers on schedule*. The residual risk is execution (delivery slip), not customer optional walk-away. This sharpens inversion path A (delivery slip) over a pure "customer cancels" path.

## Quality-of-revenue / concentration — [PRIMARY commentary]
- No company-disclosed self-service/non-anchor % or anchor concentration %.
- Core "Nebius AI cloud" = ~94% of group rev Q4'25 → ~98% Q1'26 (rest = Avride + TripleTen). This is SEGMENT mix, not anchor-vs-self-serve.
- Secondary analyst estimate (unverified): ~85% hyperscaler-dependent 2026 → ~65% by 2029 (northwiseproject).
- "Strategic long-term contracts remain an important part of our financing strategy"; "very focused on generating prepayments to reduce capital needed from equity and debt."

## Supplementary verified — [PRIMARY]
- Contracted power >3.5GW at Q1'26; YE2026 guide >4GW; >75% owned.
- Q1'26 capex ~$2.5B; raised $6.3B in Q1 ($2.0B NVIDIA equity + $4.3B converts); >$9.3B cash; +$2.3B OCF.
- NVIDIA $2.0B equity via pre-funded warrants (21,065,936 Cl A).

## COULD NOT FIND
- Company-disclosed "$46B backlog" (it's analyst/press; use RPO $33.6B Q1'26).
- Quantified self-service/non-anchor % or concentration %.
- Separate Q4'25 RPO (calendar FY; year-end RPO $21.333B from 20-F).

Date nuance: Q1'26 shareholder letter dated May 13 2026 (call); 6-K with formal statements furnished May 20 2026; both cover quarter ended Mar 31 2026.
