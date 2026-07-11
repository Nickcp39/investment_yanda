# NVDA Robotics Lens — as_of 2026-07-10

> **本节回答 batch thesis（PLAN.md §1）。核心一句：买 NVDA 是买 AI 数据中心算力（~92% 营收），不是买机器人 alpha。机器人是嵌在平台里的一张近乎免费的看涨期权，不是今天在赚钱的可买瓶颈。**

来源分级：机器人/汽车段收入数字为 A1/A2 一手（8-K/CFO commentary）+ B1 聚合交叉；产品/客户为 A2 公司公告 / B1 媒体；humanoid 量级为 OPEN。

---

## (a) robotics_revenue_pct — 机器人真实收入占比

**结论：机器人/具身智能不是 NVDA 单独披露的收入行。它是"Automotive"市场平台（FY26 $2.35B ≈ 总营收 1.09%）里的一个子集，而该平台本身以自动驾驶 DRIVE design-win 为主、机器人为辅 → 纯机器人收入 well under 1%（估 ~0.3–0.5%，未披露）。**

| 口径 | Q1 FY27 / FY26 值 | 占总营收 | 来源 |
|---|---|---|---|
| Data Center（AI 算力）| Q1 FY27 **$75,246M** | **~92%** | S001/S002 (A1/A2) |
| Graphics（Gaming+ProViz）| Q1 FY27 $7,065M | ~9% | S002 |
| Edge Computing 桶（新口径：含 PC/游戏机/工作站/AI-RAN/**机器人+汽车**）| Q1 FY27 **$6,369M** | ~7.8% | S102 (A2 CFO commentary) |
| **Automotive 平台（旧口径，含 DRIVE 自动驾驶 + robotics）** | **FY26 $2,350M**（+39% Y/Y；Q4 FY26 $604M）| **~1.09%** | S101 (B1，回挂 8-K) |
| 纯 robotics/embodied-AI（Jetson+Isaac+GR00T dev business）| **未单独披露** | **<1%（估 ~0.3–0.5%）** | OPEN (O7) |

- 关键：Q1 FY27 新口径把机器人+汽车折进"Edge Computing"$6.37B，这个桶被 **游戏/PC/工作站（GeForce/RTX）主导**，机器人只是尾巴。旧口径 Automotive $2.35B 里，多数是车厂 DRIVE design-win，不是机器人。
- **对照 NVDA 之于 AI 算力**：DC $75.2B (+92%) 是"需求已暴增+卡死瓶颈+已在赚大钱"的真龙头；机器人段在 NVDA 内**连一行独立收入都不够格**。

## (b) 需求是真是预期（real-now cash vs anticipation）

**分层判断：**
- **已发生现金（real-now）**：汽车 DRIVE design-win，FY26 $2.35B、+39% Y/Y、Q4 $604M —— 真实季度收入，但**是自动驾驶不是机器人**，且仅 ~1%。
- **机器人这块 = 主要是 anticipation**：真实在卖的是**开发套件/模块级**硬件——Jetson Thor / Jetson T4000 模块（$1,999/颗 @1,000 量，S103）、IGX Thor 工业边缘可用；平台侧 Isaac / GR00T / Cosmos / Omniverse 开放模型 + 具名生态客户（Boston Dynamics、Caterpillar、Franka、LG、NEURA，S103）。**这些是 dated 的产品/生态事件，不是 dated 的机器人营收**——humanoid 起量的收入体量仍未进报表，是期权不是现金。
- 证伪口径：若机器人真"暴增+在赚钱"，NVDA 会像当年 DC 那样把它拆成独立平台行并给 +xxx% Y/Y。**至今没有 → 判 anticipation。**

## (c) CAPITAL_CYCLE lens（针对机器人段判）

```
applicable:     partial / largely N/A（机器人段）
stage:          early / pre-inflection（unknown 拐点）
supply_barrier: high（Jetson 算力 + CUDA/Isaac/Omniverse 软件栈、开发者标准）—— 但该段尚未产生超额回报
read:           机器人段目前几乎没有可衡量的"超额回报不均衡"可供资本周期填平——它太小、太早。
                平台位置骑的是与 DC 同源的 CUDA/软件结构壁垒（HIGH，非商品），但因为还没赚到钱，
                capital-cycle 这个"高回报引来供给卷平"的机制在机器人段基本 N/A（没有高回报可卷）。
                真正需要用 capital-cycle 判的是 NVDA 的 DATA CENTER/GPU 段（partial / late? / 壁垒
                CUDA-high vs 裸算力-low）——与 06-20 读法一致，未变。我们不知道 humanoid 拐点时点。
caution:        NONE material（机器人段不是 late/peak，反而是未变现的期权；不因此加也不减 verdict）。
                DC 段的 caution 见下：仍是 partial-late 观察项，非 PEAK 定论。
```

> 天真守卫：机器人这里**看不到** demand>>supply 的可见稀缺+高价+ATH margin，所以**不触发** late-cycle 卖点警报；它是"还没开始"而非"见顶"。反过来，NVDA 的**买点风险在 DC 段的周期位置**（pull-forward + custom-silicon），不在机器人。

## (d) 真瓶颈 vs 概念（可证伪的定价权/护城河）

- **平台/开发者层：真瓶颈（有牙齿）**。Jetson 边缘算力 + CUDA + Isaac/GR00T/Omniverse 仿真构成可证伪的转换成本——机器人开发者一旦在 CUDA/Isaac 上标准化，迁移成本高（同 DC 的 CUDA 锁定机制，只是规模小几个量级）。这**不是纯概念**。
- **但在当前收入尺度：仍主要是概念/期权，不是已变现瓶颈**。护城河真实存在，却还没转成机器人现金流。**已变现的真瓶颈是 AI 数据中心算力，不是机器人。**
- 证伪触发：见 monitor（NVDA 把 robotics 拆成独立收入行 + 连续 +xxx% Y/Y = 从概念转真瓶颈的信号）。

## (e) 拆分：机器人期权价值 vs 主业价值 —— 现价买的是什么

**在 $210.96 / 市值 ~$5.145T：**
- **几乎 100% 的市值 = AI 数据中心算力生意**（~92% 营收的卓越瓶颈），按 forward ~28x 定价。三情景 DCF（base 5y IRR +4.7%）**完全由 DC run-rate 驱动**，机器人未建模。
- **机器人/具身智能 = 一张嵌在平台里的近乎免费的看涨期权**：对当前现金贡献 ~nil，未被单独估值。你**没有为机器人付溢价**，你也**拿不到"机器人 alpha"**——你买的是 AI 算力，附赠一张机器人彩票。
- **反向看 batch 框架**：若把"车/工业/机器人"当成本批要买的"主业"，那在 NVDA 里它只有 ~1% —— **为机器人敞口买 NVDA = 99% 买的是别的东西（AI 算力）**。想要纯机器人 exposure，NVDA 是错误载体（见本批 TER/ON/NOVT）。

---

## 对 verdict 的影响

**机器人 lens 不改 verdict，反而钉死"这不是机器人买点"**：现价 WATCH 的理由是 AI 算力段无安全边际（base IRR +4.7% < 8%），机器人既不加分（未变现、无独立现金）也不减分（非见顶、是期权）。机器人**不构成在 $210.96 加仓的任何增量理由**。

## OPEN（机器人段特有）
- O7: 纯 robotics/embodied-AI 收入（Jetson+Isaac dev business）金额——NVDA 未单独披露，只能估 <1%。
- O8: humanoid 起量的收入量级与时点（期权，未建模；拐点不可知）。
