# AMZN Source Register — as_of 2026-06-19

每来源: source_id · 名 · 公开/取数日期 · link/path · tier（A1/A2/B1/B2/C2/D1/E1，见 sources/source_policy.md）

| source_id | 来源 | 公开日期 | retrieved | tier | link/path |
|---|---|---|---|---|---|
| S001 | AMZN Q1 2026 8-K Exhibit 99.1 新闻稿（quarter ended 2026-03-31）| 2026-04-29 | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260331xex991.htm （本地 raw/_q1_2026_8k_ex991.html）|
| S002 | AMZN Q4/FY2025 8-K Exhibit 99.1 新闻稿（year ended 2025-12-31）| 2026-02-05 | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm （本地 raw/_fy2025_q4_8k_ex991.html）|
| S003 | AMZN 2025 Annual Report / FY25 10-K（year ended 2025-12-31）| 2026-02(approx) | 2026-06-19 | A1 | https://s2.q4cdn.com/299287126/files/doc_financials/2026/ar/Amazon-2025-Annual-Report.pdf （PDF 未逐行摘，载荷数走 S002 PR）|
| S004 | Yahoo chart API AMZN 日频价格序列 | 2026-06-18(最新close) | 2026-06-19 | B1(行情聚合) | https://query2.finance.yahoo.com/v8/finance/chart/AMZN （本地 raw 解析）|
| S005 | AMZN 官方 IR / aboutamazon Q1 2026 earnings report | 2026-04-29 | 2026-06-19 | A2 | https://www.aboutamazon.com/news/company-news/amazon-earnings-q1-2026-report |
| S006 | Q4'25 电话会(2026-02-05) + Q1'26 电话会(2026-04-29) 管理层口径（~$200B 2026 capex、AWS AI run-rate >$15B、backlog $364B）| 2026-02-05 / 2026-04-29 | 2026-06-19 | A2/B1 | CNBC/Investing.com/GeekWire 转述电话会发言（电话会原 transcript 未逐行重取，降权为 B1 转述）|
| S007 | 二手聚合 FY16–FY24 revenue/OI/AWS/FCF（10 年趋势）| 2026-06-19 | 2026-06-19 | B2 | stockanalysis / macrotrends（口径有差，降权，不作 buy 论点支撑）|
| S008 | AMZN DEF 14A proxy（治理/董事会/激励/Jassy 薪酬）— **本批未重取，用先验+一般公开立场** | — | — | OPEN | SEC EDGAR DEF 14A（待取）|

## Tier 纪律备注
- **载荷性当前事实（FY25 全年 + Q1 2026 锚定季度）全部回挂 A1**（S001/S002，SEC 8-K Ex99.1 原文本地落盘 raw/）。
- 价格走 S004（Yahoo chart，repo 既定来源，Stooq 已失效）；行情属 B1 聚合，已与 meta 52wk 字段一致性核对（高 $274.99 / 低 $198.79，相对 2026-06-19 trailing 52wk）。
- **S006 电话会口径（$200B 2026 capex、AWS AI run-rate >$15B、backlog $364B、$225B Trainium 承诺）**：$200B capex 与 backlog 量级有多家 B1 媒体转述同一电话会发言，但**未逐行回到官方 transcript 原文**，降权为 B1/A2 转述，标注待核；其中 backlog/Trainium 承诺细节仅作线索，不单独支撑 buy。
- S007 仅作 10 年趋势辅助；早期年份二手口径有差，降权，在 facts.md Contradictions 标注。
- S008 proxy 未重取 → operator 细节（Jassy 薪酬数字、董事独立性比例）标 OPEN，用 Jassy/Bezos 公开事实 + 一般立场，不杜撰具体数字。
- 无 D1 社媒进入 EVIDENCE。
