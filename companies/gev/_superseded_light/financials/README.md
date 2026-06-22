# Financials — GEV

Purpose: turn reported accounting into economic reality. **For GEV the #1 job is the one-off reconciliation** — the headline GAAP numbers are heavily distorted.

Primary artifact: `financial_quality.md` (the accounting → economics bridge + the one-off normalization).

Minimum checks (applied in `financial_quality.md`):
- Revenue + operating income by segment (Power / Electrification / Wind)
- Net income **stripped of** the FY2025 tax-valuation-allowance release + Q1'26 Prolec/Proficy M&A gains
- FCF **stripped of** the advance-payment / contract-liability timing benefit
- Margin trajectory (16% → 22% Power/Electrification; Wind drag)
- Capital allocation: dividend, buyback, Prolec M&A, capex; balance sheet (IG, <1x leverage)

Facts cite `../facts.md` / `../claim_ledger.csv`. Forward numbers are guide/assumptions, not facts.
