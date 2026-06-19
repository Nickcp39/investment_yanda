# Company Research Template

> ⚠️ **LEGACY(10 层老模板)。** Canonical 现在是 `backtests/framework_validation/` 的**精简 6 模块 pipeline**
> (产出 `decision_card.json`,已 10 案盲测验证)。本模板的 10 层已被 6 模块吸收(映射见
> `backtests/framework_validation/PIPELINE.md` 末尾),保留作参考 / 深度公司研究用。
> **分析新公司请从 `backtests/framework_validation/USER_MANUAL.md` 起,不要从这里起。**

用途: 这是单家公司买方投研的标准目录模板。复制本目录到 `companies/<ticker>/` 后，只填事实、假设和结论，不改结构。

核心原则:

0. 开题前先过 `../../frameworks/one_page_quality_company_checklist.md`: 一分钟讲不清为什么是好生意，就先补理解，不直接估值。
1. `raw/` 只放原始材料和摘录，不写结论。
2. `claim_ledger.csv` 记录每一条事实主张、来源、状态和置信度。
3. `facts.md` 只写已经审计过的事实，不写观点。
4. 分析文件只能引用 `facts.md`、`claim_ledger.csv` 或明确标注的假设。
5. `memo-v1.md` 是最后产物，不是研究起点。

目录合同:

```text
companies/<ticker>/
  README.md
  research_status.md
  step0_plan.md
  source_register.md
  raw/
  claim_ledger.csv
  facts.md
  financials/
  model/
  business_model.md
  value_chain_map.md
  moat_map.md
  bottleneck_map.md
  operator_underwriting.md
  inversion_map.md
  valuation.md
  memo-v1.md
  monitor.md
  postmortem.md
```

10 层能力对应文件:

| Layer | File |
|---|---|
| 1. Direction Selection | `../../research_queue.md`, `step0_plan.md` |
| 2. Business Thesis / Quality Gate | `../../frameworks/one_page_quality_company_checklist.md`, `business_model.md` 开头 |
| 3. Evidence Engineering | `source_register.md`, `raw/`, `claim_ledger.csv`, `facts.md` |
| 4. Accounting Trend Validation | `financials/financial_quality.md`, `model/` |
| 5. Industry / Value Chain | `value_chain_map.md` |
| 6. Moat / Bottleneck | `moat_map.md`, `bottleneck_map.md` |
| 7. Operator / Capital Allocation | `operator_underwriting.md` |
| 8. Inversion / Risk | `inversion_map.md` |
| 9. Valuation / MOS | `valuation.md` |
| 10. Decision / Portfolio Rules / Monitoring | `memo-v1.md`, `monitor.md`, `postmortem.md` |
