# NVDA Source Register — as_of 2026-06-20

每来源: source_id · 名 · 公开/取数日期 · link/path · tier（A1/A2/B1/B2/C2/D1/E1，见 sources/source_policy.md）
> **CORRECTED** vs `../2026-06-19/`：S006 价格重取并加 ≥2 独立源交叉验证（v1.1 freshness 门）；新增 China H200 出口管制 LIVE 源 S010/S011。

| source_id | 来源 | 公开日期 | retrieved | tier | decay | link/path |
|---|---|---|---|---|---|---|
| S001 | NVDA Q1 FY27 8-K 新闻稿（PR）| 2026-05-20 | 2026-06-19 | A1 | FILED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm （本地 raw/_q1fy27pr.html）|
| S002 | NVDA Q1 FY27 CFO Commentary | 2026-05-20 | 2026-06-19 | A2 | FILED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm （本地 raw/_q1fy27cfo.html）|
| S003 | NVDA FY26 10-K（year ended 2026-01-25）| 2026-02-01 | 2026-06-19 | A1 | FILED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm |
| S004 | NVDA Q4/FY26 8-K 新闻稿（full-year FY26）| 2026-02-01 | 2026-06-19 | A1 | FILED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm |
| S006 | Yahoo chart API NVDA 日频价格序列（last close ≤ as_of = 2026-06-18 $210.69）| 2026-06-18 | 2026-06-20 | B1 | **LIVE** | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| S008 | stockanalysis.com NVDA 行情页（价格/市值二次源；$210.69 / mcap ~$5.10T）| 2026-06-18 | 2026-06-20 | B1 | **LIVE** | https://stockanalysis.com/stocks/nvda/ |
| S007 | stockanalysis.com NVDA 年度财务（FY22–FY26 口径，趋势用）| 2026-06-19 | 2026-06-19 | B2 | FILED | https://stockanalysis.com/stocks/nvda/financials/ |
| S010 | USG 重发对华 H200 出口许可（限特定客户）| 2026-02-15 | 2026-06-20 | B1 | **LIVE** | Reuters/news（websearch 核，retrieved 2026-06-20）|
| S011 | NVDA 已收中国 H200 订单 / 重启生产（黄仁勋 GTC）| 2026-03-18 | 2026-06-20 | A2 | **LIVE** | NVIDIA GTC 2026 Huang remarks |
| S009 | NVDA DEF 14A proxy（治理/董事会/激励）— 本批未重取 | — | — | OPEN | FILED | SEC EDGAR DEF 14A（待取）|

## Tier × Decay 纪律备注（v1.1 新增 decay 轴）
- **tier 与 decay 正交**：S002（China，A2 一手）却是 **LIVE**——一手来源**不等于**免刷新。LIVE 源（S006/S008/S010/S011）每跑必须 ≥2 独立源交叉验证并过 `verify_freshness.py`；FILED 源（10-K/10-Q 行项）锚定带日期文件即可。
- 价格走 S006（Yahoo），并由 S008（stockanalysis）+ websearch 做 ≥2 源交叉验证（均 $210.69）。错版 2026-06-19 仅信 S006 单源 + 只验日期 → 漏掉 $145.48（≈52周低 $142.03）。
- China 出口管制（S010/S011）为 **LIVE-qualitative**：H200 许可重启是当前最新权威事件（2026-02/03），freshness 门 T6 给 WARN（94 天 > 45 天窗口）提示确认，非阻断。
- S007 仅作 10 年趋势辅助；早期年份 fiscal-year 标注 off-by-one 冲突已降权（见 facts.md Contradictions）。
- S009 proxy 未重取 → operator 细节标 OPEN，不杜撰具体数字。无 D1 社媒进入 EVIDENCE。
