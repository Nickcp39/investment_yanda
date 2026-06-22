# NVDA Source Register — as_of 2026-06-19

每来源: source_id · 名 · 公开/取数日期 · link/path · tier（A1/A2/B1/B2/C2/D1/E1，见 sources/source_policy.md）

| source_id | 来源 | 公开日期 | retrieved | tier | link/path |
|---|---|---|---|---|---|
| S001 | NVDA Q1 FY27 8-K 新闻稿（PR）| 2026-05-20 | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm （本地 raw/_q1fy27pr.html）|
| S002 | NVDA Q1 FY27 CFO Commentary | 2026-05-20 | 2026-06-19 | A2 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm （本地 raw/_q1fy27cfo.html）|
| S003 | NVDA FY26 10-K（year ended 2026-01-25）| 2026-02(approx) | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm |
| S004 | NVDA Q4/FY26 8-K 新闻稿（full-year FY26）| 2026-02(approx) | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm |
| S005 | NVDA 官方 newsroom Q1 FY27 公告 | 2026-05-20 | 2026-06-19 | A2 | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 |
| S006 | Yahoo chart API NVDA 日频价格序列 | 2026-06-18(最新close) | 2026-06-19 | B1(行情聚合) | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| S007 | stockanalysis.com NVDA 年度财务（FY22–FY26 口径）| 2026-06-19 | 2026-06-19 | B2 | https://stockanalysis.com/stocks/nvda/financials/ |
| S008 | 二手聚合 FY17–FY21 revenue/净利（早期序列）| 2026-06-19 | 2026-06-19 | B2 | companiesmarketcap / fool（口径有冲突，降权）|
| S009 | NVDA DEF 14A proxy（治理/董事会/激励）— **本批未重取，用先验+一般公开立场** | — | — | OPEN | SEC EDGAR DEF 14A（待取）|

## Tier 纪律备注
- **载荷性当前事实（FY26 全年 + Q1 FY27 锚定季度）全部回挂 A1/A2**（S001–S004）。
- 价格走 S006（Yahoo chart，repo 既定来源，Stooq 已失效）；行情属 B1 聚合，已与多源一致性核对（52wk high $236.54 / low $142.03）。
- S007/S008 仅作 10 年趋势的辅助；**早期年份 fiscal-year 标注在不同二手源间存在 off-by-one 冲突**，已降权并在 facts.md Contradictions 标注，不作 buy 论点支撑。
- S009 proxy 未重取 → operator 细节（薪酬数字、董事独立性比例）标 OPEN，用 Huang 创始人事实 + 公开一般立场，不杜撰具体数字。
- 无 D1 社媒进入 EVIDENCE。
