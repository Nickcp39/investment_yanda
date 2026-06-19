# CEG Audit / Quality Gate (Step 7 — pre-IC adversarial QA)

Last updated: 2026-06-19
Auditor stance: **对抗性找漏洞**（adversarial hole-punching），不是再夸一遍。This is the independent quality gate that sits **between** the analysis modules (Step 3-6) and the IC Panel (Step 8). 它不新增事实、不裁多空，只检验证据是否扎实、模块间是否自洽、缺口在哪、最高允许给什么 verdict。

Inputs audited: `facts.md`, `source_register.md`（S1–S12）, `claim_ledger.csv`（C001–C028，28 行）, 8 analysis modules（business_model / financial_quality / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map / valuation）, `model/{scenario_model.csv, model_assumptions.md}`, `memo-v1.md`, `step0_plan.md`。
Checklists applied: GOOGL `audit.md` 的 11 项审计 + verdict ceiling 表（同构对齐）+ `frameworks/buy_side_research_department.md` §4（硬规则）+ `frameworks/agent_testing/approved_agents.md`（灵魂分级）。

---

## 0. 一句话审计结论

证据工程与分析层质量**扎实且口径自洽**：28 条 claim 全部回挂 source_id（S1–S12），一手优先纪律（A1/A2/A3 vs B2 分级清楚）、kill-criteria 在 facts/inversion/memo 三处**逐字一致**（a defused / b floored / c partial / d not-triggered / e accelerating）、scenario_model 算术**逐项勾稽通过**（12.0×18=216、13.0×25=325、13.8×30=414）、无 D1/C2 社媒污染。**但有一个必须先处理的 #1 审计缺口**：**headline 财务（FY2025、Q1'26）的两条一手 IR 新闻稿 URL（S1、S2）在 2026-06-19 复抓返回 HTTP 404/410（link rot / 反爬）→ 这些 headline 数字目前是按 Block-1 研究 pass 的 locked confidence 携带的，并未在本轮从 SEC 一手（10-K / 10-Q）重新确认。** 这不是"数字错了"，而是"数字未被本轮独立坐实"。其次两个口径软肋：**Microsoft PPA 价格 UNDISCLOSED**（Crane 经济无法精确测算）、**post-Calpine 净债/EBITDA ~3.8x 是估算，待 Q1'26 10-Q 审计坐实**。

**与 GOOGL 的关键对比（决定 ceiling 的核心）**：GOOGL 的 ceiling 是 valuation 实质否决（$370 连 bull 都赚不到 8% → 无安全边际 → 封到 WATCH）；**CEG 相反——它是这三家里唯一 HAVE 安全边际的**（−34% 去泡沫 + FERC 尾部已斩 + §45U PTC ~$25/MWh 法定地板）。所以 CEG 的 valuation **不会**把 verdict 否到 WATCH，**完整度给的 STARTER 上限得以保留**。详见 §11。

---

## 1. Source coverage（各模块关键论断能否回到 source_register 的 S-ID / claim_ledger 行？）

抽查每个模块的核心论断 → 追溯 source_id / claim_id：

| 模块 | 抽查的关键论断 | 回挂 source_id / claim_id | 判定 |
|---|---|---|---|
| business_model | 最大美国 merchant、~22 GW 核电 ~95% CF、PPA 新利润杠杆、PTC 地板 | C020/C021、C004、C013、C026（S1/S7/S12）| ✅ 悬空=0 |
| financial_quality | FY25 adj EPS $9.39、FCF ~$1.3B、post-Calpine ~3.8x、买回 $5.0B | C002/C003/C011/C008（S1/S2/S3）| ✅ 估算项明标 ESTIMATED |
| value_chain_map | 利润在 generation node、买方 motivated、capex +77% ~$725B | C020、C025（S1/S8）| ✅ 结构推断标注 |
| moat_map | 7 行护城河逐条挂证据；Network/Brand 诚实降级 | 每行带 C0xx | ✅ Weak 项降级 |
| bottleneck_map | 8 行 bottleneck 表逐行挂证据；FERC 已 defused、PTC 地板 | C022/C015/C013/C019/C026/C011 | ✅ 未臆造数字 |
| operator_underwriting | CEO/治理、Calpine 条款、LS Power 剥离、买回/分红 | C014/C024/C008（S2/S3/S4/S11）| ✅ 未入 pack 项明标"do not invent" |
| inversion_map | 5 kills + (*) 第 6 路径，逐条挂证据 + 当前读数 | 每条带 C0xx | ✅ |
| valuation | $274.06、~24x fwd、peer 16–18x、Street $300–390 | C027/C028（S9）+ scenario_model | ✅ 非 filed 数标 needs_audit |

**结论**：source coverage **强**。逐模块抽查未发现"悬空关键论断"（=有数字/判断却无 source_id）。所有数字唯一来源=`claim_ledger.csv`，结构性推断（如"buyers price-insensitive""supply curve can't respond"）一律就地标〔结构推断〕并进 open gaps。

**但本研究 source coverage 的 #1 软肋（CEG-specific，builder 已自录）—— 最重要的审计发现，见 §4**：
- **S1（FY2025 release）与 S2（Q1'26 8-K/earnings）的一手 IR/PR URL 在 2026-06-19 自动复抓返回 HTTP 404/410**（constellationenergy.com / stocktitan.net 的 link rot + 反爬）。`source_register.md` 行 26 已诚实记录："headline figures 是 Block-1 pass 预锁、内部一致、按 pack 赋予的 HIGH confidence 携带；下次 review 须对 SEC-filed 10-K（FY2025）/ 10-Q（Q1'26）重新确认。"
- **含义**：C001–C008（FY25 + Q1'26 全部 headline 财务，含 revenue $25.5B/$11.1B、adj EPS $9.39/$2.74、FCF $1.3B、CF 94.7%/92.3%、买回 $5.0B）当前是**"locked，未由 SEC 一手在本轮重新坐实"**。S2 在 register 里标 A1/A2，但实际拉取的是 stocktitan 的 8-K 镜像而非 SEC EDGAR 原件且已 404。**这是整份研究最该补的一手缺口**——数字大概率正确（与 guidance、Street、各模块内部勾稽一致），但"primary re-confirmation"这一步未完成。

**次软肋**：valuation 的 $274.06 / ~24x / peer 倍数来自 stockanalysis.com（S9，B2 aggregator），非 A1，且 C027/C028 状态本就标 `needs_audit`。处理正确（未当 A1 用），但它是整个估值三角的输入锚，回流须交叉核对。

---

## 2. 无 source_id 的关键 claim

逐模块扫描"作为论断使用、却无 source_id 也无证据级标注"的 claim：**未发现裸奔的关键 claim。** 所有 28 条 claim 都在 ledger 内挂了 S-ID；非 filed 数字落在以下已标注的桶里，不算违规：

- **ESTIMATED（待 10-Q 坐实）**：post-Calpine 净债 ~$21.6B / ~3.8x（C011，status=`disputed`）、combined FCF。financial_quality §watch-1 + valuation §discipline + model_assumptions 三处均明标"ESTIMATED pending Q1'26 10-Q"。**合规（透明），但它同时是 kill (c)、Klarman 下行论、leverage watch 的共同支点，回流补料须用 10-Q 现金流量表/资产负债表坐实并把 C011 从 disputed 升 verified。**
- **UNVERIFIED（公司未披露）**：Microsoft PPA 价格（C013，status=`partial`，"existence HIGH / price UNVERIFIED"）。business_model、bottleneck_map、moat_map、valuation、model_assumptions 全部就地标"undisclosed → Crane 经济不可精确测算 / Crane 上行已被 MSFT capped"。**处理正确——从未拿一个杜撰价格当 EVIDENCE。**
- **needs_audit（aggregator 源）**：C027/C028 全部市场数据/peer 倍数/Street 目标（来自 S9）。valuation 顶部已声明"Multiples are aggregator-sourced (stockanalysis.com), treat as ±"。
- **〔结构推断〕**（行业机制）："buyers price-insensitive""supply curve cannot respond on AI's horizon""greenfield 10–15yr"——均就地标注 + 多由 C022 支撑。

**唯一边缘项**：Meta–Clinton（1,092 MW clean attributes from June 2027）在 facts.md/business_model 里被引用，但 ledger 中**没有独立 claim_id**，仅由 facts.md 段落和 S6/secondary 携带。**处理半正确**——它被当 MED-confidence 二手用、未支撑任何 verdict 级论断，但严格说应补一条 C0xx 入 ledger（P2，见缺口清单 G7）。

---

## 3. 冲突数字 / 模块间口径不一致（重点核 3 项 + 全面扫描）

### 重点核查项 —— 结果：**无实质冲突，但有两处"未披露/估算"必须 IC 知晓**

**(a) Microsoft PPA 价格的处理是否全模块统一？** ✅ **统一为 UNDISCLOSED，无任何模块偷偷给价。**
- business_model §revenue：「MSFT price undisclosed」；moat_map §honest-qual-1：「undisclosed/likely-fixed price → caps CEG's own upside」；bottleneck_map §risk-1：「contracted at an undisclosed (likely fixed) price」；valuation §discipline：「Crane's is locked to MSFT and undisclosed」；model_assumptions §5：「undisclosed → Crane annuity not directly sizeable」。**五处口径完全一致，且都把"价格未知"翻译成同一个结论：Crane 上行已 capped、equity re-rate 靠 next PPA。** 这是本研究最关键的诚实纠偏之一（不把 MSFT headline 当 thesis）。

**(b) post-Calpine 净债/杠杆全模块是否统一标为估算？** ✅ **统一标 ESTIMATED，无模块当已审计数用。**
- facts.md：「post-Calpine ~$21.6B (~3.8x)」标 MED；C011 status=`disputed`、notes=「ESTIMATED pending Q1'26 10-Q」；financial_quality §bridge + §watch-1：「ESTIMATED pending Q1'26 10-Q…the single most important number to confirm」；valuation §discipline + model_assumptions §discipline 均标「estimates until the Q1'26 10-Q」。**口径统一，且一致点名这是"最该确认的一个数"。**

**(c) adj EPS vs GAAP EPS 口径全模块是否统一用 adj 作 franchise 读数？** ✅ **高度统一（最强一致性项）。**
- 抽查全部模块 + facts：凡触及 EPS 的，**无一例外**用 **adj operating EPS** 作 franchise/Street KPI，并标注 GAAP（FY25 $7.40 < adj $9.39 因 mark-to-market；Q1'26 GAAP $4.49 > adj $2.74 因 favorable marks）（C002/C006、financial_quality §bridge、model_assumptions KPI-basis、scenario_model eps_type）。**没有任何模块把 GAAP 的 commodity-mark 摆动当成长读数。** 同时 Q1'26 +64% revenue **每处都标"acquisition artifact, not organic"**（C005、financial_quality §watch-2、value_chain、model_assumptions）——口径纪律到位。

### 全面扫描发现的口径项（非冲突，但需 IC 知晓）

| 项 | 状态 | 处理 |
|---|---|---|
| **carbon-free 占比 90%→58%** | ✅ 一致 | facts kill(c)、C023、moat_map、bottleneck_map、business_model 全用同一对数字，标"purity dilution / partial trigger"。无冲突。 |
| **Crane 容量"~835 MW" vs "~22 GW 核电"** | ✅ 不同口径 | 835 MW=Crane 单机重启；~22 GW=既有核电队列；并列出现不矛盾。 |
| **§45U 地板"~$25/MWh" vs 2027 open"~$34/MWh"** | ✅ 已说明 | C019（地板）vs C026（2027 open 价）；valuation/inversion/bottleneck 一致表述"$34 > $25 floor = cushion, not at floor"。 |
| **EPS basis：bear 12.0（near guide-mid）vs base 13.0/bull 13.8（fwd flex）** | 🟡 判断项 | scenario_model + model_assumptions 明标 bear 跑 guide-mid×merchant 倍数、base/bull flex EPS up；属假设非冲突，但 bear/base 差"主要是 multiple（18x vs 25x）不是 EPS"——见 §9。 |

**§3 结论**：模块间**无实质数字冲突**。28 条 claim 确实吃同一份 facts.md/ledger，纪律到位。两个"未披露/估算"（MSFT 价、post-Calpine 杠杆）不是矛盾，是**已被诚实标注的信息缺口**，IC 须知。

---

## 4. Stale facts（时效性）—— ⚠ **本审计最重要的发现（CEG-specific #1 缺口）**

与 GOOGL 不同（GOOGL 的 stale 是"自描述说模块未做"），**CEG 的 stale 风险在 source 侧——headline 财务的一手链接已腐烂、本轮未从 SEC 重新确认。**

| 项 | 状态 | 严重度 |
|---|---|---|
| **S1（FY2025 release）URL** | 🔴 **2026-06-19 复抓 HTTP 404/410** — headline（rev $25.5B、adj EPS $9.39、FCF $1.3B、CF 94.7%）按 locked confidence 携带，未由 SEC 10-K 本轮重新坐实 | 🔴 高（#1 gap）|
| **S2（Q1'26 8-K/earnings）URL** | 🔴 **同上 404/410**（stocktitan 镜像，非 EDGAR 原件）— headline（rev $11.1B、adj EPS $2.74、CF 92.3%、买回 $5.0B）同样 locked 未重抓 | 🔴 高（#1 gap）|
| **S9（市场数据/peer 倍数）** | 🟠 aggregator（stockanalysis.com）2026-06 快照；C027/C028 状态=`needs_audit`；价格 $274.06 为时点值 | 🟠 中（估值三角输入）|
| **post-Calpine 杠杆 ~3.8x** | 🟠 ESTIMATED，待 Q1'26 10-Q 审计 combined 净债/EBITDA | 🟠 中 |
| 数字本身的"时效" | ✅ 不 stale | FY2025 10-K 周期 + Q1'26 是最新一手周期；FERC（2025-12 + 2026-04）、NRC（2026-06-08）、OBBBA（2025-07）、capex（2026-02）均为最新 |

**含义与 GOOGL 的对比**：
- GOOGL 的数字**已从 SEC 一手坐实**，stale 的只是"研究进度自描述"（元数据，零成本可改）。
- **CEG 的数字本身的一手 re-confirmation 缺了一步**——链接腐烂使 headline 财务停在"locked，未重核"。这是**比 GOOGL 更实质的一手缺口**（GOOGL 缺的是"更长历史序列/更细披露行"，CEG 缺的是"当期 headline 的一手二次确认"）。
- **缓解**：数字大概率正确——它们与 FY2026 guidance（$11–12，C009）、20%+ CAGR target、Street 目标、scenario_model、各模块内部**勾稽一致**，且 source_register 已诚实记录腐烂事实而非掩盖。**这把它从"未验证的裸 claim"降为"locked、待一手二次确认"**——可进 IC，但 P0 回流。

**回流动作（P0）**：从 SEC EDGAR 直接拉 CEG FY2025 10-K + Q1'26 10-Q，把 C001–C008 从"locked（链接腐烂）"升级为"verified A1（EDGAR）"，并把 C011 的 post-Calpine 杠杆从 disputed/ESTIMATED 升 verified。这**不改 verdict**（数字一致），但把整份研究的事实底座从"高可信但未二次确认"补成"一手坐实"。

---

## 5. D1/C2 污染（社媒/KOL 是否混进 EVIDENCE 支撑某模块判断）

**结论：零污染。** 全仓扫描 source_register 与各模块：

- **source_register Tier 方案**明确把 C 级（KOL/video）定义为"narrative only, never a fact"；**实际 register 里根本没有一条 C 级源**——最低也是 S8（B2，FT/CNBC capex 编译）和 S9（B2，stockanalysis aggregator）。✅
- 所有 verdict 级论断由 A1/A2/A3 一手（SEC/IR/FERC/NRC/IRS/statute）支撑；B2 仅用于"行业 capex 量级"（C025，shared-switch demand）与"市场数据/peer 倍数"（C027/C028，且标 needs_audit）——**B2 从未支撑 moat / kill / verdict 的本体判断**。✅
- 无任何雪球/微信/视频/KOL 线索进入证据链。**未出现段永平个人交易、H&H 13F 之类需降权处理的二手持仓信号**（CEG 案与 GOOGL 不同，这里干净到没有这类项）。✅

Gate A"事实/解读/情绪分开"达标，且 CEG 案的污染面比 GOOGL 还小（连 13F-KOL 降权项都不存在）。

---

## 6. Math / Model 错误（重算 scenario_model：EPS × multiple → 价格目标 vs $216/$325/$414）

逐行重算 `model/scenario_model.csv`：

| 情景 | eps_basis | terminal_pe | 模型 implied_price | 重算（eps×pe）| 判定 |
|---|---:|---:|---:|---:|---|
| **Bear** | 12.0 | 18 | 216 | 12.0 × 18 = **216.0** | ✅ |
| **Base** | 13.0 | 25 | 325 | 13.0 × 25 = **325.0** | ✅ |
| **Bull** | 13.8 | 30 | 414 | 13.8 × 30 = **414.0** | ✅ |
| current | 11.5 | 23.8 | 274.06 | 11.5 × 23.83 = **274.05** | ✅（pe 实为 23.83，标 23.8 取整）|
| street_median | n/a | n/a | 370 | Mizuho 300 / KeyBanc 321 / Barclays 358 / UBS 388，median ≈ **370** | ✅ |

**vs 锁定的 $216 / $325 / $414**：scenario_model 三个 implied_price **逐项精确等于** task-LOCKED 的三个数。✅
**vs memo-v1 prose 区间**：memo 写 bear $200–230 / base $300–340 / bull $400+。三个 implied_price（216/325/414）**全部落在各自 prose 区间内**（216∈[200,230]、325∈[300,340]、414∈[400,+)）。✅ model_assumptions §discipline 明确要求"reconciled to land inside the locked memo-v1 ranges"——**勾稽闭环成立**。
**vs $274 的不对称**：bear 216 = −21.2%、base 325 = +18.6%、bull 414 = +51.1%。与 valuation/memo 表述"~−20% / ~+19% / ~+51%"一致。✅

**结论：模型算术全部勾稽，无错误。** 与 GOOGL 的差异：GOOGL 是 owner-earnings DCF（IRR 二分法，10 年中间 payout + 终值），CEG **刻意不做 DCF**（combined FCF 未干净列报 + hedge ratios 未披露 → DCF 是 false precision），改用 **forward adj-EPS × terminal multiple** 三角法。**这是恰当的方法选择**（model_assumptions §why-not-DCF + valuation §why-not-DCF 均论证），但代价是：**估值精度受限于 EPS basis 与 terminal multiple 两个判断变量**，而非可勾稽的现金流（见 §9）。

**一个细节澄清（非错误）**：current 行的 terminal_pe 标 23.8，但 11.5 × 23.8 = 273.7 ≠ 274.06；实际需 23.83 才得 274.05。这是**展示取整 vs 反推精度的正常差异**，不影响结论。建议把 current 行 pe 改为 23.83（可选，低优先）。

---

## 7. 缺一手源

| 缺口 | 当前状态 | 影响 |
|---|---|---|
| **headline 财务的 SEC 一手二次确认**（FY25 10-K / Q1'26 10-Q） | S1/S2 链接腐烂 404/410，按 locked confidence 携带（§4） | 🔴 **#1 gap**——数字大概率对但本轮未一手坐实；C001–C008 待 EDGAR 升 verified |
| **Microsoft PPA 价格** | UNDISCLOSED（C013） | 🔴 Crane 经济不可精确测算；base/bull EPS 上行中"多少是真、多少被 MSFT capped"无法定量 |
| **post-Calpine 净债/EBITDA（审计后）** | ESTIMATED ~3.8x，待 Q1'26 10-Q（C011） | 🔴 kill(c)、Klarman 下行锚、leverage watch 的共同支点；deleverage 证明的起点 |
| **year-by-year hedge ratios** | 未披露（facts open gaps） | 🟠 open-vs-contracted 拆分=近期 EPS 对电价敏感性，无法精确建模 |
| **confirmed NEW（post-Meta）hyperscaler PPA** | 不存在（C013/C021） | 🔴 **单一最大 re-rating catalyst**；equity 从"fair"到"cheap/上修"的唯一钥匙；base case 已假设"1–2 signed"但 0 confirmed |
| **earnings-call transcript（B1）** | 未拉（step0 计划 2–4，实际 0） | 🟠 管理层 Calpine 整合里程碑 / capex ROI 口径的唯一可能来源 |
| **CFO / 完整董事会名册 / Dominguez 薪酬结构** | 不在 pack（operator open items） | 🟡 治理"clean"判断的补强；薪酬是否绑 per-share/ROIC vs scale 未知 |

一手覆盖在**监管/政策/运营事件**侧**完整且最新**（FERC/NRC/IRS/statute/Calpine close/LS Power 全 A2/A3 一手）；缺的集中在**①当期 headline 财务的二次一手确认、②未披露的合同价/hedge、③尚未发生的 NEW PPA catalyst**。

---

## 8. 管理层未验证 claim

**审计意见：管理层 claim 处理得当——本研究主要靠可观察行为，但有两条关键前瞻 claim 是"guided, not realized"，须降权。**

- 用的多是**可观察行为**（~95% CF 实际数、买回实际数 $335M YTD、Calpine 实际成交条款、LS Power 实际签约、DOE loan 实际 close）——operator_underwriting 明确"Evidence-based…not vibes"、open items 标"do not invent"。✅
- **两条关键前瞻 claim（管理层口径，须降权）**：
  1. **「Calpine >20% FY26 EPS-accretive」**（C014）——operator 标"Accretion is guided, not yet realized; requires DOJ/FERC divestitures"；financial_quality 标"credible-but-unproven"。**正确降权为 guided。**
  2. **「20%+ base-EPS CAGR to 2029」**（C010，confidence=MED）——claim_ledger notes 明标"Targeted, not contracted; depends on Crane + Calpine accretion + new PPAs"。**正确降权。**
  3. **「deleverage 3.8x→~2.0x by 2027」**（C011/C024）——全模块标"a forecast until proven / cash not yet in"。**正确降权。**
- **关键未验证缺口（与 GOOGL 同病）**：管理层**未在一手披露里给过 Calpine 整合的量化里程碑、也未给 capex/PPA 的 ROI 门槛框架**。operator open-items + inversion 把"deleverage 证明"列为每季须 verify 项。**审计确认这是真实缺口**——但 CEG 比 GOOGL 轻，因为 CEG 的核心 thesis（既有核电 scarcity rent）**不依赖任何前瞻承诺**，依赖的是已建成的物理资产 + 法定 PTC 地板；前瞻 claim 只影响 Calpine accretion 这条**增量**线，不影响 moat 本体。

---

## 9. 估值假设过激或过松（~24x fwd vs peers 16–18x — 溢价太慷慨？bull 是否靠未签的多个 PPA？）

**审计意见：估值整体偏保守（bear 浅、base 不靠激进 terminal），但有两个 IC 必须压测的偏松点——base/bull 的 terminal multiple，以及 bull 隐含的"多个尚未签的 PPA"。**

**支持"不过激"的证据：**
- 方法本身保守：**不做 DCF**（避免 false precision），bear 直接给 merchant peer 倍数（18x，贴近 VST 16x/TLN 17–18x/NRG 18x）×near-guide-mid EPS（12.0）→ $216，**不靠任何乐观假设救下行**。
- bear 是"multiple-compression on an intact franchise，不是 earnings collapse"——因 §45U PTC ~$25/MWh 法定地板 + 2027 open ~$34/MWh，**下行被立法封底**。这是 GOOGL **没有**的结构（GOOGL bear 还有 DOJ 拆分尾部未压进）。
- Street 全员目标 $300–390（median $370）**全部 > 现价 $274**，连最低 Mizuho $300 也高于现价——即外部一致预期认为现价 over-sold，base 325 反而**低于** Street median 370（保守）。

**可被质疑的偏松点（IC 应压测）：**
- **~24x fwd 的溢价是否太慷慨？** CEG ~24x vs merchant peers 16–18x = **~6–8 turn 溢价**。bull 给到 **30x**。多头辩护=un-buildable 核电 moat + PTC-floored PPA annuity；空头说"~17x 才是对的 merchant 倍数"（bear 即采此）。**审计判断**：base 维持 ~24–25x 的前提是"premium-to-peers 持续"——这是**判断不是证据**。若 Calpine gas mix（purity 90%→58%）让市场用 merchant-gas 倍数重估全实体，base 倍数可能压向 18–20x，base 价随之下修。**bear/base 的差额主要是 multiple（18x vs 25x）不是 EPS**（model_assumptions §3 自承），意味着估值的胜负手是"市场愿不愿给溢价"，比 GOOGL（胜负手是不可观测的 capex 拆分）更**主观/情绪驱动**。
- **bull 是否靠未签的多个 PPA？** ✅ **是，且已诚实标注。** scenario_model bull driver 明写"Multiple premium PPAs + uprates + 2nd restart"；model_assumptions §forecast-drivers bull 行"New hyperscaler PPA = multiple"——而 facts/inversion 明确"**no confirmed NEW (post-Meta) PPA**"。**所以 bull $414 建立在 0 confirmed 的多个 PPA 之上**——这是 bull 的核心脆弱点，IC 须知"bull 不是基准、是 catalyst-dependent 的乐观路径"。**好在 bull 不被用来 rescue 现价**（valuation §discipline："Do not let a 30x bull multiple rescue the present"）——现价 $274 由 base/floor 支撑，不靠 bull。
- **base 已假设"1–2 new PPAs signed"** —— 但今天是 0 confirmed。**base case 本身已含一个未兑现的 catalyst 假设**。这是 base 325（+19%）的隐含前提，IC 须知"若 0 PPA 且 deleverage 顺利，落点更靠 base 下沿 $300 而非 $325"。

**净判断**：与 GOOGL 相反——GOOGL 是"假设偏保守、结论仍是无安全边际（贵）"；**CEG 是"假设偏保守、bear 被立法封底、结论是 fair-not-cheap 但 HAVE 安全边际"**。没有"为得出买入而拔高假设"的痕迹（bull 不救现价）；偏松点（base/bull terminal multiple + base 隐含 1–2 PPA）只影响**上行幅度**，不动摇**下行有底**这一核心——而下行有底正是 CEG verdict 不被否到 WATCH 的原因。

---

## 10. 风险未量化

| 风险 | 量化程度 | 缺口 |
|---|---|---|
| (c) Calpine deleverage stall（唯一真正 live kill） | 🟡 半量化 | 有路径（3.8x→2.0x via $5B 资产出售）+ LS Power $5B 已签，但 **post-Calpine 净债/EBITDA 是 ESTIMATED**、accretion 是 guided→真实 deleverage 速度未量化 |
| (*) capped flagship + no new PPA（"quality trap"） | 🟡 半量化 | Crane→MSFT 价 UNDISCLOSED → "capped 多少"无法量化；NEW PPA 0 confirmed → "dead money at 24x" 的概率/时长未量化 |
| (b) 电价向 PTC 地板压 | ✅ 充分量化（封底） | ~$25/MWh 地板（C019）+ 2027 open ~$34/MWh（C026）→ cushion 明确；**唯一被立法封底的风险** |
| (a) FERC co-location | ✅ 已 defused（定性+事件） | 5-0 enabling order（C015）+ front-of-meter flagship（C013）；残留=最终 PJM 定义诉讼（C016），低概率、industry-BTM、flagship insulated |
| (d) PTC repeal | ✅ 已 defused | 存活 OBBBA、FEOC-only（C019）；early warning=新立法 |
| (e) shared-switch hyperscaler capex | ✅ 量化（+77% ~$725B） | C025；kill not firing；监控=2027 capex guide 是否减速 |
| Microsoft PPA 价格风险 | 🟠 弱量化 | UNDISCLOSED → 整个 Crane annuity 不可直接 size；影响 base/bull 上行的"真 vs capped" |

**结论**：风险**识别完整**（5 pre-registered kills + 第 6 路径全部命中并打分：a defused / b floored / c partial / d not-triggered / e accelerating），**封底风险（b）已立法量化**——这是 CEG 相对 GOOGL 的结构优势（GOOGL 的下行尾部 DOJ 拆分**未**压进 bear）。**未充分量化的三个都集中在同两个不可观测变量上**：①post-Calpine 真实 deleverage 速度（待 10-Q）、②MSFT PPA 价 + NEW PPA timing（公司未披露/事件未发生）。这三个恰是 kill(c) + 路径(*) 的本体，**已正确进 open gaps + monitor triggers**。**对 IC：这些是"等证据/等催化"的灰区，不是被忽略的盲区——且都不触及 moat 本体或下行地板。**

---

## 11. Completeness % 粗估 + Verdict Ceiling

### 11.1 完整度加权（事实线 / 理解线 / 决策线，宁低勿高）

| 线 | 权重 | 子项完成度 | 加权得分 |
|---|---:|---|---:|
| **A. 事实线**（source→ledger→facts→audit） | 35% | source_register（S1–S12）+ 28 claim 全挂源 + kill-scorecard 三处一致；**扣分：S1/S2 一手链接腐烂、headline 财务未由 SEC 二次坐实（#1 gap）、C011 杠杆 ESTIMATED、C027/C028 needs_audit、Meta-Clinton 缺独立 claim_id** | 25/35（71%）|
| **B. 理解线**（business→value chain→moat→operator→inversion） | 35% | **5 模块全完成且高质量**；LEAD 问题（durable rent vs FERC-hostage）已正面回答；扣分：moat 中 contracts/integration 项 Medium（hedge 未披露、Calpine 未证）、MSFT 价 UNDISCLOSED 使 PPA annuity 不可 size | 29/35（83%）|
| **C. 决策线**（valuation→MoS→verdict→monitor） | 30% | EPS×multiple 三角 + bear/base/bull 勾稽通过 + MoS 表 + memo STARTER；扣分：**未做 owner-earnings DCF（方法所限，非偷懒）、base/bull terminal multiple 是判断、base 隐含 1–2 未签 PPA、monitor.md 未独立成文（triggers 散在 memo/inversion）** | 22/30（73%）|

**加权完整度 ≈ 25+29+22 = 76/100 → 落点 **76%**（与 memo-v1 LOCKED 的 76/100 一致）。**

> 说明（宁低勿高）：事实线因 #1 gap（一手链接腐烂、headline 未二次坐实）扣得最重（71%）——这是 CEG 区别于 GOOGL 的特有失分（GOOGL 事实线 80%，因其数字已 SEC 坐实、只缺更长序列）。理解线强（5 模块齐 + LEAD 已答 + kill 全打分）。决策线因方法局限（无 DCF）+ 倍数判断扣到 73%。**净 76/100，verdict band = STARTER（60–80）。**

### 11.2 Verdict Ceiling（套表 + 叠硬规则取更低）

**第一步：完整度表**
- 76/100 → 落在 **60–80 = STARTER** 区间。

**第二步：硬规则（buy_side_research_department §4）**

| 硬规则 | 是否触发封顶？ | 确认 |
|---|---|---|
| 没有 valuation.md / 安全边际 → 最高 WATCH | **❌ 不触发** | valuation.md **已完成**（EPS×multiple 三角 + bear/base/bull + MoS 表 + Street cross-check）→ 解除 |
| 没有 inversion_map.md → 最高 WATCH | **❌ 不触发** | inversion_map **已完成**（5 kills + (*) 路径 + 当前读数）→ 解除 |
| 没有 operator_underwriting.md → 最高 STARTER | **❌ 不触发** | operator **已完成**（People Map + 资本配置 + 治理 flags）→ 解除 |
| 社媒是主要证据 → 最高 INFO-GAP | ❌ 不触发 | 零 D1/C2 污染、register 无 C 级源（§5）|
| 不了解生意怎么赚钱 → REJECT/INFO-GAP | ❌ 不触发 | business_model 完整清晰（merchant nuclear + PPA 杠杆 + Calpine）|

**→ "缺模块"硬规则全部解除。**

**第三步：valuation 的实质结论（与 GOOGL 决定性分叉的地方）**
- **GOOGL**：valuation 实质=$370 无安全边际（bull IRR +5.2% < 8%）→ Buffett 第 5 节规则"无安全边际 → 最高 WATCH"→ **把 ceiling 从 STARTER 否到 WATCH**。
- **CEG**：valuation 实质=$274 是 **fair-not-cheap 但 HAVE 安全边际**——理由三条：**①−34% 去泡沫（>35x→24x，froth cut not moat）；②FERC 尾部已斩（5-0 enabling order）+ PTC ~$25/MWh 法定地板（bear 被立法封底，216 只跌 −21%）；③Street 全员目标 > 现价**。所以 **valuation 不触发"无安全边际→WATCH"否决**——bear 浅且有底、base/bull 偏上、不对称为正（−21% / +19% / +51%，三家最佳）。
- **结论：CEG 的 valuation 不把 ceiling 压低 → 完整度给的 STARTER 得以保留。**

**第四步：取更低 → 最终 Verdict Ceiling = `STARTER`**

| 来源 | 给出的上限 |
|---|---|
| 完整度 76% | STARTER |
| 缺模块硬规则 | （全部解除，不封顶）|
| **valuation 实质：fair-not-cheap 但 HAVE 安全边际**（−34% + FERC 斩 + PTC 地板 + Street>现价）| **不否决，STARTER 保留** ← 与 GOOGL 在此分叉 |
| #1 gap（headline 未二次坐实）+ MSFT 价未披露 | 不压低字母，但**封住向 CORE 的升格**（须先补一手 + NEW PPA）|

### Ceiling Rationale（为什么是 STARTER，且与 GOOGL 明确对比）

**GOOGL：ceiling = WATCH——"研究做扎实了、结论是好公司但价格太贵（无安全边际）"。**
**CEG：ceiling = STARTER——"研究做扎实了（76/100）、结论是好公司且当前价 HAVE 安全边际"。**

**决定性差异（必须对 IC 讲清）**：两家都是"好生意 + 研究扎实"，但 GOOGL 在 $370 **无**安全边际（连 bull 都赚不到 8%、下行尾部 DOJ 拆分未压进），CEG 在 $274 **有**安全边际（FERC 尾部已 empirically 斩断 + §45U PTC 立法封底使 bear 只 −21% + −34% 已去掉 >35x 泡沫 + Street median $370 远高于现价）。**所以同样"扎实",GOOGL 的 valuation 把 ceiling 否到 WATCH，CEG 的 valuation 让 ceiling 停在 STARTER。** CEG 是这三家（GEV/VRT/CEG）里**唯一**有安全边际的 → memo rank #1/3 成立。

**STARTER 而非 CORE 的封顶理由**：①#1 gap——headline 财务一手链接腐烂、本轮未从 SEC 二次坐实（§4）；②MSFT PPA 价 UNDISCLOSED → Crane 上行已 capped、annuity 不可 size；③NEW（post-Meta）PPA **0 confirmed**——equity re-rate 的钥匙未到手；④Calpine deleverage 是 forecast（杠杆 ESTIMATED 待 10-Q）。**这四条把 verdict 钉在"试仓 STARTER、scale 需催化"而非"back-up-the-truck CORE"。**

---

## 暴露缺口清单（按优先级）+ 回流到哪一步 + 给 IC 的质询点

| # | 缺口 | 优先级 | 回流步骤 | 具体动作 |
|---|---|---|---|---|
| **G1（P0）** | **headline 财务的 SEC 一手二次确认**（S1/S2 链接 404/410、C001–C008 locked 未重核） | 🔴 **P0（#1 gap）** | Step 1→Step 6(ledger) | 从 EDGAR 拉 CEG FY2025 10-K + Q1'26 10-Q，把 C001–C008 升 verified A1；把 C011 post-Calpine 杠杆从 disputed/ESTIMATED 升 verified |
| **G2（P0）** | **NEW（post-Meta）hyperscaler PPA catalyst**（0 confirmed，单一最大 re-rating 钥匙；base 已假设 1–2 signed） | 🔴 **P0** | Step 12 monitor | 跟踪任何新 AI PPA 公告 + 定价；这是 STARTER→CORE 升格的主催化 |
| **G3（P0）** | **Calpine deleverage 证明**（3.8x→2.0x 是 forecast；accretion guided 未实现） | 🔴 **P0** | Step 2→每季 10-Q | 用 Q1'26 10-Q 坐实 combined 净债/EBITDA；逐季验 LS Power 现金到账 + 后续 divestiture + accretion 兑现 |
| G4 | **Microsoft PPA 价格**（UNDISCLOSED → Crane annuity 不可 size、上行 capped 多少未知） | 🟠 P1 | Step 1（若日后披露）| 监控 10-K/合同披露；当前正确标 UNVERIFIED，不臆造价格 |
| G5 | **year-by-year hedge ratios**（open-vs-contracted 拆分 = EPS 对电价敏感性） | 🟠 P1 | Step 2/Step 8 | 拉 10-K hedge 披露 / earnings-call；收敛近期 EPS 建模 |
| G6 | **earnings-call transcript（B1）**（管理层 Calpine 里程碑 / capex ROI 口径） | 🟠 P1 | Step 6(operator) | 拉 Q1'26 及历史 transcript |
| G7 | **Meta-Clinton 补独立 claim_id + CFO/董事会/薪酬结构** | 🟡 P2 | Step 1/Step 6 | 给 Meta-Clinton 一条 C0xx 入 ledger；从 proxy 补 CFO/board/薪酬（验是否绑 per-share/ROIC）|
| G8 | **monitor.md 独立成文**（triggers 现散在 memo/inversion） | 🟡 P2（IC 后）| Step 12 | 把 5 个 monitor triggers + kill-scorecard 收成独立 monitor.md |

---

## 给 IC 的提示（本审计放行，IC 必须正面回应下列质询点）

放行结论：证据扎实、口径自洽、模型勾稽、无污染——**可进 IC Panel**，verdict 上限锁 `STARTER`（不被 valuation 否到 WATCH，因 HAVE 安全边际；也不升 CORE，因四条封顶）。IC 必须正面回应：

1. **#1 gap 质询（最硬）**：FY2025/Q1'26 的 headline 财务一手 IR 链接已 404/410，C001–C008 是 **locked、本轮未从 SEC 二次坐实**。IC 须明确："我们接受'数字与 guidance/Street/各模块勾稽一致 → 大概率正确 → 可进 IC、P0 补一手'，还是要求先补 EDGAR 再裁？"（审计建议：可放行 STARTER，但 G1 列 P0，CORE 升格前必须补。）
2. **安全边际质询（与 GOOGL 的分叉点）**：CEG 与 GOOGL 都"好生意+扎实"，但 GOOGL 在 $370 **无**安全边际（bull 也赚不到 8%）→ 否到 WATCH；CEG 在 $274 **有**安全边际（FERC 斩 + PTC 立法封底 bear 仅 −21% + −34% 去泡沫 + Street median $370>现价）→ STARTER 保留。**IC 须确认这个对比成立、且 CEG 确实是三家里唯一有边际者（rank #1/3）。**
3. **倍数质询**：~24x fwd vs peers 16–18x = ~6–8 turn 溢价，bull 给 30x。**base/bear 的差额主要是 multiple（25x vs 18x）不是 EPS**——估值胜负手是"市场愿不愿给溢价"，比 GOOGL 更主观。IC 须答："若 Calpine gas mix 让市场用 merchant-gas 倍数重估，base 倍数压向 18–20x、base 价下修，STARTER 仍成立吗？"（审计：成立——下行有 PTC 地板，bear 仍 −21%。）
4. **bull 靠未签 PPA**：bull $414 建立在"multiple premium PPAs（0 confirmed）"之上，base 325 也隐含"1–2 signed（今天 0）"。**IC 须知 bull 是 catalyst-dependent 乐观路径、不救现价；base 含一个未兑现催化假设**——若 0 PPA，落点靠 base 下沿 $300。
5. **(*) quality-trap 路径**：Crane 上行已 capped 给 MSFT（价未披露）+ NEW PPA 0 confirmed → 即便 moat 完好，equity 可能"dead money at 24x"。**IC 须确认 STARTER（试仓非满仓）正是为这条路径设计的 sizing**——catalyst（NEW PPA）到手前不 scale。
6. **kill-scorecard 一致前提**：IC 读 facts/inversion/memo 时，kill 状态以本 audit 复核一致的 **a defused / b floored / c partial / d not-triggered / e accelerating** 为准；唯一真正 live 的是 (c) Calpine 执行 + (*) capped-flagship-no-new-PPA。
