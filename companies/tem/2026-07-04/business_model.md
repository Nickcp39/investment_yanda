# TEM Business Model (M2)

Last updated: 2026-07-04 | as_of: 2026-07-04 | sources: facts.md, source_register.md

---

## What Tempus AI Does

Tempus AI is an AI-enabled precision-medicine company built around a single core asset: a large, growing, longitudinally-linked clinical + molecular + imaging dataset generated from its own diagnostic testing business. It monetizes this asset through two reportable product lines that feed each other:

### Product Line 1: Diagnostics (~75% of FY2025 revenue, $955.4M, +111.5% YoY)

CLIA-certified laboratory testing sold to physicians/hospitals (reimbursed by Medicare/Medicaid/commercial insurance) and directly to pharma/research customers (direct-bill).

- **Oncology** (xT, xF assays): comprehensive genomic profiling for cancer patients — the founding product line. Volume +26-29% YoY.
- **Hereditary**: germline genetic testing, added at scale via the **Ambry Genetics acquisition** (closed Feb 2025, ~$375M cash) — this is the single largest driver of Diagnostics revenue growth in FY2025/Q1-2026 (Ambry alone contributed $63.5M revenue / $5.5M net income in its first comparable quarter).
- **MRD** (minimal residual disease) testing: early-stage but hyper-growth (~6,500 tests Q1 2026, +~500% YoY) — a genuine new-product vector, still small in dollar terms.
- **Paige AI** (digital pathology, acquired 2025) and **Deep 6 AI** (clinical trial matching software, acquired 2025) are adjacent acquisitions expanding the diagnostic surface into pathology imaging and trial-matching workflows.

Each test performed generates a data record (genomic + clinical outcome + often imaging) that feeds Product Line 2.

### Product Line 2: Data and Applications (~25% of FY2025 revenue, $316.4M, +30.9% YoY)

De-identified data licensing + AI tooling sold to pharma/biotech customers for drug discovery and development.

- **Insights** (data licensing, the largest sub-line): licenses de-identified multimodal data (genomic + clinical + imaging) to pharma companies for target discovery, biomarker validation, and clinical trial design. Growing 38.0% YoY (FY2025) / 44.1% YoY (Q1 2026). This is the "AI moat" story — but note the FY2025 comp base was distorted by a one-off AstraZeneca warrant termination gain in FY2024, so headline growth rates require care.
- **Algorithms/"Algos"** (applications sub-line): commercialized AI models built on the data (e.g., cancer subtype classifiers). Only **$20.2M** FY2025 (1.6% of total revenue) — the company itself states it has "limited commercialized algorithms" and is early in monetizing this layer. This is the most nascent, most option-value-like piece of the story.
- **AI clinical trial matching**: software connecting patients to trials using Tempus data (via Deep 6 AI integration).

### The flywheel mechanism (the actual thesis, stated plainly)

More tests performed → more clinical-genomic-imaging data generated → more valuable data asset for pharma licensing AND for training better proprietary algorithms → better algorithms (diagnostic accuracy, drug-response prediction) → more physicians/health systems adopt Tempus testing → more tests performed. This is a genuine network-effect candidate IF the data asset is (a) sufficiently differentiated from competitors' data (Foundation Medicine/Guardant also generate genomic data at scale) and (b) actually improves diagnostic/commercial outcomes in a way customers pay for. See `moat_map.md` and `bottleneck_map.md` for a rigorous test of whether this flywheel is real or aspirational at the current stage.

---

## Revenue Composition

| Revenue Stream | ~% of FY2025 Total | Durability | Pricing Power | Related-Party Exposure |
|---|---|---|---|---|
| Oncology Diagnostics (core) | ~45-50% | High — physician relationships, CLIA moat | LOW — company admits reimbursement lags FMI/Guardant (facts.md E44) | None |
| Hereditary Diagnostics (Ambry) | ~20% | Medium-high — M&A-added, integration risk | Medium | None |
| MRD (early) | <5% | Unproven — hyper-growth off small base | Unknown | None |
| Insights (data licensing) | ~20% | Medium — lumpy, back-half-weighted, comp-base noise | Medium-high (AstraZeneca/GSK $100M+ deals show real pricing power) | **Growing fast** (SB Tempus, Pathos — facts.md E41-E43) |
| Algorithms/Applications | ~1.6% | Unproven | Unknown — nascent | None disclosed |

**The critical insight**: the "AI data moat" narrative that justifies a premium multiple rests overwhelmingly on the Insights sub-line (~20% of revenue) and the Algorithms line (~1.6% of revenue) — together well under a quarter of the business. Three-quarters of revenue is a genomic-testing lab business competing on reimbursement economics where the company itself admits it is currently behind the two most direct public comps (Foundation Medicine/Roche, Guardant Health).

---

## Business Model Economics

| Metric | FY2024 | FY2025 | Q1 2026 (quarter) | FY2026 Guide |
|---|---|---|---|---|
| Total revenue | $693.4M | $1,271.8M (+83.4%) | $348.1M (+36.1% YoY) | ~$1,590M (~+25%) |
| Adjusted EBITDA | $(104.7)M | $(7.4)M | not separately disclosed in extracted 10-Q text (OPEN) | ~$65M |
| Net loss | $(705.8)M | $(245.0)M | $(125.9)M | n/a |
| OCF (burn) | $(189.0)M | $(218.1)M | $(73.3)M (vs $(105.6)M Q1-2025) | n/a |
| Stock-based comp | $534.1M | $124.7M | $52.7M | n/a |

**Read**: Revenue growth is real, primary-sourced, and accelerating in absolute dollars even as the YoY % normalizes off a smaller base. Adjusted EBITDA crossed into low-single-digit-million positive territory in Q4 2025 ($12.9M) — a genuine inflection, though FY2025 full-year adj EBITDA is still negative. The FY2026 guide of ~$65M adj EBITDA on ~$1.59B revenue implies a ~4% margin — thin, but a continued trajectory toward sustained profitability if execution holds.

---

## Value-Creation Levers

1. **Reimbursement rate closure vs FMI/Guardant**: the single largest disclosed margin lever on 75% of revenue. Company is actively pursuing MAC (Palmetto) approval and commercial in-network status — success here could materially expand Diagnostics gross margin without needing volume growth.
2. **Ambry/Hereditary cross-sell and integration**: capturing the full hereditary-testing TAM alongside oncology referral relationships.
3. **Data-licensing deal maturation**: moving from one-off/annual licensing deals (AstraZeneca ~$200M, GSK ~$70M) toward "companies building proprietary AI models directly on Tempus' platform" (per trade press) — a stickier, higher-switching-cost relationship if it materializes at scale.
4. **Algorithm monetization**: the $20.2M Applications line is the most option-value-like piece — if Tempus can get payers to reimburse algorithmic outputs (not just raw sequencing), this could become a high-margin software-like revenue stream. Currently unproven at scale.
5. **Operating leverage on SG&A**: SG&A grew from $154.6M to $212.6M YoY in Q1 2026 (+37%) — roughly in line with revenue growth, so leverage has not yet clearly emerged in this line; watch this trend for confirmation the model scales.

---

## Customer Concentration & Structure

- Diagnostics customers: physicians/health systems (Medicare/Medicaid/commercial-insurance reimbursed) + direct-bill research institutions and pharma/biotech.
- Data and Applications customers: pharmaceutical/biotech companies (AstraZeneca, GSK, Merck, BMS, Gilead named in press/trade sources) — concentrated in a relatively small number of large pharma relationships, which the company itself flags as vulnerable to biotech-sector macro conditions and budget-cycle timing (back-half-weighted revenue).
- **Related-party customers are a growing, non-trivial slice of Data and Applications**: SB Tempus (SoftBank JV, Japan) and Pathos (Lefkofsky-co-founded) together drove related-party revenue from $0.631M (Q1 2025) to $21.823M (Q1 2026) — now ~25% of the entire Data and Applications segment in that quarter. This concentration in related-party counterparties is a data point that deserves ongoing scrutiny (see `inversion_map.md` and `operator_underwriting.md`).
