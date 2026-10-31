# NBIS 下跌驱动与 10-16 以来的新闻

as_of：2026-10-22 收盘（写于 2026-10-23 周五美股盘前）。本文件只回答两件事：为什么跌、10-16 之后发生了什么。资产负债表和 GPU 云经济性由其他文件负责。
标注：**[P]** = 一手（公司公告 / SEC / 原始媒体报道 / 交易所数据）；**[S]** = 二手（转述、聚合站）。日期都是美东时间。

---

## 0. 摘要

1. **是一连串因素叠加，不是单一触发。** 收盘价从 10-06 的 249.87 跌到 10-22 的 159.17（−36.3%）。同期 CRWV −39.4%，SMH −17.3%，NVDA −11.3%，QQQ −7.3%。10-09→10-16 这一周 NBIS 和 CRWV **都是 −25.2%**，跌幅几乎一样。这说明主要是"新云 + AI 债务融资"这个板块因子在起作用，不是 Nebius 自己出了事。[P 价格：Yahoo chart / stockanalysis 两源一致]
2. **叠加的顺序**：利率（10y 在 10-07 盘中到 5.365%，是 2002 年以来最高；同日 FOMC 纪要显示年底前还要加息）→ 10-08 FT 报道 OpenAI 对投资者说的年化收入约 $50B，而 9 月底流传的是 $68–70B → 10-13 晚 Chamath 在 X 上贴出 CoreWeave 2032 年债券收益率触及 15%，Musk 回了一句 "yikes" → 10-14 9 月 CPI 偏热，同日 Gartner 发布报告称 2030 年前 >80% 的新云会失去独立地位：CRWV −15.5%，NBIS −10.1% → 10-15 PPI 同比 +6.3%，CRWV 5 年期 CDS 约 1,038bp（1,000bp 以上一般视为困境）→ 10-16 Nasdaq −2.1%，CRWV −11.9%，NBIS −12.2%。
3. **10-14 和 10-16 两个大跌日，Nebius 都没有公司公告。** SEC 6-K 清单和公司新闻室里都没有，TECHi 和 TIKR 也分别做了同样的核查。[P/S]
4. **10-19 以后**：先小幅反弹，三天收盘 170.24 / 171.45 / 171.57；10-22 再跌 −7.2%，收 159.17，是本轮收盘新低，盘中最低 155.73。10-22 的驱动以板块和宏观为主：Meta 10-21 盘后发 Q3 财报，次日 −7%（2026 capex 下限上调到 $135–145B，Q3 FCF −$2.1B，新设无投票权 C 类股为 AI 建设融资）；黄仁勋在 CNBC 说新云 "scarcity of capital"；NYT 报道美以计划在中期选举后再次打击伊朗，Brent 涨到 $113；当天 CRWV −10%，SMH −6%。
5. **10-19 以来唯一的重大公司事项是 $35 亿 Citi 过桥贷款。** 10-17（周六）签署，10-22 盘前公告：364 天、优先**有担保**，利率 Term SOFR+2.75%，每 90 天加 0.25%，最高到 3.50%；设有最低流动性约束；担保物是借款人几乎全部资产；2027-10-16 到期。[P：6-K 0001104659-26-117978] COO 同时说，还有 ">$40B 投资级客户长期合同" 可以拿来做资产支持融资。这件事可以两面看：一面是"还能从银行借到钱"；另一面是"短期、有担保的过桥贷款，后面必须接一笔长期融资"，而且银行这一层排在 $57.5 亿无担保可转债之前。Yahoo 报道公告后盘前 −3.1%；没有任何来源量化过它对全天 −7.2% 贡献了多少。
6. **分析师动作**：Piper Sandler（James Fish）10-21 盘前把目标价从 $237 降到 $185，维持 Neutral，说板块会"in the penalty box"，直到 FCF 改善或融资变明朗。MarketBeat 把 10-22 的下跌归因于这次降级，但这站不住：报告 10-21 盘前就发了，当天 NBIS 收盘基本持平（+0.07%）。10-19 之后没有找到其他券商的实质动作。
7. **Q3'26 业绩日期仍未公告。** 截至 10-23 盘前，SEC、新闻室、IR 页都没有。第三方日历写的是 11-10 或 11-11。去年的日期通知是 10-22 发的，今年已经比去年晚。
8. **Burry**：一手来源是他的付费 Substack《Cassandra Unchained》9-28 的帖子，CNBC 9-28 引用了原文：他把 NBIS 空头换成 **2027 年 6 月到期、"double digit strike price" 的看跌期权**，理由是"moving timelines up"、想要更多杠杆。Benzinga 10-16 那篇只是转述。没有监管文件：Scion 最后一份 13F 是 2025-11-03。
9. **空头**：最新结算日仍是 **9-30，44,695,449 股**，约占总股本 16.3%，约占流通股 19.5%，回补天数 2.7 天。[P：Nasdaq] 10-15 结算日的数据还没发布。
10. **10-01 提价已有一手确认。** Wayback 存档的 Nebius 价格页 9-26 快照里有一列 "GPU-hour (Effective October 1, 2026)"：H100 $3.85→$4.50（+16.9%），H200 $4.50→$5.40（+20.0%），B200 $7.15→$8.50（+18.9%），B300 $7.85→$9.50（+21.0%）。10-23 的现网页面已经是新价。要注意同期**可抢占（preemptible）实例从固定价改成了动态竞价**：H100 原来固定 $2.15，现在是"from $0.79"。

---

## 1. 日线与驱动（10-05 → 10-22）

收盘价和成交量来自 Yahoo v8 chart 与 stockanalysis history，两个来源的收盘价逐日一致。[P]

| 日期 | 收盘 | 日涨跌 | 量(M) | CRWV | SMH | 驱动：**个股** / 行业宏观 |
|---|---|---|---|---|---|---|
| 10-05 一 | 232.57 | −4.2% | 15.1 | −2.5% | +0.5% | **个股：COO Ophir Nave 按 10b5-1 计划卖出 500,000 股，均价约 $231–244（约 $1.17 亿）。但 Form 4 是 10-06 才申报的，当天市场并不知道。** 宏观：Nasdaq 创历史新高，10y 5.31%。 |
| 10-06 二 | **249.87** | +7.4% | 21.4 | +5.0% | −0.2% | 本轮最高（盘中 255.10）。AI 建设股普涨（CNBC：Nebius 盘中 +9.5%），10y 回落到 5.28%。没有公司公告。 |
| 10-07 三 | 237.15 | −5.1% | 18.1 | −3.6% | −1.2% | 10y 盘中 5.365%（2002 年来最高），FOMC 纪要显示还会加息。（Rosenblatt 首次覆盖 Buy、目标价 $304，正面，但没拦住下跌） |
| 10-08 四 | 219.71 | −7.4% | 22.0 | −7.8% | −2.8% | **FT 报道 OpenAI 年化收入约 $50B，CNBC 确认**；当天 ORCL −5.5%，NVDA −2.9%。 |
| 10-09 五 | 221.07 | +0.6% | 9.6 | +0.6% | −0.6% | 缩量反弹。 |
| 10-12 一 | 210.06 | −5.0% | 14.1 | −2.2% | −2.1% | 美光 −3.9%（长鑫 CXMT 竞争），克利夫兰联储 Hammack 鹰派表态，油价上涨。 |
| 10-13 二 | 206.86 | −1.5% | 17.6 | −3.1% | −0.5% | 韩国存储股暴跌；晚间 Chamath 贴 CRWV 2032 年债收益率 15%，Musk 回 "yikes"。 |
| 10-14 三 | 186.01 | **−10.1%** | 34.0 | **−15.5%** | −4.0% | 9 月 CPI 偏热推高收益率；**Gartner 10-14 报告**；CRWV 2031/2032 年债 YTM 约 14.9%；ORCL −8.8%。**NBIS 没有公告。** |
| 10-15 四 | 188.41 | +1.3% | **47.7** | +5.9% | −1.0% | 盘中最低 163.36（−12%）后收红。PPI 环比 +1.3%、同比 +6.3%；CRWV 5y CDS 盘中 >1,140bp，收 ~1,038bp；Anthropic Q3 收入 $16.8B、环比 +45%（增速放缓，被当作利空）；SK Hynix 领跌韩股。董事 Boynton 按 10b5-1 卖出 7,260 股。 |
| 10-16 五 | 165.47 | **−12.2%** | 35.2 | −11.9% | −3.4% | Nasdaq −2.14%，VIX 超过 22，油价上涨；CRWV 总债务 >$51B 的担忧继续发酵。Reuters 的说法是：CRWV 约 $50B 的债务，加上通胀数据推高加息预期，导致传染（经 TIKR 转引）。**NBIS 没有公告。** |
| 10-19 一 | 170.24 | +2.9% | 26.9 | −0.4% | +1.6% | 盘中一度 +6.8%。收益率和油价回落；Goldman 把 CRWV 升到 Buy（目标价 $139→$106）；Gartner 的 Lovelock 在 CNBC 说 "more compute capacity than we have demand"。 |
| 10-20 二 | 171.45 | +0.7% | 22.6 | +1.6% | −0.4% | 盘前 −3%、开在 164，收盘转红；CRWV CDS 再度走阔。 |
| 10-21 三 | 171.57 | +0.1% | 19.7 | −0.5% | +1.9% | 利多：SpaceX Q3 电话会上 Musk 说"产能过剩"的说法 "ridiculous"；CRO Boroditsky 在 GTC Berlin 接受 CNBC 采访；Nebius 公开实时 spot 价格。利空：**Piper 目标价降到 $185（盘前发布）**。收盘基本持平。 |
| 10-22 四 | **159.17** | **−7.2%** | 26.0 | −10.1% | **−6.0%** | 盘中最低 155.73。行业宏观：Meta 财报后 −7%；黄仁勋说资本稀缺；伊朗、Brent $113.17；Nasdaq −2.6%（6 月以来最差的一天）；10y 反而 −17bp 到 4.97%。**个股：盘前公告 $35 亿 Citi 过桥贷款。** |

**区间对比**（收盘价对收盘价，同上价格源计算）

| | 10-06→10-22 | 10-09→10-16（一周） | 10-16→10-22 |
|---|---|---|---|
| NBIS | **−36.3%** | **−25.2%** | −3.8% |
| CRWV | −39.4% | −25.2% | −9.4% |
| ORCL | −13.3% | −9.3% | −2.1% |
| SMH | −17.3% | −10.5% | −3.0% |
| NVDA | −11.3% | −6.6% | −0.9% |
| QQQ | −7.3% | −5.5% | −0.8% |

159.17 相对各参照：52 周高点 $299.86 是 −46.9%；09-04 的 $226.39 是 −29.7%；可转债参考价 $223.90 是 −28.9%；2030 年可转债转股价 $313.46 是 −49.2%。

> **更正 10-19 卡上的一个数字**：卡里写"10-06 高点以来 NBIS −45%、SMH −19%"。实际从 10-06 盘中高点到 10-16 收盘，NBIS 是 −35.1%，SMH −15.6%，QQQ −7.0%，NVDA −12.0%。−45% 是相对 52 周高点的跌幅，被混到了一起。

**判断**：宏观、需求、信用三层叠在一起。
- **(a) 利率和通胀**：美伊战争带来能源冲击，10y 一度超过 5.3%，美联储还在谈加息，CPI 和 PPI 都偏热。
- **(b) AI 需求成色**：OpenAI 的 $50B 对 $68B，Anthropic 增速放缓，Gartner 的报告，Meta 的 FCF 转负。
- **(c) 新云信用**：CRWV 的债券和 CDS 进入困境区间，黄仁勋说"资本稀缺"。

Nebius 自身的负面只有几件小事：COO 售股（10-06 才披露）、Piper 降目标价、过桥贷款。两个 −10% 以上的交易日（10-14、10-16）都没有任何 Nebius 公司事件。

---

## 2. 10-19 以来的公司新事项

| 日期 | 事项 | 来源 |
|---|---|---|
| 10-17 签 / 10-22 公告 | **$35 亿 Bridge Facility Agreement**。借款人为 Nebius Group N.V.、Nebius Inc.（美国）、Nebius B.V.（荷兰）；Citibank 担任 MLA、贷款人、代理行和担保代理。senior secured term loan，用于 GPU 基础设施建设和一般用途。利率 SOFR+2.75%，每 90 天 +0.25%，上限 3.50%（三次加息点约在 2027-01-15、04-15、07-14）。可随时提前还款，无罚金。到期日 2027-10-16。**有最低流动性财务约束**。以借款人几乎全部资产及子公司股权作担保。新闻稿另含 COO Nave 的说法："asset-backed financing based on investment-grade customer commitments of more than $40 billion of long-term contracts"。 | [P] 6-K + Ex-99.1；Business Wire 10-22 |
| 10-21 | 新闻稿：公开**实时 spot 价格**（nebius.com/spot-prices，Shadeform、Silicon Data、GPU Finder 同步），另有 reserve auctions、按量付费、"capacity rebate" 试点（客户可把闲置 GPU 放回 spot 池换回一部分价值）。**新闻稿里没有任何单卡价格。** | [P] nebius.com newsroom |
| 10-21 | **CRO Boroditsky 在 GTC Berlin 接受 CNBC 采访**：Nebius 不背 CoreWeave 那种债，资金主要来自股权、可转债和客户预付；"计划中的 2027 年产能如果放出来卖，按现价可以立刻卖光"，目前有意留一部分给未来客户；客户已经在锁 2028 年的产能。 | [S] Stocktwits 10-21、247wallst 10-21（没看 CNBC 原视频） |
| 10-21 | Piper Sandler 把目标价从 $237 降到 $185，维持 Neutral；下调全板块终值倍数，建议在回调中分批建仓，板块首选 CRWV。 | [S] MarketBeat、Stocktwits（引 The Fly） |
| 10-19 | Zacks 把评级升到 Strong Buy（量化评级，参考价值低）。 | [S] MarketBeat |
| 10-19/20/21 | 董事 Arne Grimme 按 10b5-1 买入 148 / 151 / 148 股，价格约 $165–170，金额可忽略（10-15、10-16 也各买了 148 股）。 | [P] Form 4 |
| — | **没有找到**：Q3 日期公告、新的客户合同、指引变动、ATM 或增发、新的 13D/13G。 | [P] EDGAR 清单（截至 10-22 16:03 UTC 的 6-K） |

**10-01~10-15 内部人交易背景（Form 4 [P]）**：COO Nave 10-05 卖出 500,000 股、均价约 $235，备注称占其所获股权约 17%，10b5-1 计划 5-22 采纳，"No further sales will be made under such trading plan"，卖后持 454,685 股。CRO Boroditsky 10-12 行权后卖 7,000 股 @ $211.23。董事 Boynton 10-15 卖 7,260 股。CEO、CTO、CIO 10-01 为 RSU 扣税自动卖出 @ $234.16。另有 Goldman Sachs 13G/A（10-07）：5.1%（13.02M 股，截至 9-30，HC/BD 类型，属被动持有）。

---

## 3. 行业信用与需求（2026 年 10 月）

**CoreWeave**
- 股价：10-06 收 91.72 → 10-22 收 55.60（−39.4%）。[P]
- 债券：9.75% 2031 年债 YTM 15.78%（10-15，CNBC）；9.625% 2032 年债 14.8%（10-14）、14.9%（10-19）（CNBC）；Reuters 称 4 月发行的 2031 年债一度超过 16%（经 US News 和 TIKR 转引）。价格方面，10-20 的报价是 2030 年 6 月债 83.10c、2031 年 10 月债 79.46c。[S：roic.ai 聚合站]
- **5 年期 CDS**：约 1,038bp（10-15，盘中超过 1,140bp），约 1,082bp（10-19），10-20 再走阔（全部来自 CNBC [P]）。**这和 10-19 卡上写的 "CDS ~643bp" 对不上，643bp 应视为错误或过期数据。**
- 评级 S&P B+；债务加义务 >$51B；CEO 内部信称 backlog "more than supports all of our debt obligations"；Deutsche Bank 估计 backlog >$100B，约 2/3 为投资级对手方。
- 10 月**没有找到**新融资或违约条款事件（最近一次是 8 月 DDTL 5.5 $2.6B）。

**Oracle**（新云和投资级之间的"桥"）
- 10-14 −8.8%。5y CDS 282bp（10-15），315bp（10-19，同比 +311%）。S&P BBB-。2032 年 11 月到期的 6.25% 债 YTM 7.24%（10-14）。[P：CNBC]
- Rosenberg：净债务约 $132B，"A downgrade to junk would be the clearest sign of contagion"。
- 截至 10-13，GOOGL、AMZN、META、ORCL 年内合计发债超过 $228B（LSEG，经 CNBC 转引）。
- 10-28 有 Oracle 投资者日。

**OpenAI 收入"缺口"（原始出处 FT，10-08）**
- OpenAI 告诉投资者，9 月底年化收入约 **$50B**。9 月底被广泛报道的数字是 $68B（Axios 9-29 的说法是 "approaching $70B"）。
- 据 CNBC 的知情人士，$68B 里**包含合作方的总收入**，目的是方便和 Anthropic 的口径对比。所以这首先是收入口径的差别，不是 OpenAI 没完成自己的计划。
- OpenAI 同时强调 Q3 run-rate 增长 77%，企业业务增长 107%。
- 市场仍然当成利空：当天 NVDA −3%，ORCL 接近 −6%，CRWV 接近 −8%。[P：CNBC 10-08；TechCrunch 10-08]

**Anthropic**：Q3 收入 $16.8B，环比 +45%（上一季约 +147%）。来源是 10-14 IPO 前投资者会上一位与会者的说法，经 Reuters 和 FT 报道，公司没有公布。[S]

**Gartner（10-14 新闻稿）**
- gartner.com 页面有人机验证，没能直接读取；以下内容经 TheNextWeb 和 CNBC 转引 [S]。
- 到 2030 年底超过 $3.5T 的 AI 基础设施支出面临减值风险；**2030 年前 >80% 的新云会停止独立运营**。
- 2026 年支出约 $1T，2027–30 年再加 $6T；覆盖这些支出加 12% 回报需要 $8.5T 收入，Gartner 预测最多 $3.6T。
- Bloomberg 点名 CoreWeave 和 Nebius 比 MSFT/GOOGL/AMZN 暴露更直接。

**黄仁勋（10-22 CNBC）**：新云需求 "off the charts"，但 "There's a scarcity of capital. The demand [for] the capital is much greater than the availability of the capital." Wells Fargo 交易台的评论是，这句话在"惊吓市场"。[P：CNBC 当日直播稿]

**新云倒闭或困境融资**
- 10 月**没有找到** GPU 云提供商违约、重组或 GPU 抵押贷款被处置的案例。Lambda、Crusoe、Together 都没有困境消息；Lambda 8 月拿到约 $1B 的 JPM 融资，属于正常融资。
- Character.AI（算力买方，不是 GPU 云）10-12 在特拉华申请 Chapter 11。[S：amcompute 追踪表，转引 CBS/Bloomberg Law]
- The Information（经 AI Weekly 10-18 转引）：业内高管认为几百家新云里只有 7–10 家能活下来；Nvidia 有约 $20B 的数据中心租约准备转给第三方，另有 $6.3B 为 CRWV 兜底。[S]

**超大厂 capex 信号**
- **Meta**（10-21 新闻稿 [P]）：Q3 capex $34.91B；2026 指引 $135–145B，从 $130–145B 收窄（下限上调）；2027 年"continue investing aggressively"，没给数字；Q3 FCF −$2.12B；新设无投票权 C 类股。
- JPMorgan：超大厂 2026 年约 $800B，2027 年超过 $1T（经 CNBC 转引）。
- SpaceX Q4 capex 指引 $35–40B，Musk 说被"every hyperscaler... to rent more of our compute"缠着要算力。[S：247wallst]
- Tesla 下调 2026 年 capex 下限，但上调 2027–28 年。

**宏观**
- Brent 10-22 收 $113.17，是 5-04 以来最高（美伊冲突）。
- 10y：10-07 盘中 5.365% → 10-13 5.19% → 10-21 5.12% → 10-22 4.97%。
- 9 月 CPI 偏热（10-14），PPI 同比 +6.3%（10-15）。
- FOMC 10-27/28；10-16 时 CME FedWatch 显示 82% 概率按兵不动。

---

## 4. 催化剂日历

| 日期 | 事件 | 确认状态 |
|---|---|---|
| ~10-26/27 | FINRA 发布 10-15 结算日空头数据 | 按惯例推算，未核实 |
| 10-27/28 | FOMC | [P] CNBC 引 CME |
| 10-28 三 盘后 | **MSFT** FY27 Q1 | 微软 10-07 新闻稿已确认（经 finviz 转载 [S]） |
| 10-28 三 盘后 | **GOOGL** Q3（1:30pm PT） | 第三方称 10-06 已公告；abc.xyz 上未核到 |
| 10-28 | Oracle 投资者日 | [S] CNBC |
| 10-29 四 盘后 | **AMZN** Q3（2pm PT） | [P] aboutamazon.com 10-15 已确认 |
| 11-02 | Apple | [S] CNBC |
| 11-03 | 美国中期选举（据报道对伊朗的打击计划在选后） | [P] NYT，经 CNBC 转引 |
| ~11-10/11 | **NBIS Q3** | **未公告**；AJ Bell 写 11-11，stockanalysis 写 11-10 |
| ~11-10~16 | CRWV Q3 | 未公告 |
| ~11-18/19 | **NVDA** Q3 FY27 | 未公告（去年 10-29 发通知，11-19 发布） |
| 11 月（据报道） | Anthropic IPO | [S] |
| ~12-10 | **ORCL** FQ2 FY27 | 未公告 |
| 已发生 10-21 | **META** Q3 | [P] |
| 2027-01-15 / 04-15 / 07-14 / 10-16 | Citi 过桥贷款利率逐级上调，最后一天到期 | [P] 6-K 推算 |

---

## 5. 正在流传的多空论点

**多方（只列可信来源）**
- **需求**：黄仁勋说新云需求 "off the charts"；Musk 说产能过剩的说法 "ridiculous"，SpaceX AI 板块收入同比 +830%，到 $7.6B（[S] 247wallst）；Boroditsky 说 2027 年产能按现价可以卖光（[S]）。
- **定价**：按量付费的标价 10-01 起上调 17–21%（[P] 价格页存档）。据报道 5 月还提过一次（[S]，未核实）。
- **合同**：COO 说有 ">$40B 投资级长期合同"（[P] 10-22）；已知的有 Microsoft $17.4–19.4B（2025-09）、Meta 约 $3B（2025-11），以及 Meta 最高约 $27B（2026 年 6-K：$12B 确定 + 最高 $15B 兜底）。
- **融资渠道还开着**：可转债、$775M ABS、这次的 $3.5B 银行贷款；没有 CRWV 那种公开交易的垃圾债。
- **卖方**：Dan Ives（10-15，经 TipRanks 转引）认为抛售是买点，利率挤压的是融资不是需求。Goldman 对 CRWV 的看法是合同经济性数据会好于市场预期。Rosenblatt Buy、目标价 $304。共识目标价：MarketBeat $243.25（22 家），stockanalysis 约 $284。

**空方**
- **信用市场在拒绝没有经营现金流支撑的 AI 债务**：Evercore ISI 交易台原话 "basically saying 'no mas' to AI debt without operating cash flow support"。
- **过桥贷款本身**：有担保的银行层排在 $57.5 亿无担保可转债之前；只有 364 天，2027 年必须用 ABS 或股权接上；利率逐级上调。
- **资本稀缺**：黄仁勋原话。Piper 认为要等 FCF 或融资变明朗才能出"penalty box"。Redburn 9 月给 Sell、目标价 $84（20% 股权成本 DCF，[S]）。
- **需求成色**：OpenAI $50B 对 $68B；Anthropic 增速放缓；Gartner 认为产能已过剩；Meta FCF 转负、新设股票类别融资。
- **spot 定价**：可抢占实例从固定价（H100 $2.15）改成动态竞价，底价 $0.79–0.99，可能是在把闲置产能变现（我的推断，有两种读法）。
- **利率和油价**：10y 在 5% 附近，美联储倾向加息，伊朗局势推高油价。
- **持仓面**：COO 在 ~$235 卖出 50 万股；Burry 持有 2027 年 6 月看跌期权；9-30 空头 4,470 万股。
- **披露缺口（沿用 10-19 卡）**：active MW 连续四个季度未披露。

---

## 6. 来源表

| 标题 | 来源 | 日期 | URL | 级别 |
|---|---|---|---|---|
| Form 6-K: Credit Facility + Ex-99.1 "Nebius secures $3.5 billion financing facility with Citi" | SEC / Nebius | 2026-10-22 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926117978/tm2628078d1_6k.htm | P |
| Nebius brings compute pricing into the open… | Nebius newsroom | 2026-10-21 | https://nebius.com/newsroom/nebius-brings-compute-pricing-into-the-open-as-europe-s-ai-builders-scale-on-its-cloud | P |
| Nebius newsroom list | Nebius | 2026-10-23 访问 | https://nebius.com/newsroom | P |
| AI Cloud pricing（现网） | Nebius | 2026-10-23 访问 | https://nebius.com/prices | P |
| AI Cloud pricing（含 "Effective October 1, 2026" 列） | Wayback 存档 | 2026-09-26 快照 | https://web.archive.org/web/20260926001828/https://nebius.com/prices | P（存档） |
| Nebius EDGAR submissions（Form 4 / 144 / 13G/A 清单） | SEC | 2026-10-23 访问 | https://data.sec.gov/submissions/CIK0001513845.json | P |
| Form 4 COO Nave（500k 股，含备注） | SEC | 2026-10-06 申报 | https://www.sec.gov/Archives/edgar/data/1513845/000151384526000126/ | P |
| Schedule 13G/A Goldman Sachs 5.1% | SEC | 2026-10-07 | https://www.sec.gov/Archives/edgar/data/1513845/000088698226000526/ | P |
| Scion Asset Management filings（最后一份 13F 是 2025-11-03） | SEC | 2026-10-23 访问 | https://data.sec.gov/submissions/CIK0001649339.json | P |
| NBIS short interest table | Nasdaq | 结算日 9-30 | https://api.nasdaq.com/api/quote/NBIS/short-interest?assetClass=stocks | P |
| NBIS daily history | stockanalysis / Yahoo chart | 2026-10-22 | https://stockanalysis.com/stocks/nbis/history/ | P（行情） |
| Meta Reports Third Quarter 2026 Results（全文） | Meta，经 StockTitan 转载 | 2026-10-21 | https://www.stocktitan.net/news/META/meta-reports-third-quarter-2026-13ysmyjaxliq.html | P（转载） |
| Nvidia, Oracle, other AI stocks sink on OpenAI revenue report | CNBC | 2026-10-08 | https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html | P |
| OpenAI's revenue is reportedly $20 billion less… | TechCrunch（引 FT） | 2026-10-08 | https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/ | S |
| CoreWeave stock sinks as bond yields surge near 15% | CNBC | 2026-10-14 | https://www.cnbc.com/2026/10/14/coreweave-stock-bond-yields-ai-debt.html | P |
| CoreWeave credit default swaps hit distress levels… | CNBC | 2026-10-15 | https://www.cnbc.com/2026/10/15/coreweave-credit-default-swaps-hit-distress-levels-as-investors-sour-on-ai-debt.html | P |
| CoreWeave bond yields stay near 15% as AI stocks rebound | CNBC | 2026-10-19 | https://www.cnbc.com/2026/10/19/coreweave-oracle-ai-credit-stress.html | P |
| Stock market news（10-05、06、07、09、12、13、15、16、19、20、21、22 各日直播稿） | CNBC | 逐日 | 例：https://www.cnbc.com/2026/10/21/stock-market-today-live-updates.html | P |
| Michael Burry believes the AI bubble 'may burst' sooner… | CNBC | 2026-09-28 | https://www.cnbc.com/2026/09/28/michael-burry-believes-the-ai-bubble-may-burst-sooner-than-he-first-believed.html | P（引 Substack 原文） |
| Nebius Lands $3.5 Billion Financing Amid Neocloud Debt Fears | Yahoo Finance | 2026-10-22 | https://finance.yahoo.com/technology/ai/articles/nebius-lands-3-5-billion-161426077.html | S |
| Gartner Says Over $3.5 Trillion of AI Infrastructure Spending Could Be Exposed to Impairment… | Gartner | 2026-10-14 | https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030 | P（被人机验证拦住，未读到正文） |
| Gartner warns $3.5tn of AI infrastructure spending is at write-down risk | TheNextWeb | 2026-10 | https://thenextweb.com/news/gartner-ai-infrastructure-spending-3-5-trillion-write-down-neoclouds | S |
| Nebius less exposed to AI cloud debt concerns, says CRO… Piper cuts target 22% | Stocktwits | 2026-10-21 | https://stocktwits.com/news-articles/markets/equity/nebius-less-exposed-to-ai-cloud-debt-concerns-says-cro-marc-boroditsky-piper-sandler-cuts-target-22/cZxMb9dRBve | S |
| Nebius Group Price Target Cut to $185.00 by Piper Sandler | MarketBeat | 2026-10-21 | https://www.marketbeat.com/instant-alerts/analyst-nebius-group-nasdaq-nbis-price-target-cut-to-18500-by-analysts-at-piper-sandler-2026-10-21/ | S |
| NBIS forecast / ratings | MarketBeat；stockanalysis | 2026-10-23 访问 | https://www.marketbeat.com/stocks/NASDAQ/NBIS/forecast/ ；https://stockanalysis.com/stocks/nbis/ratings/ | S |
| AI Cloud Stocks Rise as Musk Calls Overcapacity Talk 'Ridiculous' | 24/7 Wall St | 2026-10-21 | https://247wallst.com/investing/2026/10/21/ai-cloud-stocks-rise-as-musk-calls-overcapacity-talk-ridiculous-nebius-and-coreweave-gain-3-oracle-edges-higher/ | S |
| Nebius Stock Fell 12% in a Day as CoreWeave's Debt Scare Spread | TIKR | 2026-10-17 | https://www.tikr.com/blog/nebius-stock-fell-12-in-a-day-as-coreweaves-debt-scare-spread-heres-why-its-balance-sheet-isnt-coreweaves-yet | S |
| CoreWeave Bonds Tumble as Credit Pressure Builds（债券价格） | roic.ai | 2026-10-20 | https://www.roic.ai/news/coreweave-bonds-tumble-as-credit-pressure-builds-10-20-2026 | S（聚合站） |
| Amazon will share its Q3 2026 earnings on October 29 | Amazon | 2026-10-15 | https://www.aboutamazon.com/md/news/company-news/amazon-earnings-q3-2026-report | P |
| Microsoft announces quarterly earnings release date | finviz（转载微软新闻稿） | 2026-10-07 | https://finviz.com/news/400058/microsoft-announces-quarterly-earnings-release-date | S |
| GPU and neocloud defaults and stress events | amcompute | 更新于 2026-10-17 | https://www.amcompute.com/gpu-risk/defaults | S |
| Information: only 7–10 neoclouds surviving… | AI Weekly（转 The Information） | 2026-10-18 | https://aiweekly.co/alerts/information-industry-execs-see-only-7-10-of-hundreds-of-neoclouds-surviving-as | S |
| Anthropic revenue jumps to $16.8 billion in third quarter, FT reports | The Star（转 Reuters/FT） | 2026-10-15 | https://www.thestar.com.my/tech/tech-news/2026/10/15/anthropic-revenue-jumps-to-168-billion-in-third-quarter-ft-reports | S |

---

## 7. 未核实 / 有冲突的条目

1. **Gartner 新闻稿正文**：gartner.com 有人机验证，没有绕过；数字全部来自 TheNextWeb 和 CNBC。
2. **Boroditsky 的 CNBC 采访**：只读到 Stocktwits 和 247wallst 的转述，没看原视频。"2027 产能可卖光"这句话是二手引述。
3. **黄仁勋的引语**：来自 CNBC 当日直播稿，属于原媒体，但没看完整采访。
4. **Burry**：Substack 是付费内容，只有 CNBC 引用的原文。行权价具体是多少、仓位多大、现在是否还持有，都不知道。没有 13F。
5. **Reuters 10-16 关于 CRWV 债务传染的报道**：只通过 TIKR 和 US News 转述（US News 页面超时）；"约 $50B 债务"这个数字也没有直接核对。
6. **CRWV 债券价格 83.10c / 79.46c**：只有聚合站 roic.ai 的数据。10-19 卡上的 "CDS 643bp" 与 CNBC 的 1,038–1,082bp 冲突，**以 CNBC 为准**。
7. **10-22 当天 −7.2% 里有多少来自 Citi 过桥贷款**：这是我的推断，没有来源量化过。能确认的只有 Yahoo 报道公告后盘前 −3.1%，以及同日板块普跌（CRWV −10%、SMH −6%）。
8. **BofA**：stockanalysis 列了一条 10-22 "Reiterates Buy $310"，但没找到对应的新报告，$310 是 8 月定的。
9. **催化剂日期**：GOOGL 10-28 的来源是第三方；NBIS、CRWV、NVDA、ORCL 的日期都是推算。
10. **"5 月第一次提价"**：没有用 Wayback 核实。
11. **Nebius RPO**：247wallst 写 $37.5B，10-19 卡写 $33.6B，存在冲突，交给资产负债表那条线核对。
12. **Character.AI Chapter 11**：来自追踪站转引 CBS/Bloomberg Law，没读原文。
13. **Benzinga 10-22 的个股解读**：页面返回 403，只看到搜索摘要。
