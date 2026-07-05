# BFLY Business Model (M2)

Last updated: 2026-07-04 | as_of: 2026-07-04 (as_of_price $7.68) | sources: facts.md, source_register.md | pipeline: lean-6module-v1.1

---

## One-Sentence Business

Butterfly Network designs (but does not manufacture) a handheld semiconductor ultrasound probe and AI/software platform, sells it directly to clinicians and healthcare systems on a hardware-plus-subscription basis, and — starting in 2025 — has begun licensing the same underlying chip platform to non-medical third parties as a separate, higher-margin revenue line [E52].

---

## What Butterfly Does

Butterfly's core technology is "Ultrasound-on-Chip" — a single semiconductor die (fabbed by TSMC, assembled by Benchmark Electronics) that replaces the array of lead-based piezoelectric crystals used in legacy ultrasound probes [E12, E62]. The company's own framing is that this lets one handheld probe (iQ+ / iQ3) image the whole body, versus incumbent handheld competitors needing 2-3 separate probes at higher combined cost [E64]. This is a genuine architectural difference (semiconductor CMOS vs. piezo-crystal), not a marketing label — E12 confirms the wafers are literally fabricated at TSMC, i.e., BFLY is designing and selling an actual chip, not just a plastic-housed piezo transducer with software attached.

Three distinct product/revenue lines have emerged, and they are economically quite different from one another:

### Line 1 — Hardware: iQ+ / iQ3 probes
- Butterfly iQ+: ~$2,700 list price. Butterfly iQ3 (launched Feb 2024): ~$3,900 list, the current best-selling generation-3 device [E52].
- Positioned against: (a) traditional cart-based ultrasound at $30,000-$120,000+ per device, and (b) incumbent handheld/POCUS competitors at ~$10,000 all-in (3-7k/probe x 2-3 probes + up to ~$2,000 software), vs. Butterfly's single-probe $2,700-$3,900 [E64] — note this $64 comparison is the company's own characterization of unnamed competitors, not independently sourced.
- This is 65.0% of FY2025 revenue ($63.44M of $97.61M), growing +17.1% YoY [E15].
- Gross margin on this line is NOT disclosed separately (single reportable segment, E11), but the FY2025 blended GAAP gross margin of 46.9% (vs. 64.9% adjusted ex the one-time $17.4M E&O inventory charge, E16) suggests hardware carries materially thinner margin than software/licensing — consistent with I1's finding that the 900bp margin improvement over 5 quarters (59.6% -> 64.9% -> 68.9%) tracks growing Embedded-licensing mix, which is a near-100%-margin revenue stream diluting a lower-margin hardware base.
- Veterinary variant: Butterfly iQ3 Vet, launched October 2025, ~20 international markets by YE2025 [E57] — same hardware platform, adjacent vertical.

### Line 2 — Software subscriptions
- Individual plans: "Core Technology" ~$300/yr, "Advanced Technology" ~$420/yr [E52].
- Enterprise: "Compass AI" platform, launched Nov 2025 [E52].
- This is the closest thing in the model to a true recurring annuity — but it is bundled into the "Software & other services" line (35.0% of FY2025 revenue, $34.17M, +22.7% YoY, E15) alongside other services, so the pure-subscription dollar figure is not separately broken out in facts.md.
- Recent product additions widen the subscription value proposition: Gestational Age AI tool (FDA-cleared, rollout began Q1 2026, exact clearance date 2026-03-30) [E55, E78] adds a differentiated clinical workflow that is hard to replicate without the same AI-training dataset (>21M images per E78's independent corroboration).

### Line 3 — Butterfly Embedded: chip/platform licensing
- Out-licensing of the Ultrasound-on-Chip semiconductor platform itself to third parties building non-competitive (non-medical-ultrasound) products [E52].
- **Midjourney deal** (dated 2025-11-17) is the reference transaction: exclusive, non-transferable, field-of-use-limited license. Economics: $15M one-time fee + $10M/yr license fee (paid quarterly) over a 5-year term + up to $9M in milestone payments + revenue-sharing on Midjourney's commercialized hardware + payments for any chip purchases. The "$15M + ($10M x 5) + $9M = $74M" headline reconciles exactly against the company's own "up to $74 million" framing [E53] — this is a rare case in the evidence base where a splashy number checks out precisely rather than needing a haircut.
- Contributed $6.8M of Q4 2025 revenue alone [E53], and drove the +55% YoY US-revenue growth in that quarter alongside iQ3 sales [E23].
- Ecosystem breadth beyond Midjourney: 9 signed Embedded partner companies as of April 2026 (separate from the 30-partner "Butterfly Garden" software-app marketplace, which is a different program) [E54].
- Per I6, at ~$13M/yr run-rate (amortized $15M upfront + $10M/yr) against ~$120M FY26 revenue guidance, Midjourney alone is a meaningful (~11%) but not thesis-defining contributor — its strategic significance is as proof-of-concept that the chip IP has value outside medical ultrasound, which is the reason the stock re-rated sharply in June 2026 when the deal (already 7 months old) received fresh media attention [I6, S3].

---

## Revenue Mix and Trend

| Revenue stream | FY2023 | FY2024 | FY2025 | Trend |
|---|---|---|---|---|
| Product (hardware) | — | ~66.1% | 65.0% ($63.44M) | Growing in $, roughly flat as % of mix |
| Software & other services | 39.2%* | 33.9% | 35.0% ($34.17M) | Growing faster than hardware (+22.7% vs +17.1% YoY in FY25) |
| Total revenue | $82.06M (FY24) | $82.06M | $97.61M (+19.0%) | Accelerating: Q1'26 +25.0% YoY [E25], FY26 guided +20-24% [E33] |

*FY2023's 39.2% software share was skewed upward by one-time medical-school grant deployments, not organic mix shift [E60].

International revenue has been stable at ~21-23% of total across FY2023-FY2025 (21% FY25, 23% FY24, 21% FY23) — this is not a business becoming more or less globally diversified, it's roughly steady [E61].

Gross margin trajectory (the cleanest single "is the model improving" signal per I1): adjusted gross margin ran 59.6% (FY24) -> 64.9% (FY25) -> **68.9% (Q1 2026, achieved with no one-time add-backs needed)** [E16, E26]. This is a genuine, monotonic ~900bp improvement over five quarters, and I1 attributes it to Embedded licensing (near-100% margin) diluting a lower-margin hardware base — real operating leverage, not an accounting artifact.

---

## Who Pays, and Why

| Customer | Product/service | Why they pay | Recurrence | Evidence |
|---|---|---|---|---|
| Individual clinicians / practitioners | iQ+/iQ3 probe + individual software subscription | Point-of-care imaging without a $30-120k cart-based machine; single probe vs. 2-3 needed by incumbent handhelds [E64] | Hardware: one-time (multi-year owned asset). Software: annual subscription ($300-420/yr) [E52] | E52, E64 |
| Hospital systems / health systems | Fleet probe deployments + enterprise "Compass AI" platform | Standardizing POCUS across a department/system; workflow AI (e.g., Gestational Age tool) [E55] | Software: recurring enterprise contract. Hardware: periodic fleet refresh | E52, E55 |
| Veterinarians | iQ3 Vet | Adjacent vertical use of same core hardware | One-time hardware, unclear subscription attach rate (not disclosed) | E57 |
| Third-party technology companies (e.g., Midjourney) | Licensed access to Ultrasound-on-Chip IP/platform for non-medical applications | Access to a differentiated, patented semiconductor sensing platform without building their own chip from scratch | Multi-year licensing contract (5-yr term), largely fixed-fee + milestones + a revenue-share component [E53] | E53 |
| ~11%-concentration single customer (unnamed) | Not disclosed | Not disclosed | Not disclosed | E59, flagged OPEN per O1 — plausibly Midjourney given Q4 timing, but not A1-confirmed |

---

## Razor-and-Blade — But Not Yet a Clean One

The intuitive comparison for a hardware-plus-subscription medtech model is the classic "razor-and-blade" annuity — the standard for that in this pipeline's coverage universe is Intuitive Surgical (ISRG), where the overwhelming majority of revenue is recurring (instruments/accessories + service, consumed per-procedure against an installed base of owned/leased robots). **BFLY is not that, and forcing the comparison would overstate the durability of its revenue.**

Three reasons this model is meaningfully weaker than a true razor/blade annuity today:

1. **The "razor" (hardware) is 65% of revenue, not a loss-leader.** iQ+/iQ3 list at $2,700-$3,900 [E52] — this is a real, non-trivial capital purchase for an individual clinician, not a subsidized give-away designed to lock in a consumable stream. Unlike a razor handle or a printer, the probe itself is the majority of the economics, and it is a durable, multi-year-owned device — a clinician who buys one iQ3 does not need to buy another for years. There is no forced, high-frequency repeat-purchase mechanic analogous to blades or ink cartridges.

2. **The "blade" (software subscription) is real but is a minority, not the core, of the model.** Software & other services is 35.0% of FY2025 revenue [E15], and only part of that is the clean subscription piece (E52's $300-420/yr individual plans) — the rest is bundled "other services" whose composition is not broken out in facts.md. Compare this to ISRG-style annuity models where recurring revenue approaches ~100%; BFLY's genuinely recurring share of revenue, even generously counting all of "Software & other services," tops out at 35%.

3. **A third, structurally different revenue line (Embedded licensing) has been bolted on.** Butterfly Embedded is not hardware-plus-blade at all — it is IP licensing with milestone payments and revenue-share [E53], an entirely separate value-capture logic (closer to a technology-licensing business than a medical-device annuity). Having three economically distinct lines (owned-hardware sale, subscription software, and third-party IP licensing) inside one $97.6M-revenue company [E15] is itself evidence that the company has not yet converged on a single, proven flywheel — it is running three different bets simultaneously.

**Net assessment**: the recurring piece of BFLY's model is real (software subscriptions exist, renew annually, and are growing faster than hardware — E15, E60) but it is currently a minority contributor, and the company's positioning as a "semiconductor platform company" (validated by the Midjourney proof-of-concept, I6) is itself an implicit admission that the core POCUS hardware-plus-subscription business alone was not yet a complete, self-sustaining growth story — hence the pivot to licensing the underlying chip IP as a third leg.

---

## Emerging Optionality: HomeCare and Veterinary

Two additional lines exist as early-stage optionality, not yet meaningful revenue contributors:

- **HomeCare Services**: piloting a CHF (congestive heart failure)-patient readmission-reduction program with an unnamed "major at-risk Health Services Organization." Target: first commercial agreement H1 2026, initial statewide deployment Q3 2026, revenue contribution expected late 2026/2027 [E56]. This is entirely forward-looking and unproven — no revenue has been attributed to it yet in any period covered by facts.md.
- **Veterinary** (iQ3 Vet): launched October 2025, ~20 international markets by YE2025 [E57] — real product, real launch, but no revenue contribution disclosed separately; treat as immaterial-to-date optionality rather than a proven fourth leg.

Both are consistent with a company still exploring adjacent applications of its core chip/software platform rather than having found and scaled a single dominant use case.

---

## Ten-Year Existence Test

- **What customer problem still exists in 10 years?** Point-of-care diagnostic imaging — getting an ultrasound image at the bedside/exam room without a $30-120k cart-based machine — is a durable clinical need; POCUS adoption is a real, ongoing shift in care delivery (E64's cost-comparison framing implies this is not a fad).
- **Why is Butterfly well-placed to solve it in 10 years?** Genuine technical differentiation exists today (semiconductor chip vs. piezo-crystal architecture, E12/E62) plus ~665 patents expiring 2030-2046 [E13] plus a growing AI/software layer (Gestational Age tool, Compass AI, E55/E52) that compounds with more scanned images over time. But — see bottleneck_map.md — the company does not own a manufacturing chokepoint (fabless, single-source TSMC dependency, E12), meaning the 10-year durability question rests almost entirely on patents + software/AI data moat + clinical workflow lock-in, not a hard supply-side barrier.
- **What changes if technology/competition shifts?** A well-funded incumbent (GE, Philips) or a profitable private competitor (Clarius, which reached profitability before BFLY did, E67) could narrow the gap; see bottleneck_map.md for the full competitive-durability assessment. On the regulatory side, BFLY's own petition to the EU to revoke the RoHS lead exemption for competitor handhelds [E63] is itself an admission that the chip-vs-piezo cost/environmental edge is not automatically decisive without a regulatory push.

---

## Business Quality Scorecard

| Question | Answer | Evidence | Assessment |
|---|---|---|---|
| Does the customer have high willingness to pay? | Mixed — probe price ($2,700-3,900) is positioned as a discount to both cart-based and incumbent handheld alternatives [E64], suggesting price-sensitivity/value-shopping behavior rather than premium pricing power | E64 | Moderate — competing partly on price, not pure value capture |
| Is revenue recurring or habit-forming? | Partially — software subscriptions renew annually and are the fastest-growing segment [E15, E60], but they are a minority (35%) of total revenue; hardware (65%) is a multi-year-owned durable good, not a consumable | E15, E52, E60 | Weak-to-moderate — real but far from ISRG-style near-100% recurring |
| Does scale improve economics? | Yes, with real evidence: adjusted gross margin rose 59.6% -> 64.9% -> 68.9% over 5 quarters as Embedded-licensing (near-100% margin) mix grew [I1] | E16, E26, I1 | Genuine and demonstrated, not aspirational |
| Can the company reinvest at attractive returns? | Unclear/early — company remains loss-making (FY25 net loss -$77.1M, FY26 guided Adj EBITDA loss $21-25M, E19/E34) though losses are narrowing and Q4'25 delivered the first-ever positive operating-cash-flow quarter (+$6.3M) [E22] | E19, E22, E34 | Not yet proven — improving trajectory, but not yet a self-funding compounder |
| Is the business understandable inside a normal circle of competence? | Yes — the mechanics (chip design, fab outsourcing, direct sales, software subscription, IP licensing) are each individually straightforward; the complexity is in judging durability of the moat, not in understanding what the company does | E12, E52 | Understandable |

---

## Honest Maturity Assessment

This is **not yet a proven flywheel**. Three quite different revenue lines (hardware sale, software subscription, IP licensing) coexist inside a company that is still guided to continued losses through FY2026 (Adj EBITDA loss $21-25M guided, E34) and only produced its first positive-operating-cash-flow quarter in Q4 2025 [E22] — a single data point, not yet an established pattern (Q1 2026 used $12.5M of cash again, E29). The Embedded-licensing pivot is real and its economics check out exactly against the disclosed contract terms [E53, I6], but it is best read as a company still actively searching for and validating its optimal business-model mix, not one that has already found and is now simply scaling a proven annuity. The most credible near-term signal that the model is working is the margin trend (I1) and the narrowing loss trajectory, not revenue growth alone (which any company can buy with discounting) or the company's own TAM framing (>$100B + $325B, E58 — flagged as unverified/promotional, I10).
