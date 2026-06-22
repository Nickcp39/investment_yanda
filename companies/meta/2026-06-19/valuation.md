# META Valuation (M6) — as_of 2026-06-19

价格 [S005]: **$577.22**（2026-06-18 收盘，≤ as_of）· 隐含稀释股 ~2,564M（NI/EPS 反推，E1）· 市值 **~$1.48T**。模型见 `model/scenario_model.csv` + `model/owner_earnings_bridge.csv`。

## 1. 倍数起点
- Trailing FY25 GAAP P/E ≈ **24.5x**（$1.48T / $60.46B）。
- Forward 经营性 normalized P/E ≈ **19.8x**（剔一次性税收，op NI ~$74.8B 年化）。
- **FCF yield ≈ 3.4%**（FCF ~$49.6B 年化 / $1.48T）——被 capex 压制，远低于 NVDA 5.1% OE yield。
- 经营 owner-earnings yield ≈ 5.05%（若把 op NI 当 earning power；但 FCF 才是落袋现金）。
- 现价距 52 周高 $796.25 **−27.5%**；52 周低 $520.26（现价高于低点 ~11%）。

## 2. owner earnings 锚 — 估值的核心张力
**META 估值的不确定性不在增速，在"owner earnings 锚选哪个"**，而这取决于未决的 O4（capex 是黑洞还是复利机器）：
- 若锚 = **FCF $49.6B**（capex 是黑洞）→ P/FCF ~30x，base IRR ~0%，无 MOS。
- 若锚 = **经营 NI $74.8B**（capex 全是 value-creating earning power）→ P/OE ~20x，base IRR ~+10%，modest MOS。
- 取**中点 ~$62B**（部分 capex 复利、多数不确定）→ base IRR **+4.0%（< 8% 门槛）**。

## 3. 三情景 IRR（5 年，hurdle 8%）
| 情景 | OE 起点 | 5y CAGR | 退出倍数 | y5 隐含每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $55B | +2% | 14x | ~$332 | **−10.5%** |
| Base | $62B | +10% | 18x | ~$701 | **+4.0%** |
| Base-乐观（capex 全有效）| $75B | +11% | 19x | ~$950 | **+10.2%** |
| Bull | $65B | +16% | 22x | ~$1,171 | **+15.2%** |

- **base IRR +4.0% < 8% 门槛** → **现价无安全边际**（与 NVDA base +13% 相反，类 GOOGL 的"价格封顶"情形，但程度较轻）。
- 只有在**乐观锚（granting capex 全是复利 earning power）**下 base 才过门槛（+10.2%）——而这正是未决的 O4。

## 4. 公允价值参考
- Base（62/10%/18x）下，8% 门槛对应公允价 **~$477** → 现价 $577 **高出 ~21%**。
- 乐观锚（75/11%/19x）下，8% 门槛对应公允价 **~$637** → 现价 $577 低于此 ~9%（仅当 capex 兑现复利才有 modest MOS）。
- **结论**: 公允价区间 **~$477–637**，现价 $577 落在区间偏上，**MOS 取决于 capex ROI 这个未决变量**。

## 5. 价格带（buy-below / size 锚）
| 档位 | 含义 | 价格 | vs $577 |
|---|---|---:|---:|
| Buy-below（base 8% 门槛，保守锚）| 有正 MOS 的建仓上限 | **~$480** | −17% |
| Starter zone（乐观锚有 modest MOS）| 仅在愿意 grant capex 复利时 | **~$480–520**（向 52 周低）| −10% 至 −17% |
| No-chase / trim 警戒 | base IRR 明显 <8% | **> ~$640** | +11% |
| 下行参考 | bear 兑现 | ~$332（−42%，可存活非破产）| — |

## 6. binding constraint
- **价格 + owner-earnings 锚的不确定性是双重 binding constraint**：现价已把"capex 全是复利"的乐观情形定价进去（base 保守锚不过门槛），而 capex ROI（O4）无一手量化 → **没有为不确定性留安全边际**。
- 与 NVDA 相反（NVDA 价格友好、owner earnings 干净）：META 是"好生意、价格偏贵、owner-earnings 锚未决"——价格是 binding constraint。

## 7. 与完整度的关系
- 完整度 ~62%（10-K 逐行 O1、capex ROI 定量 O4、proxy O3、RL 全年 O2 未取）→ verdict 上限封在 **STARTER**（60–80% 区间）。
- 但**价格进一步把实际 verdict 压到 STARTER 下沿 / WATCH 边缘**：base IRR +4% 不过门槛 → 即便完整度允许 STARTER，价格不支持现价建仓，只支持"WATCH + 等回撤到 ~$480"。
