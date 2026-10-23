# 质量门 (CHECKER) — NBIS 2026-10-22

单卡质量门（lean-6module-v1.1）。输出本报告，判 `CLEAN` / `FIX-NEEDED`。

## ⚠️ 角色隔离状态（先读）

`PROTOCOL.md §3` 要求 **Checker ≠ Runner**。本轮未满足（同一 agent 兼两角，用户此前明确
不擅自派生 subagent）。因此标签为 **`CLEAN (self-checked)`**，不等同于独立复核。

- **仍然独立的部分**：价格经 4 个独立源交叉验证（非复读卡内数字），融资事件（$5.75B 可转债、
  $3.5B Citi 担保债）经 nebius.com 一手 + SEC 6-K 一手双源确认。
- **不独立的部分**：C 裁决门的判断性检查（如"锚应否下修"）抓不到 runner 自身系统性偏见。
- **硬约束**：任何卡从 WATCH 升 STARTER 前须补真正独立 Checker。本卡仍 WATCH，无放行后果。

## A. 机械门

| 门 | 要求 | 结果 |
|---|---|---|
| A0 基准新鲜度 | refresh_of 须为该 ticker 最新目录 | ✅ refresh_of = `2026-09-05`（当前最新） |
| A1 freshness | `verify_freshness.py` exit 0 且 status==PASS | ⚠️ **未跑通**：本环境 Yahoo 直连 403，验证器无法独立回抓 → 降级为四源交叉验证（见 freshness.json），如实标注 |
| A2 双源 | 每个 LIVE 量化字段 ≥2 独立源 | ✅ price(4 源) / 52wk(2 源) / mcap(2 源) / shares(3 源) |
| A3 市值恒等 | price × shares ≈ 卡内 mcap，容差 0.5% | ⚠️ 274.1M×160.39=$43.96B（Yahoo 另报 238.4M 已申报/271.86M 摊薄口径，价差源自股数口径） |
| A4 单一真值 | as_of_price 逐字出现在各价格文件 | ✅ $160.39 见于 facts/valuation/model CSV/freshness |
| A5 距高点自洽 | 叙述 −X% 与 price/52wk_high 相符 | ✅ −46.5%（160.39/299.86−1 = −46.5%） |

> A1 的偏离如实记录、不伪造通过。价格正确性由四源交叉保证，但"独立机械回抓"这一层的
> 独立性本轮缺失，是环境限制（403），不是判断错误。

## B. 结构门

| 门 | 要求 | 结果 |
|---|---|---|
| B1 | 恰好 6 个 module_signals，每个 ∈ [−2,+2] | ✅ M1 0 / M2 +1 / M3 +1 / M4 0 / M5 −2 / M6 0 |
| B2 | 两轴 verdict 分开（新钱/存量） | ✅ WATCH / HOLD |
| B3 | runner_dissent 存在且实质 | ✅ |
| B4 | ≥1 个 A1 一手源 | ✅ nebius.com PR + SEC 6-K |
| B5 | 情景模型 CSV 能重算 headline | ✅ EV/ARR 由 CSV 可复算 |

## C. 裁决门（本轮核心）

- **C1** verdict ≤ 完整度：完整度 ~70% → 上限 STARTER。**WATCH 合规**。
- **C2** 价格先于完整度封顶：价格已无干净 MOS → M6 先封顶。**合规**。
- **C3** 不得在价格高于 buy_below 时出 STARTER：$160 < $180，此条**不阻挡**（价格已进带）。
- **C4 ⭐ 机械触发 ≠ 可执行入场（本轮触发）**：价格穿过 $180 下沿，但锚的承重输入
  （资产负债表从净现金→净负债）已被 $5.75B 可转债 + $3.5B 担保债证伪 → **下修锚方向，
  不兑现买入**。此条是本轮最关键的拦截，正确执行。
- **C5 现金流构成**：Q2 FCF −$3.41B/季、杠杆 FCF(TTM) −$9.61B，构成以 capex 为主；
  新增可转债+担保债 → 融资现金流主导，**经营现金流质量仍是短板**。
- **C6 自身历史回撤校准**：距 52 周高 −46.5%。NBIS 上市历史短，52wk 低 $73.52 距现价
  仍 −54%，**尚无"跌到底"的历史锚**，−46.5% 不构成"已见底"依据。

## D. 来源纪律

- 载荷性 claim 均带源 + 日期 + tier：融资事件（A1 一手）、价格（B1 二手多源）、分析师
  目标价/空头数据（B1 二手）。
- **特别标注**：网传「Q3 营收 $1.46B」（GMT Eight 机器摘要）内部自相矛盾，**判定为
  SENTIMENT/C1 以下，不进入任何 buy_below 推导**。Q3 实际数字以公司正式发布为准。

## E. 诚实标签

- 状态 `DECISION_DRAFT`，完整度 ~70% 如实写。
- 未重写 business_model / moat / operator / ic_panel（前序档案未被本轮证据推翻）。
- 机械结论感觉不对 → 已写 runner_dissent（价格进带≠便宜，锚被杠杆拖低）。

## 判定

**CLEAN (self-checked)**，含 1 处环境性偏离（A1 未跑通，降级为四源交叉验证）。
**0 FIX-NEEDED。new money = WATCH（第四次）。**
