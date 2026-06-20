# AAPL Source Register — as_of 2026-06-19

每来源: ID + 名 + 公开/取数日期 + link/path + tier。载荷性 claim 全部回挂这里。

| ID | 来源 | 公开日期 | retrieved | tier | link/path |
|---|---|---|---|---|---|
| S001 | Apple Q2 FY26 8-K EX-99.1 财报 PR (季度 ended 2026-03-28) | 2026-04-30 | 2026-06-20 | A1 | https://www.sec.gov/Archives/edgar/data/320193/000032019326000011/a8-kex991q2202603282026.htm |
| S002 | Apple Q4/FY25 8-K EX-99.1 财报 PR (FY ended 2025-09-27, 含 FY24 比较列) | 2025-10-30 | 2026-06-20 | A1 | https://www.sec.gov/Archives/edgar/data/320193/000032019325000077/a8-kex991q4202509272025.htm |
| S003 | Apple FY25 10-K (ended 2025-09-27) | 2025-10-31 | 2026-06-20 | A1 | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm |
| S004 | Apple Q2 FY26 10-Q (ended 2026-03-28) | 2026-05-01 | 2026-06-20 | A1 | https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm |
| S005 | Yahoo chart API AAPL (价格/52周高低/市值基础) | 2026-06-18 close | 2026-06-20 | A2(交易所行情) | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| S006 | Apple Newsroom — WWDC 2026: 下一代 Apple Intelligence + Siri AI | 2026-06-08 | 2026-06-20 | A1(公司公告) | https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/ |
| S007 | FY22–FY24 历史年度数（rev/NI/FCF/GM/Services）— 二手汇总 | 各财年 | 2026-06-20 | B2 | WebSearch 汇总 (stock-analysis-on.net / bullfincher / 媒体)；FY24 已被 S002 比较列 A1 坐实 |
| S008 | Google 反垄断救济最终令（默认协议禁令 / 选择屏，2026-06 生效）— 媒体报道 | 2026-04~06 | 2026-06-20 | B1 | DOJ / MacRumors / Brookings 报道（TAC 风险线索；裁决文本为 A 级，此处为二手）|
| S009 | AAPL 2016-05-12 历史盲测案（thesis 先验，事实不当当前） | 2016-05-12 as_of | 2026-06-20 | 内部 | backtests/framework_validation/cases/aapl_2016-05-12/ |

## 取数说明
- 价格: Yahoo chart API（repo 既定，Stooq 已失效）。2026-06-18 收盘 $298.01（≤ as_of 的最后交易日；2026-06-19 当日不入冻结边沿）。52周高 $317.40 / 低 $198.96。
- 全部载荷性财务数（季度 + 全年 + 资产负债表 + 现金流）来自 S001/S002 SEC EX-99.1 原文表格。
- FY22/FY23 早期年份为 B2 二手，明确降权、仅用于 10 年趋势方向，不进 verdict 关键勾稽。
- KOL/社媒未使用。WWDC/反垄断为公司公告(A1)/媒体(B1)，进 EVIDENCE(公司公告) / OPEN(裁决量级)。
