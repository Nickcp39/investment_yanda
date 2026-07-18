# 财富榜研究 — PLAN(先定目标 · 数据先行 · 分析后置)

## 0. 一句话
拉 **福布斯全球富豪榜(Forbes World's Billionaires)** 的 **Top 100**,三个快照
**2008 / 2015 / 2025**。先把三张干净数据表统计出来(+ 独立 checker 验),**统计完才分析**;
四条分析主轴 **分开做、一条一条来**,不一口气混比。

---

## 1. 为什么是这三年(不是随便选的)
| 年 | 时代定位 | 造富主力(待数据确认,此处是预期弧) |
|---|---|---|
| **2008** | 金融危机爆发前的顶点(该届 2008-03 发布,反映危机前财富) | 资源/大宗商品、电信、钢铁石化、俄罗斯寡头、印度实业、欧洲零售 |
| **2015** | QE 长牛中段,科技崛起但未统治 | 零售(Zara/沃尔玛)、工业(Koch)、奢侈化妆品、科技(Gates/Ellison)并列 |
| **2025** | 科技 + AI + 奢侈全面统治 | Musk/Zuckerberg/Bezos/Ellison/Arnault,英伟达系随 AI 上位 |

→ 三点正好卡住 **利润池从「资源/电信/零售」迁到「科技/AI/奢侈」的完整弧**,直接对应
你 pipeline 的 **M3(利润池/耐久性)**。

---

## 2. 研究对象与快照口径
| 快照 | 福布斯届次 | as_of(财富估值时点) | 取值 |
|---|---|---|---|
| 2008 | 2008 World's Billionaires | ~2008-02 | Top 100 |
| 2015 | 2015 World's Billionaires | ~2015-02 | Top 100 |
| 2025 | 2025 World's Billionaires | ~2025-02/03 | Top 100 |

→ 共 **300 行**人物数据。

---

## 3. Phase 1 — 数据采集(现在只做这个,不分析)

### 3.1 每行字段(受控 schema)
`rank` · `name` · `net_worth_usd_b`(当届名义值) · `age` · `source_of_wealth`(福布斯原文) ·
`industry`(受控词表,见 3.3) · `country` · `self_made_score`(福布斯 1–10,2008 可能缺) ·
`wealth_origin`(自创 / 继承 / 继承再增值) · `company` · `source_id`

### 3.2 来源(主 > 次,均记日期)
- **主源**:福布斯当届官方榜页(`forbes.com/lists` 存档 / `web.archive.org` 快照)。
- **次源交叉**:维基 “The World's Billionaires 2008/2015/2025”(引用福布斯、便于机读)、福布斯 profile 页。
- 纪律:**每个净值 + 排名都要能追到一个「带日期的福布斯当届来源」**;
  2008 的行只能用 2008 当届估值,**禁止**把某人后来的身家塞进 2008 行。

### 3.3 受控行业词表(为了三年可比,只准用这些)
`Tech · Telecom · Retail-Fashion · Industrials-Mfg · Energy-Resources · Finance-Investments ·
Real-Estate · Consumer-Food&Bev · Healthcare-Pharma · Media-Entertainment · Auto · Luxury ·
Diversified · Other`

### 3.4 产物
- `data/forbes_global_top100_2008.csv`(100 行)
- `data/forbes_global_top100_2015.csv`
- `data/forbes_global_top100_2025.csv`
- `data/sources.csv`(来源注册:id / 出版方 / 届次日期 / url / 主or次)
- (Phase 1.5)`data/master_matched.csv`:跨年人物匹配(person_key + 三年在榜与否 + 各年净值),供持久性分析用

### 3.5 出口
Phase 1 数据 **过 `CHECKER.md` → 判 CLEAN 才进 Phase 2**。

---

## 4. Phase 2 — 分析(统计完成后,分开做,一条一条)
四条主轴各自独立成文,**不一次性混比**;每条做完你看过再做下一条。默认顺序 A1→A2→A3→A4(可调):

| 轴 | 内容 | 产物 |
|---|---|---|
| **A1** | 利润池迁移 + 对现在的启示(哪些行业在造富/消失,映射现持仓) | `analysis/A1_profit_pool_migration.md` |
| **A2** | 财富持久性(谁三届都在、谁掉出去、为什么)→ 对应 operator 生命弧 + durability 天花板 | `analysis/A2_persistence.md` |
| **A3** | 结构分布变化(行业 / 国别 / 财富来源 自创vs继承vs投资) | `analysis/A3_distribution.md` |
| **A4** | 财富创造速度(0→Top100 用多久,三代人的速度差) | `analysis/A4_velocity.md` |

---

## 5. Phase 3 — 综合 + 呈现
四条做完 → `synthesis.md` + 自包含 `wealth_rankings.html`(记分卡 + 图表)。

---

## 6. 方法学注意(会写进每份产物脚注)
- 福布斯净值是 **估值**,非精确值;榜单方法多年有变化。
- **通胀**:$1B(2008) ≠ $1B(2025)。默认呈现名义值,A1/A4 另给 **CPI 调整到 2025 美元** 的对照
  (2008 ×≈1.45,2015 ×≈1.32,采集期确认系数)。
- **self-made score** 福布斯约 2014 起才有;2008 的 `wealth_origin` 需人工判定并标注来源。
- 快照统一为「当届发布值」,不追溯重估。

---

## 7. 交付物清单 + 进度表
| 阶段 | 产物 | 状态 |
|---|---|---|
| P1 | 3× Top100 CSV + sources.csv | ⬜ 待你确认 plan 后开跑 |
| P1.5 | master_matched.csv | ⬜ |
| CHK | checker_report.md(P1 数据过闸) | ⬜ |
| P2-A1 | 利润池迁移 | ⬜ |
| P2-A2 | 持久性 | ⬜ |
| P2-A3 | 结构分布 | ⬜ |
| P2-A4 | 创造速度 | ⬜ |
| P3 | synthesis.md + wealth_rankings.html | ⬜ |

---

## 8. 角色隔离(同你回测/批量的纪律)
采集者(Runner)与 **独立 Checker 不同 agent**:Checker 独立重算行数 / 排名连续性 / 净值单调 /
抽验 top-10 来源 / 查跨年匹配错配。
