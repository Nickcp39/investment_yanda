# GOOGL Accounting Trend Validation v2

Last updated: 2026-06-16

Module: Layer 4 - Accounting Trend Validation

Status: `P0_PASS_1_LAYER4_REBUILD`; this is not a buy/sell recommendation and does not make the overall Google v2 rerun complete.

Purpose: rebuild the accounting-to-economic-substance view for Alphabet using official SEC / Alphabet public filings where available. Anything not disclosed is marked `OPEN`; no point estimate is treated as filed fact unless it comes from an official filing or a directly derived formula.

Primary model files:

- `companies/googl/model/financial_history_10y_v2.csv`
- `companies/googl/model/capex_owner_earnings_bridge_v2.csv`

---

## 1. Evidence Map

Primary official sources used:

| Source | URL | Used for |
|---|---|---|
| SEC companyfacts, Alphabet CIK 1652044 | https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json | 10-year annual XBRL facts for revenue, operating income, net income, OCF, capex, SBC, buybacks, shares, cash/securities, debt. |
| FY2016 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204417000008/goog10-kq42016.htm | Historical annual filing and depreciation cash-flow line cross-check. |
| FY2017 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204418000007/goog10-kq42017.htm | Historical annual filing and depreciation cash-flow line cross-check. |
| FY2018 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204419000004/goog10-kq42018.htm | Historical annual filing and depreciation cash-flow line cross-check. |
| FY2019 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204420000008/goog10-k2019.htm | Historical annual filing and depreciation cash-flow line cross-check. |
| FY2020 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204421000010/goog-20201231.htm | Historical annual filing and depreciation cash-flow line cross-check. |
| FY2021 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204422000019/goog-20211231.htm | Historical annual filing; shares adjusted for 2022 split in later comparatives. |
| FY2022 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204423000016/goog-20221231.htm | Historical annual filing. |
| FY2023 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm | Historical annual filing. |
| FY2024 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm | Historical annual filing and 2023-2024 PPE/capex comparatives. |
| FY2025 10-K | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | FY2023-FY2025 statements, PPE note, SBC note, assets not yet in service. |
| Q1 2026 10-Q | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | Q1 2026 and TTM bridge, PPE note, Q1 equity securities gain. |
| Q1 2026 8-K Exhibit 99.1 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm | Q1 2026 release cross-check for OCF, capex, FCF, SBC, buybacks. |
| June 2026 424B5 | https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm | Forward capex guide: 2026 $180B-$190B and 2027 significantly higher. |

Notes:

- Values are USD millions unless stated otherwise.
- Free cash flow is derived as OCF minus purchases of property and equipment unless a release explicitly provides a non-GAAP FCF line. It is not a GAAP 10-K line.
- Share count is year-end common shares outstanding. FY2016-FY2020 are adjusted 20:1 for the 2022 split to make FCF/share comparable.
- For old years, depreciation of property and equipment was hand-parsed from annual 10-K cash-flow tables where the SEC companyfacts `Depreciation` tag did not cover the full 10-year span.

---

## 2. Ten-Year Trend Read

The 10-year record still shows an exceptional operating business, but the economic trend is no longer captured by revenue or operating income alone.

| Metric | FY2016 | FY2021 | FY2025 | TTM Q1 2026 | Read |
|---|---:|---:|---:|---:|---|
| Revenue | 90,272 | 257,637 | 402,836 | 422,498 | 2016-2025 CAGR 18.1%. |
| Operating income | 23,716 | 78,714 | 129,039 | 138,129 | 2016-2025 CAGR 20.7%; operating margin 26.3% to 32.0%. |
| OCF | 36,036 | 91,652 | 164,713 | 174,353 | 2016-2025 CAGR 18.4%. |
| Capex | 10,212 | 24,640 | 91,447 | 109,924 | 2016-2025 CAGR 27.6%; capex is compounding much faster than OCF. |
| FCF | 25,824 | 67,012 | 73,266 | 64,429 | FCF grew over 10 years, but has flattened since 2021 and declined on TTM. |
| Capex / OCF | 28.3% | 26.9% | 55.5% | 63.1% | Capital intensity has stepped up. |
| FCF / OCF | 71.7% | 73.1% | 44.5% | 37.0% | Cash conversion is compressing. |
| FCF/share | $1.87 | $5.06 | $6.06 | $5.32 | Buybacks helped the decade; recent FCF/share is under pressure. |
| SBC note total | 6,900 | 15,700 | 27,100 | OPEN | Persistent and material owner cost. |
| Buybacks | 3,693 | 50,274 | 45,709 | 30,641 | Q1 2026 buybacks were zero, so dilution protection is weaker. |
| Debt | 3,935 | 15,440 | 46,547 | 77,501 | Debt has moved from immaterial to visible funding support. |
| Cash + marketable securities | 86,333 | 139,649 | 126,843 | 126,840 | Liquidity remains large, but capex scale now absorbs it faster. |

Ten-year cumulative view:

- Cumulative OCF: $815.6B.
- Cumulative capex: $326.7B.
- Cumulative derived FCF: $488.9B.
- Cumulative SBC note total: $157.1B.
- Cumulative buybacks: $346.2B.
- Year-end shares fell about 12.6% from split-adjusted FY2016 to FY2025, but rose from FY2025 to Q1 2026 after buybacks paused.

Accounting conclusion: the income statement is still strong; the owner-economics question has shifted to capital intensity. The business can grow revenue and operating income while FCF/share stalls if AI/data-center capex becomes defensive or structurally recurring.

---

## 3. FCF Conversion And Capex Bridge

The key accounting-to-economic bridge is visible in four lines:

| Period | OCF | Capex | FCF | Capex / OCF | FCF / OCF | PPE depreciation | Assets not yet in service / CIP |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2023 | 101,746 | 32,251 | 69,495 | 31.7% | 68.3% | 11,946 | 35,136 |
| FY2024 | 125,299 | 52,535 | 72,764 | 41.9% | 58.1% | 15,311 | 50,597 |
| FY2025 | 164,713 | 91,447 | 73,266 | 55.5% | 44.5% | 21,136 | 78,592 |
| TTM Q1 2026 | 174,353 | 109,924 | 64,429 | 63.1% | 37.0% | 23,131 | 108,597 |

Observed:

- Capex rose from $32.3B in FY2023 to $91.4B in FY2025 and $109.9B TTM.
- PPE depreciation rose from $11.9B in FY2023 to $21.1B in FY2025 and $23.1B TTM.
- Assets not yet in service / construction in progress rose from $35.1B in FY2023 to $78.6B in FY2025 and $108.6B at Q1 2026.
- Q1 2026 capex alone was $35.7B versus Q1 2026 OCF of $45.8B, so quarter-level capex/OCF was about 77.9%.
- The June 2026 424B5 states 2026 capex is expected at $180B-$190B and 2027 capex is expected to significantly increase versus 2026.

Economic implication:

- Depreciation is a useful observable floor for replacement burden, but it is not proof of maintenance capex.
- Assets not yet in service are not yet producing full revenue and will create future depreciation once placed into service.
- Current filings do not disclose maintenance capex versus growth capex. That split remains `OPEN`.

---

## 4. Net Income Quality

Reported net income is not the cleanest owner-earnings anchor for the current period.

- FY2025 net income was $132.2B, but FY2025 other income net was $29.8B. That line can be economically real, but it is not the same as recurring operating earning power.
- Q1 2026 net income included a $36.9B gain on equity securities, mostly unrealized. TTM net income of $160.2B therefore overstates recurring operating economics.
- For owner earnings, this module starts with operating income after a 21% normalized tax assumption. That is a underwriting convention, not a disclosed normalized tax rate. It intentionally excludes nonoperating investment gains.

This is an accounting-quality caution, not an allegation of aggressive revenue recognition. The main issue is capital allocation and future depreciation, not evidence of fabricated revenue.

---

## 5. Owner Earnings Branches

Formula used in the bridge:

`owner earnings = operating income * (1 - 21%) + PPE depreciation - SBC economic cost - maintenance capex`

Rationale:

- Operating income is used to avoid one-time/nonoperating gains.
- PPE depreciation is added back, then maintenance capex is subtracted.
- SBC is treated as a real owner cost.
- FY2025 SBC uses the Note total of $27.1B. TTM Q1 2026 uses cash-flow add-back of $26.2B because TTM note-total SBC is not disclosed; therefore TTM SBC is an observable lower-bound and remains `OPEN` for exact economic SBC.

| Period | Branch | Maintenance capex assumption | Owner earnings | Owner earnings/share | What must be true |
|---|---|---:|---:|---:|---|
| FY2025 | Growth | Maintenance = PPE depreciation = 21,136 | 74,841 | $6.19 | AI/Search/Cloud capex is mostly incremental growth; capex/OCF peaks; Cloud/AI revenue and margins prove incremental returns. |
| FY2025 | Mixed | Maintenance = 35% of capex = 32,006 | 63,970 | $5.29 | Some capex defends the base, some earns growth; FCF/share resumes growth while depreciation is absorbed. |
| FY2025 | Defensive | Maintenance = 50% of capex = 45,724 | 50,253 | $4.16 | Large AI capex share is required to preserve current Search/Cloud economics; FCF/share stays flat/down. |
| TTM Q1 2026 | Growth | Maintenance = PPE depreciation = 23,131 | 82,934 | $6.84 | Same as growth branch, with Q1 2026 capex intensity assumed temporary or pre-revenue. |
| TTM Q1 2026 | Mixed | Maintenance = 35% of capex = 38,473 | 67,592 | $5.58 | Same as mixed branch; capex productivity must become visible before 2026-2027 guide is spent. |
| TTM Q1 2026 | Defensive | Maintenance = 50% of capex = 54,962 | 51,103 | $4.22 | Same as defensive branch; current AI capex is partly a tax to keep the moat. |

No branch is a valuation or trading recommendation. The branches only frame accounting-to-economic underwriting.

---

## 6. What Is Observable Versus OPEN

Observable from official filings:

- 10-year revenue, operating income, net income, OCF, PPE purchases, buybacks, share count, cash + marketable securities, and debt.
- 10-year SBC with two relevant views: cash-flow add-back and Note/allocated SBC.
- PPE depreciation for FY2016-FY2025, with older years hand-parsed from the annual cash-flow statements.
- FY2023-FY2025 and Q1 2026 assets not yet in service / construction in progress trend.
- Q1 2026 buyback pause, share count increase, debt increase, and capex/OCF spike.
- 2026 and 2027 forward capex direction from 424B5.

OPEN / not disclosed:

- Maintenance capex versus growth capex. The company does not disclose this split.
- AI Search / AI Overview / AI Mode RPM versus traditional Search RPM.
- Unit economics of each incremental dollar of AI/data-center capex.
- Cloud backlog conversion timing and realized margin after depreciation.
- TTM Q1 2026 Note-total SBC, as distinct from cash-flow SBC add-back.
- Full comparable assets-not-yet-in-service history for FY2016-FY2022 under the newer label.
- Management's numeric hurdle rate or payback framework for AI capex.

---

## 7. Layer 4 Verdict

Layer 4 has enough evidence to replace the old 3-year view with a 10-year accounting trend and an explicit owner-earnings branch model.

The underwriting center is now:

1. Alphabet's operating engine remains strong: revenue, operating income, and OCF compounded at high rates from FY2016 to FY2025.
2. The recent economic pressure is real: capex/OCF rose to 55.5% in FY2025 and 63.1% on TTM Q1 2026, while FCF/OCF fell to 44.5% and 37.0%.
3. PPE depreciation and assets not yet in service are both rising quickly, so future reported margins and owner earnings will depend on utilization and revenue conversion.
4. Owner earnings should be carried as a range, not a point: FY2025 roughly $50B-$75B under the branch set; TTM Q1 2026 roughly $51B-$83B before exact TTM note-total SBC.
5. The largest blocker is still the unobservable maintenance/growth capex split. Until that is proven with unit economics or management disclosure, the defensive and mixed branches cannot be dismissed.

Status remains within the broader company checker: `P0_PASS_1`; the full Google v2 rerun is still incomplete because other layers, source register, claim ledger, facts promotion, valuation refresh, and final audit gates remain open.
