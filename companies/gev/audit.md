# GEV Audit / Quality Gate（Step 7 — pre-IC 对抗性 QA）

最后更新: 2026-06-19
审计立场: **对抗性找漏洞**（adversarial hole-punching），不是再夸一遍。这是夹在分析模块（Step 2–6）与 IC Panel（Step 8）**之间**的独立质量闸。它不新增事实、不裁多空，只检验证据是否扎实、模块间口径是否自洽、缺口在哪、最高允许给什么 verdict。

被审输入: `facts.md`、`source_register.md`（S1–S9）、`claim_ledger.csv`（C001–C037）、7 个分析模块（business_model / financial_quality / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map）、`valuation.md`、`model/{scenario_model.csv, model_assumptions.md}`、`memo-v1.md`。
适用清单: `frameworks/investment_research_pipeline_detailed.md` §9（审计项 + verdict ceiling 表）+ `frameworks/buy_side_research_department.md` §4（硬规则）。

---

## 0. 一句话审计结论

证据工程与分析层质量**高于多数买方初稿**：37 条 claim 的载重数字基本回挂一手 A1（10-K/10-Q/8-K）或 A2（IR 投资者更新，且 S3/S4 关键数已 WebFetch 2026-06-19 二次确认），**口径纪律（剔除三项一次性收益、FCF 被预收款粉饰、用 clean forward 桥而非 trailing screener）在 7 个模块间高度一致**，scenario_model 算术与 valuation 正文勾稽。**但有一个必须先盯死的核心完整性问题、两个次级问题**：①**核心完整性检查——三项一次性收益（$2.9B 税务估值备抵释放 + ~$4.5B Prolec/Proficy M&A 收益 + Q1 ~$5.3–5.6B 营运资本/预收款流入）是否在 financial_quality / valuation / model 三处全部被剔除、且对外 verdict 用的是 clean ~46–51× fwd-EBITDA 而非 85× screener？——抽查结论：是，三处一致剔除，封顶用的是 clean 倍数**（详 §3/§6）；②真正的 verdict ceiling **不是"缺模块"的硬规则**，而是 valuation 的**实质发现：$1,109.73 现价无安全边际**（~46–51× clean fwd-EBITDA、近历史高位、对 Siemens ~39× 溢价；base 情景 ~flat、bear −40%）；③**memo-v1 与 ledger 之间一处可见的数字小不一致**（Prolec/Proficy 一次性收益 memo 写 "$4.3B" 而 ledger/financial_quality 写 "~$4.5B M&A 总额"），不改 verdict 但需对齐。综合：**ceiling = WATCH，理由是"信息够了（78/100）、价格太贵"——与 GOOGL 同构。**

---

## 1. Source coverage（各模块关键论断能否回到 facts 的 source_id / claim_id？）

抽查每个模块的核心论断 → 追溯 source_id（S）/ claim_id（C）：

| 模块 | 抽查的关键论断 | 回挂 | 判定 |
|---|---|---|---|
| business_model | 装机后服务年金、$87.4B 服务 RPO（54%）、~7,000 台在役、+10–20% 定价、预付押金 | C011/C012/C016/C017（S2/S3）| ✅ 悬空=0 |
| financial_quality | 三项一次性收益、FY25 营业利润 $1.39B clean、2026 adj-EBITDA $5.7–6.4B、Wind −$382M | C002/C003/C006/C007/C010/C021（S1/S2/S3）| ✅ 一次性逐项标注 |
| value_chain_map | 3-maker 寡头、GEV 设价（非接受）、买方预付押金（反向买方力） | C013/C016/C017（S7/S3/S2）| ✅ 结构推断标 inferred |
| moat_map | 7 行护城河逐条挂证据；durable core vs cyclical surcharge 切分 | 每行带 C 号；entry-impossible 标 inferred（C019）| ✅ Weak/cyclical 项诚实降级 |
| bottleneck_map | 100 GW 合同（44 firm + 56 reservation）、sold-out 2029、$87B 服务年金、reservation→firm 是durability test | C014/C015/C011/C017（S3/S2）| ✅ 未臆造 |
| operator_underwriting | $10B 2025–28 capex、20→24 GW/yr 量节、Prolec $5.275B、分红翻倍/回购 $6→$10B、≥⅓ 现金回报 | C031/C027/C026/C025（S4/S5）| ✅ 全用可观察行为 |
| inversion_map | A–F 失败路径、Kill (a)–(d)、shared switch 标 medium | C016/C028/C031/C030（S3/S9）| ✅ 含当前读数 |
| valuation | EV ~$292B、clean 46–51×、对 Siemens ~39× 溢价、三情景 | C032/C033/C034（S6 + 派生）| ✅ 派生倍数标 inferred |

**结论**：source coverage **强**。逐模块抽查未发现"悬空关键论断"（=有数字/判断却无 source/claim 标注）。所有载重数字唯一来源=facts.md / claim_ledger.csv，结构性推断一律就地标 inferred 并进 open gaps。

**软肋（与 GOOGL 同型）**：①现价 $1,109.73 与 EV ~$292B 来自 S6（stockanalysis.com，B2，2026-06-18），不是 A1——但价格本身公开可核、且 EV 仅用作分母，可接受；②**S7/S8/S9 三条载重的行业/市场结构与 shared-switch 输入是 B2（独立行业数据/财经汇编）**，非一手——其中 C013（寡头份额）、C019（entry impossible）、C030（hyperscaler $725B capex）均已正确标 medium / inferred，未被当 A1 用，合规但需 IC 知"这三条是 B2 强度"。

---

## 2. 无 source_id 的关键 claim

逐模块扫描"作为论断使用、却无 source/claim 标注"的 claim：**未发现裸奔的关键 claim。** 所有非 filed 数字都落在以下三类已标注的桶里：

- **inferred（分析/行业推断）**：C013（GEV+Siemens+Mitsubishi ≈ two-thirds 重型）、C019（重型燃机进入"effectively impossible"）、C031（capex 压 ROIC，尚未可见）、C033（clean 46–51× 倍数=2026 guide × EV 派生）、C034（三情景三角定价）。均明标 inferred + confidence medium/high。
- **B2 行业色彩（永不当一手数字）**：`$600/kW by end-2027`（S8 行业色，valuation/moat 已注明"S8 industry color, not in transcript"）；hyperscaler 各家 capex 拆分 AMZN $200B / GOOGL $175–185B / MSFT $190B / META $115–135B（S9，标 medium）。
- **管理层前瞻 guide（B1/A2，非已实现 actual）**：2026 收入/EBITDA/FCF guide（C010，S3，已 WebFetch 确认）、2028 段margin 目标 22%/22%/6%（C023，S4，已 WebFetch 逐字确认）。均明确标为 guide/target，未与 actual 混用。

**唯一边缘项**：`$600/kW` 路径与 hyperscaler 各家 capex 拆分是 B2，**但它们都没有进入 scenario_model 的载重计算**（模型只用 clean 2026 adj-EBITDA $5.7–6.4B 与 2028 $10B+ 目标作锚），故不污染 verdict。**处理正确**。

---

## 3. 冲突数字 / 模块间口径不一致 —— ⚠️ **本审计的中心完整性检查**

### 核心检查：三项一次性收益是否在全链路被剔除、对外倍数是否 clean？ —— 结果：**三处一致剔除，封顶用 clean 倍数（通过）；但 memo 有一处数字标签不一致（需对齐）**

**(a) 三项一次性收益是否在 financial_quality / valuation / model 三处全部识别并剔除？** ✅ **三处一致。**
- **financial_quality §"One-Off Reconciliation"** 用专表逐项列出三项：①FY2025 ~$2.9B 税务估值备抵释放（C003）；②Q1'26 ~$4.5B M&A 收益（Prolec remeasurement 为主 + Proficy ~$0.33–0.6B，**已排除在 adjusted EBITDA 之外**，C006）；③Q1'26 ~$5.3B 营运资本收益 / 合同负债 ~+$5.6B 流入（客户预付押金，递延收入时点，**非已赚利润**，C007），并明写"Screener TTM 净利 ~$9.4B / EV-EBITDA ~85× **double-counts (1)+(2)** → **Discard trailing GAAP**"。
- **valuation §"Why screener multiples are wrong"** 同样列 trailing P/E ~32 / EV-EBITDA ~85× / fwd P/E ~60 三个 headline 全部标"distorted"，并明确"Discard trailing GAAP，用 clean forward bridge"。
- **model_assumptions / scenario_model** 在 `current` 行与 Assumption Discipline 双处明写"Screener EV/EBITDA ~85× is one-off-distorted（tax release + Prolec/Proficy M&A gains）- do not use"。
- **三处口径完全统一**：没有任何模块把 net income $4.9B（FY25）或 $4.745B（Q1'26）当 earning power，没有任何模块把 Q1 FCF $4.8B 当 normalized 现金。**这是教科书级的一次性剔除纪律——本研究最硬的一致性项。**

**(b) 对外 verdict / 估值用的是 clean ~46–51× 还是 85× screener？** ✅ **用 clean。**
- valuation 的 Clean-Multiple Bridge 明确用 2026 adj-EBITDA $5.7–6.4B（= $44.5–45.5B × 12–14%）÷ EV $292B = **46–51×**；EV/FCF 39–45×（且注 FCF 被预收款粉饰，normalized ~50×+）。
- memo-v1、facts、moat、inversion、bottleneck 凡引估值倍数处，**一律引 ~46–51× clean fwd-EBITDA**，并都带"对 Siemens ~39× 溢价"对照。facts §Financial snapshot 明写"Screener '净利 $9.4B TTM / EV-EBITDA 85×' double-counts one-offs — true earning power far lower"。
- **未发现任何对外结论引用 85× 的痕迹。中心完整性检查通过。**

**(c) Q1 FCF $4.8B 是否被当 normalized 现金？** ✅ **否，全链路标"flattered"。**
- financial_quality §Quality Questions 明写"Is FCF overstating owner earnings? **Yes, currently** — Q1'26 FCF $4.8B is flattered ~$5.3B by advance payments；normalized FCF materially lower；clean bridge 是 **open gap**"。
- valuation Owner Earnings Bridge 把 Q1 FCF $4.8B 标"flattered ~$5.3B by advances"、owner earnings"not cleanly estimable today"，并据此**放弃 owner-earnings DCF、改用 normalized-EBITDA × multiple**。处理正确且诚实。

### 全面扫描发现的口径项（需 IC 知晓）

| 项 | 状态 | 处理 |
|---|---|---|
| **Prolec/Proficy 一次性收益的数字标签** memo-v1 写 **"$4.3B Prolec/Proficy gains"** vs ledger C006 / financial_quality 写 **"~$4.5B M&A 总额（Prolec ~$4.0B + Proficy ~$0.33B）"** | 🟠 **不一致（标签级）** | 同一笔一次性的不同表述：call 口径"$4.5B M&A gains（主要 Prolec）"是总额；memo 的"$4.3B"疑似漏算/早稿。**不影响 verdict（剔除方向一致），但应把 memo 对齐为 ~$4.5B M&A 或拆"Prolec ~$4.0B + Proficy ~$0.33–0.6B"。回流 G-mem。** |
| **2028 收入目标** facts 行34写"Power 22% / Elec 22% / Wind 6% margin"，未在该行复述 $52B；C023/S4 写"revenue ~$52B" | ✅ 非冲突（不同行分述）| C023 已逐字确认 $52B；facts 财务行未重复属精简，不算矛盾。 |
| **EV 锚** valuation $292B vs scenario_model `current` 行 ~$292B vs facts"市值 ~$298B / EV ~$292B" | ✅ 一致 | 市值 $298B − 小额净现金 ≈ EV $292B，三处对齐。 |
| **Wind FY26 指引** financial_quality"~$400M EBIT loss" vs inversion"FY loss > ~$400M 为升级线" | ✅ 一致 | 同一 $400M，一处作 guide、一处作 kill 阈值，自洽。 |
| **gross debt/EBITDA <1x** facts/financial_quality/operator 三处 | ✅ 一致 | 均 C009（S2）。 |

**§3 结论**：模块间**无实质数字冲突**；中心完整性检查（三项一次性全剔除、对外用 clean 46–51×、Q1 FCF 不当 normalized）**全部通过**。唯一需修的是 memo 的"$4.3B"标签 vs ledger"~$4.5B"——**标签级、不改 verdict**。这反映 7 个模块确实都吃了同一份 facts/ledger，纪律到位。

---

## 4. Stale facts（时效性）

数字本身**不 stale**：FY2025 10-K（S1）+ Q1'26 10-Q（S2）+ Q1'26 call（S3）+ Dec'25 投资者更新（S4）均为最新一手，且 S3/S4 关键数已 WebFetch 2026-06-19 二次确认（ledger notes 与 source_register 明载"Confirmed by WebFetch 2026-06-19"）。价格 $1,109.73 / 2026-06-19 与全仓一致。

**与 GOOGL 不同——GEV 全仓自描述基本不 stale**：facts/各模块/memo 均统一写 verdict=WATCH、completeness 78/100、ceiling 因价格而非缺模块。**未发现 GOOGL 那种"模块未做、硬规则封顶"的过时自描述**（GEV 的 7 模块 + valuation 在写就时即标 WATCH 因价格，元数据一致）。

| 位置 | 检查 | 判定 |
|---|---|---|
| `facts.md` 行3 | "As of 2026-06-19 · Price $1,109.73 · Verdict must rest only on what is below" | ✅ 当期 |
| `memo-v1.md` 行3 | "Verdict: WATCH（lean STARTER sub-~$950）· Info-completeness 78/100 · #2 of 3" | ✅ 与本审计一致 |
| 各模块 "Last updated: 2026-06-19" | 7 模块 + valuation 全部 2026-06-19 | ✅ 同步 |
| `bottleneck_map.md` / `inversion_map.md` / `valuation.md` 末尾引 `monitor.md` | 引用了**尚未建**的 monitor.md | 🟡 轻微（链接前向引用，monitor 待建，见 §11 G-list）|

**含义**：GEV 元数据健康，无需 GOOGL 式的"批量纠正 stale 自描述"。**唯一时效缺口是结构性的、非 stale**：缺 monitor.md（多模块已前向引用）、缺 10-Q/10-K 之外的"clean normalized-FCF 桥"（financial_quality 自标 open gap）。

---

## 5. C 级污染（KOL/视频是否混进 EVIDENCE 支撑某模块判断）

**结论：零污染。** source_register S99 行明写"(none yet) — No KOL/video source used. Reserved.（C 级 never promoted to a fact）"。全仓扫描无任何 KOL / 视频 / 论坛 / 雪球贴被用作模块判断的证据。

- 载重数字全部 A1（S1/S2/S5 SEC）+ B1（S3 call）+ A2（S4 IR 更新）。
- 行业/市场结构（S7/S8/S9）是 B2 独立数据，已正确降级 medium / 仅作 context，**未进 scenario_model 载重计算**。
- 与 GOOGL 不同：GEV **无 13F / KOL / 段永平个人持仓信号需要降权**——本案不存在"H&H 13F ≠ 段永平实时交易"这类 caveat，因为根本没引任何此类信号。Gate A（事实/解读/情绪分开）天然达标。

---

## 6. Math / Model 错误（抽查 scenario_model 与 clean-bridge 勾稽）

逐项重算关键派生数字：

| 检查 | 模型/正文值 | 重算 | 判定 |
|---|---|---|---|
| 2026 adj-EBITDA 区间 = $44.5–45.5B × 12–14% | $5.7–6.4B | 44.5×0.12=5.34；45.5×0.14=6.37 → ~$5.3–6.4B | ✅（正文取 5.7–6.4 偏窄，下限略高于机械 5.34，属取整保守，可接受）|
| EV / fwd adj-EBITDA = $292B ÷ $5.7–6.4B | ~46–51× | 292/6.4=45.6；292/5.7=51.2 | ✅ 勾稽 |
| EV / FCF = $292B ÷ $6.5–7.5B | ~39–45× | 292/7.5=38.9；292/6.5=44.9 | ✅ 勾稽 |
| 对 Siemens 溢价 | ~46–51× vs ~39× | clean GEV 显著高于 Siemens 39× | ✅ 溢价成立 |
| **Bear** norm EBITDA $5B × 25× = EV $125B | 价 ~$600–700（−40%）| 125/292=0.428 → EV 较现 −57%；股价 −40% 因含小额净现金 + 非线性，量级合理（−40% 对应 ~$666）| ✅ 量级自洽 |
| **Base** norm EBITDA $10B × 30× = EV $300B | 价 ~flat（~$1,100）| 300 vs 现 292 → +3%，约 flat | ✅ 勾稽 |
| **Bull** $10B+ × higher → EV >$360B | $1,400+（+25%+）| 360/292=1.23 → +23%，$1,109×1.25≈$1,387 | ✅ 量级自洽 |
| 市值/EV 桥 | $298B − 小额净现金 ≈ $292B EV | C009 现金 $10.17B 部分被 Prolec 债务抵销 → 小额净现金，差 ~$6B 合理 | ✅ |

**结论：模型算术全部勾稽，无错误。** scenario_model.csv 的 implied_ev = norm_ebitda × multiple 三行（125 / 300 / >360）与 implied_price（−40% / flat / +25%+）方向与量级一致。

**两个细节澄清（非错误）**：
1. scenario_model 是**三角定价（normalized-EBITDA × EV/EBITDA），非 owner-earnings DCF**——这是**正确的方法选择**（model_assumptions 已论证：trailing base 被一次性扭曲 + 设备定价 cyclical → DCF 不可靠）。审计认同此降级，**但须提示 IC：三情景是量级三角，不是精算点估计**，bear/base/bull 的倍数（25×/30×/higher）本身是判断。
2. implied_price 标"approximate, ~$298B mkt cap / ~$268M-equivalent share basis"——股数基础是约数，故 −40%/flat/+25% 是区间而非小数点级。**展示精度 vs 计算精度的正常差异，不是勾稽错误。**

---

## 7. 缺一手源

| 缺口 | 当前状态 | 影响 |
|---|---|---|
| **Clean normalized-FCF 桥**（剥离预收款时点） | financial_quality 自标 open gap；Q1 FCF $4.8B 含 ~$5.3B 预收 | 🔴 normalized FCF 是"$4.8B 印钞"与"真实自由现金"的差，直接决定 EV/FCF 真实倍数（39–45× 还是 50×+）；是 base 能否站住的胜负手之一 |
| **Reservation-fee / cancellation 条款** | facts/bottleneck 明标 undisclosed | 🔴 56 GW reservation（占 100 GW 的 56%）的可取消性=durable rent 还是 booking peak 的判定项；是 UPGRADE 触发器（reservation→firm）的可观测前提 |
| **GEV-specific heavy-duty GT 份额拆分** | C013 仅"GEV+Siemens+Mitsubishi ≈ two-thirds"（S7，B2，medium） | 🟠 影响"GEV 单独 vs Siemens/Mitsubishi 的定价权强弱"，寡头论点的本体指标 |
| **2028 目标的桥（structural vs cyclical 拆分）** | $5.7–6.4B（2026）→ $10B+（2028）的桥未拆 | 🟠 多少 EBITDA 增量来自结构性（服务年金 + Electrification scale）vs cyclical（设备 +10–20% premium）——base 落点的核心 |
| **段级 ROIC 时间序列 + capex 投向明细** | $10B 2025–28 总额（S4），无年度/段级 ROIC | 🟠 kill (c)（24 GW/yr 落地压 ROIC）无法精算；operator 自标"comp-design / ROIC hurdle review 为 open item" |
| **Siemens Energy / Mitsubishi 同期 filing 对照** | 仅 Siemens ~39× EV/EBITDA 单点（S6） | 🟡 step0 source budget 列了竞品 filing 2–4 份，实际只取 Siemens 单点倍数；溢价对照缺更细同口径 |
| **monitor.md** | 多模块前向引用，未建 | 🟡 Kill Criteria + 监控触发器已就绪可直接搬，待 IC 后落地 |

一手 SEC + call + IR 覆盖**完整且最新**；缺的是"更细的披露/拆分"（normalized-FCF 桥、reservation 条款、份额拆分、2028 桥）+ "更细的竞品同口径对照"。

---

## 8. 管理层未验证 claim

**审计意见：管理层 claim 处理得当——本研究的载重证据以可观察行为 + 已实现 actual 为主，前瞻 guide 已明确隔离。**

- operator_underwriting 明确纪律"Evidence-based（investor-update actions、buyback/dividend changes、capital-return framework、measured-capacity strategy、Wind wind-down），not vibes"——用的是**可观察行为**（capex 实际、回购实际 $3.3B、分红翻倍、Prolec $5.275B、量节 20→24 GW/yr），不是心理诊断。✅
- **管理层前瞻 claim 已隔离**：①2026 guide（收入 $44.5–45.5B / adj-EBITDA 12–14% / FCF $6.5–7.5B，C010）；②2028 段margin 目标 22%/22%/6% + 收入 $52B（C023）；③"sold-out-through-2030 by YE2026"（C015）。**前两者已 WebFetch 2026-06-19 逐字确认（升级证据强度）**；第三个是 CEO 目标，已标为目标非 actual。✅
- **关键未验证缺口**：①**reservation→firm 的转化率与 cancellation 条款无一手披露**（facts/bottleneck/inversion 三处均标 undisclosed）——这是区分"durable rent vs booking peak"的核心证据，**目前不存在**；②**管理层未披露 capex 的段级 ROIC hurdle / 利用率假设**（operator open item）——kill (c) 的精算前提缺失。审计确认这两个是真实缺口，且已被相关模块正确标注。
- **2028 目标"Power 16%→22%"是管理层 target，非已实现**：财务/估值正确地把它当"需要兑现的桥"而非既成事实——valuation 明写"market prices the 2028 22%/22% margins as already landed"，把"目标 ≠ 已兑现"作为定价错误之一。IC 应知：base case 内嵌"目标 ~met"假设。

---

## 9. 估值假设过激或过松

**审计意见：估值假设整体偏保守且方法诚实（放弃 DCF 改三角定价），未发现"用乐观假设救回报"。** 这是本研究最硬的部分之一。

支持"不过激"的证据：
- **bear 非戏剧化、base 非悲观**：bear（norm EBITDA ~$5B × ~25× → ~$600–700，−40%）= 2027 capex digestion + 设备 premium 退潮 + Wind 拖累，model_assumptions 明写"plausible not theatrical"；base（~$10B × ~30× → ~flat）= **"目标 ~met 但 success 已在价"**——即用 2028 目标兑现也只是 flat，这是对"好生意"最不留情的诚实。
- **核心估值纪律明确写死**："Do **not** value the cyclical equipment premium at a permanent-rent multiple — the central error the market is making"；"The services annuity（$87B RPO）worth paying up for；equipment premium is not"。把 durable core 与 cyclical surcharge 拆开估值，是本案最关键的 contrarian 纠偏。

**§9 核心质询：对 Siemens 的 ~39× → GEV ~46–51× 溢价是否被论证为合理，还是把设备定价 peak 当永久租金资本化了？**
- **审计判定：溢价被正确地标为"市场的错误"，而非被本研究背书。** valuation 明写"At ~46–51× clean forward EBITDA 市场同时把 (a) toll-booth 当 permanent **和** (b) 2028 margins 当 already landed"——即**溢价 = 把 cyclical 设备 peak 当 permanent rent 资本化**，这正是 bear 情景（2027 capex digestion）要证伪的。moat_map 同写"The market is pricing the cyclical surcharge as if it were part of the durable core — that is the central valuation error"。**本研究没有为溢价辩护，而是把它定为头号定价错误——方向正确。**
- **bear 的 2027 capex digestion 假设是否充分？** bear 把 hyperscaler 2027 capex 数字化为"digestion"（shared switch 转红，inversion kill d），并让设备 premium 退潮 + Wind 走阔。**但 bear 用 ~$5B normalized EBITDA × 25× = 一个量级锚，不是逐段建模**——若 2027 digestion 比假设更深（reservation 大规模取消、premium 不只是 fade 而是 reset），真实下行可能比 −40% 更差。这是"过松"方向，对结论（无安全边际）只强化、不推翻。

**可被质疑的偏松点（IC 应压测）**：
- **base 退出倍数 ~30×**：对一个设备腿 cyclical 的工业，"目标兑现后仍给 30×"本身偏高（model 给的对照是 Siemens 39×、bear 25×）。若 base 退出降到 ~22–25×，base 就从 flat 转负——即**base flat 已经是偏乐观的退出倍数支撑的**。
- **base normalized EBITDA $10B 直接取 2028 目标**：这把"Power 16→22% + Electrification 16→22% + Wind 6%"全部兑现当 base，是**判断不是证据**——真实落点取决于"2028 桥里 structural vs cyclical 的拆分"（§7 缺口），这是 base 的胜负手。
- **bear 仅给量级，未把"reservation 大规模取消 + premium reset（非 fade）"单列**：valuation/inversion 都承认 reservation 条款 undisclosed → bear 没把"硬取消"的极端尾部充分压进 → 真实下行可能更差。

**净判断**：假设偏保守、方法诚实（DCF→三角定价的降级是正确的），结论稳健。没有"为了得出买入而拔高假设"的痕迹；相反，**base flat 已靠偏高的 30× 退出倍数支撑、bear 的硬取消尾部还没充分压进**——意味着真实安全边际只会比"现价无安全边际"更差。

---

## 10. 风险未量化

| 风险 | 量化程度 | 缺口 |
|---|---|---|
| **Wind 损失走阔（kill b）** | ✅ **已量化** | Q1'26 −$382M vs −$146M YoY（C028）、$250–350M/yr 关税逆风、FY26 ~$400M EBIT 亏损 guide、2028 仅 6% margin on declining revenue——**升级阈值明确（FY loss > ~$400M）**。量化到位。 |
| **设备定价 rollover / reservation 取消（kill a）** | 🟡 **半量化** | 当前**反向**（+10–20% 定价、$5.6B 押金、sold-out 2029，C016/C017），有方向有数字；**但 reservation→firm 转化率与 cancellation 条款 undisclosed** → 56 GW 软订单的"硬取消概率 × 影响"无法精算。头号未量化项。 |
| **hyperscaler 2027 capex digestion（kill d / shared switch）** | 🟡 **半量化** | 2026 ~$725B（+77%，C030，S9 medium）已数字化为"still accelerating"；**但 2027 是否 digest、digest 多深、对 GEV 设备 premium 的弹性（~20% of 100 GW 是 DC-tied，但 DC capex 才是 moved pricing 的边际）未量化**。主 thesis-killer，证据强度 B2。 |
| **capacity capex 压 ROIC（kill c）** | 🟠 **弱量化** | $10B 2025–28 总额（C031）有，但**段级 ROIC 时间序列缺** → 24 GW/yr 落地 2027–28 是否压 ROIC"not yet visible"，概率×影响未量化。back-end-loaded。 |
| **多重 de-rate（F）** | ✅ **充分量化** | ~46–51× clean vs Siemens 39×、三情景 IRR/价位——这是唯一被完整量化的风险（valuation MoS 表）。 |
| **SMR/storage 替代（E）** | 🟡 定性 | 标 medium、longer-dated；GEV 自有 BWRX-300，近期影响低，未数字化。 |

**结论**：风险**识别完整**（inversion A–F 覆盖 cyclicality/Wind/capex/监管/替代/估值全类），**Kill Criteria（a)–(d) 可观测 + 含当前读数**，做得好；**但三个尾部的"概率×影响"未量化**：①reservation 硬取消（条款 undisclosed）、②2027 digestion 深度（B2 强度 + 弹性未建）、③段级 incremental ROIC。**这三个恰好都卡在同一类"前向 + 不可观测/未披露"的变量上，且都已正确进 open gaps。对 IC：这些是"押注 vs 定价"的灰区，不是被忽略的盲区。**

---

## 11. Completeness % 粗估 + Verdict Ceiling

### 11.1 完整度加权（事实线 / 理解线 / 决策线，宁低勿高）

| 线 | 权重 | 子项完成度 | 加权得分 |
|---|---:|---|---:|
| **A. 事实线**（source→ledger→facts→audit） | 35% | source_register（S1–S9）+ ledger（37 claim）+ facts + 本 audit 齐全；载重数 A1/A2 为主、S3/S4 已 WebFetch 二次确认；**扣分：clean normalized-FCF 桥缺、reservation 条款 undisclosed、heavy-duty 份额拆分缺（均一手不可得）** | 28/35（80%）|
| **B. 理解线**（business→value chain→moat→bottleneck→operator→inversion） | 35% | **6 模块全完成且高质量**；durable-core vs cyclical-surcharge 切分清晰、LEAD 问题已答；扣分：寡头份额本体指标 B2（S7）、2028 桥 structural vs cyclical 未拆 | 30/35（86%）|
| **C. 决策线**（valuation→MoS→scenario→verdict→monitor） | 30% | clean 46–51× 桥 + 三情景 + MoS 表 + Buy-Below 完成、勾稽通过；扣分：**base 落点压在 2028 桥拆分（不可观测）、退出倍数偏松、normalized-FCF 桥缺、monitor.md 未建** | 21/30（70%）|

**加权完整度 ≈ 28+30+21 = 79/100 → 与 memo/facts 自评 78/100 一致，取 `78/100`。**

> 说明（宁低勿高）：理解线虽 6 模块齐全，但寡头份额是 B2、2028 桥未拆，不按满分计；决策线 base 落点压在不可观测的 2028 桥拆分 + normalized-FCF 桥缺，扣到 70%。**78/100 与全仓自评一致，无需 GOOGL 式的"自评 stale 需上修"。**

### 11.2 Verdict Ceiling（套表 + 叠硬规则取更低）

**第一步：完整度表**
- 78/100 → 落在 **60–80% = STARTER** 区间（信息层够 STARTER）。

**第二步：硬规则（buy_side_research_department §4）**

| 硬规则 | 是否触发封顶？ | 确认 |
|---|---|---|
| 没有 valuation.md / 安全边际 → 最高 WATCH | **❌ 不触发** | valuation.md **已完成**（clean 桥 + bear/base/bull + MoS 表 + Buy-Below）|
| 没有 inversion_map.md → 最高 WATCH | **❌ 不触发** | inversion_map.md **已完成**（A–F + Kill (a)–(d) + 当前读数）|
| 没有 operator_underwriting.md → 最高 STARTER | **❌ 不触发** | operator **已完成**（People Map + 资本配置 + temperament）|
| 社媒是主要证据 → 最高 INFO-GAP | ❌ 不触发 | 零 C 级污染（§5，S99 reserved 未用）|
| 不了解生意怎么赚钱 → REJECT/INFO-GAP | ❌ 不触发 | business_model 完整清晰（装机 + 服务年金双层）|

**→ "缺模块"的硬规则全部不触发——模块齐全。** 完整度给的上限是 STARTER。

**第三步：valuation 的实质结论（真正的 ceiling 来源 —— GOOGL 同构）**
- valuation §MoS 的发现：**$1,109.73 现价无安全边际**——near ATH（−6% off ATH）、~46–51× clean fwd-EBITDA、对 Siemens ~39× 溢价；skew 不利（bear −40% / base ~flat / bull +25%+）；**base 情景"成功已在价"（targets ~met 仍只 flat）**；STARTER 仅 sub-~$950（~25× normalized）。
- 投资清单规则（Buffett/Klarman lens）："安全边际来自乐观假设 / 无安全边际 → 最高 WATCH"。**好生意 + 无安全边际 = WATCH。**
- **这把 ceiling 从 STARTER（完整度给的）压回 `WATCH`**——理由不是"信息不足"，而是"信息够了（78/100）、价格太贵"。**与 GOOGL 完全平行（"信息够了、价格太贵"）。**

**第四步：取更低 → 最终 Verdict Ceiling = `WATCH`**

| 来源 | 给出的上限 |
|---|---|
| 完整度 78/100 | STARTER |
| 缺模块硬规则 | （全部不触发，不封顶）|
| **valuation 实质：无安全边际（near ATH、46–51×、base 成功已在价）** | **WATCH** ← 取更低 |
| base 落点压在不可观测的 2028 桥拆分 + normalized-FCF 桥缺 | 强化 WATCH |

### Ceiling Rationale（为什么是 WATCH —— 与 GOOGL 同构的"信息够了、价格太贵"）

**这是一个"研究做扎实了（78/100、硬规则不封顶、一次性收益已全剔除、模型勾稽）、结论是'最好的生意 + 错误的价格'"的 WATCH，不是"还没研究完"的 WATCH。** 与 GOOGL 完全平行：GOOGL 是"好生意 + $370 无安全边际"，GEV 是"最好的工业生意 + $1,109 near ATH 无安全边际"。距离 STARTER 只差**价格**（跌到 ~$950 一带、~25× normalized 才给 cyclical/Wind/2027 风险补偿）与**两个证据补强**（reservation→firm 转化证durable + normalized-FCF 桥），而非缺模块。**UPGRADE 的非价格路径是 2029–30 slots 把 reservation 转 firm orders（证明 durability 而非 booking peak）。**

---

## 暴露缺口清单（按优先级）+ 回流到哪一步

| # | 缺口 | 优先级 | 回流步骤 | 具体动作 |
|---|---|---|---|---|
| G-mem | **memo-v1 的一次性收益标签**"$4.3B Prolec/Proficy" vs ledger"~$4.5B M&A 总额" | 🟠 P0（最快、零成本） | Step 9 元数据 | 把 memo 对齐为"~$4.5B M&A 收益（Prolec ~$4.0B remeasurement + Proficy ~$0.33–0.6B）"。**不改 verdict，改标签精度。** |
| G1 | **Reservation-fee / cancellation 条款**（durable rent vs booking peak 的判定 + UPGRADE 触发器前提） | 🔴 P0 | Step 1→Step 5/8 | 拉后续 10-Q/call/IR Q&A 找 reservation 押金比例、可取消性、违约金条款；这是 56 GW 软订单"硬不硬"的唯一证据路径 |
| G2 | **Clean normalized-FCF 桥**（剥离 ~$5.3B 预收款时点） | 🔴 P0 | Step 2（financial_quality 扩展）→Step 8 | 从 10-Q 现金流量表拆 contract-liability 流入，给"$4.8B 印钞 → normalized FCF"桥；决定 EV/FCF 真实倍数（39–45× 还是 50×+） |
| G3 | **2028 目标的 structural vs cyclical 拆分**（base 落点胜负手） | 🔴 P0 | Step 8（valuation/model） | 把 $5.7–6.4B（2026）→ $10B+（2028）的桥拆：多少来自服务年金 + Electrification scale（structural）vs 设备 +10–20% premium（cyclical）→ base normalized EBITDA 从"取 2028 目标"收敛到可辩护 |
| G4 | **段级 ROIC 时间序列 + capex 投向明细**（kill c 精算前提） | 🟠 P1 | Step 6（operator）→Step 8 | 拉 $10B 2025–28 的年度/段级投向 + 段级 ROIC，量化 24 GW/yr 落地 2027–28 是否压 ROIC |
| G5 | **GEV-specific heavy-duty GT 份额拆分** | 🟠 P1 | Step 4（value_chain） | 找 GEV vs Siemens vs Mitsubishi 重型燃机精确份额（升级 C013 从 B2 medium）|
| G6 | **Siemens Energy / Mitsubishi 同口径估值对照** | 🟡 P2 | Step 8 | 拉竞品 filing 做同口径 EV/EBITDA（现仅 Siemens 39× 单点），坐实溢价幅度 |
| G7 | **operator comp-design / ROIC-hurdle review** | 🟡 P2 | Step 6 | 核薪酬是否绑 ROIC vs scale/volume（operator 自标 open item）|
| G8 | **monitor.md 未建** | 🟡 P2（IC 后） | Step 9 | IC Panel 后落监控清单（Kill (a)–(d) + reservation→firm + hyperscaler-capex 早警已就绪可直接搬）|

---

## 给 IC 的提示（本审计放行，但 IC 必须正面回应下列质询点）

放行结论：证据扎实、口径自洽（**三项一次性收益全链路剔除、对外用 clean 46–51× 而非 85× screener——中心完整性检查通过**）、模型勾稽、零 C 级污染——**可进 IC Panel**，但 verdict 上限锁 `WATCH`，IC 不得突破到 STARTER 除非价格/证据补强（见 ceiling rationale）。IC 必须正面回应：

1. **价格质询（最硬）**：$1,109.73 是 near-ATH、~46–51× clean fwd-EBITDA、对 Siemens ~39× 溢价；**base 情景"目标 ~met 仍只 flat"——即用 2028 目标全兑现也赚不到超额。** Buffett/Klarman 立场下"好生意 + 无安全边际 = 不买"。IC 必须明确："我们是 WATCH 等回调（~$950，~25× normalized），还是认为估值假设太保守？"——而审计已论证假设偏保守（base flat 已靠偏高 30× 退出支撑、bear 硬取消尾部未充分压进），**无'假设太保守'的翻案空间**。
2. **screener distortion 让 naive 买家多付得更狠**：trailing EV-EBITDA 85× double-counts 三项一次性（$2.9B 税 + $4.5B M&A + $5.3B 预收）；不做一次性剔除的买家会以为"85× 已经很贵"而忽略"clean 46–51× 才是真实贵"，或反向被"P/E 32"误导以为便宜。**IC 须确认：对外结论一律引 clean 46–51×，永不引 screener。**
3. **设备 premium = cyclical peak 被当 permanent rent 资本化**（moat/bottleneck/inversion 头号定价错误）：+10–20% 定价是 hyperscaler capex 拉动的 cyclical 高点，2-yr+ lead time 使今天 bookings 押注 demand 持续到 2028–30。**市场在"押注"toll-booth permanent + 2028 targets，而非"定价"cyclical/2027-digestion 风险。** 这条路径今天无 reservation 硬取消证据证伪，是押注非定价。
4. **base 落点不可收敛**：normalized EBITDA base $10B 直接取 2028 目标，是"取目标"的判断而非证据；落点压在不可观测的"2028 桥 structural vs cyclical 拆分"（G3）+ normalized-FCF 桥缺（G2）。**在补到 G2/G3 前，base ~flat 本身就是个宽误差带的点估计。**
5. **durable core 与 cyclical surcharge 必须分开估值**：服务年金（$87B RPO，54%）是 worth-paying-up 的 durable rent；设备 premium 不是。**市场的错误是付 permanent-rent 倍数买整个（含 cyclical surcharge）。** IC 须把"服务年金该贵 / 设备 peak 不该贵"作为定价纪律，而非 blend 成一个永久倍数。
6. **Wind 是真实且走阔的拖累**：Q1 −$382M vs −$146M（kill b 已 mild 触发），最佳情形是 2028"shrinking business 上的 6% 小利"。IC 须把 Wind 当"quality story 里的真实漏点"，不是可忽略尾部。
