# TEM Value Chain Map

Last updated: 2026-07-04 | as_of: 2026-07-04 | sources: facts.md, business_model.md

---

## The Precision-Medicine / Clinical-Genomic Data Value Chain

```
Patient sample (blood/tissue biopsy)
        |
        v
[1] SAMPLE PROCESSING & SEQUENCING  <-- Tempus captures value here (Diagnostics)
    - CLIA-certified labs (Chicago, Durham NC, Raleigh NC/Palmetto MAC, others)
    - NGS panels: xT (solid tumor), xF (liquid biopsy), Hereditary (Ambry)
    - Turnaround: ~9 days xT / ~8 days xF (company claims competitive vs FMI/Guardant)
        |
        v
[2] MOLECULAR + CLINICAL DATA INTEGRATION  <-- Tempus's structural bet
    - Genomic result + de-identified clinical/outcomes data + (increasingly) imaging/pathology (Paige AI)
    - This is the layer competitors often DON'T fully capture (FMI/Guardant are more purely genomic;
      Tempus explicitly integrates clinical + imaging + genomic -- the "multimodal" claim)
        |
        v
[3] CLINICAL REPORTING  <-- reimbursed via Medicare/Medicaid/commercial insurance
    - Delivered to ordering physician
    - THIS is where Tempus admits (10-K, facts.md E44) its reimbursement RATE lags FMI/Guardant
    - Volume growth is strong; PRICE per test is the disclosed weak point
        |
        v
[4] DE-IDENTIFIED DATA AGGREGATION  <-- Data and Applications segment
    - Aggregated across ALL Tempus tests performed (oncology + hereditary + MRD)
    - Licensed to pharma/biotech for: target discovery, biomarker validation, trial design,
      AI/foundation-model training (AstraZeneca/Pathos "largest multimodal foundation model
      in oncology" -- facts.md E35)
        |
        v
[5] AI MODEL / ALGORITHM LAYER  <-- smallest, most nascent, most "optionality" piece
    - Commercialized Algos ($20.2M FY2025, 1.6% of revenue)
    - Company explicitly states "limited commercialized algorithms" -- early innings
        |
        v
[6] CLINICAL TRIAL MATCHING / APPLICATIONS  <-- Deep 6 AI integration
    - Connects patients to trials using Tempus data; monetized via pharma/CRO relationships
```

---

## Where Tempus Captures Value Today (by revenue $)

| Value Chain Step | FY2025 Revenue Attribution | Margin Character | Competitive Intensity |
|---|---|---|---|
| [1]+[3] Sample processing + clinical reporting (Diagnostics) | $955.4M (75%) | Reimbursement-gated; admits lag vs FMI/Guardant | HIGH — FMI (Roche), Guardant Health, Natera, Exact Sciences all compete directly |
| [4] De-identified data licensing (Insights) | ~$253M (~20%, Insights sub-line of the $316.4M Data segment) | High-margin if scaled; lumpy/back-weighted | MEDIUM — fewer direct comps at Tempus's multimodal breadth, but Flatiron Health (Roche-owned), Veracyte, and hyperscaler/pharma internal data efforts are latent competitors |
| [5]+[6] Algorithms + trial matching | $20.2M + undisclosed (1.6%+) | Software-like potential, unproven at scale | LOW today (nascent), but this is where hyperscalers (Google/Microsoft health AI units) could eventually compete if they access comparable clinical data |

---

## Structural Observation: Tempus's Bet vs the Market's Price

The bull case requires steps [4]-[6] (the AI/data layer, ~25% of revenue) to become the dominant value-capture point over time, effectively subsidized in the near term by step [1]+[3] (the lab-services business, 75% of revenue) which itself has a disclosed reimbursement-economics weakness. This is structurally similar to a "loss-leader lab generates the proprietary dataset; monetize the dataset" model — which can work (this is close to how Illumina/genomics-adjacent data plays have historically been framed) but requires (a) the data to be genuinely differentiated from what FMI/Guardant/Natera also generate at their own testing scale, and (b) pharma customers to keep paying premium prices for it rather than building competing internal data assets or partnering with a lower-cost data aggregator.

See `moat_map.md` for the durability test on this bet, and `bottleneck_map.md` for whether the clinical-genomic-data network effect is real at Tempus's current scale relative to larger genomic-testing competitors.
