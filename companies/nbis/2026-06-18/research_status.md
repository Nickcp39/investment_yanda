# NBIS Research Status

Last updated: 2026-06-18

Company: Nebius Group N.V.

Ticker: NBIS (Nasdaq; Amsterdam-domiciled, ex-Yandex N.V.)

Decision question:
1. （主）NBIS 建数据中心/电力是不是 bottleneck？真正的 binding constraint 是什么？
2. （决策）用户已持有（成本 ~$190–195，+~50% @ 2026-06-18）→ hold / trim / add？

Current stage: **✅ 10 层首跑完成（v1）。** 证据底座 + 10 层分析 + memo + monitor + HTML 全部写完。剩下的是少数一手核对项（见 Open Questions）和未来的季度监控。

Verdict: **HOLD 现有仓位 / WATCH 新资金（<~$150–180）** — 详见 `memo-v1.md`。主问题答案：**电力不是 bottleneck，NBIS 也不建电厂；约束是"建设-通电"链条。** 详见 `bottleneck_map.md`。

主产出：**[`nbis-full-rerun-v1.html`](nbis-full-rerun-v1.html)** = 先读这个（IC packet）。

---

## 运行记录

### Run 1 — 2026-06-18（证据采集）
5 个并行研究子代理，4 个完成、1 个（商业模式/客户）被用户中断。

| Workstream | 映射层 | 状态 | raw 产出 | tokens |
|---|---|---|---|---|
| 电力/buildout bottleneck（主） | L5/6 | ✅ | `raw/...L6_power_bottleneck.md` | 107,525 |
| 财务与会计 | L3/4 | ✅ | `raw/...L3-4_financials.md` | 84,888 |
| 管理层 + 风险 | L7/8 | ✅ | `raw/...L7-8_operator_inversion.md` | 82,739 |
| 估值 + 市场 | L9 | ✅ | `raw/...L9_valuation_market.md` | 62,847 |

### Run 2 — 2026-06-18（补缺 + 综合）
补跑被中断的商业模式 agent（后台），它又自发起了一个 contract-quality 交叉核对 agent，两个都完成。

| Workstream | 映射层 | 状态 | raw 产出 | tokens |
|---|---|---|---|---|
| 商业模式/客户/子公司 | L4 | ✅ | `raw/...L4_business_model_customers.md` | 100,796 |
| 合同质量 / RPO / backlog | L4 | ✅ | `raw/...L4_contract_quality_RPO.md` | 108,409 |

**研究 token 合计 ≈ 547k（6 个 agent）。续跑时读 6 份 raw，不要重跑。**

Run 2 带来的关键修正（已并入 facts/claim_ledger）：
- 真实合同指标是 **RPO $33.6B（Q1'26）**，不是媒体口径的"$46B backlog"（后者=合同上限之和，含 Meta 可选 $15B）。
- **take-or-pay 争议已解决**（C014/C015）：收入是 take-or-pay（保护 NBIS 抗客户少用）+ NBIS 有交付义务、违约则客户可终止/索赔（保护客户）。二者不矛盾 → 剩余风险是**交付延期（执行）**，不是客户随意走人。
- ARR +54% QoQ（非 +50%）；Toloka 那轮是 Bezos，**不是** NVIDIA。

---

## 10-Layer Checklist — 全部 done

| Layer | Artifact | Status |
|---|---|---|
| 1. Direction | `step0_plan.md` | ✅ done |
| 2. Evidence | `source_register.md`(21源), `claim_ledger.csv`(51条), `facts.md` | ✅ done |
| 3. Accounting | `financials/financial_quality.md`, `model/`(assumptions + scenario.csv) | ✅ done |
| 4. Business model | `business_model.md` | ✅ done |
| 5. Value chain | `value_chain_map.md` | ✅ done |
| 6. Moat/Bottleneck（主） | `bottleneck_map.md`, `moat_map.md` | ✅ done |
| 7. Operator | `operator_underwriting.md` | ✅ done |
| 8. Inversion | `inversion_map.md` | ✅ done |
| 9. Valuation | `valuation.md` | ✅ done |
| 10. Decision/Monitor | `memo-v1.md`, `monitor.md`, HTML | ✅ done（postmortem 待决策兑现后写） |

---

## Open Questions（一手核对项 — 不阻塞结论，但下次可收尾）

- [ ] **active power (MW) Q1'26** — 公司停披露（最后 ~170MW YE2025）。盯 Q2'26 6-K（~8月）。
- [ ] **客户集中度精确 %** — 20-F XBRL 有 CustomerA/D 成员但自动抓取没拿到 → 手动拉 `nbis-20251231x20f.htm` 收入集中度附注。
- [ ] **FY2026 capex** $20–25B（电话会）vs $31–35B（部分二手）→ Q2'26 6-K 确认。
- [ ] **俄罗斯剥离 indemnity / 或有负债** — 一手 20-F 文本 403 没读到。
- [ ] MS 的 −96.8% EBIT 口径（单一来源 futunn，未证实）。

## Pollution Checks

- [x] 无 KOL 当 fact（旧 `nbis.md` 仅作对照；核出老视频 3 处错）。
- [x] Fact/解读/假设分离（[PRIMARY]/[SECONDARY] 标注，claim_ledger status 分级）。
- [x] 关键数字有 source id（claim_ledger 51 条 + facts 全部带 claim_id）。
- [x] 每个 thesis 变量有 kill condition（`monitor.md` + `inversion_map.md`）。
- [x] memo 不超前于证据（结论 HOLD/WATCH，依赖 valuation+inversion+bottleneck）。

## 与旧版关系

- `../../nbis.md` / `nbis.html` = 旧检测器（单一视频源，结论 Watch）。保留对照。
- 本 `companies/nbis/` = 新 10-layer pipeline 首跑 v1。升级：Watch → **Hold**，不是因为变便宜，而是一手数据证明它是更好、更被验证的生意——只是不便宜。
