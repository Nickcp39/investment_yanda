# AMZN Audit (Stage 7) — as_of 2026-06-19

## 1. 完整度评估
| 模块 | 状态 | 证据强度 |
|---|---|---|
| M1 证据脊柱 | 锚定季度(Q1 2026)+全年(FY25) 载荷数全回挂 A1（SEC 8-K Ex99.1 本地落盘）| 高 |
| M2 主题/机制 | business_model 完成 | 高 |
| M3 利润池/护城河/瓶颈/operator | 完成，但广告单列(O5)、Trainium/backlog 定量(O5)、proxy(O3) OPEN | 中高 |
| M4 财务现实 | 完成；**owner earnings 桥无法闭合**（capex 维护/增长拆分 + ROIC = O4，缺一手）| 中（核心拆分缺）|
| M5 反演/陷阱 | 完成 | 高 |
| M6 估值/定价 | 双口径三情景 + 价格带完成 | 中高（情景为 E1）|

**completeness ≈ 62%**。载荷性当前事实（FY25 + Q1 2026）扎实且全 A1；缺口集中在 **owner earnings 桥的胜负手（$200B capex 的维护/增长拆分 + ROIC，O4）**、10-K 逐行、proxy、Anthropic 会计——这些是 haircut/封顶项。

## 2. verdict ceiling 规则（铁律 2）
- `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。
- 完整度 ~62% → **完整度 ceiling = STARTER（60–80 区间下沿）**。
- **但价格封顶先生效**: 现价 base IRR 负、bull 才勉强够门槛 → **价格把实际 verdict 压到 WATCH**（同 GOOGL 机制：价格无 MOS 时 verdict 不能给开仓档）。
- **净 ceiling = WATCH**（价格封顶 < 完整度封顶）。

## 3. 双重封顶逻辑
- 来自完整度: STARTER（62%）。
- 来自估值: **WATCH**——即便给足 capex 信用的 NOPAT 口径，base 5y IRR ≈ −1.5%、bull +7.7%（<8% 门槛），起始收益率仅 2.1–2.5%。价格无安全边际。
- **取更严者 → 净 ceiling = WATCH**，size 0%，buy-below ~$175–180。

## 4. 算术勾稽
- 市值: 10,874M × $244.39 = $2.657T ✓
- trailing GAAP P/E: 244.39 / 7.17 = 34.1x ✓（含股权收益，低估真实经营倍数）
- AWS OI 占比: FY25 45.6/80.0 = 57% ✓；Q1 14.2/23.9 = 59% ✓
- 起始收益率: NOPAT $67B / $2657B = 2.5% ✓；保守 OE $55B → 2.1% ✓
- IRR (NOPAT 口径): base (2460/2657)^.2−1 = −1.5% ✓；bull (3840/2657)^.2−1 = +7.7% ✓；bear (1280/2657)^.2−1 = −13.5% ✓
- FCF 坍塌勾稽: FY25 OCF $139.5B − capex $131.8B = $7.7B（PR 报 FCF $11.2B，差异为 capex 口径含 finance lease/proceeds 调整，量级一致）✓；TTM OCF $148.5B − capex $151.0B ≈ −$2.5B（PR 报 +$1.2B，口径差异，均为"近零"量级）✓

## 5. 内部一致性与 stale 检查
- 无 v1/v2 stale 文件（首次建档）。所有模块用同一 as_of=2026-06-19、同一价格 $244.39、同一股数 10,874M。
- GAAP 净利含 Anthropic 收益的口径警告已贯穿 facts/financial_quality/valuation——未用 GAAP EPS $2.78/$7.17 直接估值。
- owner earnings 桥**显式标记无法闭合**（不假装算出精确 OE），用双口径 band + IRR 表达不确定。

## 6. 给 IC 的质询点
1. **这是 GOOGL 还是 NVDA 情形？** 答: GOOGL 同构——好生意 + capex 黑洞 + 价格无 MOS。但 AMZN 价格更贵（处 52 周区间中上部，非贴低），FCF 更极端（近零）。panel 须正面回答: 价格是否就是卡点？
2. **owner earnings 桥不闭合**: $200B capex 的维护/增长拆分 + ROIC 缺一手（O4）。这把 owner earnings 起点压成一个 band（$45–67B），而非点估。panel 如何在"FCF 近零"与"正常化 OE 可能 $50B+"之间定位？
3. **GAAP 净利质量**: $16.8B Anthropic 收益使 Q1 EPS $2.78 失真，不能直接算 P/E。
4. **加杠杆**: 长债季增 $53B 到 $119B——资产负债表从堡垒转向投资期。是 haircut（OCF 可服务）还是升级风险？
5. **价格封顶 vs 完整度封顶**: 62% → STARTER，但价格 → WATCH，取更严。这与 NVDA（价格友好、完整度封 STARTER）相反，与 GOOGL（价格封 WATCH）一致——证明框架按客观事实区分，未被"AI 赢家/Mag7"叙事带跑。
