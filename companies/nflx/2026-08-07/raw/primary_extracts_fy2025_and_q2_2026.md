# NFLX Raw Primary Extracts — FY2023–FY2025, Q1/Q2 2026

抓取方式：SEC EDGAR XBRL/R-file 直读（`data.sec.gov` + `www.sec.gov/Archives/...` 带 User-Agent），
非二手镜像。Netflix 的内容资产科目全部用自定义 `nflx:` 扩展标签，不在 companyfacts API 里，
因此逐份 filing 的 R-file 渲染表被直接解析。单位：$ 千（原文）/ 下文表格换算为 $ 百万。

---

## 1. CONSOLIDATED STATEMENTS OF OPERATIONS（10-K FY2025 R3；10-Q Q2'26 R2）

| $M | FY2023 | FY2024 | FY2025 | Q1'26 | Q2'26 | H1'26 | H1'25 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Revenues | 33,723.3 | 39,001.0 | 45,183.0 | 12,249.8 | 12,559.9 | 24,809.7 | 21,622.0 |
| Cost of revenues | 19,715.4 | 21,038.5 | 23,275.3 | 5,888.2 | 6,037.0 | 11,925.2 | 10,588.5 |
| Sales & marketing | 2,657.9 | 2,917.6 | 3,301.3 | 842.2 | 823.8 | 1,666.1 | 1,401.6 |
| Technology & development | 2,675.8 | 2,925.3 | 3,391.4 | 959.7 | 1,007.7 | 1,967.4 | 1,647.5 |
| General & administrative | 1,720.3 | 1,702.0 | 1,888.4 | 602.6 | 498.9 | 1,101.5 | 862.7 |
| **Operating income** | 6,954.0 | 10,417.6 | **13,326.6** | 3,957.0 | 4,192.6 | 8,149.6 | 7,121.7 |
| Operating margin | 20.6% | 26.7% | **29.5%** | 32.3% | **33.4%** | 32.8% | 32.9% |
| Interest expense | (699.8) | (718.7) | (776.5) | (262.1) | (175.7) | (437.8) | (366.8) |
| **Interest and other income (expense)** | (48.8) | 266.8 | 172.5 | **2,852.2** | 51.7 | **2,903.8** | 90.5 |
| Provision for income taxes | (797.4) | (1,254.0) | (1,741.4) | (1,264.3) | (667.2) | (1,931.5) | (829.6) |
| **Net income** | 5,408.0 | 8,711.6 | **10,981.2** | **5,282.8** | 3,401.4 | 8,684.2 | 6,015.8 |
| Diluted EPS | $1.20 | $1.98 | $2.53 | $1.23 | $0.80 | $2.03 | $1.38 |
| Diluted shares (M) | 4,494.97 | 4,392.61 | 4,343.86 | 4,298.44 | 4,261.30 | 4,279.78 | 4,359.17 |

> **红旗**：H1'26 的 "Interest and other income" = **$2,903.8M**（H1'25 仅 $90.5M）。
> 其中 **$2.8B 是 Warner Bros. Discovery 交易的终止费**，一次性、非经营、进 Q1'26。
> 任何用 TTM 净利/TTM FCF 做锚的做法都会被它污染。全部 EPS 已按 10:1 拆股重述
> （FY2023 原报 $12.03，FY2025 10-K 重述为 $1.20）。

---

## 2. CONSOLIDATED STATEMENTS OF CASH FLOWS（10-K FY2025 R5；10-Q Q2'26 R5）— **本次核心**

| $M | FY2023 | FY2024 | FY2025 | Q1'26 | Q2'26 | H1'26 | H1'25 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Net income | 5,408.0 | 8,711.6 | 10,981.2 | 5,282.8 | 3,401.4 | 8,684.2 | 6,015.8 |
| **Additions to content assets（现金流出）** | **(12,554.7)** | **(16,223.6)** | **(17,096.6)** | (4,846.9) | (4,927.5) | **(9,774.4)** | (7,385.5) |
| Change in content liabilities | (585.6) | (779.1) | (610.8) | 45.2 | (181.8) | (136.6) | (625.3) |
| **Amortization of content assets（非现金加回）** | **14,197.4** | **15,301.5** | **16,422.2** | 4,217.9 | 4,311.3 | **8,529.2** | 7,655.2 |
| D&A of property, equipment & intangibles | 356.9 | 328.9 | 333.4 | 98.6 | 100.5 | 199.1 | 160.1 |
| Stock-based compensation | 339.4 | 272.6 | 368.4 | 140.4 | 131.3 | 271.7 | 152.8 |
| Deferred income taxes | (459.4) | (590.7) | (442.1) | 58.8 | 81.3 | 140.1 | (299.7) |
| **Net cash provided by operating activities** | 7,274.3 | 7,361.4 | **10,149.3** | 5,290.2 | 1,743.8 | 7,034.0 | 5,212.5 |
| Purchases of property and equipment | (348.6) | (439.5) | (688.2) | (196.1) | (218.6) | (414.8) | (284.2) |
| Acquisitions | 0 | 0 | (17.2) | (585.7) | 0 | (585.7) | 0 |
| **Repurchases of common stock** | (6,045.3) | (6,263.7) | **(9,127.2)** | (1,270.6) | **(4,714.4)** | (5,985.0) | (5,190.7) |
| Repayments of debt | 0 | (400.0) | (1,833.5) | 0 | 0 | 0 | (1,833.5) |
| Interest paid (supplemental) | 684.5 | 674.5 | 718.6 | — | — | — | — |

**Netflix 自己的 FCF 定义**（Q2'26 股东信脚注 10，原文）：
> "Defined as cash provided by (used in) operating activities less purchases of property and equipment."

> 定义在 Q4'25 信里做过措辞清理：此前是 "...less purchases of property and equipment **and change in
> other assets**"。该项自 FY2023 起在勾稽表中一直为 0（7,274.3 − 348.6 = 6,925.7 ✓；
> 7,361.4 − 439.5 = 6,921.8 ✓），所以是措辞清理而非口径变更。**FCF = OCF − PP&E capex，就这样。**

**Netflix 自报的季度 FCF**（Q2'26 股东信 p.1 汇总表）：
Q2'25 $2,267M · Q3'25 $2,660M · Q4'25 $1,872M · **Q1'26 $5,094M** · **Q2'26 $1,525M**
→ TTM（Q3'25–Q2'26）= **$11,151M**（与逐行计算 $11,152M 吻合）。
→ **Q2'26 FCF 同比 −32.7%**；公司归因："higher cash tax payments due in part to the Warner Bros.
termination fee"。

---

## 3. 现金内容支出 vs 内容摊销 —— 缺口表（(a) 的答案骨架）

| 期间 | 现金 additions | 摊销 amortization | **缺口 = add − amort** | **比率 add/amort** |
|---|---:|---:|---:|---:|
| FY2023 | 12,554.7 | 14,197.4 | **−1,642.7** | **0.884x** |
| FY2024 | 16,223.6 | 15,301.5 | +922.1 | 1.060x |
| FY2025 | 17,096.6 | 16,422.2 | +674.5 | 1.041x |
| H1'25 | 7,385.5 | 7,655.2 | −269.7 | 0.965x |
| Q1'26 | 4,846.9 | 4,217.9 | +629.0 | 1.149x |
| Q2'26 | 4,927.5 | 4,311.3 | +616.2 | 1.143x |
| **H1'26** | **9,774.4** | **8,529.2** | **+1,245.2** | **1.146x** |
| **TTM Jun-26** | **19,485.6** | **17,296.2** | **+2,189.4** | **1.127x** |

同比：H1'26 现金内容支出 **+32.3%**，内容摊销只 **+11.4%**。
管理层 FY2026 指引：现金内容支出/摊销比 **~1.1x**，内容摊销全年 **+~10%**（上半年前置）。

---

## 4. CONSOLIDATED BALANCE SHEET（10-Q Q2'26 R6）

| $M | 2025-12-31 | **2026-06-30** |
|---|---:|---:|
| Cash and cash equivalents | 9,033.7 | **9,099.2** |
| Short-term investments | 28.7 | 28.7 |
| **Content assets, net** | 32,778.4 | **33,837.6** |
| Property and equipment, net | 2,004.4 | 2,398.8 |
| Total assets | 55,597.0 | 58,450.4 |
| Current content liabilities | 4,084.9 | 3,866.5 |
| Non-current content liabilities | 1,579.5 | 1,625.6 |
| Short-term debt | 998.9 | **2,483.8** |
| Long-term debt | 13,464.0 | **11,825.5** |
| **Total debt** | 14,462.8 | **14,309.3** |
| **Total stockholders' equity** | 26,615.5 | **30,152.1** |
| Shares issued & outstanding | 4,222,162,150 | **4,163,939,676** |
| Treasury stock (shares) | 346,541,145 | 413,373,678 |

Netflix 自报净债（Q2'26 信 p.15）：14,309.3 + 49.0（发行成本/OID）+ 13.8（套保公允调整）
− 9,099.2（现金）− 28.7（短投）= **净债 $5,244.2M**。

内容资产构成（2026-06-30，10-Q R39）：Licensed $12,229.7M；Produced $21,607.8M
（Released 扣摊销 $10,487.5M / In production $10,313.4M / In development & pre-production $806.9M）。

内容义务（10-Q R54）：Total streaming content obligations **$25,106.7M**（2025-12-31: $24,039.2M），
其中**表外未记录部分 $19,600M**（2025-12-31: $18,400M）。

---

## 5. 分区营收（10-K FY2025 R41；10-Q Q2'26 R35；Q2'26 股东信 p.7）

| $M | FY2023 | FY2024 | FY2025 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **UCAN** | 14,873.8 | 17,359.4 | 19,957.2 | 4,929 | 5,072 | 5,339 | 5,245 | **5,432** |
| UCAN Y/Y | | +16.7% | +15.0% | +15% | +17% | +18% | +14% | **+10%** |
| **EMEA** | 10,556.5 | 12,387.0 | 14,514.6 | 3,538 | 3,699 | 3,873 | 3,998 | **4,034** |
| EMEA Y/Y（F/X 中性） | | | | +15% | +15% | +15% | +12% | **+11%** |
| **LATAM** | 4,446.5 | 4,839.8 | 5,357.5 | 1,307 | 1,371 | 1,418 | 1,497 | **1,584** |
| LATAM Y/Y（F/X 中性） | | | | +23% | +20% | +20% | +18% | **+16%** |
| **APAC** | 3,763.7 | 4,414.7 | 5,353.7 | 1,305 | 1,369 | 1,421 | 1,509 | **1,510** |
| APAC Y/Y（F/X 中性） | | | | +23% | +20% | +19% | +19% | **+18%** |
| **合计** | 33,723.3 | 39,001.0 | 45,183.0 | 11,079 | 11,510 | 12,051 | 12,250 | **12,560** |
| 合计 Y/Y | | +15.7% | +15.9% | +15.9% | +17.2% | +17.6% | +16.2% | **+13.4%** |

---

## 6. Q2 2026 股东信关键原文（2026-07-16，8-K Ex-99.1）

**FY2026 指引**
> "we are narrowing our revenue forecast to **$51.0-$51.4B**, which represents **13%-14% growth**
> (~12% F/X neutral) ... a projected **rough doubling of our ads revenue to approximately $3 billion**.
> We continue to anticipate an **operating margin of 31.5%** for 2026 ... vs. 29.5% in 2025.
> Our forecast implies **annual operating income growth of 20%+** for 2026."

**FCF 与内容比率**
> "For the full year, we continue to expect **FCF of approximately $12.5B**, and an annual
> **cash content spend to amortization ratio of ~1.1x**."

**利润率与摊销节奏**
> "operating income in Q2 grew slower than revenue because our **content amortization growth is higher
> in the first half of the year**; we continue to expect content amortization to grow slower in the
> second half of the year and to **increase ~10% for 2026**."

**参与度（engagement）**
> "in the first half of 2026, our members watched more than **97 billion hours, up 2% year over year**.
> This was slightly faster than the **1.5% growth in 2025**, despite the competitive impact of the
> Winter Olympics and the World Cup this year."
> "we serve a massive audience (**approaching 1B people**)"

**直播内容的经济学**
> "in 2026, we expect **live programming to account for just over 5% of our content spend but only ~1%
> of view hours**. Yet, live event programming accounted for **six of the top 10 new member sign-up days
> over the last five years** (and we've only been doing live events since 2023)."

**生成式 AI（(d) 的一手证据）**
> "Across the production lifecycle, from concept and pre-visualization through post and delivery,
> **GenAI utilization by our creative partners is scaling quickly. In 2026, GenAI workflows have been
> used in roughly 300 of our titles**, with the largest concentration of work in post-production.
> We are increasingly leveraging these tools to deliver **higher quality output more quickly and at a
> lower cost than traditional methods**. In some cases, productions would have had to leave out key
> shots and sequences in the absence of GenAI technology."
> "We are leveraging **LLMs to improve title discovery** ... **AI-powered natural language search**."
> "In Q2, we **expanded our AI-powered tools across the full advertising lifecycle**."

**提价**
> "Our first half price changes, in markets like the **US, Mexico and Spain**, have gone well with the
> impact consistent with prior price changes and our expectations."
> UCAN "Q2 revenue growth of 10% reflects only a **partial quarter impact** from our recent price change."

**用户获取摩擦（值得注意）**
> "last week we began **re-testing free trials for non-rejoining new members** in a number of markets
> around the world (excluding the US and UK)."

**披露收窄（第二次）**
> "After today's What We Watched report ... we will shift to publishing this report **annually in the
> first quarter, beginning in 2027**. The goal of separating the publication of the report from our
> earnings results is to **keep the focus on our primary financial metrics – revenue and operating profit**."

**资本配置**
> "In April, our Board of Directors authorized the repurchase of an **additional $25B** of our stock on
> top of the $6.8B of capacity we had remaining as of the end of Q1. In Q2, we bought back **$4.7B** of
> stock, **our largest quarter of share repurchases**, and we currently have **$27.1B of capacity** left."
> "We ended the quarter with **gross debt of $14.4B** and cash and cash equivalents of $9.1B.
> We have **$1B of debt maturing later this year, which we plan to refinance**."

---

## 7. Warner Bros. Discovery 交易全过程（10-K FY2025 R66；10-Q Q2'26 R14 原文）

> "**In March 2026**, the Company completed an acquisition which was accounted for as a business
> combination for a total purchase price of approximately **$587 million**, consisting of cash consideration.
>
> **On December 4, 2025**, the Company entered into a definitive agreement and plan of merger with
> **Warner Bros. Discovery, Inc.** ("WBD"), to acquire WBD's **streaming and studios businesses, including
> its film and television studios, HBO Max and HBO** ... which was then amended by the parties thereto on
> **January 19, 2026**.
>
> **On February 27, 2026**, WBD provided notice to the Company that it had **terminated** the Amended and
> Restated Merger Agreement in accordance with its terms in order to enter into an Agreement and Plan of
> Merger with **Paramount Skydance Corporation** ("PSKY"). Concurrently ... PSKY, on behalf of WBD, paid a
> **$2.8 billion termination fee owed to Netflix** ... The $2.8 billion termination fee received was
> recorded in "**Interest and other income (expense)**" ... during the **first quarter of 2026**."

10-K FY2025 补充（R66）：原交易 equity value **$72.0B** / 总对价 **$82.7B**；2026-01-19 修订为
全现金 **$27.75/股**；分手费条款 **$5.8B**（Netflix 侧）；Netflix 搭建了 **$42.2B 过桥融资**。
Netflix 最终**拒绝加价**，收下 $2.8B 走人。

---

## 8. 拆股（8-K 2025-10-30 Item 8.01；8-K 2025-11-14 Item 5.03）

- 比例：**10-for-1 forward split**（每股增发 9 股）
- 董事会批准/公告：**2025-10-30**
- 股权登记日：**2025-11-10**
- 分派：**2025-11-14 收盘后**（同日向 Delaware 州务卿提交章程修订）
- **首个拆股调整后交易日：2025-11-17**
- 本 dossier **所有价格与每股数据均为拆股调整后**。

---

## 9. FY2025 实际 vs 一年前指引（Q4'24 股东信 2025-01-21 vs Q4'25 信）

| 指标 | 2025-01 给的 FY2025 指引 | FY2025 实际 | 结果 |
|---|---|---:|---|
| 营收 | $43.5–44.5B | **$45.183B** | 超上限 $0.68B |
| 经营利润率 | 29%（1/1/2025 汇率） | **29.49%** | 略超 |
| FCF | "about $8B"（年内上调至 ~$9B） | **$9.461B** | 超 |
| 现金内容支出 | "roughly $18B" | **$17.097B** | 少花 ~$0.9B |

> Netflix 自述（Q4'25 信）：FCF 超预期部分原因是巴西税务争议约 **$700M 保证金的缴纳时点从 2025
> 推迟到 2026**——即 FY2025 的 $9.46B 里有 ~$0.7B 是**时点搬移**，且构成 FY2026 的逆风。
> 10-K FY2025 (R64) 披露巴西税务相关**赔偿担保计提 $619M**（FY2024 $400M，FY2023 $300M）。

---

## 10. 披露制度变化（(b) 的关键约束）

Q4'24 股东信（2025-01-21）原文：
> "beginning with our Q1'25 earnings in April, we'll **no longer report paid memberships and ARM on a
> regular quarterly basis**; we will continue to announce paid memberships as we cross key milestones."

核验结果（对 FY2025 10-K + 2026 两份 10-Q 做全文检索）：

| 项目 | FY2023/FY2024 10-K | FY2025 10-K & 2026 10-Q |
|---|---|---|
| 收入附注标题 | "Revenue **and Membership** Information" | "Schedule of Streaming Revenues **by Region**" |
| 分区付费会员数 | 每季披露 | **已删除** |
| 分区 ARM（每会员平均收入） | 每季披露 | **已删除** |
| 全球付费会员数 | 披露（FY2024 末 302M） | **已删除** |

FY2025 10-K 全文中 "average revenue per membership" 出现 **0 次**，无任何会员数。
⇒ **外部分析者已无法从申报文件里把"量"和"价"分开。** 这是 (b) 的硬约束，写进 OPEN。
