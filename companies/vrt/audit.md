# VRT Audit / Quality Gate (Step 7 — pre-IC adversarial QA)

Last updated: 2026-06-19
Auditor stance: **对抗性找漏洞**（adversarial hole-punching），不是再夸一遍。This is the independent quality gate that sits **between** the analysis modules (Step 2-8) and the IC Panel (Step 8/10). 它不新增事实、不裁多空，只检验证据是否扎实、模块间是否自洽、缺口在哪、最高允许给什么 verdict。

Inputs audited: `facts.md`, `source_register.md`（S1–S9）, `claim_ledger.csv`（33 行）, 8 analysis modules（financial_quality / business_model / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map / valuation）, `model/{scenario_model.csv, model_assumptions.md}`, `memo-v1.md`, `monitor.md`, `research_status.md`。
Checklists applied: 买方研究 OS §9（审计 11 项 + verdict ceiling 表）+ 硬规则（缺 valuation/inversion/operator 封顶表）。
Sibling baselines（同批 3/3）：[[CEG]]（contracted-floor）/ [[GEV]]（equipment oligopoly）/ **VRT（highest beta, no floor）**。

---

## 0. 一句话审计结论

证据工程质量**高**：33 条 claim 逐条挂 source_id，财务数字全部回挂一手 A1/A2（VRT Q1'26 8-K/release S1、FY25 release S3、IC deck S4），口径纪律（organic vs total、adj 非 GAAP、backlog 可取消性、FCF 转化）在 8 个模块间**高度一致**，scenario_model 算术**逐项勾稽通过**，无 C（KOL/视频）污染。**但有一个压倒一切的审计发现 + 两个次级问题**：①**唯一最重要的发现——"backlog silence"**：VRT 在一个 **+252% organic orders / book-to-bill ~2.9x 的爆炸性 Q4 之后，于 Q1'26 主动撤回了 headline 季度 orders / book-to-bill / backlog**（claim_ledger **C012，UNVERIFIED**），只给"orders up YoY / backlog elongated"的定性话术。**这是用来 underwrite kill-criterion (a) 的最干净需求计量表，偏偏在它最要紧的时点消失了。** ②估值倍数与 Street 目标价均为**聚合器来源**（S6/S7，`needs_audit`），一手交叉核对未做；③scenario_model 的**点估计（$182/$292/$360）与 valuation.md 正文的区间（bear $170–230 / base $340–380）存在展示口径差**，需对齐。三者叠加：**ceiling = WATCH**，且 actionable lean **比 info 完整度给的 STARTER 还低一档**——理由不是"信息不足/缺模块"，而是"**最关键的需求信号被管理层关掉了 + ~48× 全估值无安全边际**"。

---

## 1. Source coverage（各模块关键论断能否回到 facts 的 source_id？）

抽查每个模块的核心论断 → 追溯 source_id：

| 模块 | 抽查的关键论断 | 回挂 source_id | 判定 |
|---|---|---|---|
| financial_quality | FY25 +26% organic / 20.4% margin / $1.887B FCF；Q1'26 20.8%(+430bps)/EPS $1.17/FCF $653M；backlog WITHHELD | C001–C004 / C007–C012（S1/S3） | ✅ 悬空=0 |
| business_model | 三条线 power/thermal/services；NVIDIA stack；~75% 下游 4 家 capex | C016–C019 / C023（S1/S2/S5） | ✅ 结构推断标 inferred |
| value_chain_map | 利润在 integration 层、component 层商品化、buyer power High | C022 / C033（S5/S7） | ✅ |
| moat_map | design authority、broad-line 唯一、#1(tied) 11.3% 份额、800V DC | C018–C020 / C017（S5/S7） | ✅ Weak 项诚实降级（duopoly 非 monopoly） |
| bottleneck_map | 拥有 integration bottleneck / 供货进 component bottleneck / shared switch | C021–C025 / C033 | ✅ 三层拆分逐行挂证 |
| operator_underwriting | Albertazzi 自 2023、serial beat-raise、撤回 orders 披露、net cash $0.76B | C026–C028 / C012（S4/S2/S6） | ✅ 8 维 + life-arc 逐项挂证 |
| inversion_map | D/A/B/C 失败路径、kill-criteria 现状 (a)YELLOW (b/c/d)GREEN | C012/C023/C025/C032 等 | ✅ 每条带证据 + early warning |
| valuation | $333.05、~48× fwd、bear/base/bull、Street +13%、MoS 表 | C029–C031（S6 needs_audit）+ scenario_model | ⚠ 见 §3/§9：倍数 needs_audit + 点估计/区间口径差 |

**结论**：source coverage **强**。逐模块抽查未发现"悬空关键论断"（=有数字/判断却无 source_id）。所有模块都遵守"数字唯一来源=facts.md/claim_ledger"的纪律，结构性推断（C023/C024/C033）一律就地标 `inferred` 并进 open questions。

**唯一软肋**：valuation 的全套倍数（C029）与 Street 目标价（C031）来自 stockanalysis.com 聚合器（S6），状态 `needs_audit`，**无一手 10-Q 资产负债表 / 干净 consensus feed 交叉核对**——见 §3/§7。

---

## 2. 无 source_id 的关键 claim

逐模块扫描"作为论断使用、却无 source_id 也无证据级标注"的 claim：**未发现裸奔的关键 claim。** 所有非 filed 数字都落在以下三类已标注的桶里，不算违规：

- **WITHHELD（C012，UNVERIFIED）**：Q1'26 orders / book-to-bill / backlog。**这是本案最特殊的一项——它不是"我们没拉到"，而是"公司主动不披露"。** claim_ledger 明确：FACT of non-disclosure 是 high confidence（S1 release 里确实没有、S2 call 里管理层明确只给定性），但**底层 orders 数字本身从公开源 UNVERIFIABLE**。处理正确：它**从未被当 EVIDENCE 用**，反而被当作 kill-criterion (a) 的 YELLOW 触发 + 头号 open question，贯穿 inversion/monitor/operator/financial_quality/research_status 五处。**审计意见：这是教科书级的"把缺口当缺口处理"，不是把缺口藏起来。**
- **inferred（分析推断，已明标）**：~75% 下游集中度（C023）、backlog 可取消 ~12–18 月（C024）、"owns integration / supplies into component"综合判断（C033）。均标 `inferred`、来源为 backlog 性质 + 客户结构 commentary，非单一披露行。
- **needs_audit（聚合器，待核）**：全套倍数（C029）、Street 目标价（C031）。均明标 `needs_audit`，见 §3/§7/§9。

**§2 结论**：无裸奔 claim。最敏感的 C012 被当作"已知的未知"诚实地反复标注，而非伪装成事实——这是本案证据纪律最关键的一关，过。

---

## 3. 冲突数字 / 模块间口径不一致（重点核 3 项 + 全面扫描）

### 重点核查项 —— 结果：1 项一致、2 项需对齐（非实质冲突，但需 IC 知晓）

**(a) backlog / orders 的描述在各模块是否一致？** ✅ **一致（最强的一致性项）。**
- FY25 backlog **$15.0B(+109%)**、Q4 B2B **~2.9x**、Q4 organic orders **+252%**、TTM **+81%**：facts/claim_ledger/financial_quality/bottleneck/inversion/operator **逐处一致**（C004/C005）。
- Q1'26 **WITHHELD**：所有触及该点的模块**无一例外**写"撤回 + 仅定性 + 在 +252% Q4 之后显得 conspicuous"（financial_quality 红旗1、bottleneck §3.3、operator 治理旗、inversion 路径 A、monitor 头号变量）。**没有任何模块把"orders up YoY"的定性话术当成 ≥1.0 的证据。** 这是本案最重要的口径纪律，达标。

**(b) 估值倍数 ~48× vs scenario_model 隐含 52.4× 是否统一？** ⚠ **存在展示口径差，需注脚对齐。**
- valuation.md / facts / memo 全篇用 **"fwd P/E ~48–49x"**（on FY26E EPS $6.35）。
- 但 `scenario_model.csv` 的 `current` 行写 forward_pe = **52.4x**（333.05 / 6.35 = 52.45，as-reported 基准）。重算确认：**333.05 / 6.35 = 52.4x**，而 "48–49x" 对应的隐含 EPS ≈ $6.8–6.9（即把 FY26 上沿/含某调整后口径）。
- **判定：非实质冲突**（两者都围绕"~50× 量级、priced for perfection"这一结论），但 **48–49x 与 52.4x 的差异未在任一文件显式说明来自不同 EPS 基准**。**回流动作（P1）：在 valuation.md 与 scenario_model 注脚里写明"48–49x 用 EPS≈$6.8 口径 / 52.4x 用 FY26E $6.35 as-reported 口径"，消除读者困惑。** 对结论（无安全边际）无影响——两个口径都远在便宜之上。

**(c) scenario 点估计 vs 区间是否自洽？** ⚠ **点估计与正文区间需对齐（展示差，非算术错）。**
- `scenario_model.csv`：bear **$182**（6.50×28）、base **$292**（6.35×46）、bull **$360**（7.20×50，FY27E 另给 $430–480）。**逐项重算勾稽通过**（见 §6）。
- valuation.md 正文 / memo 表：bear **$170–230**、base **$340–380**、bull **$430–480**。
- **差异来源**：CSV 是"单点中枢"（base 用 46× × $6.35），正文 base $340–380 是"45–48× × FY26→FY27 成长 EPS"的区间（即把 FY27 EPS 长进倍数里）。**bear $182（点）落在正文 $170–230（区间）内 ✓；bull $360（近端点）+ $430–480（FY27E）与正文一致 ✓；唯 base $292（点，纯 FY26 EPS×46）低于正文 $340–380（区间，含 FY27 成长）——这是"是否把 FY27 成长计入 base"的口径选择，不是矛盾。**
- **回流动作（P1）：在 scenario_model 注脚明确"base $292 = 纯 FY26E EPS×46 的静态中枢；$340–380 = FY27 EPS 长入 45–48× 的动态区间"，并让 memo/valuation 两处口径互相指认。** 本 audit 与父任务 LOCKED 一致采用**点估计 $182/$292/$360（+FY27E $430–480）**为主锚。

### 全面扫描发现的口径项（非冲突，但需 IC 知晓）

| 项 | 状态 | 处理 |
|---|---|---|
| **organic vs total** 营收增速（Q1'26 +30% total / +23% organic） | ✅ 全模块统一用 organic 作干净读数 | financial_quality/business_model/valuation 均标 organic 优先 |
| **adj（非 GAAP）口径** margin/EPS/FCF | ✅ 全程标 "adjusted = management non-GAAP" | model_assumptions 明示；无把 adj 伪装成 GAAP |
| **net cash ~$0.76B** 来自 S6 聚合器 | 🟡 未对 10-Q 核 gross cash/debt | research_status open question 已挂（C028）；定性结论（net cash, 非杠杆）不受影响 |
| **EMEA −29% Q1'26** 单季 | ✅ 一致引用为"非普遍免疫"证据（C008） | financial_quality 黄旗2 / inversion 路径 D early warning |

**§3 结论**：模块间**无实质数字冲突**；(a) backlog 口径完全统一。需 IC 知晓的两项 **(b) 48× vs 52.4×、(c) 点估计 vs 区间** 都是**展示口径差**而非矛盾，已开 P1 回流动作。这反映 8 个模块确实都吃了同一份 facts.md/claim_ledger，纪律到位。

---

## 4. Stale facts（时效性）

数字本身不 stale（FY2025 release + Q1'26 8-K/call + 2026-05 IC deck，均为最新一手，截至 2026-06-19）。价格 $333.05 与 52 周高低（$380/$110）为 2026-06 聚合器读数，标注 volatile，可接受。

**自描述一致性**（与 GOOGL 不同，VRT **未发现 stale "未做/封顶因缺模块"自描述**）：`research_status.md` 行 14–16 已正确写"Full pipeline (Blocks 1–9) complete (v1)"、verdict WATCH、binding gap = C012；`step0_plan.md`/`facts.md`/`memo-v1.md` 三个先写文件被声明"preserved unchanged"且与后续 Block **一致**（同 verdict、同 binding gap、同 kill 现状 a→YELLOW / b,c,d→GREEN）。**审计确认这条 consistency 声明属实**（见 §11 一致性核对）。**故本案无 GOOGL 式的"stale 元数据需批量更新"问题——这是 VRT 文档纪律强于 GOOGL 初稿的一点。**

唯一时效注意：**C012 的状态本身是时间敏感的**——它在 **Q2'26 财报（~2026-07）** 会被"重新披露 ≥1.0 / 继续沉默 / 重新披露 <1.0"三种结果之一解析。**本 audit 的 WATCH ceiling 显式绑定在"Q2'26 之前 orders 信号不可得"这一时效条件上**（见 §11 ceiling rationale）。

---

## 5. C 污染（社媒/KOL/视频是否混进 EVIDENCE 支撑某模块判断）

**结论：零 C 污染。** 全仓扫描所有 B2/外部源的使用位置：

- 本案**无任何 C 级（KOL/视频）源**进入 source_register（S1–S9 全为 A1/A2/B1/B2）。research_status Pollution Check 已勾"No KOL as fact (no video sources in this case)"。✅
- **S8 "Backlog Silence"（Seeking Alpha，B2）** 的处理是关键检验点：它**没有被当作 orders 数字的来源**（orders 数字仍是 UNVERIFIED/C012），而是**仅作为"独立第三方也注意到这次撤回"的旁证**，用于支撑"撤回是 discretionary 选择、值得当 soft negative"这一**定性**判断。inversion/operator/financial_quality 三处引用 S8 均限于此定性用途。**审计意见：处理正确——B2 评论用于 flag 一个披露行为，而非替代被撤回的硬数字。**
- **S6/S7/S9（聚合器/行业/press，B2）** 仅用于市场数据（价格、倍数、52 周区间、份额、hyperscaler capex），且倍数/目标价已标 `needs_audit`（§7）。无任一模块的**生意/护城河判断**由 B2 评论支撑。✅

无任何模块判断由社媒/视频/论坛线索支撑。"事实/解读/情绪分开"达标。

---

## 6. Math / Model 错误（重算 scenario_model 勾稽）

独立重算全部关键数字（PowerShell 验算，不留脚本）：

| 检查 | 模型值 | 重算值 | 判定 |
|---|---|---|---|
| Bear price = 6.50 × 28 | 182 | **182.0** | ✅ |
| Base price = 6.35 × 46 | 292 | **292.1** | ✅ |
| Bull price = 7.20 × 50 | 360 | **360.0** | ✅ |
| current implied fwd P/E = 333.05 / 6.35 | 52.4 | **52.45** | ✅（= scenario `current` 行 52.4，**但 ≠ 正文 "48–49x"，见 §3(b)**）|
| Street upside = 377/333.05 − 1 | +13% | **+13.2%** | ✅ |
| Off 52-wk low = 333.05/110 − 1 | +203% | **+202.8%** | ✅ |
| Off 52-wk high = 333.05/380 − 1 | −12% | **−12.4%** | ✅ |
| Bear vs current = 182/333 − 1 | −45% | **−45.4%** | ✅ |
| Base vs current = 292/333 − 1 | −12% | **−12.3%** | ✅ |
| Bull vs current = 360/333 − 1 | +8% | **+8.1%** | ✅ |

**结论：scenario_model 算术全部勾稽，无错误。** `implied_price = eps_basis × forward_pe` 恒等式逐行成立。

**两个细节澄清（非算术错误，已在 §3 开 P1 回流）**：
1. **48–49x vs 52.4x**：是**两个 EPS 基准**（$6.8 口径 vs $6.35 as-reported）造成的展示差，非勾稽错误。建议注脚标明。
2. **base 点估计 $292 vs 正文区间 $340–380**：是**"是否把 FY27 成长计入 base"**的口径选择（静态中枢 vs 动态区间），非矛盾。建议两处互相指认。

两者都不改变结论方向（任何口径下 $333 都 priced for perfection、无安全边际）。

---

## 7. 缺一手源

| 缺口 | 当前状态 | 影响 |
|---|---|---|
| **🔴 Verified Q1'26 orders / book-to-bill / backlog（WITHHELD）** | 公司主动不披露（C012, UNVERIFIED）；最后硬读数 Q4'25（+252%/2.9x/$15.0B） | **🔴 BINDING——本案头号缺口。** 用来 underwrite kill (a) 的最干净需求表消失；在 no-floor / highest-beta 名字上，这是"最不该丢的那个数"。**唯一解：等 Q2'26（~2026-07）重新披露。** |
| **倍数 & Street 目标价一手交叉核对**（C029/C031, needs_audit） | 聚合器 S6（stockanalysis.com） | 🟠 估值锚未经一手 10-Q 资产负债表 + 干净 consensus 校验；定性结论（~48–52×、priced for perfection、+13% to Street）方向稳，但精度待坐实 |
| **net-cash 构成**（gross cash vs debt 拆分） | S6 聚合器 ~$0.76B | 🟡 EV ≈ mkt cap 的前提；需对 10-Q 核（C028） |
| **segment 拆分**（power / thermal / services 收入/毛利） | 10-K/10-Q 未单拉 | 🟡 影响 content-per-rack 经济学的精细拆解（C016） |
| **10-K（FY2025 完整版）/ 完整 transcript 系列** | 用 release + 单季 call | 🟠 全年 backlog、客户集中度、segment mix 的唯一一手来源 |

一手 A1/A2 覆盖**核心财务齐全且最新**；缺的是 **①公司主动撤回的那一个数（C012，不可补，只能等）** + **②聚合器倍数的一手坐实** + **③更细的 segment/集中度披露行**。

---

## 8. 管理层未验证 claim

**审计意见：管理层 claim 处理得当——但本案恰恰有一项"管理层主动制造的信息真空"，这是核心。**

- 用的多是**可观察行为**（实际营收/margin/FCF、实际 net cash、实际 bolt-on M&A、IC deck 的 2030 目标），不是空头承诺。operator_underwriting 明确按"execution operator，非 founder-controller"underwrite。✅
- **唯一的管理层前瞻 claim = FY26 guide（sales $13.5–14.0B / margin 22.8–23.8% / EPS $6.30–6.40 / FCF $2.1–2.3B）+ 2030 目标（20–22% CAGR / 27% margin）**——来自 Q1'26 release（S1）与 IC deck（S4），已 verified（C014/C015）。serial beat-raise 记录给这些前瞻**较高可信度**，但 operator 已正确标注"**tenure 全程在 AI up-cycle 内、未经 down-cycle 压力测试**"。✅
- **关键的"未验证"不是某句承诺，而是一整个被撤回的数列**：管理层在 +252% Q4 后**选择不再给 headline 季度 orders/B2B**，只给"orders up YoY / backlog elongated"（C013/C027）。**审计确认：这不是"我们没核到管理层的说法"，而是"管理层把最能验证多头论点的硬数字关掉了"**——operator 治理旗、inversion 路径 A、financial_quality 红旗1 三处一致定性为 **"trust-but-verify-quarterly 的 YELLOW，不是 thesis-breaker，但正是 no-floor/highest-beta 名字上最该盯的 selective disclosure"**。这是本案区别于其他两个 sibling（CEG/GEV 均正常披露）的核心审计事实。
- backlog $15.0B 是管理层口径（FY25 release，A2），但**可取消性 / ~12–18 月转化窗口 / 客户集中度**为 inferred（C024）——IC 应知"backlog ≠ 已确认收入、≠ 合约下限"。

---

## 9. 估值假设过激或过松

**审计意见：估值假设整体偏保守且诚实，未发现"用乐观假设救回报"。** 引擎选择（EPS × forward P/E ladder，因 VRT 是 FCF-positive）对一个 FCF 为正、swing 变量是倍数的标的是**正确建模**，区别于 NBIS 的 EV/forward-sales。

支持"不过激"的证据：
- **base 明确写"倍数 holds ~45–48× 不是保守假设、而是 the risk itself"**（model_assumptions 纪律 1 + valuation 纪律 2）：把"~48× 维持"当作需要被压测的风险而非默认，是反过激的标志。
- **bear 是 plausible 非 theatrical**：2027 capex digestion + B2B 确认 <1.0 + de-rate 到 25–30× on **flat** EPS → **$182（点）/ $170–230（区间）**，且**明确无 floor**（"$110 低点就在一年前"，C030）。**de-rate 而非盈利崩塌**做 downside 的主力，符合一个"盈利真实、估值高、倍数是胜负手"标的的机制。
- 不把 $15B backlog 当 floor（明示"visibility, not annuity, 可取消"，C024）；net cash 仅认 ~$0.76B（保守）。

**可被质疑的偏松/偏紧点（IC 应压测）**：
- **base 是否计入 FY27 成长？**（§3c）：点估计 $292（纯 FY26 EPS×46）偏静态、偏保守；正文 $340–380（FY27 长入倍数）偏乐观。**真实 base 落点取决于"Q2'26 orders 是否 ≥1.0 重新披露"——这是 gating uncertainty，在解析前任何 base 点估计都带宽误差带。** 这正是 C012 缺口对估值的直接传导。
- **bull ~50× FY27E**：对 hardware-heavy industrial，FY27E 仍给 50× 偏激进；但 valuation 已诚实标"bull 需 FY26 beaten + 27%-margin 验证 + backlog 再加速 + 溢价倍数维持"四条同时成立。
- **bear de-rate 到 25–30× 是否够狠？**：$110 低点（一年前）对应的倍数远低于 28×。**真实下行尾部（若 2027 真 digestion + 信号已 dark）可能比 bear $182 更差**——这是"偏紧"的方向，对结论（无安全边际）只会强化，不会推翻。

**净判断**：假设偏保守、引擎正确、bear 有真牙齿（−45%，无 floor）。没有"为了得出买入而拔高假设"的痕迹；相反，**真实下行（信号 dark 下的 2027 digestion）还没充分压进 bear**，意味着真实安全边际只会更差。**~48× fwd、+203% off low 之后仅 +13% 到 Street——bull 已被 priced，这是 priced-for-perfection 的定义。**

---

## 10. 风险未量化

| 风险 | 量化程度 | 缺口 |
|---|---|---|
| **D. 超大客户 capex slope 滚落**（dominant risk） | 🟡 半量化 | 有方向（Big-4 +62–77% to ~$700–725B 现在）+ β（110→380 区间）+ kill (d) 阈值（2027 guide 减速），但**"2027 digestion 概率 × 对 VRT 营收/订单的破坏量级"未量化**——头号未量化项，且因 ~75% 集中度 + no floor 而对 VRT 最致命 |
| **A. 需求信号黑屏**（C012） | 🟠 弱量化 | 这是**信息风险**，本质难量化：撤回 orders/B2B 使路径 D 的拐点会**晚一拍**（只能等它体现在营收里才看见）。inversion 正确判定"A 与 D 复合：highest beta + no floor + lost gauge"，但**"晚多久 / 晚到什么程度才不可逆"无法量化** |
| **B. 系统层商品化 / Schneider** | 🟡 有阈值 | component 层 +26% CAGR 已量化；但**"商品化 bleed up 到 system 层的速度 / Schneider 抢 system 份额的概率"未量化**——已标 800V DC 为 defense + monitor 跟踪份额 |
| **C. margin 目标未达** | ✅ 已量化（当前 GREEN） | FY26 22.8–23.8% vs 27% 2030、Q1'26 beat guide ~180bps，**唯一被完整量化且当前为支撑而非风险的项**（C032） |
| **估值 de-rate（F9 类）** | ✅ 充分量化 | bear $182（28× on flat EPS）= 这是被完整量化的下行（−45%）；与 $110 一年前低点挂钩 |
| **EMEA / 区域 air-pocket** | 🟡 单点已量化 | Q1'26 EMEA −29%（C008）是已发生的硬读数；但"是否扩散到 Americas +44% 核心"未量化——monitor 跟踪 |

**结论**：风险**识别完整**（inversion 覆盖 D/A/B/C 四路径 + 风险类型表），**阈值化（kill criteria）做得好**（a/b/c/d 可观测、各带 early warning），但**三个尾部的"概率×影响"未量化**：①2027 capex digestion 的破坏量级、②信号黑屏使拐点延迟的代价、③系统层商品化速度。**对 IC：这三者恰好都与 C012（被撤回的 orders 信号）纠缠——正因为信号 dark，①②尤其无法被提前量化，这本身就是 WATCH 的核心理由，不是被忽略的盲区。**

---

## 11. Completeness % 粗估 + Verdict Ceiling

### 11.1 完整度加权（事实线 / 理解线 / 决策线，宁低勿高）

| 线 | 权重 | 子项完成度 | 加权得分 |
|---|---:|---|---:|
| **A. 事实线**（source→raw→ledger→facts→audit） | 35% | 9 源、33 claim、核心财务全 A1/A2 verified、本 audit 已建；**扣分：① C012 orders/B2B/backlog 被公司撤回（不可补，结构性缺口）；②倍数/目标价/net-cash 聚合器 needs_audit；③ segment 未拆** | 24/35（69%）|
| **B. 理解线**（business→value chain→moat→operator→inversion） | 35% | **5 模块全完成且高质量**，LEAD（toll booth vs cycle）答得透；扣分：moat 中 design-authority/份额本体指标偏定性（Weak，行业不细披）、operator 未经 down-cycle 测试 | 28/35（80%）|
| **C. 决策线**（financial_quality→valuation→MoS→verdict→monitor） | 30% | EPS×P/E ladder + 三情景 + MoS 表 + monitor 完成、勾稽通过；扣分：**① base 落点压在"Q2'26 orders 是否重新披露"这一不可得变量上（C012 直接传导）；② 48×/52.4× + 点估计/区间口径差待对齐；③倍数 needs_audit**；memo/monitor 已建（+） | 20/30（67%）|

**加权完整度 ≈ 24+28+20 = 72/100 → 落点 **72%**（与 facts/memo/research_status 标注的 **72/100** 一致）。**

> 说明（宁低勿高）：理解线 5 模块齐全且 LEAD 答得透，是本案最强的一线；但**事实线被 C012 的结构性缺口压到 69%、决策线被"base 落点不可收敛 + 倍数 needs_audit"压到 67%**。**这两处扣分都指向同一个根因：最关键的需求信号（orders/B2B）被管理层关掉了。** 故完整度落 72%，不上修。

### 11.2 Verdict Ceiling（套表 + 叠硬规则 + 实质发现，取更低）

**第一步：完整度表**
- 72% → 落在 **60–80% = STARTER** 区间。

**第二步：硬规则（缺模块封顶表）—— 全部不触发**

| 硬规则 | 是否触发封顶？ | 确认 |
|---|---|---|
| 没有 valuation.md / 安全边际 → 最高 WATCH | **❌ 不触发** | valuation.md **已完成**（EPS×P/E + bear/base/bull + MoS 表齐全）→ 解除 |
| 没有 inversion_map.md → 最高 WATCH | **❌ 不触发** | inversion_map.md **已完成**（D/A/B/C + kill criteria）→ 解除 |
| 没有 operator_underwriting.md → 最高 STARTER | **❌ 不触发** | operator **已完成**（People Map + 8 维 + life-arc）→ 解除 |
| 社媒是主要证据 → 最高 INFO-GAP | ❌ 不触发 | 零 C 污染（§5）|
| 不了解生意怎么赚钱 → REJECT/INFO-GAP | ❌ 不触发 | business_model 完整、LEAD 答得透 |

**→ "缺模块"的硬规则封顶全部解除。** 与 GOOGL 不同，VRT 自描述也无 stale 残留（§4），故完整度表给的 STARTER 是干净的起点。

**第三步：两条实质发现（真正的 ceiling 来源）—— 把 STARTER 压回 WATCH**
- **(i) 需求信号黑屏（C012, UNVERIFIED）**：用来 underwrite kill (a) 的最干净计量表被撤回。在一个 **no-floor / highest-beta** 标的上，**无法在 Q2'26 重新披露前确认 orders 仍 ≥1.0**——bear 分支不能被排除、bull 不能被确认。**这一条单独就把 actionable lean 压到 STARTER 之下。**
- **(ii) ~48× fwd 全估值无安全边际**：+203% off low 之后仅 +13% 到 Street；bull 已 priced；base 点估计 $292 / 区间 $340–380 在 $333 之上或附近、bear $182（−45%）无 floor。**好生意 + 错价格 = 不买。**

**第四步：取更低 → 最终 Verdict Ceiling = `WATCH`**

| 来源 | 给出的上限 |
|---|---|
| 完整度 72% | STARTER |
| 缺模块硬规则 | （已全部解除，不再封顶）|
| **(i) orders/B2B 信号黑屏（C012）** | **< STARTER** ← 把可执行 lean 压到 STARTER 之下 |
| **(ii) ~48× 无安全边际** | **WATCH** ← 取更低 |
| 真实下行尾部（信号 dark 下的 2027 digestion）未充分压进 bear | 强化 WATCH |

### Ceiling Rationale（为什么是 WATCH，且 info-band 与 actionable-lean 不同）

- **按 info 完整度（72%）**：本应落 **STARTER** band。
- **但两条实质发现把 ceiling 拉到 WATCH，且把可执行 lean 压到比 STARTER 还低一档**：①最关键的需求信号被管理层关掉（C012 YELLOW），②~48× 全估值无安全边际、+13% 到 Street、bear 无 floor。
- 即：**这是一个"研究做扎实了（72%、模块齐全、无 stale）、结论是好生意但①看不清需求②价格太贵"的 WATCH，不是"还没研究完"的 WATCH。** 距离 STARTER 只差**两件事之一**：(a) Q2'26 **干净重新披露 orders/B2B ≥1.0**（解 C012、关掉信号风险），或 (b) **回调到 ~$230–250** 恢复安全边际。**与 GOOGL 的差别**：GOOGL 的 WATCH 卡在"价格 + 一个不可观测变量（capex 拆分）"；VRT 的 WATCH 卡在"价格 + 一个**被主动关掉**的可观测变量（orders/B2B）"——后者更刺眼，因为它本可披露。

---

## 暴露缺口清单（按优先级）+ 回流到哪一步

| # | 缺口 | 优先级 | 回流步骤 | 具体动作 |
|---|---|---|---|---|
| G1 | **🔴 Q1'26 orders / book-to-bill / backlog（WITHHELD, C012）** | 🔴 P0（binding，但不可主动补） | Step 9/10 monitor（Q2'26 事件） | **等 Q2'26 财报（~2026-07）**：重新披露 ≥1.0 & 透明 → 解 binding gap、可评 STARTER；继续沉默 → stay out；重新披露 <1.0 → 确认 bear-watch |
| G2 | **倍数 & Street 目标价一手交叉核对**（C029/C031, needs_audit） | 🔴 P0（最快、低成本） | Step 2→Step 9 | 对 10-Q 资产负债表 + 干净 consensus feed 核 ~48–52× / +13% 目标；**顺手对齐 §3(b) 48× vs 52.4× 注脚** |
| G3 | **scenario_model 口径对齐**（点估计 vs 区间、48× vs 52.4×） | 🟠 P1（零成本） | Step 9 元数据 | 在 scenario_model.csv + valuation.md 注脚写明 EPS 基准 + "base $292=静态 / $340–380=含 FY27 成长"，让 memo/valuation 互相指认。**不改 verdict，改展示自洽。** |
| G4 | **net-cash 构成**（gross cash vs debt） | 🟠 P1 | Step 2→Step 3 | 对 10-Q 核 ~$0.76B 拆分，坐实 EV ≈ mkt cap（C028） |
| G5 | **segment 拆分**（power/thermal/services 收入/毛利） | 🟡 P2 | Step 2→Step 4 | 从 10-K/10-Q 拉，decompose content-per-rack 经济学（C016） |
| G6 | **FY2025 10-K 全文 + 完整 transcript 系列** | 🟡 P2 | Step 2 | 全年 backlog、客户集中度、segment mix 的一手坐实 |
| G7 | **2027 capex digestion 尾部量化**（D 路径破坏量级） | 🟡 P2 | Step 8（inversion）/ Step 9（bear） | 给"2027 Big-4 capex 减速概率分布 + 对 VRT 订单/营收冲击"，把 bear 下行尾部压实 |

---

## 给 IC 的提示（本审计放行，但 IC 必须正面回应下列质询点）

放行结论：证据扎实、口径自洽（两处展示差已开 P1）、模型勾稽、零污染——**可进 IC Panel**，但 verdict 上限锁 `WATCH`，IC 不得突破到 STARTER 除非 **Q2'26 干净重新披露 orders/B2B ≥1.0** 或 **价格回调到 ~$230–250**（见 ceiling rationale）。IC 必须正面回应：

1. **信号黑屏质询（最硬，本案独有）**：用来 underwrite kill (a) 的最干净需求表（orders/B2B）**在一个 +252% blow-out Q4 之后被管理层主动撤回**（C012）。在 no-floor / highest-beta 标的上，**这是最不该丢的那个数**。IC 必须明确："我们是 WATCH 等 Q2'26 重新披露，还是认为定性话术（orders up YoY / backlog elongated）已足够？"——audit 立场：**不够，这正是把 ceiling 压到 WATCH 的第一理由。**
2. **价格质询**：~48× fwd（or 52.4× on FY26E $6.35）、+203% off low 之后仅 **+13% 到 Street**——bull 已被 priced，这不是"打折买好公司"。bear $182（−45%，无 floor，$110 低点就在一年前）有真牙齿。IC 必须回答："等回调（~$230–250）还是认为估值假设太保守？"——audit 立场：**假设偏保守、真实下行尾部更差，无'假设太保守'翻案空间。**
3. **A×D 合流**（inversion 头号复合风险）：信号黑屏（A）使 capex slope 滚落（D）的拐点**晚一拍**（只能等它进营收才看见）。highest beta + no floor + **lost demand gauge** 三者复合——**别让"margins beat"分散对"我们看不见 orders 了"的注意。**
4. **moat 真实但不护 cycle**：design authority + #1(tied) 份额 + 800V DC 是真护城河，但它护的是**份额**，不护**周期**——~75% 下游是 4 家 discretionary capex，无 floor。IC 应区分"好生意"与"好的当前投资"。
5. **operator 未经压测 + selective disclosure**：Albertazzi serial beat-raise 可信，但 tenure 全程在 up-cycle 内、**未经 down-cycle 测试**；而 down-cycle 恰恰是 orders/B2B 最该透明的时点，他却在 up-cycle 高点就把它关了——这是 trust-but-verify 的 YELLOW。
6. **展示口径差已知**：scenario 的 48×/52.4×、点估计/区间差异是**展示口径**（已开 P1 G3），非矛盾；IC 以**点估计 $182/$292/$360（+FY27E $430–480）**为主锚，结论方向不受影响。
