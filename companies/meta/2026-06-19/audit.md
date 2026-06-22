# META Audit (Stage 7) — as_of 2026-06-19

## 1. 完整度评估
| 模块 | 状态 | 证据强度 |
|---|---|---|
| M1 证据脊柱 | 锚定季度(Q1 2026)+全年(FY2025) 载荷数全回挂 A1（SEC 直取 8-K/10-Q/10-K）| 高 |
| M2 主题/机制 | business_model 完成（广告引擎质量全坐实）| 高 |
| M3 利润池/护城河/瓶颈/operator | 完成；但 capex ROI 定量(O4)、proxy 精确数(O3) OPEN | 中 |
| M4 财务现实 | 完成；owner earnings 桥建好，但维护性 vs 增长 capex 拆分(O1)、RL 全年逐行(O2) OPEN | 中高 |
| M5 反演/陷阱 | 完成 | 高 |
| M6 估值/定价 | 三情景 + 价格带完成；但 base IRR 高度依赖 owner-earnings 锚(=O4) | 中 |

**completeness ≈ 62%**。载荷性当前事实（决定 verdict 的 FY25 + Q1 2026 + 价格）扎实；缺口集中在**决策胜负手**（capex ROI 定量 O4——它直接决定 owner-earnings 锚、决定 base IRR 过不过门槛），以及 10-K 逐行、proxy、RL 全年。这些里 O4 是 blocking（封 ceiling + 压 verdict），其余是 haircut。

## 2. verdict ceiling 规则（铁律 2）
- `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。
- 完整度 ~62% → **ceiling = STARTER**（60–80 下沿）。

## 3. 双重封顶（完整度 + 价格）
- **来自完整度**: STARTER（62%，且缺的是决策胜负手 O4）。
- **来自价格**: base IRR **+4.0% < 8% 门槛**，现价高出保守公允价 ~21% → **价格把实际可执行 verdict 从 STARTER 进一步压到 WATCH**（现价无 MOS，不支持新钱建仓；只支持"等回撤"）。
- **净 verdict = WATCH**（ceiling 是 STARTER，但价格这一更紧的约束把现价 verdict 压到 WATCH）。这与 GOOGL 同型（价格封顶），但 META 价格折让程度较轻（base +4% vs GOOGL base −3%），且广告引擎更强。

## 4. 算术勾稽
- 市值: 2,564M × $577.22 = $1.480T ✓（隐含股数 = $26,773M / $10.44 = 2,564M ✓）
- forward 经营 P/E: $577.22 / ($18.7B×4/2,564M×1000=$29.17) = 19.8x ✓
- FCF yield: $49.6B / $1,480B = 3.35% ✓
- IRR: base (701/577.22)^.2−1 = +4.0% ✓；bear (332/577.22)^.2−1 = −10.5% ✓；bull (1171/577.22)^.2−1 = +15.2% ✓
- owner earnings 桥: GAAP NI $26.773B − $8.03B 一次性税收 → 经营税前 $21.752B × (1−14%) = $18.7B/季 × 4 = $74.8B 年化 ✓；FCF $12.39B × 4 = $49.6B ✓

## 5. 内部一致性与 stale 检查
- 首次建档（meta/ 此前仅有 evidence 脊柱 3 文件 + 空 raw/financials/model）；无 v1/v2 stale 文件。
- 所有模块用同一 as_of=2026-06-19、同一价格 $577.22、同一股数 2,564M、同一市值 $1.48T。
- GAAP 净利含 $8.03B 一次性税收优惠的口径警告已贯穿 facts / financial_quality / owner_earnings_bridge / valuation，未用 GAAP 净利直接估值 ✓。
- 历史盲测案（meta_2022-11-10）仅作先验对照，历史价格/事实未当当前 ✓。

## 6. 给 IC 的质询点
1. **owner-earnings 锚是估值的全部胜负手**: base IRR 在 FCF 锚下 ~0%、经营 NI 锚下 ~+10%、中点 +4%。panel 须正面回答: 在 capex ROI 无一手量化（O4 blocking）下，该用哪个锚？保守锚 → 现价无 MOS → WATCH。
2. **价格 vs 完整度哪个是 binding**: 完整度封 STARTER，价格压到 WATCH。两者一致指向"不在现价新钱建仓"。
3. **创始人控制在重资本期**: 2022 验证为正，但当前停回购全押 capex 是无外部约束的单边下注。within-band lens 下计 haircut 还是更重？
4. **广告引擎强 ≠ 买入理由**: +33%/单价 +12% 是 thesis 质量证据，但不能盖过 base IRR 不过门槛——别被满血叙事带跑（这正是框架要防的）。
5. **bear 可存活**: 净现金 + 强 OCF → bear −42% 是 de-rate 非破产 → 无硬 veto，是 size/价格控制。
