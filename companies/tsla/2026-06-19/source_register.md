# TSLA Source Register — as_of 2026-06-19

每来源: source_id · 名 · 公开/取数日期 · link/path · tier（A1/A2/B1/B2/C2/D1/E1，见 sources/source_policy.md）

> **取数限制说明**: 本环境 WebFetch 对 SEC EDGAR (sec.gov) 与 Tesla IR (ir.tesla.com / assets-ir.tesla.com) 一律返回 **HTTP 403（反爬）**。故 Q1 2026 / FY2025 载荷数据通过：①官方口径经 **B1 有采编责任媒体**（CNBC/Electrek/Teslarati）一致转述；②**Tesla 官方 X 交付报告**（A2 官方一手发布）；③**stockanalysis.com**（B2 结构化聚合，回挂 10-Q/10-K 口径）。SEC 原文 URL 已登记，**逐行核标 OPEN**。多源交叉一致的数字（营收 $22.39B、净利 $477M、FCF $1.44B、交付 1,636,129）可作 EVIDENCE；未交叉的标降权。

| source_id | 来源 | 公开日期 | retrieved | tier | link/path |
|---|---|---|---|---|---|
| S001 | Tesla 10-Q Q1 2026（quarter ended 2026-03-31）| 2026-04(approx) | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/0001318605/000162828026026673/tsla-20260331.htm （403，**逐行 OPEN**）|
| S002 | Tesla Q1 2026 Update（official shareholder deck，8-K ex99.1）| 2026-04-22 | 2026-06-19 | A2 | https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q1-2026-Update.pdf （403，OPEN）|
| S003 | Tesla 10-K FY2025（year ended 2025-12-31）| 2026-01-28 | 2026-06-19 | A1 | SEC EDGAR CIK 1318605 10-K FY2025（403，**逐行 OPEN**）|
| S004 | Tesla 官方 Q4/FY2025 交付与生产报告（X/IR）| 2026-01-02 | 2026-06-19 | A2 | https://x.com/Tesla/status/2007089900613419092 （FY25 产 1,654,667 / 交 1,636,129 / 储能 46.7GWh；Q4 交 418,227）|
| S005 | CNBC "Tesla Q1 2026 earnings report" | 2026-04-22 | 2026-06-19 | B1 | https://www.cnbc.com/2026/04/22/tesla-tsla-q1-2026-earnings-report.html |
| S006 | Electrek "Tesla Q1 2026 financial results" | 2026-04-22 | 2026-06-19 | B1 | https://electrek.co/2026/04/22/tesla-tsla-q1-2026-financial-results/ |
| S007 | Yahoo chart API TSLA 日频价格序列 | 2026-06-18(最新close) | 2026-06-19 | B1(行情聚合) | https://query2.finance.yahoo.com/v8/finance/chart/TSLA （regularMarketTime 1781812801 = 2026-06-18；close $400.49）|
| S008 | stockanalysis.com TSLA 年度+季度财报 + 资产负债表 + 现金流 | 2026-06-19 | 2026-06-19 | B2 | https://stockanalysis.com/stocks/tsla/financials/ |
| S009 | TechCrunch "Tesla shareholders approve Musk's $1T pay package" | 2025-11-06 | 2026-06-19 | B1 | https://techcrunch.com/2025/11/06/tesla-shareholders-approve-elon-musks-1t-pay-package/ |
| S010 | Yahoo/Fortune Musk 2025 comp $158B + 423.7M 股 grant 细节 | 2025-11/2026 | 2026-06-19 | B1/B2 | https://fortune.com/2025/11/29/elon-musk-pay-package-details-tesla-stock-outlook/ |
| S011 | SEC PX14A6G / SBA 机构投资者对 Musk 薪酬异议 | 2025 | 2026-06-19 | A1(filing) | https://www.sec.gov/Archives/edgar/data/0001318605/000121465925014515/o102255px14a6g.htm （403，登记）|
| S012 | Seeking Alpha / Electrek robotaxi-FSD-Optimus 运营状态 | 2026-04 | 2026-06-19 | B1/C2 | robotaxi Austin/Dallas/Houston；FSD 1.3M 订阅；Optimus 产前 |
| S013 | DEF 14A proxy（董事会/薪酬/独立性）— **本批未直取** | — | — | OPEN | SEC EDGAR DEF 14A（403，待取）|

## Tier 纪律备注
- **载荷性当前事实交叉验证**: Q1 2026 营收 $22.387B / 净利 $477M / GAAP GM 21.1% / FCF $1.444B 在 S005/S006/S008 三源一致；FY2025 交付 1,636,129 / 储能 46.7GWh 在 S004（官方）+ 多 B1 一致 → 作 EVIDENCE。
- **SEC 10-Q/10-K 逐行未直取（403）** → 资产负债表细分、现金流逐行、分部利润、purchase commitments 标 **OPEN**，量级用 S008 (B2) 近似并降权。
- 价格走 S007（Yahoo chart，repo 既定来源，Stooq 已失效）；行情 B1 聚合，52wk high $498.83 / low $288.77。
- operator/薪酬走 S009/S010/S011（B1 + filing 登记）；**具体董事独立性比例、薪酬完整结构标 OPEN（proxy 未直取）**，不杜撰精确数字。
- robotaxi/Optimus/FSD 运营状态 S012 为 B1/C2 → **仅作"已 DELIVERED 与否"的定性证据，单位经济/规模化为 NARRATIVE，不进 EVIDENCE 支撑 buy**。
- 无 D1 社媒进入 EVIDENCE。
