# 数据中心电力需求：公用事业 · 电网运营商 · 发电商（截至 2026-10-30）

> 切片：电力侧需求（大负荷管线、ISO 队列与预测、IPP 与 hyperscaler 的购电合同、EIA/LBNL 联邦数据）。
> 数据文件：`../data/utilities_grid_load.csv`（长表，216 行，每行标 P/S）。
> 性质：个人投资研究，不构成投资建议。所有数字取自下文来源表；未披露的写"未披露"，不做跨公司加总（各家口径不同）。

---

## §0 结论

1. **签约层仍在加速，没有平台化。** AEP 的增量合同负荷 Q3'26 单季新签 15 GW，达到 84 GW（口径同时从"到 2030 年"后移为"到 2031 年"）；FirstEnergy 合同需求 7.9 GW，比年初的 4.1 GW 接近翻倍；Southern 的大负荷合同约 16 GW，一年前约 8 GW；PPL 宾州 advanced-stage 管线 31.8 GW。
2. **实际用电在稳定增长，但没有提速。** EIA 全美商业售电 2026 年 1–8 月同比 +3.3%，7–8 月 +4.4%，2024、2025 年分别为 +3.0% 和 +3.6%，一直在 3–4% 区间。数据中心集中的公司增速是两位数：AEP 商业电量 +15–18%，Southern 天气调整后商业电量 Q2'26 +10.9%。
3. **漏斗顶部正在被大幅挤水，这是本轮最清楚的裂缝。** ERCOT 大负荷请求在不到一年里（2025-09 到 2026-06）从 189 GW 涨到 474 GW，但 2026-09-03 的 Batch Zero 暂定分类把 302 GW（约 61%）排除在外。Exelon 把"高概率"数据中心负荷从 ~18 GW 下调到 ~11 GW（约 −40%）。CenterPoint 的 studied load 从 ~4 GW 降到 ~2 GW。AEP Ohio 在 take-or-pay 电价生效后，队列从 ~30 GW 缩到 ~13 GW（S）。
4. **预测在下修，政策开始踩刹车。** EIA STEO 对 2027 年商业售电增速的预测从 7 月的 4.6% 降到 9–10 月的 2.7–2.8%；8 月 STEO 把德州 2027 年负荷增速从 14% 下调到 6%，原因是德州州长 8 月 3 日的指令。ERCOT 已暂停批准 ≥75 MW 数据中心通电，17 个已走完其他流程的负荷（6,608 MW）卡在最后一步。PJM 2026 年负荷预测的近端被下调（2028 年 −4,414 MW）；容量拍卖连续三次触及上限，2028/29 仍短缺 6,831 MW。
5. **裂缝来自筛选和政策，不是客户撤单。** 抵押、TSA、最低账单、14 年合同等条款把投机申请挤出去，而有抵押的合同量仍在上升。本轮在一手文件里没有找到 hyperscaler 大规模撤销已签 ESA 的证据。
6. **对 Nebius/CoreWeave 的领先意义。** 需求信号没有破；"电从哪来、何时通电"正在从利好变成约束，最近的风险点是德州 2027 年的通电节奏。下一批检查点：11 月初 D/SO/DUK/EXC/PPL/CEG/VST/TLN/NRG 的 Q3 财报，12-10 ERCOT 审计与社区影响报告（Batch Zero 最终分类），12 月 PJM 2029/30 BRA。
7. **与百年实证（2026-09-16）一致。** 需求是真的；申请量不等于需求，那份研究引用的"72% 会蒸发"正在 ERCOT、Exelon、AEP Ohio 兑现；政治回收已经开始，形式包括德州暂停、PJM 价格上限、Dominion GS-5 条款和各州 take-or-pay 电价。按那份研究的七段弧线，现在处在第 5 段"反证出现"的中段，签约层还没有进入第 6 段。

---

## §1 方法与口径说明

- **一手优先**：SEC 8-K 附件（新闻稿、财报演示）、10-Q/10-K 正文（用 `User-Agent: ResearchLab research@example.org` 抓取），以及 ERCOT/PJM/IMM/EIA/LBNL 官方文件。各公司电话会口头数字和没有进 8-K 的演示文稿用二手报道补，标 S。
- **口径不可加总**：AEP 计"ESA 或 LOA"，Southern 计"已签和/或经 PSC 审查、单个 >100 MW"，Dominion 计"各合同阶段"（SE LOA、CLOA、ESA），PPL 计"advanced stage"（ESA 或 LOA），FirstEnergy 分"Contracted / Pipeline"，Exelon 先后用过"phase 1–3"、"committed"和"high probability"。所以本文只看各家自己的时间序列，不做跨公司求和。
- **截至 10-30 已发 Q3'26 的公司**：AEP（10-28）、FirstEnergy（10-27）、CenterPoint（10-27）、Xcel（10-29，8-K 只有新闻稿）、NextEra（10-21）、WEC（10-29）。Dominion、Southern、Duke、Entergy、Exelon、PPL、CEG、VST、TLN、NRG 的 Q3 尚未发布（已于 10-30 用 EDGAR submissions 核对），最新值是 Q2'26。

---

## §2 公用事业大负荷管线

### 2.1 AEP：增量合同负荷（P，8-K EX-99.1）

| 期末 | 增量合同负荷 | 口径与备注 |
|---|---:|---|
| 2024-09-30 | 20 GW | "financial agreements"，到 2030 年 |
| 2024-12-31 | >20 GW | |
| 2025-03-31 | 21 GW | Q1 稿写"over 20"，21 取自 Q2 稿"up from 21" |
| 2025-06-30 | 24 GW | 另有 >190 GW load requests |
| 2025-09-30 | 28 GW | 首次写明"ESA 或 LOA"；系统峰值 37→65 GW（2030） |
| 2025-12-31 | **56 GW** | 一个季度翻倍；AEP Texas 13→36 GW，均为 signed LOA |
| 2026-03-31 | 63 GW | Q1 新签 7 GW；AEP Texas 41 GW |
| 2026-06-30 | 69 GW | Q2 新签 6 GW，主要在德州 |
| 2026-09-30 | **84 GW（到 2031 年）** | Q3 新签 15 GW；期限后移一年；资本计划 $100B（2027–31） |

实际电量（P）：商业零售电量同比，未经天气调整。

| 期末 | 纵向一体化公司 | T&D（Ohio Power + AEP Texas） |
|---|---:|---:|
| 2024Q3 | +3.4% | +12.8% |
| 2025Q1 | +2.2% | +20.0% |
| 2025Q3 | +6.4% | +30.4% |
| 2025Q4 | +14.7% | **+39.6%** |
| 2026Q1 | +15.8% | +33.3% |
| 2026Q2 | +14.9% | +17.4% |
| 2026Q3 | +15.2% | +18.0% |

**裂缝？**
- 合同数在加速，但有两个结构性问题。第一，Q3'26 把期限从 2030 年后移到 2031 年，84 GW 和 69 GW 不是严格同口径。第二，AEP Texas 41 GW 以上的部分以 LOA 为主，而 ERCOT 在 Batch Zero 里暂定排除了约 61% 的大负荷 MW。两者重叠多少，本轮没有数据。
- T&D 商业电量增速从 +39.6% 降到 +17–18%，季度电量 Q4'25–Q2'26 维持在约 12.8–13.0 TWh。这里有基数效应，还不能当作放缓证据。
- AEP Ohio 的 take-or-pay 电价（85% 最低需量、12 年）生效后，队列从约 30 GW 缩到约 13 GW；2026-02 致 PUCO 函中已签 ESA 为 5,642 MW（S）。这是"条款筛掉投机申请"的典型样本。
- AEP 称 take-or-pay ESA 在合同期内可为居民分摊的固定成本从 $16B 上调到 $21B；已有 5 个州批准大负荷电价，另 3 州待批（P）。

### 2.2 Dominion（Virginia）：各合同阶段数据中心容量（S，来自电话会；一手 10-K 只给售电占比）

| 期末 | 各合同阶段合计 | 其中 ESA |
|---|---:|---:|
| 2024-06-30 | ~21 GW | 未披露 |
| 2024-12-31 | ~40 GW | 未披露 |
| 2025-03-31 | ~40 GW | ~10 GW |
| 2025-06-30 | 未披露 | 未披露 |
| 2025-09-30 | ~47 GW | 未披露 |
| 2025-12-31 | ~48.5 GW | 未披露 |
| 2026-03-31 | >50 GW | 10.4 GW |
| 2026-06-30 | ~53.8 GW（7 月） | ~12 GW |

一手（P，2025 年 10-K）：数据中心占 Virginia Power 售电量，2024 年 26%，2025 年 28%。2025 年两年期复审命令要求，**自 2027-01 起高负荷客户须签 14 年合同、提供抵押、并承担配送/输电/发电收入的最低需量**。NextEra 与 Dominion 的合并演示（2026-05-18）显示 Dominion VA 的大负荷管线为 51 GW。

**裂缝？** 增速在放缓：2024 下半年翻倍，2025 年 +21%，2026 上半年 +11%。ESA 部分一年多只从 ~10 GW 到 ~12 GW，"顶部"增长远快于"已签"。EIA 数据显示弗吉尼亚 2026 年 1–8 月商业售电只增长 +2.6%（商业+工业合计 +2.0%），远低于管线增速，与 Loudoun 输电约束和接入排队一致。Q1'26 电话会上管理层称兴趣"has not waned"（S）。

### 2.3 Southern Company：大负荷合同（P，10-Q/10-K 正文）

| 期末 | 2023 年以来大负荷合同 | 口径 |
|---|---:|---|
| 2025-09-30 | ~8 GW | 已签和/或经州 PSC 审查，单个 >100 MW |
| 2025-12-31 | ~9 GW | 同上 |
| 2026-03-31 | ~11 GW | 增加"无重大前提条件"字样 |
| 2026-06-30 | **~16 GW** | ~11 GW 已经 PSC 审查 + ~5 GW 已与客户达成、待审 |

天气调整后商业电量同比：2025Q1 +1.2%，Q2 +4.4%，Q3 +5.1%；2026Q1 +6.4%，**Q2 +10.9%**（公司称"largely driven by data centers"）。

**裂缝？** 没有看到。条款在收紧：全部合同含最低账单；约 13 GW（基本覆盖 2024 年后所签）另含最短期限、解约金和抵押/担保。另外 ~5 GW 仍待 PSC 审查，存在审批风险。Q3'26 尚未发布。

### 2.4 Entergy

- 管线：超大规模数据中心潜在需求 7–12 GW，另有 3–5 GW 传统工业兴趣（Q2'26 电话会，S）；2025 年新签 ESA 超过 3.5 GW（S）。
- 一手：2026-03 与 Meta 子公司 Evest 签**第二份**路易斯安那北部数据中心 ESA，同时申请 7 台联合循环机组（2030–31 年投运）。条款含 CIAC、预付款、最低月账单和解约金（P，10-Q）。
- 实际电量（P）：天气调整后零售电量 Q1'26 +6.0%（工业 +14.9%，含数据中心），Q2'26 +5.7%（工业 +9.9%）。
- ESA 固定对价的剩余履约义务（至 2048 年）：2025 年底 $8.04B，2026Q1 末 $8.03B（XBRL，P）。

**裂缝？** 本轮没有发现。管线区间 7–12 GW 在 2025–26 年基本没变，说明 Entergy 披露"新增"的速度不像 AEP 那样快。

### 2.5 Duke Energy

| 期末 | 数值 | 口径 | P/S |
|---|---:|---|---|
| 2025-09-30 | ~3.0 GW | 数据中心 ESA（由 Q4 的 4.5 GW 减去"Q3 后新增 1.5 GW"推算） | S |
| 2025-12-31 | ~4.5 GW | 数据中心 ESA；late-stage 管线 ~9 GW | S |
| 2026-03-31 | 7.6 GW | 经济开发项目（含数据中心）已签 ESA | P |
| 2026-06-30 | 7.8 GW | 数据中心 ESA；late-stage 管线 15.4 GW，预计 2027H1 前转化 | S |

**裂缝？** Q2'26 只新增 0.2 GW，环比明显放缓，但 late-stage 管线从 ~9 GW 扩到 15.4 GW。ESA 含最低取电量、解约金和可退还资本预付（S）。

### 2.6 Xcel Energy

- 一手 8-K 新闻稿只披露 Google 明尼苏达数据中心 ESA（2026Q1）：附带 1,900 MW 的 Clean Energy Accelerator 资源，MPUC 预计 2027 年初裁决。数据中心本身的 MW 未披露。
- Q4'25（S）：已签数据中心 ESA 2 GW；目标从"2027 年底前 3 GW 合同"翻倍到 6 GW；高概率管线 ~4 GW（一个月前 1.7 GW）。
- Q2'26、Q3'26 的 GW 数：**未披露（本轮未取得演示文稿；Xcel IR 页面需要 JS，无法抓取）**。

### 2.7 Exelon（P，8-K EX-99.2 财报演示）

| 期末 | 数值 | 口径 |
|---|---:|---|
| 2024-09-30 | 11+ GW | "identified potential data center growth" |
| 2024-12-31 | 17+ GW | phase 1–3：已进入正式工程阶段、交了押金、未投运 |
| 2025-03-31 / 06-30 | 17+ GW | 沿用 Q4'24 数；另有 16 GW 在 cluster study 分析中 |
| 2025-09-30 | 19+ GW | 大负荷（数据中心 18+ GW） |
| 2025-12-31 / 2026-03-31 | ~18 GW 数据中心（"committed"） | 约 45% 签 TSA；另有未来潜在新增 ~43 GW |
| **2026-06-30** | **~11 GW "High Probability Load"** | ComEd ~9 + MidAtlantic ~2；约 40% 签 TSA，约 $1B 抵押 |
| 2026-06-30 | ~25 GW "Future Pipeline" | ComEd ~17 + MidAtlantic ~8，处于当前或未来 cluster study 中 |

**裂缝？** **有，而且是本轮公用事业里最明确的一条。** 用更严格的财务和合同标准（TSA 加抵押）重新筛选后，高概率层从 ~18 GW 降到 ~11 GW，约 −40%；二手报道称长期管线从 43 GW 降到 25 GW，当天股价 −3.1%（S）。管理层称资本计划 $41.7B 不变。性质是口径收紧，不是客户撤单；但它说明此前约 7 GW 的"committed"没有财务承诺支撑。

### 2.8 FirstEnergy（P，8-K 财报演示）

| 期末 | Contracted | Pipeline | 备注 |
|---|---:|---:|---|
| 2025-02（基数） | 2.9 GW | 6.1 GW | 后续演示回溯的基数 |
| 2025-06-30 | 2.695 GW（2029F） | 11.13 GW（2029F 以后） | 口径不同 |
| 2025-09-30 | 3.8 GW | 11.7 GW | 2025 年收到 38 GW load studies，不计入 |
| 2025-12-31 | 4.1 GW | 12.9 GW | |
| 2026-03-31 | 4.3 GW | 14.9 GW | 2035F 口径 |
| 2026-06-01 | ~5.65 GW | — | 春季投资者更新 |
| 2026-06-30 | 6.4 GW | 18.4 GW | 合计 24.8 GW；load studies 101 GW |
| **2026-09-30** | **7.9 GW** | **19.1 GW** | 合计 27.0 GW；另有 ~4 GW 在谈；load studies 117 GW |

**裂缝？** 没有。Contracted 在加速，2026 年三个季度 +3.8 GW，而 2025 年全年 +1.2 GW。西弗吉尼亚管线约增长 6 倍到 ~6 GW，公司正在研究临时表后（BTM）和桥接电源，说明那里卡的是电源而不是需求。

### 2.9 CenterPoint（Houston Electric，ERCOT 内；P）

| 披露日 | 指标 | 数值 |
|---|---|---:|
| 2025-09-29 | 并网请求（全部负荷类型） | 57 GW（2025 年 +40% 以上）；峰值 ~21→31 GW（2031E） |
| 2026-02-19 | 2029 年底前接入新增负荷 | 10 GW（提前两年） |
| 2026-04-23 | firmly committed 工业负荷 | 12.2 GW；2029 年前通电数据中心 8 GW，3.5 GW 在建 |
| 2026-07-28 | Batch Zero 预计合格 | ~14 GW（base ~10 + studied ~4；提交 >17 GW） |
| **2026-10-27** | **Batch Zero 预期需求** | **~12 GW（base ~10 + studied ~2；~5 GW 转入未来批次）** |

累计通电预期：Q2 版为 2027 年 ~3、2028 年 ~9、2029 年 ~11、2030 年 ~13 GW；Q3 版为 2027 年 ~3、2028 年 **~8**、2029 年 ~11、2030 年 **~12** GW。2030E 总负荷增长"仍为 14 GW"（Batch Zero 12 GW 加配网 2 GW）。

**裂缝？** 有，但很小。ERCOT 重新分类后，studied load 从 ~4 GW 降到 ~2 GW，2028 年累计通电预期从 9 GW 降到 8 GW。base load（~10 GW，已付 $50k/MW 保证金）没有变化。

### 2.10 PPL Electric（宾州）

| 期末 | advanced-stage 管线 | 已签 | 在建 | P/S |
|---|---:|---:|---:|---|
| 2024-12-31 | ~9 GW | 未披露 | 未披露 | S |
| 2025-03-31 | ~11 GW | 未披露 | 未披露 | S |
| 2025-06-30 | 14.4 GW | 未披露 | 未披露 | S |
| 2025-09-30 | 20.5 GW | >11 GW（ESA 或 LOA） | ~5 GW | S |
| 2025-12-31 | 25.2 GW | 未披露 | 未披露 | S |
| 2026-03-31 | 28.3 GW | ~10 GW（ESA） | 5 GW | S |
| 2026-06-30 | 31.8 GW | >11 GW（ESA） | >6.5 GW | P |

**裂缝？** "顶部"增长约 1.5 倍，而已签部分在 Q3'25 到 Q2'26 之间停在约 10–11 GW。口径从"签署协议"变成"签署 ESA"，所以不能断定是停滞。另一条一手信号：PPL/Blackstone 合资发电公司 Invitium 自 2025-07 成立以来，**截至 2026-08-07 仍未与任何 hyperscaler 签署 ESSA**（P，10-Q），尽管已锁定 >5 GW 燃机预留。也就是说，"自带发电"类合同比负荷接入合同推进得慢。

### 2.11 公用事业小结：裂缝核对表

| 信号 | 是否出现 | 证据 |
|---|---|---|
| 已签合同下降 | **否** | AEP、SO、FE、Duke、Dominion ESA 都在增加 |
| 管线口径下修或重分类 | **是** | Exelon 18→11 GW；CNP studied 4→2 GW；AEP Ohio 30→13 GW（S） |
| 期限后移 | **是（轻微）** | AEP 期限 2030→2031 |
| 新增签约放缓 | 部分 | Duke Q2'26 +0.2 GW；Dominion 增速 +21%/年 → 半年 +11%；PPL 已签部分持平 |
| take-or-pay 或抵押条款 | **普遍** | Dominion GS-5（14 年 + 抵押 + 最低需量）、SO（13 GW 含抵押）、AEP（5 州获批）、Exelon TSA（约 $1B 抵押）、PPL 80% 最低负荷（S）、Entergy 最低月账单与解约金 |
| 客户撤销已签 ESA | **本轮未发现** | 无一手证据 |

---

## §3 电网运营商

### 3.1 ERCOT（P）

**大负荷（≥75 MW）并网请求**

| 截至 | 请求量 | 数据中心占比 | 来源 |
|---|---:|---:|---|
| 2024-09 | 56 GW | 未披露 | 2025-09 董事会材料 |
| 2025-09-02 | 189 GW | ~69% | 同上 |
| 2025-12（报告日 12-23） | 238.6 GW | 未披露 | 2025 系统约束报告 |
| 2026-03-26 | ~410 GW | ~87% | 2026-04 董事会（较 2025 年底 +178 GW） |
| 2026-05 | ~438 GW | 未披露 | 2026-06 董事会（"绝大多数请求没有提交任何研究"） |
| 2026-06 | ~474 GW | ~90% | 2026-07-29 参议院听证 |

参照：ERCOT 历史峰值约 85.5 GW（2023-08，S）。请求量约为峰值的 5.5 倍。

**Batch Zero 暂定分类（2026-09-03，2026-09 董事会，P）**

| 类别 | 项目数 | MW |
|---|---:|---:|
| Base load（暂定纳入） | 204 | 66.4 GW |
| Studied load（暂定纳入） | 158 | 127.9 GW（同一文件图表写 125.4 GW） |
| 排除 | 373 | **302.2 GW** |

- 背景：PGRR145 把旧的逐个 LLIS 流程改为批量研究，2026-07-10 截止。符合条件的大负荷要把保证金补足到 $50,000/MW。
- **2026-08-03 德州州长指令**：要求对所有推进中的数据中心"a comprehensive verification and audit"。ERCOT 当即暂停 Batch Zero 研究，推迟最终分类，并**暂停批准 ≥75 MW 数据中心和加密矿场通电**。非数据中心大负荷和 25–75 MW 中型负荷不受影响。
- 被暂停的规模：截至 2026 年底有 **17 个数据中心/加密大负荷，合计 6,608 MW（5 年总峰值需求）** 已走完全部 ERCOT 流程，只差通电批准。另外，8-1 QSA 纳入 6 个负荷 1,959 MW（预计 2027Q1 通电），11-1 QSA 可能纳入 17 个负荷 6,874 MW（预计 2027Q2）。
- ERCOT 在 2026-12-10 前向 PUCT 提交核查报告和社区影响报告，最终分类随后公布；Batch Zero 原定 2027-04-09 完成，现在时间表待定。
- 对照：2022-01 至 2025 年底，获批通电的大负荷累计只有 7,502 MW；6 月董事会材料预计 2026Q4 通电 ~3.9 GW（暂停令发布前）。

**长期负荷预测**

| 版本 | 年份 | 峰值或需求 |
|---|---|---:|
| 2024 年 TSP 提供 | 2031 | 150 GW |
| 2025 年 TSP 提供 | 2031 | 218 GW |
| 2025 输电规划调整后（ETPALF） | 2031 | 159 GW（数据中心 officer-letter 负荷乘 55.4% 再乘 49.8%） |
| 2026 初步预测（2026-04-15） | 2032 | 367.79 GW（ERCOT 自称高于预期，"not a prediction of what will be built"） |

**裂缝？** **有，而且最大。** 不过性质是"排水"，不是"需求塌陷"：
- 474 GW 请求中约 61% 被暂定排除，留下的 base load 只有 66.4 GW。
- 通电被政治暂停，6.6 GW 待通电负荷卡住。EIA 因此把德州 2027 年负荷增速从 14% 下调到 6%（见 §5）。
- ERCOT 自己对 TSP 预测打了约 27.6% 的折扣（100 MW 只按 27.6 MW 计），说明运营商也不相信申请量。

### 3.2 PJM（P）

**基础容量拍卖（BRA，RTO 出清价）**

| 交付年 | 价格（$/MW-day UCAP） | 备注 |
|---|---:|---|
| 2024/25 | 28.92 | |
| 2025/26 | 269.92 | |
| 2026/27 | 329.17 | 价格上限 |
| 2027/28 | 333.44 | 价格上限；比可靠性要求短 6,516.6 MW（PJM 史上首次） |
| **2028/29**（2026-07-14） | **325.00** | 价格上限，较上次 −2.5%；清出 138,318 MW 加 FRR 10,864 MW；**短 6,831 MW**；总值 $16.4B；可靠性要求 152,400→156,013 MW，其中预测负荷 +1,374.5 MW，"largely due to additional Large Loads" |

下一次 BRA（2029/30）定于 2026-12。PJM 计划在 9 月申请"Reliability Backstop Procurement"，并推进大负荷的"Connect and Manage"框架。

**数据中心对容量成本的影响（市场监察 IMM，P）**

| 交付年 | 纳入数据中心负荷使 BRA 收入增加 | 预测中的数据中心负荷 |
|---|---:|---:|
| 2025/26 | $9.33B | 未披露 |
| 2026/27 | $7.27B（+82.1%） | 11,993 MW |
| 2027/28 | $6.50B | 17,071 MW（其中新增或上调 13,018 MW） |
| 2028/29 | **未披露**（截至 10-30 IMM 尚未发布 Part A） | — |

三次合计 $23.1B。IMM 结论："data center load growth is the primary reason" 推高了容量价格并造成短缺。

**2026 长期负荷预测（2026-01-14，P）**

- 2036 年夏季峰值 222,106 MW，10 年 CAGR 3.6%；2046 年 253,077 MW。冬季峰值 10 年 CAGR 4.0%。
- **与 2025 年版相比，近端下调**：2026 年 −2,564 MW（−1.6%），**2028 年（RPM 拍卖年）−4,414 MW（−2.6%）**，2031 年 −1,630 MW（−0.8%）。原因是 PJM 改了大负荷审核规则：近端年份只认"firm"承诺（ESO/CC），其余标"non-firm"降权；数据中心爬坡期至少按 36 个月计，利用率默认 70%。
- 有数据中心负荷调整的区域：AEP、ATSI、APS、BGE、COMED、DAYTON、DLCO、JCPL、METED、PECO、PEPCO、PL、DOM、PS。

**裂缝？** **有。** 近端预测被下修，但长期 10 年增速反而上调（3.6% 对上一版的 3.1%，3.1% 为 S）。容量市场一面在价格上限，一面短缺 6.8 GW，说明约束在供给侧；"价格上限"本身就是政治回收的一种形式。

### 3.3 其他 ISO

本轮未覆盖（MISO、SPP、NYISO 未取数）。二手线索：纽约州 2026-07 叫停新的大型数据中心设施提案；特拉华州自 2025-10 起暂停新的大负荷接入（均为 S，未核一手）。

---

## §4 发电商与 hyperscaler 的购电合同（IPP）

| 发电商 | 买方 | 资产与类型 | MW | 期限 | 签约或披露 | 价格 | P/S |
|---|---|---|---:|---|---|---|---|
| Constellation | Microsoft | Crane（原 TMI-1）重启，前表计 | ~835（见 CEG 卡） | 20 年 | 2024Q3 | 未披露（二手估计 $100–115/MWh，未证实） | P（MW 为 S） |
| Constellation | Meta | Clinton 全厂出力 | 未在一手稿取得（约 1.1 GW，S） | 20 年，2027-06 起 | 2025-06 | 未披露 | P |
| Constellation（Calpine） | CyrusOne | Thad Hill（德州，燃气，站旁） | 190 + 210 = 400 | 未披露 | 2025-07 / 09 | 未披露 | P |
| Constellation（Calpine） | CyrusOne | Freestone（德州，燃气，站旁） | 380（另有 380 MW 独家期权） | 未披露 | 2026-02 | 未披露 | P |
| Constellation | 投资级客户（含 Walmart 176 MW） | 存量核电加 Dresden 增容 30 MW | ~920 | 15–20 年（平均 18.5 年），2029–32 起供 | 2026Q2 | 未披露 | P |
| Vistra | Amazon / Microsoft | 新建光伏 | 200 + 405 | 未披露 | 2024Q3 | 未披露 | P |
| Vistra | **AWS** | Comanche Peak 核电 | 1,200 | 20 年 | 2025Q3 公告，2026-02 披露买方 | 未披露 | P |
| Vistra | **Meta** | Perry 1,268 + Davis-Besse 908 + 增容 433 | 2,609 | 20 年；存量 2026 年底起，增容 2031–34 | 2026-01 | 未披露 | P |
| Talen | **Amazon** | Susquehanna 核电，由表后共址改为前表计 | 1,920 | 至 2042 年，可延期 | 2025-06 | 未披露 | P |
| NRG | 一家现有数据中心客户 | 自有站点零售供电（ERCOT + PJM） | 295 → 445 | 长期 | 2025Q2 / Q3 | 未披露 | P |
| NRG | "全球领先云/AI hyperscaler" | 新建 1.2 GW CCGT（德州，BYOP） | 1,200 | 未披露 | 2026Q2：主要商业条款一致，**未最终签署** | 未披露 | P |
| NextEra | Google | Duane Arnold 核电重启 | 615 | 未披露 | 2025-10 | 未披露 | P |
| PPL/Blackstone（Invitium） | 无 | 新建燃气 | 0 | — | 截至 2026-08-07 无 ESSA | — | P |

**2026 年新签 hyperscaler 合同**：Vistra–Meta 2,609 MW（1 月），CEG/Calpine–CyrusOne 380 MW（2 月），NRG 1.2 GW 条款意向（Q2）。CEG 的 ~920 MW 新核电 PPA 没有被称作 hyperscaler 合同。Talen 2026 年没有新签 hyperscaler PPA，只有约 4 GW"土地开发与数据中心签约选项"。Talen 在 2028/29 BRA 清出 10,180 MW、$325/MW-day，对应约 $12.08 亿容量收入。

**裂缝？** 没有撤约或降量。但有两个值得注意的现象。第一，2026 年 IPP 的 hyperscaler 新签集中在 1 月（Vistra–Meta），二三季度以非 hyperscaler 客户、燃气站旁和意向性条款为主。第二，所有合同**价格都未披露**，没法判断溢价是否在收窄。

---

## §5 联邦数据：EIA 与 LBNL

### 5.1 EIA 月度零售售电（Electric Power Monthly 表 5.1，P）

商业部门（数据中心大多计在这里）同比：

| 期间 | 同比 | 期间 | 同比 |
|---|---:|---|---:|
| 2024 全年 | +3.04% | 2025 全年 | +3.61%（1,503,310 千 MWh） |
| 2025Q1 | +4.28% | 2026Q1 | +2.56% |
| 2025Q2 | +3.11% | 2026Q2 | +3.29% |
| 2025Q3 | +2.92% | 2026 年 7–8 月 | **+4.35%** |
| 2025Q4 | +4.26% | 2026 年 8 月 | +5.10% |
| 2026 年 1–8 月累计 | **+3.34%** | 滚动 12 个月（至 2026-08） | +3.50% |

全部门 2026 年 1–8 月累计 +1.55%。2026 年数据为初值，未做天气调整，夏季偏热会推高 7–8 月数字。

**分州：2026 年 1–8 月累计商业售电同比（表 5.4.B）**

| 州 | 商业 | 商业+工业 |
|---|---:|---:|
| 弗吉尼亚 | +2.6% | +2.0% |
| 德州 | +8.3% | **−0.3%** |
| 俄亥俄 | +14.4% | +8.4% |
| 印第安纳 | +13.8% | +6.9% |
| 亚利桑那 | +14.2% | +11.9% |
| 佐治亚 | +6.6% | +4.4% |
| 伊利诺伊 | −1.6% | −1.2% |
| 宾州 | −0.2% | −0.6% |

注：德州商业 +8.3% 而工业 −8.3%，合计持平，很可能有客户在商业和工业之间重新分类（EIA 脚注提示过这种可能），也可能有加密矿场减载。单看德州商业数会高估。

### 5.2 STEO 需求预测的逐期变化（表 7a，月度加总，P）

| STEO 期 | 2027 商业售电（十亿 kWh） | 2027 商业增速 | 2027 全美零售售电 |
|---|---:|---:|---:|
| 2026-01 | 1,587.4 | +4.3% | 4,225.3 |
| 2026-04 | 1,610.9 | +5.4% | 4,243.9 |
| 2026-07 | 1,621.4 | +4.6% | 4,258.6 |
| 2026-08 | 1,608.6 | +4.1% | 4,250.9 |
| 2026-09 | 1,584.4 | **+2.7%** | 4,210.9 |
| **2026-10** | 1,592.4 | **+2.8%** | 4,216.6 |

- 10 月 STEO 的 2026 年值：商业 +3.7%，全部门 +2.3%；2027 年全部门 +1.6%。
- 8 月 STEO 原文：州长 8-3 暂停新数据中心后，"we have lowered our forecast for electricity demand in Texas"，德州 2027 年负荷增速从 **14% 下调到 6%**。9 月 STEO 又说，尽管德州暂停，西南中部地区仍是全美售电增长的最大来源（2027 年约 40%）。
- 口径提示：STEO 里 2025 年商业售电为 1,493.5，EPM 终值为 1,503.3（十亿 kWh），两者不一致。上表增速都按 STEO 自身基数计算。

### 5.3 LBNL / DOE

| 报告 | 数字 |
|---|---|
| 2024-12 报告（基线） | 2023 年数据中心用电 176 TWh，占美国 4.4%；2028 年占 6.7%–12.0% |
| **2025 Update（2026-06 发布）** | 参考情景 2030 年 **649 TWh（11.8%）**；综合不确定区间 521–843 TWh（9.5%–15.3%） |

**裂缝？** 实际电量层面没有：全国商业售电稳定在 +3–4%，数据中心州是两位数。但这个增速**并未加速**，2024 到 2026 年一直在 3–4% 的通道里。预测层面**有**：EIA 9–10 月把 2027 年商业增速砍掉约 1.8 个百分点，2027 年全美售电预测比 7 月少约 42 TWh，主因是德州政策，并非 hyperscaler 需求转弱。

---

## §6 与百年实证研究的连接（`studies/电力需求与电力公司盈利_百年实证_2026-09-16/report.md`）

- 那份研究的核心是"需求是真的，生产者股东通常不赚超额，因为资本会过度涌入，政治会回收"。本轮数据**对前半句是正面验证**：已签合同和实际电量都在增长，数据中心占弗吉尼亚电力售电已达 28%。
- 它在 §7.5 列的"幽灵负荷"反证，**在 2026 年下半年已经变成官方数字**：ERCOT 302 GW 被排除，Exelon 合同口径 −40%，ERCOT 自己对 TSP 预测打 27.6% 折扣，PJM 近端预测下修。
- 它在 §9.3 预言的"政治回收"**已经发生**：德州暂停通电，PJM 价格上限连续三次触顶，Dominion 14 年合同加抵押，各州 take-or-pay 电价普及。顺带的含义是：take-or-pay 条款把需求风险从公用事业转给了数据中心开发商和 neocloud，所以公用事业的合同数越"硬"，下游的固定成本承诺就越重。
- IPP 端：2026 年新签 hyperscaler 核电 PPA 只有 Vistra–Meta 一笔大单，价格全部未披露。这与研究里"稀缺资产一次性重定价，随后被长期固定价锁定"的判断一致。

---

## §7 未披露与待核

**未披露或本轮未取得**
- 所有 IPP–hyperscaler PPA 的**价格**。
- CEG–Meta Clinton 的一手 MW 数；CEG 2026Q2 那 ~920 MW 的具体客户。
- IMM 对 2028/29 BRA 的数据中心成本归因（尚未发布）。
- Dominion 2025Q2 数；Xcel 2026Q2/Q3 的 GW 数；Entergy 已签 ESA 的累计 GW（一手）。
- Dominion、Southern、Duke、Entergy、Exelon、PPL、CEG、VST、TLN、NRG 的 Q3'26（尚未发布）。
- ERCOT Batch Zero 最终分类（12-10 后）；ERCOT 2026 年最终（调整后）长期负荷预测。
- PJM 2026 预测里大负荷调整（LLA）的分年 MW 表（在 Supplement 的 B-9/B-9b，本轮未取）。
- 一手文件里 hyperscaler 撤销已签 ESA 的案例：**未发现**。

**不确定、需复核的说法**
1. Dominion 整条序列是 S（电话会转述），Q2'26 的 53.8 GW 来自 Reuters，电话会原话是"over 53 GW"。
2. Exelon 18→11 GW 属于定义切换（committed → high probability）。二手报道另有"43→36 GW"的说法，口径没有对齐。
3. ERCOT studied load 在同一文件里有 127.9 GW 和 125.4 GW 两个数。
4. Duke 2025Q3 的 ~3.0 GW 是推算值；Q1'26 的 7.6 GW 是"经济开发项目"口径，比数据中心宽。
5. PPL"已签"在 Q3'25 是"ESA 或 LOA"，2026 年变成"ESA"，前后不可比。
6. 德州商业售电 +8.3% 很可能受商业和工业之间重分类影响。
7. AEP Ohio 30→13 GW 与 5,642 MW ESA 是 S（行业媒体），未核 PUCO 原件。
8. 地方反对导致项目取消的统计（Heatmap：2026Q1 至少 20 个项目、≥3.5 GW）和"Microsoft 退出 Nscale 英国项目锚定租户"的报道都是 S，日期和规模未核，未计入结论。

---

## §8 来源表

| id | URL | 日期 | P/S |
|---|---|---|---|
| AEP_Q324 | https://www.sec.gov/Archives/edgar/data/4904/000000490424000099/a3q20248kpressreleaseex991.htm | 2024-11-06 | P |
| AEP_Q424 | https://www.sec.gov/Archives/edgar/data/4904/000000490425000025/a4q20248kpressreleaseex991.htm | 2025-02-13 | P |
| AEP_Q125 | https://www.sec.gov/Archives/edgar/data/4904/000000490425000059/a1q20258kpressreleaseex991.htm | 2025-05-06 | P |
| AEP_Q225 | https://www.sec.gov/Archives/edgar/data/4904/000000490425000139/a2q20258kpressreleaseex991.htm | 2025-07-30 | P |
| AEP_Q325 | https://www.sec.gov/Archives/edgar/data/4904/000000490425000169/a3q20258kpressreleaseex991.htm | 2025-10-29 | P |
| AEP_Q425 | https://www.sec.gov/Archives/edgar/data/4904/000000490426000011/a4q20258kpressreleaseex991.htm | 2026-02-12 | P |
| AEP_Q126 | https://www.sec.gov/Archives/edgar/data/4904/000000490426000031/a1q20268kpressreleaseex991.htm | 2026-05-05 | P |
| AEP_Q226 | https://www.sec.gov/Archives/edgar/data/4904/000000490426000055/a2q20268kpressreleaseex991.htm | 2026-07-30 | P |
| AEP_Q326 | https://www.sec.gov/Archives/edgar/data/4904/000000490426000069/a3q20268kpressreleaseex991.htm | 2026-10-28 | P |
| AEPOH_S | https://newprojectmedia.com/policy-aep-ohio-touts-right-sized-load-as-data-center-pipeline-shrinks-further-under-new-tariff/ | 2026 | S |
| D_10K25 | https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm | 2026-02-23 | P |
| D_Q424_S | https://fintool.com/app/research/companies/D/earnings/Q4%202024 | 2025-02 | S |
| D_Q125_S | https://www.marketbeat.com/earnings/reports/2025-5-1-dominion-energy-inc-stock | 2025-05-01 | S |
| D_Q425_S | https://finance.yahoo.com/news/dominion-energy-inc-q4-2025-173204091.html | 2026-02 | S |
| D_Q126_S | https://www.fool.com/earnings/call-transcripts/2026/05/01/dominion-d-q1-2026-earnings-call-transcript/ | 2026-05-01 | S |
| D_Q226_S | https://www.nasdaq.com/articles/dominion-energy-q2-earnings-call-highlights | 2026-07-31 | S |
| NEED_MERGER | https://www.sec.gov/Archives/edgar/data/753308/000110465926063001/tm2614888d1_ex99-2.htm | 2026-05-18 | P |
| SO_Q125 | https://www.sec.gov/Archives/edgar/data/92122/000009212225000042/so-20250331.htm | 2025-05-01 | P |
| SO_Q225 | https://www.sec.gov/Archives/edgar/data/92122/000009212225000076/so-20250630.htm | 2025-07-31 | P |
| SO_Q325 | https://www.sec.gov/Archives/edgar/data/92122/000009212225000084/so-20250930.htm | 2025-10-30 | P |
| SO_10K25 | https://www.sec.gov/Archives/edgar/data/92122/000009212226000006/so-20251231.htm | 2026-02-19 | P |
| SO_Q126 | https://www.sec.gov/Archives/edgar/data/92122/000009212226000034/so-20260331.htm | 2026-04-30 | P |
| SO_Q226 | https://www.sec.gov/Archives/edgar/data/92122/000009212226000054/so-20260630.htm | 2026-07-30 | P |
| ETR_Q126R | https://www.sec.gov/Archives/edgar/data/65984/000006598426000217/earningsrelease1q26_ex991.htm | 2026-04-29 | P |
| ETR_Q226R | https://www.sec.gov/Archives/edgar/data/65984/000006598426000279/earningsrelease2q26_ex991.htm | 2026-07-29 | P |
| ETR_Q126Q | https://www.sec.gov/Archives/edgar/data/65984/000006598426000222/etr-20260331.htm | 2026-05-01 | P |
| ETR_XBRL | https://data.sec.gov/api/xbrl/companyfacts/CIK0000065984.json | 2026-10-30 抓取 | P |
| ETR_Q226_S | https://www.marketbeat.com/instant-alerts/entergy-q2-earnings-call-highlights-2026-07-29/ | 2026-07-29 | S |
| DUK_Q126 | https://www.sec.gov/Archives/edgar/data/1326160/000132616026000022/er-20260331xearningsreleas.htm | 2026-05-05 | P |
| DUK_Q425_S | https://www.marketbeat.com/instant-alerts/duke-energy-q4-earnings-call-highlights-2026-02-10/ | 2026-02-10 | S |
| DUK_Q226_S | https://www.nasdaq.com/articles/duke-energy-q2-earnings-call-highlights | 2026-08-05 | S |
| XEL_Q326 | https://www.sec.gov/Archives/edgar/data/72903/000007290326000178/xcelearningsreleaseq32026.htm | 2026-10-29 | P |
| XEL_Q425_S | https://www.tdworld.com/utility-business/news/55355802/xcel-doubles-two-year-data-center-contracts-goal-to-6-gw | 2026-02-06 | S |
| EXC_Q324 | https://www.sec.gov/Archives/edgar/data/1109357/000110935724000183/exc-20241030ex992.htm | 2024-10-30 | P |
| EXC_Q424 | https://www.sec.gov/Archives/edgar/data/1109357/000110935725000041/exc-20250212ex992.htm | 2025-02-12 | P |
| EXC_Q125 | https://www.sec.gov/Archives/edgar/data/1109357/000110935725000110/exc-20250501ex992.htm | 2025-05-01 | P |
| EXC_Q225 | https://www.sec.gov/Archives/edgar/data/1109357/000110935725000167/exc-20250731ex992.htm | 2025-07-31 | P |
| EXC_Q325 | https://www.sec.gov/Archives/edgar/data/1109357/000110935725000179/exc-20251104ex992.htm | 2025-11-04 | P |
| EXC_Q425 | https://www.sec.gov/Archives/edgar/data/1109357/000110935726000014/exc-20260212ex992.htm | 2026-02-12 | P |
| EXC_Q126 | https://www.sec.gov/Archives/edgar/data/1109357/000110935726000061/exc-20260506ex992.htm | 2026-05-06 | P |
| EXC_Q226 | https://www.sec.gov/Archives/edgar/data/1109357/000110935726000077/exc-20260730ex992.htm | 2026-07-30 | P |
| EXC_Q226_S | https://conduitstreet.mdcounties.org/2026/08/03/exelon-cuts-data-center-demand-forecast-after-stricter-review/ | 2026-08-03 | S |
| FE_Q225 | https://www.sec.gov/Archives/edgar/data/1031296/000103129625000039/ex9922q25strategicandfin.htm | 2025-07-30 | P |
| FE_Q325 | https://www.sec.gov/Archives/edgar/data/1031296/000103129625000080/ex9923q25highlights_vfin.htm | 2025-10-22 | P |
| FE_Q425 | https://www.sec.gov/Archives/edgar/data/1031296/000103129626000041/ex9924q25strategicfinanc.htm | 2026-02-17 | P |
| FE_Q126 | https://www.sec.gov/Archives/edgar/data/1031296/000103129626000084/ex9921q26strategicandfin.htm | 2026-04-28 | P |
| FE_JUN26 | https://www.sec.gov/Archives/edgar/data/1031296/000103129626000092/ex991springinvestorupdat.htm | 2026-06-01 | P |
| FE_Q226 | https://www.sec.gov/Archives/edgar/data/1031296/000103129626000122/ex9922q26strategicfinanc.htm | 2026-07-28 | P |
| FE_Q326 | https://www.sec.gov/Archives/edgar/data/1031296/000103129626000142/ex992-3q26festrategicand.htm | 2026-10-27 | P |
| CNP_SEP25 | https://www.sec.gov/Archives/edgar/data/1130310/000113031025000124/investorupdatepresentati.htm | 2025-09-29 | P |
| CNP_Q425 | https://www.sec.gov/Archives/edgar/data/1130310/000113031026000010/q4earningspressrelease_v.htm | 2026-02-19 | P |
| CNP_Q126 | https://www.sec.gov/Archives/edgar/data/1130310/000110465926047123/tm2612248d1_ex99-1.htm | 2026-04-23 | P |
| CNP_Q226 | https://www.sec.gov/Archives/edgar/data/1130310/000110465926087279/tm2621002d1_ex99-2.htm | 2026-07-28 | P |
| CNP_Q326 | https://www.sec.gov/Archives/edgar/data/1130310/000110465926118963/tm2628051d1_ex99-2.htm | 2026-10-27 | P |
| PPL_Q226 | https://www.sec.gov/Archives/edgar/data/922224/000092222426000042/ppl-6302026exhibit991.htm | 2026-08-07 | P |
| PPL_Q226Q | https://www.sec.gov/Archives/edgar/data/922224/000092222426000044/ppl-20260630.htm | 2026-08-07 | P |
| PPL_Q125_S | https://www.marketbeat.com/earnings/reports/2025-4-30-ppl-co-stock/ | 2025-04-30 | S |
| PPL_Q325_S | https://www.fool.com/earnings/call-transcripts/2025/11/05/ppl-ppl-q3-2025-earnings-call-transcript | 2025-11-05 | S |
| PPL_Q425_S | https://www.datacenterdynamics.com/en/news/us-utility-ppl-sees-data-center-pipeline-swell-by-23-percent-to-252gw/ | 2026-02 | S |
| PPL_Q126_S | https://www.fool.com/earnings/call-transcripts/2026/05/08/ppl-ppl-q1-2026-earnings-call-transcript/ | 2026-05-08 | S |
| ERCOT_SEP25 | https://www.ercot.com/files/docs/2025/09/15/16.2-System-Planning-and-Weatherization-Update.pdf | 2025-09-15 | P |
| ERCOT_DEC25 | https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf | 2025-12-23 | P |
| ERCOT_APR26 | https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf | 2026-04-20 | P |
| ERCOT_LTLF26 | https://www.ercot.com/news/release/04152026-ercot-releases-preliminary | 2026-04-15 | P |
| ERCOT_JUN26 | https://www.ercot.com/files/docs/2026/05/24/8-Interconnection-and-Grid-Analysis-Update.pdf | 2026-06-01 | P |
| ERCOT_JUL26 | https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf | 2026-07-29 | P |
| ERCOT_AUG26 | https://www.ercot.com/files/docs/2026/08/20/Batch-Zero-Verification-and-Audit-PUCT-Presentation.pdf | 2026-08-20 | P |
| ERCOT_SEP26 | https://www.ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf | 2026-09-14 | P |
| PJM_LF26 | https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf | 2026-01-14 | P |
| PJM_BRA2728 | https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf | 2025-12-17 | P |
| PJM_BRA2829 | https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf | 2026-07-14 | P |
| PJM_PR2829 | https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf | 2026-07-14 | P |
| IMM_2627A | https://www.monitoringanalytics.com/reports/Reports/2025/IMM_Analysis_of_the_20262027_RPM_Base_Residual_Auction_Part_A_20251001.pdf | 2025-10-01 | P |
| IMM_2728A | https://www.monitoringanalytics.com/reports/Reports/2026/IMM_Analysis_of_the_20272028_RPM_Base_Residual_Auction_Part_A_20260105.pdf | 2026-01-05 | P |
| CEG_Q324 | https://www.sec.gov/Archives/edgar/data/1868275/000186827524000066/ceg-20241104991.htm | 2024-11-04 | P |
| CEG_Q225 | https://www.sec.gov/Archives/edgar/data/1868275/000186827525000070/ceg-20250807991.htm | 2025-08-07 | P |
| CEG_Q425 | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000029/ceg-20260224991.htm | 2026-02-24 | P |
| CEG_Q126S | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000063/ceg-20260511992.htm | 2026-05-11 | P |
| CEG_Q226 | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000097/ceg-20260806991.htm | 2026-08-06 | P |
| CEG_Q226S | https://www.sec.gov/Archives/edgar/data/1868275/000186827526000097/ceg-20260806992.htm | 2026-08-06 | P |
| VST_Q324 | https://www.sec.gov/Archives/edgar/data/1692819/000119312524252608/d852941dex991.htm | 2024-11-07 | P |
| VST_Q325 | https://www.sec.gov/Archives/edgar/data/1692819/000119312525268033/d33941dex991.htm | 2025-11-06 | P |
| VST_Q425 | https://www.sec.gov/Archives/edgar/data/1692819/000119312526073364/d21122dex991.htm | 2026-02-26 | P |
| VST_10Q226 | https://www.sec.gov/Archives/edgar/data/1692819/000169281926000019/vistra-20260630.htm | 2026-08-10 | P |
| TLN_JUN25 | https://www.sec.gov/Archives/edgar/data/1622536/000162828025030559/a20250611pressreleasebusin.htm | 2025-06-11 | P |
| TLN_BRA2829 | https://www.sec.gov/Archives/edgar/data/1622536/000162253626000058/a20260714pressreleasepjm20.htm | 2026-07-14 | P |
| TLN_Q226 | https://www.sec.gov/Archives/edgar/data/1622536/000162253626000065/a20260805q22026earningsrel.htm | 2026-08-05 | P |
| NRG_Q225 | https://www.sec.gov/Archives/edgar/data/1013871/000101387125000018/nrgq22025ex991.htm | 2025-08-06 | P |
| NRG_Q325 | https://www.sec.gov/Archives/edgar/data/1013871/000101387125000023/nrgq32025ex991.htm | 2025-11-06 | P |
| NRG_Q226 | https://www.sec.gov/Archives/edgar/data/1013871/000101387126000018/nrgq22026ex991.htm | 2026-08-04 | P |
| NEE_Q325 | https://www.sec.gov/Archives/edgar/data/753308/000075330825000055/neeq32025exhibit99.htm | 2025-10-28 | P |
| EIA_EPM51 | https://www.eia.gov/electricity/monthly/xls/table_5_01.xlsx | 数据至 2026-08 | P |
| EIA_EPM54B | https://www.eia.gov/electricity/monthly/xls/table_5_04_b.xlsx | 数据至 2026-08 | P |
| STEO_OCT26 | https://www.eia.gov/outlooks/steo/xls/STEO_m.xlsx | 2026-10-06 | P |
| STEO_SEP26 | https://www.eia.gov/outlooks/steo/archives/sep26_base.xlsx | 2026-09 | P |
| STEO_AUG26 | https://www.eia.gov/outlooks/steo/archives/aug26_base.xlsx | 2026-08 | P |
| STEO_AUG26PDF | https://www.eia.gov/outlooks/steo/archives/aug26.pdf | 2026-08 | P |
| STEO_JUL26 | https://www.eia.gov/outlooks/steo/archives/jul26_base.xlsx | 2026-07 | P |
| STEO_APR26 | https://www.eia.gov/outlooks/steo/archives/apr26_base.xlsx | 2026-04 | P |
| STEO_JAN26 | https://www.eia.gov/outlooks/steo/archives/jan26_base.xlsx | 2026-01 | P |
| LBNL_2024 | https://eta-publications.lbl.gov/publications/2024-united-states-data-center-energy | 2024-12 | P |
| LBNL_2025U | https://eta-publications.lbl.gov/publications/united-states-data-center-energy-2025 | 2026-06 | P |
| ANCHOR | studies/电力需求与电力公司盈利_百年实证_2026-09-16/report.md | 2026-09-16 | 仓库内 |
