# ADBE Business Model (M2 Theme / Mechanism)

Last updated: 2026-08-07 | as_of: 2026-08-07 | sources: facts.md E1–E10、`raw/primary_extracts.md`
Module M2 · role: context + conviction · **Signal: +1** · confidence: med

---

## 0. 一句话机制

Adobe 卖的是**「内容生产的工具 + 内容的容器 + 内容的分发/度量」**三层订阅。97.0% 的收入是订阅（Q2 FY26：$6,416M / $6,618M），资本开支只占收入 0.80%，FCF 利润率 40.8%。
**这是一台几乎没有实物资本消耗的现金机器**——与 GOOGL 当前 capex/OCF 71%、FCF 转负的形态完全不是一个物种。

问题从来不是这台机器现在好不好（它很好，M4 = +2），而是：**生成式 AI 会不会让「工具」这一层变得不必要。** 本文件的任务就是把收入**按被替代风险分层**，并诚实标出哪些层公司根本不披露。

---

## 1. Adobe 现在怎么切分自己（口径已经变过两次）

### 旧口径（至 FY2025，已停用于指引）：三个报告分部
| 分部 | FY2025 收入 | 占比 | FY2023→FY2025 |
|---|---:|---:|---|
| Digital Media | **$17,649M** | 74.3% | 14,216 → 15,864 → 17,649 |
| Digital Experience | **$5,864M** | 24.7% | 4,893 → 5,366 → 5,864 |
| Publishing & Advertising | $256M | 1.1% | 300 → 275 → 256（**萎缩中**，Q2 FY26 已就该报告单元计提 $70M 商誉减值） |

**FY2025 10-K（verbatim）**："Effective in the first quarter of fiscal 2026, we will combine our prior segments—Digital Media, Digital Experience and Publishing and Advertising—**into a single operating and reportable segment**."

### 新口径（FY2026 起）：两个「客户组」订阅收入
定义出自 Q1 FY2025 8-K（**verbatim**）：
> "**Business Professionals and Consumers Group** will consist of all subscription revenue from **Document Cloud**, **Acrobat subscription revenue in Creative Cloud**, and **Adobe Express subscription revenue in Creative Cloud**, all of which are part of Digital Media. **Creative and Marketing Professionals Group** will consist of all subscription revenue from **Digital Experience** as well as all of the remaining subscription revenue from Creative Cloud in Digital Media."

| 客户组 | Q2 FY26 订阅收入 | 占总收入 | FY2025 | FY2026 指引 |
|---|---:|---:|---:|---:|
| **Business Professionals & Consumers**（Document Cloud + Acrobat + Express） | **$1,853M（+16.2%）** | 28.0% | $6.50B（+15%） | $7.44–7.48B |
| **Creative & Marketing Professionals**（Digital Experience + 其余 Creative Cloud） | **$4,537M（+12.9%）** | 68.6% | $16.30B（+11%） | $18.21–18.27B |
| 非订阅（产品 $89M + 服务 $113M） | $202M | 3.1% | ~$0.97B | — |

> **注意**：BP&C 增速（+16.2%）**持续快于** C&MP（+12.9%），FY2025 也是 15% vs 11%。**Adobe 增长最快的部分是文档/消费者端，不是创意专业端。** 这一条对下面的分层结论很重要。

---

## 2. 收入按「AI 替代风险」分层（本 dossier 的核心推算）

用两组披露交叉推算（**推算，非公司披露**）：
- Digital Experience FY2025 订阅收入 = **$5.41B**（披露）
- C&MP FY2025 = **$16.30B**（披露）
- → **Creative Cloud 专业端（不含 Acrobat/Express）≈ $16.30B − $5.41B = $10.89B**

| 层 | 内容 | FY2025 收入 | 占比 | **AI 替代性质** |
|---|---|---:|---:|---|
| **L1 文档 / PDF 容器** | Document Cloud、Acrobat、Acrobat Sign | **~$6.5B**（BP&C，含 Express） | **27.3%** | **结构性受保护**——PDF 是 ISO 32000 国际标准，Acrobat 是标准的参考实现；企业合同、法务、合规、政府文件的**归档格式**不会因为模型变强而改变。AI 在这里是**增强**（AI Assistant 读文档）而非**替代** |
| **L2 创意专业工作流** | Photoshop / Illustrator / Premiere Pro / After Effects / Lightroom / InDesign | **~$10.89B（推算）** | **45.8%** | **混合，最有争议**。「生成一张图」被完全替代；「在 4K 时间线上做 200 层调色 + 音频往返 + 团队审校 + 交付母版」没有被替代。项目文件格式（.psd/.ai/.prproj/.aep）、插件生态、受训操作工、片厂流程是真实切换成本 |
| **L3 企业营销/内容运营** | Adobe Experience Platform、Real-Time CDP、Analytics、AEM、GenStudio、Journey Optimizer | **$5.41B** | **22.8%** | **结构性受保护**——多年期企业合同（RPO $22.27B）、客户数据驻留、与 CRM/广告栈的集成、实施周期以年计。AI 反而**扩大**需求（内容量爆炸 → 更需要编排与度量） |
| **L4 遗留** | Publishing & Advertising | $0.26B | 1.1% | 已在萎缩，Q2 FY26 计提商誉减值 |

**分层结论**：
- **约 50% 的收入（L1 + L3）坐在结构性锁定层**——PDF 标准 + 企业多年合同。这两层被生成式模型直接替代的路径不清楚。
- **约 46% 的收入（L2）坐在真正有争议的那一层**，而且 **Adobe 从不披露 L2 内部「生成 vs 编辑工作流」的收入拆分**。
- **Express（被 Canva 正面攻击的产品）被塞在 BP&C 里，与 Acrobat 混在一起，无法分离。** 这意味着 BP&C 的 +16% 增速里，有多少来自 Acrobat（安全）、多少来自 Express（战场），**外部无法判断**。这是 (c) 无法完全量化的直接原因。

---

## 3. AI 替代机制：按层说清楚，不说笼统话

### 3.1 真被替代的：**单点图像/视频「生成」**
- 攻击者：OpenAI、Google（Gemini / Veo / Imagen 系）、Midjourney、Runway、Black Forest Labs、字节系视频工具。
- 机制：过去要在 Photoshop 里花 40 分钟合成的一张主视觉，现在一句 prompt 出图。
- **但这一层 Adobe 本来就几乎没有直接收入**：Firefly 是 Photoshop/Premiere **内部的功能**，不是独立收入线。**AI-first ARR = $500M+ = Total ARR $27.10B 的 1.8%**（推算）。
- **真实风险不是「Adobe 的生成收入被抢」，而是「生成变强到让编辑器本身失去必要性」**——即 L2 的入口被绕过。这是本论点唯一真正的杀伤路径，见 `inversion_map.md` F1。

### 3.2 没被替代的（且证据在披露里）：**工作流、格式、协作、合规、资产管理**
| 机制 | 为什么模型变强不解决它 | 可观测证据 |
|---|---|---|
| **文件格式引力** | .psd/.ai/.prproj/.aep 是**团队之间交换未完成工作**的载体。一个人的成品可以被 AI 替代，一条 12 人流水线的**中间态**不行 | 无直接披露（**OPEN**） |
| **PDF / ISO 32000** | PDF 是国际标准，不是 Adobe 的私有格式——但**这恰恰是护城河的形态**：标准由 Adobe 提出并被 ISO 接纳，Acrobat 是事实上的参考实现。法务/合规/政府归档的**保真要求**与模型能力无关 | BP&C 收入 **+16.2%**，是全公司增长最快的部分 |
| **团队协作 / 评审** | Frame.io（2021 收购）、Creative Cloud Libraries、AEM Assets —— 多人评审、版本、权限、时间码批注 | 无单独披露（**OPEN**） |
| **合规 / 电子签名** | Acrobat Sign 的法律效力链、审计轨迹 | 无单独披露（**OPEN**） |
| **企业合同惯性** | AEP/Analytics 的实施周期以年计，数据驻留在 Adobe 侧 | **RPO $22,270M**、cRPO 67% ——**这是分层里唯一有硬数字的锁定证据** |
| **商业使用的赔付/来源可信** | 企业客户需要「训练数据干净、可商用、有赔付」的生成来源，以及内容溯源（Content Authenticity / C2PA） | 无收入披露（**OPEN**） |

### 3.3 Adobe 自己的 AI 变现：**在捕获，但规模还很小，且关键口径「有定义无数字」**
| 指标 | 披露值 | 读法 |
|---|---|---|
| **AI-first ARR** | Q2 FY26 **「超过 $500M」，同比三倍**；FY2025 年末目标 $250M | **真捕获了，但只占 Total ARR 的 1.8%**。三倍增长是真的，基数也是真的小 |
| **Total AI-Influenced ARR** | **Adobe 在 Q4 FY2025 新闻稿术语表里给了完整定义，正文不给数字** | **这本身就是一条发现**（见下） |
| Firefly 独立收入 | **从未在一手文件中披露** | 二手转述「接近 $300M、环比 +50%」，本 run 未取得逐字稿确认（facts.md **O2**） |

**关于「有定义无数字」——按本 lab 处理 Wiley AI 授权行的同一标准处理**：
Adobe 花笔墨定义了 "Total AI-Influenced ARR"（"ARR from the product offerings and tiers that the customers select that are **enhanced by** AI features…"），却不在新闻稿里给数字。这个指标的构造本身就值得警惕——它统计的是**「客户选的那个档位里恰好含 AI 功能」的全部 ARR**，而不是**客户为 AI 多付的钱**。按这个定义，只要把 AI 功能塞进主力档位，这个数字可以逼近 100% 的 ARR 而**不代表任何增量变现**。
**结论：Adobe 既不是在纯粹捕获 AI 收入，也不是在纯粹送——它在用 AI 功能保住既有档位的定价权，同时用一条口径宽松的指标去讲这个故事，而把真正窄口径的那条（AI-first ARR，$500M，1.8%）诚实地小规模披露。** 这是三者中最接近真相的读法，且**是本 dossier 对 (d) 的答案**。

### 3.4 战略转向：**免费增值（freemium）**
Adobe 在 FY2026 把 Acrobat / Express / Firefly 推向低摩擦免费入口，并**主动承认这会压低短期 ARR 增速**。这解释了 FY2026 ARR 指引的隐含有机降速（10.2% 含并购 → 有机 ~8.3%，推算）。
- **多头读法**：这是主动选择——用 ARR 换用户规模，为后续转化蓄水。收入增速同期在**加速**（12.0% → 12.7%）支持这个读法。
- **空头读法**：这是被迫应战——因为 Canva 的免费层已经把入口拿走了，Adobe 只能跟。
- **本 dossier 的立场**：**两者的可观测后果在未来两到四个季度是一样的（ARR 增速下滑），无法用现有披露区分。** 这正是 M2 只给 +1 而不给 +2 的原因。

---

## 4. 经济机器的质量（支撑 M4 = +2）

| 指标 | Q2 FY26 / TTM | 读法 |
|---|---:|---|
| 订阅收入占比 | **97.0%** | 几乎全经常性 |
| 毛利率 | **89.2%**（$5,903M / $6,618M） | 软件本色 |
| non-GAAP 营业利润率 | **44.5%**（指引 ~45%） | |
| **TTM FCF 利润率** | **40.8%** | $10,280M / $25,198M |
| **capex 占收入** | **0.80%** | **$201M TTM** —— 对比 GOOGL 的资本黑洞，这是完全不同的物种 |
| R&D 占收入 | 18.1% | $1,198M/季，持续投 AI |
| 递延收入 | $7,250M | 现金先收 |
| RPO / cRPO | **$22,270M / 67%** | 已签约未确认收入，锁定度的硬证据 |
| 股本变化（4.5 年） | **481M → 402M（−16.4%）** | 回购完全覆盖 SBC |

**唯一的财务瑕疵**：FY2025 回购 $11,281M = 当年 FCF 的 **114%**，把净现金烧成 **$1,019M 净负债**。这不可长期持续（见 `inversion_map.md` F5 / K-F）。

---

## 5. 十年后这门生意还在不在？

**大概率在，但形态可能不同。** 三条分开判断：
- **L1（PDF/文档，27%）**：**极大概率还在，且更强**。ISO 标准 + 合规归档 + 企业签名，被生成式模型替代的路径不成立。BP&C 增速 +16% 是全公司最快的，这是最被低估的一块。
- **L3（企业营销，23%）**：**大概率还在**。AI 让内容产量爆炸 → 编排/度量/合规的需求上升而非下降。RPO 提供了 2–3 年的可见度。
- **L2（创意专业，46%）**：**这是唯一真正的赌注**。如果十年后专业内容生产的入口是「对话式生成 + 轻量修改」而不是「时间线 + 图层」，Adobe 在这一层的定价权会被重构。**本 run 无法给这条定价**（facts.md O8：竞争对手一手财务全部缺失）。

**因此 M2 = +1（不是 +2）**：机制本身健康、可观测、在加速；但机制的**耐久性**在占收入 46% 的那一层无法证实，且公司刚刚把能证实它的披露撤掉了。
