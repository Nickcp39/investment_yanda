---
title: AI Healthcare 赛道研究 (career × investment 双轨)
owner: Nick
created: 2026-05-16
updated: 2026-05-16 (v4 - PAUSED, awaiting macro framework synthesis)
status: ⏸️ PAUSED — 用户决定先让多个 AI 并行做美国/中国整体医疗系统的宏观框架，本研究在用户 macro 阶段完成前不扩展
---

# ⚠️ 状态说明（2026-05-16 晚）

用户原话："我现在已经在要求其他的AI， 分析美国中国的整个医疗体系框架了，我们要从宏观到微观，来看到底我们最终能在哪里找到合适我们的位置， 不能盲目的上来就通过用户画像直接求职。"

**这意味着:**
- 本研究的 70 美国公司 + 25 中国公司 + 各段分析 + 统计 = 仍可作为参考数据
- 但**不再扩展**，不再加新公司、新段、新维度，不再产出新的 synthesis
- 用户 macro 阶段（其他 AI 协作中）完成后会重新决定本研究是否复用、如何复用

**已归档（用户明确否定的方向）:**
- `_archive/elevator-map.md` — 用户原话"彻底歪了"
- `_archive/pm-pathways.md` — 用户原话"也别想PM的事情了"
- 详见 `_archive/README.md` 的归档原因 + 历史教训

**仍可用作 reference 的:**
- `data/companies.csv` (70 US 公司) + `data/china_companies.csv` (25 中国公司) — 事实数据
- `01-us-landscape/` 7 段 narrative + `02-us-statistics/` 5 个 stats — 事实摘要
- `03-china-mapping/00-us-china-mapping.md` — 中美对应映射
- `_meta/` — schema / methodology / runbook（infrastructure）

**用户在 worktree 外的并行工作（不在本研究目录内）:**
- 用户另一个 AI 已经产出：`D:\work\investment\career-thesis\2026-ai-healthcare\outputs\us_healthcare_industry_structure.md` (6 层美国医疗结构图)
- 这是用户 macro 框架的一部分，本研究目录不复制不修改

---

# v3 范围（user 2026-05-16 第二次拍板）

## 核心修正

| v2 | v3 |
|----|----|
| 100 家强制样本 | **60-70 家**资格筛 |
| schema 偏投资视角（16 列） | schema 增加 career 字段（**23 列**）|
| md narrative 一次性 | **`_meta/` 套件 + snapshots/**，长期可复用 |
| 隐含"能不能上电梯"过滤 | **明确不靠成功率思考**；entry_paths 描述路径不打分 |
| 无 fresh agent 接手协议 | agent-runbook.md + refresh-protocol.md |
| 无 thesis 文档化 | decision-frame.md 锁定 Nick 的 thesis 和 trigger 列表 |

## 文件夹结构（v3 final）

```
career-thesis/2026-ai-healthcare/
├── 00-research-plan.md              ← 本文件
├── _meta/                           ← 长期 reusability 套件
│   ├── decision-frame.md            ← WHY (Nick 的 thesis + trigger list)
│   ├── schema.md                    ← CSV 23 列定义
│   ├── methodology.md               ← 资格筛 + source 优先级
│   ├── agent-runbook.md             ← fresh agent 冷启动
│   ├── refresh-protocol.md          ← 6/12 mo refresh 流程
│   └── refresh-log/                 ← 每次 refresh 留 log（未来）
├── data/
│   ├── companies.csv                ← 23 列 single source of truth
│   ├── sources.csv                  ← 关键数据点的引用追溯
│   └── snapshots/
│       └── companies-YYYY-MM-DD.csv ← 每次重大改动前 snapshot
├── 01-us-landscape/
│   ├── 00-segment-map.md            ← ✅ done
│   ├── 01-clinical-documentation.md ← ✅ done v1（需 retrofit Career 字段叙述）
│   ├── 02-clinical-decision-support.md ← pending
│   ├── 03-medical-imaging-ai.md     ← pending
│   ├── 04-drug-discovery-ai.md      ← pending
│   ├── 05-revenue-cycle-admin.md    ← pending
│   ├── 06-precision-medicine.md     ← pending
│   └── 07-consumer-virtual-care.md  ← pending
├── 02-us-statistics/                ← Phase 2
├── 03-china-mapping/                ← Phase 3
└── 04-synthesis/                    ← Phase 4
    └── elevator-map.md              ← 最终 deliverable
```

## Phase 1 进度

| Block | 状态 | CSV rows | 备注 |
|-------|------|----------|------|
| 1.0 Segment map | ✅ done | n/a | 8 段 + market sizing |
| 1.1 Clinical Documentation | ✅ done v1 + retrofit v2 schema | 11 | 段 md 写好；CSV 已升级到 23 列 |
| 1.2 Clinical Decision Support | ✅ done | 7 | OpenEvidence ARR $7.9M→$150M (19x YoY) 是 healthcare AI 史上最猛增长曲线之一。但赛道本质是 LLM 大厂赛道，**不是 Nick 的主线**|
| 1.3 Medical Imaging AI | ✅ done | 16 | **段最国际化** (Israel/Korea/India/Australia/UK/Sweden 等)。HeartFlow IPO $1.54B 范本。Subtle Medical 中美双总部对 Nick 是直接 entry path。|
| 1.4 Drug Discovery AI | ✅ done | 10 | **Insilico HK IPO Dec 2025 ($293M)** 是 Nick 中港双总部 + AI 医疗 + 出海 IPO 模式的直接范本。Recursion 已上市但持续亏损是 cautionary tale。|
| 1.5 Revenue Cycle / Admin AI | ✅ done | 12 (1 已在 S1+S6) | 含 Olive + Babylon 死亡 + Waystar/R1 incumbents。Olive 死亡红旗清单可复用于其他段评估 |
| 1.6 Precision Medicine | ✅ done | 9 | **段商业化最成立**（Tempus 2025 营收 $1.3B +83% YoY）。**新发现：MGI 华大智造海外业务应作为 Nick 主线候选（与联影智能并列）**|
| 1.7 Consumer / Virtual Care | ✅ done | 9 (3 dead) | 段死亡率冠军（$1.6B 烧光）。但 Hims & Hers 公开市场年化 $2.5B 营收。死亡红旗清单 + S6 Olive 共同 calibrate Nick 评估中国公司|

### Phase 3 双表架构（user 2026-05-16 锁定）

- `data/companies.csv` = US 公司（不动）
- `data/china_companies.csv` = 中国对应公司（新建空表）
- 互引用：US row 的 `china_counterpart` 字段 = 中国公司 name；中国 row 的 `us_counterpart` 字段 = 美国公司 name
- 中国 schema 多 4 列：`name_zh`（中文名）、`listing`（HK / A-share / US-ADR / private / preparing IPO）、`founders_returnee`（bool）、`overseas_status`（none/planning/piloting/active）、`overseas_target_regions`（SEA/EU/MEA/LATAM/NA/global）
- Phase 3 启动时正式补 `_meta/schema.md` 的中国部分（现在只有空 CSV header lock 决定）
| **总** | | **🎉 70 US + 25 CN PHASE 1-4 DONE** | |

## ✅ 全研究完成（2026-05-16）

- Phase 1: 70 美国公司 in `companies.csv` (7 段全覆盖)
- Phase 2: 5 cross-segment 统计 md in `02-us-statistics/` + 可复用脚本
- Phase 3: 25 中国公司 in `china_companies.csv` + mapping in `03-china-mapping/`
- Phase 4: **elevator-map.md** in `04-synthesis/` (最终 deliverable)
- 报告: `REPORT-phase1.html` (中英对照 + 图表) 已 refresh
- snapshot: `data/snapshots/companies-2026-05-16-FINAL.csv`

**下次 refresh 建议: 2026-11-16 (6 月后)，按 `_meta/refresh-protocol.md` 走**

## 接下来一步

**STOP for Nick greenlight on v3 pipeline.**

如果 Nick 确认 schema + _meta 套件 + retrofit 方向对，下一步：
- 按 methodology.md 流程做 Block 1.6 Precision Medicine（user 选定）
- 完成后 commit snapshot + update plan

## 执行规则（不变）

1. 一次推进 1 个 block，写完 md + 更新 CSV + 写 sources.csv 关键来源
2. 每个 block 完成后 snapshot CSV
3. 每个 block 完成后 stop，让 Nick review
4. 任何疑点（schema 冲突、估值二源不一致、段边界模糊）问 Nick，不猜

---

# 历史记录（archived）

- v1 (2026-05-16 早): top-5 dossier 方法 → 用户改 N=100 统计
- v2 (2026-05-16 中): N=100 + 16 列 schema → 用户改资格筛 + career schema
- v3 (2026-05-16 晚): 60-70 资格筛 + 23 列 schema + `_meta/` 套件 ← 当前
