# INTU Business Model (M2 主题/机制) — as_of 2026-08-06

来源：`facts.md` E10–E76 | pipeline: lean-6module-v1.1

---

## 0. 一句话

Intuit 卖的不是软件，是**"把钱搬过合规关口"的通行权**——报税要过 IRS 的报送关口，
发薪要过 50 个州的税务关口，收款要过支付牌照关口。
软件界面是可以被 AI 复制的；**关口不行**。
本轮回撤的全部争议，可以化约成一个问题：**这四条腿里，哪几条的价值真的在关口上，哪几条只在界面上？**

---

## 1. 结构（FY2026 起只剩两个报告分部）

2025-08-01 起，Consumer + Credit Karma + ProTax 合并为**单一 Consumer 分部**。
但**经济上是四条完全不同的腿**，必须分开看。

| 腿 | FY2025 收入 | FY2025 分部营业利润 | 分部利润率 | 生意的本质 |
|---|---:|---:|---:|---|
| **Global Business Solutions**（QuickBooks + 支付 + 薪资 + Mailchimp） | $11,077M | $8,467M | **76%** | 订阅年金 + 交易抽成 |
| **Consumer（TurboTax）** | $4,870M | $3,786M | **78%** | 季节性、一年一次的高毛利交易 |
| **Credit Karma** | $2,263M | $835M | **37%** | 信贷周期的流量撮合 |
| **ProTax** | $621M | $533M | **86%** | 专业报税师的工具订阅 |

> 注意利润池的形状：**GBS 一条腿就贡献 FY2025 分部营业利润的约 60%**，
> 而它恰恰是本轮**唯一零恶化迹象**的一条。市场把整个公司按最差的一条腿定价了。

---

## 2. 四条腿的机制，逐条

### 2.1 Global Business Solutions —— 真正的复利机器

**收入怎么来的**：约 1,000 万家企业订阅 QuickBooks，然后 Intuit 在同一个账套上叠卖
支付（抽成）、薪资（按人头月费）、放贷（QuickBooks Capital 的利息）、营销（Mailchimp）。

```
QuickBooks 账套（订阅费）
   └─ 银行/卡直连 → 自动对账 → 现金流可见
        ├─ 支付：客户在 QuickBooks 里开发票 → 客户收款走 Intuit → 抽成
        ├─ 薪资：Intuit 作为 registered agent 代缴 50 州薪资税
        ├─ 放贷：用账套里的真实现金流做风控 → QuickBooks Capital
        └─ 营销：Mailchimp（唯一没有真正嵌进这条链的模块）
```

**为什么这是年金**：账套装的是**历史**——历史交易、历史对账、历史薪资、历史报税归档。
换软件不是换工具，是把审计线索搬家。这也是为什么 Intuit 敢每年提价：

| | FY2024 | FY2025 |
|---|---:|---:|
| Online Ecosystem ARPC 增速 | +11% | **+14%** |
| Online Ecosystem 付费客户增速 | +6% | **+5%** |

**FY2026 前三季的实际读数**：QBO Accounting **+24%**、Online Services **+17%**、
Online Ecosystem **+20%**、GBS **+17%**；中端市场（QBO Advanced + Intuit Enterprise Suite）**+38%**。
Q3 Online Services 的增量 100% 来自 money（+$107M）与 payroll（+$55M）——
**即 GBS 的增长引擎已经从"卖账本"转成了"抽交易流水"。**

**唯一的裂缝**：付费客户增速 6% → 5%，增长越来越靠提价；国际只有 +9~10%。

### 2.2 TurboTax —— 一台"以单量换单价"的收割机

**机制**：把免费/低价用户让出去，把留下的人往 TurboTax Live（人+AI 助报）上推。

| | FY2022 | FY2025 | FY2026 指引 |
|---|---:|---:|---:|
| 联邦单量（百万） | 42.7 | **39.2** | **约 −2%** |
| Consumer 收入 | — | +24.5%（vs FY22） | 约 +7%（TurboTax） |
| ARPU | — | — | **+11%** |
| TurboTax Live 收入 | — | $2.0B (+47%) | **$2.8B (+36%)，占 53%** |
| pay-nothing 客户 | — | 8M | **7M** |
| e-file 份额 | — | — | **−1pt** |

**这台机器目前还在赚钱**（价 +11% > 量 −2%）。
**但它的护城河已经搬了家**：从"垄断 DIY 软件的分发"搬到"专家网络 + 品牌"。
分发是结构性的（谁排在 Google 第一、谁在超级碗打广告、谁有 IRS 报送资质）；
专家网络是运营性的（招得到、留得住、便宜到能打价格战的报税专家）。
**后者更薄，而且和 AI 正面相撞**——AI 最直接的攻击面就是"人类专家的时薪"。

管理层自己的定性（Q3 FY2026 电话会）：
> *"We faced pressure among the most price-sensitive DIY filers earning less than $50,000 annually. **We lost on price.**"*
> *"**None of this has anything to do with AI.** This is all about being price-right for customers."*

### 2.3 Credit Karma —— 不是软件，是信贷周期的流量套利

用免费信用分把 1.4 亿会员圈进来，然后把"你大概率能批下来"的信用卡/个人贷/车险
推给对应的发卡行与贷款商，按成交（cost-per-action）收钱。

**它的收入等于：会员意愿 × 放贷方的胃口。** 后者是纯周期变量。
FY2023 已经演示过一次：收入 **−9%**，分部营业利润 **−19%**。

FY2026：+27% → +23% → **+15%**（逐季减速），增长几乎全来自个人贷与车险。
FY2026 全年指引从 10–13% 一路上调到 **~19%**——**是它把 Consumer 分部整体托住的**，
不是 TurboTax。

**交叉销售是真的**（Q3 FY2026 电话会，B1）：TurboTax + Credit Karma 双用户的 ARPU
比纯 TurboTax 用户高约 **30%**；从 Credit Karma 入口开始报税的人 **+54%**。
→ Credit Karma 对 Intuit 的战略价值可能高于它自身的利润贡献（它是 TurboTax 的获客渠道）。

### 2.4 Mailchimp —— 没有嵌进链条的那一块，正在被 AI 拆掉

2021 年以约 **$12B** 收购。理论上的协同是"小企业在 QuickBooks 里管钱、在 Mailchimp 里获客"。
实际上它从来没有像支付/薪资那样嵌进账套的数据链——
它的资产是**联系人名单**，而联系人名单是可以一键导出的。

一手证据链（全部来自 SEC 文件）：
1. FY2025 10-K：Online Services 增量 $669M 里 **Mailchimp 只贡献 +$20M**，且归因仅为"higher effective prices"（没有客户增长）。
2. Q2 FY2026 新闻稿（A1）：*"The company expects Mailchimp to return to double-digit growth **some time beyond fiscal 2026**."*（原目标是 exiting FY2026）
3. Q3 FY2026 10-Q 的 MD&A 增量桥：Online Services +$160M = money +$107M + payroll +$55M = **+$162M** → **Mailchimp 隐含 ≈ −$2M**；9M 隐含 **≈ −$15M**。
4. 公司自述的 ex-Mailchimp 差额：GBS 报告 +15% / ex-MC **+17%**；Online Ecosystem +19% / ex-MC **+22%**。
5. CFO：*"we are **rightsizing our investment** in Mailchimp"*（B1）。

**至今未计提任何减值。**

---

## 3. 季节性（读财报的必备背景）

Intuit 的现金流与利润**极度集中在 FQ3（2–4 月）**：

| | Q1 FY26 | Q2 FY26 | **Q3 FY26** | Q4 FY26E |
|---|---:|---:|---:|---:|
| 收入 | $3,885M | $4,651M | **$8,558M** | $4,247–4,280M |
| GAAP 营业利润 | $534M | $855M | **$4,020M** | $296–316M |

**Q3 一个季度贡献全年 GAAP 营业利润的约 70%。**
推论：
- 任何一年的投资结论，**几乎全押在 2–4 月那一个税季上**；税季一年只有一次，错了要等一年。
- 这也解释了 2026-05-21 的 −20%：那天是当年唯一一次能验证税季结果的时刻。
- 资产负债表也随之摆动：Q2（1/31）现金只有约 **$3.0B**，且为支持提前退税业务临时开了 **$5.8B** 循环额度；Q3（4/30）现金+投资回到 **$6.78B**。**用 Q3 的净现金去描述常态是错的。**

---

## 4. 机制层面的裁决

| 判断 | 依据 |
|---|---|
| **GBS 是一台真年金机器，AI 目前是它的武器不是敌人** | 管道（银行数据/薪资代缴/支付牌照/会计师渠道）不可被模型复制；IES/中端 +38% 说明 AI 在帮它往上打 |
| **TurboTax 的机制还在赚钱，但护城河的位置变了** | 价 +11% > 量 −2%；但分发让位给专家网络，后者薄且与 AI 正撞 |
| **Credit Karma 要按周期股定价，不按护城河定价** | FY2023 −9%/−19% 的先例 + 当前逐季减速 |
| **Mailchimp 是已实现的价值毁灭** | 收入下滑 + 目标推迟 + "rightsizing" + $12B 未减值 |
| **公司层面：一条腿的裂缝被定价成四条腿的死亡** | 利润池 60% 在零恶化的那条腿上；股价 −60% |
