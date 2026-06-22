# GOOGL Valuation / Margin of Safety v2

Last updated: 2026-06-16

Scope: Layer 9 only. This is a valuation/MOS worker output for the v2 rerun. It does not mark the company research complete and does not edit the completion checker.

Decision support read: `WATCH / 0%` remains the right posture from valuation alone. The business quality is high, but the current price requires the AI capex cycle to become high-return owner earnings, while the hardest inputs are still OPEN.

---

## 1. Valuation Frame

This pass values Alphabet from owner earnings, not reported EPS and not a mechanical PE screen.

The core equation is:

`10Y value per share = terminal owner earnings * exit P/OE / diluted shares + interim dividends`

The owner earnings bridge starts from local model ranges:

| Branch | 2026 normalized owner earnings base | Meaning |
|---|---:|---|
| Defensive capex | $52B | A large part of AI capex is maintenance/defensive and absorbs OCF. |
| Mixed/delay | $65B | Capex starts earning, but payback lags revenue growth for several years. |
| Growth capex | $82B | Most AI capex is high-return growth investment and conversion improves. |

The crucial uncertainty is still the maintenance/growth capex split. Q1 2026 capex was $35.7B against $45.8B of OCF, and the 2026 capex guide is $180B-$190B, with 2027 expected to be significantly higher. At that scale, reported operating income is not enough. The model has to ask whether capex converts into common-share owner earnings after SBC, debt, preferred dividends, ATM issuance, and repurchases.

---

## 2. Current Price Anchor

Price anchor used: GOOGL $373.19 at 2026-06-16 19:09 UTC / 15:09 ET from a finance quote snapshot, cross-checked against public quote pages. Public quote URLs: [Yahoo Finance GOOGL](https://finance.yahoo.com/quote/GOOGL/), [Google Finance GOOGL](https://www.google.com/finance/quote/GOOGL:NASDAQ), [Nasdaq GOOGL](https://www.nasdaq.com/market-activity/stocks/googl).

Using 12.116B Alphabet economic shares outstanding from Q1 2026 filings, the price implies an approximate equity value of $4.52T.

| Metric | Value | Interpretation |
|---|---:|---|
| Price | $373.19 | Current valuation anchor; not a trade instruction. |
| Shares outstanding | 12.116B | Class A + B + C economic shares at 2026-03-31. |
| Equity value | $4.52T | Before June equity/preferred/ATM adjustments. |
| Q1 cash + marketable securities | $126.8B | Hard SEC figure. |
| Q1 long-term debt | $77.5B | Hard SEC figure; current portion excluded here. |
| Approx net cash less long-term debt | $49.3B | Only about $4/share, not enough to rescue valuation. |

Price-to-owner-earnings at the anchor:

| OE base | P/OE | Starting OE yield |
|---:|---:|---:|
| $52B defensive | 87x | 1.15% |
| $65B mixed | 70x | 1.44% |
| $82B growth | 55x | 1.81% |

Interpretation: current price already prices Alphabet as a successful AI capex compounder, not merely as a strong Search/Cloud franchise.

---

## 3. What The Price Already Implies

With a $65B owner earnings base and a 22x terminal P/OE, the current price needs roughly:

| Target 10Y IRR | Required OE CAGR | Read |
|---:|---:|---|
| 8% | 21.2% | Very high for a company entering a capex-heavy cycle. |
| 10% | 23.4% | Requires strong AI monetization and capex conversion. |
| 12% | 25.7% | Requires an exceptional bull branch. |

Even with the growth-capex base of $82B and a 26x exit multiple, a 10% IRR requires about 18.6% owner-earnings CAGR. That can happen only if Search AI monetization, Cloud AI infrastructure, and infrastructure cost advantages all show up in common-share economics.

So the market is not merely implying "Google survives AI." It is implying that AI increases owner earnings per share at a rate high enough to overcome 2026-2027 capex, financing cost, SBC, and dilution.

---

## 4. Scenario Summary

Detailed annual outputs are in `companies/googl/model/scenario_model_v2.csv`.

| Scenario | Revenue growth | Owner earnings conversion | Capex intensity | SBC / dilution / repurchase | Exit assumption | 10Y IRR at $373.19 |
|---|---|---|---|---|---|---:|
| Bear / defensive capex | 5% for five years, then 3% | 10-12% normalized OE/revenue; much AI spend treated as defensive | Capex/OCF remains 80%+ through 2031 and 65% terminal | Full ATM-like dilution, preferred converts, no effective buyback offset; shares +0.5% CAGR | 16x P/OE | -11.9% |
| Base / mixed delay | 10% for five years, then 7% | OE grows 14% CAGR as conversion recovers into low-20s, but payback lags | 2026-2027 very high, then normalizes toward 45% OCF | Common + Berkshire + preferred dilution; later buybacks reduce shares 0.5% CAGR | 22x P/OE | 2.4% |
| Bull / growth capex | 14% for five years, then 10% | OE grows 19% CAGR; AI capex becomes high-return infrastructure | 2026-2027 peak, then normalizes toward high-30s OCF | Initial dilution absorbed; buybacks resume and shares fall 1.25% CAGR | 26x P/OE | 11.9% |

The base case is intentionally generous on operating quality. It still does not produce an attractive return from the current price because the starting P/OE is too high. The bull case works, but it requires the very evidence the research process still marks OPEN.

---

## 5. Financing / Dilution / Owner Earnings Impact

Hard financing facts from Q1 and June 2026:

| Item | Amount / shares | Owner earnings impact |
|---|---:|---|
| Q1 2026 senior notes issuance | $31.1B net proceeds | Adds interest burden; Q1 long-term debt rose to $77.5B. |
| 2026 capex guide | $180B-$190B | Midpoint exceeds TTM OCF of about $174B and is about 2.9x TTM FCF. |
| 2027 capex direction | Significantly higher than 2026 | Extends the period where FCF is not a clean owner earnings proxy. |
| Public common stock offering | 50.9M A/C shares | Immediate dilution if completed as described. |
| Berkshire private placement | 28.6M A/C shares, $10B gross | Validation signal, but still common dilution. |
| Mandatory convertible preferred | $16.75B gross principal | Estimated about $1.05B annual preferred dividend cost if both series price near the observed 6.25% rate; final series-by-series terms remain OPEN. Estimated 37.7M-47.2M future common shares. |
| ATM program | Up to $40B | About 107M shares at $373.19 if fully used; company says primary use is employee-equity tax mechanics, but buyback support is still weaker. |

Post-financing diluted share count estimate:

| Share count case | Shares | Increase vs Q1 |
|---|---:|---:|
| Q1 reported | 12.116B | 0.0% |
| Mid diluted, excluding ATM | 12.238B | 1.0% |
| Mid diluted, full ATM at anchor | 12.345B | 1.9% |

These percentages look small, but the direction matters. Alphabet's historical per-share story used buybacks to offset SBC and shrink share count. Q1 had zero Class A/C repurchases while capex and financing rose. That makes SBC, preferred dividends, and ATM mechanics real owner-earnings issues, not footnotes.

---

## 6. MOS Bands

These are process bands, not price targets.

| Zone | Price / condition | Action |
|---|---|---|
| Buy-below | $180-$220, plus evidence that AI RPM is not dilutive and capex/OCF has peaked | Base branch begins to offer roughly 8-10% 10Y IRR. This is where quality plus MOS can coexist. |
| Watch | $220-$300, or higher only after hard proof of capex conversion | Continue research. Quality is real, but the price still needs evidence upgrades. |
| Reject for new capital | Above $300 without proof of AI RPM, capex ROI, and FCF/share recovery | Current-like price is in this zone. The business is not rejected; the entry price is. |

Condition override: if Search & other falls to high-single-digit growth for two quarters while capex/OCF stays above 70%, this moves from `WATCH` to `REJECT / AVOID` regardless of price until the owner earnings bridge is rebuilt.

Upgrade condition: if Search AI monetization is shown to be equal/better than traditional Search, Cloud margin stays strong through depreciation headwinds, capex/OCF peaks, and share count resumes falling, the buy-below band can move upward. That requires hard evidence, not management optimism alone.

---

## 7. Evidence Grade

| Claim type | Grade | Read |
|---|---|---|
| Q1 revenue, Search, Cloud, OCF, capex, FCF, debt, shares | A1 | SEC-filed numbers. |
| 2026 capex $180B-$190B and 2027 significantly higher | A1 | June 2026 SEC offering documents. |
| Common offering, Berkshire placement, preferred, ATM structure | A1 | SEC offering documents. |
| Management comments on AI usage, compute constraint, Cloud backlog conversion | A2 | Official transcript, but still management commentary. |
| Owner earnings base ranges | B/C | Derived from local model; maintenance/growth capex split remains open. |
| Scenario IRRs and buy-below bands | C | Model outputs using explicit assumptions, not facts. |

---

## 8. Open Questions

Blocking:

- OPEN: AI Overviews / AI Mode RPM versus traditional Search RPM.
- OPEN: Maintenance versus growth capex split for AI infrastructure.
- OPEN: Cloud backlog margin and conversion economics, especially AI infrastructure and TPU-related sales.
- OPEN: Final preferred series terms, realized ATM issuance price, and whether buybacks resume enough to offset SBC/tax mechanics.
- OPEN: Numeric AI capex hurdle rate, utilization target, and payback period.

Monitoring:

- DOJ / EU remedy structure and effect on TAC/default distribution.
- Cloud margin durability as depreciation catches up.
- Share count trend after preferred conversion and ATM usage.
- FCF/share recovery after the 2026-2027 capex surge.

---

## 9. Sources

- Alphabet Q1 2026 Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm
- Alphabet Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet June 2026 FWP: https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm
- Alphabet June 2026 424B5: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm
- Alphabet Q1 2026 earnings call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Yahoo Finance GOOGL quote page: https://finance.yahoo.com/quote/GOOGL/
- Google Finance GOOGL quote page: https://www.google.com/finance/quote/GOOGL:NASDAQ
- Nasdaq GOOGL quote page: https://www.nasdaq.com/market-activity/stocks/googl
