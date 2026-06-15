# Buy-Side Research Department

创建: 2026-06-15

目标: 把这个仓库当成一个小型买方投资部运行。我们不是卖研究报告，而是形成可下注、可否决、可复盘的判断。

---

## 1. Operating Philosophy

研究部的工作不是“找到好故事”，而是回答:

```text
这是不是一门十年后还存在的好生意？
我们是否真正理解？
当前价格是否给足安全边际？
如果错，会怎么错？
什么证据会让我们改变想法？
```

默认结论不是买入，而是 `INFO-GAP`。只有证据、估值、安全边际、风险和人都过关，才升级。

---

## 2. Roles

一个人也可以扮演多个角色，但每次输出要分角色。

| Role | 职责 | 主要产物 |
|---|---|---|
| Research Lead | 定义问题、拆 block、维护 research queue | `research_queue.md`, `research_status.md` |
| Primary Analyst | 收集一手资料、建 facts 和 model | `facts.md`, `claim_ledger.csv`, `model/*.csv` |
| Industry Analyst | 价值链、竞争格局、瓶颈层 | `value_chain_map.md`, `bottleneck_map.md` |
| Moat Analyst | 护城河机制、攻击面、可持续性 | `moat_map.md` |
| Operator Analyst | 创始人、CEO、董事会、文化、激励 | `operator_underwriting.md` |
| Devil's Advocate | 反向思考、失败路径、kill criteria | `inversion_map.md` |
| Valuation Analyst | owner earnings、情景估值、安全边际 | `valuation.md`, `scenario_model.csv` |
| PM / IC Chair | 最终判断、仓位级别、监控计划 | `memo-vN.md`, `memory.md` |

---

## 3. Research Stages

| Stage | 名称 | 进入条件 | 退出产物 | 升级门槛 |
|---|---|---|---|---|
| 0 | Idea Intake | 一个 ticker/theme/传闻 | queue item | 问题足够明确 |
| 1 | Triage | 5-8 个高质量来源 | triage note | 不是明显烂生意/明显太贵/明显无证据 |
| 2 | Full Research Plan | scope 已明确 | `research_status.md` + block plan | 用户确认或研究价值足够 |
| 3 | Evidence Build | 按 block 收集 | `raw/`, `facts.md`, `claim_ledger.csv` | source completeness >= 60% |
| 4 | Analysis Modules | facts 完成 | moat/operator/inversion/valuation | 每个模块有证据和 open questions |
| 5 | IC Memo | 模块完成 | `memo-v1.md` | thesis 有可证伪条件 |
| 6 | Decision | IC review | verdict + monitor | REJECT/WATCH/STARTER/CORE |
| 7 | Monitor | 已有 memo | `memory.md` 更新 | 新证据触发 revision |

---

## 4. Verdict System

| Verdict | 含义 | 允许动作 |
|---|---|---|
| REJECT | 生意/价格/人/风险不过关 | 归档，除非新证据 |
| INFO-GAP | 信息不够 | 补资料，不给仓位 |
| WATCH | 值得跟踪但未达下注门槛 | 建监控清单 |
| STARTER | 小仓位研究仓可讨论 | 必须有明确 kill criteria |
| CORE | 高理解度、高质量、高安全边际 | 需要最严格复盘和监控 |

硬规则:

- 没有 `valuation.md` 或安全边际: 最高 `WATCH`。
- 没有 `inversion_map.md`: 最高 `WATCH`。
- 没有 `operator_underwriting.md`: 最高 `STARTER`。
- 社交媒体是主要证据: 最高 `INFO-GAP`。
- 不了解生意怎么赚钱: `REJECT` 或 `INFO-GAP`。

---

## 5. Weekly Operating Loop

### Monday: Queue Review

- 新 idea 入队。
- 给每个 idea 标 stage、priority、next action。
- 只允许 1-2 个 active deep research，避免分心。

### Research Blocks

- 每次只跑一个 block。
- raw 阶段不写结论。
- block 完成后更新 `research_status.md`。

### Investment Committee

IC 只读:

- `facts.md`
- `moat_map.md`
- `operator_underwriting.md`
- `inversion_map.md`
- `valuation.md`
- `memo-vN.md`

IC 不接受:

- 没 source_id 的事实。
- 只有观点没有证据的护城河。
- 没有下行情景的估值。
- 只讲 upside 的故事。

### Monitor

每个 WATCH/STARTER/CORE 必须有:

- 下一次财报要看什么。
- 哪个指标恶化会降级。
- 哪个价格才有安全边际。
- 哪个新闻/监管/技术事件会改变判断。

---

## 6. Standard Company Folder

```text
companies/<ticker>/
  research_status.md
  step0_plan.md
  raw/
  facts.md
  claim_ledger.csv
  moat_map.md
  operator_underwriting.md
  inversion_map.md
  bottleneck_map.md
  valuation.md
  model/
    ten_year_financials.csv
    owner_earnings_bridge.csv
    scenario_model.csv
  memo-v1.md
  memory.md
```

---

## 7. Quality Gates

### Gate A: Evidence

- [ ] 所有关键 claim 有 source_id。
- [ ] 事实、解读、情绪分开。
- [ ] 一手资料优先。
- [ ] 冲突数字没有被抹掉。

### Gate B: Business Quality

- [ ] 十年视角完成。
- [ ] owner earnings bridge 完成。
- [ ] moat mechanism 和 attack surface 完成。
- [ ] 技术颠覆检查完成。

### Gate C: People

- [ ] 创始人/CEO/董事会/控制权 map 完成。
- [ ] 激励和 capital allocation 检查完成。
- [ ] 文化和人才风险有证据。

### Gate D: Downside

- [ ] inversion map 完成。
- [ ] downside scenario 完成。
- [ ] kill criteria 可观测。
- [ ] 估值安全边际明确。

### Gate E: Decision

- [ ] verdict 与信息完整度匹配。
- [ ] next checks 明确。
- [ ] monitor plan 明确。
- [ ] memory 更新。

