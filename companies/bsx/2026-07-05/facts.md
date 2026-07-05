# BSX Facts (Evidence Foundation)

Last updated: 2026-07-05 (run_date) | as_of: 2026-07-05 | as_of_price: **$45.14**
Source discipline: `../../../sources/source_policy.md`. Only A1/A2 primary or explicitly labeled derived enters EVIDENCE; commentary/secondary only in SENTIMENT/OPEN.

---

## EVIDENCE (A1/A2 verified)

### Price / Market Data
- E1. Last close (2026-07-02): **$45.14** [YAHOO-BSX-PRICE — independently re-fetched via scripts/market_data_download.py; matches frozen as_of_price input exactly]
- E2. 52-week high: **$108.14** (2025-09-08) / 52-week low: **$42.68** (2026-06-30, per Yahoo daily close series; stockanalysis.com shows intraday low $42.25) → price is **−58.3% off 52wk high**, **+5.8% above 52wk low (Yahoo basis)** — a LOW-HUG pattern [YAHOO-BSX-PRICE]
- E3. Market cap: **~$67.1B** (1.49B shares × $45.14) [BSX-SA-STATS]; shares outstanding **~1.49B** [BSX-SA-STATS]
- E4. Trailing P/E **18.89x** / Forward P/E **13.15x**; Beta **0.58**; no dividend (BSX does not pay a dividend) [BSX-SA-STATS]
- E5. Analyst consensus: **Buy** (30 analysts); average price target **~$75.00** (+66% from $45.14) [BSX-SA-STATS]
- E6. Next earnings (Q2 2026) scheduled **2026-07-29** [BSX-SA-STATS]

### CRITICAL FINDING: Verified Real, Multi-Event Drawdown (Not a Data Error)
- E7. Full daily price series 2025-07-01→2026-07-02 confirms a sustained, THREE-STEP decline driven by three distinct earnings/guidance events, not a single crash or stale price:
  - **Event 1 — 2026-02-04 (Q4/FY2025 earnings, 8-K item 2.02)**: stock fell **−17.6% same day** ($91.62→$75.50). FY2025 results themselves BEAT guidance (net sales $5.286B Q4, +15.9% reported/+12.7% organic vs guided 11-13%; adj EPS $0.80 vs guided $0.77-0.79), but initial FY2026 guidance (10.5-11.5% reported growth / adj EPS $3.43-3.49) was perceived as light relative to FY2025's 15.8% organic growth rate and elevated investor expectations. This is also the START of the alleged securities-fraud class period end-date (see E20). [MOTLEYFOOL-FEB4 / BSX-Q4FY25-PR]
  - **Event 2 — 2026-04-22 (Q1 2026 earnings, 8-K item 2.02)**: Q1 2026 itself beat (net sales $5.203B, +11.6% reported/+9.4% organic; adj EPS $0.80 vs $0.75 PY) but management CUT full-year 2026 guidance from 10.5-11.5%/$3.43-3.49 EPS down to **7.0-8.5% reported (6.5-8.0% organic) / adj EPS $3.34-3.41**, citing three areas: Electrophysiology (larger-than-expected US market-share erosion despite strong absolute growth), Watchman (standalone-procedure deceleration since February, offset partly by concomitant-procedure strength), and Urology (~2% YoY growth, well below expectations, $646M Q1 sales). Stock actually ROSE ~9% same day on relief that Q1 beat estimates despite the cut. [MASSDEVICE-APR22 / BSX-Q1-2026-PR]
  - **Event 3 — 2026-05-27 (Bernstein 42nd Annual Strategic Decisions Conference presentation, not an 8-K earnings release)**: stock fell **−10.3% to −12.5% intraday** (new 52wk low $50.75 that day), CEO Mahoney cut guidance AGAIN to **full-year organic growth 6.5-8.0%** (Q2 2026 guided at just 5-7% organic), citing "unanticipated headwinds and changing business patterns" — the same three factors (EP competitive share loss, Watchman standalone deceleration, Urology softness) reiterated as WORSE than the April 22 framing suggested. Daiwa downgraded to Neutral (target $83→$60); Bank of America cut target $105→$68 (kept Buy). [TRADINGPEDIA-MAY27 / STOCKTWITS-BERNSTEIN]
  - Stock continued declining through June 2026 on a wave of further analyst price-target cuts (TD Cowen $80→$61, Piper Sandler $90→$65, BofA $68→$61, Wells Fargo downgraded Overweight→Equal Weight with target $75→$55) before a partial rebound to $45.14 by 2026-07-02. [WSJ/AGGREGATOR search corroboration]

### The Core Quantified Driver: Electrophysiology (Farapulse PFA) US Market Share Erosion
- E8. **BSX's US PFA (pulsed-field ablation) market share fell from ~100% (2023, launch-year monopoly) to ~41% (early 2026)**, while Medtronic (PulseSelect, launched Jan 2024) grew to **~48% share** — Medtronic has now SURPASSED BSX in the segment BSX pioneered. J&J/Biosense Webster's Varipulse (launched Dec 2024) reached **~11% share**; Abbott's Volt (launched Jan 2026) reached **~1% share** in its first months. [QSIGHT-GUIDEPOINT-PFA2026 — industry analyst tracking, B2 tier, cited across multiple corroborating sources]
- E9. Despite share loss, the underlying EP MARKET is still growing fast: total AFib ablation catheter unit volume grew from ~76,000 (2018) to ~250,000 (2025); total market spend grew from ~$1B to ~$3.8B over the same period, +20% YoY unit growth in 2025 alone [QSIGHT-GUIDEPOINT-PFA2026]. BSX has treated **500,000+ patients cumulatively** with Farapulse [company-cited, multiple sources].
- E10. Q1 2026 EP segment itself grew organically **+22%** globally (+18% US, +30% international) — i.e., BSX's EP business is NOT shrinking, it is growing more slowly than the market/competitors, which is a RELATIVE share-loss problem, not an absolute revenue collapse [FOOL/SIMPLYWALLST Q1 coverage — needs primary-source (10-Q) confirmation, currently B1/B2 sourced, flagged O-item].
- E11. Investor Day (2025-09-30) framing: global EP market forecast to grow from **~$13B (2025) to ~$20B (2028)**; PFA global penetration of the broader ablation market expected to reach **~50% by end-2025, ~80% by 2028**; BSX's stated ambition (per EP global president Nick Spadea-Anello) is to be "not just a leader in pulsed field ablation, but a leader in overall electrophysiology" [BSX-INVESTOR-DAY-2025 — company source, A2].

### Watchman (LAAC) Specifics
- E12. Q1 2026 Watchman sales: **$506M**, +19.2% YoY — still growing, but management explicitly flagged that STANDALONE Watchman procedures began DECLINING in February 2026 for the first time (offset by continued strength in CONCOMITANT procedures, i.e. Watchman implanted alongside another cardiac procedure) [multiple B1/B2 sources corroborating the Apr 22 and May 27 management commentary — needs primary 10-Q confirmation].
- E13. FY2025 Watchman growth: **+29%** (both Q4 2025 and full-year) — following ~30% growth in prior year (2025 vs 2024) per management's own framing at the May Bernstein conference [BSX-Q4FY25-PR / TIKR-BERNSTEIN].

### Litigation (LIVE — material, must refresh each run)
- E14. **Active securities fraud class action lawsuits** (multiple law firms: Levi & Korsinsky, others) filed in 2026 against Boston Scientific Corporation AND FIVE NAMED EXECUTIVES: Chairman/CEO Michael F. Mahoney, CFO Jonathan R. Monson, Chief Medical Officer Kenneth M. Stein, EVP Cardiology Joseph M. Fitzgerald, and Global President of Electrophysiology Nicholas Spadea-Anello. Alleged class period: **2025-07-23 to 2026-02-03** (i.e., ending the day BEFORE the Feb 4 gap-down). Core allegation: defendants made materially false/misleading statements about EP segment growth sustainability and competitive strength while allegedly concealing deteriorating market share and slowing growth. Lead plaintiff deadline was **2026-05-04**. [ZLK-CLASSACTION / MORNINGSTAR-PRNEWSWIRE-INVESTORALERT — multiple corroborating law-firm investor-alert press releases, B1/B2 tier legal-notice sources; status as of as_of date is ACTIVE/UNRESOLVED, no settlement or dismissal found this run]

### Corporate Structure / Segments (FY2025 as-filed)
- E15. BSX reorganized in Q4 2025: combined legacy **Cardiology** + **Peripheral Interventions** into a single **"Cardiovascular"** reportable segment. Current two reportable segments: **Cardiovascular** (66.0% of FY2025 revenue) and **MedSurg** (34.0% of FY2025 revenue, comprising Endoscopy / Urology / Neuromodulation) [BSX-SA-FINANCIALS / search cross-check — 10-K primary confirmation still pending, O-item].
- E16. Cardiovascular segment includes: Interventional Cardiology (coronary/structural heart), WATCHMAN (LAAC), Cardiac Rhythm Management (CRM/pacemakers-ICDs), Electrophysiology (Farapulse PFA + OPAL mapping), and Peripheral Interventions (vascular). MedSurg includes Endoscopy, Urology, Neuromodulation (incl. 2026 Nalu Medical acquisition — peripheral nerve stimulation for chronic pain) [BSX-Q4FY25-PR].
- E17. CEO: **Michael F. Mahoney** — Chairman & CEO since **October 2011** (~14.7 years tenure as of as_of date) [SIMPLYWALLST-MGMT / search cross-check].

### FY2025 Full-Year Results (filed 2026-02-04 per 8-K item 2.02; 10-K filed 2026-02-17)
- E18. FY2025 net sales: **$20.074B**, +19.9% reported / +19.2% operational / +15.8% organic (vs FY2024) [BSX-Q4FY25-PR]. Note: an independent aggregator (stockanalysis.com) shows FY2025 revenue as $20,074M and FY2024 as $16,747M — consistent with the +19.9% reported growth figure, confirming internal coherence.
- E19. FY2025 GAAP diluted EPS: **$1.94**; adjusted EPS: **$3.06** [BSX-Q4FY25-PR / BSX-SA-FINANCIALS].
- E20. FY2025 gross margin: **69.01%**; operating margin: **18.00%**; operating income **$3,613M**; net income **$2,892M** [BSX-SA-FINANCIALS].
- E21. Q4 2025 segment detail: MedSurg $1.809B (+6.5% organic); Cardiovascular $3.477B (+16.1% organic). FY2025: MedSurg $6.824B (+6.7% organic); Cardiovascular $13.250B (+20.8% organic) [BSX-Q4FY25-PR].
- E22. FY2025 initial FY2026 guidance (given 2026-02-04, later cut TWICE — see E7): net sales growth ~10.5-11.5% reported / 10.0-11.0% organic; adjusted EPS $3.43-3.49 [BSX-Q4FY25-PR].

### Q1 2026 Results (filed ~2026-04-22 per 8-K item 2.02; 10-Q filed 2026-05-01)
- E23. Q1 2026 net sales: **$5.203B**, +11.6% reported / +9.4% organic [BSX-Q1-2026-PR / SEC-8K-Q1-2026].
- E24. Q1 2026 segment detail: **MedSurg $1.701B** (+7.8% reported/+5.7% organic) — Endoscopy $736M (+9.4%/+6.8% organic), Urology $646M (+2.1%/+0.5% organic), Neuromodulation $318M (+17.4%/+15.4% organic). **Cardiovascular $3.503B** (+13.5% reported/+11.2% organic) [BSX-Q1-2026-PR].
- E25. Q1 2026 geographic: US $3.284B (+10.9%); EMEA $932M (+10.1% reported/+1.2% operational); APAC $803M (+14.7% reported/+12.0% operational); LACA $185M (+19.0% reported/+12.0% operational) [BSX-Q1-2026-PR]. Note: China is NOT separately broken out from APAC in this release — material OPEN item for career-relevant China analysis (O7).
- E26. Q1 2026 GAAP net income: **$1.341B** ($0.90 diluted EPS, vs $674M/$0.45 EPS prior year — GAAP figure boosted by a one-off, not yet identified this run, flagged O-item); adjusted EPS **$0.80** (vs $0.75 PY) [BSX-Q1-2026-PR].
- E27. Q1 2026 gross profit **$3.614B**, gross margin **69.5%** [BSX-Q1-2026-PR].
- E28. Q1 2026 guidance revision (first cut): full-year 2026 net sales growth reduced to **7.0-8.5% reported / 6.5-8.0% organic**; adjusted EPS reduced to **$3.34-3.41** [BSX-Q1-2026-PR / MASSDEVICE-APR22].

### China / International Exposure
- E29. BSX's China strategy (per company commentary, 2025-era) targeted **China revenue "well above $1 billion" in 2025** [company-cited via search, needs primary confirmation — O-item] and has historically framed China as a growth market despite VBP (volume-based procurement) pricing pressure, with company messaging emphasizing "learning to thrive in VBP" (in contrast to peers who have "pulled back") and investing in "innovative Chinese companies" as part of its portfolio strategy [search-derived, B2 tier, needs primary IR/10-K confirmation — O-item].
- E30. Recent (2026) commentary: China described as delivering "robust growth despite VBP-related impacts," led by interventional cardiology / imaging technologies [search-derived B2, needs primary confirmation].
- E31. 10-K risk factors (per secondary summary, primary text not yet directly read — O-item): BSX explicitly identifies competition from **domestic medical device companies benefiting from local-supplier status, particularly in China**, as a named competitive risk factor [search-derived summary of 10-K language, B2 — primary verbatim text still OPEN].

### Tariffs
- E32. BSX guided to **fully offsetting ~$200M of tariff costs in 2026** through pricing/cost actions [search-derived, B1/B2 — needs primary 10-Q/earnings-call confirmation, O-item]. Broader medtech sector context: Section 301 China tariffs plus Section 122/232 layering can push effective duty rates on some Chinese-sourced device components/materials above 40-50% as of 2026 [MEDDEVICEGUIDE — industry-general context, not BSX-specific].

### Management Compensation
- E33. CEO Mahoney total compensation: **~$23.5M in 2025** (salary $1.44M, stock awards $13.6M, option awards $3.8M, cash bonus $4M) — a **+10% increase** from 2024's $21.4M (itself +14% from 2023's $18.7M) [MEDICALDESIGN-CEOPAY — proxy-statement-sourced media coverage, B1/B2, needs DEF 14A primary cross-check — O-item]. **Notable tension**: comp rose ~10% in the same fiscal year (2025→2026 disclosure cycle) that guidance was cut three times and a securities-fraud suit was filed naming Mahoney personally.

---

## INTERPRETATION (derived/judgment)

- I1. **The drawdown is a real, evidenced, three-stage fundamental repricing, not a data artifact or single-event panic**: each of the three major price gaps (Feb 4, Apr 22 magnitude, May 27) corresponds to a specific, identifiable corporate disclosure event with a clear, consistent causal narrative (EP share loss + Watchman standalone deceleration + Urology softness), each confirmed via ≥2 independent sources. This satisfies the T2 low-hug tripwire justification requirement.
- I2. **The EP story is genuinely nuanced, not a simple "moat broken" story**: BSX's Farapulse franchise is still growing at a healthy absolute rate (Q1 2026 +22% organic globally) and BSX remains the single largest player by cumulative patients treated (500,000+) — but it went from a 100% monopoly (2023) to trailing Medtronic in share (41% vs 48%, early 2026) in about 2.5 years. This is the single most important, career-relevant finding: first-mover advantage in a hot medtech category compressed extremely fast once two more large, well-capitalized competitors (Medtronic Jan 2024, J&J Dec 2024) and now a third (Abbott Jan 2026) entered. The overall PFA market is still expanding rapidly (unit volume +20%/yr), so this is a share-of-a-growing-pie problem, not a shrinking-pie problem — but the SPEED of share loss from monopoly to sub-50% in ~2 years is a real data point on how fast medtech moats can erode absent a structural (patent/regulatory/switching-cost) barrier.
- I3. **Securities litigation is a live, material, unresolved risk**: naming the CEO, CFO, CMO, and two other named executives personally is a serious escalation beyond a routine "stock dropped, lawyers circled" pattern — it specifically alleges management KNEW about and concealed the competitive deterioration during the 2025-07-23 to 2026-02-03 class period. This must be tracked in freshness.json as LIVE-qualitative (active_litigation) and re-verified every refresh; no resolution (settlement, dismissal, or advancement) confirmed as of as_of.
- I4. **Watchman's standalone-vs-concomitant split is an important, not-yet-fully-quantified nuance**: management describes concomitant Watchman (implanted alongside another procedure) as still strong, only standalone procedures declining since February 2026. This distinction matters for the moat analysis (durability of Watchman as an independent franchise vs. an attach-rate product) but is not numerically broken out in any source found this run — flagged O-item.
- I5. **China/APAC revenue is not separately broken out in current quarterly disclosure** (Q1 2026 shows APAC $803M but does not isolate China) — this is a material gap for the career-relevant China analysis and should be a top research priority for the next refresh (likely requires the 10-K geographic footnote or investor-day slides, neither fully extracted this run).
- I6. **Valuation context**: at $45.14, trailing P/E 18.89x / forward P/E 13.15x is a STEEP de-rating from where BSX traded in 2025 (52wk high $108.14 implies the stock was trading at a materially higher multiple on lower or similar earnings). Average analyst target ~$75 (+66% upside) reflects a sell-side view that the selloff has substantially overshot the fundamental deterioration — but sell-side price targets are lagging indicators typically slow to fully re-rate, and multiple analysts (Wells Fargo, Daiwa) have already cut both target AND rating, suggesting the consensus itself is still adjusting downward, not stable.

---

## SENTIMENT (B2/C2 only — does not support thesis)

- S1. Sell-side largely remains constructive: "30 analysts rate Buy," average target ~$75 (+66% from current price) despite the guidance cuts — but this pre-dates the full run of June downgrades (Wells Fargo Overweight→Equal Weight, Daiwa to Neutral) which may not be fully reflected in the aggregate consensus figure pulled this run (potential staleness in the "30 Buy" figure — O-item).
- S2. 24/7 Wall St and other outlets frame the Apr 22 pullback as a potential "buying opportunity" given Q1 beat fundamentals, contrasted against the stock's steep decline — a classic "is this overdone" sell-side framing, not independently verified.
- S3. TIKR/other commentary frames the situation as a possible "60% mispricing" given the gap between fundamental EP growth (+22% Q1) and the stock's ~58% drawdown — directional commentary only, not a verified valuation conclusion.

---

## OPEN (unverified / gaps)

- O1. Primary SEC 10-K (filed 2026-02-17, accession 0000885725-26-000010) and 10-Q (filed 2026-05-01, accession 0000885725-26-000033) direct HTML fetch blocked (HTTP 403 on both SEC EDGAR direct-document attempts and the cgi-bin browse-edgar company search, 2 attempts made total per the robustness rule, no retry-loop). SEC's data.sec.gov submissions JSON API DID work (confirms CIK 885725, filing list/dates/accessions) — used for filing calendar/timeline reconstruction (E7, E15 context) but not for line-item financial extraction. All FY2025/Q1 2026 financial figures are cross-checked ≥2 independent secondary sources (official press releases via news.bostonscientific.com/prnewswire.com [A1, company-issued] + stockanalysis.com [B1 aggregator] + search-corroborated trade press).
- O2. Exact Watchman/Electrophysiology/Cardiac Rhythm Management/Interventional Cardiology PRODUCT-LEVEL sales figures (below the Cardiovascular segment roll-up) not confirmed from a primary financial-statement table this run — Q1 2026 Watchman ($506M) and EP (+22% organic) figures are sourced from secondary earnings-call coverage (Fool/SimplyWallSt/MassDevice), not directly from the 10-Q's segment footnote. Needs primary confirmation next refresh.
- O3. China-specific revenue % of total not found in any source this run (APAC is the smallest disclosed geographic bucket, China not broken out separately in Q1 2026 or Q4/FY2025 releases reviewed). This is the single largest gap for the career-relevant China analysis.
- O4. Balance sheet detail (total debt, cash, net debt, leverage ratios) not yet fetched — pending (see financial_quality.md placeholder).
- O5. Q1 2026 GAAP net income more than doubling YoY ($674M→$1.341B) while adjusted EPS only grew modestly ($0.75→$0.80) implies a significant one-off item (tax, gain on sale, remeasurement) inflating GAAP figures — not yet identified/confirmed this run.
- O6. Exact tariff $ impact and mitigation mechanics ($200M figure is search-derived, not confirmed from a primary earnings-call transcript or 10-Q).
- O7. Standalone vs. concomitant Watchman procedure volume/revenue split not numerically available.
- O8. Full Q1 2026 and Q4/FY2025 earnings call transcripts not fetched this run (time/efficiency tradeoff) — would likely resolve O2, O5, O6 and add management color on litigation (E14) and China (O3).
- O9. DEF 14A (proxy, filed 2026-03-18) not directly read — CEO comp figures (E33) are media-reported, not primary-verified; would also confirm insider ownership/incentive structure for operator_underwriting.md.
- O10. Farapulse/EP competitive share data (E8) is from a single industry-tracking source (Qsight/Guidepoint) cited across multiple secondary re-reports — treat as a single ultimate source until independently corroborated (e.g., via a sell-side note or company's own competitive commentary), though the 100%→41% direction is consistent with and directly explains the guidance-cut narrative from BSX's own management commentary (E7-E10), which corroborates the MAGNITUDE indirectly even if the tracking-firm source itself is singular.

---

*Facts current as of research completed 2026-07-05. See claim_ledger.csv for full source-tagged claim registry and source_register.md for tier/date detail on all sources cited above.*
