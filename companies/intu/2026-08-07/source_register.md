# INTU Source Register

Last updated: 2026-08-07 (run_date) | as_of: 2026-08-06 | pipeline: lean-6module-v1.1
Tier rules: `../../../sources/source_policy.md`

**CIK: 0000896878**

## A 级（一手，SEC / IR 原文，本轮直接抓取全文）

| source_id | Tier | 来源 | 公开日期 | URL / 本地路径 | 承载什么 |
|---|---|---|---|---|---|
| **S-10K-FY25** | **A1** | Intuit FY2025 Form 10-K（财年结束 2025-07-31） | 2025-09-03 | https://www.sec.gov/Archives/edgar/data/896878/000089687825000035/intu-20250731.htm · 摘录 `raw/SEC_10K_FY2025_extract.txt` | FY23–FY25 全公司与四分部收入/营业利润、Online Ecosystem 拆分、**ARPC +14% / 付费客户 +5%**、Mailchimp 仅 +$20M、员工 **约 18,200 人**、现金流表、股息、**公共部门竞争风险因子原文**、股数 278,805 千股（2025-08-26） |
| **S-10Q-Q3** | **A1** | Intuit FY2026 Q3 Form 10-Q（季度结束 2026-04-30） | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/896878/000089687826000025/intu-20260430.htm · 摘录 `raw/SEC_10Q_FY26Q3_segment_extract.txt` | 分部与产品线收入表（QBO Accounting / Online Services / Desktop / TurboTax / Credit Karma / ProTax）、**Online Services 增量桥（Mailchimp 反推的依据）**、分部营业利润率、资产负债表、**股数 273,537 千股（2026-05-14）**、递延所得税 |
| **S-8K-Q3** | **A1** | Intuit FY2026 Q3 财报 8-K Ex-99.01 | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000024/fy26q3earningspressrelease.htm · 全文 `raw/SEC_8K_FY26Q3_earnings_press_release_2026-05-20.txt` | Q3 数字、**FY2026 修订指引全套**、**TurboTax 单量/e-file 份额/ARPU/Live/pay-nothing 指标**、**17% 裁员 + $300–340M**、回购 $1.6B + $8B 新授权、现金 $6.8B / 债务 $6.2B、逐季 GAAP↔non-GAAP 对账表（FY25 与 FY26） |
| **S-8K-Q2** | **A1** | Intuit FY2026 Q2 财报 8-K Ex-99.01 | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/896878/000089687826000012/fy26q2earningspressrelease.htm · 本地 `scratchpad/q2pr.txt` | Q2 数字、**FY2026 指引重申（原始版本）**、ex-Mailchimp 增速差、**"Mailchimp to return to double-digit growth some time beyond fiscal 2026"**、$5.8B 临时循环额度 |
| **S-8K-0316** | **A1** | Intuit 8-K Item 7.01（Reg FD） | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/896878/000089687826000017/intu-20260316.htm · 全文 `raw/SEC_8K_2026-03-16_insider_10b5-1_termination.txt` | **创始人与全体 ELT 终止全部 10b5-1 减持计划**；加速回购；上半财年回购 $1.8B（+40%） |
| **S-IR-FY25Q4** | **A1** | Intuit FY2025 Q4/全年财报新闻稿（IR） | 2025-08-21 | https://investors.intuit.com/news-events/press-releases/detail/1266/... | FY2025 实际数、**FY2026 初始指引（回撤归因的峰值锚）**、**TurboTax 单量 39.2M / 34.9M / 4.3M** |
| **S-IR-Q3REL** | **A1** | Intuit Q3 FY2026 IR 新闻稿页 | 2026-05-20 | https://investors.intuit.com/news-events/press-releases/detail/1312/... | 与 S-8K-Q3 同内容（交叉确认） |
| **S-IR-CAL** | **A1** | Intuit "Q4/FY2026 结果将于 8 月 25 日公布；Investor Day 9 月 17 日" | 2026-07-30 | https://investors.intuit.com/news-events/press-releases/detail/1318/... | **确认 FY2026 全年在 as_of 时点尚未公布**（O1 的依据） |
| **S-EDGAR-8K** | A1 | SEC EDGAR 8-K 申报列表（CIK 0000896878） | — | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000896878&type=8-K | 事件时间线的申报日期（含 2026-06-11 发债、2026-04-28 高管变动） |

## B 级（价格/市场数据，双源交叉）

| source_id | Tier | 来源 | 日期 | URL | 承载什么 |
|---|---|---|---|---|---|
| **S-YHOO** | B1 | Yahoo Finance chart API（INTU 日线，含股息/拆分事件） | 2026-08-07 抓取 | https://query1.finance.yahoo.com/v8/finance/chart/INTU | **$321.91（2026-08-06 结算收盘）**、峰值 $807.39（2025-07-30，复权 $798.42）、52 周高 $762.48 / 低 $252.84、周期低点收盘 $255.07（2026-06-25）、**全部单日涨跌幅事件时间线**、股息序列 |
| **S-SA-HIST** | B1 | stockanalysis.com INTU 历史价格页 | 2026-08-07 | https://stockanalysis.com/stocks/intu/history/ | **独立确认 2026-08-06 收盘 = $321.91（delta 0.00%）** |
| **S-SA** | B1 | stockanalysis.com INTU 主页 | 2026-08-07 | https://stockanalysis.com/stocks/intu/ | 股数 273.54M、52 周区间、TTM EPS $16.35 / 收入 $20.93B（与自算 $16.39 / $20.925B 互证）、市值 |
| **S-PEERS** | B1 | Yahoo chart API（ADBE / CRM / NOW / WDAY / HRB / MSFT / ^NDX） | 2026-08-07 | https://query1.finance.yahoo.com/v8/finance/chart/{ticker} | **同窗口横向对照（本轮自算）**：INTU −60.1% / NOW −40.0% / CRM −29.5% / ADBE −28.5% / WDAY −28.4% / **HRB −16.1%** / MSFT −2.6% / **NDX +25.8%** |

## B 级（叙事与政策，**未经一手核实的部分已在正文标注**）

| source_id | Tier | 来源 | 日期 | URL | 承载什么 |
|---|---|---|---|---|---|
| **S-FNN-DF** | B1 | Federal News Network："IRS tells states Direct File 'will not be available' in 2026" | 2025-11-05 | https://federalnewsnetwork.com/it-modernization/2025/11/irs-direct-file-will-not-be-available-in-2026-agency-tells-states/ | **Direct File 2026 报税季取消**（转述 2025-11-03 IRS 致州函）；296,531 份使用量 |
| **S-TAXNOTES-DF** | B1 | Tax Notes："IRS Shutters Direct File, Citing Cost and Low Uptake" | 2025-11-05 | https://www.taxnotes.com/featured-news/irs-shutters-direct-file-citing-cost-and-low-uptake/2025/11/05/7t7q0 | Treasury 理由；$41M / ≥$138 每份；OBBBA §70607 |
| **S-GS-DG** | B2 | Goldman Sachs（Gabriela Borges）下调至 Sell 的媒体转述 | 2026-06-02 | https://finance.yahoo.com/markets/stocks/articles/goldman-sachs-downgrades-intuit-intu-190239482.html | PT $519→$276；**AI 处理个税 $0.12 vs TurboTax $162**；TurboTax 约占收入与营业利润 25%；**Mailchimp 约占收入 7%**；2030 年 TurboTax 收入较 FY2025 低约 18% 的 base case |
| **S-FORBES-WORST** | B2 | Forbes："Intuit Becomes S&P 500's Worst Performer This Year" | 2026-06-02 | https://www.forbes.com/sites/tylerroush/2026/06/02/intuit-becomes-sp-500s-worst-performer-this-year-heres-why/ | 选题前提的独立佐证 |
| **S-TREFIS-FEB** | B2 | Trefis："Why Intuit Stock Crashed −30%" | 2026-02-04 | https://www.trefis.com/stock/intu/articles2/589573/why-intuit-stock-crashed-30/2026-02-04 | **2025-11-05→2026-02-03 跌 34%，其中 P/E 压缩约 −38%，收入与净利率各 +3%**（独立的倍数/基数分解，与本轮自算互证） |
| **S-FOOL-Q3CALL** | **B1** | Motley Fool：Intuit Q3 FY2026 电话会转录 | 2026-05-20 | https://www.fool.com/earnings/call-transcripts/2026/05/20/intuit-intu-q3-2026-earnings-transcript/ | **全部管理层引语**：*"We lost on price"*、*"we did not have the overall tax season we expected"*、*"None of this has anything to do with AI"*、IRS 报税人 −30bp/约 200 万单、QBO Advanced + IES **+38%**、Mailchimp"rightsizing"、CFO"mid-teens EPS growth"、5,000 万笔/周 AI agent 交易、consumption-based 定价 |
| **S-PRN-CLASS** | B2 | PR Newswire：Intuit 证券欺诈调查/集体诉讼公关稿 | 2026-06-02 / 2026-07-21 | https://www.prnewswire.com/news-releases/intu-stock-drop-intuit-investigated-for-securities-fraud-after-stock-plummets-20-on-pricing-issues-302787918.html | −20% 当日价格（$383.93 → $307.07）；**TurboTax FY2026 收入指引美元区间 $5.305–5.330B → $5.277–5.282B**（O7，仅此一源） |

---

## Fetch notes（2026-08-07）

- **SEC EDGAR 直取成功**：WebFetch 对 sec.gov 返回 403，但用 Python + 合规 User-Agent（`yc-research nickcp39@gmail.com`）直接抓取 `.htm` 全文成功。FY2025 10-K（2.76MB）、FY26 Q3 10-Q、三份 8-K 全部拿到原文并转纯文本存入 `raw/`。**本 dossier 的全部财务数字来自这些原文，不是聚合站。**
- **IR 站 script PDF 失败**：`investors.intuit.com/_assets/.../Q3FY26+Earnings+Script.pdf` 返回 **403**。这是 **O6** 的成因——管理层引语目前只有 Motley Fool（B1）转录支撑，**未与官方 script 逐字对上**。所有引语在正文中均已标注 B1。
- **价格双源**：$321.91（2026-08-06 结算收盘）经 Yahoo chart API 与 stockanalysis.com history 两个完全独立来源确认，**delta 0.00%**；`verify_freshness.py` 独立重抓亦得 321.9100 → **status PASS（exit 0）**。
- **2026-08-07 盘中价（~$328.2–328.6）刻意未采用**：run_date 当日未结算。房规为"settled close ≤ today"，与 `companies/googl/2026-07-24` 同纪律。任务书给的参考值 −58.9% / YTD −47.4% 是基于该盘中价与另一套基准，本 dossier 全部重算并在 `facts.md` §A 登记了偏差。
- **52 周高点两源不一致（$762.48 vs $786.28，3.1%）**：窗口起点差一到两天所致，非数据冲突。采用较严格的 Yahoo 值。
- **横向对照为本轮自算**：ADBE/CRM/NOW/WDAY/HRB/MSFT/^NDX 的同窗口涨跌幅直接从 Yahoo chart API 计算，不依赖任何二手引述。
- **未取用的来源**：DEF 14A（proxy，O13）、irs.gov e-file 授权文档（O9）、FTC/多州 AG 案卷（O10）、竞品份额一手数据（O12）。这四项是本 dossier 最主要的证据缺口。
- 登记来源总数：**19**（9 个 A1 一手 + 3 个价格/市场 B1 + 7 个叙事/政策 B1-B2）。
