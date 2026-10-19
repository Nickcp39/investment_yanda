# 日元套息交易（Yen carry trade）历史：机制、规模、三次平仓，以及对"人民币套息"说法的对照

> 编写日期：2026-10-15。规则：只引用本人实际打开过的原始来源；每个数字附来源编号（S1…S24，见文末附录，含 URL、日期、原文关键句）。凡是没打开原文的说法，单独标为【未核实】。
> 汇率数字用美联储 H.10 纽约中午价（S10），持仓用 CFTC 原始年度文件（S11），散户用 FFAJ 原始 Excel（S16），均为本人下载计算；与媒体常引的日内极值会有出入。

---

## 0. 先给结论（5 条）

1. **"日元套息"不是一个东西，而是三类人**：(a) 境外对冲基金/投行用远期、掉期、期货做空日元（带杠杆、会被追保证金，是平仓的"燃料"）；(b) 日本散户的保证金外汇（"渡边太太"，带杠杆但存量小，而且习惯逆势）；(c) 日本居民/机构用自有储蓄买外币资产（投信、uridashi、寿险、GPIF，量最大，但**不借钱、不被强平**）。美联储 Gagnon & Chaboud（S4）明确说 (c) "cannot be considered a carry position, because the sector is not leveraged"。
2. **规模没有权威单一数字**。BIS 对 2024 年 8 月前的"中间估计"是 **¥40 万亿（约 $2,500 亿）**（S1）；CFTC 期货投机净空峰值只有约 **¥2.3 万亿**（2007-06、2024-07 两次几乎相同，S11）；媒体上的 "$1 万亿""$4 万亿""$20 万亿" 都没有可追溯的原始测算，多是把"所有日元债权"或"日本全部海外资产"混进来了（见 §3.3）。
3. **三次大平仓的共同形态**：日元先长期贬值（1995–98 美元兑日元 +81%，2005–07 +21%，2021–24 +57%），美日政策利差约 **4.75–5.4 个百分点**；然后利差"开始收窄或预期收窄"+ 风险偏好骤降（VIX 上升）触发平仓，日元在**几天内**升值 10% 以上。1998 年 10 月 5→9 日 USDJPY −13%（S10）；2008 年 10 月一个月内 AUDJPY −32.7%；2024 年 7-10→8-05 USDJPY −11%、日经单日 −12.4%（S12）。
4. **平仓伤的是带杠杆的人和高息货币**：1998 年老虎基金两天亏约 12%（S5）；2007-08 年澳元/纽元/比索兑日元跌 47–54%（S10）、日本散户被自动止损（S15）；2024 年墨西哥比索、日本银行股/保险股、加密资产（−20%）（S1）。日本的寿险、GPIF 等只有估值损失，没有被迫卖出。
5. **对照"人民币套息"最关键的四个问题**：①非居民能否在离岸以接近在岸的利率大规模借到人民币、远期/掉期市场有多深（日元用了 1980–1998 近二十年才打通，S24）；②人民币趋势是贬还是升（日元套息只在日元贬值期赚钱，S10/S24）；③利差有多大、波动率多低（日元三次都是 ~5pp）；④汇率风险最终在谁手里——是不怕追保证金的储蓄者，还是带杠杆的境外投机者。另：中国与日本一样是巨额净债权国（2025 年末日本 ¥561.8 万亿、中国约 ¥636 万亿，S18），这类国家的货币在避险时倾向于**急升**，这正是融资货币的尾部风险。

---

## 1. 背景：日本央行利率路径与美日利差

| 日期 | BOJ 政策 | 来源 |
|---|---|---|
| 1998-09-09 | 隔夜拆借利率引导至 "around 0.25%" | S21 |
| 1999-02-12 | 零利率：先 ~0.15%，再 "as low as possible" | S3 |
| 2000-08-11 | 退出零利率，0.25% | S3 |
| 2001-03-19 | 量化宽松，目标改为准备金余额 "around 5 trillion yen" | S3 |
| 2006-03-09 / 07-14 | 结束 QE（"effectively zero"）/ 加息至 0.25% | S3 |
| 2007-02-21 | 0.5%（2007 年套息高峰期的日本利率） | S3 |
| 2008-10-31 / 12-19 | 降至 0.3% / 0.1% | S3 |
| 2010-10-05 | 全面宽松，0–0.1% | S3 |
| 2016-01-29 | 负利率 −0.1%（2016-02-16 起的准备金维持期生效） | S3 |
| 2024-03-19 | 结束负利率与 YCC，0–0.1% | S3 |
| 2024-07-31 | 0.25% + 宣布缩减购债 | S3 |
| 2025-01-24 | 0.5% | S3 |
| 2025-12-19 | 0.75% | S3 |
| 2026-06-16 | 1.0% | S3 |
| **2026-09-18** | **1.25%（2026-09-24 生效，7–2 票）＝截至 2026-10-15 最新** | S3 |

美日政策利差（美联储官方表 S21）：1998 年 8 月 ~5.0–5.25pp；2007 年 6 月 ~4.75pp（5.25% vs 0.5%）；2024 年 7 月 ~5.1–5.4pp（5.25–5.50% vs 0–0.25%）；**2026 年 10 月 ~2.5–2.75pp**（美联储 2026-09-17 加息至 3.75–4.00% vs BOJ 1.25%）。

---

## 2. 渠道与工具：谁借日元、怎么借、钱去了哪

### (a) 对冲基金 / 投行 / 银行自营（杠杆套息的主体）
- **工具**：BIS 1999（S5）列出三种：远期卖出日元；"synthetic forward"（即期卖日元 + 掉期）；卖空借来的日元证券。BIS 2024（S6）："The more common approach used by hedge funds and other speculators relies on derivatives – eg FX forwards, swaps and options"——**不需要资产负债表上借日元，所以统计上难追踪**。
- **银行间通道**：Hattori & Shin（S8）：华尔街银行东京分行在日本同业市场借日元、转给纽约总部，体现在"interoffice accounts"；2007 年危机前外资银行出现"unprecedented net short position in Japanese assets"，**2007 年 8 月急剧平仓**。BIS 2024（S1）称同一指标 2021 年以来翻倍至近 ¥14 万亿。
- **钱去了哪**：1995 年春起投向美国国债到新兴市场高息资产，1996–97 年大量进入泰国等东亚货币市场（"paid off as long as the yen did not appreciate and other East Asian currencies remained firmly pegged"，S5）；2002–07 年主要目标货币是澳元、纽元、英镑、巴西雷亚尔、南非兰特（S2）；2024 年受冲击最大的高息货币是墨西哥比索、巴西雷亚尔、南非兰特（S1）。
- **期货（CFTC）只是冰山一角**：BIS 说期货 "only the tip of the iceberg"，场外远期上限约 $1,600 亿（S1）。

### (b) 日本散户："渡边太太"保证金外汇、投信（toshin，含"双层"基金）、uridashi 债
- **保证金外汇**：外为 Gaitame 一家账户从 2003 年初不到 2,000 个增至 2007-06 近 12 万个，保证金约 ¥900 亿（S2）。BOJ（S15）：成交额 2006Q1 约 ¥50 万亿 → 2008Q1 ¥230 万亿；但 **2008-03 末未平仓总额只有 ¥3.1 万亿**，远小于外币投信 ¥32.1 万亿；行为"逆势"（"buying into declines and selling into gains"）；2007-08-16 美元/日元跌破 115 时大量账户被自动止损，加速了日元升值。现状（S16，FFAJ）：未平仓总额 2024-07 约 ¥8.6 万亿、2026-09 约 ¥11.7 万亿；2026-07 散户净多外币 ¥4.13 万亿为序列最高。
- **投信（toshin）**：BIS（S2）：日本家庭通过外币投信 2007 年上半年每月净增约 ¥1.2 万亿，存量达 ¥35 万亿。BOJ（S15）把它定性为影响"long-term supply and demand"，不同于保证金外汇的短线冲击。**"双层/三层"基金**（底层资产 + 货币选择层，常选巴西雷亚尔、澳元等）机制见行业报道，但规模数字（如 Cerulli 引述的 ¥10.4 万亿）我没能打开原文，【未核实】。
- **uridashi 债**：境外发行人在日本向散户发行的外币债（S2 定义："Debt issued outside Japan and registered under Japanese securities laws for sale to Japanese investors"）。RBNZ（S17）：纽元 Eurokiwi/uridashi 发行在 2003–05 年激增，动因是"high domestic interest rates"与"low yields in Europe and Japan"。**本质是日本散户用储蓄承担汇率风险，不是借日元**。

### (c) 日本机构（寿险、GPIF、银行）买外债——算不算"套息"？
- **未对冲**：承担汇率风险，但资金是储蓄/养老金，不是借来的日元，无保证金追缴。Gagnon & Chaboud（S4）：2006 年末日本私人非银部门净外币资产约 $1.3 万亿，但"net long yen assets by an even larger magnitude"，所以**不算套息**；日本官方部门（外汇储备）$8,750 亿"net yen carry position"，但"would likely not be viewed as standard yen carry trade"。GPIF 2026-03 末持有外债 ¥73.4 万亿 + 外股 ¥74.4 万亿，外债基准为**不对冲**（S19）。
- **对冲**：反而是日元的"供给方"。BIS 2024（S6）："Japanese banks are natural suppliers of yen via FX derivatives"；日本信托账户 $2.7 万亿外币资产若 80% 对冲，相当于通过衍生品供给约 **$1.7 万亿**日元——对手方中就包括做空日元的投机者。Gagnon & Chaboud 的推论相同："many of the derivatives counterparties to Japanese exporters and investors are likely to be engaged in the carry trade"。
- **结论**：日本机构外投是"广义的利差驱动的资本外流"，不是狭义杠杆套息；但它们的对冲行为为境外杠杆套息提供了对手方。

### (d) 境外日元贷款（东欧房贷等）
- BIS 2007（S2）：东欧流行的是**瑞郎**房贷，且"less likely to be unwound quickly"。
- 奥地利 FMA（S20）：2012-09 家庭外币贷款 €334 亿中 92.9% 是瑞郎，其余"几乎全是日元"（本人推算约 €24 亿）。**"东欧大规模日元房贷"缺乏官方数据支撑**。
- 银行口径的境外日元贷款：对日本境外非银的日元贷款 2021Q2 ¥25 万亿 → 2024Q1 ¥41 万亿，主要借款人在英国、开曼、美国（S6）。

### (e) 2023–24 "日元资金支撑美股/AI 科技股"的叙事
- 证据是间接的：BIS（S1）：2024-07-24 "AI/tech stocks ... had dropped by around $1 trillion"，同日出现套息平仓迹象；BOJ（S14）指出美科技股市盈率处于历史高位；Hattori & Shin（S8）的"broad carry"论点——日元负债为对冲基金与金融中介的整体资产负债表扩张提供资金。**没有数据能直接说"多少日元买了纳指"**。

---

## 3. 规模估计：每个数字在量什么

### 3.1 各时期主要估计
| 时点 | 数字 | 量的是什么 | 来源 |
|---|---|---|---|
| 1998 年初 | $200–300 亿 | 经开曼注册载体的日元套息（McCauley & von Kleist，作者称可能低估） | S5 |
| 1998 年初 | $400–500 亿 | 某汇率策略师估计的日元空头（报刊引述） | S5 |
| 1998-05-26 | ¥0.79 万亿 | CFTC 非商业净空（期货） | S11 |
| 2006 年末 | < $3,000 亿 | 日本境外私人非银部门"经典套息"毛额上限（资产负债表） | S4 |
| 2006 年末 | $400 亿 | 日本银行业净日元套息头寸 | S4 |
| 2007Q1 | $1.05 万亿 | BIS 报告银行**全部**日元债权（各种用途，不等于套息） | S2 |
| 2007-06-26 | **¥2.35 万亿（有记录以来最大）** | CFTC 非商业净空 | S11 |
| 2008-03 | ¥3.1 万亿 | 日本散户保证金外汇未平仓**毛额** | S15 |
| 2023 年末 | $14.2 万亿 | 一边是日元的外汇掉期/远期/货币互换**名义本金**（大部分是对冲） | S6 |
| 2024Q1 | ¥41 万亿（$2,710 亿） | 对日本境外非银的日元贷款 | S6 |
| 2024Q1 | ¥133 万亿（$8,800 亿） | 对日本境外非银的全部日元债权（主要是开曼 SPV 证券，几十年的结构） | S6 |
| 2021→2024Q1 | +¥66 万亿（$4,350 亿） | 估算的衍生品市场"净日元供给"增量（被未观测的非银吸收） | S6 |
| 2024-07-02 | ¥2.30 万亿 | CFTC 非商业净空 | S11、S1 |
| 2024 年 8 月前 | ≤ $1,600 亿 | 对冲基金外汇远期投机上限（$14.2 万亿 × 5% × 24%） | S1 |
| 2024 年 8 月前 | **¥40 万亿（$2,500 亿）** | **BIS 综合"中间估计"（表内+表外），作者称偏低** | S1 |
| 2026-07-28 | ¥2.04 万亿 | CFTC 非商业净空（2026-09-15 已转为净多 ¥1.5 万亿） | S11 |

### 3.2 读数要点
- **CFTC 期货**：频率高但只覆盖交易所，且时点不一定对：1998 年投机者在 9 月初就已转为净多，比 10 月 7–8 日的暴涨早一个多月（S4、S11）。
- **BIS 银行统计**：只看资产负债表，抓不到远期/掉期；开曼的日元债权大量是 SPV 结构（例如投资美国 CLO），不能等同套息（S1、S6）。
- **散户数据**：成交额巨大（2024-07 单月 ¥1,455 万亿）但存量小，且散户常常逆势（2024-06 日元最弱时净空美元/日元，S16）。

### 3.3 常被转述、但没有可靠原始出处的说法【未核实】
- "2007 年日元套息 $1 万亿"：最接近的权威数字是 BIS 的 $1.05 万亿，但那是**全部日元银行债权**，BIS 自己说"the available data do not allow for a more refined measurement"（S2）。
- 2024 年的 "$4 万亿""$20 万亿"：未找到可追溯的测算。作为对照，日本**全部**对外资产 2025 年末才 ¥1,805.6 万亿（S18），日元一边的衍生品名义本金 $14.2 万亿中大部分是对冲（S6）。
- "摩根大通称 75% 套息已平仓"（2024-08）：广泛转述，原报告未打开；BIS 的判断是"Only a share ... appear to have been unwound"（S1）。
- "渡边太太主导日元汇率"：BOJ 数据显示其存量小且逆势（S15、S16）。
- 日经 2024-08-05 跌幅"仅次于 1987 年黑色星期一"：搜索摘要提及，未打开原文。
- 日本金融厅 2010/2011 年把散户外汇杠杆上限降到 50 倍/25 倍：多家券商与媒体转述，金融厅 PDF 已下载但文字无法提取，未核实原文。

---

## 4. 三次平仓（另附 2006–07 小波与 2026 年近况）

### 4.1 1998 年 10 月（LTCM / 俄罗斯危机之后）
- **积累**：日元自 1995 年春开始贬值（USDJPY 1995-04-19 81.12 → 1998-08-11 147.14，S10）；资金借日元投向美债、东亚货币市场等（S5）。
- **触发**：夏末全球风险偏好骤降（"sudden increase in market participants' risk aversion"）、银行收缩对冲基金杠杆（S4、S5）；10 月初市场预期日美政策方向反转：日本推出财政刺激、美欧央行转向宽松（S5）。LTCM 危机在"end-August and early-September 1998"，与 10 月 7–8 日的日元暴涨"quite distinct"；美联储意外降息 0.5pp 在 10 月 15 日（S7 原文如此；美联储官方表显示 9-29 和 10-15 各降 25bp，S21）。俄罗斯违约的具体日期本笔记未开原文核实。
- **日元涨幅**：BIS：8-31 至 9-07 美元兑日元跌约 9%，10-07/08 两天再跌 12%（S5）；"sharpest move in major foreign exchange rates since 1974"，一个月隐含波动率达 40%（S2）。H.10 中午价：10-05 134.54 → 10-09 117.00（−13.0%）；8-11 147.14 → 1999-01-11 108.83（−26%）；AUDJPY −22%（S10）。
- **伤到谁**：老虎基金旗舰 Jaguar Fund 在 10 月两天内亏约 12%，报刊称亏损高达 $20 亿；9 月初第一波时已亏约 $8 亿，市场传其开始了结 $350 亿美元/日元多头、其中约 $100 亿一夜抛出（均为市场传闻，S5）。
- **多久**：急性阶段 3 个交易日；整体从 8 月高点到 1999 年 1 月低点约 5 个月。
- **政策**：BOJ 9-09 降至 0.25%，1999-02 零利率；美联储 9-29、10-15、11-17 三次降息（S3、S21）。

### 4.2 2007–2008 年（次贷危机 → 雷曼）
- **积累**：BOJ 0–0.5%、美联储 5.25%；CFTC 净空 2007-06-26 创纪录 ¥2.35 万亿；散户保证金账户与外币投信激增（S2、S11、S15）；USDJPY 2007-06-22 124.09、AUDJPY 2007-07-19 107.36（S10）。
- **前奏**：2006 年 5 月、2007-02-27 两次小规模平仓（S4）。
- **第一波（2007 年 8 月）**：信用危机爆发，外资银行东京分行的日元净空"sharply unwound in August 2007"（S8）；2007-08-16 散户被自动止损（S15），AUDJPY 当日 −7.2%（96.60 → 89.63，S10）；CFTC 投机者 2007-08-21 已转为净多（S11）。
- **第二波（2008 年 9–10 月雷曼后）**：AUDJPY 2008-10-01 84.18 → 10-27 56.65，一个月 −32.7%（S10）。
- **总幅度**：USDJPY 124.09 → 87.80（2009-01-21，−29%）；AUDJPY −47%、NZDJPY −54%、MXNJPY −47%（S10）。
- **多久**：约 18 个月，分两波。
- **政策**：美联储 2007-09-18 开始降息、2008-12-16 降至 0–0.25%（利差从美国这一侧消失）；BOJ 只能从 0.5% 降到 0.1%（S3、S21）。

### 4.3 2024 年 7–8 月
- **积累**：2021–24 年 BOJ 负利率/零利率、美联储 5.25–5.50%；USDJPY 2021-01-05 102.70 → 2024-07-10 161.73（S10）；"carry-to-risk ratios ... peaked in the first quarter of 2024"（S1）；CFTC 2024-07-02 净空 ¥2.30 万亿（S11）。
- **触发链**：7-11/12 日本财务省买入日元 ¥5.53 万亿（S22）→ 7-24 AI/科技股市值蒸发约 $1 万亿（S1）→ 7-31 BOJ 加息至 0.25% + 缩表计划（S3）→ 8-02 美国就业数据疲弱（S1）→ 8-05 日本股市崩跌。
- **幅度**：USDJPY 7-10 161.73 → 8-05 143.95（−11%）→ 9-13 140.66（−13%）；AUDJPY −14.4%（S10）；AMRO：7-30 至 8-05 日元兑美元升值约 5.6%，墨西哥比索跌约 3.2%（S9）。8-05 日经 −12.40%（−4,451.28 点，收 31,458.42，S12），TOPIX −12%，VIX 在非交易时段超过 60（S1）。
- **伤到谁**：日本银行股、保险股；高息货币（比索最重）；散户保证金与加密资产（BTC/ETH 最多 −20%）；动量型 CTA；日本证券清算所把股指多头初始保证金上调 60–80%（S1）。离岸人民币（CNH）也明显升值（S1、S9）。
- **多久**：急性阶段 1–3 天；8-09 标普已收复本周全部跌幅，TOPIX 收复大部分（S1）；CFTC 净空 6 周内转为净多（S11）。
- **政策**：8-07 BOJ 副行长内田："the Bank will not raise its policy interest rate when financial and capital markets are unstable"（S13）。BIS 结论："Only a share ... appear to have been unwound"，且"leveraged positions were quickly being rebuilt"（S1）。

### 4.4 2026 年近况（截至 2026-10-15，供对照）
- BOJ 已加到 1.25%，但日元仍在 2026-07-29 贬到 163.86（高于 2024 年峰值，S10）；日本财务省 2026 年两轮买入日元合计约 ¥27 万亿（4-30 至 5-06 ¥11.73 万亿；7-30 至 8-26 ¥15.40 万亿，其中 7-31 为**美日联合干预**，S22）。
- CFTC 投机净空 7-28 ¥2.04 万亿 → 9-15 转为净多 ¥1.5 万亿（S11）；USDJPY 回落至 153.50（9-09）后又回到 158.34（10-09）。散户 2026-07 净多外币创纪录 ¥4.13 万亿（S16）。
- 2026-10-15 日经盘中 −5.39%，但日元只升值约 0.6%，主因是美国通胀（9 月 CPI 3.7%）与科技股（S23）——**不是每次日股大跌都是套息平仓**。

---

## 5. 对比"人民币套息"时真正有用的教训

1. **可兑换性 / 资本账户是前提，不是细节**。日本 1980-12 新外汇法把原则从"禁止、有例外"改为"自由、有例外"，境内外日元利率因此打通；机构投资者外投限额又过了约 8 年才不再约束，再过约 8 年才有 1996 年的"big bang"（S24）。日元套息能做到 ¥40 万亿级，靠的是：非居民可在东京同业市场借日元（S8）、日元衍生品名义本金 $14.2 万亿（S6）、CME 期货等。**看人民币时要先问**：非居民能否以接近在岸利率、大规模、可展期地借到人民币？离岸 CNH 资金池和掉期市场有多深？央行能否通过离岸流动性管理随时抬高借贷成本？——这些本笔记**没有研究**，需另查。可参照的事实：2024-08 平仓时 CNH 已"appreciated notably"，BIS 说它"not typical in carry trade funding"（S1），说明人民币已有一部分作为融资货币的头寸；AMRO 统计中国非银部门借了全球日元贷款/债券的 3.4%（S9），即中国主体此前更多是日元套息的**借方**。
2. **融资货币的趋势决定成败**。三轮日元套息都发生在日元持续贬值期，套息收益 = 利差 + 融资货币贬值，后者往往更大；一旦趋势反转（1998 年政策预期反转、2007 年美联储降息、2024 年 BOJ 加息+干预），就在几天内吐出数年收益（S10、S24）。若人民币的基本趋势是升值（顺差国、净债权国，S18），借人民币做套息就是逆势；若人民币处于有管理的稳定或缓慢贬值，则更像 2005–07 年的日元。**这是判断"人民币套息"能否成气候的第一变量**。
3. **利差与波动率**。日元三次都在 ~5pp 利差时发生；BIS 用"carry-to-risk"（利差 ÷ 隐含波动率）衡量吸引力（S1、S2）。低波动的有管理汇率会**放大** carry-to-risk——这正是"在压路机前捡硬币"（S1 原话"picking up nickels in front of a steamroller"）的典型设定：平时收益平滑，一旦汇率制度或政策预期变化，损失是跳跃式的。当前美日利差已缩到 ~2.5–2.75pp（S21）；人民币对美元的利差需另查。
4. **谁承担汇率风险，决定平仓会不会变成踩踏**。日本的绝大部分"空日元、多外币"敞口在不加杠杆的本国储蓄者手里（官方储备、寿险、GPIF、投信、uridashi），他们不被追保证金；真正的"踩踏燃料"是境外杠杆头寸（期货 ~¥2 万亿、远期 ≤$1,600 亿）和本国散户保证金（¥8–12 万亿毛额）（S1、S4、S16、S19）。对中国要区分：(i) 中国居民/机构出海（类似投信/GPIF，属组合分散）；(ii) 外国人借人民币投高息资产（真正的套息，可从 BIS 银行统计的人民币跨境债权、CNH 掉期、熊猫债等追踪）；(iii) 中国企业把美元债换成人民币债（负债币种切换，不是套息）。媒体口中的"人民币套息"常把三者混为一谈。
5. **平仓的触发与止损**：往往是融资国政策信号（BOJ 加息、财务省干预）+ 投资国风险事件（美国数据、科技股回调）叠加；融资国央行的反应决定持续时间（2024 年内田讲话一句话止跌，S13；2008 年 BOJ 无力降息，平仓持续 18 个月）。结构性的储蓄外流（投信、GPIF、寿险）几乎不会因一次冲击而逆转，所以 BIS 说"只有一部分"平仓（S1）。

## 6. 本笔记未覆盖 / 待核实
- 中国侧的任何数据（PBOC 政策利率、CNH 资金池、人民币跨境贷款、熊猫债、离岸掉期）——需另行研究。
- 俄罗斯 1998 年违约日期、日经 2024-08-05 是否为 1987 年后最大百分比跌幅、双层基金规模、金融厅杠杆上限原文、IMF GFSR（IMF 网站对 curl 返回 403，未打开）。
- 2026 年 7–9 月日元快速升值与 CFTC 转多的具体原因（除财务省联合干预外）未查证。

---

# 附录：已打开的原始来源（逐条摘录）

### S1. BIS Bulletin No 90 — Aquilina, Lombardi, Schrimpf, Sushko，"The market turbulence and carry trade unwind of August 2024"，2024-08-27
- URL（页面）：https://www.bis.org/publications/bulletin-90-market-turbulence-and-carry-trade-unwind-august-2024
- URL（PDF，已下载全文）：https://www.bis.org/publications/bulletin-90-market-turbulence-and-carry-trade-unwind-august-2024.pdf （旧链接 https://www.bis.org/publ/bisbull90.pdf 会跳转）
- 规模（核心）："Various estimates based on both on- and off-balance sheet activity yield a rough middle ballpark of ¥40 trillion ($250 billion) going into the event, which, if anything, is biased down due to data gaps."
- 期货（CFTC）："Net short positions in yen futures by 'speculative traders' ... had reached historical peaks of around ¥2 trillion (or about $14 billion) and were unwound during the event"；"currency futures are only the tip of the iceberg."
- 场外远期上限估算："an upper bound on the size of hedge fund speculative activity with currency forwards yields an estimate of around $160 billion"；脚注 3 算法："$14.2 trillion × 5% × 24% ≈ $160 billion"（远期+外汇掉期名义存量 × 对冲基金/自营交易商成交占比 × 远期占比）。
- 外资银行在日分行汇回总部（Hattori & Shin 2009 方法）："These have nearly doubled since 2021 ... to almost ¥14 trillion (or over $90 billion)."
- BIS 全球流动性指标："yen-denominated loans to non-banks resident outside Japan rose markedly after Covid-19, to about ¥40 trillion ($250 billion) by March 2024"
- 离岸中心最宽口径："cross-border yen bank claims on this segment had exceeded ¥80 trillion (approximately $500 billion) prior to the event"；但 "This figure covers bank claims of various types, most notably on special purpose vehicles issuing yen-denominated secured notes to fund various investments, such as in the US collateralised loan obligation market. Thus, care needs to be taken when interpreting various estimates."
- 触发与时间线："From the first half of July, the yen's depreciation trend had reversed, amid rumoured Bank of Japan interventions"；"on 24 July ... valuations of AI/tech stocks ... had dropped by around $1 trillion"；"After what was perceived as a hawkish rate hike by the Bank of Japan ... investors coalesced around a somewhat disappointing US labour market data release on 2 August."
- 冲击："On Monday 5 August the TOPIX lost 12%"；"the S&P 500 lost another 3.0%"；"the VIX spiked to levels above 60"；"In Japan, bank and insurance company stocks were hit especially hard."
- 恢复速度："By the close at the end of the week on Friday 9 August, the S&P 500 had recovered all the losses incurred since Monday, while the TOPIX had recovered most of them"
- 散户："Japanese retail margin traders had mostly shorted the yen after the pandemic, while their trading volumes ballooned"；"Bitcoin and Ethereum posting losses of up to 20%"
- 牵连货币："On 5 August, the yen appreciated the most, followed by the Swiss franc ... the recent episode also involved currencies not typical in carry trade funding, most notably the offshore renminbi (CNH), which also appreciated notably."；"Among the high-yielding investment currencies, the Mexican peso was hit hardest, followed by the Brazilian real and South African rand"
- 保证金："The Japan Securities Clearing Corporation increased initial margins for long positions of equity indexes by 60–80%"
- 结论："Only a share of various trades predicated on low volatility and cheap yen funding appear to have been unwound."；"the magnitudes of exchange rate changes were not outsized when compared to past well-known carry crashes"
- 套息吸引力："carry-to-risk ratios, which peaked in the first quarter of 2024, before policy tightening commenced in Japan"

### S2. BIS Quarterly Review 2007-09 — Galati, Heath, McGuire，"Evidence of carry trade activity"，pp 27–41
- URL：https://www.bis.org/publications/evidence-carry-trade-activity_1.pdf （旧链接 https://www.bis.org/publ/qtrpdf/r_qt0709e.pdf 跳转至 https://www.bis.org/publications/evidence-carry-trade-activity）
- 定义："A currency carry trade is usually defined as a leveraged cross-currency position designed to take advantage of interest rate differentials and low volatility."
- 1998："the sharp appreciation of the yen against the US dollar between 6 and 8 October 1998, following a prolonged period of depreciation. This was the sharpest move in major foreign exchange rates since 1974 ... one-month implied volatility reached 40%"；"despite the lack of an apparent trigger"
- 融资/目标货币："the yen and the Swiss franc are the most commonly cited funding currencies ... The Australian dollar, the New Zealand dollar and sterling ... popular target currencies ... (eg the Brazilian real and the South African rand). Since 2004 ... the US dollar has moved from being a funding currency to a potential target."
- 参与者："Traditionally, carry trades are used by large financial institutions, such as hedge funds and commodity trading advisors (CTAs)"
- 渡边太太（外为 Gaitame 一家）："the number of accounts it manages increased from less than 2,000 at the beginning of 2003 to almost 120,000 in June 2007, with deposits worth almost 90 billion yen ($0.7 billion)"；"the size of these investors in aggregate is still relatively small"
- 投信（toshin）与非杠杆区分："It is useful to distinguish the leveraged carry trades ... from two other investment strategies"；"foreign currency investments made by Japanese households through investment trust funds, which increased on average by 1.2 trillion yen per month in the first six months of 2007, pushing the stock of such investments to 35 trillion yen"；uridashi 债券 = "Debt issued outside Japan and registered under Japanese securities laws for sale to Japanese investors"
- 东欧外币房贷："Swiss franc-denominated mortgages have become popular in some central and eastern European countries. However, unlike the leveraged carry trades of larger institutions, these types of foreign currency exposures are less likely to be unwound quickly"
- BIS 银行统计（口径极宽，不等于套息）："Total yen-denominated claims reached $1.05 trillion in the first quarter of 2007, just shy of their most recent peak in the fourth quarter of 2005"；同期瑞郎 "$678 billion"
- 流向离岸中心："the largest net flows of yen over this five-year period were from Japan to the Caribbean financial centres ($45 billion)"（2002Q2–2007Q1 累计）；但 "it is impossible to distinguish them from other types of activity, for example purchases of securities issued by special purpose vehicles. In any event, these yen flows were relatively small"
- 经银行间市场流出："since mid-2004, an estimated $76 billion has been channelled from Japan through the interbank market to banks in these areas"（英国+欧元区）
- 机制解释："banks have sold borrowed yen in the swap market to square forward purchases of yen from leveraged counterparties that were shorting the currency."
- CFTC 口径警告："only a very small proportion of foreign exchange market activity is executed through exchanges."
- 结论："the available data do not allow for a more refined measurement of the size of carry trade positions."

### S3. 日本央行（BOJ）政策利率时间线 — 全部来自 BOJ 官网原始声明（已逐份打开）
| 决议日 | 内容（原文关键句） | URL |
|---|---|---|
| 1999-02-12 | 零利率（ZIRP）："encourage the uncollateralized overnight call rate to move as low as possible ... initially aim to guide the above call rate to move around 0.15%" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_1999/k990212c.htm |
| 2000-08-11 | 退出零利率："encourage the uncollateralized overnight call rate to move on average around 0.25%" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2000/k000811.htm |
| 2001-03-19 | 量化宽松（QE）：操作目标改为准备金账户余额 "around 5 trillion yen"，预期隔夜利率 "stay close to zero percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2001/k010319a.htm |
| 2006-03-09 | 结束 QE："encourage the uncollateralized overnight call rate to remain at effectively zero percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2006/k060309.htm |
| 2006-07-14 | 加息："remain at around 0.25 percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2006/k060714.pdf |
| 2007-02-21 | 加息："remain at around 0.5 percent"（2007 套息高峰期的日本利率） | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2007/k070221.pdf |
| 2008-10-31 | 降息 20bp 至 "around 0.3 percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2008/k081031.pdf |
| 2008-12-19 | 降至 "around 0.1 percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2008/k081219.pdf |
| 2010-10-05 | 全面宽松（CME）："remain at around 0 to 0.1 percent" | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2010/k101005.pdf |
| 2016-01-29 | 负利率："apply a negative interest rate of minus 0.1 percent to current accounts"（5–4 票；自 2016-02-16 起的准备金维持期生效） | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2016/k160129a.pdf |
| 2024-03-19 | 结束负利率与 YCC："encourage the uncollateralized overnight call rate to remain at around 0 to 0.1 percent"（2024-03-21 生效，7–2 票） | https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240319a.htm |
| 2024-07-31 | 加息至 "around 0.25 percent"（7–2 票，2024-08-01 生效），同时宣布缩减购债至 2026Q1 约 3 万亿日元/月 | https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240731a.htm |
| 2025-01-24 | 加息至 "around 0.5 percent"（8–1 票，2025-01-27 生效） | https://www.boj.or.jp/en/mopo/mpmdeci/state_2025/k250124a.htm |
| 2025-12-19 | 加息至 "around 0.75 percent"（全票，2025-12-22 生效） | https://www.boj.or.jp/en/mopo/mpmdeci/state_2025/k251219a.htm |
| 2026-06-16 | 加息至 "around 1.0 percent"（7–1 票，2026-06-17 生效） | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf |
| 2026-09-18 | 加息至 "around 1.25 percent"（7–2 票，2026-09-24 生效）——**截至 2026-10-15 的最新政策利率 = 1.25%** | https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf |
- 2026 年 1/3/4/7 月为维持不变（BOJ 2026 声明索引：https://www.boj.or.jp/en/mopo/mpmdeci/state_2026/index.htm ，2026-10-15 查阅）。
- 2026-09-18 声明提到日元贬值仍是通胀推手之一："reflecting the impact of the expansion in AI-related demand, in addition to high crude oil prices and the depreciation of the yen."

### S4. 美联储 IFDP No 899 — Gagnon & Chaboud，"What Can the Data Tell Us about Carry Trades in Japanese Yen?"，2007-07
- URL：https://www.federalreserve.gov/pubs/ifdp/2007/899/ifdp899.pdf
- 定义（中间口径）："We define an individual or a sector to be engaged in the carry trade if it has a short position in yen and a long position in other currencies."；"A common characteristic of carry trades under this definition is that they are leveraged."
- 两条通道："1) borrowing in low-interest currencies and investing the proceeds in high-interest currencies, which we term the 'canonical carry trade;' and 2) taking on leveraged positions in derivatives markets ... which we term the 'derivatives carry trade.' The realized profit from either channel is identical"（由抛补利率平价保证）
- 三次公认平仓："October 1998, immediately after the LTCM crisis, as many banks were reported to be cutting back on the leverage of their hedge fund clients"；另两次 "May 2006 and February 2007"；"the October 1998 episode ... contained the largest ever one-day movement of the dollar-yen exchange rate"
- 不对称尾部："For the yen ... the frequency of tail events is clearly higher for appreciations than for depreciations. For the Australian dollar ... tail events are more common for depreciations"
- **关键结论（谁承担了汇率风险）**："The Japanese official sector has a net yen carry position of $875 billion. The Japanese banking sector has a net yen carry position of $40 billion. The Japanese private non-banking sector has positive net foreign-currency assets of around $1.3 trillion. However, the position of the private non-banking sector cannot be considered a carry position, because the sector is not leveraged; it is net long yen assets by an even larger magnitude."（数据截至 2006 年末）
- 境外非银行部门（对冲基金等）资产负债表上限："gross canonical yen carry trades by the private non-banking sector outside of Japan surely total less than the $300 billion displayed in Chart 7."
- 日本银行业对外日元净债权："Net claims in yen were nearly $300 billion in 1996, fell to $200 billion by the middle of 1998, turned slightly negative in 2004, and have since rebounded to just over $100 billion."
- 衍生品通道无数据："There are no published data on the magnitude of the yen carry trade through derivatives markets."；推断对手方："Possible sources of supply are Japanese exporters and Japanese households holding foreign-currency assets, both of whom may wish to hedge ... Sources of demand for yen carry positions include hedge funds, pension funds, investment banks, charitable endowments, and individual investors. Most of the demand ... likely arises in the private non-banking sector outside of Japan."
- 渡边太太规模（2007）："Typical estimates of gross open retail foreign exchange positions in Japan are well under $100 billion, so that this sector is not short yen in the aggregate."
- CFTC 数据可靠性："the sharp movement to a net long yen position in late 1998 occurred more than a month before the sharp yen appreciation of October 1998"；"we are not inclined to draw broad conclusions about the existence and magnitude of carry trade behavior from these volatile data."
- 日本整体（2006 年末）："Japan had net debt claims on the rest of the world valued at $2.2 trillion"

### S5. BIS Quarterly Review 1999-03（International banking and financial market developments），第 V 节 "The yen carry trade and recent foreign exchange market volatility"（Béranger, Galati, Tsatsaronis, von Kleist 撰），pp 33–37
- URL：https://www.bis.org/publications/qr-199903_1.pdf （旧链接 https://www.bis.org/publ/r_qt9902.pdf 跳转至 https://www.bis.org/publications/qr-199903）
- 起点："The yen carry trade has reportedly been a fairly widespread strategy since the yen started its declining trend in the spring of 1995. Investors could borrow cheaply in the Japanese money market and invest the proceeds in a wide array of assets ranging from US Treasuries to high-yielding emerging market securities."
- 去向（亚洲）："in 1996 and early 1997 high interest rates in East Asian money markets and stable dollar exchange rates attracted much of these funds. This strategy paid off as long as the yen did not appreciate and other East Asian currencies remained firmly pegged to the US dollar."（借日元投泰铢货币市场，直到 1997-05 泰铢承压）
- 实现方式：远期卖出、"a synthetic forward transaction ... outright sale of the currency in the spot market and a swap of the proceeds"、卖空借来的证券。
- **1998 年两段升值**："the dollar fell by about 9% in the period between 31 August and 7 September, and then by a further 12% on 7 and 8 October. Market commentary attributed these movements (at least partially) to the unwinding of yen carry trades by hedge funds and other institutional investors."
- 背景（政策预期转向）："In early October, there were signs of a substantial shift in the relative stance of policy in Japan and abroad ... central banks in the United States and Europe were inclined to accommodate financial markets' liquidity needs."
- 老虎基金："the fund [Jaguar Fund, Tiger Management] had substantial short yen positions and suffered losses of about 12% in the course of a couple of days. The financial press reported that losses were as high as $2 billion"
- 平仓规模（标注为市场传闻）："market observers suggested that the US hedge fund began unwinding a massive $35 billion long dollar/yen position, of which around $10 billion was offloaded in the market overnight. Other sources estimated that unwound carry trades amounted to between $8 and 10 billion."
- 规模（早期估算）：脚注 48 "McCauley and von Kleist estimated the amount of outstanding yen carry trades channelled through vehicles registered in the Cayman Islands in early 1998 at between $20 billion and $30 billion ... A currency strategist quoted in the financial press estimated yen short positions at $40-50 billion in early January 1998."
- 数据局限："it is difficult to provide empirical estimates on the magnitude of the yen carry trade ... no such data are available."
- 1995→1998 日元成交额增长 37%（不变汇率），美元 33%、全球 ... （见原文表）。

### S6. BIS Quarterly Review 2024-09（2024-09-16），Box D "Sizing up carry trades in BIS statistics"
- URL：https://www.bis.org/publ/qtrpdf/r_qt2409y.htm （跳转 https://www.bis.org/publications/sizing-carry-trades-bis-statistics）
- 主流实现方式："The more common approach used by hedge funds and other speculators relies on derivatives – eg FX forwards, swaps and options ... Since the use of derivatives requires no on-balance sheet borrowing of the funding currency, it is difficult to trace the trade in the statistics."
- 最宽口径（不等于套息）："Banks' yen-denominated claims ... on non-banks resident outside of Japan reached $880 billion, or ¥133 trillion, in Q1 2024 (up from ¥110 trillion in Q4 2021). The bulk of these claims are on borrowers in the Cayman Islands ... Such financing structures, however, have been in place for decades ... so that they may not be related to speculative carry trade positions."
- 贷款口径："Outstanding amounts rose from $228 billion (¥25 trillion) in Q2 2021 to $271 billion (¥41 trillion) in the most recent data for Q1 2024 ... mainly to borrowers located in the United Kingdom, the Cayman Islands and the United States. Without more detailed data, however, it remains unclear whether this relates to carry trades."
- 衍生品总量（绝大多数是对冲）："the notional value of outstanding FX swaps, forwards and currency swaps with the yen on one side has grown to $14.2 trillion (¥1,994 trillion) by end-2023 ... The bulk of these are used for hedging and liquidity management"
- **日本机构对冲 = 日元供给方**："Japanese banks are natural suppliers of yen via FX derivatives ... they have a domestic yen deposit base but hold portfolios of foreign currency assets and use FX swaps to hedge the currency risk."；信托账户 "$2.7 trillion at end-Q1 2024 ... Assuming 80% of these holdings are hedged ... supply of yen via FX derivatives reached $1.7 trillion (¥254 trillion)"
- 净日元供给（被未观测非银吸收）："The measure rose by ¥66 trillion between end-2021 and Q1 2024, or $435 billion at Q1 2024 exchange rates, coinciding with a significant depreciation of the yen"

### S7. NBER WP 14473 — Brunnermeier, Nagel, Pedersen，"Carry Trades and Currency Crashes"，2008-11
- URL：https://www.nber.org/system/files/working_papers/w14473/w14473.pdf
- 摘要："carry traders are subject to crash risk: i.e. exchange rate movements between high-interest-rate and low-interest-rate currencies are negatively skewed. We argue that this negative skewness is due to sudden unwinding of carry trades, which tend to occur in periods in which risk appetite and funding liquidity decrease."
- 1998 无新闻崩盘："dramatic exchange rate movements occasionally happen without fundamental news announcements, e.g. the large depreciation of the US Dollar against the Japanese Yen on October 7th and 8th of 1998"；脚注："While the LTCM debacle, which occurred between end-August and early-September 1998, is not completely unrelated, it is quite distinct from the US Dollar/Japanese Yen crash on October 7th and 8th 1998 ... the Fed's surprise interest rate cut of .5 percent happened only on October 15th."
- VIX 机制："an increase in global risk or risk aversion as measured by the VIX ... coincides with reductions in speculator carry positions (unwind) and carry-trade losses"
- 偏度谱："skewness is positive and highest for Japanese Yen (a 'funding currency')"，另一端是澳元/新西兰元（投资货币）。

### S8. BOJ IMES Discussion Paper 2007-E-19 — Hattori & Shin，"The Broad Yen Carry Trade"，2007-10（后刊于 IMF Staff Papers 2009 vol 56 no 2，题为 "Yen Carry Trade and the Subprime Crisis"）
- URL：https://www.imes.boj.or.jp/research/papers/english/07-E-19.pdf
- 机制（银行间/总分行通道）："A bank with global reach can borrow yen through its Tokyo office. The Tokyo office of the Wall Street bank then has yen liabilities to Japanese banks, but has yen assets against its New York head office ... captured in its 'interoffice' accounts, and reported to the Bank of Japan."
- "Yen liabilities fund not only pure currency carry trades, but also fund the general increase in balance sheets of hedge funds and financial intermediaries."
- 2007 平仓："in the period leading up to the credit crisis of 2007, yen liabilities of foreign banks surged, leading to an unprecedented net short position in Japanese assets ... These net short positions were sharply unwound in August 2007, coinciding with the peak of the credit crisis of 2007."
- 政策含义："Domestic monetary policy thus has a global dimension."

### S9. AMRO Analytical Note，"Understanding Currency Carry Trades: The Yen Carry Trade and Its Impact on ASEAN+3 Economies"，2024-12-19
- URL：https://amro-asia.org/wp-content/uploads/2024/12/20241219-Analytical_Note_Carry_Trade.pdf
- 2024-08 幅度："the JPY appreciated by around 5.6 percent against the USD between July 30 and August 5"；"the Mexican peso (MXN) depreciated sharply by around 3.2 percent between July 30 to August 5"
- 跨境日元贷款："around 41 trillion yen as of June this year ... as compared to 27 trillion yen in March 2021"
- 离岸中心："total yen-denominated claims to offshore financial centers from all banks amount to approximately 579 billion USD ... the Cayman Islands ... 530 billion USD"
- 中国敞口："yen-denominated loans and debt securities borrowed by the non-bank sector in China account for 3.4 percent of total yen-denominated loans and debt securities worldwide, the largest share among the economies with available data"
- 2024-08 期间："Malaysia ringgit, Thai baht, and offshore RMB showed significant appreciation"

### S10. 美联储 H.10 每日中午买入汇率（原始数据，本人下载计算）
- 来源：https://www.federalreserve.gov/releases/h10/hist/dat96_ja.htm （1990–1999）、https://www.federalreserve.gov/releases/h10/hist/dat00_ja.htm （2000–，页面 Release Date 2026-10-13，数据至 2026-10-09）；澳元 dat96_al / dat00_al，新西兰元 _nz，墨西哥比索 _mx。AUDJPY = AUDUSD × USDJPY（交叉计算）。（FRED 在本机超时，故改用 H.10 原始页面。）
- 注意：H.10 是纽约中午报价，不是日内极值；与 BIS 文中"7–8 Oct 跌 12%"等数字口径不同。

| 事件 | 序列 | 高点（日期，值） | 低点（日期，值） | 外币兑日元跌幅 |
|---|---|---|---|---|
| 1998 | USDJPY | 1998-08-11 147.14 | 1999-01-11 108.83 | −26.0% |
| 1998 | AUDJPY | 1998-04-06 88.84 | 1999-01-05 69.10 | −22.2% |
| 1998 单周 | USDJPY | 1998-10-05 134.54 → 10-06 131.15 → 10-07 123.97 → 10-08 118.85 → 10-09 117.00 | | 10-05→10-09 −13.0%（三个交易日 10-05→10-08 −11.7%） |
| 2007–09 | USDJPY | 2007-06-22 124.09 | 2009-01-21 87.80 | −29.2% |
| 2007–09 | AUDJPY | 2007-07-19 107.36 | 2008-10-27 56.65 | −47.2% |
| 2007–09 | NZDJPY | 2007-07-24 97.53 | 2009-02-02 45.16 | −53.7% |
| 2007–09 | MXNJPY | 2007-06-22 11.50 | 2009-02-03 6.11 | −46.9% |
| 2007-08 次贷首波 | AUDJPY | 2007-08-15 96.60 → 2007-08-16 89.63 | | 单日 −7.2% |
| 2008-10 雷曼后 | AUDJPY | 2008-10-01 84.18 → 2008-10-27 56.65 | | 一个月 −32.7% |
| 2024 | USDJPY | 2024-07-10 161.73 | 2024-08-05 143.95（中午价）；2024-09-13 140.66 | 至 08-05 −11.0%；至 09-13 −13.0% |
| 2024 | AUDJPY | 2024-07-10 109.12 | 2024-08-05 93.39 | −14.4% |
| 2024 | MXNJPY | 2024-07-10 9.07 | 2024-09-10 7.08 | −21.9% |
| 2026 夏 | USDJPY | 2026-07-29 163.86（高于 2024 峰值） | 2026-09-09 153.50 | −6.3%；2026-10-09 回到 158.34 |

### S11. CFTC Commitments of Traders（Legacy，期货，CME 日元合约代码 097741；原始年度文件本人下载计算）
- 来源：https://www.cftc.gov/files/dea/history/deacot1986_2016.zip 及 deacot2017.zip … deacot2026.zip（数据至 2026-10-06）
- 口径：非商业（non-commercial）多头 − 空头，合约 = 1250 万日元。这是 BIS 所说"冰山一角"（场内期货），不是套息总量。
- 有记录以来最大净空头：**2007-06-26，−188,077 张 ≈ ¥2.35 万亿**（未平仓 352,299）。
- 2024 峰值：**2024-07-02，−184,223 张 ≈ ¥2.30 万亿**（与 BIS Bulletin 90 "around ¥2 trillion" 一致）。到 2024-08-06 降至 −11,354；2024-08-13 转为净多 +23,104；2024-09-24 净多 +66,011。
- 2007 平仓路径：2007-06-26 −188,077 → 07-31 −51,162 → 08-14 −21,889 → 08-21 **+1,516（转净多）**。
- 1998：年内最大净空 1998-05-26 −63,478（≈¥0.79 万亿）；1998-08-25 −41,682 → 09-08 已转净多 +8,430 → 10-06 +7,826。即：期货投机者在 10 月 7–8 日暴涨前一个月已转多（与 Gagnon & Chaboud 观察一致）；10 月的暴涨更多来自场外/资产负债表头寸（老虎基金等）。
- 2008：全年净空最多仅 −23,138（2008-08-19），9 月起转净多 —— 2007 下半年已大幅平仓。
- **2026（截至最新）**：2026-07-28 净空 −163,412（≈¥2.04 万亿，接近 2007/2024 峰值量级）→ 2026-08-04 −45,473 → 2026-09-01 −92,227 → 2026-09-15 **净多 +120,359** → 2026-10-06 净多 +62,325。也就是说，2026 年 7–9 月期货市场又发生了一轮"空日元"头寸的快速了结（伴随 USDJPY 从 163.86 回落到 153.50，幅度远小于 2024）。原因本笔记未查证，不作推断。

### S12. 日经 225 在 2024-08-05 的跌幅 — The Japan Times，Elizabeth Beattie，"Nikkei plunges by 12% as it registers largest-ever point fall"，2024-08-05
- URL：https://www.japantimes.co.jp/business/2024/08/05/markets/nikkei-plunge/ （WebFetch 遇付费墙，经内置浏览器打开）
- 原文："At the close Monday, the benchmark index was down 4,451.28 points, or 12.40%, to 31,458.42."
- 搜索摘要称这是点数上最大单日跌幅，百分比上次于 1987-10-20 的 14.9%（Nikkei Asia）—— **该"次于 1987"的说法我未打开原文核实**，仅作背景。

### S13. BOJ 副行长内田真一 函馆讲话，2024-08-07（平仓中的政策转向）
- URL：https://www.boj.or.jp/en/about/press/koen_2024/ko240807a.htm
- 承认套息平仓："the yen has appreciated significantly against the U.S. dollar, since large positions that had been built up on a weaker yen are being unwound. Moreover, partly due to the correction of the yen's depreciation, stock prices in Japan have declined to a greater extent than other economies."
- 关键承诺："Therefore, the Bank will not raise its policy interest rate when financial and capital markets are unstable."；"the Bank needs to maintain monetary easing with the current policy interest rate for the time being"
- 含义：融资货币央行主动"放缓加息"是 2024 年平仓迅速止住的原因之一（BIS 称到 8-09 美股已收复全部跌幅）。

### S14. BOJ Financial System Report 2024-10（2024-10-24），Box 1 "Volatility in financial and foreign exchange markets at the beginning of August 2024"
- URL：https://www.boj.or.jp/en/research/brp/fsr/data/fsr241024a.pdf （索引页 https://www.boj.or.jp/en/research/brp/fsr/fsr241024.htm）
- "the yen had recently been under depreciation pressure due to yen carry trades from which investors have attempted to take advantage of the yield differential between Japan and the United States ... the net yen short position reached a record high in early July 2024 ... However, the yen carry positions were rapidly unwound partly due to the global depreciation of the dollar amid heightened concerns over a slowdown in the U.S. economy and to the changes in the Bank's monetary policy at the end of July."
- 股市放大器："follow-on selling by foreign investors ... and loss-cutting by individual investors engaged in margin trading"；"investors who exceeded risk limits closed positions across a wide range of assets"
- 美国科技股估值背景："the price-earnings (P/E) ratios of major high-tech firms had hovered at high levels relative to current market and historical averages, driven by expectations for a spread of generative artificial intelligence (AI)"

### S15. BOJ Review 2008-E-3 — Terada, Higashio, Iwasaki，"Recent Trends in Japanese Foreign-Exchange Margin Trading"，2008-09（"渡边太太"官方数据）
- URL：https://www.boj.or.jp/en/research/wps_rev/rev_2008/data/rev08e03.pdf
- 成交量："the market has more than quadrupled from just over 50 trillion yen during the first quarter of 2006 to 230 trillion yen during the first quarter of 2008"；日均 2008Q1 "3.6 trillion yen per day (14.5%)" 相当于全球日元即期成交的比重。
- **存量很小**："as of the end of March 2008, on a stock basis, foreign-exchange margin trading had an outstanding balance (gross positions) of 3.1 trillion yen. This was significantly smaller than the balance on foreign-currency-denominated investment trusts (32.1 trillion yen) ... smaller than outstanding household outward investment in securities (12.2 trillion yen) and foreign currency deposits (4.8 trillion yen)"
- 行为特征（逆势）："retail players appear to primarily take contrary positions, buying into declines and selling into gains"
- 2007-08 平仓："During 2007, and particularly in July and early August, Japanese margin trading saw a surge in carry trades ... Of particular note is August 16, the date on which the dollar/yen rate plummeted through 115 yen. Large numbers of foreign-exchange margin positions were liquidated under automatic loss cutting rules ... viewed as a factor in accelerating the appreciation of the yen"
- 杠杆：平均杠杆 2007Q2 约 8.5 倍 → 2007Q3 明显下降（图 7）："average leverage at the third quarter of 2007 was noticeably lower than the second quarter of 2007"
- 投信（toshin）定位："trading through investment trusts is considered to have a relatively large influence from the perspective of a long-term supply and demand for currencies. Meanwhile, foreign-exchange margin trading has a relatively large impact on short-term market movements"

### S16. 日本金融先物取引业协会（FFAJ）店头外汇保证金月度统计（原始 Excel，本人下载计算）
- 页面：https://www.ffaj.or.jp/library/performance/fx_flash （2026-10-15 查阅）；文件：https://www.ffaj.or.jp/wp-content/uploads/2026/10/trading_vol_and_position.xls （更新日 2026-10-13，数据 2008-11 至 2026-09；单位百万日元）
- 口径："全通貨ペア合計"的"買建"（多头）对 XXX/JPY 即"多外币、空日元"；但合计里也含 EUR/USD 等非日元货币对，所以只是近似。以下"净多"= 买建 − 卖建（基准货币，正值≈散户净空日元）。
| 月末 | 月成交额 | 建玉合计（未平仓总额） | 净多（≈净空日元） | 其中 USD/JPY 净多 |
|---|---|---|---|---|
| 2008-12 | ¥129 万亿 | ¥1.23 万亿 | +¥0.23 万亿 | +¥0.01 万亿 |
| 2020-12 | ¥542 万亿 | ¥7.47 万亿 | +¥1.59 万亿 | +¥2.20 万亿 |
| 2024-06 | ¥1,120 万亿 | ¥8.66 万亿 | −¥0.43 万亿 | −¥0.37 万亿 |
| 2024-07 | ¥1,455 万亿 | ¥8.62 万亿 | +¥1.85 万亿 | +¥1.20 万亿 |
| 2024-08 | ¥1,448 万亿 | ¥7.69 万亿 | +¥0.02 万亿 | −¥0.07 万亿 |
| 2026-06 | ¥668 万亿 | ¥11.13 万亿 | −¥1.46 万亿 | −¥2.86 万亿 |
| 2026-07 | ¥882 万亿 | ¥11.96 万亿 | **+¥4.13 万亿（序列最高）** | +¥1.89 万亿 |
| 2026-09 | ¥1,227 万亿 | ¥11.72 万亿 | +¥3.04 万亿 | +¥0.87 万亿 |
- 观察：(1) 散户总未平仓仅约 ¥8–12 万亿，远小于 BIS 估计的 ¥40 万亿量级的整体套息；(2) 散户呈明显"逆势"特征：2024-06 日元最弱时散户反而净空美元/日元，2024-07 日元开始升值时才转为净多外币（=接飞刀），8 月被迫了结——与 BOJ 2008 Review 描述的"buying into declines"一致；(3) 2026-07 散户净多外币达到 ¥4.13 万亿的序列最高值，USD/JPY 同月见顶 163.86 后回落。

### S17. RBNZ Bulletin Vol 68 No 3 — Drage, Munro, Sleeman，"An update on Eurokiwi and Uridashi bonds"，2005-09-01
- URL：https://www.rbnz.govt.nz/hub/publications/bulletin/2005/rbb2005-68-03-03 （摘要页，经内置浏览器打开；PDF 对 curl/WebFetch 返回 403）
- "Net issuance of these bonds has surged in the past two years, driven by strong demand for credit in New Zealand (high domestic interest rates) and by supply conditions internationally (low yields in Europe and Japan). Offshore issuance of New Zealand dollar bonds provides an important channel for New Zealand firms and households to access foreign capital"
- "Ex-post returns on Eurokiwi bonds that had matured by the end of 2004 were on average the same, in euros, as German government bonds, but more variable, reflecting exchange rate risk."
- 含义：uridashi 是日本散户**用自己的储蓄**买高息外币债，汇率风险由日本散户承担；它不是"借日元"，不带杠杆——属于 Galati 等（S2）所说的"组合分散"而非杠杆套息。

### S18. 日本财务省（MOF）International Investment Position of Japan（End of 2025）
- URL：https://www.mof.go.jp/english/policy/international_policy/reference/iip/e2025.htm
- "Total assets 1,805,634"；"Total liabilities 1,243,884"；"Net international investment position 561,750"（单位：十亿日元）
- 排名（Jiji Press，经 Adnkronos 转载，2026-05-26，https://english.adnkronos.com/2026/05/26/japan-falls-to-3rd-in-net-external-assets-after-germany-china/ ）："grew 4.4 pct from a year before to 561,750.4 billion yen"；Japan "fell from second to third place in the world"；"Germany's net external assets at the end of 2025 came to 675,537.4 billion yen"，"followed by China's 636,339.1 billion yen"（按 IMF 汇率）。
- 含义：日本是长期巨额净债权国——汇率风险主要由日本居民（持有外币资产者）承担；"套息"的融资货币恰恰来自一个储蓄过剩国。中国同样是净债权国（2025 年末约 ¥636 万亿），这一点结构上与日本相似。

### S19. GPIF（日本年金公积金）
- 资产配置（第五期中期目标，FY2025–FY2029）：国内债/外国债/国内股/外国股 = 25%/25%/25%/25%；外债基准 "FTSE World Government Bond Index (excluding Japan, excluding China, unhedged, yen basis)"；"Yen-denominated short-term assets and currency-hedged foreign bonds should be [classified as domestic bonds]"。URL：https://www.gpif.go.jp/en/topics/Adoption_of_New_Policy_Portfolio_details_2_en.pdf
- 规模（FY2025 年末 = 2026-03 末）：总资产 "¥293,643.7 billion"；外国债券 "¥73,399.0 billion"，外国股票 "¥74,356.9 billion"。URL：https://www.gpif.go.jp/en/performance/73509681gpif/annual_report_summary_2025_en.pdf
- 含义：GPIF 持有约 ¥148 万亿未对冲外币资产，资金来自养老金储备，不是借日元——它承担汇率风险，但没有保证金追缴，不会被强平；与对冲基金的杠杆套息性质不同。

### S20. 奥地利金融市场管理局（FMA），Q3 2012 外币贷款季度调查，2012-11-22（日元房贷在欧洲的真实体量）
- URL：https://www.fma.gv.at/en/fma-q3-2012-quarterly-survey-on-changes-in-foreign-currency-loans/
- "the total share of lending to domestic households in foreign currencies amounted to 25.3%"；"€ 33.4 billion had still to be repaid"；"the majority (92.9%) of outstanding foreign currency loans is denominated in Swiss francs"，其余几乎全是日元。
- 2008 秋 FMA 禁止新发外币贷款："Austria's Financial Market Authority announced its prohibition on the granting of new foreign currency loans"
- 推算（本人计算，非原文）：日元部分 ≈ €33.4bn × (1−92.9%) ≈ €2.4bn —— 欧洲家庭外币贷款以瑞郎为主，日元是小头。
- 匈牙利/波兰：本次检索未找到可靠的"日元房贷"官方数据；Galati 等（S2）描述的东欧家庭外币房贷主要是瑞郎（"Swiss franc-denominated mortgages have become popular in some central and eastern European countries"）。**"东欧大规模日元房贷"属于常见但缺乏官方数据支撑的说法。**

### S21. 美联储联邦基金利率目标（官方表）与日美政策利差
- URL：https://www.federalreserve.gov/monetarypolicy/openmarket.htm （2026-10-15 抓取）；1990s：https://www.federalreserve.gov/monetarypolicy/openmarket_archive.htm
- 1997-03-25 升至 5.50%；1998-09-29 降至 5.25%；1998-10-15 降至 5.00%；1998-11-17 降至 4.75%。BOJ 1998-09-09："encourage the uncollateralized overnight call rate to move on average around 0.25%"（https://www.boj.or.jp/en/mopo/mpmdeci/mpr_1998/k980909c.htm ）
- 2006-06-29 升至 5.25%（维持至 2007-09-18 降至 4.75%）；2008-12-16 降至 0–0.25%。
- 2023-07-27 升至 5.25–5.50%（维持至 2024-09-19 降至 4.75–5.00%）。
- 2025-12-11 降至 3.50–3.75%；**2026-09-17 升 25bp 至 3.75–4.00%**（表中 2026 年唯一一次变动）。
| 时点 | 美国政策利率 | 日本政策利率 | 利差（约） |
|---|---|---|---|
| 1998 年 8 月（平仓前） | 5.50% | ~0.25–0.5%（9-09 起 0.25%） | ~5.0–5.25pp |
| 2007 年 6 月（峰值） | 5.25% | 0.5%（2007-02-21 起） | ~4.75pp |
| 2024 年 7 月（峰值） | 5.25–5.50% | 0–0.1% → 7-31 升至 0.25% | ~5.1–5.4pp |
| 2026 年 10 月（当前） | 3.75–4.00% | 1.25%（2026-09-24 起） | ~2.5–2.75pp |
- 观察：三次大平仓都发生在利差 ≈5pp、且利差**开始收窄（或市场预期收窄）**之时：1998 年美联储开始降息、2007 年 9 月美联储开始降息、2024 年 BOJ 加息+美联储降息预期。

### S22. 日本财务省外汇干预（官方数据）
- 2024 Q3：https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2024_3Qe.html —— "Total amount ... from July through September 2024: ¥5,534.8 billion"；"July 11, 2024 ¥3,167.8 billion"，7-12 ¥2,367.0bn（卖美元买日元）。即 BIS 所说"rumoured Bank of Japan interventions"实为财务省 7-11/12 两天买入 ¥5.53 万亿日元，正是 USDJPY 见顶（7-10 161.73）后的第一推。
- 2026 Q2：https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2026_2Qe.html （发布 2026-08-07）—— "¥11,734.9 billion"：2026-04-30 ¥6,278.7bn、05-04 ¥780.2bn、05-06 ¥4,675.9bn（均为卖美元买日元）。
- 2026-07-30 至 08-26：https://www.mof.go.jp/english/policy/international_policy/reference/feio/monthly/20260828e.html —— "¥ 15,399.3 billion"。2026-08-27 至 09-28：¥0（https://www.mof.go.jp/english/policy/international_policy/reference/feio/monthly/20260930e.html ）。
- 财务大臣片山皋月声明，2026-08-03（https://www.mof.go.jp/english/public_relations/statement/others/20260803073000.html ）："On Friday 31st, July (U.S. Eastern Time), Japan's Ministry of Finance purchased the Japanese yen in coordination with the U.S. Department of the Treasury."；"We will not hesitate to conduct further joint intervention."
- 含义：2026 年日元在 BOJ 加息到 1.0–1.25% 的同时仍贬到 163.86（7-29），日本当局 2026 年至今累计买入日元约 ¥27 万亿（11.73 + 15.40），包括一次美日联合干预；CFTC 投机净空随之在 8–9 月了结并转为净多（S11）。

### S23. 当前背景（新闻，仅作时间点参照）：The Japan Times，Kazuaki Nagata，"Nikkei 225 falls 5% on rate and AI concerns"，2026-10-15
- URL：https://www.japantimes.co.jp/business/2026/10/15/nagata-nikkei-decline/
- "At about 1 p.m., the Nikkei 225 hit the low for the day of 64,092.74, down 5.39%."；"September's inflation was 3.7%"（美国）；"The yield on the 10-year Japanese government bond fell to 2.93%"；"While the Japanese yen was trading near ¥159 to the dollar on Wednesday night, the currency moved below ¥158 on Thursday."
- 观察：今天的下跌由美国通胀/科技股驱动，日元只升值约 0.6%——与 2024 年（H.10 中午价：USDJPY 7-10 161.73 → 8-05 143.95，日元约四周内升值约 12%）形态不同；不宜把每次日股下跌都归为"套息平仓"。

### S24. BIS Papers No 15，"China's capital account liberalisation: international perspectives"，2003-04（BIS/SAFE 北京研讨会 2002-09-12/13），其中深尾光洋（Mitsuhiro Fukao）"Capital account liberalisation: the Japanese experience and implications for China"
- URL：https://www.bis.org/publications/paper-15-chinas-capital-account-liberalisation-international-perspective.pdf （旧链接 https://www.bis.org/publ/bppdf/bispap15h.pdf 跳转）
- 1980 新外汇法："This law changed the basic principle behind foreign exchange control in Japan from that of 'prohibition of foreign transactions with exceptions' to 'freedom of transactions with exceptions'."（1980-12 实施）
- 时间跨度（编者综述）："From 1971, when there was partial deregulation of foreign exchange control, to Japan's new foreign exchange law of 1980, when onshore and offshore yen money market yields were equalised, took nine years. Another eight years passed before the limits on foreign securities holdings by institutional investors were raised enough to become non-binding. And another eight years intervened before the 1996 'big bang' liberalisation."
- 对中国："depending on the milestone used, at Japan's pace, China could be 10, 15 or 25 years away from effective and full capital account liberalisation."（2003 年的判断）
- 含义：日元套息之所以能做大，前提是**境内外日元利率打通（1980 后 euroyen ≈ gensaki）+ 外资银行可在东京同业市场借日元 + 深度远期/掉期市场**。
- 数据补充（H.10，本人计算）：三轮套息累积期日元都在贬值——1995-04-19 USDJPY 81.12 → 1998-08-11 147.14（美元 +81%）；2005-01-12 102.26 → 2007-06-22 124.09（+21%）；2021-01-05 102.70 → 2024-07-10 161.73（+57%）；2025-04-21 140.81 → 2026-07-29 163.86（+16%）。
