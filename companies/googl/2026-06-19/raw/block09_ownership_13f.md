# raw/block09 — Berkshire & H&H 13F (Alphabet holdings)

- **Sources (all A1, SEC EDGAR 13F information tables, VALUE = 整美元 "to nearest dollar"):**
  - Berkshire Q1 2026 (CIK 1067983): https://www.sec.gov/Archives/edgar/data/1067983/000119312526226661/xslForm13F_X02/53405.xml
  - H&H Q1 2026 (CIK 1759760): https://www.sec.gov/Archives/edgar/data/1759760/000175976026000005/xslForm13F_X02/infotable.xml
  - H&H Q4 2025: https://www.sec.gov/Archives/edgar/data/1759760/000175976026000001/xslForm13F_X02/infotable.xml
- **Retrieved:** 2026-06-16 · CUSIP: Class A 02079K305 / Class C 02079K107 · 完整入账见 `../claim_ledger.csv`。

## Berkshire Q1 2026（季末 2026-03-31 快照）
> CL C 02079K107 | 1,028,454,775 | 3,585,215 sh
> CL A 02079K305（4 个经理分行）| 16,700 + 6,700,000 + 6,250,000 + 41,283,098 = **54,249,798 sh** / **$15,600,071,913**
- **总计 A+C = 57,835,013 股 / $16,628,526,688**；implied ~$287/sh（与季末价一致）。

## H&H（机构申报主体）
- Q1 2026: CL C **3,706,000 股 / $1,063,103,160**（无 Class A）；implied $286.86/sh。
- Q4 2025: CL C **1,855,400 股 / $582,224,520**；implied $313.80/sh。
- **Δ = +1,850,600 股 = +99.74% ≈ 2.0×** → 验证"翻倍到约 3.7M 股"。

## ⚠ 口径警示
- 13F = 季末机构快照，季中操作不可见；**Berkshire 13F ≠ Buffett 个人决策**（多经理分管）；**H&H ≠ 段永平个人实时交易**。
- H&H 市值变化 +$480.9M 混合了加仓(+1.85M 股)与价格下跌(313.80→286.86)，**不可解读为净买入金额**。

## 入账 source_id：BRK-13F-2026Q1.* / HH-13F-2026Q1.* / HH-13F-2025Q4.* / HH-13F-DELTA.001
