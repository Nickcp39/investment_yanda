# BFLY Moat Map (M3)

Last updated: 2026-07-04 | as_of: 2026-07-04 | sources: facts.md E9-E14, E52-E79

---

## Moat Summary: THIN, EARLY-STAGE, PATENT+SOFTWARE MOAT ON TOP OF A COMMODITY-SUPPLY-CHAIN CHIP

Business quality grade: **UNCERTAIN-TO-GOOD-AND-IMPROVING** (not exceptional, not broken -- a genuine technology with a real but not-yet-proven durable edge)

Butterfly's marketing claim is a "semiconductor moat" (Ultrasound-on-Chip vs. incumbent piezoelectric crystal). The evidence supports a **real, differentiated technology** with **improving unit economics** [I1], but does **not** support a **hard, durable, decade-long moat** in the way GEV's turbine-oligopoly or ISRG's installed-base annuity do. The moat -- to the extent it exists -- lives in patents + accumulated clinical/software/workflow integration + brand-with-hospitals, not in exclusive access to chip manufacturing (Butterfly does not own a fab; TSMC does [E12]). This is graded honestly below rather than accepting the company's own framing at face value, consistent with source-policy discipline on company-authored claims [I10].

---

## Moat Candidate 1: Semiconductor ("Ultrasound-on-Chip") Technology + Patents -- REAL BUT NARROWER THAN CLAIMED

**Evidence**:
- Butterfly's probes use a single semiconductor chip instead of lead-based piezoelectric crystal arrays, enabling one probe to do whole-body imaging (vs. competitor handhelds often needing 2-3 probes) [E64, company framing]
- ~665 issued patents + pending applications (US, EU, UK), expiring 2030-2046 [E13]
- RoHS (EU lead-restriction) compliance advantage since chip-based probes avoid the lead-piezoelectric exemption competitors rely on; BFLY petitioned the EU to revoke that exemption industry-wide (Oct 2024) [E63]
- Adjusted gross margin has genuinely and monotonically improved: 59.6% (FY24) -> 64.9% (FY25) -> 68.9% (Q1'26, no adjustment needed) [I1] -- real evidence the underlying unit economics work

**Why this is NOT as deep as it looks**:
- Butterfly is **fabless** -- it does not manufacture its own chips. TSMC manufactures under a **non-exclusive** Foundry Service Agreement [E12]. The chip IP (design) is Butterfly's; the chip MANUFACTURING scarcity is not -- any well-capitalized competitor could commission a similar chip design at the same foundry (or a rival foundry) if they chose to invest the R&D dollars. The moat is design know-how + patents, not a hard supply chokepoint. See bottleneck_map.md for the full analysis.
- Patents (2030-2046 expiry) can be designed around, especially for a technology category (semiconductor ultrasound transducers) that is not exotic physics -- Exo Imaging has independently achieved 14 FDA-cleared AI indications on its own chip-based platform [E68], suggesting the core chip-based approach is replicable by well-funded rivals, not uniquely Butterfly's.
- Clarius Mobile Health, a private competitor, reached **full-year profitability in FY2025** with 20% growth and added 2 new FDA-cleared AI models [E67] -- a direct handheld competitor got to sustainable unit economics before Butterfly did, which weighs against the "only Butterfly's chip approach makes handheld-ultrasound economics work" claim. (Whether Clarius uses the same chip-on-a-die architecture or an alternative approach is not established in evidence gathered -- flagged OPEN; if Clarius uses a *different* non-semiconductor approach and still profits, that is even stronger evidence against a durable Butterfly-specific chip moat.)

**Durability**: MEDIUM, narrowing. A 3-7 year technology lead, not a permanent structural barrier. The improving gross margin [I1] is the strongest evidence the technology genuinely works and is getting more efficient to produce/license -- but "genuinely works and is improving" is a different (weaker) claim than "durable competitive moat that locks out rivals for a decade."

---

## Moat Candidate 2: Software / AI / Clinical Workflow Lock-In -- EARLY, GENUINE, BUT SMALL SHARE OF REVENUE TODAY

**Evidence**:
- Compass AI enterprise workflow platform (launched Nov 2025) integrates into hospital PACS/EMR systems [E52] -- this is the ISRG-style "sticky installed base" mechanism, but far earlier stage
- Software & other services = 35.0% of FY2025 revenue (up from 33.9% FY2024) [E60] -- growing, but well short of ISRG's 76-86% recurring mix (per the comparable dossier in this pipeline) and well short of a "razor-and-blade" business
- Butterfly Garden (third-party AI-app marketplace/SDK) has 30 partners as of Q1 2026 [E54] -- a genuine platform-ecosystem play, still small
- 665 patents include software/AI claims presumably, though the 10-K does not break down hardware vs. software patent count [E13]

**Durability**: LOW-TO-MEDIUM today, rising if the mix shift continues. Once a hospital deploys Compass AI + trains staff on the Butterfly workflow, switching cost exists -- but the *base* to switch away from is much smaller and much younger than an installed base of 11,000+ da Vinci systems (ISRG comparable). This is a moat in formation, not a moat in being.

---

## Moat Candidate 3: Butterfly Embedded -- Licensing/Royalty Optionality, Unproven at Scale

**Evidence**:
- Midjourney deal: $15M upfront + $10M/yr license (5yr) + up to $9M milestones + revenue share + chip sales, reconciling exactly to the "$74M" headline [E53]
- 9 signed Embedded partners as of April 2026 [E54]; independent commentary notes "30-40 more in discussion that have not converted to production revenue" [E73]
- If this scales, it would be a genuinely differentiated, high-margin (near-100%, licensing-style) profit pool layered on top of the core hardware business -- the platform-company repositioning the market rewarded with the June 2026 re-rating [I6]

**Durability**: SPECULATIVE / OPTIONALITY, not yet a moat. One real, verified deal (Midjourney) plus 8 more signed but unquantified partners. This is exactly the kind of claim source-policy discipline says should not be treated as an evidenced moat until conversion happens -- it is a call option on the platform thesis, not yet cash-flow-proven optionality. [E73] itself is the most balanced independent read available and stops short of confirming this converts to durable economics.

---

## Moat Weaknesses / Attack Surface

1. **No manufacturing chokepoint**: Butterfly's dependence on TSMC (non-exclusive contract) [E12] means Butterfly does not control a scarce input the way GEV controls turbine-forging capacity or ISRG controls a trained-surgeon installed base. A rival with capital and patience could commission a competing chip.
2. **Well-capitalized incumbents are not standing still**: GE Healthcare (>22% overall ultrasound share) [E65] has its own Vscan Air line; Philips has Lumify; both are large, profitable companies that could out-invest Butterfly in R&D if chip-based handheld ultrasound is validated as the future of the category.
3. **A private, less-capitalized competitor (Clarius) already reached profitability first** [E67] -- undercuts the narrative that Butterfly's specific approach is necessary to make handheld-ultrasound economics work, and raises the question of whether Butterfly's slower path to profitability (still guiding to a loss through FY2026, E33-34) reflects company-specific execution/cost-structure issues rather than a structural technology advantage.
4. **Patents expire on a known clock (2030-2046)** [E13] and are challengeable; this is a depreciating-but-long-duration asset, not a permanent barrier.
5. **~11% customer concentration with an unnamed single customer** [E59, O1] introduces a real, currently unquantifiable single-point-of-revenue-loss risk that has nothing to do with moat depth but affects near-term durability of results.

---

## Durability Test

| Horizon | Does moat hold? | Why | Evidence gap |
|---|---|---|---|
| 1-2 years | Mostly yes | Patents fresh (2030+ expiry), gross margin trend intact [I1], installed base (145K users) [E59] provides switching-cost inertia; near-term revenue visibility from reaffirmed guidance [E33-35] | None material |
| 3-5 years | Uncertain | Depends on whether Butterfly Embedded converts partners-in-discussion to revenue [E73], whether Compass AI achieves ISRG-style lock-in at scale, and whether incumbents (GE/Philips) or private rivals (Clarius, Exo) close the cost/versatility gap | Independent verification of Clarius's underlying chip technology (piezoelectric-array vs. true semiconductor) not established [OPEN]; Embedded partner conversion rate unknown |
| 10 years | Low confidence, genuinely unknown | If the semiconductor approach is the long-run winning architecture for point-of-care ultrasound, whoever has the best AI/software layer + distribution (not necessarily Butterfly specifically) likely wins; Butterfly's patents alone do not guarantee it retains leadership through 2036 given 2030-2046 patent expiry starts biting mid-decade | No evidence base exists this far out for any player in this category; genuinely speculative at this horizon |

---

## Moat Scorecard

| Moat Source | Depth | Durability | Trend |
|---|---|---|---|
| Semiconductor chip design/patents | SHALLOW-MEDIUM | 5-10 years (patent clock, not manufacturing scarcity) | Improving execution, uncertain competitive spread |
| Software/AI/workflow lock-in (Compass AI, Butterfly Garden) | SHALLOW, forming | Rising if mix shift continues | Growing (35% -> higher of revenue) |
| Butterfly Embedded licensing optionality | SPECULATIVE | Unproven | One verified deal, 8 more signed, unquantified pipeline |
| Brand / clinical trust / installed base (145K users) | SHALLOW-MEDIUM | Improves with scale | Growing |
| Manufacturing / supply chokepoint | **NONE** (fabless, non-exclusive TSMC) | N/A -- this is a RISK not a moat | Structural, not improving |

**Overall moat verdict**: Butterfly has a genuine, improving, differentiated technology and a real (if early) platform-optionality story, but it does **not** have the kind of hard, multi-decade moat that would justify labeling this an "exceptional" business today. The single cleanest piece of evidence FOR the thesis is the gross-margin trend [I1] -- real operating leverage, not marketing. The single cleanest piece of evidence AGAINST an overclaimed "chip moat" is Butterfly's own fabless dependency on a non-exclusive TSMC agreement [E12] plus a smaller, less-capitalized private rival (Clarius) reaching profitability first [E67]. **Grade: 2.5-3/5** (uncertain-to-good, not exceptional) -- this caps the valuation multiple appropriate for the business and is a primary driver of a cautious new-money verdict regardless of price (see inversion_map.md and valuation.md).
