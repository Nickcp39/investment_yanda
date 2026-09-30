# Mega7 活体批次 — 组合级汇总 (SYNTHESIS)

**批次 ID**: `mega7_2026-07-28` · **as_of (冻结边沿)**: 2026-07-28
**pipeline_version**: `lean-6module-v1` · **weights_version**: `none` · **run_date**: 2026-07-28
**方法**: 读 6/19 dossier 做业务基线（M2/M3 六周内快速复核），用**今天的价** + **7/28 regime** 重算 M4/M5/M6，重导两轴 verdict。**不是从零重研究。**
**回测出处**: pipeline 经 10-case 框架验证 **9 PASS / 1 FAIL** 后固化（`backtests/framework_validation/`）。
**Checker 裁定**: 7 家**全 CLEAN**（价格经 Checker 独立 Yahoo 重抓坐实、非 52 周极值/无 INC-001、衍生数逐项 tie out、无伪造引语、verdict 被完整度/价格正确封顶、regime 真并入 M4/M5）。
**诚实状态**: 7 家全部 **DECISION_DRAFT（~55–75% 完整度）**，不是 COMPLETE。

> ## ⚠ 关键定时（读排序前必看）
> 本批锁在 **Mega7 财报周的正中央**，且 as_of 就是 **7/28 半导体暴跌当天**（SOX −25%、SK 海力士腰斩、KOSPI 年内第 8 次熔断、NVDA 领跌 ~$300B、AAPL 反超 $5T）。
> **7 家里只有 GOOGL / TSLA 带 Q2-2026 实数**（均 7/22 已报，`dq2=true` = 本轮有已报季度把某个模块真正重估到 M4 −2）。**其余 5 家全锁在 print 前**：MSFT 7/29 盘后、META 7/29 盘后、AAPL 7/30、AMZN 7/30、NVDA 8/26。**FOMC + Warsh 记者会 7/29**。
> ⇒ 本批是**双重临时**：既是 DECISION_DRAFT 完整度，又是 pre-print 定时。4/7 在 as_of 后 48h 内出财报——排序可用于"当前价买不买"的口径，但任何开仓都应等 print 或分批穿越。

---

## 1. 七名排序（attractiveness：新钱 verdict → base IRR → ceiling）

排序口径：先按新钱 verdict（STARTER 高于 WATCH），同档再按 base IRR 相对 8% hurdle 的位置，再看 ceiling/完整度。

| # | Ticker | context_label | biz | 新钱 / 存量 | init/max | buy_below → 现价 | base IRR | binding constraint | checker (dq2) | Δ 6/19→7/28（verdict + 一句因） |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | quality_compounder_de-rated_capex-audit_pre-Q4-binary | exceptional | **STARTER** / HOLD | 3% / 9% | $436 → **$393.35** (−10%，正 MOS) | **+9.1%** *(10y)* | **完整度 ~63%**（capex 维护/成长拆分 O2 + OpenAI 经济学 O3）— **非价格** | CLEAN (F) | **STARTER→STARTER**（唯一）。价 +3.7% 出"back-up-truck"区、MOS 13-15%→~10%，init **4%→3%**、存量 **ADD→HOLD**；7/29 Q4+FOMC 双二元 24h 外。**[价+定时]** |
| 2 | **NVDA** | exceptional_bottleneck_no_MOS_derated_into_capex_audit | exceptional | WATCH / HOLD | 0% / 0% | $181 → **$197.01** (+8.8%，无 MOS) | **+6.2%** *(5y)* | **价格**（base < 8% hurdle，仍 +8.8% 高于买入线）+ regime（capex 审计 + custom-silicon + Warsh） | CLEAN (F) | **WATCH→WATCH**。7/28 领跌 −6.5%（$210.69→$197.01），base IRR **+4.8%→+6.2%**、缺口 3.2pp→**1.8pp** = **最接近 STARTER 但未到**；Q2 FY27 要等 8/26。**[价/regime]** |
| 3 | **META** | good_business_fairly_to_richly_priced_capex_ROI_unresolved_pre_Q2_regime | good | WATCH / HOLD | 0% / 5% | $480 → **$593.41** (+24%，无 MOS) | **+3.4%** *(5y)* | **价格**（+2.8% 比 6/19 更贵，MOS 反而更差）+ capex ROI 未决（O4）+ 事件定时 | CLEAN (F) | **WATCH→WATCH**。7 月冲 ~$681 又跌回、净 **+2.8% 更贵** = **唯一没变便宜的 Mega7**；base IRR +4.0%→**+3.4%（更差）**；Q2+FOMC 7/29。**[价—反向]** |
| 4 | **AAPL** | exceptional_compounder_overpriced | exceptional | WATCH / HOLD | 0% / 15% | $231 → **$340.08** (+47%，无 MOS) | **~0.0%** *(5y)* | **价格 / 估值**（41.7x OE、2.40% 起始收益率）— **比 6/19 更 binding** | CLEAN (F) | **WATCH→WATCH**，但**新钱更差**：避险买盘推 +14.1% 到轮动新高（**唯一上涨**），base IRR +2.7%→**~0%**；存量 HOLD 但**倾向 TRIM**（41.7x 近"绝对贵" + 6 个更便宜同侪）。**[价/regime]** |
| 5 | **AMZN** | good_business_wrong_price_capex_reinvestment | good | WATCH / HOLD | 0% / 0% | $178 → **$230.86** (+30%，无 MOS) | **−0.4%** *(5y)* | **价格无 MOS + owner-earnings 桥不闭合**（$200B capex 拆分 O4） | CLEAN (F) | **WATCH→WATCH**。价 −5.5%，base IRR −1.5%→**−0.4%**、bull **首次过线 +8.9%**，但 base 仍 ~breakeven；**锁在 print 前**（Q2 7/30）。**[价—轻改善]** |
| 6 | **GOOGL** | great_business_no_margin_of_safety_capex_audit_regime | good | WATCH / HOLD | 0% / 0% | $117 → **$333.71** (+185%，无 MOS) | **−1.5%** *(10y)* | **价格无 MOS**（~60x OE，连 bull 10y +7.7% < 8%）；buybacks $0，发优先股+债供 capex | CLEAN (**T**) | **WATCH→WATCH**。Q2(7/22) **FCF 转负 −$5.9B**、capex 指引上调 $195-205B、**M4 −1→−2**；价 −9.3% 但 **TTM FCF −20% 同步** → mkt-cap/FCF 反而更贵(~76.6x)，无 MOS。**[财报—警告兑现]** |
| 7 | **TSLA** | narrative_premium_cyclical | **uncertain** | WATCH / HOLD | 0% / 3% | $160 → **$307.44** (~2×，无 MOS) | **−12%** *(5y)* | **利润池坍塌**（从"价格"转来）：op margin 1.4%、op income −57%、reg credits −67%、FCF 转负 | CLEAN (**T**) | **WATCH→WATCH；存量 TRIM→HOLD**。Q2(7/22) op margin 4.6%→**1.4%**、FCF **转负**、**M4 −1→−2**；但 −23% de-rate **已执行 6/19 的 trim** → 存量 TRIM→HOLD、M6 −2→−1。**[财报+价]** |

> **IRR 口径注**: MSFT、GOOGL 为 **10 年** 口径（+9.1% / −1.5%），其余为 **5 年**；排序按各卡自报 base 对 8% hurdle 的相对位置。**没有一家新钱 verdict 变档**——7/28 的价改善(4 家)与 regime 风险抬升相互抵消，全部维持 6/19 的两轴结论；变化都在 IRR/MOS 与存量微调里。
> **ceiling**: AAPL(~55%)/TSLA(~57%) 完整度落 40–60 带 → ceiling=WATCH；其余落 60–80 带 → ceiling=STARTER，但 GOOGL/AMZN/NVDA/META 被价格(或价格+定时)进一步压到实际 WATCH。仅 MSFT 的完整度 ceiling(STARTER) = 实际 verdict，且**由完整度封、非价格**（唯一有正 MOS 者）。

**逐名 Δ 的驱动归类**（价 / 财报 / regime）：
- **只有 GOOGL、TSLA 是"财报驱动"**（dq2=true，Q2 实数把 M4 打到 −2）——两者的坏消息都是 **capex/margin 吃掉 owner earnings 的机制第一次兑现**，不是价格。
- **AMZN、NVDA、AAPL、META 是"价格/regime 驱动"**——4 家里 3 家（NVDA/AMZN + GOOGL 价格端）跌出更好的入场 IRR，但**没一家跌进 MOS**；AAPL、META 是反向（涨了/没变便宜）。
- **MSFT 是"价格+定时驱动"**——涨 3.7% 削薄 MOS + 24h 后双二元，触发 init 4%→3% 与存量 ADD→HOLD。

---

## 2. 单因子集中度检查（METHODOLOGY §5 · 一句话判断，不做协方差）

**会一起跌——而且 7/28 就是它当场跌给你看。** 这七名几乎全部坐在同一根 **"AI capex 周期 + 流动性"** 因子上：NVDA 卖铲子、MSFT/AMZN/GOOGL/META 花 $125–205B/yr 买铲子建数据中心、AAPL 借 Google 云/Nvidia GPU 租算力、TSLA 的估值压在 AI/自动驾驶叙事上——**7/28 的半导体暴跌 + 轮动 = 这根因子在实时 de-rate**：6 家在同一天/同一周相关性地跌 5.5%~23%（NVDA 领跌 ~$300B），唯一上涨的 AAPL 也只是"资金从 AI-capex 逃向防御"这**同一根因子的反向表达**，不是独立敞口。更关键：叠加用户**已持有的 BTC / GOOGL / NBIS**——按 §5 这三者也全在"AI + 流动性"上（BTC 吃流动性、GOOGL 与 NBIS 直接是 AI capex），其中 **GOOGL 用户本就持有**，所以在这七名里再买任何一个（尤其再买 GOOGL = 字面意义上加倍同一个名字）**= 把一个本已隐藏的单一押注加倍，而不是分散**。7/28 已经证明了这本书会一起动。直白结论：组合层面的真实风险不是"选错某一家"，而是**整本书押在同一件事（AI capex 能否转成 FCF + 流动性不收紧）会不会发生上**；即便逐名 verdict 都对（MSFT 是真有 MOS 的 STARTER），把它们一起买进来仍会让这根因子成为压倒性的单敞口。**能分散的是因子正交的名字**（与 AI-capex/流动性低相关的消费/医疗/能源/防御 + ~5% 机会仓现金），而不是在 Mega7 里换哪一家。操作落点：本批即便开仓，也应**把整个 Mega7 + BTC/GOOGL/NBIS 当成一个仓位来管**，新增只能是**替换/收敛**这根因子的敞口（例如只留 MSFT 作单一表达），而非往同一注上再叠第 4、5、6 个名字。

---

## 3. 跨名一致性（同一套宏观假设是否被一致地套到 7 家）

三条宏观假设**基本一致地**贯穿 7 卡，无口径矛盾：

- **AI-capex 周期（审计年）——一致。** 4 个 capex 支付方（MSFT/GOOGL/AMZN/META）被同一问题压顶："$125–205B/yr 多久转成 FCF"；capex 接收方 NVDA 被反过来测"客户 capex 的持续性"；capex-light 的 AAPL 被当**相对受益方**（不被这条测）；TSLA 自己的 capex +142% 且 FCF 转负 → 被同一条审计**直接惩罚**。同一框架、按角色分流，一致。
- **利率 / FOMC-Warsh（7/29 偏鹰）——一致。** 7 卡全部把 FOMC 记为**长久期资产的多重压缩风险**（AAPL 41.7x、MSFT 22x 退出、GOOGL ~1.7% 收益率、AMZN 杠杆+贴现率双打、NVDA、META、TSLA），无一家漏掉或双标。
- **CXMT / 内存威胁——一致且正确分型。** 5 个内存**买方**（AAPL/MSFT/GOOGL/AMZN/META）一致判为**成本顺风、非护城河威胁**（更便宜 DRAM 降 capex 元件通胀）；NVDA 判为 **sentiment/需求信号**（SK 海力士 HBM 放缓是 AI 硬件降温的领先探针，CXMT 属"China chip fears"的情绪面，NVDA 非内存制造商 → 不是直接护城河威胁，真正的耐久性威胁是 custom-silicon）；TSLA 明确 **N/A（无内存敞口）**。每卡都正确识别了自己是买方/硬件邻近/无关，无矛盾。

**唯一需点名的跨名张力（非假设矛盾，是组合级反身耦合）**：NVDA 卡把 7/28 崩盘判为"crowded-trade 修正、**非需求机制破裂**"（DC +92% 仍在），而 MSFT/GOOGL/AMZN/META 卡的**熊侧**恰恰是"capex 审计逼迫 hyperscaler 削减 capex"。**这两件事不能同时为真**：hyperscaler 若真为满足审计而砍 capex，那正是 NVDA 的需求。逐卡各自自洽，但整个系统里 **NVDA 的 bull = 四个 capex 支付方的 bear**——这条反身回路不是"谁写错了假设"，而是 §2 单因子集中度在名字之间的具体传导，恰恰强化了"把它们当一个仓位管"的结论。

---

## 4. 诚实状态（honest status）

7 家全部 **DECISION_DRAFT 级**，不是 COMPLETE：AAPL ~55% · TSLA ~57% · META ~60% · AMZN ~62% · MSFT ~63% · NVDA ~65% · GOOGL ~72%。每家都有显式 OPEN（多为 capex 维护/成长拆分 + ROIC、proxy/operator 细节、分部利润、owner-earnings 桥），blocking 项已正确封顶 verdict。**本批的额外临时性来自定时**：5/7 锁在 Q2-2026 print 之前，4/7 在 as_of 后 48h 内出财报（MSFT/META 7/29、AAPL/AMZN 7/30），NVDA 8/26；只有 GOOGL/TSLA 带已报实数。Checker 7 家全 **CLEAN**，仅非阻断 nit（如 MSFT 的 52 周高 555.45 vs PLAN 542.07 的 vendor 口径差、若干 T6 active_litigation WARN 已诚实上浮、NVDA 跨档案遗留的 6/19 IC panel 建议标 superseded）。逐名打磨到 COMPLETE（补一手、闭合 owner-earnings 桥、并入 7/29–8/26 的 print、升完整度 >80% 解封 CORE 讨论）是 follow-up，不在本批一遍内承诺。

---

*产物：本汇总 `mega7_synthesis.md`。dashboard 由 orchestrator 另建。*
