# Professional Research Pipeline

创建: 2026-06-15

目标: 把投资研究变成一个**可暂停、可恢复、可审计、可复盘**的流程。AI 不负责“一口气想明白一切”；AI 负责按规矩推进一个个 research block，把证据、推断、情绪和未知分开。

---

## 1. 本地已有资产

本仓库已经有很好的骨架:

- `frameworks/info_collection_pipeline.md`: 公司研究 Step 0，已经定义 L1/L2/L3、Fact/Signal/Sentiment、plan-first、raw/facts/memory。
- `companies/_step0_plan_template.md`、`_raw_block_template.md`、`_facts_template.md`: 公司研究的可恢复执行模板。
- `sectors/china-healthcare/research-notes/L3/_research-protocol.md`: 行业深调的 4 phase 模式，核心是 collect 不综合、extract 入库、analyze 派生、synthesize 带 source id。
- `frameworks/souls_workflow.md`: 投资人视角 panel，适合放在 facts 完成之后，不适合替代事实收集。
- `frameworks/agent_testing/rubric.md`、`source_grounding_matrix.md`: agent/skill 采纳标准，强调来源忠实度和边界校准。
- `frameworks/duan-yongping/README.md`: 段永平框架目录已开，但一手来源、原则、checklist 还没有补齐。

缺口不是没有流程，而是缺少一层统一的 Research OS: 所有公司、行业、主题、投资人方法，都必须走同一套来源账本、批次预算、质量门和记忆机制。

---

## 2. 外部扫描结论

### GitHub / Agent 工程

- [FinRobot](https://github.com/ai4finance-foundation/finrobot) 强调自动生成 equity research、财务分析、估值、风险评估，说明“角色化金融 agent”已经常见，但不能替代我们自己的 source ledger。
- [FinGPT](https://github.com/ai4finance-foundation/fingpt) 是金融 LLM 基座项目，README 明确提示不是投资建议；适合作为工具/模型参考，不作为事实源。
- [TradingAgents](https://github.com/tauricresearch/tradingagents) 的多角色结构可借鉴，但它偏 trading decision，我们这里要先做 investment memo 和证据审计。
- [deep-research-machine](https://github.com/druce/deep-research-machine) 最值得借鉴的是 DAG: 先 gather/index/research/write/assemble，并让流程可配置、可恢复，而不是一条 prompt 跑到底。

### Serenity / “白毛股神” / Chokepoint

公开资料里，“bottlenect”大概率对应的是 **bottleneck / chokepoint / 瓶颈点投资法**。可吸收的方法，不是跟单:

- [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) 把流程写成 `market story -> system change -> required parts -> supply-chain layers -> scarce constraints -> public companies -> evidence -> what could prove the idea wrong`，这条链条值得纳入。
- 该 skill 要求先排产业链层级再排公司，深度主题扫描尽量覆盖 20 个候选和 25 个来源，并明确社交媒体只作线索。
- [lanfuli/aleabito-serenity-skills](https://github.com/lanfuli/aleabito-serenity-skills) 把 Serenity 的公开 X 历史做成 data/method/radar 三层，但它自己也提示 candidate generator，不是 oracle，有幸存者偏差和单账号脆弱性。
- [SevenBlues/serenity-chokepoint](https://github.com/SevenBlues/serenity-chokepoint) 强调可审计复现、red-team 和样本外回测，这是更健康的方向；不过仓库也提示自带数据是示例估计，不能直接信。

结论: Serenity 只能作为“产业链稀缺层模块”，不能作为投资裁判。所有白毛股神战绩、身份、收益率自述，按 D1/C2 处理。

### 小红书 / RED Skill

- 2026-06-08 起，小红书 RED Skill 开始把 skill 挂到内容下方，定位更像 skill 发现与传播入口，而不是严肃研究来源。
- [小红书搜索总结 skill](https://github.com/piekill/xiaohongshu-summarizer-skill) 可用于抓取图文、评论和情绪，但小红书内容必须进入 D1/SENTIMENT 或 OPEN QUESTIONS。
- 第三方 skill registry 对小红书工具有安全风险提示；任何自动登录、抓取、发布工具都必须先做安全审计，不进入默认 pipeline。

---

## 3. 总原则

1. **先本地，后联网**: 先 `rg` 本仓库，找已有事实、旧结论、视频/播客 notes，再决定外部搜索。
2. **先计划，后执行**: 每次研究先写 plan，拆 block，估预算，再收集。
3. **先收集，不综合**: raw 阶段只保存结果和摘录，不写观点。
4. **先证据，后灵魂**: Buffett/Munger/Duan/Serenity panel 只能读 facts 和 claim ledger，不能凭空补资料。
5. **先产业链层级，后公司排名**: 主题研究必须先找到 scarce layer，再讨论 ticker。
6. **每条 claim 可追溯**: 没有 source_id 的事实不能进入 memo。
7. **社媒只作线索**: X/小红书/雪球/Reddit 只能触发调查，不直接证明 thesis。
8. **AI 输出不是来源**: AI 可以提取、对比、建模、批判，但不能成为 source。
9. **低完整度限制 verdict**: source completeness < 40% 必须 `INFO-GAP`；40%-60% 最高 `WATCH`；60%-80% 最高 `STARTER`；80%+ 才允许讨论 `CORE`。
10. **每个 thesis 要能被杀死**: memo 必须写 kill criteria、监控源、触发阈值。

---

## 4. 目录标准

### 公司研究

```text
companies/<ticker>/
  step0_plan.md
  raw/
    block01_identity.md
    block02_filings.md
    ...
  facts.md
  claim_ledger.csv
  bottleneck_map.md
  model/
    revenue_bridge.csv
    scenario_model.csv
  memo-v1.md
  memory.md
```

### 行业/主题研究

```text
sectors/<sector>/<project>/
  plan.md
  raw-searches/
  data/
    sources.csv
    analysis/
  value_chain_map.md
  bottleneck_map.md
  synthesis-v1.md
  memory.md
```

### 投资人/方法框架

```text
frameworks/<method-or-investor>/
  source_inventory.md
  principles.md
  checklist.md
  quotes_and_sources.md
  eval_cases.md
```

---

## 5. Request Router

| 用户需求 | 默认路径 | 输出 |
|---|---|---|
| 单家公司深度分析 | Company pipeline | facts + memo + memory |
| 一个行业/主题机会 | Sector/theme pipeline | value chain + bottleneck map + candidate priority |
| “现在最值得看什么” | Theme scan，不直接给买卖 | scarce layers + research queue |
| 验证一个传闻/说法 | Verification pipeline | claim-by-claim truth table |
| 学某个投资人/skill | Method build pipeline | source inventory + checklist + eval |
| 更新旧标的 | Delta update | changed facts + revised thesis |

---

## 6. Pipeline Stages

### Stage 0: Intake

输出 `plan.md` 顶部:

- decision question: 这次到底要回答什么
- object: company / sector / theme / method / rumor
- geography: US / A-share / HK / global
- time horizon: 3-12m、3-5y、10y
- output type: memo / watchlist / model / verification table
- hard constraints: 时间预算、是否允许社媒、是否需要一手文件

### Stage 1: Local Inventory

先搜本仓库:

```powershell
rg -n "<ticker|company|theme|keyword>" .
```

输出:

- 已有文件路径
- 已有结论
- 已有 source_id
- 与当前问题冲突或过期的地方

### Stage 2: Plan And Budget

每次只推进一个 batch。默认预算:

| 类型 | 搜索/来源预算 | 适用场景 |
|---|---:|---|
| Quick triage | 5-8 sources | 判断是否值得开题 |
| Standard company | L1 + L2, 15-25 sources | 出单家公司 memo |
| Deep company | 30-60 sources | 重大仓位/高争议标的 |
| Sector/theme | 30-80 sources, 分 4-8 批 | 行业地图/候选池 |
| Method build | 20+ primary/near-primary sources + 3 eval cases | 投资人/skill 采纳 |

Plan 必须列:

- batch 名称
- query/source list
- expected artifact
- stop condition
- acceptable gap

### Stage 3: Collect Raw

只做三件事:

- 保存 URL/path、搜索词、抓取日期。
- 保存短摘录或 close paraphrase。
- 标注 source tier。

禁止:

- 在 raw 阶段写“所以可以买/不能买”。
- 把二手文章里的数字直接当事实。
- 因为某个 KOL 说了就跳到结论。

### Stage 4: Extract Claim Ledger

把 raw 变成结构化 claim:

```text
source_id, claim, value, unit, as_of, retrieved_at, source_type,
source_url_or_path, original_excerpt, reliability_note, destination
```

destination 只能是:

- EVIDENCE
- INTERPRETATION
- SENTIMENT
- OPEN_QUESTION

### Stage 5: Derived Analysis

只在 claim ledger 之后做派生:

- revenue bridge
- margin bridge
- unit economics
- moat technical analysis
- founder/operator underwriting
- inversion failure map
- capex/capacity reconciliation
- customer/supplier concentration
- TAM sanity check
- scenario model
- valuation range

规则:

- 派生表必须引用 source_id。
- estimate 必须单独标，不能伪装成事实。
- 冲突口径要并列，不提前抹平。

### Stage 6: Bottleneck / Chokepoint Module

用于 AI 基建、半导体、机器人、电力、医疗制造、供应链重的行业。它是一个模块，不是完整 pipeline。

固定链条:

```text
market story
-> system change
-> required parts
-> value-chain layers
-> scarce constraints
-> public/private companies
-> evidence grade
-> repricing path
-> what could prove it wrong
```

评分维度:

| 维度 | 问题 |
|---|---|
| Demand pressure | 下游需求是否真实增长，还是只有叙事 |
| Criticality | 这个环节失败会不会卡住整个系统 |
| Supplier concentration | 是否少数供应商控制 |
| Qualification gate | 客户认证/导入周期是否长 |
| Expansion difficulty | 扩产是否受设备、材料、工艺、人才、监管限制 |
| Substitution risk | 替代技术/替代供应商是否快 |
| Evidence quality | 是 A/B 证据，还是 D1 社媒线索 |
| Valuation/crowding | 市场是否已经充分定价 |

输出 `bottleneck_map.md`:

```markdown
## Scarce Layers
| rank | layer | why scarce | evidence | main failure mode |

## Candidate Universe
| company | market | chain position | constrains what | evidence grade | next check |

## Not Yet Investable
| company/layer | why it is only a lead |
```

### Stage 7: Audit

进入 memo/panel 前必须过 audit:

- source coverage: L1/L2 是否够
- contradiction table: 关键冲突数字和观点
- missing proof: 哪些判断还没有强证据
- social contamination: 是否把 D1 当成 A/B
- freshness: 当前事实是否过期
- operator evidence: 创始人/CEO/董事会/激励是否有足够证据支持判断
- inversion map: 是否明确写出“如果我要让它失败，会攻击哪里”
- verdict ceiling: 根据信息完整度设置结论上限

### Stage 8: Lens / Panel

只在 facts + audit 后运行。

默认 panel:

- Buffett: ten-year ownership test / business quality / owner earnings / price vs value / margin of safety / technology disruption / capital allocation
- Marks: cycle / consensus / asymmetry
- Munger: inversion / incentives / failure modes / psychology and organization traps
- Klarman: downside / margin of safety
- Duan Yongping: 懂生意、用户价值、企业文化、不为清单、100% 私有化测试

按需扩展:

- Fisher/Li Lu: 信息完整性和 scuttlebutt
- Serenity: 供应链瓶颈层，不评价最终买卖
- Dalio/Soros: 宏观 regime / reflexivity
- Graham/Greenblatt: 量化或资产保护起点

### Stage 9: Decision Memo

标准结论不是 buy/sell，而是:

- `REJECT`: 逻辑或证据不成立
- `INFO-GAP`: 信息缺口太大
- `WATCH`: 值得跟踪但不够强
- `STARTER`: 可以讨论小仓位研究仓
- `CORE`: 只有高完整度、高理解度、高赔率才允许

Memo 必须包含:

- one-line verdict
- what has to be true
- evidence supporting it
- evidence against it
- ten-year ownership test
- moat mechanism and attack surface
- founder/operator underwriting
- inversion: how would this fail if attacked intelligently?
- owner earnings bridge
- price vs intrinsic value
- margin of safety
- technology disruption check
- valuation/scenario discipline
- kill criteria
- next checks
- monitor list

### Stage 10: Memory / Monitor

每次研究结束更新 `memory.md`:

- 长期不变: business model, culture, moat, value-chain position
- 中期更新: quarterly numbers, capex, orders, customer evidence
- 短期监控: news, price dislocation, sentiment, regulatory dates
- changed-mind log: 哪条新证据改变了旧判断

---

## 7. External Skill Adoption Gate

任何 GitHub/小红书/社媒 skill 先进入候选池，不能直接安装/采用。

采纳步骤:

1. 记录 repo URL、作者、license、commit/date、star/fork 只是参考。
2. 阅读 `SKILL.md` / README / scripts 权限。
3. 标注它使用的数据源和外部 API。
4. 跑 3 个 eval case: 一个成功案例、一个反例、一个信息不足案例。
5. 按 `frameworks/agent_testing/rubric.md` 打分，>=75 才能试用。
6. 安全审计: 不自动登录券商、不自动交易、不上传私密文件、不运行未审查脚本。
7. 只作为模块接入，不覆盖本 pipeline 的 source policy。

当前建议状态:

| 外部项目 | 状态 | 用法 |
|---|---|---|
| muxuuu/serenity-skill | Adapt | 借鉴 bottleneck module 和 evidence ladder |
| lanfuli/aleabito-serenity-skills | Watch | 可作为 Serenity 账号跟踪工具，不作投资判断 |
| SevenBlues/serenity-chokepoint | Watch/Study | 借鉴 red-team 和 out-of-sample 精神 |
| deep-research-machine | Adapt | 借鉴 DAG、resume、critic loop |
| FinRobot / FinGPT | Study | 借鉴金融 agent 形态，不直接信输出 |
| Xiaohongshu summarizer tools | Restricted | 只做 D1 情绪/线索，先安全审计 |

---

## 8. Google 下一步应用

已开目录: `companies/googl/`

建议下一批按这个顺序做:

1. `facts.md`: 把 FY2025 + Q1 2026 revenue bridge、Cloud margin、capex/cash flow、buyback 归一。
2. `claim_ledger.csv`: 把 Alphabet SEC、Berkshire 13F、H&H 13F、新闻解释拆成 A/B/C/D。
3. `bottleneck_map.md`: 不是只看搜索广告，要看 AI 搜索、TPU/数据中心、电力、Cloud GPU/TPU capacity、YouTube、监管。
4. `holder_trace.md`: Berkshire 买入、Alphabet 对 Berkshire 私募、H&H/Duan 13F 的时间线和证据边界。
5. `memo-v1.md`: 再让 Buffett/Duan/Marks/Munger/Klarman panel 发言。

关键问题:

- Google 的收入质量是否仍由 Search 广告保护，还是 AI search 改变了用户入口和广告 load？
- Cloud 的增长和利润率改善是否足以解释 capex 激增？
- TPU/数据中心/电力是否成为 Alphabet 自身的瓶颈，还是反而是护城河？
- Berkshire 买 Google 是现金替代、AI 基建下注、广告垄断补票，还是交易结构驱动？
- H&H/Duan 的 13F 只能说明管理人披露持仓变化，不能直接等同于段永平个人全部仓位。
