# NVDA Audit (Stage 7) — as_of 2026-06-19

## 1. 完整度评估
| 模块 | 状态 | 证据强度 |
|---|---|---|
| M1 证据脊柱 | 锚定季度(Q1 FY27)+全年(FY26) 载荷数全回挂 A1/A2 | 高 |
| M2 主题/机制 | business_model 完成 | 高 |
| M3 利润池/护城河/瓶颈/operator | 完成，但 custom-silicon 定量份额(O4)、proxy(O3) OPEN | 中高 |
| M4 财务现实 | 完成；FY26 OCF/FCF 为 B1 近似(O1)、10 年序列早期年份冲突(O2) | 中高 |
| M5 反演/陷阱 | 完成 | 高 |
| M6 估值/定价 | 三情景 + 价格带完成 | 中高（情景为 E1）|

**completeness ≈ 65%**。载荷性当前事实（决定 verdict 的 FY26 + Q1 FY27）扎实；缺口在前瞻定量（custom-silicon 份额）、10-K 逐行、proxy、10 年精确序列——这些是 haircut/封顶项，不阻断决策草案。

## 2. verdict ceiling 规则（铁律 2）
- `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。
- 完整度 ~65% → **ceiling = STARTER**。即便估值友好（base IRR 13%、forward 19x），**完整度不足以支撑 CORE**。
- 周期股纪律（铁律 3）→ size 天花板另封在 **Confirmed 以下**（max ~12%）。

## 3. completeness → ceiling 的双重封顶
- 来自完整度: STARTER（65%）。
- 来自周期性/耐久性 haircut: size cap ≤ Confirmed（~12%）。
- 来自估值: 现价 base IRR +13% **未触发价格封顶**（与 GOOGL 相反——GOOGL 是价格把 ceiling 压到 WATCH；NVDA 估值不压制，完整度才是 binding ceiling）。
- **净 ceiling = STARTER**，size 初始 3–5% / 最大 ~12%。

## 4. 算术勾稽
- 市值: 24,391M × $145.48 = $3.548T ✓
- forward P/E: 145.48 / 7.48 = 19.4x ✓
- IRR: bear (80/145.48)^.2−1=−11.3% / base (266/145.48)^.2−1=+12.8% / bull (495/145.48)^.2−1=+27.7% ✓
- owner earnings 桥: non-GAAP EPS $1.87 × 24,391 = $45.6B/季 × 4 ≈ $182B；FCF run-rate ($48.55B×4≈$194B) 略高，取 $180–185B 保守带 ✓

## 5. 内部一致性与 stale 检查
- 无 v1/v2 stale 文件（首次建档）。所有模块用同一 as_of=2026-06-19、同一价格 $145.48、同一股数 24,391M。
- GAAP 净利含股权证券收益的口径警告已贯穿 facts/financial_quality/owner_earnings_bridge，未用 GAAP 净利直接估值。

## 6. 给 IC 的质询点
1. **估值是友好的**——这不是 GOOGL 式"好生意错价格"，而是"好生意 + 合理偏低价格 + 前瞻不确定"。panel 须正面回答: 在 forward 19x / base IRR 13% / yield 5.1% 下，binding constraint 是否真是 run-rate 可持续性而非价格？
2. **pull-forward 不可证伪**: Q2 指引 $91B 仍升，但无法排除部分为周期高点提前下单。这是 haircut 还是该升为 veto？（修好的规则: haircut）
3. **custom silicon 份额未定量(O4)**: 这是唯一能升级为结构性破裂的路径，但当前 DC +92% 未见份额坍塌。panel 如何在"证据不足"与"份额未塌"间定位？
4. **GAAP 净利质量**: $30.2B 股权头寸使 GAAP EPS 失真，估值须用 non-GAAP/经营 owner earnings。
5. **周期股 vs 真瓶颈**: 这是 exceptional_bottleneck（瓶颈真实、多季坐实），但仍是周期需求——size 封 Confirmed 以下是否正确？
6. **完整度封顶**: 65% → STARTER，估值友好不能突破到 CORE。
