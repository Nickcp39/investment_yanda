# SNOW Decision Card — as_of 2026-09-01

**pipeline_version**: lean-6module-v1.1 · **run_date**: 2026-09-01 · **批次**: `saas_derate_2026-09-01`
**completeness**: **~45%** · **status**: `DECISION_DRAFT`（**非 COMPLETE**）
**context_label**: `consumption_saas_recovered_no_margin_of_safety`

> ⚠️ **本卡不得标 CLEAN。** `verify_freshness.py` 因全部行情源 EGRESS_BLOCKED 无法运行
> （INC-004）。**claim_ledger 37 条中，verified 条数 = 0。**

---

## 前提修正（必须先读）

用户点名 SNOW 的理由是「跌得很凶」。**这个前提对 2026 年上半年成立，对今天不成立。**

| | 值 |
|---|---:|
| 2026 最大回撤 | **−56%**，底约 $118.30 @ **2026-04-10** |
| 现价 | **$331.43** @ 2026-08-31 |
| YTD | **+50%** · 过去一年 **+65%** · 较 2024-09 低点 **+200%** |

**SNOW 不是一个跌透的标的，它是一个崩完并创出新高的标的。**
本批 T2 命题（「往返是不是第三类」）在 SNOW 上的答案是：**是。**

---

## 锁定结论

| 字段 | 值 |
|---|---|
| as_of 价格 | **$331.43**（2026-08-31，⚠️ unverified，交叉区间 $322.78–332.78） |
| 市值 | ~**$114.9B**（derived；交叉 $111.9–116B） |
| business_verdict | **uncertain** |
| **new_money_verdict** | **WATCH** |
| existing_position_verdict | **N/A**（用户 0%） |
| suggested_initial_size | **0%** |
| suggested_max_size | **0%** |
| **buy_below** | **~$173**（base 10% IRR 锚）→ **距现价 −48%** |
| 观察线（8% 门槛） | ~$208（−37%） |
| **Trim / no-chase zone** | **N/A —— 无持仓，不适用**（若未来建仓，本栏必须补，见 NBIS 教训） |
| **binding_constraint** | **价格 + owner-earnings 锚不存在** |

## 六模块

| 模块 | 角色 | 分 | 一句话 |
|---|---|:--:|---|
| M1 证据脊柱 | confidence | **−2** | **零条 verified**。无一手文件，无可验证价格，freshness 门跑不了 |
| M2 主题/机制 | context+conviction | **+2** | 需求侧站对了：产品收入 +29%→+34% 加速，NRR 125→126%，指引上调 |
| M3 利润池/耐久 | conviction | **0** | 跨云中立是真锁定（+）；但成本结构受制于最大竞争对手，AI 负载稀释毛利（−） |
| M4 财务现实 | warning | **−2** | SBC=收入 34.2%；GAAP 净亏 $1.329B ≈ SBC；**三锚无一支持现价** |
| M5 反演/陷阱 | risk | **−1** | K-C 🔴 FIRING（SBC）；K-A 🟡 未知（DDOG 式单一 AI 客户）；K-F ⚫ 永久盲区 |
| M6 定价/仓位 | price+output | **−2** | base 10y IRR **+3.1%**；8% 门槛 $208 vs 现价 $331 |

信号向量：**−2 / +2 / 0 / −2 / −1 / −2**

## 三情景（10y IRR @ $331.43，门槛 8%）

| 情景 | 收入 CAGR | y10 收入 | OE 利润率 | y10 OE | 退出 | **IRR** |
|---|---:|---:|---:|---:|---:|---:|
| Bear | 12% | $16.8B | 20% | $3.35B | 18x | **−6.2%** |
| Base | 18% | $28.3B | 25% | $7.07B | 22x | **+3.1%** |
| Bull | 24% | $46.4B | 28% | $12.99B | 26x | **+11.4%** |

> **base +3.1% 已经假设了「SBC 从 34% 收敛到可忽略」，而这个转变一天都还没开始。**

## 三锚 owner earnings（本卡的核心）

| 锚 | FY26 OE | 市值/OE |
|---|---:|---:|
| A 公司口径（调整后 FCF，SBC 全加回） | +$1.17B ⚠️derived | **98x** |
| B 全额扣 SBC | **−$0.43B** | **负** |
| C 扣 50% SBC | +$0.37B | **310x** |

> META 的教训在这里是极端版：**换个锚不是从 0% 到 +10%，是从 98 倍到负数。**
> **三个锚没有一个支持 $331。**

## Kill criteria
K-A 单一 AI 买家集中度 **🟡 未知（O-S1，最危险）** ·
K-B AI 稀释毛利 **🟠 进行中**（76%→75%，抵消手段是一次性的 AWS 带宽降本）·
K-C SBC 不收敛 **🔴 FIRING** ·
K-D 估值 **🔴 ACTIVE（binding）** ·
K-E 集体诉讼 🟡 ·
K-F Databricks 份额 **⚫ 永久盲区**

## Runner dissent
需求侧的证据是真的好：收入加速、NRR 回升、大客户加速、指引上调，
而且 consumption 模型在 AI 时代确实站在负载增长的正确一侧 ——
`inversion_map.md` 的第 3 条反问（毛利率下降但毛利绝对额加速）本卡**无法反驳**。
但 verdict 仍是 WATCH 0%，因为**问题不在生意，在于 owner earnings 这个量在 SNOW 身上
目前不存在一个各方能同意的定义**，而三个候选定义没有一个支持现价。
**$173 的 buy_below 不是在等更好的故事，是在等一个能被承认的分母。**

## 完整度封顶说明
本库规则：<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER / >80 CORE。
**~45% → verdict 上限即 WATCH。** 即使价格跌到 $173，
**在 O-S1（单一 AI 买家）和 O-S3（FY26 调整后 FCF）补齐之前，本卡也开不出 STARTER。**

## OPEN
O-S1 单一 AI 公司大额合同（**最重要**）· O-S2 AI 原生客户收入占比（批次 T1 主命题未答）·
O-S3 FY26 调整后 FCF 绝对值 · O-S4 股数序列与净稀释率 · O-S5 客户集中度一手数据 ·
O-S6 集体诉讼进展 · O-S7 Cortex Code 是否单独披露收入
