# EROC Step 0 Search Plan

按 [frameworks/info_collection_pipeline.md](../../../frameworks/info_collection_pipeline.md)
执行 Stage 1 产出。指导 Stage 2 (按 block 执行) 收集到 `raw/`。

**Status 图例**: ⏸ pending · 🟡 in-progress · ✅ done · ⏭ skipped (acceptable gap) · ❌ blocked

最后更新: 2026-08-13

---

## 触发来源

用户提供的一篇中文自媒体文章截图（`美股投资网 / TradesMax`，101 赞 / 544 转），
主张要点：Q2 收入 $39,878K（同比 **−41.7%**）、毛利率 18.6%（去年 22.2%）、
调整后 EBITDA **亏 $1400 万**、backlog **$17 亿**、现价约 **$17**，
文章结论是"盯交货速度 / 收入爆发 / 毛利率回升三件事"。

> ⚠️ **这是 SENTIMENT 层输入，不是 EVIDENCE 层。** 该文所有数字进 `claim_ledger.csv`
> 时一律先标 `unverified_secondary`，需独立源核实后才升级。
> 同时该文本身是 §舆论热度轨迹 研究的样本：**它就是"新一代热点股"正在被
> 中文自媒体推荐的现场证据**。

---

## 已确认的事实 (Stage 0 Identify 输出)

来源: 2026-08-13 WebSearch

| 项 | 值 | Tier | Note |
|---|---|---|---|
| Legal name | ERock, Inc. | A1 | 中文自媒体写作 "EROC"，实为 ERock |
| Ticker | EROC | A1 | |
| Exchange | **NYSE** | A1 | 非 Nasdaq |
| IPO date | **2026-06**（月份确认，具体日待核） | A1 | 募资 $4 亿 gross，约 2790 万股 Class A |
| CIK | 待取 | — | EDGAR 可能被出口代理拦截 |
| Sector / 子行业 | 资本品 / **分布式发电（distributed power）** | A1 | Simply Wall St 归类 capital-goods |
| 主营业务 | 为**数据中心与公用事业**提供**快速部署发电容量**，绕开电网并网排队 | A1 | |
| 最近 filing | 10-Q (Q2 FY2026)，2026-08-11/12 | A1 | businesswire 有 PR，可能被拦 |
| **特殊情况** | **年轻公司（IPO 距今 ~2 个月）** + **锁定期未到期** + **收入同比腰斩但环比 +26%** | — | 三项都要单独查 |

### Stage 0 已捕获的关键数字（待 Stage 2 核实）

| 项 | 值 | 状态 |
|---|---|---|
| Q2'26 收入 | $39.9M（环比 +26%，同比 −41.7%） | 两个方向**同时成立**，需解释基数 |
| Backlog | **$1.7B**，同比约 **10×** | ⭐ 本案核心变量 |
| 其中 | **Anthropic 470MW 订单** | ⭐ 与 lab 已有 WULF-Anthropic 线索联动 |
| 现金 | $627M 无限制现金、**零负债**、$250M 未提取信贷 | IPO 募资后 |
| 调整后 EBITDA | **−$14M** | 亏损 |

---

## 复杂度系数 + 时间预算

- 基础 1.0×
- **年轻（< 5 年公开，实为 2 个月）: +30%** → 缺乏历史财报、无 10-K、无 13F、无长期 track record
- 跨境: 否 · 加密: 否
- **本公司系数: 1.3×** → 预计 L1+L2 约 3.3–5.9 h（本次为压缩单会话跑）

> **年轻公司的特殊风险**：本 lab 的 `_newname_batch` 经验——IPO 后头两个季度
> 的 backlog 数字**没有历史兑现率可对照**，这是本案完整度的天然上限。

---

## Block 列表

### Block 1: Anchor identity ✅
Stage 0 已完成（见上表）。CIK 与精确 IPO 日归入 Block 2。

### Block 2: 身份补全 + 商业模式 ✅
- [x] 卖设备 vs 卖电（PPA/租赁/按 MW 月费）
- [x] 合同结构（take-or-pay？期限？）
- [x] 设备供应链（自制 vs 集成；依赖哪家涡轮机/发动机厂）
- [x] "快速部署"相对并网排队快多少
- [x] 管理层背景 · 双重股权 · 锁定期
→ `raw/block02_identity_business.md`

### Block 3: Q2'26 财报与订单质量 ✅
- [x] 逐项核实自媒体文章的 6 个数字
- [x] **解释"同比 −41.7% vs 环比 +26%"的基数问题**
- [x] backlog 构成：多少 take-or-pay / 多少 LOI；转化时间表
- [x] Anthropic 470MW 条款
- [x] 单位经济（$/MW，与 NBIS $40–50M/MW、IREN $8.33M/MW 对照，注意口径不同）
- [x] 现金消耗与 capex 计划
→ `raw/block03_q2_financials.md`

### Block 4: 竞争格局与瓶颈 ✅
- [x] 玩家清单（Bloom/GEV/CAT/Cummins/VoltaGrid/ProEnergy/Mainspring/PowerSecure/Aggreko…）
- [x] **设备供应是否比客户需求更硬**（燃气轮机排产已到哪一年）
- [x] 护城河检验：是壁垒还是"有钱就能做"
- [x] 环保许可尾部风险（xAI 孟菲斯先例）
- [x] 资本周期位置：新进入者是否蜂拥
→ `raw/block04_competition_bottleneck.md`

### Block 5: 估值 · 股东结构 · 情绪 ✅
- [x] 市值/EV/倍数；与 BE/GEV/GNRC/VRT 对照
- [x] 承销商与静默期后首次覆盖
- [x] **⚠️ 锁定期到期日与可解禁比例**（本案头号供给风险）
- [x] 散户情绪与 meme 化迹象
→ `raw/block05_valuation_ownership.md`

### Block 6: 一手源尝试 ❌ BLOCKED
- [ ] SEC EDGAR 10-Q 原文 · businesswire PR 原文 · 公司 IR
→ **本环境出口代理拦截**（与 NBIS 2026-08-12 跑同因）。
→ 解除路径见 `source_register.md`。**本案完整度上限因此被封。**

---

## 砍掉的项（acceptable gap，附理由）

| 砍掉 | 理由 |
|---|---|
| 10 年 look-back | **公司公开史仅 2 个月**，物理上不存在。地板规则不适用 |
| 13F 机构持仓 | IPO 太新，首个 13F 窗口未到 |
| 历史 backlog 兑现率 | 无历史，**这正是本案最大的不可知** |
| 管理层历史业绩 track record | 归入 Block 2 尽力而为，不作为封顶项 |

---

## 停止条件（灵魂能否开口）

本案要能回答的三个问题：
1. **$17 亿 backlog 是收入还是意向？** → Block 3
2. **这门生意有壁垒，还是有钱买机器就能做？** → Block 4
3. **在锁定期解禁前，现价 $17 是什么位置？** → Block 5

三个都答不上 → 不出裁决。答上但源全为二手 → 裁决封顶在 WATCH（沿用 NBIS 08-12 规则）。
