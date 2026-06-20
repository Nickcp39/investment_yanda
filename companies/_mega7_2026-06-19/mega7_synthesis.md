# Mega7 活体批次 — 组合级汇总 (SYNTHESIS)

**批次 ID**: `mega7_2026-06-19` · **as_of (冻结边沿)**: 2026-06-19
**pipeline_version**: `lean-6module-v1` · **weights_version**: `none` · **run_date**: 2026-06-19
**回测出处**: 该 pipeline 经 10-case 框架验证 **9 PASS / 1 FAIL** 后固化（`backtests/framework_validation/`）。
**诚实状态**: 7 家全部 **DECISION_DRAFT 级（~55–75% 完整度）**，**不是 COMPLETE**；逐名打磨为 follow-up，不在本批一遍内承诺。
**Checker 裁定**: 7 家全 **CLEAN**（载荷数回挂一手、独立重算 tie out、无伪造引语、verdict 被完整度/价格正确封顶）。

---

## 1. 七名排序（attractiveness：verdict → IRR → ceiling）

排序口径：先按新钱 verdict（STARTER 高于 WATCH），verdict 同档再按 base IRR，再看 ceiling/完整度。

| # | Ticker | context_label | biz verdict | 新钱 verdict | 存量 verdict | initial/max size | ceiling | 完整度 | base 5y IRR | binding constraint | checker |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | exceptional_bottleneck | exceptional | **STARTER** | HOLD | 4% / ~12% | STARTER | ~65% | **+13%** | run-rate 可持续性 vs pull-forward + custom-silicon 份额（**价格友好，非约束**） | CLEAN |
| 2 | **MSFT** | quality_compounder_de-rated_on_capex_shock | exceptional | **STARTER** | ADD | 4% / ~9% | STARTER | ~65% | **+9.5%** *(10y)* | **完整度**（OpenAI 经济学 O3 + capex ROI 拆分 O2）— 非价格（FV~$436 > $379，有正 MOS） | CLEAN |
| 3 | **AAPL** | exceptional_compounder_overpriced | exceptional | WATCH | HOLD | 0% / 15% | WATCH | ~60% | +2.7% | **价格 / 估值**（~36x OE，2.7% 起始收益率，base IRR « 8% hurdle） | CLEAN |
| 4 | **META** | good_business_fairly_to_richly_priced | good | WATCH | HOLD | 0% / 5% | STARTER | ~62% | +4.0% | **价格 + capex ROI 未决（O4）**；广告引擎满血但 owner earnings 被 capex 吃 | CLEAN |
| 5 | **AMZN** | good_business_wrong_price | good | WATCH | HOLD | 0% / 0% | WATCH | ~62% | −1.5% | **价格无 MOS + owner-earnings 桥不闭合**（$200B capex 拆分 O4） | CLEAN |
| 6 | **GOOGL** | great_business_no_margin_of_safety | good | WATCH | HOLD | 0% / 0% | WATCH | ~75% | **−3.0%** *(10y)* | **价格无 MOS**（~69x OE，连 bull 10y IRR +5.2% < 8%）；buybacks 暂停，杠杆上行供 capex | CLEAN |
| 7 | **TSLA** | narrative_premium_cyclical | uncertain | WATCH | **TRIM** | 0% / 0% | WATCH | ~55% | **−17%** | **价格无 MOS（delivered 端）+ 核心汽车利润池萎缩 + Musk key-man / 12% 稀释** | CLEAN |

> **IRR 口径注**: MSFT、GOOGL 的 base IRR 是 **10 年** 口径（+9.5% / −3.0%），其余为 **5 年**；为可比已在表内标注，排序时按各卡自报 base 对 8% hurdle 的相对位置处理。NVDA 的 M6 信号在卡里记 +1（价格友好但仍受 run-rate 不确定性约束），其余价格受限名 M6 为负。

**唯二可开新仓的是 NVDA 与 MSFT（STARTER）**，且两者被**不同的约束**封在 STARTER：NVDA 是完整度（~65%）+ 周期性封顶、价格友好；MSFT 是完整度（OpenAI 黑箱 + capex ROI 缺口）封顶、价格有正 MOS。其余 5 名全是 **WATCH / 0% 新钱**，TSLA 存量更进一步到 **TRIM**。

---

## 2. 同因子内的"分流"——框架不是一刀切

七名几乎全骑同一条 **"AI capex + 流动性"** 因子，但 verdict 与封顶**理由各不相同**，这正是 lean-6module 想证明的：同一因子下仍能逐名分流，而非把所有 AI-capex 名字打成一档。

- **NVDA — 周期性封顶（价格站买方这边）**：owner earnings 异常干净（capex-light，FCF≈OE≈$182B run-rate，净现金 ~$72B），forward ~19x / 起始 OE yield 5.1% / base 5y IRR +13% **有正安全边际**。约束是"+85% 增速 / 75% 毛利率这种极值能撑多久（pull-forward + custom-silicon）"——**控制 size，不否决**；周期性把天花板压在 Confirmed 以下。
- **MSFT — 完整度封顶（价格不是约束）**：去化 32%（capex shock 已被市场打掉），FV~$436 > 现价 $379 = **正 MOS**，base 10y IRR +9.5%。但 OpenAI 关系经济学（O3，Azure +40% 里有多少是 OpenAI compute？）和 capex 维护/成长拆分（O2）两个**信息缺口**把 verdict 封在 STARTER、挡住 CORE。**与 GOOGL 的对照最干净：同因子，MSFT 被完整度封、GOOGL 被价格封。**
- **AAPL — 价格封顶（耐久性没问题）**：annuity 护城河 HIGH（耐久性本可支持 Core 级 size），但 ~36x OE、2.7% 起始收益率、base IRR +2.7% « 8% → **价格独立把 verdict 压到 WATCH**。耐久性没被用来抬 size；价格门 binding（GOOGL 同机制）。
- **META — 价格 + capex ROI 双重封顶**：广告引擎满血（营收 +33%、ad price +12%、3.56B DAP），但 FCF 被 capex 吃（FCF yield 仅 3.4%），base 5y IRR +4% < hurdle，capex ROI（O4）未量化 → 现价无 MOS。完整度封在 STARTER、价格再压到 WATCH。
- **AMZN — 价格无 MOS + 桥不闭合**：三引擎好生意，但 TTM FCF ~$1.2B（capex $200B/yr 吃光 OCF），起始 OE yield 2.1–2.5%，base 5y IRR 负。owner-earnings 桥**不闭合**（GOOGL 同病更极端）。价格封顶 WATCH。
- **GOOGL — 价格无 MOS（最贵）**：~69x owner earnings，连 bull 10y IRR 才 +5.2%（全 < 8%），reported NI 被 ~$36.9B 非现金股权收益灌水 2–3 倍，buybacks 暂停 = 稀释裸露，资产负债表为 capex **加杠杆而非护底**。完整度 ~75%（最高）但价格更紧地封到 WATCH。
- **TSLA — 价格 + 萎缩利润池 + key-man**：$1.41T 由**叙事**而非已交付基本面支撑（P/E 371x，起始 OE yield 0.35%，base 5y IRR −17%）；汽车经营利润率 16.8%→4.6% 萎缩，Musk key-man + $1T pay package ~12% 稀释。唯一从 HOLD 进一步到 **TRIM** 的名字。business_verdict 也是唯一的 **uncertain**。

> 一句话：**同一根因子，三种封顶机制各演一遍** —— GOOGL/AMZN/AAPL/TSLA 价格封、MSFT 完整度封、META 价格+ROI 双封、NVDA 价格友好仅被周期+完整度封。证据是 framework 在因子内做了**真实分流**，不是 one-size-fits-all。

---

## 6. 单因子集中度检查（METHODOLOGY §5 · 一句话判断，不做协方差）

**会一起跌。** 这七名几乎全部坐在同一根 **"AI capex 周期 + 流动性"** 因子上：NVDA 是卖铲子的瓶颈、MSFT/AMZN/GOOGL/META 是花 $125–200B/yr 买铲子建数据中心的 hyperscaler、AAPL 的 AI 入口又借 Google 云 / Nvidia GPU、TSLA 的 $1.41T 估值也压在 AI/自动驾驶叙事上——**若 AI capex 周期回撤或流动性收紧，这七名的 owner-earnings 预期与多重估值会同向收缩，大概率一起跌**（NVDA 跌需求与 run-rate、hyperscaler 跌 capex-ROI 故事、TSLA 跌叙事溢价）。更关键的是叠加用户**已持有的 BTC / GOOGL / NBIS**——按 METHODOLOGY §5，这三者也都在"AI + 流动性"这根因子上（BTC 吃流动性、GOOGL 与 NBIS 直接是 AI capex），所以**在这七名里再加任意一个 AI 名字 = 把一个本已隐藏的单一押注加倍，而不是分散**。直白的结论：组合层面的真实风险**不是选错某一家**，而是**整本书押在同一件事会不会发生上**；即便逐名 verdict 都对（NVDA/MSFT 是真有 MOS 的 STARTER），把它们一起买进来仍会让"AI capex + 流动性"成为压倒性的单因子敞口。**真正能分散的，是因子正交的名字**（现金流稳定、与 AI capex/流动性低相关的消费/医疗/能源/防御性资产，或干脆留 ~5% 机会仓现金），而不是在 Mega7 里换哪一家。落到操作：本批即便开仓，也应**只在 NVDA / MSFT 里二选一或合计控量**，把 AI-capex 因子的总敞口当成一个仓位来管，而非七个独立仓位。

---

## 诚实状态（honest status）

7 家全部为 **DECISION_DRAFT 级（~55–75% 完整度）**，不是 COMPLETE。一遍并行跑到决策草案是本批的现实目标（GOOGL 用整天并行才到 ~75%）。每家都有显式 OPEN（多为 capex 维护/成长拆分、proxy/operator 细节、分部利润），blocking 项已正确封顶 verdict。逐名打磨到 COMPLETE（补一手、闭合 owner-earnings 桥、升完整度 >80% 解封 CORE 讨论）是 follow-up，不在本批承诺。Checker 全 CLEAN，仅有非阻断 nit（AAPL 52 周低抄录转置、TSLA 能源"翻倍"措辞夸大 +48% 实际、若干口径统一建议）。
