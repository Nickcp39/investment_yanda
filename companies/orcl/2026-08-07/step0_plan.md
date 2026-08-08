# ORCL Step-0 Plan — run_date 2026-08-07

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **as_of**: 2026-08-06（最后已结算收盘）
**status**: DECISION_DRAFT

## 1. 冻结的研究范围（Scope & Definition）

| 项 | 值 |
|---|---|
| ticker / share class | **ORCL**, NYSE, 普通股单一股权类别（无双层结构） |
| as_of | **2026-08-06**（最后已结算收盘；2026-08-07 美东 13:45 市场仍在交易，不用盘中价） |
| run_date | 2026-08-07 |
| 财年口径 | Oracle 财年 **5/31 结束**。FY2026 = 2025-06-01 ~ 2026-05-31，Q4 FY2026 于 **2026-06-10** 盘后公告 |
| 决策目的 | ①给出 ORCL 自身的 business/new-money 裁决；②**把 ORCL 当作"AI capex 豪赌被市场否决"的对照实验**，产出可回喂 GOOGL/AMZN/META/MSFT 的可观测序列 |
| 时间跨度 | 10 年（与 GOOGL 卡一致，便于横比） |
| hurdle rate | **8%** |

## 2. 为什么这轮选 ORCL（选题理由，先于结论写下）

本库有四张卡卡在**同一个未解数字**上：

| 卡 | 未解项 | 编号 |
|---|---|---|
| GOOGL 2026-07-24 | maintenance vs growth capex 拆分；未披露 capex ROI hurdle | O1 / O2 |
| AMZN 2026-06-19 | $200B capex 维护/增长拆分 + ROIC（blocking，owner-earnings 桥胜负手）| O4 |
| META 2026 | 同类 | O4 |
| MSFT 2026 | 同类 | O2 |

这四家都还**没有被市场否决**——所以我们无法观察"如果市场不再给 capex 信用，会先看到什么"。
Oracle 押了同一注（**债务融资的 AI 数据中心建设 vs 巨额合同 backlog**），但市场已经投过票：
自 2025-09-10 峰值收盘 $324.63 起 **−55.8%**，距 52 周高点 $345.72 **−58.5%**。

**ORCL 因此是一个自然对照实验**：同样的机制、同样的会计模糊地带，但**结果已知**。
本轮的最高价值产出不是 ORCL 的买卖裁决，而是 `decision_card.md` 的
`## 回喂：capex 豪赌失败的可观测序列` —— 一份可以直接套回其余四家的观察清单。

## 3. 本轮必须回答的问题（先于结论冻结）

- **(a) 资金面**：capex 实际数、融资结构（新增债务 vs 股权）、净债务、利息负担；FCF 正负与趋势。
- **(b) Backlog 质量**：RPO 规模与季度轨迹、集中度（OpenAI/Stargate 类承诺）、**交易对手信用**。
  Backlog 只值"客户付得起"那么多。
- **(c) ROI 披露**：Oracle 是否披露 capex ROI hurdle / 增量 ROIC / 维护-增长拆分？
  **若没有，"没有"本身就是发现**——而且要和合并 ROIC 的实际走向做交叉检验。
- **(d) 可迁移教训**：市场停止给信用时，**哪些指标先转、按什么顺序转**？写成清单。
- **(e) −55.8% 是估值 de-rating 还是生意本身减值？** 用数字把两者分开。

## 4. 完成标准（先于结论写下）

本轮达到 `DECISION_DRAFT` 需要：

- [x] as_of 价格为已结算收盘、双源交叉验证、delta 明示
- [x] FY2026 完整损益表（含利息费用、税、优先股股息）来自 8-K 原文口径
- [x] FY2022–FY2026 现金流量表 + 资产负债表五年序列
- [x] RPO 四季度轨迹 + 12 个月转化率 + 集中度估计（并标注 Oracle 披露 vs 媒体报道）
- [x] 三情景 IRR，owner-earnings 起点显式、CAGR 显式、退出倍数显式
- [x] buy_below 锚 + 价格梯子
- [x] kill criteria 三态 + runner_dissent + OPEN 清单封顶 completeness
- [x] `## 回喂` 序列清单
- [x] `freshness.json` + `verify_freshness.py` PASS
- [ ] 10-K 原文逐行（服务器折旧年限、资本化利息、分部毛利率、客户集中度风险因子原文）← **本轮未达成，见 OPEN**

## 5. 已知的方法论风险（先记下，防止自我欺骗）

1. **叙事对称陷阱**：ORCL 跌了 55%，很容易写成"所以 GOOGL/AMZN 也会跌"。
   但 ORCL 与那四家有一个**结构性差异**：ORCL 用债务和股权融资 capex，那四家用经营现金流。
   回喂清单必须把"杠杆"这一条单独拎出来，不能把 ORCL 的结局无差别外推。
2. **INC-001 教训**：现价必须机械校验。本轮 as_of 用 2026-08-06（$143.47），因为 08-07 当日盘中未收。
   如果误用 08-07 盘中价，所有衍生数会内部自洽地错下去。
3. **来源降级**：SEC.gov / oracle.com 本轮对抓取返回 403。
   8-K 数字通过 StockTitan 的 SEC filing 复刻页取得（**转载一手，非二手评论**），
   已与另一独立聚合源（stockanalysis.com）逐行对账。仍标注为 A1-proxy 而非 A1。
