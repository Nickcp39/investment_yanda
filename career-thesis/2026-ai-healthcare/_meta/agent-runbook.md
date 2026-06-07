---
title: Agent Runbook - 接手本研究的第一步
audience: Fresh Claude agent or future Nick
purpose: 冷启动接手时该读哪些文件、按什么顺序、第一步该干嘛
version: 1.0 (2026-05-16)
status: stable
---

# Agent Runbook

## 你是谁，你接手了什么

如果你是 fresh Claude agent 被指派来"继续 / 扩展 / refresh 这份 AI healthcare 研究"，
你接手的是 Nick 的个人 career × investment 双轨研究项目。
**这不是一个 sector report 项目，是一个为 Nick 的具体职业决策 inform 的项目。**

## 阅读顺序（强制 - 不要跳）

按这个顺序读，每个文件读完再读下一个：

1. **`_meta/decision-frame.md`** ← 为什么这份研究存在 + Nick 是谁 + 决策准则
2. **`_meta/schema.md`** ← CSV 23 列的含义
3. **`_meta/methodology.md`** ← 资格筛 + source 优先级 + 反 anti-pattern
4. **`00-research-plan.md`** ← 当前阶段 + status
5. **`data/companies.csv`** ← 已采集数据
6. **`01-us-landscape/00-segment-map.md`** ← 段级 narrative
7. (按需) `01-us-landscape/0X-*.md` 段内详细分析

## 第一步该干嘛（按场景）

### 场景 A: "请继续推进研究"

1. 读 `00-research-plan.md` 的 todo list（即 status 表）
2. 找下一个 status=pending 的 block
3. 按 methodology.md 的查询模板搜索
4. 一次只推进 1 个 block，写完 segment md + 更新 CSV
5. 在 sources.csv 记录关键数据点的来源
6. 更新本 block 在 plan 的 status 为 done
7. **停下来等 Nick 反馈，不要连续推进多个 block**

### 场景 B: "Refresh 6 个月前的数据"

走 `_meta/refresh-protocol.md` 流程。

### 场景 C: "添加新 segment / 新公司"

1. 读 decision-frame.md 确认这个 segment / 公司是否符合本研究范围
2. 如果是新 segment：在 schema.md 加 enum，更新 plan
3. 检查公司是否过资格筛（methodology.md）
4. 加入 CSV + 在对应段 md 加入分析

### 场景 D: "Nick 想看某个具体问题"

例如："S5 imaging AI 中创始人是 PhD 的公司有几家？"
直接查 CSV：

```python
import pandas as pd
df = pd.read_csv("data/companies.csv")
df[(df.segment == "S5") & (df.founders_phd_count >= 1)]
```

不需要从头读所有 md。

### 场景 E: "Nick 改主意了，方向变了"

读 decision-frame.md 的 "什么会让本研究的结论改变" 表。
按表里说的做（归档 / 重读 / review）。

## 反 anti-pattern

- ❌ 跳过 decision-frame.md 直接动手——你会犯方向性错误
- ❌ 把 md 当 source of truth——CSV 才是
- ❌ 给公司打"profile match 分数"——Nick 明确说过不要数字分
- ❌ 用"Nick 进不去"作为剔除理由——见 methodology.md
- ❌ 用 aifundingtracker 等聚合器作为唯一来源——经常错（详见 methodology.md Tier 5）
- ❌ 一次性批量推进 8 个 block——一次 1 个，写完确认再继续

## 输出 / 沟通规范

- Nick 偏好中文 + 数据 + 直接结论。不要英文，不要"as an AI"，不要 hedge 太多
- 段 md 文件用中文标题 + 中文内容
- schema / methodology / 代码注释用英文 OK（机器友好）
- 任何"推荐"必须给理由 + trade-off。不要单一选项

## 如果你不确定

如果遇到模糊情况，**问 Nick**，不要猜。例如：
- 新出来一家公司不在 candidate pool，进不进？
- 某个估值数字两个 Tier 2 源冲突？
- segment 边界模糊（例：scribe + RCM 二合一）？

不要为了快进编决定。Nick 的反馈比你节省的时间贵。
