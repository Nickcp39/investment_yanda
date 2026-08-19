# EROC Source Register

as_of: 2026-08-13 · 本文件记录源可达性与解除路径（沿用 `../../nbis/2026-08-12/source_register.md` 体例）

---

## 一手源状态：❌ 全部不可达

| 源 | 用途 | 状态 | 备注 |
|---|---|---|---|
| SEC EDGAR（10-Q / S-1 / 424B4 / Form 4） | Q2'26 原始报表、IPO 招股书、锁定期条款、内部人交易 | ❌ 出口代理拦截 | 与 NBIS 08-12 跑同因 |
| businesswire.com（Q2 PR 原文） | 财报新闻稿与管理层原话 | ❌ 拦截 | 检索可见标题，正文不可达 |
| 公司 IR / erock 官网 | 投资者演示稿、backlog 口径定义 | ❌ 未尝试成功 | |
| 财报电话会原始录音/官方 transcript | 管理层对交付节奏的原话 | ❌ | 仅有 investing.com 的二手转述 |

**后果**：本 dossier 全部数字为 **二手聚合源**，`claim_ledger.csv` 一律标
`unverified_secondary`。**按 lab 规则，裁决封顶在 WATCH 或更低，且完整度不得
标为高于 ~50%。**

> ⚠️ 本案比 NBIS 更严重的一点：**NBIS 至少有历史 dossier 三版可交叉**，
> EROC **无任何历史版本、无 10-K、无一年以上公开财报**。
> 二手源错误在这里没有任何内部校验机制。

---

## 二手源分级（本次实际使用）

| 层级 | 源 | 用途 | 可信度 |
|---|---|---|---|
| B+ | investing.com（财报 slides 报道 + 电话会 transcript 转述） | Q2 数字、管理层表态 | 转述完整但非原文 |
| B+ | stocktitan（10-Q 摘要） | 资产负债表项 | 结构化摘要，通常忠实 |
| B | tradingkey / simplywall.st / yahoo finance | 收入、backlog、比率 | 二次加工 |
| B | stockanalysis / CNN markets / tradingview | 价格、市值、52周 | 报价类可信度较高 |
| **C** | **美股投资网（TradesMax）微信文** | **触发线索** | **见下：定级依据** |

### 美股投资网的定级依据（重要）

本 lab 已有 `frameworks/meigu_touziwang_playbook.md`，明确定性：

> "This playbook treats the channel as **an idea and hypothesis source, not as
> validated evidence**. Any claim from these notes must still pass the source
> policy and claim-ledger process."

同时 `notes/videos/` 有该频道 **124 篇**存档笔记，可用于**主题谱系**判读：

| 时间 | 该频道的电力主题推荐 | 对象 |
|---|---|---|
| 2024-04-05 | "AI 耗电，3 只电力能源股必买" | **VST（明示 $70 附近合理进场）、CEG、NRG** |
| 2024-10-18 | "核能股暴涨，哪家最值得投资" | NNE / OKLO / LEU / SMR / CCJ |
| **2026-08（本次）** | **"EROC 值多少钱？三种情况"** | **EROC** |

**读数**：AI 电力主题在该来源已连续跑 **2.5 年、至少三代标的**
（公用事业 → 核能/SMR → **分布式快速发电**）。
标的一代比一代小、一代比一代早期。**这本身是主题成熟度的指标**，
与 `macro/ai_zeitgeist_timeline.md` 的"资金梯子往下走"读数一致。

> 用法：**该文的数字全部需核实（已在 Block 3 逐条核）；但该文的存在本身
> 是 SENTIMENT 层的一手证据**——它证明"AI 电力"叙事已下沉到中文散户渠道，
> 这条进 `../../../studies/…/舆论热度轨迹_2026-08-13.md` 的第五条规律
> （"被大众爱过"是风险因子）作为新样本。

---

## 解除路径（下次跑之前需要的）

1. **在可联网环境重跑**：取 10-Q 原文核对收入/毛利率/backlog 口径定义；
   取 424B4 招股书核对**锁定期条款与可解禁股数**（本案头号供给风险）。
2. **backlog 定义是本案的关键歧义**：需要一手文件确认
   "$1.7B contracted backlog" 里 take-or-pay 与 LOI 各占多少。
   二手源普遍只转述总数，不转述构成。
3. **等 2026-12 前后**：锁定期到期 + 第三份季报 + 首个 13F 窗口，
   届时才有最小可用的历史序列。
