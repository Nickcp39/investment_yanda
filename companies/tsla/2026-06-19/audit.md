# TSLA Audit (Stage 7) — as_of 2026-06-19

## 1. 完整度评估
| 模块 | 状态 | 证据强度 |
|---|---|---|
| M1 证据脊柱 | 锚定季度(Q1 2026)+全年(FY2025) 载荷数多源交叉一致；**但 SEC 10-Q/10-K 逐行 403 未直取（分部利润 OPEN）** | 中 |
| M2 主题/机制 | business_model 完成（DELIVERED vs NARRATIVE 严格区隔）| 中高 |
| M3 利润池/护城河/瓶颈/operator | 完成；护城河窄化、无瓶颈地位、key-man 强封顶；proxy(O3) + 能源分部利润(O5) OPEN | 中 |
| M4 财务现实 | 完成；利润率压缩趋势清晰；但 FCF 美化 + 分部利润(O1) OPEN | 中 |
| M5 反演/陷阱 | 完成 | 高 |
| M6 估值/定价 | 三情景 + moonshot + 价格带完成 | 中高（情景 E1）|

**completeness ≈ 55%**（低于 NVDA 的 65%）。原因: ①SEC 逐行 403 未直取 → 分部利润（能源/AI 到底赚不赚钱）这个**关键缺口**无一手；②robotaxi/Optimus 单位经济无法量化（O2）；③proxy 未取（O3）。但**决定 verdict 的核心事实（营收/利润率塌缩、交付 −9%、极端估值、$1T 包稀释）是多源交叉坐实的**，足够交 DECISION_DRAFT。

## 2. verdict ceiling 规则（铁律 2）
- `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。
- 完整度 ~55% → **ceiling = WATCH**（40–60% 区间）。
- **更紧的封顶来自价格**: 现价对 DELIVERED 基本面无任何安全边际（只有 moonshot 过 8% 门槛、base IRR −17%）→ **价格独立把 verdict 压到 WATCH/REJECT 区**，即便完整度更高也不解封。
- **净 ceiling = WATCH（新钱 0%）**，business_verdict = uncertain。

## 3. completeness → ceiling 的双重封顶（与 NVDA 对照）
- 来自完整度: WATCH（55%）。
- 来自价格: WATCH/REJECT（无 MOS）——**本案的主导封顶**。
- 来自 operator: key-man（Musk）+ $1T 包 12% 稀释 → 进一步压制 size。
- **净 ceiling = WATCH**，suggested size 0%（new money REJECT/WATCH）。
- 对照: NVDA 完整度封顶 STARTER 但价格友好开仓；**TSLA 价格 + 利润池收缩封顶 WATCH，不开仓**。同一框架对"价格友好的真瓶颈"与"价格极端的故事股"给出相反结论。

## 4. 算术勾稽
- 市值: 3,528M × $400.49 = **$1,413B** ✓（$1.4–1.5T 区间，diluted 口径）。
- P/E: 400.49 / 1.08 = **371x** ✓；P/FCF: 1413 / 6.22 = **227x** ✓。
- 起始 OE yield: 5 / 1413 = **0.35%** ✓（FCF 口径 6.22/1413 = 0.44%）。
- IRR: bear (84/400.49)^.2−1 = −27% ✓ / base (159/400.49)^.2−1 = −17% ✓ / bull (520/400.49)^.2−1 = +5.3% ✓ / moonshot (1030/400.49)^.2−1 = +21% ✓。
- 距 52 周高 −19.7% ✓ / 高于低 +38.7% ✓。

## 5. 内部一致性与 stale 检查
- 首次建档，无 v1/v2 stale 文件。全模块同 as_of=2026-06-19、同价格 $400.49、同股数 3,528M。
- **DELIVERED vs NARRATIVE 区隔**已贯穿 facts/business_model/valuation/scenario_model——robotaxi/Optimus 未计入 DELIVERED owner earnings，仅作 upside tail（moonshot）。
- FCF 美化警告（capex 低谷 [C2]）、GM 一次性项警告 [C1] 已贯穿。

## 6. 给 IC 的质询点
1. **这是不是 GOOGL 式价格封顶、还是更紧？** 现价对 DELIVERED 基本面 base IRR −17%、只有 moonshot 过门槛——价格封顶比 GOOGL（bull +5%）更紧。panel 须确认 verdict = WATCH/REJECT 而非 STARTER。
2. **能否让故事驱动 size？（铁律核心）** robotaxi/Optimus 是真期权但未兑现、不可量化。panel 须确认 size 跟 DELIVERED 信念走（薄且收缩）→ 0%，不被 narrative 带跑。
3. **资产负债表 fortress 是否足以开小仓？** 净现金 $35.5B 死不了——但"死不了"≠"该买"；价格无 MOS 下，fortress 不构成买入理由。
4. **key-man + $1T 稀释如何计入？** 估值人格化绑定 Musk + 12% 稀释悬顶 → operator 封顶。
5. **完整度 55% + SEC 逐行缺口（分部利润）**: 能源/AI 是否真利润腿无一手 → 进一步支持封顶在 WATCH。
6. **runner_dissent 方向**: 机械结论 = WATCH/REJECT。是否有"too_small_missed_asymmetry"（SNDK 教训）的反向风险？见 dissent——本案是相反风险（故事溢价的价格陷阱），不是错过真便宜的瓶颈。
