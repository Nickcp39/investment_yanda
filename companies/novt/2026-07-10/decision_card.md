# NOVT Decision Card — as_of 2026-07-10

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10
**context_label**: quality_compounder_no_margin_of_safety__robotics_mostly_option · **status**: DECISION_DRAFT · **completeness**: ~60%
**batch**: ai_robotics_2026-07-10 (§1 thesis answered in `thesis_answer.md`)

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$156.65**（2026-07-10 收盘，≤ as_of；Yahoo=stockanalysis 两源到分一致）|
| market cap | **~$5.915B**（~37.76M 稀释股 × $156.65）|
| business_verdict | **good**（好生意，非卓越/非收费站）|
| new_money_verdict | **WATCH（0%）** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%**（现价无安全边际）|
| buy_below | **~$115**（base 5y IRR 回到 8% hurdle 的中性价，近 52 周低）|
| verdict ceiling | 完整度 ~60% → WATCH/STARTER 边界；价格无 MOS → 封到 **WATCH** |
| binding_constraint | **价格（无 MOS）** — base IRR +1.2% << 8%，且支撑 47x 的机器人上行仍是 2027 预期 |

## 机器人 thesis 速答（详见 thesis_answer.md）
- **机器人收入占比**: ~15–25%(components-into-robots 口径,**估算**,公司不单独披露);humanoid/embodied-AI 专门 **<1–2%,基本 pre-revenue**。基座 = 医疗 53% + 高级工业 47%。
- **真需求 vs 预期**: 工业机器人=真现金但单位数(rev +7%);humanoid=预期(Holoscan 原型期,2027 才 meaningful)。+37% bookings 含全年订单前置。
- **capital_cycle**: applicable=partial;humanoid 段=EARLY-ANTICIPATION(共识、资本在涌入→别追);工业基座=中周期回升;supply_barrier=在位精密 niche med-high、humanoid 抢位 low;caution=**别为 humanoid 期权付溢价**。
- **真瓶颈 vs 概念**: 真、可证伪的换机成本/精密 know-how 护城河(44% GM、vitality 27%、Holoscan 唯一 servo drive),**但是零件级,不是 NVDA 式收费站**;humanoid 现为概念/期权。
- **拆分**: 现价 ~47x adj 主要买**医疗+工业精密件的高质量复利机**,humanoid 只是小内嵌期权;为"人形机器人敞口"买 NOVT = 为 <2% pre-revenue 溢价买单。

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+1** | med | 分部/财务/价格全一手核实;但机器人收入**无披露**(估算 O1)、operator OPEN;价格 2 源到分交叉 |
| M2 主题/机制 | context+conviction | **+1** | med | 真 secular 向量但是 picks-and-shovels 零件商,非 chokepoint;机器人 ~15–25%,humanoid <1–2% 原型 |
| M3 利润池/耐久 | conviction | **+1** | med | designed-in 护城河真实(44% GM、Holoscan、consumables 15%),但零件级、M&A 依赖、GAAP<<adj |
| M4 财务现实 | conviction | **0** | med | 净现金 ~$121M 堡垒、可存活;但 FCF 转换弱(FY25 FCF $54M/yield<1%)、GAAP vs adj 2.2x gap |
| M5 反演/陷阱 | risk | **−1** | high | 无 thesis 破裂/无偿付风险;主风险=**paying-up trap**,multiple 压回致 −30~35% 而 thesis 不破 |
| M6 定价/仓位 | price+output | **−2** | high | 47.6x adj、fwd EV/EBITDA 23x、FCF yield<1%、距高点 −8.8%;base IRR +1.2%<<8% → **价格是卡点** |

## 三情景（5y IRR @ $156.65，hurdle 8%）
| 情景 | 路径 | y5 adj EPS | 退出 P/E | y5 价 | 5y IRR |
|---|---|---:|---:|---:|---:|
| Bear | 有机走平+工业下行+de-rate 向 $98 | $4.00 | 24x | ~$100 | **−8.5%** |
| Base | ~7% 营收/~10% adj EPS,multiple 归 30x | $5.30 | 30x | ~$166 | **+1.2%** |
| Bull | humanoid/机器人 2027 拐点,双位数,溢价保持 | $6.62 | 34x | ~$234 | **+8.4%** |

> base **+1.2% << 8% hurdle**;连 bull 才勉强 8% 且**需 2027 humanoid 真兑现** → 现价为预期付费,无安全边际。

## 价格带
- **No new money @ $156.65**（已在 ~$115 无 MOS 线之上）。
- **Starter 区** ~$100–120(base IRR 回 8% 之上)**或** 机器人 booking→revenue 双位数且 book-to-bill>1.1 连续 2 季(证伪前置)+ FY26 OCF 兑现,initial 3–5%。
- **Add 区** ~$95–105(向/破 52 周低)且确认双位数有机 + humanoid 有金额披露 → 8–12%(周期封 Core 以下)。
- **No-chase** 向 $171.85 ATH。

## Kill Criteria
K1 有机走平/负 + B2B<1.0(2 季) · K2 机器人营收减速 + bookings 正常化(前置被证实) · K3 GM<42% · K4 商誉减值/毁价并购 · K5 Holoscan 内容商品化/被设计出局 · K6 价格持续 >~$115 且无增长加速 → 维持 WATCH(现已触发)。

## runner_dissent
多头本能:净现金、44% 毛利、designed-in、机器人 bookings +50%、consumables 15%、NVIDIA Holoscan 唯一 servo drive——为何不开小仓赌机器人期权?框架 override 到 WATCH,因为**价格是卡点**:~47x adj 对单位数有机增长,base 5y IRR +1.2%(<<8%),连 +8.4% 的 bull 都要靠 2027 humanoid 真兑现——等于今天为预期付溢价。机器人业务真但小(~15–25%,主要工业,营收单位数),humanoid <1–2% 且 pre-revenue。以本批的判据(需求暴增+瓶颈+已赚钱),NOVT **瓶颈腿不过**(好零件护城河,非收费站)、**现金腿只过一半**。是质量型 WATCH,不是机器人版 NVDA。未决 OPEN:机器人收入 $(O1,公司不披露)、operator/proxy(O3)、owner-earnings 桥质量(O4)、2027 humanoid 量级(O5)。

## OPEN（封顶完整度）
O1 机器人收入 $ 拆分（公司未披露）· O2 10-K 逐行/10 年序列/地区客户集中（EDGAR 403,用 relay）· O3 proxy/operator · O4 owner-earnings 桥质量 · O5 Holoscan-humanoid 2027 量级 · O6 关税/中国/诉讼。
