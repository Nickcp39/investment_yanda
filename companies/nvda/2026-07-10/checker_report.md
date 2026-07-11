# NVDA Checker Report — ai_robotics_2026-07-10 (refresh of mega7_2026-06-19 chain)

裁定: **FIX-NEEDED**
真实状态标签: **DECISION_DRAFT**（~65%，非 COMPLETE）— 标签诚实，未越级措辞。
verdict / size / ceiling: new-money **WATCH (0%)** / existing **HOLD** / initial 0% / ceiling **STARTER**（完整度 65% → 60-80% 档）。价格门更严封到 WATCH。 ← 是否被完整度正确封顶: **是**（WATCH ≤ STARTER ceiling；未越顶）。
数据新鲜度: **PASS**（`freshness_check.json` status==PASS, exit 0）← 非 BLOCK。
Gate 勾选: A✓ / B✗ / C✗ / D✓ / E✓ / F~（B、C 未过；F 轻微）

---

## 独立复核（verify, don't trust）

- **价格独立重抓**: WebFetch stockanalysis.com → **$210.96**（2026-07-10 收盘），与卡值分毫不差。freshness_check.json 的 Yahoo 再抓 $210.9600 + stockanalysis $210.96 两源一致（max pairwise delta 0.0%）。**价格 PASS，非 INC-001 复现。**
- **市值恒等式**: 24,391M × $210.96 = **$5,145,525M ≈ $5.146T** = 卡值，恒等式成立。stockanalysis 报 $5.11T（−0.7%，卡内已披露为稀释 vs 基本股本口径差）。
- **52 周带**: 161.61 ≤ 210.96 ≤ 236.54 ✓；距高 −10.8%、距低 +30.5%，算术自洽。旧 $142.03 低点已滚出窗口，交代清楚。
- **base IRR 复算**: OE $182B ×1.12^5 = $320.7B ×20x / 24,391M ≈ $263/股；(263/210.96)^0.2−1 ≈ +4.5%，卡值 +4.7%（含股息）—— 对得上。
- **旗标**: T6 两条 WARN（export-control 114d、guidance 51d 老于 45d 窗口）为**非阻断提示**，卡内如实记录并保守处理（Q2 归零 China DC），可接受。

## 批次 thesis 诚实度（本轮亮点，真实且有据）

- **robotics_revenue_pct**: **<1%（~0.3-0.5%，未披露）** —— 有据非手挥。机器人埋在 Automotive 平台（FY26 $2.35B ≈1.09% [S101, B1 回挂 8-K]，且多为汽车 DRIVE 非机器人）；Edge Computing 桶 [S102, A2 CFO commentary] 由游戏/PC 主导。DC=~92%。明确标 OPEN(O7)=未单独披露，不杜撰精确数。**诚实。**
- **demand real-vs-anticipation**: **ANTICIPATION（机器人本体）** —— 证据支撑。real-now 现金=汽车 DRIVE $2.35B（+39%），但那是**汽车不是机器人**且仅 ~1%；机器人本体在卖的是 Jetson/IGX 模块 + Isaac/GR00T/Cosmos 平台 + 具名生态（dated 产品事件，非 dated 营收）。给了证伪口径（真暴增 NVDA 会拆独立行）。**evidence-backed。**
- **CAPITAL_CYCLE（机器人段）**: 已套用且判得对 —— applicable=partial/largely N/A、stage=early/pre-inflection、supply_barrier=high 但未赚超额回报 → caution=NONE（非见顶，是未变现期权）。正确指出该 lens 的真实对象是 DC/GPU 段（partial/late?/CUDA-high）。**高质量。**
- **real_bottleneck**: **PARTIAL** —— 平台/开发者层护城河真实可证伪（CUDA+Isaac 转换成本），但当前尺度仍主要是概念/期权；已变现的真瓶颈是 AI 算力非机器人。判词有据。
- **option-vs-core split**: 已做 —— 现价 ~100% 市值=AI 算力（~28x fwd），机器人=近乎免费嵌入式看涨期权、~nil 现值、付 0 溢价拿 0 机器人 alpha。**结论钉死"NVDA 非机器人载体"，与批次框架自洽。**

## FIX 清单（每条指到文件）

1. **[Gate C] 决策版 dossier 缺 Stage 8 IC Panel，且唯一现存 panel 与当前 verdict 矛盾。** `companies/nvda/2026-07-10/`（及 `../2026-06-20/`）无 `ic_panel.md`；唯一的 `../2026-06-19/ic_panel.md` 建立在 **INC-001 错价 $145.48** 之上，五票一致 **STARTER**、明写"价格站在买方这边（forward 19x/yield 5.1%/base IRR 13%）"——**与本轮 WATCH（价格无 MOS）直接相反且未作废/标注 superseded**。修：在 07-10 用 $210.96 重跑五灵魂 panel，或在 dossier 内显式标注 06-19 ic_panel 因错价 void/superseded，避免读者取到已被推翻的 STARTER 结论。
2. **[Gate B] `source_register.md` 陈旧且不完整。** 文件头仍 `as_of 2026-06-20`，且**不含本轮 card/claim_ledger 引用的 source_id**：机器人 S101/S102/S103、新价 S106/S108。claim_ledger 用 S106/S108，source_register 仍称 S006/S008——**source_id 失配，S101-S103/S106/S108 无法回挂 source_register**。修：把 5 个新 source_id 登入 source_register（名/日期/tier/link），或统一新旧 ID。
3. **[Gate F 轻微] 本轮无独立 `audit.md` / `research_status.md` 产物。** README.md 代行状态记述且反映当前态，可接受；建议补一份轻量 audit 记数字勾稽 + 明示 ic_panel 未重跑这一已知缺口。

## 伪造引语 / 失配数字

- **伪造引语: 无。** 当前 07-10 dossier 不含任何投资人引语；06-19 ic_panel 的立场引用均显式标为释义/一般性立场（"严禁杜撰具体名言"纪律遵守），无引号内逐字伪造。
- **失配数字: 无（当前文件内）。** $210.96 / $5.145T / base IRR +4.7% / forward 28x / −10.8% off ATH 在 decision_card.json/.md、facts、valuation、refresh_note、README、freshness 六处前后一致，并经独立重抓 + 恒等式复算通过。唯一"矛盾"是 06-19 ic_panel 的 **STARTER 结论**（基于错价）未被作废——属陈旧结论治理问题（见 FIX #1），非当前数字失配。

## 一句话

本轮 NVDA 是一次**诚实、机械新鲜度过关、数字全对得上**的 light refresh：WATCH（新钱 0%）verdict 正确、价格独立可核、robotics thesis 是全批最扎实的一段（占比有据、需求判 anticipation、capital-cycle 与 option-split 都做到位）——**决策本身可信**；FIX-NEEDED 仅因两处**可追溯性/一致性缺口**（缺当前 IC panel 且唯一现存 panel 停留在被推翻的 STARTER 错价结论、source_register 未登新源），补齐即 CLEAN。
