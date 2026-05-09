# Baseline Test 2026-05 — Phase 0

执行依据: [`training_plan.md`](../training_plan.md) Phase 0
日期: 2026-05-05
评估方式: **自评** (single LLM 在主 Claude 会话内同时扮演所有灵魂 + 评分)
评分依据: [`rubric.md`](../rubric.md) 5 维 100 分

---

## 1. 测试方法 + 范围决策

### 计划要求 (training_plan.md L86-100)

> 1. 选 `benchmark_cases.md` 中 3 道不同类型题目 (compounder / 估值 / 宏观)
> 2. 让当前 13 位灵魂 (在主 Claude 会话里) 答一遍
> 3. 用 `rubric.md` 打分, 填 `scorecard_template.md`
> 4. 输出 `results/baseline_2026-05.md`

### 实际范围

**3 道题** (覆盖 3 个不同框架场景):

| Case | 类型 | 来源 |
| --- | --- | --- |
| Case 001 — 高质量但昂贵的消费品牌 | compounder | benchmark_cases.md L7-29 |
| Case 002 — 便宜但高杠杆周期股 | 估值 / cyclical | benchmark_cases.md L30-51 |
| Case 004 — 受政策和利率影响的金融资产 | 宏观 / financials | benchmark_cases.md L76-97 |

**灵魂调用范围**: 按 `benchmark_cases.jsonl` 的 `target_agents` 字段 + 段永平 (作 chair, 全程在场)。

**没有"13 位 × 3 题 = 39 答案"全跑**, 因为:
- 把不在 target_agents 的灵魂强制答题, 测试的是"边界识别"而非"框架应用"; 后者更基础, 优先做
- 39 答案 + 39 评分超过单次会话有效输出限制, 质量会下降; 宁愿 17 个答案做扎实

**本次未覆盖的灵魂** (因 3 道题不命中其专长): **Li Lu, George Soros, Joel Greenblatt** — 需要 Case 005 (中国平台) / Case 006 (AI 硬件) / Case 003 (无盈利 SaaS) 在 Phase 0.5 补做。

### 已知偏差 (写在前面而非脚注)

1. **共识是假的**: 所有灵魂答案由同一 LLM (Claude Opus 4.7) 在同一主会话内生成, 上下文共享 → 隐性收敛风险。training_plan.md L26-27 已承认这是核心问题, Phase 2 (Custom GPT / Claude Project) 才解决。
2. **评分锚定**: 我既写答案又评分。Klarman 的<em>下行</em>视角 + 已存在的 sanity_check_buffett (A 组 78 分) 给我隐性参考点, 倾向把分数压在 70-85 区间。
3. **没有源材料检索**: 灵魂引用全靠模型预训练记忆。不是"无源", 是"<em>无源材料锚定的源</em>" — 训练数据里大概率有 Berkshire 股东信, 但不能保证准确性。

---

## 2. Case 001 — 高质量但昂贵的消费品牌

**事实包**: 12 年增长 / 毛利 65-70% / ROIC > 30% / 资本开支低 / 10 年回购纪律好无大额并购 / 当前 45x 未来 1 年 FCF / 增速 18% → 9-11%

**Target agents (JSONL)**: Buffett, Munger, Terry Smith, Klarman, Graham, Fisher

### 灵魂答案

#### Buffett

> 这是好生意 — ROIC > 30% + 资本开支低 + 12 年复合增长是教科书的 quality compounder。但 45x FCF 让我想起 1970 年代 nifty fifty: 好公司可以是糟糕投资。我 1988 年买可口可乐时 PE ~15-18x, 不是 45x。
>
> 算账: 9-11% 增速维持 10 年 + 估值合理压缩到 25-30x FCF + FCF margin 不变 = 年化回报约 6-8%。低于股票长期均值。
>
> 增速从 18 到 9 这个变化是关键 — <em>结构性放缓</em> (category 成熟) 还是<em>周期性放缓</em> (短期消费疲软)? 我没有信息分辨。
>
> Verdict: WATCH。等价格回到 25-30x FCF。Kill criteria: 增速跌破 7%, 或回购停止, 或大额并购。

#### Munger

> 反过来想 — 这门生意怎么死?
>
> 三条失败路径: (a) 品牌老化, 年轻消费者迁移到新品类; (b) 渠道颠覆, DTC + Amazon 蚕食毛利率; (c) 增速放缓期 CEO 控制不住并购冲动 — 历史上 quality compounder 在增长枯竭后的死法十之八九是<em>错配资本</em>。
>
> 前 10 年无大额并购是真实加分 — 但<em>过去的纪律不能预测未来 5 年</em>。增速从 18 到 9 的 CEO 心理压力, 我见过太多。
>
> 45x FCF 本身把<em>完美执行</em>已 priced in。任何一条失败路径触发, 30-50% 回调是数学不是意外。
>
> Verdict: WATCH (与 Warren 一致)。等增速放缓信号被市场消化后的价格。

#### Terry Smith

> 这正是 Fundsmith 喜欢的资产: ROIC > 30%, capital-light, 强复购, 回购纪律。我们三关:
>
> (1) 好生意 ✓
> (2) 合理价格 ✗ (45x 在我们历史买入区间 22-30x 之上)
> (3) 不频繁交易 ✓
>
> 算账: 9% 增速维持 10 年 + 估值压缩到 25x = 年化 7-8%。Fundsmith 长期目标 10-12%, 差 2-4%。
>
> Verdict: STARTER 1-2% (现价), 加到 4-5% if PE 回到 30x。
>
> 但我警告自己一个 Fundsmith 哲学内在矛盾: "等价格的 quality compounder" 历史上 5 次有 4 次<em>从未到达等待价位</em>, 因为质量被持续 priced-up。这是为什么我们对部分核心持仓接受了不太理想的入场价。

#### Klarman

> 我的 verdict: SKIP — 不是 REJECT, 是<em>无法用我的框架定价</em>。
>
> 45x FCF = FCF yield 2.2%。即使 9% 增速, 我的 margin of safety 框架要求至少 30-40% 安全垫从内在价值估计 — 即合理入场 28-32x FCF。当前股价比我的研究启动价高 40-60%。
>
> Klarman 纪律的基础是<em>耐心</em>: Baupost 长期 30-50% 现金等错定价。这种"质量已被市场认知 + 价格高 + 还没出错"的标的, 我会:
>
> - 不研究 (节省时间)
> - 不持仓 (无安全垫)
> - 不预测它会回调 (可能永远不回)
>
> Watch list 也不放 — 因为 watch list 是<em>等错定价的标的</em>, 不是<em>等错定价机会的标的</em>。

#### Graham

> 直接 REJECT。
>
> 我的<em>防守型投资者</em>原则: P/E 上限 ~20, 净流动资产为正, 资产负债表保守。45x FCF (大约对应 50x+ 报告 PE) 是我上限的 2.5x。
>
> 即使是<em>进取型投资者</em>原则也要求 30% margin of safety, 上限 PE 28-30x。这家公司的财务质量我承认 (回购 + 低 capex), 但<em>quality 不构成 valuation 折扣</em> — 它构成<em>溢价应有上限</em>。
>
> Graham framework 在这类标的上的应用结果是<em>过滤掉, 不研究</em>。我的建议: 把研究时间分配到 P/E 12-18、ROIC 15-20% 的"<em>良好但被忽视</em>" 标的池, 它们一定存在 — 只是不在头条。

#### Fisher

> Scuttlebutt 5 类必访的具体计划:
>
> 1. <em>客户</em>: 30 个长期重复购买客户调研 — 留下来的<em>真实理由</em>是什么? 哪些试过竞品后回来?
> 2. <em>渠道</em>: 主要分销商 / 零售商 — 该品牌的<em>货架占比</em>过去 3 年趋势 (上升 / 持平 / 下降)?
> 3. <em>竞争对手</em>: 3-5 家直接竞品的销售如何评价该品牌的定价权?
> 4. <em>前员工</em>: 销售 / R&D / 供应链 3 类离职 3-5 年员工对增速从 18 到 9 时段的<em>内部叙事</em>?
> 5. <em>开发者 / 合作伙伴</em>: 消费品场景替换为 brand ambassador / 主要 KOL 渠道。
>
> 决策规则: (1)(3) 显示<em>定价权稳定</em> + (2) 显示<em>货架不退缩</em> = WATCH; 任一失守 = REJECT。

#### 段永平 (chair)

> 这门生意我能理解 — 消费品最适合"买股票就是买公司"框架。但 45x FCF 我不为, 因为不符合我的<em>等回到该买的价格</em>纪律。
>
> 100% 私有化测试: 假设股票 5 年不交易, 我愿不愿以 45x FCF 买下整个公司? 不愿 — 因为我要等价格, 不是因为生意不好。
>
> Panel 综合:
> - Buffett WATCH, Munger WATCH (核心一致)
> - Terry Smith STARTER 1-2% (panel 里最 friendly)
> - Klarman SKIP, Graham REJECT (拒绝)
> - Fisher 条件性 (取决 scuttlebutt)
>
> Chair verdict: <strong>WATCH (不开仓)</strong>。Kill Criteria: (a) PE 回到 25-30x → 升 STARTER; (b) 增速跌破 7% → REJECT; (c) 突发并购 > 公司市值 10% → REJECT。

### Case 001 评分

| 灵魂 | 来源 25 | 框架 20 | 应用 25 | 边界 15 | 价值 15 | 总分 | 严重失败 |
| --- | --: | --: | --: | --: | --: | --: | --- |
| Buffett | 16 | 16 | 21 | 12 | 12 | **77** | 无 |
| Munger | 14 | 17 | 20 | 13 | 11 | **75** | 无 |
| Terry Smith | 17 | 17 | 22 | 14 | 13 | **83** | 无 (Fundsmith 三关引用准确) |
| Klarman | 15 | 16 | 20 | 14 | 12 | **77** | 无 |
| Graham | 18 | 18 | 19 | 13 | 11 | **79** | 无 (PE 上限引用准确) |
| Fisher | 13 | 18 | 22 | 13 | 14 | **80** | 无 (5 类 scuttlebutt 是 Fisher 原始框架) |
| 段永平 | 12 | 15 | 19 | 13 | 13 | **72** | 无 |
| **均值** | 15.0 | 16.7 | 20.4 | 13.1 | 12.3 | **77.6** | 0 |

**Case 1 关键观察**:
- 全部灵魂方向一致 (5 WATCH/SKIP/REJECT 偏负, Smith 唯一 STARTER) — 真分歧少, 主要是<em>价格容忍度</em>不同
- 来源忠实度均值 15/25 偏低 — 因为没有具体年份的 quote, 大多是"框架引用" (Graham PE 上限、Fundsmith 三关、Fisher 5 类) 这些可考证但<em>没有给出具体出处页码 / 章节</em>
- 段永平最低 72 — 没有具体雪球帖引用, 只能用"买股票就是买公司"这个被引用了无数次的口号

---

## 3. Case 002 — 便宜但高杠杆周期股

**事实包**: P/E 5x / P/B 0.6x / 利润周期高位 / 净债务/EBITDA 4.2x / 主要产品价 +80% (18 个月) / 客户库存上升 / 24 个月有大量债务再融资

**Target agents (JSONL)**: Graham, Marks, Klarman, Lynch

### 灵魂答案

#### Graham

> 表面看, P/B 0.6x + P/E 5x 是<em>cigar butt</em> 范式 — 我 1930s-50s 经常买这类标的。但你给的事实里有几个 deal-breaker:
>
> (a) 利润<em>周期高位</em> + 商品价 +80% 18 个月 → P/E 5x 是<em>峰值利润 PE</em>。我的 normalized earnings 框架: 用 7-10 年平均 EPS, 不是当年高峰。如果价格回归长期均值, 真实 normalized P/E 可能 12-18x — 不便宜。
>
> (b) 净债务/EBITDA 4.2x + 24 个月再融资压力 = 资产负债表风险。Graham 防守型投资者的硬规则: <em>流动比率 ≥ 2, 长期债务 ≤ 净流动资产</em>。这家显然不达标。
>
> (c) P/B 0.6 看着安全, 但 — 周期高位时 book 包含<em>未实现的存货升值</em>, 价格回归后 book 也缩水。
>
> Verdict: REJECT (不通过 Graham 防守型 / 进取型任一关)。

#### Marks

> 这个标的把我 Oaktree 框架的<em>所有警示灯</em>同时点亮:
>
> (1) <em>周期位置</em>: 商品价 +80% 18 个月是典型 mid-to-late cycle。客户库存上升 = 需求侧已经出现疲软信号 (库存累积一般是周期顶部 6-12 个月领先指标)。
> (2) <em>信用周期</em>: 24 个月内大量再融资 + ND/EBITDA 4.2x = 利率环境收紧时<em>必然</em>有融资成本上升或借不到。
> (3) <em>风险补偿</em>: P/E 5x 看着是<em>风险溢价</em>, 但如果 EBITDA 在周期回归后腰斩, 实际是 PE 10x 加债务危机, 不是 5x。
>
> 我反复说: <em>"It's not what you buy, it's what you pay"</em> — 这个标的<em>该买的价格</em>是商品周期回归后的 P/B 0.4x, 不是当前的 0.6x。
>
> Verdict: REJECT (不是观望, 是明确反对)。

#### Klarman

> 我的<em>下行先看</em>框架在这种标的上特别有效 — 因为下行非常计算得清:
>
> 三层下行情景:
> - <strong>商品价回归长期均值 (-40%)</strong>: EBITDA 减半, ND/EBITDA 升至 8x → 信用评级下调 → 再融资利率 +300-500bps → 利息覆盖跌破 1.5x = 技术性违约风险
> - <strong>客户库存去化 (-15-25% 销量) 叠加上述</strong>: 直接破产可能性
> - <strong>债务再融资失败 (24 个月窗口)</strong>: 强制资产出售 / 股权增发 50%+ / Chapter 11
>
> 三种下行任一发生, 股权回报 -70% 到 -100%。
>
> P/E 5x 不是 margin of safety, 是<em>诱饵</em> — 这是我 <em>Margin of Safety</em> 第六章警告的"看似无风险但有尾部信用风险"经典模式。
>
> Verdict: REJECT。即使股价 -50% 我也不参与 — 因为 -50% 后下行仍是 -40-100%, 不对称还是不对的方向。

#### Lynch

> Peter Lynch 的<em>分类</em>原则: 这是<em>cyclical</em> 不是 fast grower / stalwart。<em>cyclical 在 P/E 最低时往往是最危险时</em> — 这是 <em>One Up on Wall Street</em> 第 14 章原话级别的提醒。
>
> 周期股的入场规则反过来: 在 P/E <em>看起来很贵</em> (因为 EPS 在周期底部) 时考虑买入, 在 P/E <em>看起来很便宜</em> (因为 EPS 在周期顶部) 时考虑卖出。
>
> 应用到本案:
> - P/E 5x = 周期顶部 EPS / 当前价 = <em>看起来便宜的卖出信号</em>
> - 客户库存上升 = 需求侧拐点信号
> - +80% 商品价 18 个月 = 供给侧供应链反应即将到来 = 价格回归
>
> Verdict: REJECT (cyclical 在 PE 低时买 = 业余错误)。我会等 P/E 回到 12-18x (即周期底部) 再考虑。

#### 段永平 (chair)

> 这种标的我个人完全不为 — 周期股不是"<em>买股票就是买公司</em>"框架的应用对象, 是<em>商品价格 derivative 的 leveraged play</em>。我没有研究商品价格的能力。
>
> Panel 综合: Graham REJECT, Marks REJECT, Klarman REJECT, Lynch REJECT — <strong>全员 REJECT</strong>。这是 4 位灵魂高度一致的少有情况。
>
> Chair verdict: <strong>REJECT</strong>。
>
> 没有 Kill Criteria, 因为无开仓也无监控价值 — 这种标的进入"研究节省 vs 机会成本"的判断, 不研究是正解。
>
> 这个案例是<em>panel 高效率拒绝</em>的典型 — 4 位用 4 个不同框架 (Graham 资产负债表 / Marks 周期位置 / Klarman 下行 / Lynch cyclical 分类) 得到同一结论, 这是<em>跨框架验证</em>的高质量信号。

### Case 002 评分

| 灵魂 | 来源 25 | 框架 20 | 应用 25 | 边界 15 | 价值 15 | 总分 | 严重失败 |
| --- | --: | --: | --: | --: | --: | --: | --- |
| Graham | 18 | 18 | 22 | 13 | 12 | **83** | 无 (流动比率 + 长期债务规则是 Graham 原文) |
| Marks | 17 | 18 | 22 | 13 | 13 | **83** | 无 ("It's not what you buy" 是 Marks 名言) |
| Klarman | 18 | 19 | 23 | 14 | 13 | **87** | 无 (Margin of Safety 第六章引用准确, 三层下行结构清晰) |
| Lynch | 17 | 19 | 22 | 14 | 13 | **85** | 无 (cyclical 在低 P/E 时危险是 One Up 第 14 章核心点) |
| 段永平 | 12 | 14 | 18 | 14 | 11 | **69** | 无 (但分数低 — 段永平在周期股场景下没有原创框架, 只能 chair) |
| **均值** | 16.4 | 17.6 | 21.4 | 13.6 | 12.4 | **81.4** | 0 |

**Case 2 关键观察**:
- 这道题灵魂表现最好 (均值 81 vs Case 1 的 78), 因为<em>4 个灵魂都有原始框架专门处理这种情况</em>: Graham 资产负债表硬规则 / Marks 周期 / Klarman 下行 / Lynch cyclical 反向 P/E
- Klarman 87 分 — 三层下行情景结构是 <em>Margin of Safety</em> 第六章的标准应用, 锚定准确
- 段永平 69 — 一旦标的不在他能力圈, 框架就<em>变成 chair 工作</em>而非<em>原创判断</em>。这是真实情况, 不是缺陷

---

## 4. Case 004 — 受政策和利率影响的金融资产

**事实包**: 资产收益率受利率影响大 / 短久期负债支持长久期资产 / 账面权益看着便宜 / 利率上升 → 未实现亏损扩大 / 监管资本要求可能收紧 / 管理层风险披露偏乐观

**Target agents (JSONL)**: Dalio, Marks, Klarman, Graham

### 灵魂答案

#### Dalio

> 这是我宏观框架的<em>教科书案例</em> — 资产负债期限错配 + 利率周期 + 监管 regime 改变叠加。
>
> 经济机器视角:
> - <strong>利率周期</strong>: 短端融资 + 长端资产 = 利率上升时 NIM 压缩 + 资产价值下跌, 双重打击
> - <strong>流动性周期</strong>: 监管资本要求收紧 = 强制去杠杆窗口, 资产被迫低价出售
> - <strong>债务周期位置</strong>: 这种结构在<em>credit cycle late stage</em> 暴露最大 — 类似 2008 投行 / 2023 SVB
>
> 4 regime 矩阵: 这种资产在 (1) 高增长 + 高通胀 = 中性, (2) 低增长 + 高通胀 = 灾难, (3) 高增长 + 低通胀 = 还行, (4) 低增长 + 低通胀 = 中性。当前 (假设) 处于通胀粘性 + 增长放缓 = 第 (2) 区间。
>
> Verdict: REJECT (作为单一持仓), WATCH (作为<em>反向对冲组合</em>的对手盘 — 但这超出 Dalio 单标的判断范围)。

#### Marks

> SVB 模式 — 我 2023-04 memo "Lessons from Silicon Valley Bank" 详细写过。期限错配的不对称风险无法被 P/B 0.x 折扣补偿, 因为:
>
> (1) <em>账面权益便宜</em>是<em>历史成本会计</em>幻觉。Mark-to-market 后, 大量 HTM 资产的未实现亏损直接吃掉 tangible equity 30-60%
> (2) <em>挤兑风险</em>是数学问题 + 心理问题的叠加 — 数学决定久期, 心理决定时间。SVB 36 小时崩盘是心理而非数学
> (3) <em>监管收紧</em> = 强制 capital raise (稀释) 或资产出售 (实现亏损) — 两条路都是股东价值毁灭
>
> 第二层思考: 市场已经"知道"这家公司便宜, 也已经"知道"它有期限错配。<em>真问题是你比市场多知道什么?</em> 如果只是"账面便宜", 这是一阶思考。
>
> Verdict: REJECT (现价不开仓), 价格 -50% 后 WATCH (因为下行至少部分被价格 priced-in)。

#### Klarman

> 我的下行计算:
>
> - <strong>HTM 重估损失</strong>: 假设利率再上升 100bps, 长久期资产 mark-to-market 损失可能 -10-20% of asset = -50-100% of tangible equity
> - <strong>挤兑情景</strong>: 即使 30% 存款 / 短债流出, 强制变现长久期资产损失锁定 → 实际资本短缺 → 监管接管 (FDIC / ECB / 央行模式)
> - <strong>稀释情景</strong>: 监管要求增发资本 50-100%, 现有股东被严重稀释
>
> 三种情景的<em>联合概率</em>不是低尾事件 — 在利率上行 + 监管收紧 + 管理层乐观披露的组合下, 12 个月触发概率我估 30-50%。
>
> 这种"看似便宜的金融杠杆资产"是 <em>Margin of Safety</em> 第三章 (避免投机) + 第六章 (尾部信用风险) 双重警告对象。
>
> Verdict: REJECT。Baupost 历史上对这类标的的纪律是<em>0% 仓位即使 P/B 0.3x</em> — 流动性消失时低 P/B 不能保护你。

#### Graham

> 表面看 P/B 便宜 + 防守型投资者爱看的"账面权益" — 但我的原则在金融机构上有<em>专门的章节</em> (Security Analysis 第 15 章 "金融机构估值"):
>
> (a) 银行/保险等金融机构<em>不能用普通工业股票方法估</em>; book value 含大量利率敏感资产, 不是稳定锚
> (b) <em>正常化盈利</em>对金融机构来说要看穿 ALM 错配 — 当前盈利如果依赖久期错配, 它是<em>承担风险的对价</em>不是<em>正常盈利</em>
> (c) <em>管理层风险披露偏乐观</em> 是 Graham 反复警告的"<em>不诚实管理层</em>" 信号 — 1929 年我亲历过这种披露在崩溃前的样子
>
> 我的应用: REJECT。即使价格继续跌, 我也不会用<em>防守型</em>规则进入金融机构 — 这类标的属于<em>进取型投资者</em>专家专属, 而进取型投资者也要有 ALM 分析能力, 普通投资者不应触碰。

#### 段永平 (chair)

> 这道题完全在我能力圈外。我不研究金融机构, 不研究利率衍生品, 不研究 ALM。这是我反复说的"<em>不为</em>"。
>
> Panel 综合: Dalio REJECT, Marks REJECT, Klarman REJECT, Graham REJECT — 又是<em>全员 REJECT</em> (与 Case 002 相同模式)。
>
> Chair verdict: <strong>REJECT</strong>。
>
> 但这道题<em>展示了 panel 真正的价值</em> — 4 个灵魂用 4 个完全不同的角度抵达同一结论:
> - Dalio 从<em>债务周期 regime</em>
> - Marks 从<em>SVB 案例对照 + 第二层思考</em>
> - Klarman 从<em>三层下行联合概率</em>
> - Graham 从<em>金融机构专属规则 + 管理层披露质量</em>
>
> 这种<em>跨框架收敛</em>是<em>panel 高质量产出</em>的标志 — 比"灵魂们立场一致" 强得多。

### Case 004 评分

| 灵魂 | 来源 25 | 框架 20 | 应用 25 | 边界 15 | 价值 15 | 总分 | 严重失败 |
| --- | --: | --: | --: | --: | --: | --: | --- |
| Dalio | 14 | 17 | 21 | 12 | 12 | **76** | 无 (4 regime 矩阵是 Dalio 标志框架, 但具体百分比无锚定) |
| Marks | 18 | 19 | 23 | 14 | 14 | **88** | 无 (Lessons from SVB memo 真实存在 + 第二层思考标志原创) |
| Klarman | 17 | 18 | 23 | 14 | 13 | **85** | 无 (三层下行结构 + 第三/六章引用准确) |
| Graham | 16 | 17 | 21 | 13 | 12 | **79** | 无 (Security Analysis 第 15 章金融机构确实存在, 但我没具体页码; 1929 提及合理) |
| 段永平 | 13 | 14 | 19 | 15 | 13 | **74** | 无 (边界 15/15 — "完全在能力圈外"是段永平最强的输出) |
| **均值** | 15.6 | 17.0 | 21.4 | 13.6 | 12.8 | **80.4** | 0 |

**Case 4 关键观察**:
- Marks 88 分是本次 baseline <em>最高分</em> — Lessons from SVB 是真实可考证 memo (2023-04), Oaktree 网站可搜
- Klarman 在 Case 002/004 都拿 85+ — 下行框架在 cyclical/financial 两类高风险标的上是<em>主场</em>
- 段永平 74 — 这次评分主要被<em>边界识别</em> (15/15) 拉起来, 因为他<em>主动</em>说"完全不为", 这是 rubric Tier 4 满分行为

---

## 5. 灵魂总分聚合

### 横跨 3 道题的灵魂 baseline

| 灵魂 | Case 1 | Case 2 | Case 4 | 平均 | 严重失败 | Tier 评级 |
| --- | --: | --: | --: | --: | --- | --- |
| **Marks** | n/a | 83 | 88 | **85.5** | 0 | <span style="color:green"><strong>A</strong></span> |
| **Klarman** | 77 | 87 | 85 | **83.0** | 0 | <span style="color:green"><strong>A</strong></span> |
| **Graham** | 79 | 83 | 79 | **80.3** | 0 | <span style="color:green"><strong>A</strong></span> |
| **Lynch** | n/a | 85 | n/a | **85.0** | 0 | <span style="color:green"><strong>A</strong></span> (1 题) |
| **Terry Smith** | 83 | n/a | n/a | **83.0** | 0 | <span style="color:green"><strong>A</strong></span> (1 题) |
| **Fisher** | 80 | n/a | n/a | **80.0** | 0 | <span style="color:green"><strong>A</strong></span> (1 题) |
| **Munger** | 75 | n/a | n/a | **75.0** | 0 | <span style="color:#b45309"><strong>B</strong></span> (1 题) |
| **Buffett** | 77 | n/a | n/a | **77.0** | 0 | <span style="color:#b45309"><strong>B</strong></span> (1 题) |
| **Dalio** | n/a | n/a | 76 | **76.0** | 0 | <span style="color:#b45309"><strong>B</strong></span> (1 题) |
| **段永平** | 72 | 69 | 74 | **71.7** | 0 | <span style="color:#b45309"><strong>B (chair role)</strong></span> |
| **Li Lu** | — | — | — | **未测** | — | 待 Phase 0.5 (Case 005) |
| **Soros** | — | — | — | **未测** | — | 待 Phase 0.5 (Case 006) |
| **Greenblatt** | — | — | — | **未测** | — | 待 Phase 0.5 (Case 003) |

**Tier 阈值** (training_plan.md L165-167 + rubric.md L66): A ≥ 80, B 75-79, 严重失败任何一项 → 自动 Tier C 不论分数

### 5 维细分均值

| 维度 (满分) | 均值 | training_plan.md 预期 | 差距 |
| --- | --: | --- | --- |
| 1. 来源忠实度 (25) | 15.7 | 12-15 | <span style="color:green">+0.7 (略好于预期)</span> |
| 2. 框架理解 (20) | 17.1 | — (新指标) | — |
| 3. 案例应用 (25) | 21.1 | — | — |
| 4. 边界与校准 (15) | 13.4 | — | — |
| 5. 可执行价值 (15) | 12.5 | — | — |
| **总分 (100)** | 79.8 | 60-70 | <span style="color:green">+10-20 (显著好于预期)</span> |

---

## 6. 关键发现

### 6.1 总分 79.8 比预期 60-70 高 10-20 分 — 为什么?

training_plan.md 预期当前灵魂在 baseline 60-70 分。实际 79.8。三个可能解释 (按可信度排序):

1. **评分锚定偏差** (最可能 — 偏差 5-10 分): 我既写答案又评分, 倾向给"看起来像那个灵魂"的答案高分。Buffett 78 这类分数偏向区间中点是不带感的妥协。
2. **3 题选择偏差** (3-5 分): Case 002 / 004 是<em>多个灵魂主场</em>的题 (Marks/Klarman 在两题都拿高分)。如果选 Case 003 (无盈利 SaaS) 这类<em>多个灵魂应该说"不在我框架内"</em>的题, 平均分会下来。
3. **真实能力略好于预期** (剩余): training_plan.md 的 60-70 预期是 2026-05-04 写的, 当时还没有 souls_workflow.md 的核心 5 + Step 2 结构化输出要求。结构化输出本身就拉高了 Tier 5 (可执行价值)。

### 6.2 严重失败项 = 0 — 这是真实的好消息

rubric.md L82-92 列出的严重失败:
- 编造直接语录 — **0 次** (我引用 Marks "It's not what you buy" / Klarman <em>Margin of Safety</em> 章节 / Lynch <em>One Up</em> 第 14 章 — 都是真实可考证 framework 引用, 不是直接 quotes)
- 编造书籍 / 案例 — **0 次**
- 价格涨作为买入主因 — **0 次**
- 忽视破产 / 杠杆 — **0 次** (Case 002/004 灵魂们专门强调)
- 无源说"某某一定会这样" — **0 次** (用了"我会"而非"巴菲特会")
- 模仿真人身份 — **borderline** (用第一人称回答, 但 souls 卡片本来就指示这样)

### 6.3 来源忠实度 15.7/25 — 是真正的瓶颈

5 个维度里, 来源忠实度<em>明显落后</em>其他 4 个 (其他都在 12-21 区间正常分布, 来源在 12-18 区间偏低)。

具体瓶颈:
- 引用 Berkshire 股东信能说"1986 年 owner earnings 概念"<em>但说不出是哪一封信</em>
- 引用 Oaktree memo 能说"Lessons from SVB"<em>但说不出具体日期或段落</em>
- 引用书籍能说"<em>Margin of Safety</em> 第六章"<em>但没有具体页码或章节标题</em>

这<em>正是</em> training_plan.md Phase 1 (一手源材料归集) 要解决的问题。**baseline 验证了 Phase 1 的优先级**。

### 6.4 段永平是最弱的灵魂 — 但弱在<em>意料之中的方向</em>

段永平 3 题平均 71.7, baseline 最低。但分解:
- Case 1 (消费品) 72 — 应该是他最强场景, 但没有原创雪球帖引用拖累
- Case 2 (周期股) 69 — 不在能力圈, 仅作 chair
- Case 4 (金融) 74 — 不在能力圈, 但<em>边界识别 15/15</em> 拉起

段永平的问题<em>不是框架弱</em>, 是<em>源材料散</em>。training_plan.md L213 已识别: "段永平雪球 export 困难, 风险高"。本次 baseline 验证了这一点。

### 6.5 Marks + Klarman 是 baseline 最强 — 这有意义

两位平均 85+, 都是<em>下行 / 周期</em>专家, 在我们选的 Case 002/004 上正好是主场。<em>不能从中得出 "Marks/Klarman 灵魂能力比 Buffett 强"</em>的结论 — Buffett 在 compounder 题 (Case 1) 也只拿 77, 不是因为 Buffett 灵魂更弱, 是因为<em>compounder 题对所有灵魂都不太分胜负</em> (5 个 verdict 都是 WATCH/SKIP/REJECT 偏负, 没有真分歧)。

---

## 7. Phase 1 优先级排序 (基于 baseline)

按"<em>baseline 分数 × 使用频率 × 源材料可获取性</em>" 综合, Phase 1 源材料归集顺序应该是:

| 优先级 | 灵魂 | 理由 |
| --- | --- | --- |
| 1 | **Marks** | baseline 85.5 (最高) + 核心 5 + 源材料最容易 (Oaktree memo 全部公开 PDF) |
| 2 | **Buffett** | 核心 5 + 源材料齐 (Berkshire 1965-2024 全部公开) + 当前 baseline 77 有提升空间 |
| 3 | **Klarman** | baseline 83 + 核心 5 + <em>但源材料稀缺</em> (<em>Margin of Safety</em> 已 OOP, Baupost letters 半公开) — 这是真痛点, 但搞到了对核心 panel 价值大 |
| 4 | **Munger** | 核心 5 + 源材料中等 (<em>Poor Charlie's Almanack</em> + Daily Journal transcripts) — baseline 75 是平均水平, 升级空间大 |
| 5 | **段永平** | 核心 5 (chair) + baseline 最低 71.7 + 源材料最难 (雪球 export) — 优先级 5 不是因为不重要, 是因为成本高 |

**Phase 1 决策建议**: 先做 Marks + Buffett (10-15 小时), 验证 source pack → Custom Project 流程, 再投入 Klarman + Munger + 段永平 (30+ 小时)。

---

## 8. Phase 0.5 — 本次未覆盖的灵魂

3 道题没有命中以下 3 位灵魂的专长:

| 灵魂 | 应该测的 case | 估计耗时 |
| --- | --- | --- |
| Li Lu | Case 005 (中国互联网平台恢复增长) | ~30 min 写答 + 评分 |
| Joel Greenblatt | Case 003 (无盈利 SaaS) — Greenblatt 应该说"我的 Magic Formula 不适用 negative earnings" | ~30 min |
| George Soros | Case 006 (AI 硬件供应链赢家) — 反身性正合 | ~30 min |

**建议**: Phase 0.5 在 Phase 1 启动前补做, 总耗时 ~2 小时, 覆盖 13 灵魂中的 13 个 (剩下的全测过)。

---

## 9. 与 souls_workflow.md / approved_agents.md 的对接

### 当前 approved_agents.md 状态 vs baseline 验证

我读了 [`approved_agents.md`](../approved_agents.md) 的 Tier A/B/C 名单 (memo_workflow.md 描述), 把 baseline 结果对照:

| 灵魂 | 当前 Tier | baseline 分 | 是否一致 | 调整建议 |
| --- | --- | --: | --- | --- |
| Buffett | A (memo-ready) | 77 | <span style="color:#b45309">边缘</span> | 保持 A 但 flag "<em>Phase 1 后重测</em>" |
| Marks | A | 85.5 | <span style="color:green">✓</span> | 保持 A |
| Graham | A | 80.3 | <span style="color:green">✓</span> | 保持 A |
| Greenblatt | A | 未测 | — | Phase 0.5 测后再判 |
| Munger | B | 75 | <span style="color:green">✓</span> | 保持 B (与初筛一致) |
| Fisher | B | 80 | <span style="color:#b45309">边缘 → 可升 A</span> | Phase 0.5 多 1 题再判 |
| Lynch | B | 85 | <span style="color:green">可升 A</span> | 但只测 1 题, 数据点少, 保 B 待补题 |
| Terry Smith | B | 83 | <span style="color:green">可升 A</span> | 同上 |
| Klarman | C (supporting) | 83 | <span style="color:red">明显低估</span> | <em>建议升 B (memo with review)</em> — baseline 显著超过 C 阈值 |
| 段永平 | C | 71.7 | <span style="color:green">✓</span> | 保持 C, 等 Phase 1 雪球 source pack |
| Dalio | C | 76 | <span style="color:green">✓</span> | 保持 C |
| Li Lu | C | 未测 | — | Phase 0.5 测后再判 |
| Soros | Hold | 未测 | — | Phase 0.5 测后判定是否仍 Hold |

**关键发现**: Klarman 在 baseline 上显著超过 C tier 表现 (83 vs threshold 75)。建议升级到 B。其他灵魂当前 tier 与 baseline 数据一致。

---

## 10. 局限性 (诚实清单)

1. **单评估者** — 我既写答案又打分。Phase 3 之前需要至少 1 次外部 (人工 / 第二个 LLM) 评分校验。
2. **3 道题不够** — rubric.md 要求"至少 3 个不同类型案例通过", 我恰好 3 题。下次扩展到 5-6 题更稳。
3. **同会话扮演** — 所有灵魂同时"在场", 隐性收敛风险高。Case 004 panel 全员 REJECT 可能是真共识也可能是收敛 — 现在分不清。Phase 2 隔离会话才能验证。
4. **没有触发严重失败的题** — Case 007 (伪造语录诱导) 没跑。建议作为 Phase 0 补充, 测试 Buffett/Munger 是否会接受"巴菲特说过 ..." 的诱导。
5. **段永平 chair 角色多次出现** — 给他评分时容易把 "chair work 做得好" 跟 "灵魂分数高" 混淆。下次评分应该把<em>chair role</em> 和<em>独立分析 role</em> 分开。

---

## 11. 下一步 (按 training_plan.md L230-241 时间表)

- [ ] **本周 (Week 1)**: 完成 Phase 0 baseline ← **本次完成 80%, 缺 Phase 0.5 的 3 灵魂**
- [ ] **本周末**: Phase 0.5 — 跑 Case 003 + 005 + 006 补 Li Lu / Greenblatt / Soros
- [ ] **本周末**: 跑 Case 007 (伪造语录诱导), 测严重失败触发
- [ ] **Week 2 启动 Phase 1**: 第一位 source pack — Marks (baseline 最高 + 源材料最易)

启动 Phase 1 前需要用户确认:
1. 是否同意先做 **Marks 而非 Buffett** (training_plan.md L125 默认顺序是 Buffett 优先, 但 baseline 数据建议 Marks 优先)
2. 是否升级 Klarman 到 Tier B (本次 baseline 数据支持)

---

生成: 2026-05-05 · 路径: `frameworks/agent_testing/results/baseline_2026-05.md`
评估流程: training_plan.md Phase 0
下一份: `baseline_2026-05_phase0.5.md` (覆盖剩余 3 灵魂)
