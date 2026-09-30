# INTU Decision Card — as_of 2026-08-27 settled（run_date 2026-08-28）

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-08-28
**status**: DECISION_DRAFT · **completeness**: **~68%**（O1 已解锁，自 62% 上调）
**context_label**: fy2026_print_answered_units_ok_guidance_decel_price_above_starter_anchor

> **一句话**：8/25 的 FY2026 全年财报把 8/7 卡片最大的 blocking 项（O1）**解锁了**——
> TurboTax 单量 −2%（未触发 K-A 的 ≤−4% 降级线）、全年收入/EPS 落在指引上沿、
> FCF $8.6B、回购 $5.5B；但 **FY2027 指引减速**（收入 +9–10%，TurboTax 仅 +2–3%）
> 让市场两日砸掉 −6.5%，而股价自 8/7 以来累计 **+8.1%** 至 $348.00，
> **已经涨出 starter 主锚 $328 之上**—— thesis 变好了，入场点变差了。

---

## 锁定结论

| 字段 | 值 |
|---|---|
| as_of price | **$348.00**（2026-08-27 **结算**收盘；Yahoo + Nasdaq previousClose 双源，delta 0.0%。8/28 盘中 ~$356 **未结算不用**，INC-003 纪律）|
| market cap | **$97.3B**（Nasdaq 口径；~273.5M 股 × $348 ≈ $95.2B，差异为股数口径时滞，标注）|
| business_verdict | **good**（FY26 实际值全面落在或超指引；分部质量分层不变）|
| **new_money_verdict** | **WATCH_AT_PRICE**（thesis 是 STARTER，但现价高于 starter 主锚 $328——**新开仓等回调**）|
| **existing_position_verdict** | **HOLD_TO_ADD**（已开的 2% 持有；≤$328 才加，≤$274 加向 6%）|
| suggested_initial_size | **0%（现价）/ 2%（≤$328）** |
| suggested_max_size | **6%**（O2/O5 解锁后 ≤$274 才谈）|
| **buy_below** | **~$328**（base 10% IRR 锚，不变）|
| verdict ceiling | **STARTER**（completeness ~68% → 上限 STARTER，未越顶）|
| **binding_constraint** | **价格回到约束位**：base 10y IRR **+9.3%** 仍过 8% hurdle，但 cushion 自 2.2pt 收窄至 1.3pt；现价在 starter 锚 $328 与 no-chase $394 **之间**——框架在这一带的动作是"持有、不加、不追" |

---

## O1 解锁：FY2026 实际值 vs 8/7 卡片的钉死点

| 检查项（8/7 卡片写的） | 实际（8/25 8-K，A1） | 判定 |
|---|---|---|
| K-A：单量 ≤ −4% 降级 | **39.0M，−2%**（Online −2%/Desktop −7%） | 🟡→**不触发**，与指引一致 |
| TurboTax 收入指引 ~7% | **+7% to $5.3B**，Live +37% 占 53% | ✅ 符合 |
| 全年收入指引 $21.34–21.37B | **$21.4B（+14%）** | ✅ 上沿 |
| non-GAAP EPS 指引 $23.80–23.85 | **$24.27** | ✅ **超指引** |
| 全年 FCF（估 ~$7.5B） | **~$8.6B**（OCF 8,838 − capex 221） | ✅ 高于估 |
| Credit Karma ~19% | **+20%** | ✅ |
| Mailchimp | FY27 指引 **−1%~0%**；**FY27 起独立分部披露** | 🔴 仍缩；🟢 O3 开始解锁 |

**owner-earnings 起点重估**：现金侧读数 = FCF $8.62B − 递延税 $1.28B − SBC $2.06B
= **$5.28B**（8/7 卡片同一公式算出来是 $4.1B）。利润侧：NI $4.57B + 无形摊销税后
~$0.4–0.5B ≈ $5.0B。**OE0 合理中枢自 $4.8B 上移至 ~$5.0B**（敏感性见下）。

**FY2027 指引的减速是本次唯一的坏信息**：收入 +9–10%（vs FY26 +14%）；
**TurboTax +2–3%（vs +7%）——"以量换价"模式的增长引擎明显降档**；
Mailchimp −1~0% 连续第二年不增长。对冲项：GAAP 营业利润指引 **+26–27%**
（margin 扩张 + 裁员红利 + 回购缩股），GAAP EPS +22–24%。

## 六模块信号

| 模块 | 角色 | 信号 | Δvs8/7 | 一句话 |
|---|---|---|:--:|---|
| M1 证据脊柱 | confidence | **+1** | 信心↑ | FY26 全年 A1 入库，最大 blocking 项 O1 关闭；完整度 62%→~68% |
| M2 主题/机制 | context+conviction | **+1** | = | "以量换价"数学仍成立（量 −2%、Live +37%），但 FY27 指引显示换挡 |
| M3 利润池/耐久 | conviction | **+1** | = | GBS +16%/OE ex-MC +23% 零裂缝；Mailchimp 独立分部披露将终结黑箱 |
| M4 财务现实 | conviction | **+1** | 边际↑ | FCF $8.6B、回购 $5.5B（+96%）、授权余 $7.9B、股息 +15%；注意 OCF 里又有 $1.28B 递延税顺风（第二年）|
| M5 反演/陷阱 | risk | **−1** | = | TurboTax FY27 +2–3% 是"护城河变薄"的量化延续；Mailchimp K-D 仍 🟠 |
| M6 定价/仓位 | price+output | **+1 → 0** | **↓** | **本轮唯一动的模块**：价格 +8.1% 把 base IRR cushion 从 2.2pt 压到 1.3pt，现价涨出 starter 区间 |

## 三情景（10y IRR @ $348.00，hurdle 8%；模型复现验证：8/7 卡片输出逐位一致）

| 情景 | @$321.91 (8/7) | **@$348.00 (8/28)** | 内容 |
|---|---:|---:|---|
| Bear | −5.9% | **−6.7%** | 单量流失加速 + CK 周期下行 + MC 减值 |
| Base | +10.2% | **+9.3%** | OE CAGR 8%、退出 16x |
| Bull | +19.8% | **+18.8%** | AI 定价收上钱 + IES 第二曲线 |
| sens: OE0=$5.0B base | — | **+9.5%** | FY26 实际支持的 OE0 上移 |

## 价格带（模型不变量，不变）

- **≤ ~$274**（base 12%）→ ADD 向 6% · **≤ ~$328**（base 10%，**主锚**）→ STARTER 2%
- **现价 $348.00**（base +9.3%）→ **持有不加**；**≥ ~$394**（base 8%）→ no-chase
- **~$175** = bear 情景 10 年总价值（永久损失防线）；周期低点 $255.07（6/25）已被市场测试过

## Kill Criteria 更新

| id | 状态 | 变化 |
|---|---|---|
| K-A 单量 | 🟡 | **FY26 −2% 落地，未触发**；FY27 指引 +2–3% 收入隐含单量继续微降 → 盯 FY27 报税季 |
| K-B 定价权 | 🟢 | ARPU 模式延续（收入 +7% vs 量 −2%） |
| K-C QuickBooks 年金 | 🟢 | OE +19%、ex-MC +23%、QBO +23% |
| K-D Mailchimp 减值 | 🟠 | FY27 指引 −1~0% 仍缩；独立分部披露后减值判定将无可回避 |
| K-E Credit Karma 周期 | 🟢 | +20%（指引 +11–13%，减速在指引内） |
| K-F AI 竞品实证 | 🟢 | 仍无任何纯 AI 报税份额证据 |
| K-G 估值 | 🟡 | $348 在 $328 锚之上、$394 之下 → 持有不加 |
| K-H 资本配置 | 🟢 | $5.5B 回购 +96%、授权 $7.9B、股息 +15%——低倍数时买自己，教科书式 |

## runner_dissent

**这轮财报同时给了多空双方弹药，而市场选择了先砸（两日 −6.5%）再拉回。**
多头：每一条 8/7 卡片写的"等待验证"都往好的方向落地——单量没崩、EPS 超指引、
FCF $8.6B、回购接近翻倍。空头：**FY27 指引就是 runner_dissent 里担心的那个剧本的开头**
——TurboTax +2–3% 意味着"以量换价"的提价空间正在耗尽，收入端换挡到个位数后，
+26% 的利润指引全靠 margin 和回购撑，这不是增长故事是收割故事。
框架的裁决不变：**生意 good、thesis STARTER 级，但价格已经不在 starter 位置**。
8/7 在 $321.91 开 2% 的人现在浮盈 +8%，该做的动作是**拿着、别加、别追**；
没上车的人等 $328 以下。三个解锁点还剩两个：FY2026 10-K 的 ARPC/客户数（~9 月初）、
Investor Day 的 AI 变现量化（**2026-09-17**）。

## OPEN（封顶 ~68%）

- **O2**（blocking）FY2026 Online Ecosystem ARPC 与付费客户数 → 10-K，~9 月初
- **O5**（blocking）AI 变现量化 → Investor Day **2026-09-17**（CEO 口径 "Big Bets +34%、
  占收入 30%" 是第一个可追的代理指标，但仍非 AI 归因收入）
- **O4**（monitoring→升温）Mailchimp 减值判定：FY27 独立分部披露后无处可藏
- **O13**（新）FY27 指引减速的构成：TurboTax +2–3% 里量/价拆分、GBS +13–14% 的
  可持续性 → FY27 Q1 财报（~11 月）
- O9/O10/O12（监管与竞品一手核实）照旧挂起，未恶化
