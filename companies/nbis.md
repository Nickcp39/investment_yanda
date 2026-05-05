# Nebius (NBIS) - 投资简报

## Snapshot

- Company: Nebius Group N.V.
- Ticker: NBIS
- Exchange: Nasdaq (Yandex N.V. 拆分后于 2024 在阿姆斯特丹重组)
- Sector: AI 基础设施 / "Neocloud"
- Last updated: 2026-05-04
- 简报性质: 仅基于本仓库已收录的 TradesMax (美股投资网) 4 集主题视频
  + 3 集顺带提及。**所有数字都是该频道单方口径，未经一手验证**，
  需对照 NBIS IR 文件、20-F、季报方可入下一步研究。

## Source Tier (按 sources/source_policy.md)

| 来源 | 等级 | 用途 |
| --- | --- | --- |
| TradesMax (美股投资网) YouTube 视频 x 4 | 市场评论 / 二次解读 | 仅作叙事样本与待验证线索池，**不可作事实** |
| 一手 IR / SEC / 财报 | 暂未收录 | 下一步必须补 |

## Research Question

NBIS 在 2024-12 (~$28) → 2025-09 (~$114) 走了一段大行情。当前价位下，
是否值得进 starter / core，还是应当 watch 或 reject？

## Business Overview (视频口径)

- 业务: 全栈式 AI 专用云。底层硬件 + 网络调度 + 集群优化 + AI Studio
  平台一体化交付。
- 配置: H100/H200 起步，已上 GB200，规划 GB300 (液冷)。InfiniBand
  互联。
- 物理 footprint: 芬兰自建数据中心 (自然冷却) + 巴黎节点 + 新泽西
  Vineland 在建。
- 关联资产: 子公司 Toloka (数据标注) / TripleTen (AI 培训) / Avride
  (自驾, 与 Uber 合作); ClickHouse 28% 股权 (B 轮估值 $20 亿)。
- 关键合作: 2025-09 微软签 $174 亿多年期合作 (视频口径); NVIDIA 持
  NBIS ~120 万股 (13F 口径, 视频引用)。

## 待验证事实清单 (视频→需到一手补)

| 项目 | 视频声称 | 验证渠道 |
| --- | --- | --- |
| 2024 全年营收 | $117M (vs 2023 $21M) | 20-F / Q4 release |
| 2024Q4 营收 | $38M | Q4 release |
| 2025Q1 ARR | $200M | Q1 release / IR deck |
| 2025 全年指引 | $700M | IR guidance |
| 现金储备 | $20 亿+ | 资产负债表 |
| 2025 计划 capex | $10 亿+ | management commentary |
| 微软合同 | $174 亿、多年期 | 8-K / 公司公告 |
| GPU 数量 | 2024 末 2 万 → 2025 3.5-6 万 | IR deck |
| EBITDA 转正 | 2025 内 | guidance / 季报 |
| NVIDIA 持股 | ~120 万股 | NVIDIA 13F |

⚠ 所有以下 agent 判断**假设上述数字大体属实**。任何一项被一手数据
证伪，对应判断需要重写。

---

## Agent Panel

### Tier A (memo-ready)

**Buffett — 业务主人视角**

NBIS 当前 owner earnings 是负的: capex 远超营收 ($10 亿 vs $700M
指引)，FCF 不可能为正。管理层背景特殊: 拆自 Yandex N.V.，2024 年才
完成俄罗斯业务剥离，新公司在阿姆斯特丹。资本配置历史**短且复杂**，
没法用 10 年 owner letter 评估。生意本身要求"准确预测 GPU 周期 + AI
capex 周期 + hyperscaler 战略" — 这不是简单的 owner-operator 生意。

判断: **不在能力圈、非 buy-and-hold-forever 候选**。Buffett 不会买。

---

**Marks — 周期与共识**

红旗清单:
1. Neocloud 这个标签从"小众挖掘"变成"博主反复推介"，TradesMax 自身
   就是迹象。
2. 微软合同公告后单天 +70%，9 月 26 日视频时 5 个交易日再涨 22% —
   "好消息已经被 price in"的典型形态。
3. 资金面: AI capex 周期处于狂热中后段。NVIDIA "AI 央行"叙事 (1000
   亿投 OpenAI、10GW、入股 Intel) 是顶级反身性燃料。

下行非对称: 客户跳船条款 + GPU 折旧 + hyperscaler 自研芯片这三件事
任意一件兑现，估值压缩可能 50%+。当前价位**没有充分补偿这种非对称
风险**。

判断: **second-level 结论是 watch / 不追**。

---

**Greenblatt — Magic Formula**

ROC 当前为负，earnings yield 无意义。公式直接 reject。**不要逼公式
做它做不了的事**。该 agent 在此案保持沉默。

判断: 跳过。

---

**Graham — 撑得住吗**

无利润、无 asset 安全边际，传统 Graham 框架不适用。但他能给一个有
用的子问题: 现金跑道。
- 现金 $20 亿 + 营收 ~$700M (假设兑现) - capex $10 亿+ - 运营烧钱
- → 2026 中前后大概率需要再融资。
- → 含义: 当前股东几乎肯定要承担**未来 12-18 个月内的稀释风险**。

判断: 非 Graham 候选，但贡献关键发现 — **稀释是定价中应当扣除的隐
性成本**。

---

### Tier B (memo with human review)

**Munger — 反过来想，三大致命路径**

1. **客户跳船**: 微软合同据视频包含 take-back 条款 (CRWV + OpenAI
   合同的同款逻辑)。微软自有 Azure capacity 一旦补上，订单即可削减。
   HSBC 已对 CoreWeave 给"减持 / 目标价低 77%"，同样逻辑直接适用 NBIS。
2. **GPU 折旧加速**: B200 → GB200 → GB300 → Rubin 节奏越来越快。
   两年前买的卡今天就接近残值。Capex 资本化 + 折旧表的一致性是关键
   财务质量信号。
3. **Hyperscaler 反扑**: Google TPU、AWS Trainium、Azure Maia 量
   产 + 内部价格战 → neocloud 商品化压扁。

判断: 三条任一条都能击穿 thesis，需要**显式的早期预警指标**而不是
"等到发生再说"。

---

**Fisher — Scuttlebutt 计划 (不是结论)**

仓库内信息**完全不够下结论**。需要补:
- 微软之外锚定客户名单 (Anthropic? Apple? Mistral?)
- 续约率、合同条款 (take-or-pay 还是按使用付费)
- 开发者社区 (Reddit / HN / Twitter) 对 NBIS AI Studio 真实评价
- Yandex 拆分后核心工程团队留存率
- 欧洲与美国销售组织搭建进度

判断: **挂"信息不足"标签**，不投票。

---

**Lynch — 分类**

教科书 fast grower。简单故事: "AI 算力里的台积电代工版本，但只有
一家客户 (微软) 锁定基本盘"。

但: $223 亿市值 / $700M 营收 ≈ 32x P/S。Lynch 的标准警告: "fast
grower with stretched valuation and slowing unit economics"。如果
2025-2026 收入加速放缓 + 利润率不达预期，估值修复幅度大。

判断: **故事简单，估值不简单**。

---

**Terry Smith — Quality compounder?**

不是。当前: ROIC 负、capital intensity 极高、pricing power 微弱
(GPU 商品 + 客户集中)、recurring revenue 主要靠合同而非品牌粘性。
Terry Smith 框架直接 fail。

未来可能转 quality? 取决于**单位经济跑通 + 利用率达 70-90%**。这
是远期看涨情景的核心成立条件，不是当下事实。

判断: 现在不是 quality compounder。**远期能不能进，要看运营杠杆
真实数字。**

---

### Tier C / Hold (supporting lens, 不作决策依据)

**Soros — 反身性 (Hold 状态，但本案高度适配)**

教科书反身性循环:
融资 → 买 GPU → 锁合同 → 营收增 → 估值飙 → 再融资 → 买更多 GPU。

关键脆弱点: **流动性环境**。低利率/宽松信贷下循环放大；紧缩时同
一循环倒转 — GPU 折价、合同削减、再融资困难、估值雪崩。NBIS 高度
暴露于宏观流动性 regime。

NVIDIA "AI 央行"叙事 (1000 亿、10GW、ONO 铁三角) 是该反身性的**整
个赛道层面**，不仅 NBIS 单家。

**支持视角，非决策依据**。

---

**段永平 — Do-not-do**

- 是否被叙事拉走? 视频本身充满"翻倍潜力 / 散户专属机会 / 别错过"
  营销话术 — 兴奋驱动信号强烈。
- 真的愿意 100% 买下 NBIS 吗? 答: 不能，因为不真懂业务长期形态、
  治理 (Yandex 遗留)、和用户黏性。
- 用户黏性: 弱。客户切换 NBIS → CRWV → Lambda 的物理成本不高 (主
  要是模型权重搬迁 + 合同重谈)。

**支持视角**: 该案在段永平"不为清单"上的概率高 — 不在叙事高峰追。

---

## Verdict

**Watch — 不开仓**

理由:
1. 业务确实位于赛道正中 (neocloud 是真实存在的市场结构现象)。
2. 但当前估值 (~32x P/S) 已经反映了乐观情景。
3. 三大失败路径 (客户跳船 / GPU 折旧 / hyperscaler 反扑) 中任一条
   兑现都会带来非对称下行。
4. 一手数据缺位 — 当前所有判断都依赖 TradesMax 单一二手来源。
5. 几乎肯定 12-18 月内有稀释风险，未充分定价。

## Kill Criteria (会让我重新评估的事)

进 watch 触发:
- 估值压缩 30-50% (P/S 从 32x → 15-20x)
- 第二个锚定大客户公开 (Apple / Anthropic / Mistral 量级)
- EBITDA 转正路径用一手财报验证
- 新一轮再融资完成 + 稀释幅度可接受 (<10%)

转 reject 触发:
- 微软合同条款披露包含明显 take-back 条款 + 客户集中度 >60%
- 利用率指引低于管理层目标 70% 显著差距
- GPU 折旧政策被会计师/审计师下调
- 美/欧出于俄罗斯遗产或技术出口管控启动审查

## Next-Step Research (按优先级)

1. **拉一手财报**: NBIS 最新 20-F / Q1-Q4 季报 / IR investor day
   deck，验证上面"待验证事实清单"中每一行。
2. **微软 8-K / 合同披露**: 看 take-back 条款、定价机制、是否
   take-or-pay。
3. **NVIDIA 13F**: 验证持股口径与时间。
4. **Scuttlebutt**: Reddit r/MachineLearning + HN + 开发者评价。
5. **可比公司**: CoreWeave (CRWV) Q 报 + HSBC 减持研报，对照逻辑
   是否对称适用 NBIS。
6. **拆分文件**: Yandex N.V. 重组的 SEC 文件，了解资产/负债边界、
   俄罗斯业务剥离条款、是否存在 contingent liability。

## Sources (本简报)

| 视频 | 日期 | 路径 |
| --- | --- | --- |
| 抓住美股年底AI机会 NBIS 首推 | 2024-12-06 | notes/videos/2024-12-06_Bn-xmMi0Yj8_*.md |
| 7月必买AI基建股 NBIS Neocloud 论 | 2025-07-18 | notes/videos/2025-07-18_sFNt8cBzSBg_*.md |
| AI 股暴涨/英伟达危机/IREN-NBIS-ORCL | 2025-09-12 | notes/videos/2025-09-12_0Vz8JDQ46pE_*.md |
| 英伟达 AI 央行 / 1000 亿 / ONO 铁三角 | 2025-09-26 | notes/videos/2025-09-26_wvCWF6zz_Bc_*.md |

source_policy 等级: 全部为市场评论/二次解读，**作叙事样本，不作事实**。

---

> 本简报由 Tier A panel (Buffett/Marks/Greenblatt/Graham) + Tier B
> panel (Munger/Fisher/Lynch/Terry Smith) + Tier C/Hold supporting
> lens (Soros/段永平) 跑完。Tier C/Hold 仅作支持视角。最终决策口径
> 来自 Tier A + Tier B 加权。
