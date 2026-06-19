# Financial Quality — GEV

Last updated: 2026-06-19

Source base: FY2025 10-K (S1), Q1'26 10-Q (S2), Q1'26 call (S3, confirmed via WebFetch 2026-06-19), Dec 2025 investor update (S4). Facts: `../facts.md` / `../claim_ledger.csv`.

## One-line read

A genuinely improving industrial — FY2025 revenue +9%, operating income +$0.9B, segment margins inflecting (Power 16.3% / Electrification 17.8% Q1'26, targeted 22%/22% by 2028) — **but the headline GAAP numbers are heavily distorted by three one-offs that all flatter the same period.** Strip them and the clean reads are FY2025 operating income **$1.39B** and 2026 guide adjusted EBITDA **~$5.7–6.4B**. Wind is a real, *widening* loss. The balance sheet is investment-grade (<1x leverage, $10.17B cash).

## ⚠️ The One-Off Reconciliation (do this before anything else)

| # | One-off | Period | Size | What it distorts | claim_id |
|---|---|---|---:|---|---|
| 1 | **Tax valuation-allowance release** | FY2025 | ~$2.9B | FY2025 **net income $4.9B** (non-operating, non-cash) | C003 |
| 2 | **M&A gains (Prolec remeasurement + Proficy sale)** | Q1'26 | ~$4.5B | Q1'26 **net income $4.745B** — primarily Prolec buy-in remeasurement, **excluded from adjusted EBITDA**; Proficy ~$0.33–0.6B | C006 |
| 3 | **Working-capital / contract-liability inflow** | Q1'26 | ~$5.3B benefit (contract-liability ~+$5.6B) | Q1'26 **FCF $4.8B** — customer reservation deposits, deferred-revenue timing, **not earned profit** | C007 |

> **Screener TTM net income ~$9.4B / EV-EBITDA ~85x DOUBLE-COUNTS (1)+(2)** (C008). **Discard trailing GAAP.** Use: FY2025 operating income **$1.39B**; 2026 guide adj-EBITDA margin **12–14%** (≈ $5.7–6.4B); normalized FCF **below** the $4.8B Q1 print.

## Accounting → Economics Bridge

| Item | Reported | Economic interpretation | claim_id |
|---|---:|---|---|
| FY2025 revenue | $38.07B (+9%) | Real, broad-based (Power + Electrification) | C002 |
| FY2025 operating income | $1.39B (+$0.9B) | **Cleanest FY2025 profitability read** | C002 |
| FY2025 net income | $4.9B | **Not economic** — ~$2.9B is a tax-valuation-allowance release; strip it | C003 |
| FY2025 FCF | $3.7B (>2x FY2024) | Genuine improvement; benefits at margin from down-payment timing | C004 |
| Q1'26 revenue | $9.34B (+16%) | Real growth | C005 |
| Q1'26 net income | $4.745B | **Not economic** — ~$4.5B M&A gains (excluded from adj EBITDA) + Proficy | C006 |
| Q1'26 FCF | $4.8B | **Flattered** by ~$5.3B WC benefit (advances); normalized far lower | C007 |
| Q1'26 segment EBITDA | Power 16.3% / Elec 17.8% / Wind −$382M | The real economics — group GAAP is one-off noise | C021 |
| Cash / leverage | $10.17B / <1x gross debt-EBITDA | Investment-grade; funds Prolec + capex + returns | C009 |
| 2026 guide | rev $44.5–45.5B / adj-EBITDA 12–14% / FCF $6.5–7.5B | **The clean forward anchor** | C010 |

**Normalized earning-power estimate:** the honest clean base is FY2025 operating income ~$1.39B rising toward the 2026 adjusted-EBITDA guide (~$5.7–6.4B) and the 2028 target (~$10B+ EBITDA on ~$52B revenue at ~20%). The *bridge from here to there is the investment question* — and it embeds a cyclical equipment-pricing premium (see `../valuation.md`, `../model/`).

## Quality Questions

- **Is revenue recurring?** Partly — **$87.4B (54%) of the $163.3B RPO is services** (multi-decade, sticky aftermarket on ~7,000 turbines) = high-quality recurring. The $75.9B equipment book carries the *cyclical* +10–20% pricing premium. (C011, C016)
- **Does growth require rising capital intensity?** Moderate and *measured* — $10B 2025–28 capex/R&D, capacity adds paced 20→24 GW/yr. Watch ROIC as capacity lands 2027–28 (kill c). (C031)
- **Are margins expanding from scale, pricing, or cycle?** A mix: real operating leverage + Electrification scale **and** a *cyclical* equipment-pricing premium (+10–20%) that may not persist. Don't assume the premium is structural. (C016)
- **Is FCF overstating owner earnings?** **Yes, currently** — Q1'26 FCF $4.8B is flattered ~$5.3B by advance payments. The *normalized* FCF is materially lower; a clean bridge stripping the timing is an **open gap**. (C007)
- **Buybacks / dividends?** Yes — dividend doubled to $2.00/yr; buyback $6B→$10B ($3.3B spent); ~$3.6B returned 2025. Retiring shares, IG-disciplined. (C025, C026)

## Red Flags / Quality Notes

1. **🚩 Three coincident one-offs flatter the trailing window** — tax release + M&A gains + advance-payment FCF. Any trailing-GAAP read is wrong. (C003, C006, C007)
2. **🚩 Wind is a *widening* loss** — Q1'26 −$382M vs −$146M; FY2026 ~−$400M EBIT; $250–350M/yr tariff headwind. A real drag inside the quality story. (C028)
3. **FCF quality** — 2026 FCF guide $6.5–7.5B partly advance-payment timing; normalized lower. (C007)
4. **M&A-gain noise from Prolec** — clean transaction, but a reminder to read adjusted, not GAAP. (C006, C027)

## So what

The underlying economics are genuinely good and improving — segment margins inflecting, services annuity durable, balance sheet strong. **But reported profitability quality this trailing window is low because of the one-offs**, and the path to the 2028 targets embeds a *cyclical* equipment-pricing premium. Re-underwrite on **adjusted, forward** figures — never trailing GAAP. Carried into `../valuation.md` and `../model/`.
