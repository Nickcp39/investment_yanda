# AI-机器人 4 龙头批次 — SYNTHESIS

**批次 ID**: `ai_robotics_2026-07-10` · **as_of**: 2026-07-10 · **pipeline**: `lean-6module-v1.1` · weights none
**产物**: 本文件 + `dashboard.html`(同目录)
**诚实状态**: 全 4 家 **DECISION_DRAFT**(完整度 ~58-65%),无一 COMPLETE。verdict 一致 **WATCH(新钱 0%)/ HOLD(存量)**。
**线索出处**: 美股投资网视频《未来1年最大美股投资机会——AI机器人产业链》(D1/KOL,仅线索,从不进 facts、不支撑 verdict)。

---

## 1. 排序表(4 家)

排序口径:业务质量 + 真瓶颈耐久性 + 距可买价的接近度(全 WATCH,故排"谁最值得盯"而非"谁能买")。

| # | Ticker | 新钱 verdict | as_of_price | 机器人收入占比 | 机器人需求 REAL / ANTICIPATION | capital_cycle stage + caution | 真瓶颈(机器人段) | WATCH→STARTER 触发 | checker 裁决 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **NVDA** | WATCH / HOLD | $210.96 | **<1%**(~0.3-0.5%,未披露;Automotive 含机器人 ~1.09% FY26;Data Center ~92%) | **ANTICIPATION**(机器人段);真现金=AI 算力,非机器人 | partial / early-pre-inflection · barrier high(CUDA/Jetson)· **caution NONE**(机器人段=未变现期权,非顶) | **PARTIAL**(平台级真护城河但未变现;真瓶颈是 AI 算力,不是机器人) | 回落 ~$155-181(base 5y IRR 回 ≥8% hurdle);或机器人拆成独立收入线且持续 +xxx% Y/Y | **FIX-NEEDED**(仅可追溯性缺口:缺当前 IC panel/source_register 未登新源;**决策本身可信**) |
| **2** | **NOVT** | WATCH / HOLD | $156.65 | **~15-25% est.**(未披露;人形/具身 <1-2% 原型级) | **ANTICIPATION**(人形段;工业基座=真但单位数增长);机器人收入 +7%/有机 +3% | partial / early-anticipation(人形)· mid-recovery(工业)· barrier med-high(在位件)/low(人形)· **caution EARLY-ANTICIPATION** | **PARTIAL**(designed-in/转换成本真护城河,但组件级 ≠ chokepoint;NVIDIA Holoscan 唯一 servo drive) | de-rate 到 ~$100-120(base IRR 回 ≥8%);或机器人从 bookings 转成持续两位数收入 + book-to-bill>1.1 连 2 季 | **CLEAN** |
| **3** | **TER** | WATCH / HOLD | $359.60 | **7.1%**(Q1'26 $91M/$1282.5M)/ ~9.6% FY25(~$308M),且**亏损**(<$365M 盈亏线) | **REAL 但劣质**:机器人=已部署现金(UR cobot+MiR)却亏损、5 年停滞(FY24 $365M→FY25 ~$308M) | partial · 机器人 early/trough-exiting · **semi-test(主导 86.6%)late/possible-PEAK** · barrier low-med(机器人)/high(ATE)· **caution PEAK** | **NO-CONCEPT**(机器人段:低壁垒、商品化、无硬瓶颈、亏损);真瓶颈=半导体测试 ATE 双寡头,但**周期性且不是机器人** | 回落 ~$250-280(非峰值盈利倍数 ~28-32x 且 AI-test 仍在打印) | **CLEAN** |
| **4** | **ON** | WATCH / HOLD | $95.96 | **~0%**(de minimis;仅 design-win/demo,无 dated 机器人收入/订单/出货) | **ANTICIPATION**(纯);真现金在汽车($797M +5%)/工业/AI-DC 电源($250M→$500M'26E),机器人零现金 | no(机器人段)/partial(核心)· 核心 demand trough→early · **valuation late(+115% off low)** · barrier low-med · **caution PEAK-lean(估值)** | **NO-CONCEPT**(机器人段:商品件、4+ 竞争、无转换成本;机器人里的瓶颈节点是算力/执行/软件,不是 onsemi) | 回落 ~$65-72(base 中周期 ~16x 有 MOS,核心复苏未变) | **CLEAN** |

---

## 2. 直接回答 THESIS(PLAN §1)

> 机器人链里有没有一个"**需求已暴增 + 卡死瓶颈 + 已经在赚钱**"的真龙头(像 NVDA 之于 AI 算力),还是全是"人形起量才受益"的期权 → WATCH?

**决定性裁决:没有。这 4 家里不存在一个"机器人版 NVDA"。全部 WATCH。**

把 NVDA 三条件的与门逐家过一遍(证据来自 4 张卡):

| 与门条件 | NVDA(机器人段) | NOVT | TER | ON |
|---|---|---|---|---|
| 需求已暴增(dated 现金) | ✗ <1%,anticipation | ✗ 机器人有机 +3%,人形 <2% pre-rev | △ 有现金但 5 年**停滞** | ✗ ~0%,仅 design-win |
| 卡死瓶颈(可证伪定价权) | ✗ 平台真但未变现 | ✗ 好组件商,非 chokepoint | ✗ 机器人段低壁垒商品化 | ✗ 商品件 4+ 竞争 |
| 已经在赚钱(机器人段) | ✗ ~nil | △ 混在工业里 | ✗ **亏损**(<breakeven) | ✗ 零 |

**没有任何一家三条件同时满足。** 每家都在**至少两条**上失败:
- **NVDA** 三条件确实在 **AI 算力**上全过(exceptional_bottleneck,DC +92%、networking +199%、Q2 guide $91B、FCF≈OE ~$182B、净现金 $72B)——但那是 AI 数据中心算力,**不是机器人**;机器人只是它 <1% 收入的近乎免费嵌入期权。买 NVDA = 买 AI 算力估值 + 白送一张机器人彩票,**不是机器人 alpha**。
- **TER** 确实有一个真硬瓶颈(半导体测试 ATE 只剩 Teradyne+Advantest、58-61% GM、qualification 转换成本)——但它**周期性 + 现价在峰值倍数**(~40-43x '26E / ~102x FY25,M6=−2),而**机器人段本身亏损且停滞,thesis 直接被一手数据证伪**。
- **NOVT / ON** 连"真瓶颈"这条都不满足:NOVT 是优质 designed-in 组件商(非收费站),ON 是披机器人外衣的汽车/工业周期股(机器人现金≈0)。

**一句话:机器人现在没有一个"需求暴增+卡死+赚钱"三合一的可买瓶颈。想要那种资产,标的是 AI 基础设施(算力/网络/内存),不是这批机器人链名字。**

---

## 3. Capital-cycle 横向交读(机器人段)

对 **机器人段** 逐家套 `CAPITAL_CYCLE.md` lens,结论高度一致:

- **需求是"证实-暴增"还是"anticipation"?→ 压倒性 ANTICIPATION。** 唯一有已部署机器人现金的是 **TER**(UR cobot + MiR ~7-10%),但它**亏损、5 年停滞**——即"真现金但不是暴增、也不赚钱"。其余三家机器人段现金 ~0(NVDA <1% 且混在 auto、ON ~0%、NOVT 人形 <2% pre-rev)。人形/具身智能这块**普遍是发布会/design-win/bookings 信号,不是 dated 收入**。
- **供给壁垒普遍 LOW(机器人段)。** cobot/AMR(TER)、功率+传感件(ON)、精密运动件(NOVT)都是**多竞争、商品化、供给能响应**的节点 → 按 lens,即便需求真起来,超额回报也会被资本填平,**不是耐久 bottleneck**。真正 high-barrier 的是各自的**非机器人主业**(NVDA CUDA、TER ATE 双寡头、NOVT designed-in 在位)。
- **天真守卫触发。** 三家现价都在"可见叙事 + 已 re-rate"位置:TER 4x off low、ON +115% off low、NVDA/NOVT 距 ATH 仅 -9~-11%。可见的"机器人/AI 需求">供给是**共识,已被定价**——按 lens 默认是 late-cycle,不是买点。故机器人叙事在四家**都只压不升 verdict**。
- **什么会改变判断(转 REAL-surging)?** 需要看到:(a) 某家把**机器人/具身智能拆成独立收入线**并连续多季 +xxx% Y/Y(概念→变现);(b) 该段**跨过自身盈亏线并持续盈利**(TER 机器人 >$365M breakeven 且转正);(c) bookings→sustained revenue 且 book-to-bill>1.1 连 2 季、pull-forward 被证伪(NOVT);(d) 出现**可证伪的定价权**(转换成本/稀缺 know-how,而非商品件)。在此之前,机器人段 = TROUGH-WATCHLIST / 期权,**不加 size**。

---

## 4. AI-infra vs 机器人框架:是否证实用户的读法

**证实。这批用一手数据把用户的判断钉死了:**

> **机器人现在没有可见-真实-需求的瓶颈;AI 基础设施有。**

- **AI-infra 侧(NVDA 为代表):** 三条件全过——需求 dated 暴增(DC +92%、net +199%、Q2 guide $91B)、真瓶颈(CUDA/full-stack,可证伪转换成本)、已在赚钱(FCF≈OE ~$182B、GM ~75%)。它是 `exceptional_bottleneck`。**唯一挡住的是价格**(base 5y IRR +4.7% < 8% hurdle,-10.8% off ATH),不是业务。
- **机器人侧(TER/ON/NOVT + NVDA 的机器人段):** 无一满足三条件与门。要么无现金(ON/NVDA-机器人段/NOVT 人形)、要么无瓶颈(NOVT/ON)、要么有现金但亏损停滞(TER)。这批的**真实价值 = 用一手证据证实"机器人现在没有可买的真瓶颈"**,并给每家写死了 WATCH→STARTER 的触发信号(见排序表末列)。
- **对用户的操作含义:** 想买"AI 版收费站"的资产,方向是**算力/网络/内存等 AI 基础设施**(且等价格给 MOS);机器人链这批名字现在买到的是**主业(车/工业/半导体测试/AI 算力)+ 一张定价 ~$0 的机器人期权**——**wrong vehicle for pure robotics**,且四家现价都无 MOS。

---

## 5. 诚实状态与限制

- **全 4 家 = DECISION_DRAFT**(完整度 ~58-65%),**非 COMPLETE**;verdict 一致 **WATCH(0%)/ HOLD**,均被完整度正确封顶(未越级)。
- **freshness 机械门全 PASS**(价格 ≥2 源交叉,分毫对得上);T6 个别 WARN(guidance 源 >45d)属预期(Q1'26 是最新披露,Q2 财报在 as_of 之后),非 blocking。
- **Checker:** TER/ON/NOVT = **CLEAN**;NVDA = **FIX-NEEDED**——**仅**可追溯性缺口(dossier 缺当前 $210.96 的 IC panel,唯一现存 06-19 panel 停在被 INC-001 错价推翻的 STARTER 结论未标 superseded;source_register 未登新源)。**NVDA 决策本身可信、数字全对得上、robotics thesis 是全批最扎实一段**;补齐即 CLEAN。
- **未闭合 OPEN(共性):** 各家机器人收入均**无独立披露**(NVDA 混 Automotive、NOVT 无 discrete line、ON design-win 为 B2-relay、TER robotics $ 为推导)→ 机器人占比%是 estimate/derived,不是 filed fact;operator/proxy 多为 provisional。以上均为**haircut,非 veto**,已在各卡诚实标注。
