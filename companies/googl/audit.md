# GOOGL Audit / Quality Gate (Step 7 — pre-IC adversarial QA)

Last updated: 2026-06-16
Auditor stance: **对抗性找漏洞**（adversarial hole-punching），不是再夸一遍。This is the independent quality gate that sits **between** the analysis modules (Step 4-6) and the IC Panel (Step 8). 它不新增事实、不裁多空，只检验证据是否扎实、模块间是否自洽、缺口在哪、最高允许给什么 verdict。

Inputs audited: `facts.md`, `claim_ledger.csv`（61 行）, 8 analysis modules（business_model / financial_quality / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map / valuation）, `model/{financial_history, owner_earnings_bridge, scenario_model}.csv`。
Checklists applied: `frameworks/investment_research_pipeline_detailed.md` §9（审计 11 项 + verdict ceiling 表）+ `frameworks/buy_side_research_department.md` §4（硬规则）。

---

## 0. 一句话审计结论

证据工程与分析层质量**高于多数买方初稿**：~50 条关键 claim 全部回挂一手 A1（SEC），口径纪律（剔除一次性收益、SBC 真实成本、FCF derived 标注）在 8 个模块间**高度一致**，模型算术**逐项勾稽通过**，无 D1/C2 污染。**但有两个必须先处理的问题**：①**全仓多处自描述已 stale**——facts.md / research_status.md / README.md / 三个分析模块仍写"valuation/inversion/分析模块未做、硬规则封顶 WATCH"，而事实是这些模块现已全部完成（硬规则封顶**应已解除**）；②真正的 verdict ceiling 已**不再是"缺模块"的硬规则**，而是 valuation 的**实质发现：$370 现价无安全边际**（连 bull 情景 10y IRR 仅 +5.2%，低于 8% 门槛）。两者叠加：**ceiling = WATCH，但理由从"信息不足"变成了"信息够了、价格太贵"。**

---

## 1. Source coverage（各模块关键论断能否回到 facts 的 source_id？）

抽查每个模块的核心论断 → 追溯 source_id：

| 模块 | 抽查的关键论断 | 回挂 source_id | 判定 |
|---|---|---|---|
| business_model | Search +19%、Cloud +63%/32.9%、Network 下滑、capex 压 FCF | `.2026Q1.004/.010/.015/.006`、`.2025K.016/.017` | ✅ 悬空=0 |
| financial_quality | OE 区间 $52–77B、净利剔 $36.9B、capex 3 年 3.4x | `.2025K.007/.016/.023`、`.2026Q1.022` + bridge.csv | ✅ ASSUMPTION 均明标 |
| value_chain_map | 利润 95%+ 在 Services、Network 下滑、capex 出资规模 | `.2025K.005/.009/.010`、`.2026Q1.006`、`424B5-.009` | ✅ 结构推断均标〔E1〕 |
| moat_map | 7 条护城河逐条挂证据、Cloud 利润率跃升 | 每条 H5-x 均带 `[source_id]` | ✅ Weak 项诚实降级 |
| bottleneck_map | B1-B8 表逐行挂证据；未量化项标"未挂证据" | capex/Cloud/SBC 系列 | ✅ 未臆造数字 |
| operator_underwriting | capex 决策、回购暂停、52.7% 投票权、薪酬 | `.2025K.016/.018`、`PROXY2026.004/.007` | ✅ 8 维记分卡逐项挂证 |
| inversion_map | F1-F9 失败路径、Kill Criteria 阈值 | 每条 F 带 `[source_id]` + 当前读数 | ✅ |
| valuation | 现价 $370、IRR 三情景、MoS 表、市值 | scenario_model.csv + `.2025K.020/.021` | ✅ 非 filed 数标 ASSUMPTION |

**结论**：source coverage **强**。逐模块抽查未发现"悬空关键论断"（=有数字/判断却无 source_id 或无明确证据级标注）。所有模块都遵守了"数字唯一来源=facts.md"的纪律，结构性推断一律就地标〔E1/结构推断〕并进 open questions。

**唯一软肋**：valuation 的"当前价 $370"来自 WebSearch（2026-06-15 stockanalysis/Yahoo），不是 A1——但已用 Berkshire 私募 $348–352（A1）作独立交叉锚，差 ~5%，可接受。

---

## 2. 无 source_id 的关键 claim

逐模块扫描"作为论断使用、却无 source_id 也无证据级标注"的 claim：**未发现裸奔的关键 claim。** 所有非 filed 数字都落在以下三类已标注的桶里，不算违规：

- **ASSUMPTION_TASK**（父任务给定、非 facts）：D&A ~$21.1B（FY25）/ ~$24B（TTM）。**这是估值与 OE 桥的输入，却不在 facts.md/10-K pull 里** → 已在 bridge.csv、financial_quality §1.2、valuation §2 三处明标 ASSUMPTION_TASK 并进 open questions。**审计意见：合规（透明），但它同时是维护 capex 下限锚，是 OE 区间的隐性支点，回流补料时必须用 10-K 现金流量表坐实并入 ledger。**
- **ASSUMPTION**（分析判断）：维护/成长 capex 拆分、营运资本=0、TTM 残差 other income −$15B、归一化投资收益 +$1.5B、WACC 8–10%、各情景增速/退出倍数。均明标。
- **〔结构推断/E1〕**（行业机制）：TAC 去向、创作者分成 ~55%、NVDA 抽税、TPU 成本优势、各份额量级。均就地标注 + 进 open questions。

**唯一边缘项**：`GOOG.SEED.SearchFY2025`（Search&other FY2025 年度 $224,532M）在 ledger 中状态=`seed_needs_audit`、destination=`OPEN_QUESTION`，且 business_model §2.1 已明确"降级待核、未由 10-K 验证"。**处理正确**——它没有被当 EVIDENCE 用。

---

## 3. 冲突数字 / 模块间口径不一致（父任务重点核 3 项 + 全面扫描）

### 父任务指定的 3 个重点核查项 —— 结果：**全部一致，无冲突**

**(a) owner earnings 区间在 financial_quality vs valuation 是否一致？** ✅ **一致。**
- financial_quality：FY2025 **$52B–77B**、TTM **$51B–82B**（§1.2/§1.4）。
- valuation：FY2025 **$52–77B**、TTM **$51–82B**，结论区间"$52–82B"（§2 表 + 正文）。
- 两者同引 `owner_earnings_bridge.csv`，逐行数字一致。**这是父任务最担心的点，实际无矛盾。**

**(b) 当前价锚 $370 vs Berkshire 私募 $350 的处理是否统一？** ✅ **一致且处理正确。**
- valuation 把 **$370 设为基准锚**（IRR/MoS 全用 $370），把 **Berkshire $348–352 设为独立交叉锚**（差 ~5%，互验），并明确"用 $350 锚结论方向不变（IRR 抬升<1pp）"。
- 全仓所有模块（operator/inversion/value_chain/financial_quality）口径统一："Berkshire $10B 是 Section 4(a)(2) **私募融资定价**，不是纯二级增持 → '巴菲特背书安全边际'叙事须降权为'参与了一轮 AI capex 融资'"。**口径完全统一，且这是本研究最关键的 contrarian 纠偏之一。**

**(c) 净利 vs 营业利润口径全模块是否统一剔除一次性收益？** ✅ **高度统一（最强的一致性项）。**
- 抽查全部 8 模块 + facts：凡触及 Q1'26 净利 +81% 的，**无一例外**都标注"被 $36.9B 未实现股权收益抬高、营业利润 +30% 才是干净读数"（business_model §2.0、financial_quality §1.1/§3、moat_map §2.2/§4.2、operator §3/§4.5、inversion F-表、valuation §2、facts Contradictions #1）。**没有任何模块把 net income +81% 当成长读数。** 这是教科书级的口径纪律。

### 全面扫描发现的口径项（非冲突，但需 IC 知晓）

| 项 | 状态 | 处理 |
|---|---|---|
| **SBC 双口径** Note13 $27.1B vs 加回 $24,953M | ⚠ 两模块都用 $27.1B（保守） | financial_quality + valuation 均取 Note13 总额，差额 $2,147M 已说明=现金结算/Waymo。**一致，无冲突。** valuation §7 cross-check 已提示"若用加回口径 OE 高 ~$2B/年"。 |
| **股本** facts 12,088M（FY25末）vs valuation/history 12,116M（Q1'26） | ✅ 不同日期 | 非冲突；financial_quality/valuation 均正确读出"回购暂停→股数由 12,088 回升 12,116"。 |
| **FCF** derived（FY25 $73.3B）vs stated（TTM $64.4B） | ✅ 已标 | 多模块均标"FCF 非 10-K 列报项，FY 为 derived、Q1'26/TTM 为 non-GAAP stated"（facts Contradictions #3）。 |
| **EC 罚款** facts 写"€3.0B 计提 $3.5B" | 🟡 汇率换算 €3.0B→$3.5B 未单列汇率 | 一手 10-K 口径，可接受；属定性尾部，不影响数字结论。 |

**§3 结论**：模块间**无实质数字冲突**。父任务担心的 3 项实测全部一致。这反映 8 个模块确实都吃了同一份 facts.md，纪律到位。

---

## 4. Stale facts（时效性）—— ⚠ **本审计最重要的发现**

数字本身不 stale（FY2025 10-K + Q1'26 10-Q + 2026-06 proxy/424B5 + Q1'26 13F，均为最新一手，截至 2026-06-16）。

**但全仓"研究进度/verdict 上限"的自描述严重 stale**——多处仍声称分析层与估值"未做"，而它们现已全部完成：

| 文件 / 位置 | stale 文字 | 实际状态 | 严重度 |
|---|---|---|---|
| `facts.md` 行 6 | "分析模块(business/moat/value-chain/operator/inversion)与估值**尚未完成**…最高只能到 WATCH" | 全部已完成 | 🔴 高 |
| `facts.md` Minimum Coverage Check（行 92-105） | Business/ValueChain/Moat/Inversion 标"⏸ 未做"；Valuation"⏸ 未做→硬规则封顶 WATCH"；完整度"45-50%" | 8 模块 + 估值全建 | 🔴 高 |
| `research_status.md` 行 11 | "valuation / inversion / 分析模块**未做**，硬规则封顶 WATCH。信息完整度 ~45-50%" | 同上 | 🔴 高 |
| `README.md` 行 7 | "Current verdict ceiling: **INFO-GAP**" | 更 stale（连 WATCH 都不到） | 🟠 中 |
| `moat_map.md` 行 10 | "facts.md Minimum Coverage Check 已硬规则封顶 WATCH（缺 valuation/inversion）" | valuation/inversion 已做 | 🟠 中 |
| `bottleneck_map.md` 行 6 | "估值/inversion **未做**" | 已做 | 🟠 中 |
| `inversion_map.md` 行 7、129 | "verdict 仍受 valuation **未做**封顶 WATCH" | valuation 已做 | 🟠 中 |

**含义**：这些 stale 自描述会误导 IC 以为"还缺模块、ceiling 是因信息不足"。**真相相反**：模块齐了，ceiling 之所以仍是 WATCH，是因为**估值实质结论=无安全边际**（见 §11）。**回流动作**：把上述 7 处"未做/封顶 WATCH 因缺模块"的文字更新为"模块已完成；ceiling=WATCH 因 valuation 无安全边际 + 10 年序列仍缺"。这不改变 verdict，但改变 verdict 的**理由**，对 IC 很关键。

---

## 5. D1/C2 污染（社媒/KOL 是否混进 EVIDENCE 支撑某模块判断）

**结论：零污染。** 全仓扫描 TradesMax / 美股投资网 / meigutouzi-wechat / KOL / 段永平 / H&H 的所有出现位置：

- `facts.md` SENTIMENT 段：TradesMax = D1/C2，明标"只能作选题入口与 contrarian 信号，**永不进 EVIDENCE**"。✅
- `value_chain_map.md` 行 229：明确声明"本模块未引用任何 D1 社交/C2 评论作为价值链结构证据"。✅
- **段永平 / H&H** 全部经 13F（机构季末快照）处理，且每处都带"H&H ≠ 段永平个人实时交易、市值变化≠净买入"caveat（facts Contradictions #4、block09、claim_ledger HH 行）。✅ H&H 翻倍到 3.7M 股是 13F 一手（A1）坐实的，不是 KOL 传闻。
- "KOL 易误读净利 +81%"仅作为**反向提醒**出现（valuation/operator/facts），不是用 KOL 当证据。✅

无任何模块判断由社媒/视频/论坛线索支撑。Gate A"事实/解读/情绪分开"达标。

---

## 6. Math / Model 错误（抽查 scenario_model IRR 勾稽、owner_earnings_bridge 加总）

用独立脚本重算全部关键数字（脚本已删，不留仓）：

| 检查 | 模型值 | 重算值 | 判定 |
|---|---|---|---|
| FY25 OE maint_low | 76,783 | 76,783 | ✅ |
| FY25 OE maint_high | 52,183 | 52,183 | ✅ |
| TTM 净利（132170−34540+62578） | 160,208 | 160,208 | ✅ |
| TTM OE 区间 low/high | 81,793 / 50,793 | 81,793 / 50,793 | ✅ |
| TTM 营收/营业利润/FCF | 422,498 / 138,129 / 64,429 | 同 | ✅ |
| FY25 derived FCF | 73,266 | 73,266 | ✅ |
| OE_y10（复利）bear/base/bull | 63 / 140 / 248 | 63.4 / 140.3 / 248.1 | ✅ |
| Terminal equity value bear/base/bull | 968 / 2,886 / 6,530 | 967.4 / 2,885.4 / 6,529.9（用**未取整** OE） | ✅ |
| **10y IRR @ $370 bear/base/bull** | **−13.1% / −3.0% / +5.2%** | **−13.1% / −3.0% / +5.2%** | ✅ **完全勾稽** |
| 市值 / net cash / OE yield / P/FCF | 4,483 / 80.3 / 1.45% / 69.6x | 同 | ✅ |
| Cloud Q1 利润率 / Services OI 率 / 各营业利润率 | 32.9% / 40.7% / 32.0% / 36.1% | 同 | ✅ |

**结论：模型算术全部勾稽，无错误。** IRR 二分法引擎（中间 payout + 第 10 年终值卖出）重算与模型一致到小数点。

**一个细节澄清（非错误）**：terminal_equity_value 三个数（968/2886/6530）是用**未取整**的 OE_y10（967.4/2885.4/6529.9）× 退出倍数 + net cash 得出，与正文展示的取整 OE_y10（63/140/248）相乘会差 ~6（962/2880/6528）。**IRR 用的是未取整路径，故结果不受影响**——这是展示取整 vs 计算精度的正常差异，不是勾稽错误。建议在 scenario_model.csv 给 OE_y10 加一位小数以消除读者困惑（可选，低优先）。

---

## 7. 缺一手源

| 缺口 | 当前状态 | 影响 |
|---|---|---|
| **10 年财务序列** | 仅 FY2023–2025 + Q1'26/TTM（3 年） | 🔴 Buffett §3 要求的 10 年 ROIC、累计 FCF vs 累计回购/SBC"漏桶"分析无法做；financial_quality §2 已硬标 GAP |
| **D&A 绝对值** | 父任务给 $21.1B，非 10-K pull | 🟠 是 OE 桥维护 capex 下限锚，需核 10-K 现金流量表 |
| **Search&other FY2025 年度细分** | seed $224,532M，未由 10-K disaggregation 验证 | 🟡 已正确降级 OPEN_QUESTION |
| **TAC、CPC、paid clicks、YouTube 时长/订阅/Play 单列** | 10-K 未单列 | 🟡 影响"量 vs 价"拆分、护城河本体指标量化 |
| **sell-side 一致预期 / 行业估值锚（B 级）** | 未拉，facts INTERPRETATION 为空 | 🟡 估值 OE CAGR/退出倍数缺外部对照 |
| **earnings call transcript** | 未拉 | 🟠 管理层 capex ROI 口径的唯一可能来源（见 §8） |

一手 SEC 文件覆盖**完整且最新**；缺的是"更细的披露行"（10-K 内不单列）+ "更长的历史序列" + "B 级外部对照"。

---

## 8. 管理层未验证 claim

**审计意见：管理层 claim 处理得当——本研究几乎不依赖任何未验证的管理层说法。**

- 用的全是**可观察行为**（capex 实际数、回购实际数、发债实际数、proxy 持股/薪酬/关联交易），不是管理层的前瞻承诺。operator_underwriting 明确纪律"只用可观察行为，不做心理诊断"。✅
- **唯一的管理层前瞻 claim = 2026 capex 指引 $180–190B + 2027"显著增加"**——这来自 424B5（A1 法律文件，非口头），已 verified（`424B5-2026-06.009`）。✅
- **关键未验证缺口**：管理层**从未在一手披露里给过 AI capex 的 ROI 门槛 / 利用率假设 / 回报回顾框架**。operator §4 红旗1 + inversion K3 都把这点列为"区分纪律性押注 vs FOMO 军备竞赛的证据**目前不存在**"。**审计确认这是真实缺口，且已被两个模块正确标为最大不确定性**，需拉 earnings call 补（B/A2 级）。
- Cloud "backlog over $460B"是管理层口径（季报披露，A1），但**可取消性/确认周期/客户集中度未知**（bottleneck OQ 已挂）——IC 应知"backlog ≠ 已确认收入"。

---

## 9. 估值假设过激或过松

**审计意见：估值假设整体偏保守，未发现"用乐观假设救回报"。** 这是本研究最硬的部分。

支持"不过激"的证据：
- bull 情景已给到 revenue CAGR 15%、营业利润率 37%、退出 26x、OE 起点 $80B（成长读上限），**IRR 仍只有 +5.2%**——即用激进假设也救不回 8% 门槛。valuation §5 自检"未用激进 terminal 假设救回报"成立。
- 另做极端乐观穿透（OE 起点 $82B、13%/10%、退出 24x）：IRR **+4.3%**，方向不变。
- net cash 只认 marketable（$80.3B），未计 non-marketable $68.7B（保守）；payout 含回购但已提示"回购长期暂停则 base IRR 再降"。

**可被质疑的偏松点（IC 应压测）**：
- **base 退出倍数 20x**：对一个"FCF 转化率被 capex 永久压低"的公司，成熟期 20x P/OE 可能偏高；valuation §6 自己承认"若市场重定价，成熟期倍数可能落 12–15x（bear 锚）"。若 base 退出降到 16x，base IRR 会更负。
- **base OE 起点 $65B = 防御$52B 与成长$77/82B 的中点**：这个"取中点"是判断，不是证据。**真实落点完全取决于维护 vs 成长 capex 拆分（不可观测）**——这是整个估值的胜负手，已正确标为头号 open question。
- **bear 仅压增速（2%/2%），未单列 DOJ 结构性救济/拆分冲击**：valuation §6 + inversion 都承认 bear 没把"剥离 adtech"的尾部量化进去 → **真实下行可能比 bear −13.1% 更差**。这是"过松"的方向，对结论（无安全边际）只会强化，不会推翻。

**净判断**：假设偏保守，结论稳健。没有"为了得出买入而拔高假设"的痕迹；相反，下行尾部（监管拆分）还**没有充分压进 bear**，意味着真实安全边际只会更差。

---

## 10. 风险未量化

| 风险 | 量化程度 | 缺口 |
|---|---|---|
| AI 侵蚀搜索变现（F1） | 🟡 半量化 | 有 Kill Criteria 阈值（Search 连 2 季 ≤+8%），但 AI Overviews 对单 query RPM 的**单位经济无证据**——头号未量化项 |
| capex 黑洞 / 增量 ROIC（F3） | 🟡 半量化 | OE 区间 + capex/OCF 比率（Q1'26 78% 已踩线）有量化，但 incremental ROIC 因维护/成长拆分缺失**无法精算** |
| 监管结构性救济（F2） | 🟠 弱量化 | €3.0B/$3.5B 罚款已量化（占净利 ~2.6%），但**剥离/拆分的概率与利润池冲击未量化**，bear 情景未单列 |
| Cloud 利润率坍塌（F5） | 🟡 有阈值 | 32.9% 可持续性"未经多季验证"——已标 open question + Kill Criteria（连 2 季回落>5pp） |
| 控制权集中（F7） | ✅ 已量化（定性） | 52.7% 投票权是事实；inversion 正确判定"放大器，不单独裁多空" |
| 估值过高（F9） | ✅ 充分量化 | 这是唯一被完整量化的风险（IRR/MoS 表）；K8 已与 QQQ 4yr 2.03× 基准挂钩 |

**结论**：风险**识别完整**（inversion 覆盖 9 类全部命中 checklist），**阈值化（Kill Criteria）做得好**（K1-K9 可观测），但**三个尾部的"概率×影响"未量化**：①AI 对搜索 RPM 的单位经济、②DOJ 拆分的破坏量级、③incremental ROIC。这三个恰好都卡在同一个不可观测变量上，且都已正确进 open questions。**对 IC：这些是"押注 vs 定价"的灰区，不是被忽略的盲区。**

---

## 11. Completeness % 粗估 + Verdict Ceiling

### 11.1 完整度加权（事实线 / 理解线 / 决策线，宁低勿高）

| 线 | 权重 | 子项完成度 | 加权得分 |
|---|---:|---|---:|
| **A. 事实线**（source→raw→ledger→facts→audit） | 35% | raw/ledger/facts/audit 齐全、61 claim、~50 verified A1；**扣分：10 年序列仅 3 年、D&A 未入 facts、Search 年度细分待核** | 28/35（80%）|
| **B. 理解线**（business→value chain→moat→operator→inversion） | 35% | **5 模块全完成且高质量**；扣分：moat 中 TPU/人才/YouTube 本体指标证据 Weak（10-K 不披露）、量 vs 价未拆 | 30/35（86%）|
| **C. 决策线**（owner earnings→valuation→MoS→verdict→monitor） | 30% | OE 桥 + 三情景 IRR + MoS 表完成、勾稽通过；扣分：**维护/成长 capex 拆分不可观测（base 落点的胜负手）、退出倍数/bear 尾部偏松、monitor.md 未建、memo 未写** | 22/30（73%）|

**加权完整度 ≈ 28+30+22 = 80/100 → 取保守区间 `72–78%`，落点 **~75%**。**

> 说明（宁低勿高）：理解线虽 5 模块齐全，但其中 3 条护城河（TPU/人才/YouTube）证据是 Weak（一手指标 10-K 不披露），不能按满分计；决策线的 base case 落点完全压在一个不可观测变量上，扣到 73%。**故不取 80%，取 ~75%** —— 比 facts.md/research_status 现写的"45-50%"显著高（因为那两处是 stale，写于分析层未做时）。

### 11.2 Verdict Ceiling（套表 + 叠硬规则取更低）

**第一步：完整度表**
- ~75% → 落在 **60-80% = STARTER** 区间。

**第二步：硬规则（buy_side_research_department §4）—— 父任务要求确认的关键点**

| 硬规则 | 是否触发封顶？ | 确认 |
|---|---|---|
| 没有 valuation.md / 安全边际 → 最高 WATCH | **❌ 不再触发** | valuation.md **已完成**（owner earnings + bear/base/bull + 10y IRR + MoS 表齐全）→ **此硬规则解除** |
| 没有 inversion_map.md → 最高 WATCH | **❌ 不再触发** | inversion_map.md **已完成**（F1-F9 + Kill Criteria）→ **解除** |
| 没有 operator_underwriting.md → 最高 STARTER | **❌ 不再触发** | operator **已完成**（People Map + 8 维记分卡 28/40）→ **解除** |
| 社媒是主要证据 → 最高 INFO-GAP | ❌ 不触发 | 零 D1/C2 污染（§5）|
| 不了解生意怎么赚钱 → REJECT/INFO-GAP | ❌ 不触发 | business_model 完整、清晰 |

**→ 父任务的核心确认点成立：valuation/inversion/operator/moat 现已齐全，"缺模块"的硬规则封顶已全部解除。** 这是相对 facts.md/research_status 旧状态的实质变化。

**第三步：valuation 的实质结论（新的、真正的 ceiling 来源）**
- valuation §0/§4 的发现：**$370 现价无安全边际**——bull 情景 10y IRR 仅 +5.2%（<8% 门槛），base −3.0%，bear −13.1%；起始 OE yield 仅 1.45%。
- Buffett 清单第 5 节规则："安全边际来自乐观假设 / 无安全边际 → 最高 WATCH"。
- **这把 ceiling 从 STARTER（完整度给的）压回 `WATCH`** —— 但理由不是"信息不足"，而是"信息足够、价格太贵"。

**第四步：取更低 → 最终 Verdict Ceiling = `WATCH`**

| 来源 | 给出的上限 |
|---|---|
| 完整度 ~75% | STARTER |
| 缺模块硬规则 | （已全部解除，不再封顶）|
| **valuation 实质：无安全边际** | **WATCH** ← 取更低 |
| 10 年序列缺 + base 落点压在不可观测拆分 | 强化 WATCH |

### Ceiling Rationale（为什么是 WATCH，且和过去不同）

**过去（facts.md/research_status 现写）：WATCH，因为"分析层+估值未做、信息 45-50%"。**
**现在（本审计）：WATCH，因为"模块齐了（完整度 ~75%、硬规则已解除），但 ① $370 现价连最乐观情景都赚不到 8%、无安全边际；② 10 年序列缺 + 维护/成长 capex 拆分不可观测，使 base case 落点无法收敛。"**

即：**这是一个"研究做扎实了、结论是'好公司但当前价格不值得买'"的 WATCH，不是"还没研究完"的 WATCH。** 距离 STARTER 只差**价格**（需跌到 ~$113 一带 base 才给 10%）与**两个证据补强**（10 年序列 + capex 拆分），而非缺模块。

---

## 暴露缺口清单（按优先级）+ 回流到哪一步

| # | 缺口 | 优先级 | 回流步骤 | 具体动作 |
|---|---|---|---|---|
| G1 | **stale 自描述**（facts/research_status/README/3 模块仍写"未做/封顶因缺模块"） | 🔴 P0（最快、零成本） | Step 6→7 元数据 | 更新 7 处文字为"模块已完成；ceiling=WATCH 因无安全边际 + 10 年序列缺"。**不改 verdict，改理由。** |
| G2 | **维护性 vs 成长性 capex 拆分**（base case 落点的胜负手 + incremental ROIC 前置） | 🔴 P0 | Step 5(原始)→Step 8(估值/财务质量) | 拉 earnings call + 单位经济（每 MW/每 TPU/每 query 推理成本）逼近拆分；这是 OE 区间从"$52–82B 大区间"收敛到"可定 base"的唯一路径 |
| G3 | **管理层 AI capex ROI 门槛/利用率**（区分纪律 vs FOMO 的证据现不存在） | 🔴 P0 | Step 5→Step 7(operator)+Step 8(inversion K3) | 拉 Q1'26 及历史 earnings call transcript（B/A2） |
| G4 | **10 年财务序列**（Buffett §3 漏桶分析） | 🟠 P1 | Step 5(Block 04 扩展)→Step 8(financial_quality) | 从 SEC/XBRL 拉 FY2016–2022 收入/利润/FCF/ROIC/股本/SBC |
| G5 | **D&A 绝对值入 facts**（OE 桥维护 capex 下限锚，现为 ASSUMPTION_TASK） | 🟠 P1 | Step 5→Step 6(ledger)→Step 8 | 核 10-K 现金流量表，把 $21.1B 升级为 verified A1 |
| G6 | **DOJ adtech 结构性救济尾部量化**（bear 未单列拆分冲击） | 🟠 P1 | Step 8(inversion F2/valuation bear) | 给"纯罚款 / 行为救济 / 结构剥离"概率分布 + 对广告利润池冲击 |
| G7 | **Cloud 32.9% 利润率可持续性 + backlog 质量**（多季趋势/可取消性/集中度） | 🟡 P2 | 跨季 monitor | Step 12 monitor.md（待建）逐季跟踪 |
| G8 | **Search&other FY2025 年度细分 / TAC / CPC / 量价拆分** | 🟡 P2 | Step 5→Step 6 | 核 10-K 广告 disaggregation 表 + MD&A cost of revenues |
| G9 | **sell-side 一致预期（B 级对照）** | 🟡 P2 | Step 5→facts INTERPRETATION | 拉 1-2 家投行 owner-earnings/估值锚作外部对照 |
| G10 | **monitor.md + memo-v1.md 未建** | 🟡 P2（IC 后） | Step 11/12 | IC Panel 后落决策 memo + 监控清单（Kill Criteria 已就绪可直接搬） |

---

## 给 IC 的提示（本审计放行，但 IC 必须正面回应下列质询点）

放行结论：证据扎实、口径自洽、模型勾稽、无污染——**可进 IC Panel**，但 verdict 上限锁 `WATCH`，IC 不得突破到 STARTER 除非价格/证据补强（见 ceiling rationale）。IC 必须正面回应：

1. **价格质询（最硬）**：$370 用 bull 假设都只有 +5.2% IRR、起始 OE yield 1.45%——**这不是"打折买好公司"，是"用乐观假设也难赚 8%"。Buffett/Klarman 立场下，好生意 + 无安全边际 = 不买。** IC 必须明确："我们是 WATCH 等回调（~$113 区间），还是认为估值假设太保守？"
2. **base case 落点不可收敛**：OE 区间 $52–82B 太宽，base $65B 是"取中点"的判断而非证据；落点完全压在不可观测的维护/成长 capex 拆分上。**在补到 G2 前，base IRR −3.0% 本身就是个宽误差带的点估计。**
3. **F1×F3 合流**（inversion 头号永久减值路径）：AI 答案压单 query 变现 + 被迫越投越多 capex 防守 = 收入仍增、owner earnings 被永久稀释。**这条路径今天无单位经济证据证伪，市场在"押注"而非"定价"。**
4. **Berkshire 不是背书**：$10B 是 $348–352 **私募融资定价**，不是抄底——"巴菲特买入=安全边际"的叙事必须在 IC 桌上被正式否掉。
5. **双层股权的双向性**：52.7% 投票权在"押注正确"时是长期主义护城河，在"押注错误"时是无法叫停的放大器；而判断押注对错的 capex ROI 证据**恰恰缺失**（G3）。
6. **stale 元数据已修正前提**：IC 读到的 facts.md/research_status 若仍写"45-50%/未做"，请以本 audit 的"~75%/模块齐全/ceiling 因无安全边际"为准。
