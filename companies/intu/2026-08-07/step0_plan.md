# INTU Step 0 Plan — as_of 2026-08-06 / run_date 2026-08-07

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **status**: DECISION_DRAFT

## 冻结的 Scope

| 字段 | 值 |
|---|---|
| ticker / 交易所 | INTU / Nasdaq（单一普通股，无双层结构） |
| CIK | 0000896878 |
| 财年 | **7 月 31 日结束**（FY2026 = 2025-08-01 → 2026-07-31）。全文严格区分 FY 与 CY |
| as_of（数据冻结） | **2026-08-06**（≤ today 的最后一个**结算收盘**） |
| run_date | 2026-08-07（当日盘中 ~$328.4 **不作为冻结边界**，与 GOOGL 2026-07-24 同纪律） |
| 决策目的 | 新钱是否建仓 / 已有仓位如何处置；10 年持有视角 |
| hurdle | **8%** |
| 时间跨度 | 10 年 IRR 为主，5 年为交叉验证 |

## 为什么选这家（选题理由）

INTU 是**当前美股软件里市值最大、速度最快、时间最近的一次 AI 去估值**：
高点 2025-07-30（$807.39 收盘 / $798.42 复权），到 2026-08-06 收盘 $321.91，
**−60.1%（复权 −59.7%）**，比 Adobe / Salesforce / ServiceNow 同窗口都惨。
一个此前被当作"堡垒型复利机器"的生意在 12 个月内蒸发 6 成，必须给出机制性解释。

## 本轮必须回答的五个问题（论文脊柱）

- **(a) 拆解 −60%**：多少是倍数压缩、多少是盈利/FCF 基数变化？把回撤钉到**有日期的事件**上。
- **(b) 替代机制，分部逐个判**：TurboTax / QuickBooks(GBS) / Credit Karma / Mailchimp
  四条腿的护城河来源不同，**禁止给一个混合结论**。
- **(c) 政策风险与 AI 叙事分开**：IRS Direct File / Free File 独立时间线与现状。
- **(d) 经营指标是否已经在恶化**？如果指标健康而股价 −60%，就是"倍数碎了、生意没碎"，
  必须用数字说；反之亦然。
- **(e) Intuit 自己的 AI**：在收钱（ARPC/提价）还是在花钱防守？未披露本身就是一个发现。

## 需要 ≥2 源验证的锚定事实（结果见 facts.md）

- 价格 $321.91（2026-08-06 结算收盘）— Yahoo chart API + stockanalysis.com history。[已验证，delta 0.00%]
- 股数 273,537 千股 — SEC 10-Q 封面（2026-05-14）+ stockanalysis。[已验证，delta 0.00%]
- FY2026 指引三次版本（2025-08-21 初始 / 2026-02-26 重申 / 2026-05-20 上调）— SEC 8-K 原文。[已验证]
- FY2026 Q3 分部收入与 TurboTax 单量指标 — SEC 8-K + 10-Q。[已验证]
- 17% 裁员与 $300–340M 重组费用 — SEC 8-K 原文。[已验证]

## 载重重算项（load-bearing recompute）

1. **回撤归因**：峰值 vs 现在的 P/E、P/FCF、EV/Sales，以及 TTM 收入/EPS/FCF 的实际变化 → 乘法分解。
2. **owner earnings 桥**：GAAP 净利 vs non-GAAP 净利 vs FCF vs (FCF − SBC)，
   并剔除 FY2026 递延所得税一次性释放（DTA $1,222M → $113M）对 OCF 的虚增。
3. **分部利润池**：用分部 operating income 而非收入给四条腿定价。
4. **三情景 10y IRR @ $321.91** + buy_below 阶梯。

## 产出

`companies/intu/2026-08-07/` 标准件 + `freshness.json` / `freshness_check.json`（机械门必须 PASS）
+ `ic_panel.md` / `claim_ledger.csv` / `decision_card.json` / `completion_checker.md`。

## 已知的硬边界（决定 completeness 上限）

- **FY2026 全年业绩尚未公布**：Q4/FY2026 财报定于 **2026-08-25**，Investor Day **2026-09-17**，
  均在 as_of 之后 → 全年实际单量、e-file 份额、FY2027 指引全部缺席。
- Mailchimp 从不单独披露收入；QBO 订阅户绝对数从不披露（只披露 online ecosystem paying customers 增速与 ARPC，且只在 10-K 年披露）。
- 管理层承诺"Q4 财报中提供 TurboTax 联邦单量对比"——该数据本轮拿不到。
