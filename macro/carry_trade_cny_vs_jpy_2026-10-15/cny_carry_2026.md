# 人民币套息交易（CNY/CNH carry trade）是真的吗？——2026-10-15 核查

> 规则：只报告亲自打开过原文的数字；每个数字附 URL + 发布日期 + 原文关键句（「」内为原文）。打不开的标"未核实"。标"我的计算"的是我根据已核实数字推算的，不是原文。
> 读取方式：WebFetch 或内置浏览器直接打开原文。Bloomberg（人机验证页）、CNBC（403）、SWIFT（403）、TMA（需先接受条款页）没能打开，涉及它们的内容只用二手转述，并单独标注。

---

## 一句话结论

**"人民币成了便宜的融资货币"是真的；"像日元那样，外资大规模借人民币去买美元资产的套息交易已经开始"，证据很弱，大半是卖方的说法。**
- 真实发生、规模大的有三件事：①中资和外资发熊猫债/点心债、借人民币贷款，2026 年两项发行都创了纪录；②中国企业手里留着美元不结汇（麦格理估计超 8000 亿美元）；③内地资金出海买外国债券（2026 上半年 1199 亿美元）。
- 但①大多是中资发行人，或者做了货币掉期对冲，不是赌汇率的"裸套息"；②和③是**中国境内主体**持有美元，不是外国人借人民币。
- 真正"日元式"的那种（对冲基金借 CNH、做多美元或新兴市场货币），目前只有卖方观点、一个彭博指数 3 个月 +1.5%、期权成交量 +60% 这几条线索，**没有任何规模数据**。而且人民币自 2024 年底以来**升值近 9%**，做空人民币、做多美元的套息在 2025 和 2026 两年**都是亏钱的**。

---

## 0. 先把概念分清（最重要）

媒体说的"人民币 carry"，其实是四件不同的事：

| 类别 | 谁在做 | 怎么做 | 是不是"日元式套息" |
|---|---|---|---|
| **A. 投机型套息** | 对冲基金、外资 | 借 CNH（或做空 CNH 远期）→ 买美元或新兴市场货币吃利差 | **是**：日元套息的原型 |
| **B. 融资型** | 外国政府/企业/银行，以及中资企业 | 发熊猫债、点心债，借人民币贷款；钱留在人民币里用，或掉期换成外币 | 部分是：融资货币属性是真的，但多数不承担汇率风险 |
| **C. 企业持汇型** | 中国出口商、跨国公司 | 不结汇，留着美元吃美元利息（麦格理称其为 carry） | 不是"借人民币"，而是"不换回人民币"；平仓 = 人民币升值 |
| **D. 资本出海型** | 内地居民、机构 | 南向通、QDII、对外债券投资 | 不是套息，是资本流出找收益 |

---

## 1. 利差：中美利率对照（截至 2026-10 中旬）

| 指标 | 最新水平 | 何时到达 | 来源（原文） |
|---|---|---|---|
| 中国 7 天逆回购（主要政策利率） | **1.40%** | 2025-05 下调后未动；2026-10-13 实际操作仍是 1.40% | 新华财经 2026-10-13：「10月13日以固定利率、数量招标方式开展了650亿元7天期逆回购操作，全额满足了一级交易商需求，操作利率1.40%」 https://www.cnfin.com/zs-lb/detail/20261013/4480181_1.html ；每经/同花顺 2026-09-20：「主要政策利率(央行7天期逆回购利率)保持在1.4%」 https://news.10jqka.com.cn/20260920/c680091504.shtml |
| 1 年 / 5 年以上 LPR | **3.0% / 3.5%** | 2025-05 起连续 16 个月不变（9 月报价） | 同花顺 2026-09-20：「2026年9月20日贷款市场报价利率(LPR)为：1年期LPR为3.0%，5年期以上LPR为3.5%，均较上月保持不变」（同上链接） |
| 中国 10 年期国债（活跃券 26附息国债16） | **1.6565%**（30 年 2.083%） | 2026-10-13 | 新华财经 2026-10-13：「10年期国债"26附息国债16"收益率下行0.45BP报1.6565%」（同上 cnfin 链接） |
| CNH HIBOR 隔夜 / 7 天 / 3 个月 / 1 年 | **1.4621% / 1.4682% / 1.6361% / 1.6694%** | 2026-09-30（月末） | 中国外汇交易中心《2026年9月境外人民币市场综述》，新浪 2026-10-12 转载：「隔夜、7天、3个月和1年期CNH HIBOR分别收于1.4621%、1.4682%、1.6361%和1.6694%」 https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-10-12/doc-iniuxrzr8527460.shtml |
| CNH 1 年期掉期点 | **-2102BP** | 2026-09-30 | 同上：「CNH 1年期掉期点收于-2102BP，较上月末下降278BP」 |
| 美国联邦基金目标区间 | **3.75–4.00%** | 2026-09-16 加息 25bp（12:0） | 美联储 2026-09-16：「The Committee decided to raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4 percent」 https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm |
| 美国国债 3 个月 / 1 年 / 10 年 | **4.28% / 4.53% / 5.19%** | 2026-10-14 | 美国财政部 Daily Treasury Par Yield Curve（2026-10 表格；10-05 时 10 年期为 5.31%） https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610 |
| 日本央行政策利率 | **1.25%** | 2026-09-18 加息（31 年来最高） | Nation Thailand 2026-09-18：「On September 18, the Bank of Japan increased its policy interest rate by 0.25 percentage points to 1.25%」 https://www.nationthailand.com/news/world/40071184 （二手报道，没有打开日本央行原文） |

**利差（我的计算）：**
- 3 个月：美债 4.28% − CNH 1.64% ≈ **2.6 个百分点**
- 1 年：美债 4.53% − CNH 1.67% ≈ **2.9 个百分点**。远期市场的定价也对得上：1 年掉期点 0.2102 ÷ 即期 6.7089 ≈ **3.1%/年**，这是"做空 CNH 远期、做多美元"一年能拿到的利差（前提是汇率不动）。
- 10 年：5.19% − 1.66% ≈ **3.5 个百分点**。路透 2025-12 报道，中美 10 年期利差在 2025 年初「hit a high of nearly 315 basis points」（见 2.1），现在比那时更宽。
- **和日元比（关键）**：日本央行已加到 1.25%，CNH 隔夜 1.46%。**在短端，人民币已经不比日元便宜。**彭博（二手转述）在 9 月初就说「If the BOJ raises rates this month, funding costs for the yen and the yuan could converge.」，这件事已经发生了。

---

## 2. 人民币作为融资货币的直接证据

### 2.1 B 类（融资型）：证据最硬，规模在创纪录

**路透 2025-12-19《Debt boom signals yuan's arrival as a funding currency》**（The Standard 转载，用浏览器读了原文）https://www.thestandard.com.hk/finance/article/319758/Debt-boom-signals-yuans-arrival-as-a-funding-currency
- 「China's overseas bank lending has tripled in four years to 2.52 trillion yuan (HK$2.79 trillion) and sales of onshore and offshore yuan debt are at or near records for the second year running.」
- 「central bank data shows lending in foreign currencies - mostly dollars - fell to US$375 billion at the end of November, from a peak of US$587 billion in 2022, while the value of yuan lending hit US$357 billion.」
- 「This year non-Chinese issuers raised 169.7 billion yuan … in onshore markets over the 11 months to end November, while a record 801.9 billion yuan was raised by all issuers in offshore markets」
- 「Three-year panda bonds were issued between 1.7 percent and 2.7 percent this year, far below the 3.5 percent yield on U.S. Treasuries for the same tenor, according to S&P Global.」
- 「Kenya converted dollar-denominated railway-construction loans to yuan in October, while Ethiopia is in talks to do the same.」另有：印尼 2025 年 10 月发 60 亿元点心债，哈萨克斯坦开发银行 9 月发 20 亿元。
- 同一篇的限制条件：「international yuan debts are worth about 0.2 percent of China's domestic debt market」；「A rising yuan, which is up about 3.6 percent on the dollar so far this year, can also be a negative for borrowers.」

**人民银行《2026年人民币国际化报告》相关数据**（国际金融报，东方财富 2026-09-30 转载；文章首段注明引自该报告，后面的数字没逐条注明出处）https://finance.eastmoney.com/a/202609303887853021.html
- 「境内银行境外人民币贷款余额也已超过1.44万亿元，占本外币境外贷款余额的50.7%。」（原文没写时点）
  - ⚠ 和路透的 2.52 万亿元**口径不一致**，可能一个是全部境外人民币贷款，一个只算境内银行。但两边方向一致：**人民币贷款已经占到中资银行对外贷款的一半左右，超过了美元。**
- 「2026年6月末主要离岸市场人民币贷款余额达到1.2万亿元」
- 「熊猫债发行保持热度，2025年发行规模约1830.6亿元，2026年上半年已经达到1600.3亿元；同期，离岸人民币债券发行金额达到8961亿元，同比增长94.4%」

**熊猫债（外国主体在境内发的人民币债）**
- 标普信评《2026 熊猫债市场观察》2026-08-13（读了 PDF 原文第 1–6 页）https://www.spgchinaratings.cn/upload/20260813_pandabonds_CN.pdf
  - 「2026年上半年熊猫债发行约1,600亿元，同比增长68%，7月存量首次突破5,000亿元。境外发行人占比升至50%」（按发行人家数算；2025 年末是 39%，其余主要是红筹中资企业）
  - 「截至7月31日，年内已累计发行111只，募资规模达1,957亿元，已超2025年全年发行总量」
  - 「从存量规模占境内有债市的比重来看，目前尚不足1%」
  - 「以法国巴黎银行2026年3月发行的5年期熊猫债为例，票面利率仅为2.05%，而其境外美元债票息通常在5%左右」
  - **关于机制的关键一句**：「境外发行人通过发行熊猫债获取人民币资金，再通过货币掉期兑换为所需外币，即便计入汇兑成本，综合融资成本仍可能低于直接发行美元债或欧元债」。这就是"借人民币、换美元"，但做了**掉期对冲**。按抛补利率平价，利差大部分在掉期成本里被抵掉，所以它不是日元式的裸套息。
  - 「2026年上半年……外国政府类熊猫债发行规模近200亿元，而2025年全年该类发行人发行规模仅为70亿元」；「2026年1至7月，外资银行和外资非银金融机构合计发行超600亿元」
- 新华财经 2026-08-14：「截至8月14日，2026年熊猫债发行规模同比增幅73.57%，累计发行债券2024.75亿元」，「已超越2025全年1854.6亿元人民币的发行总量，创下历史新高」；拜耳、汉高等发行人的募资「用于全球产业链周转、境外存量债务置换」 https://www.cnfin.com/zs-lb/detail/20260814/4455594_1.html

**点心债（离岸人民币债）**
- 新华财经转《证券日报》2026-09-23（Wind 口径）：「截至9月22日，年内点心债共发行1726只，发行规模合计14481.5亿元，超过2025年全年发行规模（14288.68亿元），创下历史新高。」受访者说：「美元债利率普遍在4.5%至5.5%区间，而点心债利率多在1.7%至2.2%」；「吸引大量中资企业选择点心债来优化负债结构」 https://www.cnfin.com/zs-lb/detail/20260923/4473816_1.html
- 中国外汇交易中心 9 月月报（见第 1 节新浪链接）：9 月单月「发行额为1842.27亿元，较上月增加68.8%」
- 口径差异很大：SCMP 引德银的数字是 2024 年 8500 亿元，Wind 口径 2025 年是 1.43 万亿元。https://www.scmp.com/business/china-business/article/3343282/yuan-rally-puts-fresh-steam-hong-kongs-dim-sum-bond-revival （2026-02-12）

**一个典型案例：腾讯 2026-10-14 定价**（路透，The Standard 转载，用浏览器读了原文）https://www.thestandard.com.hk/finance/article/345414/Tencent-prices-US18-billion-26-billion-yuan-notes-under-MTN-programme
- 「US$1.3 billion of notes due in 2036 carrying a 6.1 percent coupon」，对比「20 billion yuan of notes due in 2036 with a 2.40 percent coupon」
- 我的计算：同一发行人、同为 2036 年到期，美元票息比人民币高 **370bp**。人民币部分 260 亿元（约 39 亿美元），约占这次融资的 2/3。
- 定性：这是中资公司用便宜的人民币为国内 AI 资本开支融资，**不是借人民币去买美元资产**。

**政策推动（官方在主动"供应"离岸人民币）**
- 香港金管局 2026-07-07：「Increasing the size of the HKMA's RMB Business Facility from RMB200 billion to RMB500 billion」，期限延长到 9 个月、2 年、3 年，2026-07-10 起生效 https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260707-3/
  - 财新 2026-07-16 写的是「The PBOC's standing swap agreement with the Hong Kong Monetary Authority was expanded to 500 billion yuan」，很可能把这个 5000 亿元的 RBF 和央行与金管局的互换协议混在了一起，**以金管局原文为准**。https://www.caixinglobal.com/2026-07-16/pboc-moves-to-deepen-offshore-yuan-liquidity-broaden-asset-supply-102464635.html
- 新华网 2026-04-15，两部门（人民银行、外汇局）调整境外贷款政策：「境外贷款余额上限从20亿元上调至100亿元」；外资行境外贷款杠杆率「由0.5上调至1.5」 https://www.news.cn/fortune/20260415/e51bda1091444b308a76f46c5f6c5c0c/c.html
- BIS 季报 2025-12-08：「CNY was by far the most traded EME currency, accounting for 8.8% of global turnover in April 2025」，2022 年是 7.0%；「as much as 96% of all CNY transactions were against USD in April 2025」 https://www.bis.org/publ/qtrpdf/r_qt2512w.htm

### 2.2 A 类（日元式投机套息）：只有卖方观点和间接线索，**没有规模数据**

- 彭博 2026-09-03（BBVA）和 2026-09-09（《Yuan Steps Into Carry Trade Spotlight Over Yen》）：**原文被人机验证拦截，没能打开**。以下是 Bloomingbit 2026-09-09 注明转自彭博的二手内容 https://en.bloomingbit.io/feed/news/120010
  - 一个"借离岸人民币、投资 8 个新兴市场货币"的策略：「returned 1.5% over the past three months, according to data compiled by Bloomberg.」同期日元融资的版本约亏 1%。**注意：这是 CNH 对新兴市场货币的收益，不是对美元。**
  - DTCC 数据（9 月 1–8 日）：「Average daily trading volume in dollar-offshore yuan put options rose more than 60% from the previous month」。这里说的是美元兑离岸人民币的看跌期权，也就是押人民币升值的期权；成交量上升说明对冲和交易需求在增加，并不能证明有人在大规模做空人民币。
  - 被点名的机构有 Citi、Maybank、SocGen、BBVA。立场都是"值得关注、可能成为"，没有人说"已经大规模发生"。
- 彭博 2026-08-05（swissinfo 转载）谈全球套息时，主角是**欧元**融资：借欧元买巴西雷亚尔、哥伦比亚比索、土耳其里拉的篮子 2026 年「roughly 19%」；这篇文章**完全没提人民币**。Citi 的 Tobon：「We've seen a diversification of funding currencies」 https://www.swissinfo.ch/eng/carry-trade-is-powering-on-as-investors-sidestep-yens-gains/91850324
- 结构性背景（路透 2024-08-13 解释文章，**是旧数据**）：「A large proportion of yuan carry trades are by Chinese exporters parking cash in dollars.」「It is hard to gauge the total size of the yuan carry trade.」「it is smaller than yen-funded global trades.」 https://finance.yahoo.com/news/explainer-chinese-yuan-carry-trade-043313350.html
- CNBC 2026-09-14《Yen appreciation has carry-trade seekers looking at these two currencies》：**403，没能打开**。

### 2.3 C 类（中国企业持美元）：规模最大，但方向和"外资借人民币"相反

- 麦格理（The Standard 2026-05-26 转引彭博，用浏览器读了原文）https://www.thestandard.com.hk/finance/article/332985/Chinas-yuan-might-rise-to-5-against-USD-should-carry-trades-unwind-Macquarie-says
  - 「These firms have stockpiled over US$800 billion (HK$6.24 trillion) positions since 2022 through carry trades – borrowing the Chinese currency with a low interest rate, converting to the US dollar and investing in higher-yielding assets overseas」
  - 「China's yuan could rise to 6 or even 5 against the US dollar if domestic companies unwind their massive greenback holdings」
  - 注意：8000 亿美元是**卖方估算**，不是官方统计。2024 年 8 月麦格理的同口径估算是「more than $500 billion」（见上面 2024 年路透解释文章）。
- 官方数据侧证（境内外币存款还在增加）：格隆汇 2026-07-15 引人民银行数据：「6月末，外币存款余额1.16万亿美元，同比增长13.7%。」「上半年外币存款增加980亿美元。」 https://m.gelonghui.com/live/2554099
- 企业结汇意愿：
  - 外汇局副局长李斌（每经 2026-07-18）：「上半年，衡量结汇意愿的外汇收入结汇率是65%……与2025年相比变化不大」；「2026年1~6月，银行累计结售汇顺差18731亿元人民币。」 https://stock.10jqka.com.cn/20260718/c678267736.shtml
  - 每经 2026-09-17：「8月份，银行客户结汇率为61.51%，较上月提升逾4个百分点，7月份该项为57.23%。」「结售汇顺差扩至485亿美元。」 https://www.mrjjxw.com/articles/2026-09-17/4584065.html

---

## 3. 限制"日元式套息"的另一面

### 3.1 汇率：人民币一直在升值（做空人民币就亏钱），央行在"踩刹车"
- 路透（The Standard 2026-10-08）：「The yuan has gained nearly 9 percent against the dollar since late 2024 in a seven-quarter rising streak」；「The onshore yuan changed hands at 6.7030 per dollar in mid-morning trade」 https://www.thestandard.com.hk/finance/article/344937/Yuan-steady-despite-dollar-strength-during-Chinas-Golden-Week-holiday
- 路透（The Standard 2026-10-08）：「China's yuan has strengthened about 4 percent against the US dollar so far this year, defying the drag from a widening yield gap between US and Chinese government bonds.」人民银行同时表示，不会为贸易优势让人民币贬值。https://www.thestandard.com.hk/finance/article/344997/China-has-no-need-or-intention-to-weaken-yuan-for-trade-edge-central-bank-says
- 2025 年：路透 2025-12-19：「up about 3.6 percent on the dollar so far this year」，并且「China has been diligent in keeping a lid on yuan gains, with state banks buying dollars」
- 中间价持续定得比市场预期弱，说明央行在给升值降速：
  - 2025-12-04：「179 pips weaker than a Reuters estimate」，「the largest weak side deviation since the data was available in November 2022」 https://www.thestandard.com.hk/finance/article/318479/The-yuan-eases-as-PBOC-signals-caution-on-currency-strength-via-fix
  - 2026-01-23：中间价 6.9929，「448 pips weaker than a Reuters estimate of 6.9481」 https://www.thestandard.com.hk/finance/article/322430/China-lifts-yuan-guidance-to-stronger-than-7dlr-level-first-time-since-2023
  - 2026-07-10：「set the yuan's midpoint rate at 6.7989 per US dollar」，「still 58 pips weaker than a Reuters estimate」，年初至今「strengthened 3.1 per cent」 https://www.nst.com.my/amp/business/corporate/2026/07/1485130/yuan-climbs-one-week-high-pboc-sets-stronger-fixing-dollar-eases
  - 2026-07-31：中间价 6.7894，「581 pips weaker than a Reuters' estimate of 6.7313, marking the biggest deviation on the weaker side since Feb 27」，年初至今「3.6%」 https://theedgemalaysia.com/node/812845
  - 2026-10-12：中间价「100美元 673.13人民币」 https://www.news.cn/20261012/bccd72a446f0452c85ac4466c34becb3/c.html ；9 月末 CNH「收于6.7089」（中国外汇交易中心月报）
- **做空人民币套息的损益（我的粗算）**：2026 年至今利差约 2.6–3.1%/年 × 0.79 年 ≈ +2.1~2.5%，人民币升值约 4% → **净亏约 1.5~2%**。从 2024 年底算起，利差累计约 4~5%，人民币升值近 9% → **净亏约 4~5%**。日元套息能成立的前提是融资货币不升值，人民币过去 7 个季度恰恰在单边升值。
- 央行"压升值"的效果有两面：一方面让人民币波动低（这是融资货币的优点），另一方面趋势仍是升值，而且麦格理警告，一旦 C 类头寸平仓，人民币可能**急升**到 6 甚至 5。**这和日元套息平仓时日元暴涨是同一种风险。**

### 3.2 规模与资本管制：资金池太小
- 香港人民币存款（中国外汇交易中心月报，2026-08 数据）：「香港地区人民币存款规模为11014.96亿元，较上月减少2.1%」。我的计算：约 1640 亿美元，单笔腾讯发行（260 亿元）就占了这个池子的约 2.4%。
- 国际人民币债务「about 0.2 percent of China's domestic debt market」（路透 2025-12）；熊猫债存量占境内债市「尚不足1%」（标普信评 2026-08）。
- 人民币在岸不能自由兑换。CNH 虽然可以自由交易，但和在岸价差很小，等于被在岸锚住：9 月 CNY 和 CNH「日均平均价差（CNY-CNH的绝对值）为30BP」（中国外汇交易中心月报）。美银 Piron 的说法「The openness of the capital account of China is much more restricted than that of Japan」**只见于搜索摘要，没有打开原文，未核实**。
- 历史上 CNH HIBOR 多次被"挤压"、隔夜利率飙升（2024 年底曾到 8.1%，见 Mizuho 周报的搜索摘要，**未打开原文**）。对借 CNH 的人来说，这是一种**央行可控的平仓风险**，日元套息没有这一项。

### 3.3 D 类：内地资金出海找收益（要和"外资借人民币"分开看）
- 外汇局《2026年上半年中国国际收支报告》（中国证券报 2026-09-30）：「境内对外证券投资净增加1629亿美元，同比增长5%」；「对外债券投资净增加1199亿美元，同比增长1.9倍」；「对外股本证券投资净增加430亿美元，同比减少62%」；「境外对境内证券投资净增加117亿美元」；「外资来华股本证券投资净增加537亿美元」 https://stock.10jqka.com.cn/20260930/c680381230.shtml
  - 我的推算：外资来华证券投资总共 +117 亿美元，股票 +537 亿美元，倒推债券约 **-420 亿美元**，即外资在**卖出**中国债券。这和人民币国际化报告的数字一致：「境外主体持有的境内债券余额由约4.28万亿元下降至约3.23万亿元」（2025-06 → 2026-06，东方财富链接同上）。低收益的人民币资产正在被外资减持，这正是融资货币的特征。
- 路透（2026-10-08）引 Pantheon 的 Wrigley：「Chinese residents bought US$119 billion in foreign bonds」「during the first half of 2026」，并认为是「a trend likely propelled by the yawning yield gap」
- 南向通：中证报/东方财富 2026-06-03：「截至6月2日，2026年以来南向资金累计净买入2808.12亿港元」 https://finance.eastmoney.com/a/202606033757989120.html
- 定性：D 类是"中国人拿人民币储蓄换外币资产"，属于**资本流出**，受 QDII、南向额度等管制约束。它和"外国人借人民币"是两回事，但两者都由同一个利差驱动。

---

## 4. 结论

**"中国的套息交易已经开始了"这句话，能算真的部分约三成；把它说成"像日元那样"，大半是炒作。**

1. **真的（高可信度）**：人民币已经是低成本的**融资货币**。熊猫债 2026 年 1–7 月 1957 亿元，点心债截至 9 月 22 日 1.45 万亿元，两者都超过 2025 年全年。境外人民币贷款约占中资银行对外贷款的一半。同一发行人的人民币和美元票息差达 370bp（腾讯）。肯尼亚把美元铁路贷款换成了人民币。外资减持中国债券约 1 万亿元。
2. **真的，但不是外国人在做（高可信度，规模属卖方估算）**：中国企业持有美元资产（麦格理估 8000 亿美元以上，外币存款 1.16 万亿美元、同比 +13.7%），再加上内地资金出海买外国债券（上半年 1199 亿美元）。**最大的"人民币 carry"头寸在中国人自己手里**，它的平仓方向是人民币升值。
3. **基本没被证实（低可信度）**："日元式"投机套息，即外资借 CNH 做多美元。证据只有卖方观点、一个 3 个月的指数收益、期权成交量，**没有规模数字**。反面的证据倒有好几条：①过去 7 个季度人民币单边升值近 9%，做空人民币兑美元的套息两年都亏钱；②日本央行加到 1.25% 之后，人民币短端（CNH 隔夜 1.46%）**已不比日元便宜**；③CNH 池子只有约 1.1 万亿元，还会被央行挤压；④彭博 8 月对全球套息的综述里，主角是欧元融资，没提人民币。
4. **对投资者的含义**：真正要盯的风险不是"人民币套息平仓导致全球抛售"，而是 C 类头寸平仓（企业集中结汇）带来的**人民币急升**。这对持有美元资产的人民币投资者不利，对用人民币计价的境内资产相对有利。

### 要盯的指标（按重要性排序）
1. **USD/CNY 中间价相对路透预测的偏离**（几百个基点偏弱 = 央行在压升值）和**年内升值幅度**。只要人民币年升值 ≥ 利差（约 3%），A 类套息就做不起来。
2. **CNH 1 年掉期点 / CNH HIBOR 和美债、日本隔夜利率的差**（中国外汇交易中心每月出综述）。人民币相对日元的融资成本优势是在扩大还是消失。
3. **结汇率、外币存款余额**（外汇局、人民银行每月数据）。结汇率持续上升、外币存款下降 = C 类在平仓 = 人民币升值压力。
4. **熊猫债中外资发行人的占比、发行人是否掉期**；**境内银行境外人民币贷款余额**（人民币国际化报告、人民银行季度数据）。
5. **香港人民币存款**和**金管局人民币业务资金安排（RBF）使用率**。池子变大、而 CNH 拆息又没有飙升，才说明离岸人民币撑得住大规模借贷。
6. 卖方或交易数据：DTCC 上 USD/CNH 期权成交、路透亚洲货币持仓调查、BIS 国际银行业统计里的人民币跨境债权（本次**没取到**最新值）。

---

## 说法 / 证据 / 可信度

| 说法 | 证据（详见正文链接） | 可信度 |
|---|---|---|
| 人民币利率远低于美元，利差在 2.6–3.5 个百分点 | 7 天逆回购 1.40%，CNH 3 个月 1.64%、1 年 1.67%，中国 10 年 1.66%；美国 3 个月 4.28%、1 年 4.53%、10 年 5.19%（10-14）；CNH 1 年掉期点 -2102BP，约 3.1%/年 | **高**（一手和官方数据） |
| 人民币已成为全球融资货币，熊猫债、点心债创纪录 | 熊猫债 1–7 月 1957 亿元（标普信评），截至 8-14 为 2024.75 亿元（新华财经），都超过 2025 全年；点心债截至 9-22 为 1.45 万亿元（Wind），超过 2025 全年 | **高**（但大量发行人是中资企业） |
| 外国主体借人民币再换成美元 | 标普信评：发熊猫债后「通过货币掉期兑换为所需外币」；肯尼亚把美元贷款转成人民币；境外人民币贷款约占对外贷款 50.7% | **中高**：确实存在，但多为**对冲**的融资套利，不是裸套息 |
| 对冲基金像日元那样借 CNH 做多美元，"套息交易已经开始" | 只有彭博（二手）卖方观点、3 个月 +1.5% 的指数（对象是新兴市场货币，不是美元）、DTCC 期权成交量 +60%；没有任何规模数据 | **低** |
| 人民币将取代日元成为主要融资货币 | 日本央行已升到 1.25%，CNH 隔夜 1.46%，短端人民币不比日元便宜；CNH 池子约 1.1 万亿元；资本账户受限 | **低**（短期内不成立） |
| 存在 8000 亿美元的"人民币 carry"，平仓会让人民币升到 6 甚至 5 | 麦格理估算（The Standard 转引）；外币存款 1.16 万亿美元、同比 +13.7%（人民银行）支持"企业囤美元"这一事实 | **中**：囤美元是事实，8000 亿美元和"到 5"是卖方情景假设 |
| 人民币在升值，做空人民币的套息在亏钱 | 自 2024 年底升值近 9%、连续 7 个季度；2026 年至今约 +4%；2025 年约 +3.6%（截至 12 月 19 日）；我粗算的净损益为负 | **高**（汇率是事实；损益是我的估算） |
| 央行在压人民币升值 | 中间价持续比路透预测偏弱 58~581 个基点（2025-12 到 2026-07 的几个样本日）；国有银行买美元 | **高** |
| 内地资金出海找收益（和外资借人民币不是一回事） | 外汇局：2026 上半年对外债券投资 +1199 亿美元（同比 1.9 倍）；南向资金截至 6-2 为 2808 亿港元；外资持有的境内债券降到 3.23 万亿元 | **高** |

---

## 未能核实或有出入（如实列出）
- 彭博 2026-09-03、09-09 原文（人机验证页）和 CNBC 2026-09-14（403）没能打开，相关内容只用 Bloomingbit 的二手转述。
- 彭博 2026-07-22《Hong Kong's Offshore Yuan Market Evolves Into Global Funding Hub》：没找到可读版本，内容没有引用。
- SWIFT RMB Tracker 最新一期（403）没能打开；搜索摘要里"2026 年 4 月份额 2.85%、排第六"**未核实**，正文没有使用。
- 香港财资市场公会（TMA）的 CNH HIBOR 页面要先接受使用条款，我没有替你点"接受"，所以改用中国外汇交易中心的月末数据。10 月中旬的 CNH HIBOR 没有一手数字。
- BIS 国际银行业统计（LBS）里人民币计价跨境信贷的最新值：没找到。
- 境外人民币贷款：路透写 2.52 万亿元（2025-11），人民币国际化报告的转载写境内银行境外人民币贷款 1.44 万亿元（没写时点），口径不同，没能统一。
- 日本央行 1.25% 来自泰国 Nation 的报道，没打开日本央行原文。
