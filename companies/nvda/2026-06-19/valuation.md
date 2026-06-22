# NVDA Valuation (M6) — as_of 2026-06-19

价格 [S006]: **$145.48**（2026-06-18 收盘，≤ as_of）· 稀释股 24,391M · 市值 **~$3.55T**。模型见 `model/scenario_model.csv`。

## 1. 倍数起点
- Trailing GAAP EPS (FY26) $4.90 → **P/E ~29.7x**（GAAP 含股权证券收益，偏高）。
- Forward run-rate non-GAAP EPS ~$7.48（Q1 $1.87 ×4，且环比仍升）→ **forward P/E ~19.4x**。
- 起始 owner-earnings yield（经营 owner earnings 年化 ~$182B / $3.55T 市值）≈ **5.1%**（远优于 GOOGL 的 1.45%）。
- 现价距 52 周高 −38%、贴 52 周低 $142.03。

## 2. owner earnings 锚
- 经营性 owner earnings ≈ non-GAAP 净利 ≈ FCF（capex 极轻、R&D 费用化）→ run-rate **~$180–185B/年**（剔除 GAAP 净利中的股权证券收益）。
- 与 GOOGL 关键差异: **不存在 capex 黑洞**，owner earnings 与 FCF 一致，估值不确定性**不在 owner earnings 桥**，而在 **run-rate 的可持续性**（增速/份额/毛利率能否守）。

## 3. 三情景 IRR（5 年，hurdle 8%）
| 情景 | OE 起点 | 5y CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−11%** |
| Base | $182B | +12% | 20x | ~$266 | **+13%** |
| Bull | $185B | +22% | 24x | ~$495 | **+28%** |

- **base IRR +13% > 8% 门槛** → 现价**留有正安全边际**（与 GOOGL bull 都只有 +5.2% 截然不同）。
- 赔率: 上行 +28% / 基准 +13% / 下行 −11%（可存活，非永久减值）→ **不对称偏向上行**，这是结构化建仓的依据。

## 4. 价格带（buy-below / size 锚）
| 档位 | 含义 | 价格 | vs $145.48 |
|---|---|---:|---:|
| Starter 主锚 | 现价即 base 10%+ IRR | **~$130–150（现价区）** | 现价 |
| Add zone | de-rate 或确认后加 | **~$110–130**（向 52 周低破位的回撤）| −10% 至 −24% |
| No-chase / trim 警戒 | 隐含 IRR <8% | **> ~$200** | +37% |
| 下行保护参考 | bear 兑现 | ~$80（−45%）| 资产负债表存活 |

## 5. binding constraint
- **不是估值 air-pocket（2023 案的卡点），而是"需求耐久性 vs pull-forward + 份额 vs custom silicon"**。估值在 $145 是友好的（forward 19x、base IRR 13%、yield 5.1%）；真正控制 size 的是**run-rate 可持续性这一前瞻不确定性**——按修好的规则，这是 size 控制项 + kill 监控项，不是 veto。

## 6. 与完整度的关系
- 完整度 ~65%（10-K 逐行、custom-silicon 定量份额、proxy 未取）→ **verdict 上限封在 STARTER**（60–80% 区间）。即便估值友好，证据完整度不足以支撑 CORE。
