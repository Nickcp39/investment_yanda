# RMD Value Chain Map

Last updated: 2026-07-05 | as_of: 2026-07-05 | sources: facts.md E5-E48

---

## Chain: Diagnosis → Device Sale → Consumables Resupply → Data → Software/AI → Reinforced Adherence

```
[1] DIAGNOSIS
    Sleep study (in-lab polysomnography OR home sleep apnea test e.g. RMD's NightOwl)
    → OSA diagnosis, AHI (Apnea-Hypopnea Index) severity score assigned
    → Physician prescribes CPAP/APAP therapy
        |
        | (GLP-1 intersection point: weight-loss-drug patients increasingly
        |  screened for OSA during drug-engagement visits — bull case;
        |  OR some patients achieve enough weight loss to avoid diagnosis
        |  threshold entirely — bear case; unresolved, see business_model.md)
        v
[2] DEVICE SALE (capital-equipment-style, ~52% of FY25 revenue)
    DME (durable medical equipment) provider or hospital/sleep-lab
    purchases AirSense 11 (or similar) device from RMD
    → Sold via DME channel (largest), hospital/health-system channel,
      increasingly direct-to-consumer/telehealth
    → Device is 100% cloud-connectable (31.5M+ installed base, E36)
        v
[3] MASK FITTING + ONBOARDING
    Patient fitted with mask (multiple form factors: nasal, full-face, pillow)
    → myAir app onboarding; Smart Comfort AI recommends personalized
      comfort settings from day 1 (FDA-cleared Dec 2025, E35)
        v
[4] ONGOING THERAPY + DATA CAPTURE
    Device streams usage/pressure/leak/AHI data nightly to AirView cloud
    → 34M+ patients in AirView, 24B+ cumulative nights of data (E36)
    → AirView + generative AI (added 2025) flags at-risk/low-adherence
      patients for clinician outreach (E37)
        v
[5] CONSUMABLES RESUPPLY (TRUE recurring annuity, ~36% of FY25 revenue)
    Masks/cushions/tubing/filters replaced on ~3-6 month cycles per
    insurance resupply rules
    → This is the highest-quality, most annuity-like revenue line
    → Currently the FASTEST-growing line (+15% Q3 FY26 vs devices +9%, E26)
    → GLP-1+PAP patients show HIGHER resupply rates than PAP-only
      (+5.1% 2yr / +6.2% 3yr, E40) — a genuine adherence-driven
      reinforcement of this exact revenue line
        v
[6] REPLACEMENT CYCLE (~5yr device life)
    Device eventually replaced — patient re-enters step [2] but
    typically stays within the RMD ecosystem (myAir data/history,
    prescriber familiarity, insurance continuity) — genuine switching
    friction, though not quantified as a churn/retention rate this run
```

## Parallel/Adjacent Chain: Residential Care Software (Brightree/MatrixCare)

```
Home-health/hospice/HME/post-acute-care AGENCY (the customer, NOT the
end patient) subscribes to Brightree or MatrixCare SaaS
    → Manages billing, scheduling, clinical documentation, compliance
    → Distinct customer relationship from the Sleep and Breathing Health
      chain above — agencies, not individual OSA patients
    → ~3-4% of Q3 FY26 revenue, +6% YoY (E25/E26) — stable, lower-growth
      software annuity, strategically diversifying but not currently a
      major growth engine
```

---

## Where Value Concentrates / Where Margin Lives

- **Highest structural quality**: Masks/accessories resupply (step 5) — true recurring consumables, growing fastest, and the mix shift toward this line is the primary driver of the multi-year gross-margin expansion evidenced in facts.md (55.78%→62.2% FY23→Q3FY26).
- **Highest strategic leverage (unmonetized)**: The AirView/Smart Comfort data layer (steps 3-4) — this is the asset a new entrant (whether a legacy competitor or a China-based fast-follower) cannot replicate without years of connected-device installed base and hundreds of millions of nights of training data. It currently reinforces adherence/resupply (an indirect monetization) rather than generating its own separately-priced software revenue.
- **Most exposed to the GLP-1 debate**: Step [1] (diagnosis) and the device-sale step [2] — if GLP-1 materially reduces new-patient volume entering the funnel, the entire downstream chain (consumables, data, software reinforcement) shrinks with it. This is why the diagnosis-funnel question (not the retention/adherence question, which RMD has evidenced) is the crux risk.
- **Least differentiated / most commoditizable**: Base-tier device hardware and basic masks in price-sensitive international markets (see moat_map.md China discussion) — this is where BMC Medical/Jiangsu Yuyue-style domestic competitors compete, typically NOT at the premium/connected/AI-enabled tier where RMD's moat is strongest.
