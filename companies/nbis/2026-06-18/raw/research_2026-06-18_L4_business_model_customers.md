# NBIS Research Run — Layer 4: Business Model, Customers & Revenue Quality

- Run date: 2026-06-18 (re-run after the original workstream #3 was interrupted)
- Method: general-purpose research subagent (background); primary = Q1'26 shareholder letter (read in full), Q2'25 letter, FY2025 20-F; secondary press/review sites. A redundant contract-quality cross-check agent ran in parallel (saved separately).
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Promote via `claim_ledger.csv` before use.
- Subagent id (may expire): a1daff5a44cd8c75a | tokens: 100,796 | tool_uses: 46

---

## BOTTOM LINE

1. Revenue quality improving but young and prepayment-funded. Q1'26 AI-cloud revenue $389.7M (+841% YoY), AI-cloud segment adj. EBITDA margin ~45%, implied GM ~74%. But audited **RPO $21.33B at Dec'31'25** (≈half the "$46-50B backlog" headline); large share of cash is customer prepayments.
2. Durability anchored by two long-dated take-or-pay-style contracts: Microsoft (~$17.4B, up to $19.4B; invoiced monthly through Oct 2031; service-credit/termination rights) and Meta (~$27B; $12B firm Vera Rubin from early 2027 + $15B optional/backstop NBIS can resell). ">half" of $7-9B exit-2026 ARR already contracted.
3. Concentration real and unquantified by mgmt. No top-1/top-5 disclosure. By inspection MSFT+Meta ≈ ~$44-46B of backlog = **~90%+ of contracted backlog is two customers**.
4. Non-anchor book genuinely broadening (key bull signal): 25+ named paying customers beyond MSFT/Meta; self-service/inference pipeline +~3.5x QoQ ex-hyperscalers. But none have disclosed $ values — logos/use-cases, so diversified revenue still small in dollars.
5. Hidden SOTP ~$7-8B of non-core stakes, led by ClickHouse (~28% marked at $15B post-Series D Jan'26 → ~$4.2B to NBIS, drove $780.6M non-cash Q1'26 gain); Avride (~83%, ~$2.2-2.3B); Toloka (~28%, ~$0.4-0.5B); TripleTen (100%, loss-making).

## 1. REVENUE MODEL & PRODUCT LINES
Three-tier sales (nebius.com/prices + Q1'26 transcript): (a) on-demand per-GPU-hr [PRIMARY]: H100 $3.85, H200 $4.50, B200 $7.15; (b) reserved committed: H100 $2.15, H200 $2.45, B200 $3.95 (~35-44% off); (c) large multi-year anchor (MSFT/Meta, private pricing). Committed-vs-spot split NOT quantified. Prices raised again Q1'26.
Product lines: **AI Cloud (core GPU IaaS)** ~98% of group revenue ($389.7M Q1'26); platform "Aether 3.5" (Mar'26) adds serverless inference. **AI Studio → Token Factory** (same line, not two): AI Studio launched 2024-11-28 (per-token inference, OpenAI-compatible) → rebranded Token Factory 2025-11-05 (60+ models, 99.9% SLA, fine-tuning/RAG). Token Factory = "fastest-growing segment" but NOT separately disclosed (inference $ still small). Prosus runs up to 200B tokens/day on it. Acquisitions: Tavily (agentic search Feb'26), Eigen AI (inference, closed ~Jun'26), Clarifai (team+IP May'26).

## 2. CUSTOMER ROSTER BEYOND MSFT/META (all [PRIMARY] shareholder letters; no $ values disclosed)
- Enterprise (Q2'25): Cloudflare, Prosus (Token Factory, 200B tokens/day), Shopify (FM training, expanding beyond GCP).
- AI-native/model builders: HeyGen, Lightning AI, Photoroom, Recraft (B200), Prime Intellect (GB200 NVL72), Higgsfield (B200); tail: Brave, Chatfuel (Llama-405B), Stanford (CRISPR-GPT), Krisp, Quantori.
- Q1'26 letter (most recent): Revolut (Token Factory fraud agents, 1.2M tickets/mo), monday.com, Sword Health (healthcare 200B+ param), 1X Technologies (humanoid robotics), Rhoda, Core Automation, Logical Intelligence; Prima Mente (UK Sovereign AI-backed).
- Sovereign: UK — NBIS (with Nscale) deploying 14,000 Blackwell GPUs; expanded Jun'26 to ~£1.7B, 4 UK sites, 65MW by 2027 (NBIS building sovereign capacity, not a single gov customer).
- FALSE POSITIVES ruled out: Mistral (peer, not customer), Black Forest Labs (Cloudflare compute), Recursion & CHAI (could NOT confirm), AI21 (acquisition target not customer).

## 3. CUSTOMER CONCENTRATION
No quantified disclosure (mgmt only "diversified core"). Best inference: MSFT (~$17.4-19.4B) + Meta (~$27B) ≈ $44-46B → ~90%+ of backlog is two customers. Near-term revenue concentration *lower* than backlog (Meta $12B firm tranche starts early 2027; MSFT ramps 2026-27). 20-F XBRL shows CustomerA/CustomerD concentration members exist but %s not retrievable via automated fetch (recommend manual pull of the rev-concentration note).

## 4. CONTRACT QUALITY
- RPO $21.33B at 12/31/25 (~28% within 24 months); deferred revenue $1,578M (cur $275.5M + non-cur $1,302.0M). [PRIMARY 20-F] (NOTE: cross-check agent found RPO rose to $33.585B at 3/31/26 after 2nd Meta deal — see contract-quality raw.)
- "$46B backlog" is NOT SEC-defined; word "backlog" absent from 20-F. = media sum of deal ceilings. Audited metric is RPO.
- Microsoft 5-yr, monthly invoicing through Oct 2031, ~$6.96B upfront, service-credit/termination rights for missed SLAs.
- ARR $1.92B end-Mar'26 (+674% YoY, +54% QoQ from $1.25B Dec'25). Quality-of-revenue: ">half" of $7-9B exit-ARR contracted; non-anchor pipeline +3.5x QoQ but disclosed $ outside MSFT/Meta thin.
- Accounting flag: server life 4→5yr eff Q1'26 (flatters D&A).

## 5. SUBSIDIARY SOTP (NBIS discloses sub revenues, generally NOT valuations/exact stakes)
| Asset | Stake | Latest round / valuation | Implied to NBIS |
|---|---|---|---|
| ClickHouse | ~28% | Series D $400M @ ~$15B Jan'26 (Series C ~$6.35B May'25) | ~$4.2B (drove $780.6M Q1'26 non-cash gain) |
| Avride | ~83% | up to $375M Uber+NBIS Oct'25 (split undisclosed) | ~$2.2-2.3B (analyst) |
| Toloka | ~28% econ (lost voting Q2'25) | $72M Bezos Expeditions May'25 (**NOT NVIDIA**) | ~$0.4-0.5B (analyst) |
| TripleTen | 100% | no round; 9M'25 rev $39.0M (+137%) but adj EBITDA -$32.1M | ~$0.2-0.3B (analyst) |
Aggregate ~$7.5-8.0B (analyst). No committed spin/IPO; mgmt: "utilize stakes as funding sources over time."
CORRECTION to prior brief: Toloka round = Bezos, NOT NVIDIA. ~28% applies to BOTH ClickHouse and Toloka (distinct stakes).

## 6. COMPETITIVE DIFFERENTIATION & DEVELOPER SENTIMENT
Claimed moat: full-stack/AI-native (own rack design, ~500 ex-Yandex-Cloud eng); NVIDIA's deepest partner ($2B, Exemplar Cloud GB300, early Vera Rubin); self-funded ($9.3B cash) vs CoreWeave debt model; >3.5GW/>75% owned; EU/sovereign + Token Factory managed inference.
Pricing: H100 $3.85/H200 $4.50 undercuts CoreWeave (H100 ~$6.15), ~ line with Lambda (~$4.29), above RunPod (~$2.69). Competitive mid-market.
Developer scuttlebutt (ALL ANECDOTAL): +GPU quality/performance & connectivity strong (Gartner verified); +onboarding "minutes, just works" (HN); −availability/quota gating on H100/H200; −support ~24-48h, thin docs; −one enterprise legal veto over Yandex/Russia heritage. Caveat: organic Reddit/X discussion genuinely thin.

## COULD NOT VERIFY
Committed-vs-spot split; numeric utilization; standalone Token Factory revenue; quantified top-1/5 concentration %; $ value/duration for any non-MSFT/Meta customer; official post-money for Toloka/Avride/TripleTen; Recursion/CHAI as customers; MSFT $6.96B upfront verbatim in a NBIS primary doc (verified via 20-F figure $6,958.1M actually — see contract-quality raw).
