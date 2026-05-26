# 中国医疗行业结构与机会分析 — 研究计划

> 创建：2026-05-16
> 目的：对仗 US 那份重写 China，但不照搬 US 的 6 层模板
> 状态：**等 Nick greenlight 才开始 Block 1.1**

---

## 1. 输出物（两份，对仗 US）

| 文件 | 对应 US 文件 |
|---|---|
| `sectors/china-healthcare/行业结构与机会分析.md` | `sectors/us-healthcare/行业结构与机会分析.md` |
| `sectors/china-healthcare/各层工作机会矩阵.md` | `sectors/us-healthcare/各层工作机会矩阵.md` |

**现有的 [`行业全景与切入点.md`](sectors/china-healthcare/行业全景与切入点.md) 不删**，定位降为"个人决策侧文档"（约束/排除/三城/5 个口子）。新两份是"行业侧文档"，分工清楚。

---

## 2. 层数：不锁死 6 层，先做完 1.1-1.3 看实际再定

US 那份是 6 层。中国结构有 3 个 US 没有的维度，可能需要加层 / 改层：

| China-specific | 为什么 US 没有 |
|---|---|
| 集采 / DRG / 国谈 | 政府单一买方定价权 |
| 公立医院 vs 民营医院 二元结构 | 美国不分公私 |
| 出海路径（药/械/CXO/AI） | 美国是被出海方 |

**预案：6+1 层**
- 1.1 宏观盘子
- 1.2 钱从哪来（医保 / 财政 / 商保 / 自费）
- 1.3 钱花在哪（医院 / 药 / 器械 / 服务）
- 1.4 产业垂直分层（监管 / 付费 / 产业 / 终端）
- 1.5 子行业 + 头部公司
- 1.6 工种 + 薪酬层级
- 1.7 出海路径层（China-only）

做完 1.3 如果发现 1.4 跟前 3 节冗余，砍掉合并。

---

## 3. 数据源（按优先级，data_as_of 必填）

**P1 primary**
- 国家卫健委《卫生健康统计年鉴》2024
- 国家医保局《医保基金运行报告》2024 / 集采批次数据
- 国家统计局年度数据
- NMPA 注册年报
- 头部公司年报（H 股 / A 股财报、招股书）

**P2 secondary（数字带日期，标注口径）**
- 米内网（药品销售）
- 灼识 / 弗若斯特沙利文 招股书行业数据
- 中商情报 / 头豹 / 艾瑞咨询

**禁止**：自媒体公众号数字、未署名的"亿欧/36 氪"汇编、AI 估算未标注的数字。

---

## 4. 已有 25 公司 CSV 的处理

来源：`festive-lamarr-2a6ec5/career-thesis/2026-ai-healthcare/data/china_companies.csv`

**先 audit 再用：**
1. 拷贝到 `sectors/china-healthcare/data/china_companies-imported.csv`
2. 随机抽 5 行，逐字段交叉验证（估值 / 营收 / 最新轮 / 上市状态 / 出海状态）
3. 通过的字段直接用；可疑的字段标 `<audit-pending>` 后续单独补
4. 用法：作为 1.5 "AI 医疗子行业头部公司"的种子表，不是全部子行业

**不要做：** 直接 trust + 拷进文档不审计。

---

## 5. 执行顺序（一段一段做，每段 STOP 等 review）

```
Block 1.1 宏观盘子               ~5 web fetches    STOP → Nick review
Block 1.2 钱从哪来                ~8                STOP
Block 1.3 钱花在哪                ~6                STOP
[决策点] 1.4 是否需要单独成层？
Block 1.4 产业垂直分层（如保留）   ~3                STOP
Block 1.5 子行业 + 头部公司        ~15 (含 CSV audit) STOP
Block 1.6 工种 + 薪酬层级          ~10               STOP
Block 1.7 出海路径层               ~10               STOP
─────
Part 2 机会分析（钱→AI→其他）     ~10               STOP
Part 3 最优工作解（我写候选 + 你拍） ~3               STOP
─────
各层工作机会矩阵.md（独立文档）     ~20               最后做
```

每个 Block 完成后：
- 更新本 plan 的进度表
- snapshot 关键数据到 `data/snapshots/`
- 写一行 "下一步问号" 等 Nick 确认

---

## 6. 明确不做的事（前一份 agent 跑歪的教训）

- ❌ 不一口气推 Block 1.2 → 1.7
- ❌ 不自己改 plan 版本（v1 → v2 → v3 同一天 3 版那种）
- ❌ 不建 `_meta/` 治理套件 / refresh-protocol / agent-runbook
- ❌ 不写 HTML 报告（除非 Nick 明说要）
- ❌ 不自己 synthesize 最终"职业主线推荐"（那是 `career-thesis/` 那份 elevator-map 的事，不是 sectors/ 文档的事）
- ❌ 不剔除"难进"的公司（违反 decision-frame 的 "不靠成功率思考"）
- ❌ 数字不带 data_as_of + 出处不写

---

## 7. 进度表（每 Block 完成更新）

| Block | 状态 | 数据点数 | sources 记录 | snapshot |
|---|---|---|---|---|
| 1.1 宏观盘子 | pending | - | - | - |
| 1.2 钱从哪来 | pending | - | - | - |
| 1.3 钱花在哪 | pending | - | - | - |
| 1.4 产业垂直分层 | pending | - | - | - |
| 1.5 子行业+头部公司 | pending | - | - | - |
| 1.6 工种+薪酬 | pending | - | - | - |
| 1.7 出海路径 | pending | - | - | - |
| Part 2 机会分析 | pending | - | - | - |
| Part 3 最优解 | pending | - | - | - |
| 工作机会矩阵.md | pending | - | - | - |

---

## 8. 等 Nick 拍板的 3 件事

1. **6+1 层方案 OK 吗？** 还是先做 6 层、出海作为 Part 2 的一个机会维度？
2. **Web fetch 预算**：Block 1.1 大概 5 次搜索（卫健委 / 医保局 / 统计局 / 世卫 / OECD），可以直接跑吗？
3. **输出目录结构**：是否在 `sectors/china-healthcare/` 下加 `data/` 子目录存 CSV 和 snapshots？
