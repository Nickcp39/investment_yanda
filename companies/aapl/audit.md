# AAPL Audit (Stage 7) — as_of 2026-06-19

## 1. 完整度评估
| 模块 | 状态 | 证据强度 |
|---|---|---|
| M1 证据脊柱 | 锚定季度(Q2 FY26)+全年(FY25/FY24) 载荷数全回挂 A1（S001/S002）；价格 A2（S005）| 高 |
| M2 主题/机制 | business_model 完成（年金 + Services 复利）| 高 |
| M3 利润池/护城河/瓶颈/operator | 完成；proxy(O3)、AI 入口定量(O4) OPEN | 中高 |
| M4 财务现实 | 完成；owner earnings 桥干净；FY16–FY23 早期序列 B2(O5) | 高 |
| M5 反演/陷阱 | 完成；Google TAC 量级(O1)、App Store 救济量级 OPEN | 中高 |
| M6 估值/定价 | 三情景 + 价格带完成（情景为 E1）| 高（输入扎实，IRR 派生）|

**completeness ≈ 60%**。载荷性当前事实（决定 verdict 的 FY25 + Q2 FY26 + 价格 + 资产负债表）扎实且全 A1/A2；缺口在前瞻定量（Google TAC 量级、AI 入口、App Store 救济）、10-K 逐行、proxy、早期 10 年序列——haircut/封顶项，不阻断决策草案。

## 2. verdict ceiling 规则（铁律 2）
- `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。
- 完整度 ~60% → 完整度本身落在 WATCH/STARTER 边界。
- **但真正的 binding 封顶来自 M6 价格门**: base 5y IRR +2.7% « 8% hurdle，现价无 MOS → **价格把 verdict 封到 WATCH**（与 GOOGL 同机制）。
- 净 ceiling = **WATCH**（价格门 binding；完整度 60% 一致支持封在 WATCH/STARTER 下沿，价格门取更严的 WATCH）。

## 3. 双重/三重封顶
- 来自完整度: ~60% → WATCH/STARTER 边界。
- 来自价格: base IRR +2.7% < 8% → **价格门封 WATCH（binding）**。
- 来自耐久性: 年金护城河 HIGH → 耐久性**不**压低天花板（若价格合理本可到 Core size）；此处不 binding。
- **净 ceiling = WATCH，size = 0%（新钱），存量 HOLD。**

## 4. 算术勾稽
- 市值: 14.726B × $298.01 = $4.388T ✓
- trailing P/E（TTM NI）: 4388 / 122.6 = 35.8x ✓；P/OE 4388/120 = 36.6x ✓
- 净现金: 146.6 − 84.7 = 61.9B ✓（占市值 1.41%）
- IRR base: 退出价 334 + 股息 5.5，(339.5/298.01)^(1/5)−1 = +2.66% ✓
- buy-below 8%: (334+5.5)/1.08^5 = 231 ✓
- TTM NI: 112.010 + 71.675 − 61.110 = 122.575 ✓

## 5. 内部一致性与 stale 检查
- 首次建档，无 v1/v2 stale 文件。所有模块用同一 as_of=2026-06-19、同一价格 $298.01、同一股数 14.726B、同一 OE 锚 $120B。
- 历史盲测案（2016 $90.34/~10x）的价格/事实**未**当当前事实使用；仅作 thesis 先验（耐久性高），并显式记录"价格起点完全不同"。

## 6. 给 IC 的质询点
1. **价格是 binding constraint**: 这是 GOOGL 式"好生意错价格"，不是 NVDA 式"好生意友好价"。panel 须正面回答: ~36x trailing / 2.7% OE yield / base IRR +2.7% 下，新钱给 0% 是否正确？
2. **2016 教训不复发的论证**: 2016 undersize 错在便宜（~10x + 净现金 31%）时不敢买；2026 是贵（~36x + 净现金 1.4%）时不该追。耐久性先验仍高，但价格门 binding——panel 须确认这不是重犯 undersize。
3. **Google TAC + App Store 救济（O1）**: 量级未定，是 haircut 还是该升 veto？（规则: haircut，除非 App Store 全球抽租结构性崩坏）。
4. **存量 vs 新钱**: 存量持有者 HOLD（优质资产、无减值、缩股复利）；新钱 WATCH（无 MOS）。panel 须分开两个 verdict。
5. **completeness 60% vs 价格门**: 哪个才是真正 binding？（结论: 价格门更严，封 WATCH）。
