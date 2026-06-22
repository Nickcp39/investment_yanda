# GOOGL 估值 / 安全边际 (H8)

Last updated: 2026-06-16
模块负责: 估值 + 安全边际 (H8)
数据来源: 全部数字来自 `facts.md`（挂 `source_id`）与本目录 `model/owner_earnings_bridge.csv`、`model/financial_history.csv`。所有非 filed 数字标 `ASSUMPTION`，假设全程可见。

> 单位: USD，金额 billions（B）除非标注。计算脚本口径见文末"方法学"。

---

## 0. 一句话结论（module verdict）

**当前价 ~$370 没有安全边际——这是"用乐观假设也很难赚到 8%"的价格，不是"打折买好公司"的价格。** 即使最乐观情景（owner earnings 起点 $80B、十年 OE CAGR 14%/10%、退出 26x）10 年 IRR 也只有 **+5.2%**，低于 8–10% 的最低门槛；基准情景 **-3.0%**，保守情景 **-13.1%**。当前市值 ≈ **70x TTM 自由现金流**、≈ **69x 基准 owner earnings**。要在 $370 赚到 10%，需要 owner earnings 十年复合增长 **~22%**（即十年做到 ~7x）。

按 Buffett 清单第 5 节的结论上限规则：**没有安全边际 → 最高 `WATCH`**。本模块对下游 verdict 的贡献是"价格端封顶 WATCH，且只有跌到 ~$110–135 区间才进入可讨论的 starter 安全边际"。

---

## 1. Current Setup（当前价锚）

| 项目 | 值 | 来源 | 备注 |
|---|---:|---|---|
| Share class | Class A (GOOGL) | — | A=1票, B=10票, C(GOOG)=0票 [GOOG.A1.PROXY2026.001] |
| **当前价（canonical）** | **$368.03** | S-YHOO 2026-06-18 收盘 · 三源交叉验证（Yahoo + stockanalysis + websearch，delta 0.0%，过 verify_freshness.py） | 最后一个 ≤ as_of 2026-06-19 的日收盘；区间 $356–373；ATH 收盘 $402.38（2026-05-13）；52周 $162.00–408.61；现价**距高 −9.9% / 距低 +127%**（区间上部，非 52 周低） |
| 当前价（IRR 引擎基准，placeholder） | ~$370 | WebSearch 2026-06-15 | 下文 IRR/MoS 表以 $370 计；canonical $368.03 仅低 0.5%，base 10y IRR 同为 −3.0%，结论不变 |
| 当前价（备用锚） | A $351.81 / C $348.20 | [GOOGL-424B5-2026-06.002/.004] | Berkshire 2026-06 私募定价；与市价仅差 ~5%，互为验证 |
| 摊薄股本 | 12,116M | [GOOG.A1.2026Q1] | 3/31/26；**回购暂停 → 股数在回升**（FY25 末 12,088M） |
| **市值** | **~$4,459B（$4.46T）** | derived | = $368.03 × 12,116M（canonical）；以 $370 placeholder 计为 ~$4,483B，差 0.5% |
| Net cash（保守口径） | +$80.3B | [GOOG.A1.2025K.020/.021] | 现金+有价证券 $126.843B − 长期债务 $46.547B；**未计** non-marketable $68.687B |
| EV（近似） | ~$4,403B | derived | 市值 − 保守 net cash |
| Forward P/E（sell-side 口径，参考） | ~25–26x | gurufocus 2026-06-09（D 级，仅参照） | 注: 这是 GAAP-EPS 口径，**未做 owner-earnings 调整** |
| 市值 / TTM FCF | **~70x** | derived | TTM FCF $64.4B（已被 capex 压缩）[GOOG.A1.2026Q1.025] |

> 锚定说明: 市价 $370 与 Berkshire 私募 $348–352 仅差约 5%，两个独立锚一致，价格基础可靠。下文 IRR/安全边际全部以 **$370** 为基准；用 $350 锚结论方向不变（IRR 抬升不到 1pp）。

---

## 2. Owner Earnings Bridge（owner earnings 桥）

口径: 从 owner-earnings 出发 = 常态化经营净利 + D&A − **维护性 capex** − 真实 SBC 成本 ± 营运资本，**剔除一次性收益**。维护性 capex 不可观测，故给区间: 下限 = 折旧（替换底线），上限 = 总 capex 的 ~50%（假设大量 AI capex 是防御性的、保住护城河所必需而非可选成长）。

完整逐行见 `model/owner_earnings_bridge.csv`。关键节点:

| 项目 | FY2025 | TTM (Q1'26 trailing) | source_id |
|---|---:|---:|---|
| 报告净利 | $132.2B | $160.2B | [GOOG.A1.2025K.007] / derived |
| − 一次性/非经营收益 | −$29.8B（other income net） | −$36.9B（**未实现股权收益, +$2.35 EPS**）+残差 | [block04_10k_fy2025] / [GOOG.A1.2026Q1.022] |
| + 常态化投资收益 | +$1.5B | +$1.5B | ASSUMPTION |
| = **常态化经营净利** | **~$103.9B** | **~$109.8B** | derived |
| + D&A | +$21.1B | +$24.0B | ASSUMPTION_TASK（折旧 ~$21B 任务给定，非 filed 行） |
| − 真实 SBC | −$27.1B | −$28.0B | [GOOG.A1.2025K.023]（Note 13 总额口径） |
| − 维护性 capex（下限 = D&A） | −$21.1B | −$24.0B | → **growth read** |
| − 维护性 capex（上限 = ~50% capex） | −$45.7B | −$55.0B | → **defensive read** |
| **Owner earnings 区间** | **~$52B（防御） … ~$77B（成长）** | **~$51B（防御） … ~$82B（成长）** | derived |

**Owner earnings 结论区间: ~$52B–$82B**（取防御下限到成长上限）。

三个关键判读:
1. **报告净利严重高估 owner earnings ~2–3x。** TTM 报告净利 $160B vs owner earnings $51–82B。最大扭曲源是 Q1'26 的 $36.9B 未实现股权证券收益（非现金、非经营），KOL 易误读为"净利暴增 81%"。干净的增长读数是**营业利润 +30%**。[Contradictions #1]
2. **capex 拆分是整个估值的胜负手。** $91B（FY25）→ 指引 $180–190B（2026）→ 2027"显著增加"[GOOGL-424B5-2026-06.009]。若这是高回报成长（growth read），OE 起点 ~$80B；若是防御性保位（defensive read），OE 起点 ~$52B。10-K/季报**未直接披露**维护 vs 成长拆分 → 这是最大的 OPEN QUESTION，直接决定 base case 落在哪。
3. **SBC 是真实成本 $27.1B。** 回购仅部分对冲稀释，且 Q1'26 回购已归零、股数回升 → SBC 的稀释正在"裸露"。owner-earnings 桥用 Note 13 总额口径（非现金流加回 $24,953M），更保守。[Contradictions #2]

---

## 3. 情景表（bear / base / bull）

每个情景: 给 revenue CAGR、营业利润率路径、capex 强度、退出倍数（terminal P/OE）、payout 路径，得出 owner earnings 十年路径与**在当前价 $370 买入的 10 年 IRR**。完整假设与输出见 `model/scenario_model.csv`。

| 情景 | OE 起点 | revenue CAGR | 营业利润率 | capex 强度 | OE CAGR(1–5y/6–10y) | 退出 P/OE | OE_y10 | **10y IRR @ $370** |
|---|---:|---:|---|---|---:|---:|---:|---:|
| **Bear** | $52B | ~6% | 32%→28% | 22%→18%（防御低回报） | 2%/2% | 14x | $63B | **−13.1%** |
| **Base** | $65B | ~11% | 33%→34% | 20%→15%（26-27峰后回落） | 9%/7% | 20x | $140B | **−3.0%** |
| **Bull** | $80B | ~15% | 34%→37% | 18%→13%（高回报, FCF反转向上） | 14%/10% | 26x | $248B | **+5.2%** |

补充极端乐观穿透检验（成长读 OE 起点 $82B、13%/10%、退出 24x）: IRR 仍仅 **+4.3%**。

### 反推: 当前价 $370 隐含了什么？

| 要达到的 IRR | 退出倍数 | 需要的 OE 十年 CAGR | OE_y10 需到 | = 当前 OE 的 |
|---:|---:|---:|---:|---:|
| 8% | 18x | **21.6%** | $460B | 7.1x |
| 8% | 22x | **19.4%** | $384B | 5.9x |
| 10% | 18x | **23.9%** | $554B | 8.5x |
| 10% | 22x | **21.7%** | $462B | 7.1x |

> 解读: $370 的价格已经把"owner earnings 十年复合增长 ~20–24%、即十年做到约 6–8 倍"当成了**仅仅够格赚到 8–10%** 的前提。对比 facts: 营业利润 FY23→FY25 两年 CAGR ~24%（$84B→$129B），但那是 capex 从 $32B 飙到 $91B、FCF 反而停滞换来的。把营业利润高增长**净化成 owner earnings 高增长**，必须 capex 强度先回落——而指引是 2026-27 还在加。**价格隐含的增长是历史峰值增速，且要求 capex 同时见顶回落，两个乐观假设叠加。**

Owner-earnings yield 视角（最直白）: base OE $65B / 市值 $4,483B = **1.45% 收益率（P/OE 69x）**；bull $80B 也只有 **1.78%（56x）**。即使用报告净利 $132B 也只有 2.95%（P/E 34x）。无论哪个口径，起始收益率都远低于无风险利率，全部回报依赖远期高增长兑现。

---

## 4. Margin of Safety（安全边际表）

买入价反推: 在 base 情景的 OE 路径（退出 20x、payout 30%→55%）下，要达到目标 IRR 的 buy-below 价位:

| 档位 | 目标 IRR | Buy below | vs $370 | 隐含 P/OE0 | 说明 |
|---|---:|---:|---:|---:|---|
| **Avoid above** | — | **> ~$300** | — | >46x | 超过此价，连 bull 情景 IRR 都 <8%，任何合理读法都无安全边际 |
| **(当前价 $370)** | — | — | — | 69x | **位于 avoid 区；不构成 starter** |
| **Starter（试仓）** | 10% | **~$113** | **−70%** | 21x | 跌到此价 base 情景才给 10% |
| **Core（核心仓）** | 12% | **~$95** | **−74%** | 18x | 真实安全边际起点 |
| Deep value | 15% | ~$75 | −80% | 14x | |
| Buy-below 最低门槛 | 8% | ~$134 | −64% | 25x | 连最低 8% 都要 −64% |
| **下行保护锚** | bear 8% | **~$48** | **−87%** | 14x(bear) | 即使 bear 情景兑现仍能赚 8% 的价格——真正"不会永久亏损"的水平 |

### 安全边际是否真实？

**否（在当前价）。** 逐条对 Buffett 清单第 5 节:
- 「保守估值明显高于价格」: ✗ 保守（bear/base）估值远**低于**价格。base 公允价 ~$113（10% 折现），bear 下行锚 ~$48。
- 「business quality 极高、即使低增长也不易永久亏损」: 质量高，但**起始 owner-earnings yield 仅 1.5%**——低增长情景下今天买入会永久跑输，护城河保护的是"生意存活"，不是"$370 的本金"。
- 「资产/现金流/资本结构保护下行」: ✗ 反向。资产负债表正在**加杠杆做 capex**（FY25 净发债 ~$64.6B，Q1'26 再 +$31.4B，回购归零 [facts §5]），$80B 自由放在 capex 与发债上，现金缓冲对 $4.48T 市值微不足道。
- 「未来三年没增长今天价格是否合理」: ✗ 三年零增长则 owner earnings 停在 ~$65B，对 $4.48T 是 1.45% 收益率，明显不合理。

**安全边际来源测试**: 当前价的全部回报来自**乐观假设**（capex 转化为高回报增长 + 退出倍数维持高位）。按清单规则，"安全边际来自乐观假设 → 最高 WATCH"。

---

## 5. Valuation Discipline 自检

- ✅ 好公司在错的价格仍是差投资——本案的标准范例: 生意质量与价格安全边际是两件事，GOOGL 生意大概率优秀，但 $370 的价格安全边际为负。
- ✅ 未用激进 terminal 假设救回报: 即便给 bull 26x 退出，IRR 也只有 5.2%；没有靠拔高倍数把弱回报包装成强回报。
- ✅ 不确定性高 → 要求更大折扣: capex 维护/成长拆分不可观测 + 反垄断尾部（DOJ adtech 结构性救济"could have a material adverse effect" [facts §9]）+ AI 对搜索广告 load 的颠覆风险，三重不确定性叠加，要求的安全边际应偏向 base 甚至 bear 锚，即 buy-below 应更靠近 $95–113 而非 $134。

---

## 6. Open Questions（触发回流/影响裁决）

- [ ] **维护性 vs 成长性 capex 拆分**（最高优先级）: 整个 base case 落点取决于此。10-K/季报未披露；需用单位经济（每单位算力的增量收入/利润）或管理层 call 口径逼近。当前用"D&A 下限 / 50% 上限"是粗口径。
- [ ] **2026 capex $180–190B、2027"显著增加"对前瞻 owner earnings 的压制**未滚进十年模型的逐年路径（当前用 OE CAGR 概括）。若 2027-28 capex 占营收仍 >20%，base 的 9% OE 增速可能偏乐观。
- [ ] **退出倍数（terminal P/OE）的合理区间**: 用了 14/20/26x。若市场对"AI capex 永久压低 FCF 转化率"重定价，成熟期倍数可能落到 12–15x（bear 锚），base IRR 进一步恶化。
- [ ] **D&A 真实数字**: $21.1B（FY25）是任务给定/估计，非 facts.md/10-K pull 行——它同时是维护 capex 下限锚，需用 10-K 现金流量表核实。[owner_earnings_bridge: ASSUMPTION_TASK]
- [ ] **sell-side 一致预期 / 行业估值锚**未拉（B 级），facts.md INTERPRETATION 为空——本模块的 OE CAGR/利润率假设缺一致预期对照。
- [ ] **DOJ adtech 结构性救济最终判决**的尾部量化未进 bear 情景（当前 bear 只压增速，未单列分拆/救济冲击）。

---

## 7. 与 financial_quality 模块需交叉核对（cross-check）

本模块的 owner-earnings 桥与下列项必须与 financial_quality / 财务质量模块对齐，**任一不一致以更保守者为准**:

1. **维护性 capex 拆分口径**: 本模块取"D&A 下限 / 50% 上限"。若 financial_quality 用单位经济得出不同拆分（如成长 capex 占比更高 → OE 起点上移；或折旧周期短、替换需求高 → 维护 capex 更高 → OE 下移），需统一，因为它直接决定 base IRR 正负。
2. **SBC 口径**: 本模块用 Note 13 总额 $27.1B（保守）；现金流加回口径为 $24,953M。financial_quality 若用后者，owner earnings 会高 ~$2B/年——需说明并统一。[Contradictions #2]
3. **一次性收益剔除**: 本模块剔除 FY25 other income $29.8B 与 TTM 的 $36.9B 未实现股权收益。financial_quality 的"质量调整后盈利"必须同口径剔除，否则两模块的 owner earnings 基数对不上。[Contradictions #1]
4. **net cash 口径**: 本模块只认 marketable（+$80.3B），未计 non-marketable $68.687B。若 financial_quality 把 non-marketable 计入流动性，安全边际会略松——但这些是 VC/私募股权，流动性差，建议维持本模块的保守口径。
5. **股数走向**: 回购暂停 + Q1'26 股数回升 12,088M→12,116M。financial_quality 的稀释/回购分析需确认 forward 股数假设（本模块隐含 payout 含回购，若回购长期暂停则 payout 中"buyback"部分要下调，base IRR 再降）。
6. **FCF 口径**: 本模块用 derived FCF（FY25 $73.3B）/ stated TTM $64.4B，注意 FCF 非 10-K 列报项 [Contradictions #3]——两模块引用 FCF 时需标明 derived/stated。

---

## 方法学（IRR 计算口径）

- IRR 引擎: 投资者 t0 按 $370×12,116M 支付股权对价；每年收到 owner earnings × payout（股息+净回购，随 capex 正常化由 30% 升至 55%）；第 10 年额外收到 terminal 股权价值 = OE_y10 × terminal P/OE + net cash。留存的 owner earnings 用于驱动 OE 增长（不重复计入），故唯一的额外现金事件是终值。用二分法解 NPV=0 的折现率。
- 保守取舍: net cash 只认 marketable；payout 近年压低（capex 超级周期）；bear 退出倍数压到 14x；终值 net cash 假设不随回购/现金堆积放大。
- 这些取舍**偏保守**，意味着真实 IRR 可能略高于表中数字，但即便如此 bull 也仅 +5.2%，结论稳健。
- 计算脚本: 临时脚本（已删除），核心公式与全部输出固化在 `model/scenario_model.csv`。
