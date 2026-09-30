# Raw Block 13 — EDGAR / Market Incremental (2026-07-28 → 2026-08-28)

> raw 阶段纪律：本文件只记录来源、日期、tier、原文摘录/接近原文转述、候选 claim。
> 不下结论、不写"所以"、不写"我觉得"。分析见 ../valuation.md 与 ../decision_card.md。

检索人：Kimi（pipeline run as_of 2026-08-28）· 检索日：2026-08-28

---

## R1. Alphabet 8-K（2026-08-10，SEC，tier A1）

- URL: https://www.sec.gov/Archives/edgar/data/1652044/000119312526342390/d171253d8k.htm
- accession: 0001193125-26-342390 · filed 2026-08-10 · Item 8.01 Other Events
- 原文摘录（Item 8.01）：
  > "On August 10, 2026, Alphabet Inc. closed its underwritten public offering of
  > $25 billion aggregate principal amount of U.S. dollar-denominated senior notes
  > ... pursuant to an Indenture ... dated as of February 12, 2016"
- 各档明细（原文数字）：$750M 浮息 2028 · $1,250M 4.500% 2028 · $500M 浮息 2029 ·
  $2,000M 4.625% 2029 · $3,500M 4.875% 2031 · $2,500M 5.200% 2033 ·
  $4,500M 5.450% 2036 · $3,000M 6.250% 2046 · $4,500M 6.375% 2056 ·
  $2,500M 6.500% 2066（合计 $25.0B，10 档，2028–2066）
- 同文件 XBRL 头显示：6.25% Series A / Series B Mandatory Convertible Preferred
  的存托股份（1/20 权益）于 NASDAQ 挂牌（对应 8/6 两份 424B5 与 8/7 424B2/FWP）。
- 候选 claim：C-01（发债 $25B 细节）、C-02（优先股存托股挂牌）

## R2. Berkshire Hathaway 13F-HR（filed 2026-08-14，as of 2026-06-30，SEC，tier A1）

- URL: https://www.sec.gov/Archives/edgar/data/1067983/000119312526352200/56757.xml
- accession: 0001193125-26-352200 · 组合 89 条持仓，总市值 $299,253,556,246（千美元口径 $299.25B）
- Alphabet 条目（5 条，多管理人/类别）：
  - 27,188,433 股 / $9,606,489,032
  - 16,700 股 / $5,968,079
  - 6,700,000 股 / $2,394,379,000
  - 6,250,000 股 / $2,233,562,500
  - 65,824,467 股 / $23,523,689,772
- 合计：105,979,600 股 / $37,763,988,383（≈ 组合 12.6%）
- 对照 Q1 13F-HR（filed 2026-05-15，as of 2026-03-31，accession 0001193125-26-226661，
  https://www.sec.gov/Archives/edgar/data/1067983/000119312526226661/53405.xml）：
  Alphabet 合计 57,835,013 股 / $16,628,526,688
- 推导（标注为 derived）：Q2 内股数 +48,144,587（+83.2%）
- 候选 claim：C-03（伯克希尔 Q2 加仓）、C-04（组合占比）

## R3. GOOGL 价格（2026-08-27 收盘，双源）

- Yahoo chart API（v8, range=5d）：2026-08-27 close = $340.65；
  meta.regularMarketPrice = 340.65 USD。近 5 日：8/21 344.82 / 8/24 348.06 /
  8/25 346.96 / 8/26 342.00 / 8/27 340.65。
- Nasdaq API（api.nasdaq.com/api/quote/GOOGL/info）：lastSalePrice $340.65，
  netChange −1.35（−0.39%），lastTradeTimestamp "Aug 27, 2026"，volume 23,391,551。
- 双源 delta = 0.0%。
- Yahoo 1y 区间（close 口径）：52wk high $402.62 / 52wk low $211.35。
- 候选 claim：C-05（as_of 价格）、C-06（52wk 区间）

## R4. 媒体佐证（tier B2 / C，不进 EVIDENCE）

- Motley Fool（2026-08-27，tier B2）
  https://www.fool.com/investing/2026/08/27/alphabet-is-paying-a-dividend-while-selling-usd85-billion-of-new-stock/
  摘录："in August, Alphabet sold another $25 billion of notes. The mandatory
  convertible preferred stock Alphabet sold in June pays 6.25% a year, about
  $1.2 billion..."（"another" 与 "in June" 为原文口径）
- AOL.ca（2026-08-26，tier C）
  https://www.aol.ca/articles/big-tech-borrowing-way-ai-100000000.html
  摘录："Alphabet's latest sale could add as much as $25 billion more. If it
  reaches $25 billion, Alphabet will have issued nearly $77 billion of debt this year."
- thoughtcanvas IT weekly（2026-08-01，tier C）：Q2 同业表——AMZN FY26 capex 指引
  $220B、MSFT FY27 capex 预计 $175B（服务器折旧年限延至 25 年）、META FY26 capex
  $130–145B 且 FCF 单季 $784M；Alphabet Q2 收入 $119.8B(+24%)、op margin 34%、
  指引 $195–205B——与 7/28 dossier 的 Q2 数据一致（交叉验证用）。
- 候选 claim：C-07（优先股股息成本 ~$1.2B/年，B2）、C-08（年内发债 ~$77B，C 级，仅 OPEN/佐证）

## R5. EDGAR 申报流水（2026-07-01 → 2026-08-27，tier A1 索引）

- 10-Q（Q2-2026）filed 2026-07-23（accession 0001652044-26-000071）——已并入 7/28 dossier。
- 8-K 2026-07-22（Q2 财报）——已并入 7/28 dossier。
- 7/28 之后无新的 10-Q/10-K/财报 8-K；下一份季度数据预计 Q3 财报（~10 月下旬）。
- 8/7 13F-HR（CIK 1652044 自家申报，Alphabet 投资组合持仓，housekeeping）。
- Form 4 多笔（7/6–8/27，含 8/27 七笔）：例行内部人交易，本轮未逐条展开（非 blocking）。
- 候选 claim：C-09（7/28 后无新财报，数据真空期至 Q3）

## R6. 监管事件检索（WebSearch，2026-07-28 之后，tier 检索记录）

- 查询："Alphabet Google DOJ adtech remedy ruling August 2026"（after 2026-07-28）——
  未检到 adtech 救济裁决落地的新闻；命中均为旧文（2025 年程序节点）。
- 候选 claim：C-10（DOJ adtech 救济裁决在本窗口未落地 → OPEN，非事实断言"没有裁决"，
  仅"本次检索未发现"）
