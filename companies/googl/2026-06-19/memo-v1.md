# Alphabet (GOOGL) 买方决策 Memo

| 字段 | 值 |
|---|---|
| **Date** | 2026-06-16 |
| **Analyst** | 买方研究 OS · 第 9 步（决策 Memo），承接 IC Panel（第 8 步）+ Audit（第 7 步） |
| **Version** | v1 |
| **Verdict** | **WATCH** |
| **Verdict ceiling** | **WATCH**（audit §11.2：模块齐全、硬规则封顶已解除；ceiling 来自 driver + valuation 实质——收入上行真实，但 AI capex / owner earnings 证据未闭合，且 $370 现价无安全边际） |
| **Position rule** | **Watch only / 0% 仓位（个人 & panel 均不开仓）**；需要 driver 证据收敛 + 安全边际价格，才重开 panel 讨论 starter（试仓 1–3%） |

> 本 memo 是把扎实研究落成"可执行 + 可复盘"的结论：**先拆生意驱动，再谈价格**。五灵魂五票一致 WATCH、段永平主审 WATCH（个人 0%），与本 memo verdict 完全一致。所有关键数字挂 `[source_id]`（一手 A1 = SEC EDGAR），上游论证 Reference 指向对应分析 md，不在本 memo 重复推导。

---

## 1. One-Line View（一句话观点）

Alphabet 是一门"用十亿级免费产品聚合商业意图、再卖给广告主 + 卖算力给云客户"的高质量双边平台生意（Services 分部营业利润率 ~40.7% [GOOG.A1.2025K.009/.010]、Cloud 两年从微利做到 $13.9B 营业利润 [GOOG.A1.2025K.012]）——**之所以 WATCH 而非买入，不是只因为价格，而是收入概率树和支出概率树还没闭合：Search +19%、Cloud +63%、backlog >$460B 说明收入上行真实，但 2026 capex $180–190B 且 2027 继续增加，使 owner earnings 是否能跟随收入增长仍未证实；$370 = 69x owner earnings 只是最后一道安全边际检查。**

---

## 2. Decision Question（决策问题，抄开题可证伪问题）

> 本 memo 支持的决策：**Alphabet 的收入增长机会、收入下降风险、支出上升压力和支出下降机会，是否已经足够清楚，使我们能承保 10 年 owner earnings？若不能，还需要什么证据 / 什么价格才进入 starter？**

可证伪形式（开题问题）：**"Google 的增量收入，是否会超过 AI capex、折旧、TAC、SBC 和监管成本的增量，从而让 owner earnings 在十年维度持续增长？"**
- 证伪条件：若 Search/YouTube/Cloud 的增量美元不能转成 FCF/share，或 AI capex 只是防守性支出，则 owner earnings 会被稀释；即使收入增长，也不能买。
- 当前裁决：**答案还不够清楚，因此 WATCH**。在这个前提下再看价格：$370 对应三情景 IRR bear −13.1% / base −3.0% / bull +5.2%，全部 < 8% [valuation §3]，没有给研究误差留安全边际。

---

## 3. What Must Be True（多头论点成立的前提，每条挂 1 条 kill criteria + 1 个监控指标）

> 这些是"能承保 10 年 owner earnings，并在合理价格买入长期持有 GOOGL"成立的前提。前五条解决业务驱动，第六条解决安全边际；二者缺一不可。每条带 checkbox，对应 §11 的 K-A..K-E 与 monitor.md 的 KPI。

- [ ] **WMBT-1｜搜索现金牛不被 AI 界面结构性绕过**：Search & other 在 AI Overviews/AI Mode 渗透上升的同时仍维持双位数增长（当前 Q1'26 **+19%** [GOOG.A1.2026Q1.004]）。→ 对应 **K-A**（连 2 季同比 ≤+8% 且管理层归因 AI）；监控指标 = Search & other 同比增速。
- [ ] **WMBT-2｜AI capex 是高回报成长而非低回报黑洞**：capex 高峰后 2–3 年内 FCF per share 重新增长、incremental ROIC 维持高位（当前 capex/OCF：FY25 ~56%、Q1'26 ~78% 已踩线 [GOOG.A1.2025K.016/.015 / GOOG.A1.2026Q1.024/.023]，TTM FCF $64.4B 已被压缩 [GOOG.A1.2026Q1.025]）。→ 对应 **K-B**；监控指标 = FCF per share 趋势 + capex/营业现金流比率。
- [ ] **WMBT-3｜管理层对 AI capex 有可见的回报纪律**：在 earnings call / 公开沟通给出 capex 的 hurdle rate / 预期 ROIC / 利用率框架（当前一手披露中**该框架不存在** [operator 红旗1 / audit §8]）。→ 对应 **K-C**；监控指标 = 管理层是否披露 capex ROI 门槛 / 是否出现数据中心/TPU 减值。
- [ ] **WMBT-4｜监管止于罚款或行为救济，而非结构性拆分**：DOJ adtech / search 最终救济为纯罚款或行为救济（如 EC 模式），默认搜索分销协议得以保留（当前 DOJ adtech 部分败诉、结构性救济待裁、"could have a material adverse effect" [GOOG.A1.2025K.026 notes]）。→ 对应 **K-D**；监控指标 = DOJ adtech 救济判决形态（罚款 / 行为 / 结构剥离）。
- [ ] **WMBT-5｜owner earnings 区间可收敛到可定 base**：拿到维护 vs 成长 capex 拆分 / 单位经济，使 owner earnings 从 $52–82B 大区间收敛（当前完全压在不可观测拆分上 [financial_quality §1.3 / valuation §2]）。→ 证据触发（可上修 verdict）；监控指标 = 10-K 现金流量表 D&A 坐实 + 年度 capex 维护/成长拆分披露。
- [ ] **WMBT-6｜证据和价格同时给安全边际**：先让 owner earnings 区间收敛，再要求买入价隐含十年 IRR ≥ 8%（≈ 价格 ≤ ~$134 见 8% 门槛、≤ ~$113 见 base 10%）。当前 $370 严重违反（IRR base −3.0% [valuation §3]）。→ 对应 **K-E**；监控指标 = driver 证据状态 + 股价 vs buy-below 阶梯（$134 / $113 / $95 / $48）。

> **裁决**：WMBT-1 当前成立（搜索仍 +19%）、WMBT-4 待裁、WMBT-2/3/5 证据缺失（押注非定价）、**WMBT-6 明确不成立**。verdict 锁死在 WATCH 的原因是双重的：driver 证据还不能承保 owner earnings，价格也没有给研究误差留安全边际。

---

## 4. Business Quality（生意质量）

**Reference**：`business_model.md`（H1 生意模式 + 生意质量记分卡）、`financials/financial_quality.md`（owner earnings 桥）。

- **裁决**：生意质量是 10 年级别的好生意——付费意愿极强（广告主为可衡量商业意图持续付费 + Cloud backlog "over $460B" [GOOG.A1.2026Q1.010]）、规模经济显著（搜索边际成本近零、Cloud 营业利润率两年 ~17.8%→32.9% [GOOG.A1.2026Q1.015]）、能力圈友好（清晰的双边平台 + 基础设施生意）。
- **但 owner earnings 质量是死穴**：TTM 报表净利 $160B 里约一半是不可重复的 $36.9B 未实现股权收益 [GOOG.A1.2026Q1.022]，**干净读数是营业利润 +30%** [GOOG.A1.2026Q1.018]；真实 owner earnings 仅 **~$51–82B**（financial_quality §1.4），且营收 3 年 +31% 而 derived FCF 从 $69.5B（FY23）原地踏步到 TTM $64.4B [financial_quality §2]——**增长正被 capex 吃掉**（教科书红灯：营业利润涨、每股自由现金流不涨）。

---

## 5. Moat（护城河）

**Reference**：`moat_map.md`（H5，7 条护城河逐条挂证据 + 攻击面 + ROIC–WACC 透镜）。

- **最强护城河**：搜索习惯与默认分发（H5-1，**Strong**，Services ~40.7% 利润率 + Search +19% 是当下硬证据 [GOOG.A1.2025K.010 / GOOG.A1.2026Q1.004]）；广告拍卖流动性自有面（H5-2，**Strong**）；Cloud 规模 + AI 基建（H5-4，当下 **Strong**，+63%/32.9%/backlog $460B [GOOG.A1.2026Q1.010/.015]）。
- **最弱 / 被高估**：TPU 成本优势（H5-6，**Weak**，facts 零量化）、人才/模型（H5-7，**Weak**）——市场最爱讲、最缺一手证据的两条。
- **裁决**：整体 **Strong 但处于形态切换期**——存量护城河（历史高 ROIC、宽 ROIC–WACC spread）扎实，但**增量护城河未证实**："AI capex 抬升后增量资本能否维持高回报"目前只有间接乐观信号（Cloud 利润率/backlog），无 owner earnings 桥验证 [moat §2.2]。核心攻击面 = AI 原生回答绕过搜索框（已现负面信号：Google Network 营收 Q1'26 已同比下滑 [GOOG.A1.2026Q1.006]）+ 监管强制开放默认入口。

---

## 6. Operator（管理层 / 资本配置承保）

**Reference**：`operator_underwriting.md`（H6，People Map + 8 维记分卡 28/40 + 红旗）。

- **裁决**：把 $180B+/年的 capex 决策权交给这群人长期配置 = **有条件可信（中性偏正，28/40）**。强在创始人契合度（Page/Brin 是搜索发明者，AI 是原生战场）、长期导向（顶住市场做回购暂停 + 多年把 Cloud 从微利养到大幅盈利）、披露坦诚。
- **两点钳制**：(a) **$180–190B AI capex 无一手可见的回报纪律框架**（hurdle rate / 利用率 / 回报回顾均不存在 [operator 红旗1 / GOOGL-424B5-2026-06.009]）→ 无法证伪 FOMO；(b) **52.7% 投票权 + 持股<11%** [GOOG.A1.PROXY2026.004] → 押注错误时外部股东无投票纠错杠杆。**双层股权双向性**：押注对=长期主义护城河，押注错=无法叫停的放大器，而判断对错的 capex ROI 证据恰恰缺失。
- **Berkshire 正确读法**：$10B 是 Section 4(a)(2) **私募融资定价**（Class A @~$351.81 / Class C @~$348.20 [GOOGL-424B5-2026-06.001/.002/.004]）= 参与了一轮 AI capex 融资，**不是抄底背书**——"巴菲特买入=安全边际"叙事正式从决策依据剔除。

---

## 7. Inversion（反演 / 失败地图）

**Reference**：`inversion_map.md`（H7，F1–F9 失败路径 + Kill Criteria）。

如果我想让 Alphabet 十年内失去超额利润，我会攻击（最致命三条）：
1. **F1×F3 合流（头号永久减值路径）**：AI 答案压低单 query 变现（F1）+ 被迫越投越多 capex 防守（F3）= **收入仍增、owner earnings 被永久稀释**。单看任一项都可对冲（搜索仍 +19%、Cloud 已转盈），叠加且 incremental ROIC 撑不住时不可逆 [inversion §0/§7]。
2. **F2 监管结构性救济（尾部加速器）**：DOJ adtech 被迫剥离 ad exchange / 禁默认搜索协议——管理层自标"could have a material adverse effect" [GOOG.A1.2025K.026 notes]，落地则切走高毛利广告利润池，bear 下行锚（~$48）需再下修。
3. **F9 估值过高（买入即锁定）**：即便生意不坏，$370 买入把十年 IRR 压到低于机会成本——与生意质量正交的纯价格风险。
- **裁决**：市场对 F1/F5 是在"押注"而非"定价"（缺单位经济证据 [inversion §3]）；所有失败路径与所有估值不确定性**卡在同一个不可观测变量：维护 vs 成长 capex 拆分（= incremental ROIC）**。

---

## 8. Financial Quality（财务质量 / owner earnings）

**Reference**：`financials/financial_quality.md`（H2，会计→经济重构）、`model/owner_earnings_bridge.csv`。

- **裁决**：会计质量本身高（收入真实、无激进确认），但 **2026 版 Alphabet 的"会计利润"严重高于"owner earnings"**：
  - owner earnings 区间 FY2025 **~$52B（防御）–$77B（成长）**、TTM **~$51–82B**——仅为报表净利的 40–58% [financial_quality §1.2/§1.4]。
  - SBC 是真实成本 **$27.1B**（Note 13 总额，保守口径 [GOOG.A1.2025K.023]），回购暂停（Q1'26 $0 vs Q1'25 $15.1B [GOOG.A1.2026Q1.027]）使稀释正在"裸露"，股数由降转升（12,088M→12,116M）。
  - 资本结构剧变：FY25 净发债 ~$64.6B、Q1'26 再 +$31.4B、$80B 股权融资专投 AI capex [GOOG.A1.2025K.021 / GOOGL-FWP-2026-06.001]——从"净现金自筹"转向"外部融资支撑增长"。
- **硬 GAP**：仅 3 年序列（FY23–25 + Q1'26/TTM），Buffett 10 年"漏桶"分析无法做 [financial_quality §2]。

---

## 9. Valuation & Margin of Safety（估值与安全边际）

**Reference**：`valuation.md`（H8）、`model/scenario_model.csv`（IRR 引擎已逐项勾稽，audit §6）。

| 项目 | 值 | 来源 |
|---|---:|---|
| **Current price** | **~$370** | WebSearch 2026-06-15（区间 $365–373；ATH $402.38；备用锚 Berkshire 私募 $348–352 [GOOGL-424B5-2026-06.002/.004]） |
| 市值 | ~$4,483B（$4.48T） | derived = $370 × 12,116M [GOOG.A1.2026Q1] |
| 起始 owner-earnings yield | **1.45%（P/OE 69x）** | base OE $65B / 市值 [valuation §3] |
| **Base IRR（10y @ $370）** | **−3.0%** | [valuation §3 / scenario_model.csv] |
| Bull IRR（10y @ $370） | +5.2% | 连最乐观假设也 < 8% 门槛 [valuation §3] |
| **Downside IRR（bear, 10y @ $370）** | **−13.1%** | [valuation §3] |
| **Required buy price（base 10% starter 锚）** | **~$113** | −70% vs $370 [valuation §4] |
| 8% 最低门槛价 | ~$134 | −64% [valuation §4] |
| Core（12%） / Deep value（15%） | ~$95 / ~$75 | [valuation §4] |
| 下行保护锚（bear 仍 8%） | ~$48 | −87% [valuation §4] |

- **裁决（安全边际是否真实）**：**否（在当前价）。** 逐条 fail Buffett 清单第 5 节——保守（bear/base）估值远**低于**价格；起始 yield 仅 1.45%，低增长情景今天买入会永久跑输；资产负债表非但不护底，反而在**加杠杆做 capex**，$80B 现金/融资全砸 capex，对 $4.48T 市值缓冲微不足道 [valuation §4]。
- **要在 $370 赚 10%**，需 owner earnings 十年复合 ~22%（≈十年做到 7x），即把历史峰值增速 + capex 同时见顶回落两个乐观假设叠加 [valuation §3]。
- **审计交叉确认**：估值假设**偏保守**（bull 已给 revenue CAGR 15%/退出 26x，IRR 仍 +5.2%；DOJ 拆分尾部尚未压进 bear），**真实安全边际只会更差**，无"假设太保守"翻案空间 [audit §9]。

---

## 10. Evidence Against The Thesis（反方证据 / 逼自己写空头的反驳）

> 以下任一成立，则"WATCH 等回调"可能是错的（要么我会永远等不到、要么我低估了生意）：

- [ ] **优质资产很少打到 −70%**：base 10% 的 ~$113 是 −70%，历史上 Alphabet 这种公司极少回调到此——"等回调买入"可能是在等一个永远不来的价格，机会成本（QQQ 4 年 2.03× 基准）持续流失（Marks→Buffett critique [ic_panel §2]）。
- [ ] **搜索韧性可能被系统性低估**：在 ChatGPT/AI 答案盛行两年后，Q1'26 Search & other **仍加速到 +19%** [GOOG.A1.2026Q1.004]——若 AI Overviews 的 RPM ≥ 传统搜索（管理层若披露），F1 空头路径应被推翻，owner earnings 起点上移、base IRR 改善 [inversion §6]。
- [ ] **capex 可能是高回报扩张而非黑洞**：Cloud 两年从 $1.7B 微利做到 $13.9B 营业利润 [GOOG.A1.2025K.012] + backlog $460B [GOOG.A1.2026Q1.010] 是"重资本投入跑出回报"的先例；若 2–3 年内 FCF per share 重新增长，WMBT-2 成立，OE 起点应取 $80B 成长端 [inversion §6]。
- [ ] **退出倍数假设可能偏低 / 偏高两难**：base 用 20x，audit 自承对"FCF 被 capex 永久压低"的公司可能偏高（→IRR 更负）；但若 AI 兑现、市场维持高倍数，则 bull 26x 不算激进（→IRR 改善）——倍数本身是宽误差带 [audit §9 / valuation §6]。
- [ ] **段永平 H&H 13F 翻倍是真实一手**：H&H Q1'26 持 Class C 翻倍至 3.706M 股 [HH-13F-2026Q1.001]——虽按纪律降权（13F ≠ 个人实时操作、市值变化≠净买入 [facts Contradictions #4]），但仍是"懂行者在加仓"的弱反向信号，不可完全无视。

---

## 11. Kill Criteria（沿用 panel K-A..K-E，可观测阈值 + 当前读数）

> 任一触发 = 重新审视多头论点 / 下调或放弃"等回调买入"计划（"便宜"可能是价值陷阱）。三态跟踪见 monitor.md。

- [ ] **K-A [F1 搜索变现，最强单一信号]**：**Search & other 收入连续两个季度同比增速 ≤ +8%**，且管理层归因于 AI 答案/界面迁移（非宏观/汇率）。当前 Q1'26 **+19%**（绿，离触发尚远）[GOOG.A1.2026Q1.004]。
- [ ] **K-B [F3 capex 黑洞 / owner earnings 胜负手]**：**FCF per share 连续两年下降** 且 **capex / 营业现金流持续 > 70%** 且无 incremental ROIC 回升证据。当前 capex/OCF：FY25 ~56%、**Q1'26 ~78% 已踩线**（黄，需看全年是否坐实）[GOOG.A1.2025K.016/.015 / GOOG.A1.2026Q1.024/.023]。
- [ ] **K-C [F3 资本配置纪律]**：管理层**连续两个财报周期仍无法/拒绝给出 AI capex 的回报门槛（hurdle rate / 预期 ROIC）**，或出现**数据中心/TPU 资产减值**。当前一手披露中**该框架不存在**（黄/红，区分纪律 vs FOMO 的核心）[operator 红旗1 / audit §8]。
- [ ] **K-D [F2 监管尾部加速器]**：法院/监管下达**结构性救济**（剥离 adtech 资产、禁默认搜索分销协议、强制开放平台），而非纯罚款。当前 DOJ adtech 部分败诉、结构性救济待裁、"could have a material adverse effect"（黄，未落地）[GOOG.A1.2025K.026 notes]。
- [ ] **K-E [F9 估值 / 买入纪律]**：**买入价隐含的 10 年 IRR < 8% 门槛**（≈ 价格 > ~$134；现价 $370 严重违反）。**只有价格回到 ~$113（base 10%）一带才解除 WATCH 进入 STARTER 讨论**（红，当前严重违反；以 QQQ 4 年 2.03× 历史基准作上行机会成本对照）[valuation §4 / qqq_4yr_doubling_benchmark]。

> 补充观察项（非主 Kill，季度跟踪）：Cloud 营业利润率连续 2 季回落 >5pp（当前 32.9%）；Network 负增长扩散至核心 Search（Network 已负 [GOOG.A1.2026Q1.006]）；股本由降转增（回购长期暂停 + 持续增发稀释，拐点信号）。

---

## 12. Position Decision（仓位决策）

- **当前动作：watch only / 0% 仓位**（个人 & panel 一致，五票 WATCH，主审不突破封顶）。$370 位于 avoid 区（>~$300 连 bull IRR 都 <8% [valuation §4]）。
- **进入 starter（试仓 1–3%）的明确条件**：价格回调到 **~$95–113 区间**（主审定调以 base/bear 锚为准，buy-below 取 $95–113 而非"刚够 8%"的 $134，宁可错过、不在薄边际上动手 [ic_panel §3.6]）。到 ~$113 重开 panel 评 STARTER；到 ~$95 评 Core；到 ~$48 评 deep value。
- **加仓 / 退出阶梯**（valuation §4 安全边际表）：

| 档位 | 目标 IRR | 价位 | vs $370 | 动作 |
|---|---:|---:|---:|---|
| 当前（avoid） | — | **$370** | — | **0%，不开仓** |
| 8% 门槛 | 8% | ~$134 | −64% | 进观察，尚不构成 starter |
| **Starter 主锚** | 10% | **~$113** | −70% | 重开 panel 评 STARTER（试仓 1–3%） |
| Core | 12% | ~$95 | −74% | 核心仓 5%+ |
| Deep value | 15% | ~$75 | −80% | — |
| 下行保护锚 | bear 8% | ~$48 | −87% | "即便 bear 兑现仍不永久亏损" |

- **重要约束**：即便价格跌到 buy-below，若 K-A / K-B / K-D 已触发，需先确认多头论点未被结构性破坏——**便宜可能是价值陷阱**，下行锚（~$48）届时需再下修。

---

## 13. 必答三问（Final IC Notes）

1. **错在哪会知道（What would tell me I'm wrong）？**
   - 若 WMBT-1/2/3 兑现（搜索在 AI 渗透下持续双位数 + capex 高峰后 FCF per share 回升 + 管理层给出 capex ROI 框架），且价格**始终不回调到 ~$113**——则"等回调"是错的，我会因坚持价格纪律而永久错过一个证明了 incremental ROIC 的优质复利机会（机会成本 = QQQ 4 年 2.03× 基准）。反向：若在 ~$113 建仓后 K-A/K-D 触发（搜索结构性失血 / 监管强拆），则"便宜买入"是错的，落入价值陷阱。
   - **复盘锚**：每次 review 对照 §3 六条 WMBT 的状态变化 + §11 五条 K 的三态读数。

2. **哪个单一事实会改变主意（The one fact that flips the view）？**
   - **维护 vs 成长 capex 拆分（= incremental ROIC）**。这一个不可观测变量同时决定 Buffett 的 owner earnings 死穴、Munger 的 F1×F3 胜负手、段永平"真懂吗"的答案、Marks 的赔率分母、Klarman 的下行锚 [ic_panel §2 收敛点]。一旦 10-K 现金流量表 + 管理层口径能把 owner earnings 从 $52–82B 大区间收敛到可定 base，base IRR 从"宽误差带的点估计"变成可定论——verdict 可上修（但仍受价格封顶）。

3. **下次何时更新（When to update）？**
   - **Q2 2026 财报**（预计 2026-07 下旬，见 monitor.md 事件日历）——重点看：① Search & other 同比增速是否仍 ≥ 双位数（K-A）；② **capex 拆分披露**——是否给出维护 vs 成长 capex 拆分 / 全年 capex 兑现路径 / 任何 ROI 门槛口径（K-C / WMBT-5，解 owner earnings 收敛的唯一路径）；③ capex/OCF 全年是否坐实 >70%（K-B）；④ Cloud 32.9% 利润率多季可持续性（补充观察项）。
   - **事件触发更新**：DOJ adtech 结构性救济判决落地（K-D）→ 立即重估 bear 锚；年度 capex 指引更新（2027 "显著增加"的具体量级）→ 重估 base 落点。
   - 价格触发：跌至 ~$134 进观察、~$113 重开 panel。

---

*交接说明：本 memo（第 9 步）与 `monitor.md`（第 10 步）配套；Kill Criteria 已在 monitor.md 转为三态跟踪表，事件日历 + Change-My-Mind 日志骨架就绪。本 memo 不新增无 source_id 的事实，所有数字回挂 `facts.md` 的 verified A1。verdict = WATCH，与 IC Panel 完全一致，未突破 audit ceiling=WATCH。*
