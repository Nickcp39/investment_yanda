# ORCL Source Register — run_date 2026-08-07

**来源等级**：`A1` 一手申报/财报电话会原文 · `A1-proxy` 申报文件的复刻页（非评论） ·
`B1` 结构化聚合器（衍生自申报） · `B2` 媒体（含对电话会的转述） · `C1` 评级机构

> **本轮的一个结构性限制必须先说明**：`sec.gov`、`oracle.com`、`investor.oracle.com`
> 在本轮对 WebFetch **一律返回 HTTP 403**（机器人拦截，非权限问题）。
> 因此**没有任何一条 A1 级直连来源**。8-K 数字通过复刻页取得并与独立聚合器逐行对账。
> 这是 completeness 只有 58% 的主要原因之一。

---

## A 级 — 申报文件（本轮均为 proxy）

| source_id | 名称 | tier | public_date | fetched_at | URL |
|---|---|---|---|---|---|
| **A1p-1** | Oracle Q4 & FY2026 业绩 8-K Exhibit 99.1（完整损益表）| **A1-proxy** | 2026-06-10 | 2026-08-07 | 取得: https://www.stocktitan.net/sec-filings/ORCL/8-k-oracle-corp-reports-material-event-808097bbcd84.html<br>原文(403): https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm |
| A1-2 | Oracle 官方业绩新闻稿（**403，未取得**）| A1 | 2026-06-10 | — | https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ |
| A1-3 | Oracle FY2026 10-K（**403，未取得** → O2/O3/O10 的根因）| A1 | 2026-06 | — | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm |
| A1-4 | 2026-02 票据发行 424B2（未直读，仅引用）| A1 | 2026-02 | — | https://www.sec.gov/Archives/edgar/data/1341439/000119312526035603/d33906d424b2.htm |

**A1p-1 覆盖的数字**：FY2026 与 Q4 全部收入分部、营业利润、**利息费用 $4,599M / $1,438M**、
非营业收入 $3,547M、税前 $19,554M、税 $2,467M、净利 $17,087M、**优先股股息 $103M / $81M**、
EPS $5.83 / $1.45、基本与稀释加权股数、OCF $32,000M、capex $55,663M、FCF −$23,700M、
RPO $638B（+363%，环比 +$85B）、$75B 预付/自带硬件、FY2027 指引 $90B / $8.05、
FY2026 融资 $43B 债 + $5B 股权、季度股息 $0.50。

---

## B 级 — 聚合器与市场数据

| source_id | 名称 | tier | fetched_at | URL | 用途 |
|---|---|---|---|---|---|
| **A2-3** | stockanalysis.com — ORCL 损益表 / 资产负债表 / 现金流量表 / 比率（FY2022–FY2026）| B1 | 2026-08-07 | https://stockanalysis.com/stocks/orcl/financials/ 及 /balance-sheet/ /cash-flow-statement/ /ratios/ | **五年序列的唯一来源**。FY2026 三个关键行与 A1p-1 **逐行一致** → 本轮判定可信 |
| **A2-4** | Yahoo Finance chart API — ORCL 日收盘 + 52 周区间 | B1 | 2026-08-07 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL | 价格、52 周高低、市场状态 |
| A2-5 | stockanalysis.com — ORCL 历史价格 / 统计 | B1 | 2026-08-07 | https://stockanalysis.com/stocks/orcl/history/ 、/statistics/ | 价格第二源、股数、EV/净债务 |
| A2-6 | investing.com — ORCL 报价 | B1 | 2026-08-07 | https://www.investing.com/equities/oracle-corp | 价格第三源 |

> **A2-3 的口径警告**：其"市值/EV/P-E/EV-EBITDA"列对最新财年使用**当前**市值，
> 早年列的定价基准未明。**因此 de-rating 分解（facts.md F9）不用该表，改用实际收盘价 × 已报告 EPS 自算。**
> 与市价无关的比率（ROIC / Debt-EBITDA / 毛利率 / 现金流 / 资产负债表）则采用。

---

## B2 级 — 媒体（多为对电话会与公告的转述，已在 raw/ 中逐条标注）

| source_id | 名称 | public_date | URL | 提供了什么 |
|---|---|---|---|---|
| B1-3 | Cloud Wars | 2026-06 | https://cloudwars.com/ai/oracle-q4-blowout-led-by-backlog-growth-of-363-to-638-billion/ | **RPO 四季度轨迹** 455/523/553/638 |
| B1-4 | MLQ.ai + SeekingAlpha（Q4 电话会汇总）| 2026-06-10 | https://mlq.ai/news/oracle-reports-557b-fy2026-capex-guides-to-70b-net-outlay-in-fy2027/ · https://seekingalpha.com/news/4602468-... | FY2027 净现金 capex ~$70B、$40B 融资、**毛利率 step-down**、**管理层 ROIC 口径** |
| B1-5 | Barchart | 2026-07 | https://www.barchart.com/story/news/3276434/... | **GPU 利用率 97.5%**、49% 客户续约/92% GPU、四客户各 >$8B、"OpenAI ≈ 一半 RPO" |
| B1-6 | Motley Fool | 2026-07-29 | https://www.fool.com/investing/2026/07/29/oracle-stock-20-billion-reasons-not-to-buy/ | FY2026 发债 $43B、$20B ATM、YTD −38% |
| B1-7 | Yahoo Finance / Motley Fool | 2026-07 | https://finance.yahoo.com/markets/stocks/articles/oracle-biggest-backlog-ai-industry-203117785.html | **CFO Hilary Maxson "ROIC in the high 20s"**、卖方共识 $259.07（区间 $155–400）、丢失 MSFT 数据中心合约 |
| B1-8 | Cryptobriefing | 2026-06 | https://cryptobriefing.com/oracle-ai-backlog-638-billion/ | 上年 RPO $138B、12% / $76B 转化、**OpenAI >$319B（>50%）**、**2026-06-10 盘后 −7~10%** |
| B1-9 | EBC Financial | 2026-07 | https://www.ebc.com/forex/oracle-stock-falling-ai-backlog | OpenAI 合约 ~$300B/5yr 自 FY2028、平均目标价 $251.85（37/5/1）、Jeff Henley 减持 |
| B1-10 | Dealroom 汇总（403，未取得）| 2026 | https://app.dealroom.co/news/feed/oracle-s-ai-gamble-638b-backlog-built-on-156b-debt-and-risky-openai-dependence | — |
| B1-11 | Simpson Thacher 交易公告 | 2025-09-26 | https://www.stblaw.com/about-us/news/view/2025/09/26/oracle-completes-$18-billion-senior-notes-offering | **$18B 高级票据**（由 $15B 上调）|

---

## C 级 — 评级机构

| source_id | 机构 | 动作 | public_date | URL |
|---|---|---|---|---|
| **C1-2** | **S&P Global** | **下调 BBB → BBB−**；FY2027 capex 预测上修至 $90–95B；FOCF 缺口预测 −$42B；杠杆升至 4x 中段；点名 OpenAI 集中敞口 | **2026-07-09** | https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101695609 |
| C1-3 | Moody's | 确认 Baa2 / P-2，**展望转负面**；另点名 OpenAI 合约"significant counterparty risk" | 2026 | https://www.investing.com/news/stock-market-news/moodys-revises-oracles-outlook-to-negative-amid-ai-expansion-93CH-4155891 |
| C1-4 | Fitch | 确认 BBB / F2，展望稳定 | 2026 | https://finance.yahoo.com/news/oracle-stock-rises-fitch-affirms-125343106.html |

---

## 本轮**未能取得**的来源（→ 直接对应 OPEN 项）

| 缺失来源 | 阻塞的 OPEN | 影响 |
|---|---|---|
| FY2026 **10-K 全文**（403）| **O1 / O2 / O3 / O10** | 客户集中度原文、折旧年限、资本化利息、完整资产负债表 |
| Q4 FY2026 **电话会一手 transcript** | **O4** | CFO "high 20s" 与 ROIC 口径均为二手转述 |
| **OpenAI** 财务数据（收入 run-rate / 烧钱 / 融资）| **O1（blocking）** | 交易对手信用完全不可量化 |
| DEF 14A / Form 4 | **O7** | operator 模块不给评分 |
| ORCL **CDS 利差**历史 | O9 | C10 的信用市场维度缺失 |
| 卖方一致预期**修正历史** | O8 | 无法判断预期是否被下调 |
| The Information 关于 **OCI 毛利率**的报道 | O6 | 分部单位经济无直接读数 |

> **WebSearch 预算在本轮中途耗尽（200/200）**，其后仅能使用 WebFetch 在已发现的 URL 上取数。
> 这是上表多项缺失的直接原因，**已如实反映在 completeness 58% 中**。
