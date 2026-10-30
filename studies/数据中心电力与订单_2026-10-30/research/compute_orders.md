# 算力订单侧：谁签了、签了多少、还在长吗（2026-10-30）

范围：neocloud（NBIS、CRWV、IREN、APLD）、Oracle、三家云厂商的 backlog，以及四大云厂商的 capex 指引。
截至 2026-10-30 已公布的最新季度：MSFT、GOOGL 到 9/30；ORCL 到 8/31（FQ1 FY27）；AMZN 8-K 到 9/30，但 Q3 10-Q 未递交，所以 AWS backlog 只到 6/30；CRWV、NBIS、IREN 只到 6/30；APLD 到 8/31。
标签：**P** = 一手（SEC 8-K/10-Q/10-K/6-K/20-F 及附件、公司 IR）；**S** = 二手（电话会转录、媒体、评级机构）。**推算** = 本文算术，算式写在旁边。
数据文件：`../data/compute_orders.csv`（长表，216 行）。不是投资建议。

---

## §0 结论

1. **签约 backlog 的水位还在升，但最新一季的净新增明显放缓，不是在加速。** MSFT、GOOGL、ORCL 三家口径可比，季度净新增合计从 Q1'26 约 $256B、Q2'26 约 $188B 降到 Q3'26 约 $73B（推算，见 §1）。其中 MSFT 商业 RPO 环比 −$1B（P），ORCL +$26B，是近五个财季最少（P），GOOGL +$48B 与上季持平（P）。AMZN 的 Q3 积压还没披露，它前两季是 +$120B、+$132B。
2. **neocloud 的 Q2 也同步放缓：** CRWV backlog +$4.8B（Q1 +$32.6B），NBIS RPO +$3.9B（Q1 +$12.3B）（P）。反方证据也有：CRWV 称 7 月初另签了 >$25B；各家都在涨价，CRWV 7 月全 SKU 涨约 70%，NBIS H100 挂牌价 +52%，"需求大于供给"仍是一手原话。所以更像是"巨额单之间的空档"，还不是需求塌陷。这要等 11 月中 CRWV、NBIS 的 Q3 来验证。
3. **裂缝一，集中度：** OpenAI 同时是多家的大客户：MSFT（约占商业 RPO 的 45%，S）、ORCL（约 $300B，S）、AMZN（$138B 承诺，P）、CRWV（最高 $22.4B，P）。NBIS 的 RPO 约 86% 来自 MSFT 和 Meta（推算上限）。CRWV 前三客户占收入 72%（P）。
4. **裂缝二，卖方融资和循环需求：** AMZN 2026 年向 OpenAI 投了 $50B，对 Anthropic 的融资额度随 AWS 交付算力逐步开放（P）。GOOGL 为第三方数据中心兜底 $48B，关联方 Crux AI 占它 backlog $16.8B（P）。ORCL 在 Investor Day 上把 vendor financing 写进融资来源，Q1 客户预付 $11.4B，付了当季 40% 的 capex（P）。NVIDIA 兜底 CRWV，Meta 用最高 $15B 兜底 NBIS（P）。
5. **裂缝三，交付延迟，但没有取消：** 2026 年各家 8-K 里没有找到客户取消。但 MSFT CFO 10-28 说"部分第三方 GPU-as-a-Service 合同推迟到下半财年"，并因此把日历 2026 年 capex 从约 $175B 下调到约 $170B（S，转录稿）。CRWV 在 1 月为"对齐交付时间"修订了贷款契约（P）。IREN 微软合同的 4 期里有 3 期挤在 2026 年 Q4 交付（P）。
6. **backlog 越来越远期：** MSFT 12 个月内确认的比例从 40% 降到 30%（P），ORCL 只有 13%（P）。backlog 的增长不等于近期收入的增长。

---

## §1 总表：各家 backlog 的季度净新增（$B，推算 = 本季 − 上季，原值见各节）

| 日历季 | MSFT 商业 RPO | GOOGL 收入 backlog | AMZN AWS（>1 年合同） | ORCL RPO（财季） | **三家合计（MSFT+GOOGL+ORCL）** | CRWV backlog | NBIS RPO |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q3'25（7–9 月） | +24 | +49.5 | +5 | +317.5（6–8 月；主因 OpenAI 大单，S） | 391 | +25.5 | 未披露 |
| Q4'25（10–12 月） | +233（主因 OpenAI 追加 $250B Azure 承诺，S） | +85.1 | +44 | +68.0（9–11 月） | 386 | +11.2 | 期末 21.3 |
| Q1'26（1–3 月） | +2 | +224.8（含口径变化约 7.3） | +120 | +29.3（12–2 月） | **256** | +32.6 | +12.3 |
| Q2'26（4–6 月） | +51 | +51.9 | +132 | +85.4（3–5 月） | **188** | +4.8 | +3.9 |
| Q3'26（7–9 月） | **−1** | **+48.2** | **未披露** | **+26.0（6–8 月）** | **73** | Q3 未出（公司称 7 月初另签 >25） | Q3 未出 |

- ORCL 的财季比日历季早一个月，所以合计只是近似可比。
- 同比增速也在降：MSFT +110% → +99% → +84% → +73%；ORCL FQ1 FY27 同比 +46%（664/455.3）。GOOGL 同比 +260%（567.7/157.7），仍在高位。
- **最新水位**（各家最新已披露值相加，推算）：MSFT 677 + GOOGL 567.7 + AMZN 496（6/30）+ ORCL 664 + CRWV 104.2 + NBIS 37.5 + IREN 16.6 + APLD 36 ≈ **$2.6T**。这个数有重复：APLD 的约 $11B 是 CRWV 的租金成本；NBIS、IREN 来自 MSFT 的合同，是 MSFT 在为自己的客户（主要是 OpenAI）买算力。所以不能当作独立的终端需求。
- **OpenAI 的跨家承诺量级**：MSFT 约 281（S，45% × 625）+ ORCL 约 300（S）+ AMZN 138（P）+ CRWV 22.4（P）≈ $740B（推算）。对照：二手报道称 OpenAI 2 月把 2030 年前的算力支出计划从 $1.4T 降到 $600B（CNBC，经 repo 10-23 研究转述，S）。两者期限口径不同，只能作量级对照。

---

## §2 Nebius（NBIS）

**Q3'26 未出**：SEC submissions 查询（2026-10-30）显示 2026-10-22（Citi 过桥贷款）之后没有新的 6-K，只有 Form 4 和 Form 144。财报日按惯例约 11-10/11，尚未公告。

| 季末 | RPO（$B） | ARR（$B） | 递延收入（$B，含预付） | 合同电力（contracted） | active power | capex（$B） | 来源 |
|---|---:|---:|---:|---|---|---:|---|
| 2025-03-31 | 未披露 | 0.249 | — | — | — | — | N1 P |
| 2025-06-30 | 未披露 | 0.430 | 0.019 | 年底目标 >1 GW | 未披露 | — | N1 P |
| 2025-09-30 | 未披露 | 0.551（约） | 0.016 | 年底目标约 2.5 GW | 年底目标 100 MW | — | N2、N13 P |
| 2025-12-31 | **21.333** | 1.25 | 1.578 | >2 GW（2-12 信）；年底目标 >3 GW | **约 170 MW** | — | N3、N8 P |
| 2026-03-31 | **33.585**（29% 在 24 个月内） | 1.92 | 4.778 | >3.5 GW（5-13 信）；目标 >4 GW | **未披露** | 2.47 | N4、N5 P |
| 2026-06-30 | **37.491**（36% 在 24 个月内） | **3.0** | **5.975** | 当期未披露；年底目标 5 GW | **未披露** | 5.66 | N6、N7 P |
| 2026-09-30 | 未出 | 未出 | 未出 | 未出 | 未出 | 未出 | N11 |

- **口径**：ARR 在 Q1'26 之前是"核心 AI 基础设施业务末月收入 × 12"，之后改为"Nebius AI cloud revenue 末月 × 12"。三种电力的定义：contracted = 已签土地和电力；connected = 接入已建成机房；active = IT 设备在用、可产生收入（Q1'26 信）。
- **2026 指引**（P，Q2 信重申）：收入 $3.0–3.4B；年底 ARR $7–9B；年底 connected 800 MW–1 GW；2026 年客户预付超过 $9B；2027 年起每年部署 >1 GW。全年 capex $20–25B 只出现在电话会（S）。
- **另一口径**：Q2 信写 "$40 billion in customer commitments"，10-22 的 6-K 写 "more than $40 billion of long-term contracts"（P），都比 6/30 的 RPO $37.5B 高。差额的构成没有说明。

**主要合同**

| 客户 | 签约日 | 金额 | 关键条款 | 来源 |
|---|---|---|---|---|
| Microsoft | 2025-09 | $17.4B，最高 $19.4B，5 年 | Vineland NJ；预付约 $6.96B；交付延迟可按批次终止；截至 08-12 已全部交付 | N8、N6 P |
| Meta #1 | 2025-11-01 | 约 $2.88B（约 $3B），5 年 | 不论使用量都付费；规模受限于当时可用产能 | N2、N8 P |
| Meta #2 | 2026-03-13/16 | 最高约 $27B | $12B 专用产能（Vera Rubin，2027 年初起）+ 最高 $15B 未售产能，可按约定价卖给 Meta，也可按市价卖给其他客户 | N9、N4 P |
| Q2 四笔 | 2026 Q2 | 平均 TCV >$1B | Reflection、Cohere 等；$20–25M/MW；70% 的交易带预付，覆盖相关 capex 50–60%；大部分针对 2026 年底才上线的产能，主要贡献 2027 年收入 | N6 P |

- **集中度**：MSFT 与 Meta 的合同额约占 6/30 RPO 的 86%（推算上限：(17.4 + 2.88 + 12) / 37.49；未扣已确认收入，公司未分客户披露）。Q2 收入前三客户 C/D/E 分别占 24%/21%/14%（P，N7）。
- **延迟、取消、重新定价**：一手文件没有。方向反而是**涨价**：Q2 新签 ACV 超过 $20M/MW，Q3 首笔短约在 $40–50M/MW 区间（N6 P）。
- **融资**：2026-10-17 签 Citi $3.5B 364 天有担保过桥贷款，提款状态未披露（N10 P）。

---

## §3 CoreWeave（CRWV）

| 季末 | revenue backlog（$B） | 其中 RPO（$B） | RPO 24 个月内确认 | active power | contracted power | 最大客户占收入 | 递延收入（$B） | 来源 |
|---|---:|---:|---:|---:|---:|---|---:|---|
| 2025-03-31 | 25.9 | 14.7 | — | 约 420 MW | 约 1.6 GW | — | — | C1 P |
| 2025-06-30 | 30.1 | 30.1 | — | 约 470 MW | 约 2.2 GW | — | — | C2 P |
| 2025-09-30 | 55.6 | 50.0 | 42% | 约 590 MW | 约 2.9 GW | Microsoft 67% | 5.3 | C3、C7 P |
| 2025-12-31 | 66.8 | 60.7 | 43% | >850 MW | 约 3.1 GW | Microsoft 67%（全年） | 8.2 | C4、C8 P |
| 2026-03-31 | 99.4 | 98.8 | 36% | >1 GW | >3.5 GW | 客户 A 45%，B 20% | 7.5 | C5、C9 P |
| 2026-06-30 | **104.2**（新闻稿写约 $104B） | 103.7 | 41% | **约 1.5 GW** | 约 3.7 GW；8-11 约 4.2 GW | **A 36%，B 26%，C 10%** | 9.7 | C6、C10、C13 P |
| 2026-09-30 | 未出；公司称 7 月初另签 >$25B，未计入上行 | — | — | — | — | — | — | C6 P |

- **最大合同**（P）：OpenAI 最高约 $22.4B（$11.9B + $4B + $6.5B，2025 年分三次）；Meta $14.2B（2025-09）加 $21B（2026-03-31，至 2032-12）；Anthropic 多年协议，金额未披露（Q1'26）；NVIDIA "$6.3B strategic collaboration"（2025-09，二手称为未售产能兜底，至 2032-04）。Meta 加 OpenAI 合计约占 backlog 的 55%（推算上限，都是 up to 金额）。
- **集中度在分散，但仍高**：Microsoft 从 67% 降到 36%（2026 年起不再点名），前三客户合计 72%（Q2'26，P）。
- **延迟和异常**（P）：
  - **2026-01-02 8-K**：修订 DDTL 3.0 贷款，目的是对齐 Q3'25 电话会所说的交付时间。DSCR 首次测试推到 2027-10-31，最低流动性要求下调，允许无限次股权补救。这是一手层面最清楚的延迟证据。
  - **Q1'26 10-Q**：$1.3B 递延收入被重分类为"customer liabilities"，该科目从 $0.137B 升到 $1.469B，原因未说明。到 6/30，其他流动负债合计只剩 $0.070B。性质待核，可能是可退还预付或抵扣。
  - 10-Q 的 RPO 定义写明，变动对价包括"amounts that may not be recognized as revenue due to delivery delays"。
  - 2026 年 8-K 里**没有找到客户取消或降额**。最近一份 8-K 是 09-22。
- **定价**（P，C13）：2026 年 7 月全 SKU 涨价约 70%；Q3 新签 3–6 个月短约约 $40M/MW；Q2 新签合同的预期贡献利润率比前几季高约 25%。
- **融资**（P，C13）：09-17 启动 3,500 万股 ATM（含 collared forward），同时发 2033 可转债。Q2 capex $9.4B。

---

## §4 IREN

| 日期 | 指标 | 数值 | 来源 |
|---|---|---|---|
| 2025-09-30 / 12-31 / 2026-03-31 / 06-30 | RPO（ASC 606，只含已交付并验收的部分） | $0.195B / $0.289B / $0.710B / **$5.1B** | I10–I12、I9 P |
| 2026-06-30 | RPO + 租赁合同总值（ASC 842，含微软） | **约 $16.6B** | I9 P |
| 2025-11-02 | Microsoft 合同 | **$9.7B / 5 年**，20% 预付，Horizon 1–4 共约 200 MW IT，2026 年分批交付；**交付延迟时微软可终止**；预期 ARR 约 $1.9B | I2、I1 P |
| 2026-05-07 | NVIDIA AI cloud 合同 | $3.4B / 5 年，60 MW，2027 年初爬坡 | I5 P |
| 年底 ARR 目标的变化 | 2025-11 $3.4B → 2026-02 $3.4B → 2026-03 >$3.7B → 2026-05 $3.7B（含 NVIDIA 后 2027 初 $4.4B） | | I1、I3、I4、I5、I6 P |
| 2026-05-07 / 08-27 | 已签 ARR | $3.1B → **$4.0B（2026 年产能）** | I5、I8 P |
| 2026-08-26 | 运营中 ARR | **$1.0B** | I8 P |
| Q3 FY26 / Q4 FY26 | AI cloud 季度收入 | $33.6M / $70.5M | I8 P |
| 产能目标 | 2026 年 480 MW（gross，约 0.3 GW IT）；2027 年 1.2 GW（gross，约 0.8 GW IT） | | I7、I8 P |
| 2026-06-30 | 递延收入 | 资产负债表 $1.84B；附注只写 ASC 606 部分 $219.1M，两处口径不同 | I9 P |

- **交付状态**：Horizon 1 在 2026-08 交付微软并通过验收；Horizon 2–4 目标 2026 年 Q4（I7 P）。仍在合同写的"2026 年内"窗口里，但 4 期中 3 期挤在最后一个季度。结合 MSFT CFO 说"第三方 GPU 合同推迟到 H2"（S），这是 Q4 要看的交付风险。
- **10-K**（P）：如果微软有效终止某一批次，又找不到替代客户，母公司要为该批次的 GPU 融资提供担保。
- **定价**（P，I8）：3 年合同 >$20M/MW(IT)，在谈约 $25M/MW；预付占 GPU capex 45–55%。
- **已签和运营之间的落差**：$4B 已签 ARR 对 $1B 运营中 ARR。这说明 backlog 要靠交付兑现，NBIS 的 $7–9B 年底 ARR 目标也面临同样的问题。

---

## §5 Applied Digital（APLD，出租机房，不买 GPU）

| 财季末 | 已租 critical IT | 基础期合同收入（$B） | 新增租约 | 来源 |
|---|---:|---:|---|---|
| 2025-05-31（FQ4 FY25） | 250 MW | 约 7 | CoreWeave 首两份约 15 年租约（PF1） | A1 P |
| 2025-08-31（FQ1 FY26） | 400 MW | 约 11 | CoreWeave 再租 150 MW，PF1 租满 | A1 P |
| 2025-11-30（FQ2） | 600 MW | 约 16 | 投资级 hyperscaler 200 MW（PF2，约 $5B） | A2 P |
| 2026-02-28（FQ3） | 600 MW | 约 16 | 季报未见新租约（推断未变）；CoreWeave 租约改由 CoreWeave SPV 承租，母公司提供 springing 担保，另开 $50M 信用证 | A3 P |
| 2026-05-31（FQ4） | 约 1.2 GW（推算） | 约 31（推算） | 一家 tier-one 投资级 hyperscaler：DF1 300 MW（$7.5B）+ PF3 300 MW（$7.5B），均 15 年 take-or-pay | A4 P |
| 2026-08-31（FQ1 FY27） | **约 1.41 GW** | **约 36**（含续约约 86） | 同一客户 DF2 210 MW（$5.2B，06-08 签） | A5 P |

- **租户**：CoreWeave 400 MW（约 $11B）；投资级 hyperscaler 200 MW（约 $5B）；tier-one 投资级 hyperscaler 810 MW（约 $20.2B，连续三次签约）。CoreWeave 是唯一非投资级租户，它的租约在 FQ3 做了信用增强。
- **已交付**：PF1 2025-10 交付 100 MW，2026-07-01 达 175 MW，10-01 达 250 MW。年底北达科他累计目标 300 MW（A5 P）。公司称"Construction remains on schedule"（A3），没有披露延迟。
- 另外在营销约 1.7 GW 未签产能（A4 P）。

---

## §6 Oracle（ORCL，财年截至 5/31）

| 财季末 | RPO（$B） | 环比 | capex（$B） | 客户预付抵 capex（$B） | 来源 |
|---|---:|---:|---:|---:|---|
| 2025-02-28 | 130.2 | — | — | — | O1 P |
| 2025-05-31 | 137.8 | +7.6 | — | — | O1 P |
| 2025-08-31（FQ1 FY26） | 455.3 | +317.5 | 8.50 | — | O1、O3 P |
| 2025-11-30 | 523.3 | +68.0 | 12.03 | — | O1、O3 P |
| 2026-02-28 | 552.6 | +29.3 | 18.64 | — | O1、O3 P |
| 2026-05-31 | 638.0 | +85.4 | 16.49 | 4.59 | O1、O3 P |
| 2026-08-31（FQ1 FY27） | **664.0** | **+26.0** | **28.50** | **11.36** | O1、O2、O3 P |

- **FQ1 FY27 要点**（P）："booked more than $30 billion of additional AI cloud contracts"，但 RPO 只增 $26B，差额是消耗和确认。RPO 中 **13%** 在 12 个月内确认，37% 在 13–36 个月，34% 在 37–60 个月。"Customer demand ... continues to grow faster than supply."
- 尚未起租的租约 **$288B**（FQ2 FY27 到 FY29 起租，15–19 年）；ATM 用尽，净得 $19.9B；Q1 净现金 capex（公司口径）$17.97B（O2、O3 P）。
- **OpenAI 占比**：公司从未在申报文件里点名。WSJ 报道约 $300B / 5 年，自 FY2028 起（S，O6）；媒体与 S&P 估计约占 RPO 一半（S，O5、O7）。
- **10-28 Investor Day**（P，O4）：FY30 收入 ≥$225B；FY28 下半年 FCF 转正；FY27–FY28 是 capex 峰值，FY29 回落；FY27–30 新增外部融资上限 $20B（股、债各 $10B）。原文明确："**Vendor financing**, customer-provided hardware and customer prepayments are expected to reduce upfront cash requirements"。FY27 capex 没有给数字；S&P 估计 $90–95B（S）。

---

## §7 三家云厂商的 backlog 与单一关联客户

### 7a Microsoft 商业 RPO（财年截至 6/30）

| 季末 | 商业 RPO（$B） | 同比 | 全公司 RPO（$B） | 12 个月内确认 | 来源 |
|---|---:|---:|---:|---|---|
| 2025-06-30 | 368 | — | 375 | 40%（全公司） | M1 P |
| 2025-09-30 | 392 | +51% | 398 | 40%（全公司） | M2 P |
| 2025-12-31 | 625 | +110% | 631 | 25%；加权久期约 2.5 年 | M3 P |
| 2026-03-31 | 627 | +99% | 633 | 商业 25% | M4 P |
| 2026-06-30 | 678 | +84% | 684 | 30%；久期约 2.3 年 | M5 P |
| 2026-09-30 | **677** | **+73%** | 683 | 30% | M6 P（repo 10-28 已收） |

- **OpenAI**：2025-12-31 的商业 RPO 中约 45% 来自 OpenAI，剔除后同比 +28%（CFO 电话会，S，M8）。2026-06-30 剔除 OpenAI 后同比 +25%（电话会，S，repo 09-26 卡转述）。9/30 的拆分在一手文件里没有。一手可见的是收入：OpenAI 本季贡献 $10.0B，占总收入 10.8%（FY26 全年 $24.1B，约 7.3%）；应收 $7.2B（M6 P）。
- 尚未起租的数据中心租约 $364.6B，一季前是 $329.1B（M6 P）。
- **第三方算力延迟**（S，M10，10-28 转录）：CFO 原话 "some third-party capacity deliveries we expected in Q1 were delayed"，以及 "some 3P GPU-as-a-Service contracts that have been delayed to H2"（即 2027 年 1–6 月）。微软的 3P GPU 供应商包括 NBIS、IREN、CRWV、Nscale 等，CFO **没有点名**是哪家。

### 7b Alphabet 收入 backlog

| 季末 | 总 backlog（$B） | 其中 Google Cloud（$B） | 24 个月内确认 | 来源 |
|---|---:|---:|---|---|
| 2025-06-30 | 108.2 | 未拆分（"primarily"） | 约 55% | G1 P |
| 2025-09-30 | 157.7 | 未拆分 | 刚过 55% | G2 P |
| 2025-12-31 | 242.8 | 未拆分 | 刚过 50% | G3 P |
| 2026-03-31 | 467.6 | 462.3 | 刚过 50% | G4 P |
| 2026-06-30 | 519.5 | 513.9 | 刚过 50% | G5 P |
| 2026-09-30 | **567.7** | **560.8** | 刚过 55% | G6 P |

- **口径变化**（P）：2026 Q1 起，backlog 也计入原始期限 ≤1 年的合同，这部分在 3/31 约 $7.3B。Q1 的 +$225B 主要不是口径造成的。
- **关联方**（P，G6）：backlog 含 **$16.8B** 来自 Crux AI（Google 与 Blackstone 的权益法合营，关联方），占 Cloud backlog 3.0%（推算）。Google 另对 Crux 有 $10B 数据中心和能源兜底承诺。数据中心兜底合计 $75.7B，其中 **$48.0B 是给第三方数据中心的**（记为信用衍生品）。
- Anthropic 对 Google Cloud 的 5 年承诺约 $200B：The Information 报道，未证实（S，repo 10-23 研究）。

### 7c Amazon AWS backlog（原始期限 >1 年合同的未确认承诺，"primarily AWS"）

| 季末 | 数值（$B） | 来源 |
|---|---:|---|
| 2025-06-30 | 195 | Z1 P |
| 2025-09-30 | 200 | Z2 P |
| 2025-12-31 | 244 | Z3 P |
| 2026-03-31 | 364 | Z4 P |
| 2026-06-30 | **496**（加权剩余期限 6.4 年） | Z5 P |
| 2026-09-30 | **未披露**：Q3 10-Q 截至 2026-10-30 未递交，8-K 新闻稿不含 | Z7 |

- **被投公司同时是客户**（P，Z5）：OpenAI 在原有 $38B 承诺上，Q1'26 再扩 $100B / 8 年；Anthropic 在 Q2'26 扩 >$100B / 10 年。两家合计约等于 6/30 积压的 48%（推算名义对照，宣布金额 ≠ 已入积压金额）。Amazon 2026 年向 OpenAI 投了 $50B 优先股（Q1 $15.0B + Q2 $13.7B 来自 P；Q3 $21.3B 来自 repo 10-29 refresh，待 10-Q）。对 Anthropic 的 $20B 融资额度随 AWS 交付算力逐步开放（repo，P）。
- AWS Q3 增速 39%；公司预测 2027、2028 年 AWS 增速 >40%（Z6 P）。

---

## §8 云厂商 capex 指引（最新季）

| 公司 | 最新季 capex | 2026 全年指引 | 2027 表述 | 来源 / 级别 |
|---|---|---|---|---|
| Amazon | Q3 净现金 capex $75.9B（Q2 $53.1B） | **约 $220B** 现金 capex | 没有 capex 数字；只说 AWS 2027、2028 年增速 >40% | Z6 **P**（EX-99.1） |
| Alphabet | Q3 $51.4B；前三季 $132.0B | **$195–205B**，不变 | "显著增加"，无数字 | 指引来自电话会 **S**（G8）；10-Q 只写 "significantly increase" vs 2025（P） |
| Meta | Q3 $34.91B（含融资租赁本金） | **$135–145B**（由 $130–145B 收窄） | 没有数字："continue investing aggressively" | F1 **P** |
| Microsoft | Q1 FY27 现金 capex $39.4B（P）；含融资租赁 $45.2B（S） | 日历 2026 **约 $170B**（10-28；7 月为约 $175B，再之前约 $190B）。下调**因第三方算力延迟**，另有租赁年限重分类 | FY27 同比增长；Q2 FY27 >$50B；H2 FY27 加速，主要是 CPU | **S**（M9、M10 转录稿） |
| Oracle | FQ1 FY27 $28.5B（P） | FY27 没有数字；FY27–28 是峰值，FY29 回落（P） | — | O4 P；S&P 估 $90–95B（S） |

- 四家 2026 年合计约 **$730B**（推算：220 + 200 + 140 + 170，GOOGL、META 取中值；混合 P/S），7 月底约 $733B。**全年总盘子基本没变，但 MSFT 的下调来自供给侧交付延迟，不是需求下降**（S）。

---

## §9 裂缝清单（按证据级别）

| 类型 | 事实 | 级别 |
|---|---|---|
| 延迟 | MSFT：部分第三方 GPU-as-a-Service 合同推迟到 H2 FY27；日历 2026 年 capex 因此降到约 $170B | S |
| 延迟 | CRWV：2026-01-02 修订 DDTL 3.0，对齐交付时间，推迟契约测试 | P |
| 延迟（窗口内） | IREN：微软 4 期中 Horizon 2–4 目标 2026 Q4；合同允许微软因延迟终止 | P |
| 异常 | CRWV：Q1'26 $1.3B 递延收入转入"customer liabilities"，原因未披露 | P（性质待核） |
| 取消 | 2026 年 CRWV、NBIS、IREN、APLD 的 8-K/6-K 中**未发现**客户取消或降额 | P（搜索结果为无） |
| 重新定价 | 方向是**上调**：CRWV 7 月全 SKU 约 +70%；NBIS 挂牌价 +52%，长约 $20–25M/MW；IREN >$20M/MW | P |
| 集中度 | OpenAI 在 MSFT（约 45%，S）、ORCL（约 50%，S）、AMZN（$138B，P）、CRWV（$22.4B，P）；NBIS MSFT+Meta 约 86%（推算） | 混合 |
| 卖方融资 | AMZN→OpenAI $50B、Anthropic 额度；GOOGL 第三方兜底 $48B + Crux 关联方 $16.8B；ORCL "vendor financing" 加客户预付 $11.4B；NVIDIA 兜底 CRWV；Meta 兜底 NBIS 最高 $15B；CRWV 在 APLD 的租约由母公司担保 | P |
| 久期 | MSFT 12 个月内确认 40% → 30%；ORCL 13%；CRWV 24 个月内 42% → 36% → 41% | P |
| 融资成本 | NBIS 有担保过桥 $3.5B；CRWV 重启 ATM 并发可转债；ORCL ATM $20B 用尽 | P |

---

## §10 NBIS Q3 要查什么（从同业推出来的检查清单）

财报日约 11-10/11（未公告）。基线都是 6/30 一手数。

1. **RPO 能否越过 $40B。** 6/30 为 $37.49B，Q2 只增 $3.9B。同业最新季：MSFT −$1B，ORCL +$26B（一年最低），CRWV 7 月另签 >$25B。如果 NBIS Q3 RPO 低于 $40B 且没有新的大单，就和 MSFT、ORCL 的放缓同步。同时看 24 个月内确认比例（6/30 为 36%）。
2. **active power 和 connected power 第一次更新。** 年底约 170 MW 之后连续两季没有披露。CRWV Q2 单季就加了约 500 MW。年底 connected 800 MW–1 GW 的目标需要 Q3 有明显爬升。**如果还不披露，这本身就是信号。**
3. **ARR 路径。** 6 月 $3.0B，到年底 $7–9B，H2 要增 $4–6B，平均每季 +$2–3B（推算）。Q3 ARR 低于约 $4.5B，年底下限就吃紧。参考 IREN 已签 $4B 对运营中 $1B：签约到收入有落差。
4. **微软第三方 GPU 延迟影响谁。** MSFT CFO 说部分第三方 GPU 合同推迟到 2027 年上半年（S）。NBIS Q2 信说微软批次已全部交付，所以看点是：NBIS 有没有提到微软收入确认推迟、延迟抵扣或违约金；有没有谈新的微软扩容。
5. **Meta #2（$12B 专用，Vera Rubin，2027 年初）的时间表。** 只要有后移，就对照 CRWV 1 月因交付延迟修订贷款契约的先例，以及 IREN 3 期挤在 Q4 的做法。
6. **递延收入和预付。** 6/30 为 $5.98B。全年预付 >$9B，H1 递延收入已增约 $4.40B，H2 还需约 $4.6B（推算，把预付近似为递延收入增加）。另看有没有像 CRWV 那样把递延收入重分类为可退负债。递延收入附注写明含 "amounts that may be refundable"。
7. **新签合同的 ACV/MW。** 基线：长约 $20–25M/MW，短约 $40–50M/MW。同业：CRWV 短约约 $40M/MW，7 月涨价约 70%；IREN >$20M，在谈 $25M。如果 Q3 新签低于 $20M/MW，涨价叙事就破了。
8. **客户集中。** Q2 前三客户占收入 59%（24/21/14），CRWV 是 72%。看是否出现第三个 hyperscaler 级长约：公司说过会用投资级长约做资产担保融资。
9. **capex 与在建。** H1 $8.13B，全年指引 $20–25B（S），H2 隐含 $11.9–16.9B。同时看尚未投用的 PP&E（6/30 占原值 55%）是否开始转固。
10. **融资。** Citi $3.5B 过桥是否已提款；有没有新的 ABF；ATM 剩余约 1,227 万股是否在用。CRWV 9 月同时重启 ATM 和发可转债，是同业的先例。
11. **合同电力。** 年底目标 5 GW；CRWV 8/11 约 4.2 GW，两者已在同一量级。看当期实际数是否给出。

---

## §11 没有披露的、拿不准的

**未披露**
- NBIS：9/30/25 的 RPO；2026 年两季的 active 和 connected power；6/30 的当期合同电力；分客户 RPO；$40B "commitments" 与 RPO $37.5B 之间差额的构成。
- AMZN：9/30 的 AWS backlog（10-Q 未递交）；OpenAI、Anthropic 在积压中的确切占比。
- MSFT：9/30 剔除 OpenAI 后的 RPO；是哪家第三方 GPU 供应商延迟。
- ORCL：OpenAI 占比（申报文件不点名）；FY27 capex 数字。
- META、AMZN：2027 年 capex 数字。CRWV：Anthropic 合同金额。

**拿不准**
- MSFT "约 45% 来自 OpenAI" 和"第三方 GPU 合同推迟到 H2"都只来自转录稿或媒体（S）。TradingKey 转录把 RPO 写成 "$677 million"，明显是转录错误，所以对其中的措辞细节保留怀疑。
- CRWV 的 $1.3B "customer liabilities" 重分类：性质不明，不宜当作取消证据。
- IREN 10-K 里递延收入有两个数（资产负债表 $1.84B，附注 $219.1M）。推测附注只算 ASC 606 部分，未核实。
- APLD 2026-02-28 和 05-31 的租约总量是推算，前者按"季报未见新租约"推断，后者按两份新租约加总。
- §1 三家合计把 ORCL 的财季当日历季用，存在一个月错位。
- 各家 backlog 口径不同：MSFT 是 RPO；AMZN 是原始期限 >1 年合同的承诺；CRWV 的 backlog 比 RPO 多出其他预计收入；IREN 的 RPO 不含未交付的租赁。横向加总只代表量级。

---

## §12 来源

| id | 文件 | 日期 | URL | P/S |
|---|---|---|---|---|
| N1 | NBIS Q2'25 股东信（6-K Ex 99.2）/ 新闻稿（Ex 99.1） | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1513845/000110465925075028/tm2522866d1_ex99-2.htm ; …/tm2522866d1_ex99-1.htm | P |
| N2 | NBIS Q3'25 股东信 / 新闻稿 | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465925109806/tm2530882d1_ex99-2.htm ; …/tm2530882d1_ex99-1.htm | P |
| N3 | NBIS Q4'25 股东信 / 新闻稿 | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926013946/tm266173d1_ex99-2.htm ; …/tm266173d1_ex99-1.htm | P |
| N4 | NBIS Q1'26 股东信 / 新闻稿 | 2026-05-13 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926059872/tm2614392d1_ex99-2.htm ; …/tm2614392d1_ex99-1.htm | P |
| N5 | NBIS Q1'26 未审计报表（RPO） | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm | P |
| N6 | NBIS Q2'26 股东信 / 新闻稿 | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm ; …/tm2622968d1_ex99-1.htm | P |
| N7 | NBIS Q2'26 未审计报表（RPO、客户集中度） | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926094844/nbis-20260812xex99d2.htm | P |
| N8 | NBIS 20-F FY2025 | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm | P |
| N9 | NBIS–Meta 协议 6-K Ex 99.1 | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926027886/tm268879d1_ex99-1.htm | P |
| N10 | NBIS Citi 过桥贷款 6-K | 2026-10-22 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926117978/tm2628078d1_6k.htm | P |
| N11 | NBIS EDGAR submissions（10-22 后无 6-K） | 2026-10-30 查询 | https://data.sec.gov/submissions/CIK0001513845.json | P |
| N12 | MarketBeat：NBIS Q2 电话会摘要（capex 指引） | 2026-08-12 | https://www.marketbeat.com/instant-alerts/nebius-group-q2-earnings-call-highlights-2026-08-12/ | S |
| N13 | NBIS Q3'25 未审计报表（递延收入） | 2025-11-13 | https://www.sec.gov/Archives/edgar/data/1513845/000110465925110831/tm2531034d1_ex99-2.htm | P |
| C1 | CRWV Q1'25 新闻稿 | 2025-05-14 | https://www.sec.gov/Archives/edgar/data/1769628/000176962825000010/coreweave1q25earningspress.htm | P |
| C2 | CRWV Q2'25 新闻稿 | 2025-08-12 | https://www.sec.gov/Archives/edgar/data/1769628/000176962825000039/coreweave2q25earningspress.htm | P |
| C3 | CRWV Q3'25 新闻稿 | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1769628/000176962825000059/coreweave3q25earningspress.htm | P |
| C4 | CRWV Q4'25 新闻稿 | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm | P |
| C5 | CRWV Q1'26 新闻稿 | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000220/coreweave1q26earningspress.htm | P |
| C6 | CRWV Q2'26 新闻稿 | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm | P |
| C7 | CRWV 10-Q Q3'25 | 2025-11-13 | https://www.sec.gov/Archives/edgar/data/1769628/000176962825000062/crwv-20250930.htm | P |
| C8 | CRWV 10-K FY2025 | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm | P |
| C9 | CRWV 10-Q Q1'26 | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm | P |
| C10 | CRWV 10-Q Q2'26 | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm | P |
| C11 | CRWV 8-K：DDTL 3.0 修订（交付时间） | 2026-01-02 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000003/crwv-20251231.htm | P |
| C12 | CRWV 8-K：Meta $21B 订单 | 2026-04-09 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000154/crwv-20260331.htm | P |
| C13 | CRWV 8-K：可转债路演（backlog $104.2B、4.2 GW、涨价约 70%）+ ATM | 2026-09-17 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000429/crwv2026convertpresentat.htm ; …/crwv-20260917.htm | P |
| C14 | CRWV XBRL RPO 序列 | 2026-10-30 查询 | https://data.sec.gov/api/xbrl/companyconcept/CIK0001769628/us-gaap/RevenueRemainingPerformanceObligation.json | P |
| I1 | IREN Q1 FY26 新闻稿 | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1878848/000187884825000079/q1fy26resultspressreleas.htm | P |
| I2 | IREN 8-K：微软合同 | 2025-11-03 | https://www.sec.gov/Archives/edgar/data/1878848/000114036125040072/ef20058139_8k.htm ; …/ef20058139_ex99-1.htm | P |
| I3 | IREN Q2 FY26 新闻稿 | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000014/a991irenreportsq2fy26res.htm | P |
| I4 | IREN 150k GPU 新闻稿 | 2026-03-04 | https://www.sec.gov/Archives/edgar/data/1878848/000114036126007905/ny20064909x3_ex99-1.htm | P |
| I5 | IREN Q3 FY26 新闻稿（NVIDIA $3.4B） | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000025/irenreportsq3fy26results.htm | P |
| I6 | IREN $4.4B ARR 新闻稿 | 2026-05-26 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000030/irentrgts44bninarrwithbl.htm | P |
| I7 | IREN Horizon 1 交付新闻稿 | 2026-08-13 | https://www.sec.gov/Archives/edgar/data/1878848/000114036126032638/ef20080141_ex99-1.htm | P |
| I8 | IREN FY26 新闻稿 | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm | P |
| I9 | IREN 10-K FY2026 | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm | P |
| I10 | IREN 10-Q Q1 FY26 | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1878848/000187884825000081/iren-20250930.htm | P |
| I11 | IREN 10-Q Q2 FY26 | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000015/iren-20251231.htm | P |
| I12 | IREN 10-Q Q3 FY26 | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm | P |
| A1 | APLD FQ1 FY26 新闻稿 | 2025-10-09 | https://www.sec.gov/Archives/edgar/data/1144879/000114487925000068/apldq126earningsrelease.htm | P |
| A2 | APLD FQ2 FY26 新闻稿 | 2026-01-07 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000002/apldq226earningsrelease.htm | P |
| A3 | APLD FQ3 FY26 新闻稿 | 2026-04-08 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000029/apldq326earningsrelease.htm | P |
| A4 | APLD FQ4 FY26 新闻稿 | 2026-07-27 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000044/apldq426earningsreleaseasf.htm | P |
| A5 | APLD FQ1 FY27 新闻稿 | 2026-10-07 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000057/apldq127earningsrelease.htm | P |
| O1 | ORCL XBRL RPO / capex 序列 | 2026-10-30 查询 | https://data.sec.gov/api/xbrl/companyconcept/CIK0001341439/us-gaap/RevenueRemainingPerformanceObligation.json | P |
| O2 | ORCL 10-Q FQ1 FY27 | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm | P |
| O3 | ORCL FQ1 FY27 新闻稿（含季度 capex 与客户预付表） | 2026-09-10 | https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm | P |
| O4 | ORCL Investor Day 8-K Ex 99.1 | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/1341439/000119312526435853/d75538dex991.htm | P |
| O5 | Cryptobriefing：OpenAI 约占 RPO 一半 | 2026-06 | https://cryptobriefing.com/oracle-ai-backlog-638-billion/ | S |
| O6 | EBC：OpenAI 约 $300B / 5 年（转 WSJ） | 2026-07 | https://www.ebc.com/forex/oracle-stock-falling-ai-backlog | S |
| O7 | S&P 下调至 BBB−（FY27 capex 估 $90–95B） | 2026-07-09 | https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101695609 | S |
| M1 | MSFT 10-K FY2025 | 2025-07-30 | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm | P |
| M2 | MSFT 10-Q 2025-09-30 | 2025-10-29 | https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm | P |
| M3 | MSFT 10-Q 2025-12-31 | 2026-01-28 | https://www.sec.gov/Archives/edgar/data/789019/000119312526027207/msft-20251231.htm | P |
| M4 | MSFT 10-Q 2026-03-31 | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm | P |
| M5 | MSFT 10-K FY2026 | 2026-07-29 | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm | P |
| M6 | MSFT 10-Q 2026-09-30 / 新闻稿 | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm ; https://www.sec.gov/Archives/edgar/data/789019/000119312526436122/msft-ex99_1.htm | P |
| M8 | Constellation Research：OpenAI 约占 RPO 45% | 2026-01-28 | https://www.constellationr.com/insights/news/microsoft-q2-strong-azure-growth-39-openai-45-rpo | S |
| M9 | MarketBeat：MSFT Q4 FY26 电话会摘要 | 2026-07-29 | https://www.marketbeat.com/instant-alerts/microsoft-q4-earnings-call-highlights-2026-07-29/ | S |
| M10 | TradingKey：MSFT Q1 FY27 电话会转录（第三方延迟、约 $170B） | 2026-10-28 | https://www.tradingkey.com/news/transcripts/262249601-tradingkey | S |
| G1 | GOOGL 10-Q Q2'25 | 2025-07-24 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000062/goog-20250630.htm | P |
| G2 | GOOGL 10-Q Q3'25 | 2025-10-30 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000091/goog-20250930.htm | P |
| G3 | GOOGL 10-K FY2025 | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | P |
| G4 | GOOGL 10-Q Q1'26 | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | P |
| G5 | GOOGL 10-Q Q2'26 | 2026-07-23 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm | P |
| G6 | GOOGL 10-Q Q3'26（Crux、兜底） | 2026-10-29 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm | P |
| G7 | GOOGL Q3'26 新闻稿 | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm | P |
| G8 | Investing.com：Alphabet Q3'26 电话会转录 | 2026-10-28 | https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037 | S |
| Z1 | AMZN 10-Q Q2'25 | 2025-08-01 | https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/amzn-20250630.htm | P |
| Z2 | AMZN 10-Q Q3'25 | 2025-10-31 | https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm | P |
| Z3 | AMZN 10-K FY2025 | 2026-02-06 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm | P |
| Z4 | AMZN 10-Q Q1'26 | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm | P |
| Z5 | AMZN 10-Q Q2'26（OpenAI、Anthropic 承诺） | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm | P |
| Z6 | AMZN Q3'26 新闻稿 EX-99.1 | 2026-10-29 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm | P |
| Z7 | AMZN EDGAR submissions（Q3 10-Q 未递交） | 2026-10-30 查询 | https://data.sec.gov/submissions/CIK0001018724.json | P |
| F1 | META Q3'26 新闻稿 EX-99.1 | 2026-10-21 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm | P |
| R1 | repo 复用：`companies/nbis/2026-10-23/research/gpu_cloud_economics_peers.md`、`balance_sheet_financing_runway.md`；`companies/_mega7_refresh_2026-10-29/synthesis.md`；`companies/_earnings_msft_googl_2026-10-28/note.md`；`companies/amzn/2026-10-29/refresh_note.md`；`companies/googl/2026-10-29/raw/goog_10q_2026-09-30.txt`；`companies/meta/2026-10-29/refresh_note.md`；`companies/orcl/2026-08-07/` | 2026-08-07 至 10-29 | 本地文件 | 按原文件标注 |
