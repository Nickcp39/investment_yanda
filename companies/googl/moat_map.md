# GOOGL Moat Map（护城河 H5）

最后更新: 2026-06-16
负责模块: H5 护城河（把「有护城河」拆成可验证机制）
状态: `analysis_built`. 数字一律挂 `facts.md` 的 `[source_id]`；推理/估算明确标注「derived / 推理」与口径局限。

> 纪律提醒：
> - 数字唯一来源 = `facts.md`（A1 一手）。本文件不引入新数字；凡未挂 source_id 的判断都是「机制推理」或「待验证」。
> - 护城河 ≠ 形容词。只有当某结构能**持续产生超额回报 / 定价权 / 更低成本 / 更强分发 / 更高留存**时才算护城河（见 `frameworks/moat_technical_analysis.md` §1）。
> - 本模块**不给 verdict**——`facts.md` Minimum Coverage Check 已硬规则封顶 WATCH（缺 valuation/inversion）。这里只判**护城河强度 + 攻击面**。

---

## 0. 一句话结论（module verdict）

Alphabet 拥有**多重、互相加固的真护城河**（搜索分发 + 广告拍卖流动性 + YouTube 双边网络 + 全栈 AI 成本结构），整体强度 **Strong**；但护城河正处于**结构形态切换期**——核心攻击面是「AI 原生回答侵蚀搜索点击/分发」与「监管强制开放默认入口」，叠加 **2026 capex $180-190B、2027 再显著增加 [GOOGL-424B5-2026-06.009]** 把"高回报"押注在 AI 基建增量资本上。问题不是「有没有护城河」，而是**旧河被削弱的速度 vs 新河（Cloud/TPU/Gemini 分发）形成的速度**。

---

## 1. 逐条护城河拆解

每条按：类型 / 机制 / 证据(挂 source_id) / 指标 / durability(三层时间) / attack surface / 证据分级。

---

### H5-1 搜索习惯与默认分发（Search habit & default distribution）

- **类型**：分销/入口 + 品牌习惯（混合）。这是 Alphabet 最古老、也最受攻击的核心河。
- **机制**：默认搜索位（Chrome 地址栏、Android、第三方默认协议）→ 海量 query → 广告库存 → 现金 → 买回/维持默认 + 投研发。query 习惯本身形成品牌默认（动词化的"Google it"），降低获客成本到接近零。
- **证据 [source_id]**：
  - Google Services FY2025 营收 **$342,721M**、营业利润 **$139,404M**（营业利润率 ~40.7%，derived）[GOOG.A1.2025K.009 / .010] —— 极高的分部利润率是定价权/低边际成本的直接读数。
  - Google Search & other Q1 2026 **$60,399M，+19% YoY** [GOOG.A1.2026Q1.004] —— **关键反驳"AI 已侵蚀搜索"的当下读数**：在 ChatGPT/AI 回答盛行两年后，搜索广告仍加速到 +19%。
  - 全公司 Q1 2026 **第 11 个连续两位数增长季**，+22% YoY（cc +19%）[GOOG.A1.2026Q1.001] —— 习惯/分发未见断裂信号。
- **指标（监控）**：Search & other 同比增速、Google Services 营业利润率、TAC（流量获取成本，**未在 facts 中验证 → open question**）、默认协议存续。
- **Durability 三层**：
  - **1-2 年（Strong）**：Search +19% [GOOG.A1.2026Q1.004]、第 11 个两位数季 [GOOG.A1.2026Q1.001]，无恶化信号。
  - **3-5 年（Medium）**：DOJ search 默认案 + AI 回答双重压力；默认协议若被禁、入口经济会被改写（见 H5-1 attack surface）。
  - **10 年（Watch/不确定）**：搜索框是否仍是商业意图入口本身存疑；若 monetization 从"链接点击"迁到"AI 答案内嵌广告/agent 交易"，护城河换形态——能否保留取决于 H5-7（模型/分发）能否承接。
- **Attack surface**：
  1. **AI 原生回答绕过搜索框**（OpenAI/Perplexity/Anthropic + 设备级 assistant）→ 减少高意图点击。
  2. **监管禁止默认协议**（DOJ search 案救济）→ 流量需"赢回"而非"买到"，TAC 上升或份额流失。
  3. **设备厂商自建入口**（Apple AI、三星）切走默认。
- **证据分级**：**Strong**（当下分部利润 + 加速增速是一手 A1 直接证据；唯削弱来自前瞻性攻击面，尚未在数字中显现）。

---

### H5-2 广告主数据 / 拍卖流动性（Advertiser data & auction liquidity）

- **类型**：网络效应（双边：广告主 ↔ 受众）+ 数据优势 + 转换成本（工作流）。
- **机制**：海量广告主竞价 → 拍卖流动性 → 每次展示更高出清价；转化/归因数据回流改善定向 ROI → 广告主预算粘性（投放工具、归因体系、自动出价形成工作流习惯）。买卖两边互为门槛：受众多→广告主来，广告主多→变现高→能补贴受众产品。
- **证据 [source_id]**：
  - Google Services 营业利润率 ~40.7%（derived from [GOOG.A1.2025K.009/.010]）—— 拍卖流动性的利润表现。
  - YouTube ads Q1 2026 **$9,883M，+11%** [GOOG.A1.2026Q1.005]（同一广告主基础的跨面分发）。
  - **⚠ Negative 信号**：**Google Network 营收 Q1 2026 $6,971M，YoY 下滑**（vs $7,256M）[GOOG.A1.2026Q1.006] —— 这是**站外网络（AdSense/AdMob 第三方库存）**的萎缩，正是"拍卖流动性"边缘的负面读数（见 §4 风险）。
- **指标（监控）**：CPC / 每次点击成本趋势（**未在 facts 验证 → open question**）、广告主留存/净增、Network 营收趋势（已恶化）、自动出价采用率。
- **Durability 三层**：
  - **1-2 年（Strong on owned surfaces / Negative on network）**：自有面（Search/YouTube）拍卖强；**第三方 Network 已在收缩** [GOOG.A1.2026Q1.006]。
  - **3-5 年（Medium）**：DOJ adtech 案 2025-04 部分败诉，**结构性救济"could have a material adverse effect"** [GOOG.A1.2025K.026 notes]——可能拆分广告中介栈，直接攻击拍卖流动性的中介环节。EC 已 €3.0B 罚（计提 $3.5B，已上诉）[GOOG.A1.2025K.026]。
  - **10 年（Watch）**：AI agent 代理购买、隐私政策（cookie/信号衰减）是否削弱定向数据优势。
- **Attack surface**：
  1. **DOJ adtech 结构性拆分**（强制剥离 ad exchange/中介）→ 拆掉拍卖流动性中枢。
  2. **高意图广告迁移**（Amazon retail media、TikTok、AI 购物 agent 直接成交）。
  3. **隐私/信号衰减**削弱定向 → ROI 下降 → 预算外流。
  4. **Network 库存萎缩**已是进行时（一手负面）。
- **证据分级**：自有面 **Strong**；第三方 Network + 监管中介风险 **Negative/Medium**（监管攻击面已部分落地 = 实打实负面）。

---

### H5-3 YouTube 网络效应（YouTube network effects）

- **类型**：网络效应（创作者 ↔ 观众双边）+ 数据优势（推荐）+ 转换成本（创作者收入沉没）。
- **机制**：观众时长 → 吸引创作者 → 内容供给 → 更多观众；推荐算法用观看数据自我强化；创作者一旦在 YouTube 建立收入与订阅，迁移成本高。变现双引擎：广告 + 订阅（YouTube Premium/Music、电视端）。
- **证据 [source_id]**：
  - YouTube ads Q1 2026 **$9,883M，+11% YoY** [GOOG.A1.2026Q1.005] —— 双位数增长，网络仍在扩张但**增速低于 Search(+19%)**，是 Services 内相对较慢的引擎。
  - 计入 Google Services 合计 Q1 2026 **$89,637M，+16%** [GOOG.A1.2026Q1.009]。
  - **局限**：facts **未单独披露 YouTube 订阅营收、观看时长、创作者数**（藏在 Services 内）→ 网络效应的核心指标无法用 A1 直接验证（**open question**）。
- **指标（监控）**：观看时长、创作者/频道数、订阅用户与 ARPU、广告 vs 订阅占比（**均未在 facts → 需补**）。
- **Durability 三层**：
  - **1-2 年（Medium）**：广告 +11% 是正向但非强证据；缺时长/创作者一手数据，不能升 Strong。
  - **3-5 年（Medium）**：短视频（TikTok/Reels）争夺时长；AI 生成视频可能压低内容稀缺性也可能增产能。
  - **10 年（Watch）**：视频是否仍是稀缺注意力入口；版权/内容成本是否吞噬利润。
- **Attack surface**：
  1. **短视频平台**（TikTok）争夺时长与创作者。
  2. **AI 生成视频**改变内容供给经济学（双刃）。
  3. **创作者多平台分发**（Patreon/Substack/直接订阅）降低单平台锁定。
- **证据分级**：**Medium**（广告增速正向是 A1，但网络效应的本体指标——时长/创作者/订阅——在 facts 中缺失，无法证明"双边飞轮仍在加速"）。

---

### H5-4 Cloud 规模 + AI 基建（Google Cloud scale & AI infrastructure）

- **类型**：规模经济 + 转换成本（企业迁移/工作流）+ 成本优势（自研栈，见 H5-6 TPU）。
- **机制**：数据中心/网络规模摊薄单位成本；企业一旦上云、数据/应用迁移成本高（contract length、integrations）；AI 训练/推理需求把 Cloud 从"通用 IaaS"推向"AI 算力供给"，与 Gemini/TPU 全栈协同。
- **证据 [source_id]**：
  - Cloud FY2025 营收 **$58,705M（+36%）**，营业利润 **$13,910M**；**两年内 OI $1,716M→$6,112M→$13,910M**（微利→大幅盈利）[GOOG.A1.2025K.011 / .012]。
  - Cloud Q1 2026 营收 **$20,028M（+63% YoY）**，营业利润 **$6,598M**，**营业利润率 32.9%**（derived；Q1'25 ~17.8%）[GOOG.A1.2026Q1.010/.014/.015] —— **利润率一年翻近一倍是规模经济兑现的强证据**。
  - **Cloud backlog "over $460B"，环比近翻倍** [GOOG.A1.2026Q1.010 / block03] —— 远期合约锁定 = 转换成本 + 需求可见度的强信号。
- **指标（监控）**：Cloud 营收增速、营业利润率趋势、backlog/RPO、利用率（**利润率可持续性 = facts 已列 open question**）。
- **Durability 三层**：
  - **1-2 年（Strong）**：+63% 增速 + 32.9% 利润率 + $460B backlog [GOOG.A1.2026Q1.010/.015] 三重一手强证据。
  - **3-5 年（Medium）**：AWS/Azure 三强军备竞赛；利润率是否被价格战/利用率波动侵蚀（facts 警示：32.9% 可持续性待多季验证）。
  - **10 年（Medium/Watch）**：能否从"资本密集型公用事业"升级为"高回报平台"——取决于 TPU 成本优势(H5-6) + AI 工作负载锁定。
- **Attack surface**：
  1. **AWS/Azure + 专用 AI 云（CoreWeave 类）**价格/性能竞争压利润率。
  2. **大客户多云/自建**（超大规模 AI 客户自研芯片，如对手买 Nvidia 或自研）。
  3. **利用率/会计一次性**抬高的利润率回落（facts 明列此风险）。
  4. **capex 黑洞**：增量资本回报若 < WACC，则"规模"变成"负担"（见 §2 ROIC-WACC）。
- **证据分级**：**Strong（当下）**——增速、利润率跃升、backlog 三项均 A1 verified；但**利润率可持续性 = Medium**（单看一两季，facts 自身列为 open question）。

---

### H5-5 Android / Chrome 生态分发（Android / Chrome ecosystem distribution）

- **类型**：分销/入口 + 生态系统（多产品互锁）。
- **机制**：Android（移动 OS）+ Chrome（浏览器）+ Play + Gmail/Maps 控制用户进入路径，把搜索/广告/Cloud/订阅默认推到用户面前；多产品互相导流抬高整体沉没成本。这是 H5-1 搜索默认的**底层载体**。
- **证据 [source_id]**：
  - **facts 中无 Android/Chrome 用户规模、Play 营收、分发份额的 A1 数据**——这些在 10-K 内不单独披露。当前只能从 Google Services 整体规模 [GOOG.A1.2025K.009] **间接**推断生态分发在支撑变现。
  - 治理侧：三层股权使创始人保留 52.7% 投票权 [GOOG.A1.PROXY2026.004]——与生态无关，但意味着**生态/分发战略不受短期股东压力干扰**（双刃，见 operator 模块）。
- **指标（监控）**：Android/Chrome 装机与活跃、Play 营收、默认搜索协议金额与存续（**均未在 facts → 重大 open question**）。
- **Durability 三层**：
  - **1-2 年（Medium，证据弱）**：生态显然在运转（Services 规模为证），但**缺直接一手指标**，不能给 Strong。
  - **3-5 年（Medium/Watch）**：反垄断救济（DOJ search/adtech）可能强制开放默认、限制捆绑。
  - **10 年（Watch）**：移动平台范式若转向 AI 设备/agent OS，浏览器+搜索框入口价值可能下降。
- **Attack surface**：
  1. **反垄断结构性救济**：强制开放默认、禁止 Play 捆绑、甚至剥离 Chrome（曾被 DOJ 提议）。
  2. **平台范式迁移**：AI 原生设备/OS 绕过浏览器入口。
  3. **Apple 生态**封闭 + 自研 AI 入口切走高价值用户。
- **证据分级**：**Medium（机制可信但一手指标缺失）**；监管攻击面 = **Negative 倾向**（DOJ 案 [GOOG.A1.2025K.026 notes] 已部分败诉）。

---

### H5-6 TPU 自研芯片 / AI 成本结构（TPU & full-stack AI cost advantage）

- **类型**：成本优势 + 技术/工艺 know-how（垂直整合）。
- **机制**：自研 TPU + 自建数据中心 + 自研模型(Gemini) → 训练/推理单位成本理论上低于"买 Nvidia GPU + 通用云"的对手；全栈控制使 AI 产品（搜索 AI、Cloud AI、Gemini）成本结构更优 → 在 AI 军备竞赛中以更低成本提供同等算力。
- **证据 [source_id]**：
  - **这是 facts 中证据最薄的一条**：facts **没有 TPU 单位成本、自研 vs 外购占比、推理成本/query 的任何 A1 数据**。
  - 唯一间接证据：Cloud 利润率从 ~17.8%→32.9% [GOOG.A1.2026Q1.015] **可能**部分来自自研栈成本优势——但也可能来自规模/利用率/会计，**无法归因**（facts 列为 open question）。
  - 反向证据（成本压力）：**capex FY2025 $91.4B(+74%)、Q1'26 $35.7B(~2x)、2026 指引 $180-190B、2027 再显著增加** [GOOG.A1.2025K.016 / GOOG.A1.2026Q1.024 / GOOGL-424B5-2026-06.009]——TPU/数据中心是**巨额前置资本**，"成本优势"需在这笔资本上跑出回报才成立。
- **指标（监控）**：推理成本/query、TPU vs GPU TCO、Cloud AI 利润率归因、capex 增量回报（**全部未在 facts → 最大 open question**）。
- **Durability 三层**：
  - **1-2 年（Weak 证据）**：机制合理但**无一手量化**；Cloud 利润率跃升不能单独证明 TPU 优势。
  - **3-5 年（Medium/Watch）**：若 TPU 确有 TCO 优势，AI 推理规模化时是结构性护城河；若没有，则是 capex 黑洞。
  - **10 年（Watch）**：芯片/架构换代（对手追赶、Nvidia 生态、开源加速器）是否抹平自研优势。
- **Attack surface**：
  1. **Nvidia 生态 + 商用 GPU**性价比追上自研，抹平 TCO 优势。
  2. **对手也自研**（Amazon Trainium、Microsoft Maia、Meta MTIA）→ 优势相对化。
  3. **capex 增量回报 < WACC** → "成本优势"沦为重资产负担（核心风险，见 §2）。
- **证据分级**：**Weak（机制强但 facts 无量化）**。这是最被市场讲、却最缺一手证据支撑的护城河 → 必须降级处理，并把"成本优势能否兑现"列为头号 open question。

---

### H5-7 技术人才 / 模型（Talent & frontier models: Gemini / DeepMind）

- **类型**：技术/工艺 know-how（人才密度 + 模型能力）。
- **机制**：DeepMind/Google Research 人才密度 + 算力 + 数据 → 前沿模型(Gemini) → 反哺搜索 AI、Cloud AI、生产力套件；模型能力是承接"搜索护城河换形态"的关键载体（若搜索框被 AI 取代，Gemini 分发是接盘者）。
- **证据 [source_id]**：
  - **facts 中无模型能力/人才/Gemini 采用的 A1 数据**（benchmark、DAU、token 量均非 SEC 披露项）。
  - 间接：全公司营业利润率扩张（Q1'26 36.1%，+2pp [GOOG.A1.2026Q1.019]）+ Cloud AI 增长 [GOOG.A1.2026Q1.010]**暗示** AI 产品在变现，但不能直接归因于模型领先。
  - SBC FY2025 **$27.1B**（Note 13）[GOOG.A1.2025K.023]——巨额股权激励是"留住人才密度"的成本侧间接信号（也是 owner earnings 的拖累，双刃）。
- **指标（监控）**：模型 benchmark 相对位次、Gemini DAU/分发、AI 研发人才流入流出、token/推理量（**全部未在 facts → open question**）。
- **Durability 三层**：
  - **1-2 年（Weak 证据/Medium 机制）**：前沿模型梯队公认靠前，但**无 A1 量化**；竞争激烈（OpenAI/Anthropic）。
  - **3-5 年（Watch）**：前沿差距收敛快、人才流动性高 → 人才/模型本身是否构成持久护城河存疑（更可能是"分发×模型×数据"组合才有壁垒，单看模型不够）。
  - **10 年（Watch）**：模型可能商品化（开源追赶），护城河回落到分发(H5-1/5)+数据(H5-2)+成本(H5-6)。
- **Attack surface**：
  1. **OpenAI/Anthropic/开源**模型能力追平或反超。
  2. **人才高流动性**（明星研究员跳槽/创业）稀释密度。
  3. **模型商品化** → 单纯"模型领先"不再值钱。
- **证据分级**：**Weak（无一手量化）**。人才/模型更应视为**护城河的"换形态载体"而非独立护城河**——真正壁垒在它与分发/数据/成本的耦合。

---

## 2. ROIC–WACC 透镜（资本回报）

> **口径声明（重要局限）**：facts **未直接披露 ROIC / WACC / 投入资本(invested capital)**。以下为**粗略 derived 估算**，仅用于判断"回报水平量级"，**不可当精确 ROIC**。三个口径局限：
> ①分母（投入资本）无一手数据，只能用资产负债表片段近似；②营业利润含/不含一次性需调整；③AI capex 大量进在建工程、当期未折旧，使**当期回报被高估、未来折旧未充分反映**。

### 2.1 回报水平量级（基于 facts）

- **盈利能力极高（毛回报侧 Strong）**：
  - FY2025 营业利润 **$129,039M** / 营收 $402,836M = 营业利润率 **32.0%** [GOOG.A1.2025K.005/.006]。
  - Q1 2026 营业利润率进一步到 **36.1%（+2pp）** [GOOG.A1.2026Q1.019]。
  - Google Services 分部营业利润率 ~40.7%（derived [GOOG.A1.2025K.009/.010]）——核心广告业务是超额回报来源。
- **粗略资本基数（分母近似，仅量级）**：
  - 长期债务仅 **$46,547M** [GOOG.A1.2025K.021]，现金+有价证券 **$126,843M**（净现金为正）[GOOG.A1.2025K.020]——**历史上 Alphabet 是净现金、轻资本的高 ROIC 生意**，营业利润($129B)相对其有形投入资本，回报率历史上远高于任何合理 WACC（行业共识 ROIC 长期 20%+，**此为常识性判断，非 facts 直接证据**）。
- **WACC 量级（推理，非 facts）**：以净现金资本结构 + 大盘 beta，WACC 大致 8-10% 区间（**推理，无 source_id**）。
- **Spread（结论）**：历史 ROIC − WACC **显著为正且宽**（Strong）——这是"有护城河"在财务上最硬的证据：长期高营业利润率 + 轻资本 = 持续超额回报。

### 2.2 AI capex 抬升后：增量资本能否维持高回报？（核心矛盾）

这是整个护城河论点的**胜负手**。facts 已把矛盾摆清：

- **资本强度正在结构性抬升**：
  - capex FY2025 **$91,447M（+74%）** [GOOG.A1.2025K.016]；Q1'26 **$35,674M（~2.07x）** [GOOG.A1.2026Q1.024]。
  - **2026 指引 $180–190B，2027 再"显著增加"** [GOOGL-424B5-2026-06.009]。
  - FCF 被压缩：FY2025 derived FCF **$73,266M** [GOOG.A1.2025K.017]；Q1'26 stated FCF **$10,116M**、TTM $64,429M（**FCF 正被 capex 吃掉**）[GOOG.A1.2026Q1.025]。
  - **资本配置转向**：回购**暂停**（Q1'26 $0 vs Q1'25 $15B）[GOOG.A1.2026Q1.027]，转向 capex + 净发债 $31.4B（Q1'26 proceeds from debt $31,379M，见 facts §5 / block03）+ $80B 股权融资 [GOOGL-FWP-2026-06.001]。
- **关键问题**：增量资本（2026-27 合计 ~$370B+）投入 TPU/数据中心，其**增量 ROIC** 能否仍 > WACC？
  - **乐观侧（护城河成立）**：Cloud 利润率 17.8%→32.9% [GOOG.A1.2026Q1.015] + backlog $460B [GOOG.A1.2026Q1.010] 暗示需求真实、规模摊薄在兑现 → 增量资本可能维持高回报。
  - **悲观侧（护城河被军备竞赛拖累）**：若 capex 是"被竞争逼的军备竞赛"而非"主动高回报投资"，增量 ROIC 会向 WACC 收敛甚至跌破——重资产 + 折旧滞后 = 未来几年 owner earnings 被侵蚀。
  - **facts 自身的诚实警示**：①Q1'26 净利 +81% 被 **$36.9B 未实现股权收益**抬高，**营业利润 +30% 才是干净读数** [GOOG.A1.2026Q1.020/.022]——别用净利假象掩盖 capex 压力；②**capex 维护性 vs 成长性拆分缺失**（facts open question）——没有这个拆分，增量 ROIC 无法精算。
- **ROIC 透镜结论**：
  - **存量护城河 = Strong**（历史高 ROIC，宽 spread）。
  - **增量护城河 = 未证实（Watch）**——"AI capex 抬升后增量资本维持高回报"目前**只有间接乐观信号（Cloud 利润率/backlog），无 owner earnings 桥验证**。这是从 WATCH 抬到更高 verdict 前**必须**做的前置（指向 financial_quality / valuation 模块）。

---

## 3. Attack Surface 总表 + 三层时间测试 + Falsification

### 3.1 Attack Surface 汇总（含三层时间侵蚀）

| 护城河 | 主攻击路径 | 谁能攻 | 侵蚀时间窗 | 监控信号(挂 facts 指标) | 证据级 |
|---|---|---|---|---|---|
| H5-1 搜索分发 | AI 回答绕过搜索框 + 监管禁默认 | OpenAI/Perplexity/Anthropic/Apple；DOJ | 3-5 年(监管)/5-10 年(行为) | Search&other 增速[.2026Q1.004]、Services 利润率[.2025K.010]、TAC(缺) | Strong |
| H5-2 广告拍卖流动性 | DOJ adtech 结构性拆分 + 高意图迁移 + 信号衰减 | DOJ/EC；Amazon/TikTok/AI agent | 1-3 年(监管已动)/3-5 年(迁移) | Network 营收(**已降**[.2026Q1.006])、CPC(缺)、罚款[.2025K.026] | Strong(自有)/Negative(网络+监管) |
| H5-3 YouTube 网络 | 短视频夺时长 + AI 视频 + 创作者多平台 | TikTok；AI 视频；Patreon 类 | 3-5 年 | 观看时长/创作者/订阅(**全缺**)、广告增速[.2026Q1.005] | Medium |
| H5-4 Cloud+AI 基建 | 三强价格战 + 大客户自建 + 利用率回落 + capex 黑洞 | AWS/Azure/CoreWeave；超大客户 | 1-2 年(利润率)/3-5 年(格局) | 增速[.2026Q1.010]、利润率可持续[.015]、backlog[.010] | Strong(当下)/Medium(持续) |
| H5-5 Android/Chrome 分发 | 反垄断救济 + 平台范式迁移 + Apple | DOJ；AI 设备厂商；Apple | 3-5 年 | 装机/Play/默认协议(**全缺**)、DOJ 案[.2025K.026notes] | Medium/Negative(监管) |
| H5-6 TPU 成本 | Nvidia 追上 + 对手自研 + 增量 ROIC<WACC | Nvidia 生态；Amazon/MS/Meta 芯片 | 3-5 年 | 推理成本/TCO(**全缺**)、capex[.2025K.016/.2026Q1.024] | Weak |
| H5-7 人才/模型 | 对手追平 + 人才流动 + 模型商品化 | OpenAI/Anthropic/开源 | 1-3 年(差距收敛快) | benchmark/Gemini DAU(**全缺**)、SBC[.2025K.023] | Weak |

### 3.2 三层时间测试（整体生意）

| 时间 | 问题 | 当下判断（挂证据） |
|---|---|---|
| **1-2 年** | 数据是否仍支持 moat、无恶化？ | **多数 Yes**：Search +19% [.2026Q1.004]、Cloud +63%/32.9% [.2026Q1.010/.015]、11 连两位数季 [.2026Q1.001]。**例外恶化**：Google Network 营收下滑 [.2026Q1.006]；FCF 被 capex 压缩 [.2026Q1.025]。 |
| **3-5 年** | 竞争/客户/技术是否仍支持超额利润？ | **不确定**：DOJ search+adtech 结构性救济 [.2025K.026notes]、AI 回答侵蚀、capex 增量 ROIC 未证。胜负取决于**旧河削弱速度 vs Cloud/TPU/Gemini 新河形成速度**。 |
| **10 年** | 生意是否还在、客户是否仍为同一价值付费？ | **形态可能变**：搜索框可能让位于 AI/agent；护城河若能从"链接广告"迁到"AI 答案变现 + Cloud AI + 分发"则延续，否则削弱。**不能只靠历史优势论证未来**。 |

### 3.3 Falsification 清单（什么信号证明护城河比想象弱）

护城河比想象的弱，如果出现以下任一：

- [ ] **Search & other 增速连续两季 < 双位数甚至转负**，同时 AI 助手使用上升 → 搜索分发河正在被绕过（当前反例：Q1'26 +19% [.2026Q1.004]）。
- [ ] **Google Services 营业利润率持续下行**（破 ~38% 并续降）→ 定价权/拍卖流动性松动。
- [ ] **Google Network 营收继续萎缩并扩散到自有面**（当前已降 [.2026Q1.006]）→ 拍卖流动性边缘塌陷。
- [ ] **DOJ/EC 落地结构性拆分**（剥离 adtech 中介 / Chrome / 禁默认协议）→ 入口与拍卖中枢被强制改写 [.2025K.026notes]。
- [ ] **Cloud 营业利润率从 32.9% 显著回落**（证明是利用率/会计/一次性而非结构）→ 规模经济证伪 [.2026Q1.015]。
- [ ] **capex 持续超 $180B 但 Cloud backlog/增速停滞** → 增量资本回报跌向 WACC，capex 变黑洞 [GOOGL-424B5-2026-06.009 vs GOOG.A1.2026Q1.010]。
- [ ] **owner earnings 桥做出来后，维护性 capex 占比高、成长性 capex 增量 ROIC < WACC** → "增量护城河"证伪（核心待办）。
- [ ] **回购长期不恢复 + 持续靠发债/增发融 capex** → 现金生成无法自给 AI 投资 [.2026Q1.027 / FWP.001]。
- [ ] **Gemini/模型在前沿 benchmark 与分发上明显掉队** → 承接"搜索换形态"的载体失效（指标缺，需建监控）。

---

## 4. 证据分级汇总 + 负面信号入风险

### 4.1 各护城河证据分级

| 护城河 | 证据分级 | 一句话依据 |
|---|---|---|
| H5-1 搜索分发 | **Strong** | Services 高利润 + Search +19% 当下硬证据；削弱仅来自前瞻攻击面 |
| H5-2 广告拍卖流动性 | **Strong(自有面)** / **Negative(网络+监管)** | 自有面利润强；Network 已降 + DOJ/EC 监管落地 |
| H5-4 Cloud+AI 基建 | **Strong(当下)** / **Medium(可持续)** | 增速/利润率跃升/backlog 三项 A1；利润率可持续性待多季 |
| H5-3 YouTube 网络 | **Medium** | 广告 +11% 正向，但时长/创作者/订阅核心指标 facts 缺失 |
| H5-5 Android/Chrome | **Medium** | 机制可信、规模间接，但一手分发指标缺；监管偏负 |
| H5-6 TPU 成本 | **Weak** | 机制强但 facts 零量化；最被讲、最缺证据 |
| H5-7 人才/模型 | **Weak** | 无一手量化；更应视作"换形态载体"而非独立护城河 |

### 4.2 负面信号（→ 进 inversion / 风险模块）

明确的 Negative / 恶化读数（一手 A1）：

1. **Google Network 营收 YoY 下滑** [GOOG.A1.2026Q1.006] —— 站外拍卖流动性边缘萎缩（唯一直接收缩的广告分部）。
2. **FCF 被 capex 压缩**：Q1'26 FCF $10.1B、TTM $64.4B 且下行 [GOOG.A1.2026Q1.025]——护城河的"现金兑现"正被 AI 投资抽干。
3. **回购暂停** [GOOG.A1.2026Q1.027] + **靠发债/$80B 增发融 capex** [GOOGL-FWP-2026-06.001]——内生现金已不足以自给 AI 投资，资本回报承压信号。
4. **DOJ adtech 部分败诉，结构性救济"could have a material adverse effect"** [GOOG.A1.2025K.026 notes] + **EC €3.0B 罚款** [GOOG.A1.2025K.026]——监管攻击面已部分落地（不是假设）。
5. **2026 capex $180-190B、2027 再显著增加** [GOOGL-424B5-2026-06.009]——增量资本回报未证，是护城河"增量侧"的最大悬而未决风险。
6. **会计质量陷阱**：Q1'26 净利 +81% 被 $36.9B 未实现股权收益抬高 [GOOG.A1.2026Q1.020/.022]——易被误读为"护城河更强"，实则营业利润 +30% 才是真增长。

---

## Open Questions（触发回流补料 / 移交其他模块）

- [ ] **TAC（流量获取成本）趋势**：搜索分发河的成本侧，facts 未含 → 核 10-K（H5-1/H5-5 关键）。
- [ ] **CPC / 每次点击成本 + 广告主留存**：拍卖流动性的定价权读数，facts 缺（H5-2）。
- [ ] **YouTube 时长 / 创作者数 / 订阅营收**：网络效应本体指标，藏在 Services 内未单列 → 需补一手或行业数据才能把 H5-3 从 Medium 升级（H5-3）。
- [ ] **Android/Chrome/Play 装机与默认搜索协议金额**：生态分发硬指标，10-K 不单披露（H5-5）。
- [ ] **TPU 单位成本 / 自研 vs 外购 / 推理成本-per-query**：H5-6 全靠这些才能从 Weak 升级——**头号缺口**。
- [ ] **Cloud 32.9% 利润率归因与可持续性**：规模 vs 利用率 vs 会计一次性（facts 已列；决定 H5-4 是 Strong 还是回落）。
- [ ] **capex 维护性 vs 成长性拆分 + 增量 ROIC**：决定"AI capex 后能否维持高回报"——**移交 financial_quality / valuation 模块**，是 §2 结论从"未证实"变"成立/证伪"的前置。
- [ ] **Gemini/模型分发与 benchmark 监控**：承接"搜索换形态"的载体，需建立非 SEC 监控源（H5-7）。
- [ ] **DOJ/EC 救济最终判决**：把监管攻击面从"定性负面"量化为尾部风险（移交 inversion）。
- [ ] **Search & other FY2025 年度细分**：facts 仍为 seed_needs_audit [GOOG.SEED.SearchFY2025]——核 10-K 广告 disaggregation 表。
