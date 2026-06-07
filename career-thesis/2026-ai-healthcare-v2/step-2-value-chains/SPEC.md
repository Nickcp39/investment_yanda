---
step: 2
title: Value Chains — 每个 surviving 子赛道的钱流路径
input_from: step-1-macro-sizing
output_to: step-3-rent-capture-and-fit
status: spec-only (no thread has executed)
---

# Step 2 SPEC: Value Chains

## 1. Question

**对每个 survivor 子赛道，钱从 sponsor 经过哪些 actor 到 end user？每个 actor 在这条 chain 上做什么、收什么、profit margin 大概多少？**

## 2. Input

必读:
- `_methodology/process-overview.md`
- `_methodology/handoff-protocol.md`
- `step-1-macro-sizing/work/segments-ranked.csv` (只看 keep + escape 段)
- `step-1-macro-sizing/work/sources.csv` (可继承数据源)

参考（可选）:
- v1 (`../2026-ai-healthcare/01-us-landscape/*.md`) 段级分析里的 actor 信息（事实部分可用）
- 另一 AI thread 输出: `D:\work\investment\career-thesis\2026-ai-healthcare\outputs\us_healthcare_industry_structure.md` 中 US 6 层结构（已经把 sponsor → payer → service → product → infra → user 框架定好）— **本 step 直接复用此 6 层框架**

禁读:
- `_personal/nick-profile.md`
- 任何 step-3 / step-4 / step-5 的 work/
- v1 elevator-map 类结论

## 3. Output

### 3.1 主 artifact: 每个 surviving 段一份 `step-2-value-chains/work/{geography}/{segment_code}-valuechain.md`

例:
```
work/us/S5-valuechain.md
work/us/S3-valuechain.md
work/cn/S5-valuechain.md
work/cn/S3-valuechain.md
...
```

每份 md 结构（**严格遵循，便于 step 3 解析**）:

```markdown
---
segment_code: S5
geography: us
generated_by: thread-id, YYYY-MM-DD
input_source: step-1-macro-sizing/work/segments-ranked.csv row N
---

# {segment} {geography} value chain

## Layer A: Sponsors
- Actor: ...
- 出钱给谁: ...
- 收什么: ... (na if pure sponsor)
- 年支出 USD: $...B
- profit margin: na

## Layer B: Payers / Coverage decision makers
- Actor: ...
- ...

## Layer C: Service providers
...

## Layer D: Product makers (drug / device / SaMD)
...

## Layer E: Infrastructure / data / rails
...

## Layer F: End users
...

## Flow diagram (ASCII or mermaid)
[Sponsor] → [Payer] → [Provider] → [Patient]
                ↓
            [PBM/TPA]
            ...

## Notes
- 任何 anomaly / 数据 gap / 与 step 1 假设不一致的发现
```

### 3.2 配套: `step-2-value-chains/work/actors-master.csv`

跨所有段 + 双地理 的 actor 主表，schema:
```
actor_name, actor_type, layer (A-F), segments_active (列表), geography (us/cn/both),
revenue_usd_b, profit_margin_pct, employee_count, notes, sources
```

actor_type 枚举: government / commercial_payer / pbm / tpa / hospital_system / physician_group / pharmacy / lab / pharma / medtech / cro / ehr_vendor / clearinghouse / rcm_vendor / data_vendor / consumer_brand / employer

### 3.3 STATUS.md

## 4. Method

### 框架统一
**直接复用** 另一 AI thread 已建好的 6 层结构（Layer A-F），不要重新发明分层。
- A: Rules and regulators
- B: Sponsors and payers
- C: Care delivery
- D: Products and life sciences
- E: Infrastructure and rails
- F: End users

如果某个段的 actor 不 fit 6 层（罕见但可能），在该段 md 的 Notes 里 flag，不要自创新 layer。

### 跨地理对比
US 和 CN 不是 mirror。同一段（如 S5 imaging AI）在两国的 actor 结构可能差异极大（如 CN 没有 PBM）。每个段两份独立 md，**不要强行 1:1 对照**。

### 多 segment 并行
建议：每个 surviving segment × 2 geography = N × 2 个子文件。可用 subagent 并行 spawn (handoff-protocol §subagent)。

### Profit margin 估计
对每个 actor type，给出该 type 在 US/CN 的典型 profit margin（不是单家公司）。
- public 公司：用 10-K 数据
- private：用行业报告（McKinsey, Frost）
- 完全估不出：标 "unknown" 不要瞎写

## 5. Pruning

**本 step 不做 segment 级 pruning**（已在 step 1 做完）。但允许 **actor 级标记**：

- 段内的 actor 如果完全不参与钱流（如政府"道德监督"非付费方）→ 在该 actor 行加 column `excluded_from_money_flow: true`
- 但仍保留在 actors-master.csv（step 3 可能用到）

## 6. Validation

- [ ] 每个 surviving 段都有 us + cn 两份 valuechain.md
- [ ] 每份 md 6 层全覆盖（即使某层 actor 极少也要写"该层 actor: none for this segment, because ..."）
- [ ] actors-master.csv 行数 = 各段 unique actor 数之和（去重）
- [ ] STATUS.md = validated

## 7. Anti-patterns

- ❌ 列具体公司估值/融资（这是 step 1 的细节 + step 4 的 deep dive，不在 step 2）
- ❌ 给出 "S5 是最好赛道" 类对比（横向对比是 step 3）
- ❌ 写 "Nick 应该" 任何内容
- ❌ 自创 layer 命名（必须 A-F）
- ❌ 把 US 结构强加到 CN（如把 PBM 概念塞给 CN）

## 8. Money lens

> "我在每个 actor 那里写的 revenue 是它的 GMV / 流过它的钱 还是 它 truly 收入囊中（profit pool 一部分）的钱？这两个数字差几个量级，我有没有混？"

如发现混淆，在该 actor 行 notes 标注。

## 9. Effort hint

- per segment per geography ~1-2 天
- 假设 step 1 keep 6 段 × 2 geo = 12 子任务
- 单 thread 顺序: ~2 周
- 并行 (subagent per segment): ~3-5 天 + 0.5 天 actors-master 合并
