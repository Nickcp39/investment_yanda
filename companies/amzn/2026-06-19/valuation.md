# AMZN Valuation (M6) — as_of 2026-06-19

价格 [S004]: **$244.39**（2026-06-18 收盘，≤ as_of）· 稀释股 10,874M · 市值 **~$2.66T**。模型见 `model/scenario_model.csv`。

## 1. 倍数起点（为什么不能用常规倍数）
- Trailing FY25 GAAP EPS $7.17 → **P/E ~34x**——但 GAAP 净利**含股权投资（Anthropic 等）公允价值收益**，**低估了真实经营倍数**。
- **P/FCF 无意义**: TTM FCF 仅 $1.2B（capex 已超过 OCF）→ P/FCF >2000x，无参考价值。
- 现价距 52 周高 $274.99 仅 **−11%**，较 52 周低 $198.79 高 **+23%** → **处区间中上部，不是便宜的起点**（与 NVDA forward 19x/贴 52 周低、GOOGL 贴低相反——AMZN 价格情绪偏多）。
- **必须用正常化 owner earnings / NOPAT 估值**，不能用现成倍数。

## 2. owner earnings 锚（本案核心难点）
- 当前 FCF（$1.2B TTM）**不是** owner earnings——它被 ~$200B/年 AI capex（远超折旧）暂时压制。
- 正常化路径有两个口径，**都指向同一结论（价格贵）**:
  - **NOPAT 口径（给 capex 信用，假设增长 capex 创造价值、FCF 终将释放）**: FY25 营业利润 $80B × (1−16% 税) ≈ **NOPAT ~$67B**。这是**对 AMZN 最有利**的看法。
  - **保守正常化 owner earnings**: NOPAT 减维护性 capex（O4 缺一手拆分），保守带 **$45–65B**。
- 起始收益率: NOPAT $67B / $2.66T = **2.5%**；保守 OE $55B → **2.1%**。**远低于 NVDA 的 5.1%、甚至低于多数蓝筹**。

## 3. 三情景 IRR（5 年，hurdle 8%）— headline 用 NOPAT 口径（给 capex 信用）
| 情景 | NOPAT 起点 | 5y CAGR | 退出倍数 | y5 NOPAT | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|---:|
| Bear | $60B | +6% | 16x | $80B | ~$118 | **−13.5%** |
| Base | $67B | +13% | 20x | $123B | ~$227 | **−1.5%** |
| Bull | $70B | +18% | 24x | $160B | ~$353 | **+7.7%** |

- **关键发现**: **即便在给足 capex 信用的 NOPAT 口径下，base 5y IRR ≈ −1.5%、bull 仅 +7.7%（仍 <8% 门槛）**。保守 owner earnings 口径更低（bull +5.0%、base −6.0%）。
- 原因: $2.66T 市值 + 起始收益率仅 2.1–2.5% → 价格已 price-in 多年高速复利 + 退出仍维持高倍数。**这与 NVDA（base +13%、价格友好）截然相反，与 GOOGL（base 负、价格封顶）同构。**
- 赔率: 上行有限（bull 才勉强够门槛）、下行实在（base 负、bear −13.5%）→ **赔率不对称偏下**。

## 4. 价格带（buy-below / size 锚）
| 档位 | 含义 | 价格 | vs $244.39 |
|---|---|---:|---:|
| No-chase / 现价 | base IRR 负、bull 才够门槛 | **$244（现价）= 不追** | 现价 |
| Watch 观察 | 接近 8% base IRR 需要的折扣 | **~$180–195** | −20% 至 −26% |
| Starter 候选 | base IRR 回到 >8% 门槛 | **≲ $175**（约 52 周低附近） | −28% |
| 下行参考 | bear 兑现 | ~$118（−52%）| 资产负债表存活 |

- **buy-below ≈ $175–180**: 要在现价上打 ~25–28% 折扣，base IRR 才回到 8% 门槛。现价**无安全边际**。

## 5. binding constraint
- **价格（无 MOS）+ owner earnings 在重投资期无法闭合（$200B capex 的 ROI）**，**不是生意质量**。生意是好的（AWS 重新加速、零售利润率创纪录），但 ①$2.66T/起始收益率 2.1–2.5% 下，连给足 capex 信用的 base IRR 都为负；②正常化 owner earnings 取决于 $200B capex 的 ROIC（O4 缺一手）。**两者叠加 → 价格是卡点（与 GOOGL 同构，与 NVDA 相反）**。

## 6. 与完整度的关系
- 完整度 ~62%（10-K 逐行、capex 维护/增长拆分 + ROIC、proxy、Anthropic 会计未取）→ verdict 上限本可到 STARTER（60–80% 区间）；**但价格无 MOS 把实际 verdict 压到 WATCH——价格封顶先于完整度封顶生效**（同 GOOGL）。
