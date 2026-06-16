# GOOGL Facts Foundation

Last updated: 2026-06-16

Status: `evidence_layer_built`. ~50 claims promoted to EVIDENCE, each verified against a primary SEC filing (A1) with a verbatim excerpt in `raw/` and a stable `source_id` in `source_register.md` + `claim_ledger.csv`. 这一步是 OS 流水线第 4-6 步(原始证据→Claim Ledger→Facts)对 GOOGL 的实跑产物。
**更新 2026-06-16（全流程跑通后）**：证据层 + 全部 8 分析模块 + 审计 + IC Panel + memo 均已完成。**Verdict = WATCH**，但原因已从"缺模块"变为"当前价 ~$370 无安全边际"（硬规则封顶已解除，completeness ~75%）。详见 `memo-v1.md` / `audit.md` / `ic_panel.md`。

> 单位：USD millions，除非标注。FY = 财年(截至 12/31)。一手来源全部为 A1（SEC EDGAR）。

---

## EVIDENCE（A1 一手，已验证）

### 1. 营收与盈利
- FY2025 总营收 **$402,836M**（+15% YoY；FY2024 $350,018M，FY2023 $307,394M）。[GOOG.A1.2025K.001]
- FY2025 营业利润 **$129,039M**，营业利润率 **32.0%**（derived）。[GOOG.A1.2025K.005 / .006]
- FY2025 净利 **$132,170M**，摊薄 EPS **$10.81**。[GOOG.A1.2025K.007 / .008]
- Q1 2026 总营收 **$109,896M**，**+22% YoY**（恒定汇率 +19%），第 11 个连续两位数增长季。[GOOG.A1.2026Q1.001]
- Q1 2026 营业利润 **$39,696M**（+30% YoY），营业利润率 **36.1%**（+2pp）。[GOOG.A1.2026Q1.018 / .019]

### 2. 分部（Services / Cloud / Other Bets）
- FY2025 Google Services 营收 **$342,721M**，营业利润 **$139,404M**。[GOOG.A1.2025K.009 / .010]
- FY2025 Google Cloud 营收 **$58,705M**（+36% YoY），营业利润 **$13,910M**（FY2024 $6,112M、FY2023 $1,716M——两年内从微利到大幅盈利）。[GOOG.A1.2025K.011 / .012]
- FY2025 Other Bets 营业亏损 **$(7,515)M**（含 Q4 Waymo $2.1B 估值补偿费用）。[GOOG.A1.2025K.014]
- Q1 2026 分部营收：Google Search & other **$60,399M**（+19%）、YouTube ads **$9,883M**（+11%）、**Google Network $6,971M（YoY 下滑）**、Google Services 合计 **$89,637M**（+16%）。[GOOG.A1.2026Q1.004/.005/.006/.009]
- Q1 2026 Google Cloud 营收 **$20,028M**（+63% YoY），营业利润 **$6,598M**，**营业利润率 32.9%**（derived；Q1'25 约 17.8%）；Cloud backlog "over $460B"。[GOOG.A1.2026Q1.010/.014/.015]

### 3. 现金流、capex 与 owner-earnings 压力点（核心矛盾）
- FY2025 经营现金流 **$164,713M**；capex（购置 P&E）**$91,447M**（**YoY +74%**）；derived FCF **$73,266M**。[GOOG.A1.2025K.015/.016/.017]
- Q1 2026 经营现金流 **$45,790M**；capex **$35,674M**（**YoY ~2.07x**）；stated FCF **$10,116M**（TTM FCF $64,429M——**FCF 正被 capex 压缩**）。[GOOG.A1.2026Q1.023/.024/.025]
- **2026 全年 capex 指引 $180–190B；且 2027 将"显著增加"**（来自 424B5 融资文件，非季报）。[GOOGL-424B5-2026-06.009]
- FY2025 总 SBC（Note 13）**$27,100M**（现金流加回口径 $24,953M）。[GOOG.A1.2025K.023]

### 4. 资产负债表与资本结构
- FY2025 现金+有价证券 **$126,843M**（另有 non-marketable $68,687M）。[GOOG.A1.2025K.020]
- FY2025 长期债务 **$46,547M**（FY2024 仅 $10,883M；FY2025 净发债约 $64.6B）。[GOOG.A1.2025K.021]
- FY2025 末总股本 **12,088M 股**（A/B/C 三类，较 12,211M 因回购下降）。[GOOG.A1.2025K.022]

### 5. 资本配置
- FY2025 回购 **$45,709M**（FY2024 $62,222M）；**Q1 2026 回购 $0**（Q1'25 $15,068M）——**回购暂停**，现金转向 capex + $31.4B 发债。[GOOG.A1.2025K.018 / GOOG.A1.2026Q1.027]
- FY2025 股息 **$10,049M**（首年 FY2024 $7,363M）；Q1 2026 季度股息 **$0.22/股**（+5%）。[GOOG.A1.2025K.019 / GOOG.A1.2026Q1.030]
- 回购授权 2025-04 新增 $70B，年末剩余 **$69.5B**，无到期日。[GOOG.A1.2025K.025]

### 6. 2026 融资与 Berkshire 私募（GOOGL 特殊情况）
- 2026-06 宣布 **$80B 股权融资**（$30B 承销公开 + $40B ATM + $10B Berkshire 私募），明确用于 **AI 基础设施与算力 capex**。[GOOGL-FWP-2026-06.001]
- **Berkshire 私募 $10B**：Class A **14,212,035 股 @~$351.81** + Class C **14,359,656 股 @~$348.20**；文件称"adds to the position it has built since Q3 2025"。[GOOGL-424B5-2026-06.001/.002/.004]

### 7. 机构持仓（13F，季末快照）
- Berkshire Q1 2026 13F 持 Alphabet **57,835,013 股 / $16.63B**（Class A 54.25M + Class C 3.585M）。[BRK-13F-2026Q1.005/.001/.003]
- H&H Q1 2026 持 Class C **3,706,000 股 / $1.063B**；Q4 2025 为 **1,855,400 股**——**季度环比 +99.74%（~翻倍），坐实"翻倍到约 3.7M 股"**。[HH-13F-2026Q1.001 / HH-13F-2025Q4.001 / HH-13F-DELTA.001]

### 8. 治理（proxy）
- 三层股权：**Class B = 10 票/股，Class A = 1 票，Class C(GOOG) = 0 票**。[GOOG.A1.PROXY2026.001]
- **Page 27.4% + Brin 25.3% = 合计 52.7% 投票权**（持有不到 11% 的投票股）；全体高管+董事 14 人合计 54.3%。[GOOG.A1.PROXY2026.004 / .009]
- 董事会 10 人、7 名独立；**独立董事长 John L. Hennessy（与 CEO 分离，2018-01 起）**。[GOOG.A1.PROXY2026.005 / .006]
- CEO Pichai 2025 总薪酬 **$10,906,079**（其中 $8.8M 为个人安保；**2025 年 0 股票授予**——多年期授予使该数字低估常态经济薪酬）。[GOOG.A1.PROXY2026.007]
- 关联交易：向创始人关联实体的机库租赁（Moffett/LTA ~$8.43M + San Jose/BCH ~$1.58M），审计委员会认定按公平交易。[GOOG.A1.PROXY2026.010]

### 9. 法律与监管
- EC adtech "self-preferencing" 罚款 €3.0B，Q3 2025 计提 **$3.5B**（已上诉），驱动 G&A 同比增约 $6.2B；年末短期计提的罚款/和解 $15.6B。[GOOG.A1.2025K.026]
- DOJ adtech 案 2025-04 部分败诉，结构性救济提案"could have a material adverse effect"，最终判决待定。[GOOG.A1.2025K.026 notes]

---

## INTERPRETATION（二手解读，需复核回 EVIDENCE）
- 暂无。本轮未拉 sell-side 一致预期 / 行业研报（B 级）——属 OPEN QUESTIONS，下游 Marks/估值锚需要时补。

## SENTIMENT（D 级，仅线索，不可作 thesis）
- 美股投资网 / TradesMax YouTube 对 GOOGL 的 AI/搜索叙事 = **D1/C2 频道线索**，只能作选题入口与 contrarian 信号，**永不进 EVIDENCE**。[TRADESMAX.C2.note]

---

## Contradictions / 口径警示（不裁决，下游处理）
1. **Q1 2026 净利 $62.578B（+81%）被一次性收益严重抬高**：其中 $36.9B 是非经营的**未实现股权证券收益**（+$2.35 EPS）。→ **营业利润 +30% 才是干净的增长读数**；KOL 易误读"净利暴增 81%"。[GOOG.A1.2026Q1.020/.022]
2. **SBC 两个口径**：Note 13 总额 $27.1B vs 现金流加回 $24,953M（差额为现金结算/Waymo 类补偿）——owner earnings 桥要选对口径。[GOOG.A1.2025K.023]
3. **FCF 非 10-K 列报项**（FY2025 $73.266B 为 derived；Q1'26 $10.116B 是季报里 non-GAAP 列示）。
4. **13F = 季末机构快照 ≠ 个人实时交易**；Berkshire 13F ≠ Buffett 个人决策；H&H ≠ 段永平个人操作；H&H 市值变化混合了加仓与价格下跌，不可当净买入金额。[各 13F notes]
5. **Berkshire $10B 是"私募融资"的一部分**（定价 $351.81/$348.20），而非纯二级市场增持——"Berkshire 买入=安全边际背书"的叙事需重估为"参与了一轮 AI capex 融资"。

---

## OPEN QUESTIONS（触发回流补料）
- [ ] Google Search & other **FY2025 年度细分**未由 10-K 验证（旧 memo seed $224.532B 待核 10-K advertising disaggregation 表）。[GOOG.SEED.SearchFY2025]
- [ ] **10 年财务序列**：当前只有 FY2023–2025 + Q1'26；owner earnings 桥与长周期 ROIC 需补（Block 04）。
- [ ] **capex 维护性 vs 成长性拆分**：owner earnings 桥的关键前置，10-K/季报未直接披露。
- [ ] **sell-side 一致预期 / 估值锚**未拉（B 级）。
- [ ] **Cloud 32.9% 利润率可持续性**：需多季趋势 + 是否受利用率/会计一次性影响。
- [ ] DOJ adtech 结构性救济最终判决（尾部风险量化）。

---

## Minimum Coverage Check（更新 2026-06-16，全流程跑通后）

| 模块 / 门槛 | 状态 | 备注 |
|---|---|---|
| 事实线（raw→ledger→facts） | ✅ 强 | ~50 条 verified A1 |
| 10 年财务序列 | 🟡 部分 | 仅 3 年 + TTM（gap，但不阻塞 verdict） |
| Business model | ✅ | business_model.md |
| Value chain | ✅ | value_chain_map.md |
| Moat | ✅ | moat_map.md（整体 Strong，增量护城河待验） |
| Bottleneck | ✅ | bottleneck_map.md |
| Operator underwriting | ✅ | operator_underwriting.md（28/40 中性偏正） |
| Inversion | ✅ | inversion_map.md（9 失败路径 + 9 kill criteria） |
| **Valuation / owner earnings / 安全边际** | ✅ | valuation.md（$370 无安全边际，buy below ~$113） |
| 5 灵魂开口门槛 | ✅ | IC Panel 五票 WATCH + 段永平主审 |

**结论**：信息完整度约 **75%**；"缺模块"硬规则封顶已解除。**Verdict = WATCH**，原因是价格端 valuation 无安全边际（$370 even-bull IRR +5.2%），非信息不足。距 STARTER 只差价格回调（~$113）+ 两个证据补强（10 年序列、capex 维护/成长拆分）。见 `memo-v1.md`。
