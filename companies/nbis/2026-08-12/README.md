# NBIS — 2026-08-12（Q2'26 财报事件重跑）

**触发**：2026-08-12 盘前发布 Q2 2026 业绩，股价大涨。
这是 `../2026-06-18/monitor.md` 事件日历上写死的 `Q2 2026 6-K | ~Aug 2026` 检查点。

## 先读

**`decision_card.md`** → 裁决与三条最重要的发现
**`monitor.md`** → 逐项打分 + 🔴 计数 + 新增监控变量

## 一句话结论

**0 个 🔴 → 不 trim；价格 ~$220 仍高于 buy-below $150–180 → 不买。**
**三个条款一个都没触发 ⇒ 不动。**

## 本次三条最重要的发现

1. **⭐ 单 MW 价格 $20M → $40–50M** —— 商品化从"预测"变成"需要解释的反例"。
   **但涨价不是 capital cycle 的证伪，是它的第一步**（见 decision_card）。
2. **⚠️ active MW 连续第三季未披露** —— YE2025 ~170MW 之后，Q1、Q2 只给合同数
   和年底指引。**这是模式不是疏漏。**
3. **🔴 融资形态已变，旧 kill criteria 没覆盖** —— 实际路径是
   "预付款 → 资产担保债 → 可转债 → ATM"，非流动负债一季 $4.10B→$8.50B。
   **K-C 需重写。**

## 本次新增到卡上的字段

- **Trim / no-chase zone**（此前缺失，导致 S2 条款无法触发）：建议 **≥$250**，
  推导自本卡 base $330–400 ÷ hurdle 12–15% ÷ 2.48yr。**待持有人拍板生效。**
- **K-G 杠杆分支**（新 kill criterion）
- monitor 新增三个变量：杠杆与融资形态、**供给响应**、合同→active 转化率

## ⚠️ 本次的局限（必读）

**一手源全部被本运行环境的出口代理拦截**（SEC / nebius.com / businesswire）。
所有 Q2 数字为二手聚合源，`claim_ledger.csv` 中标 `unverified_secondary`。
**两处数值冲突（递延收入、净负债口径）未解决。**

→ **完整度 ~50%，低于 07-10 版的 ~70%。裁决按规则封顶在 WATCH。**
→ 解除路径见 `source_register.md`。

## 未重建的模块

本次是**事件重跑**，不是全模块重建。以下沿用 `../2026-06-18/`：
`business_model.md` / `value_chain_map.md` / `bottleneck_map.md` / `moat_map.md` /
`operator_underwriting.md` / `inversion_map.md` / `ic_panel.md` / `memo-v1.md`

**若要全模块重建，需先解决一手源可达性问题。**
