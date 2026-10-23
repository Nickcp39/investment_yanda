# NBIS Decision Card — as_of 2026-10-22 (EVENT RERUN: Q3 earnings due TODAY + financing escalation)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-10-22
**status** DECISION_DRAFT · **completeness** ~70%
**refresh_of** `companies/nbis/2026-09-05` (RE-PRICE + SOURCE UPGRADE)
**context_label** `price_finally_in_band_but_leverage_escalated_and_proof_metric_still_absent`

> ## ⚠️ 两件必须先说清的事
> 1. **今天（2026-10-22）是 NBIS 的 Q3'26 财报日**，但截至本次运行（美东 11:23），
>    **财报尚未发布**（nebius.com 新闻中心无 Q3 结果稿、SEC 无对应 6-K、聚合源无实际数字）。
>    本卡所有 Q3 数字都是**分析师估计**，不是公司披露。
> 2. **本轮价格是盘中实时价，非收盘价**。见 M6 与 freshness.json 的 `intraday` 标注。

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **~$160.39（盘中，10/22 11:23 ET）** · 前收 $171.57（10/21） |
| vs prior card ref ($226.39, 09-04) | **−29.1%** |
| vs 08-13 真实参照收盘 $254.40 | **−37.0%** |
| vs 52 周高 $299.86 | **−46.5%** |
| market cap | ~$43.9B（274.1M 股；Yahoo 摊薄口径 ~271.9M、已申报 238.4M） |
| business_verdict | **good**（连续四卡不变） |
| **new_money_verdict** | **WATCH (0%)** — 连续第四次 |
| existing_position_verdict | **HOLD**（账户持仓中） |
| suggested initial / max size | **0% / 4%** |
| **buy_below** | **$150–180（标称不变，但锚已恶化，见下）** |
| no_chase_zone | ≥$250（已无意义，现价远在其下） |
| binding_constraint | **M5 杠杆分支升级 + active MW 第五个季度未披露（Q3 今日待出）** |

## 六模块信号（net 0，上一卡 −1）— 唯一移动的是 M6

| Module | Role | 08-12 | 09-05 | **10-22** | 一句话 |
|---|---|---:|---:|---:|---|
| M1 Evidence Spine | confidence | −1 | 0 | **0** | Q3 6-K 尚未归档；Q2 已一手印证；active MW 仍待披露 |
| M2 Theme / Mechanism | context | +1 | +1 | **+1** | 满产售罄、单 MW 价续涨、Meta/MSFT 锚完好、$40B+ 长协 |
| M3 Profit Pool / Durability | conviction | +1 | +1 | **+1** | ⭐ 10/22 CRO 再确认"每 MW 价格仍超预期上涨" |
| M4 Financial Reality | conviction | 0 | 0 | **0** | 无新 Q3 数据；Q2 adj EBITDA 40.6% 但单季 FCF −$3.41B；负债已重 |
| M5 Inversion / Trap | risk | −2 | −2 | **−2** | 🔴 杠杆分支**从"转热"到"兑现"**：$5.75B 可转债 + $3.5B Citi 担保债 |
| M6 Price / Position | price | −1 | −1 | **0** | ⭐ $160 **首次进入** $150–180 带，但锚被杠杆拖低，非干净 MOS |

## 本轮最重要的实质变化：价格首次进了带，但锚在同步恶化

1. **价格 −29% 进了带**。$226.39 → ~$160，三年多以来第一次穿过 $180 的下沿。机械层面，
   这是 M6 从 −1 → 0 的原因，也是"现在有没有机会"这个问题第一次值得认真看。

2. **但杠杆分支（K-G）在同一时期兑现了，而且比旧卡预想的更大**：
   - 08-19 提议 $4.5B 可转债 → 上修至 **$5.0B** → 08-24 以 **$5.75B** 完成定价交割；
   - **10-22（今天）再签 $3.5B Citi 高级担保债**（364 天，SOFR+2.75%→最高 3.50%）。
   - Yahoo：总债务（mrq）**$10.2B**，债务/权益 **98.6%**——这还是 Q2 口径，未含上面两笔。
   - 旧卡 K-C 写"预付款 → 资产担保债 → 可转债 → ATM"的路径，**现在前三站全部走完**。

3. **证明指标 active MW 仍然缺席，Q3 今日待出**。BofA 估计退出 Q3 时 675MW 连接 /
   525MW active（年初 170MW）——**这是分析师估计，不是公司披露**。公司口径仍只有
   "合同 5GW + 连接指引 800MW–1GW（未上调）"。

4. **空头聚集**：9/30 空头 44.7M 股 = 流通盘 18.93%；Michael Burry 明确做空；CoreWeave
   CDS 利差升破"财务压力"阈值向全板块传染；Rothschild Redburn 给出 Sell / $84。

## 为什么 verdict 不翻转（第四次 WATCH）

价格进带触发了 C4（机械触发 ≠ 可执行入场）。按 C4，先重算锚：

- **锚的承重输入变了**：$150–180 带是在"接近净现金"的资产负债表上推的（旧卡 C111 还在
  争是净现金 $0.6B 还是净现金 $7.2B）。现在负债已到 ~$10B（Q2）再加 $5.75B 可转债 +
  $3.5B 担保债，**同样是 $160 的股价，对应的 EV 比旧锚高得多 → 每股的安全边际更薄**。
- **STARTER 的第二条硬条件仍不满足**：active MW 未披露（连续第五个季度，Q3 今日待出）。
- **好消息不构成买入条款**：满产、涨价、$40B 长协都是真的（M2/M3），但对面的杠杆成本
  是新增的真实约束，且 Q3 财报几小时后就要落地——在证明指标落地前追入，是在赌财报。

**结论：价格进带是"终于值得盯"，不是"现在可以买"。**

## Kill Criteria（carried + 更新状态）

- **K-A** active MW 持续不披露 + ARR 放缓 — 🟡 **仍 OPEN**：ARR 未放缓，但 active MW
  **第五个季度未披露**；Q3（今日）是裁决点
- **K-B** 锚客户砍 capex / 转竞争 — 🟢 未触发：$40B+ 长协、Meta/MSFT 锚完好
- **K-C** 融资从预付款转稀释 — 🔴 **实质兑现**：$5.75B 可转债（稀释）+ $3.5B 担保债（杠杆）
- **K-D** 折旧延寿 / rev-per-MW 下滑 — 🟢 反证：rev/MW 仍在涨（10/22 CRO 再确认）
- **K-E** capex 高端无转化 — 🟢 未坐实：capex $20–25B 指引，ARR/RPO 同步升
- **K-F** 集中度 / ICFR — ⬜ 仍无法判定
- **K-G** 杠杆分支 — 🔴 **升级**：非流动负债 $4.10B→$8.50B→+$5.75B 可转债→+$3.5B 担保债
- **K-VAL** 入场无 MOS — 🔴 **仍成立但形态变了**：价格进了带，但锚被杠杆拖低，净 MOS 未改善

## 存量仓（HOLD）的额外提示

- monitor 规则「2+ 🔴 → trim」：目前 🔴 计数 = **2**（K-C、K-G 同一杠杆分支，算一条
  主线；K-VAL 是估值不是基本面）。**已逼近 trim 门槛但未触发**，因为杠杆分支尚未
  直接损害经营（需求仍满、定价仍涨），且 Q3 今日落地是最后一块拼图。
- **Q3 财报是唯一枢纽**：① active MW 是否终于披露 ② ARR 是否在 $7–9B 轨道 ③ 单 MW 价
  是否守住 ④ 负债增速 ⑤ 是否还有新的融资/稀释。**财报落地后再定 HOLD/TRIM，不抢跑。**

## WATCH → STARTER trigger（不变，第四卡）

**(1)** 价格 < ~$180，**AND (2)** active MW 实际披露且与连接指引一致。近期可证伪检验
不变：ARR 6 月末 $3.0B → 年末 $7–9B（六个月 2.3–3.0×）。**Q3 2026 是 checkpoint，就在今天。**

## runner_dissent

这次运行最大的诚实义务是：**不要因为"价格终于进了带"就宣布转折。** 价格进带是事实，
但同一时期杠杆从"潜在风险"变成了"已发生的事实"（$5.75B 可转债 + $3.5B 担保债），
而 anchor 恰恰是在杠杆较轻的资产负债表上推的。把这两个放在一起看，**净安全边际并没有
比 09-05 更厚，甚至更薄**。另外，今天的运行环境拿不到 Yahoo 直连（403），freshness
机械门（verify_freshness.py）未能跑通，价格改为四源交叉验证（腾讯行情 / TipRanks /
Yahoo key-statistics / 富途），并如实标注 `intraday`——这一点不能假装是完整通过。
