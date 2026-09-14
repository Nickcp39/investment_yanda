# Memory / AI-infra 活体批次 — 运行计划 (PLAN)

**批次 ID**: `memory_ai_refresh_2026-09-05`
**as_of (冻结边沿)**: 2026-09-05(周六 → as_of_price = 2026-09-04 周五收盘,last close ≤ as_of)
**pipeline_version**: `lean-6module-v1.1` · **weights_version**: `none`
**状态**: ✅ **5/5 完成,freshness gate 5/5 PASS。裁决:全部 WATCH,新钱 STARTER = 0 个。**
**主目录**: `companies/_memory_ai_refresh_2026-09-05/`

---

## 0. 触发与目标

用户提问:*"存储是不是已经跌了不少,说不定是个机会"* —— 要求对 NVDA / SNDK / MU / NBIS / GEV
重跑 pipeline,**核心交付是"现在有没有 STARTER"**。

五家全部有前序 dossier,因此本批是 **REFRESH 批次**,不是新建。每家回答三个问题:

1. 价格相对上一版怎么动了(M6)
2. 上一版之后出了什么**已归档财报**(M1/M4)
3. **verdict 是否翻转** —— 特别是有没有跌进 buy-below

## 1. 名单与本轮动作

| # | Ticker | 前序 dossier | 上版价 / 裁决 | 本轮动作 | 本轮类型 |
|---|---|---|---|---|---|
| 1 | NVDA | `nvda/2026-07-10` | $210.96 · WATCH | 折入 Q2 FY27 (8/26) | LIGHT REFRESH |
| 2 | SNDK | `sndk/2026-06-22` | $2,288.92 · WATCH / TRIM | 折入 Q4 FY26 (8/5) + 投资者日 (8/13) | REFRESH |
| 3 | MU | `mu/2026-07-10` | $979.30 · WATCH | **无新财报**(Q4 FY26 = 9/30) | RE-PRICE ONLY |
| 4 | NBIS | **`nbis/2026-08-12`** ⚠️ | ~$215–220 · WATCH(真实参照收盘 $254.40 @08-13) | 重定基准 + 一手源升级 | RE-PRICE + SOURCE UPGRADE |
| 5 | GEV | `gev/2026-06-19` | $1,109.73 · WATCH | 折入 Q2 2026 (7/22) **+ 修正估值模型错误** | REFRESH + 模型修正 |

## 2. 每家产物(LIGHT REFRESH 档,对齐 `mu/2026-07-10` 与 `nbis/2026-07-10`)

```
companies/<ticker>/2026-09-05/
  decision_card.json       ← 锁定卡(打版本戳 + module_signals + kill + runner_dissent)
  decision_card.md         ← 人读卡
  facts.md                 ← M1 证据(EVIDENCE / INTERPRETATION / OPEN 分层)
  valuation.md             ← M6 估值与价格带
  model/scenario_model.csv ← 情景与 IRR(数字在此重算,不手抄)
  freshness.json           ← LIVE 数据 manifest(每个量化字段 ≥2 独立源)
  freshness_check.json/.txt← verify_freshness.py 产物,须 status==PASS
  refresh_note.md          ← old → new 对照
  checker_report.md        ← 质量门
```

**不产**完整 GOOGL 级 dossier(business_model / moat / operator / ic_panel 等)。五家的前序档案里这些
模块未被本轮证据推翻,重写属于文档工厂,不是决策工作。完整度因此封在 **60–70%**,如实标注。

## 3. 执行与角色

### ⛔ 批次开跑前的强制步骤(INC-002 后新增)

```bash
git fetch origin
git log --oneline HEAD..origin/main                       # 本地是否落后?
git diff --name-only HEAD origin/main -- companies/<tickers>   # 远端有没有更新的档案?
```

**分支落后于远端时不得开跑。** 本批违反了这一条 —— 在落后 29 个提交的库上起跑,导致 NBIS 用错基准。
见 `INCIDENTS.md → INC-002` 与 `synthesis.md §0'`。

```
每家: Runner 取数 + 重算 → 锁 decision_card.json → freshness.json
      → verify_freshness.py(exit 0)→ freshness_check.json PASS
      → Checker 过 CHECKER.md → checker_report.md
末端: Synthesis 读全 5 张卡 → 排序 + 单因子集中度检查 → synthesis.md
```

### ⚠️ 协议偏离(必须记录,不得隐瞒)

`PROTOCOL.md §3` 与 `PIPELINE.md` 要求 **Checker ≠ Runner**(角色隔离,独立重算/抽验)。
**本批未满足**:同一个 agent 同时担任 Runner 与 Checker(用户已明确不要擅自派生 subagent)。

后果与缓解:

- **真实削弱**:checker_report.md 是**自检**,不是独立复核。它抓不到"我自己的系统性偏见"。
- **仍然成立的部分**:`verify_freshness.py` 是**机械**验证器,独立重抓价格、独立跑 T1–T6,
  不依赖 runner 的判断 —— 这一层的独立性是真的,5/5 PASS 有效。
- **本批 CLEAN 的含义因此被降级**为 `CLEAN (self-checked)`,不等同于 mega7 批次的 `CLEAN`。
- **补救路径**:任何一张卡要从 WATCH 升 STARTER 之前,必须先跑一次真正独立的 Checker。
  本批全为 WATCH,**没有卡因此偏离而被放行**,所以偏离未造成决策后果。

## 4. 交付结果(2026-09-05)

| Ticker | as_of price | vs 上版 | 新钱裁决 | 存量裁决 | buy_below | 距入场 | freshness |
|---|---:|---:|---|---|---:|---:|---|
| NVDA | 230.36 | +9.2% | **WATCH** | HOLD | **$148–222(带)** | −3.4% ~ −35.6% | PASS |
| SNDK | 1740.00 | −24.0% | **WATCH** | HOLD *(TRIM 软化)* | **$769**(↑ 自 $600) | −55.8% | PASS |
| MU | 1016.59 | +3.8% | **WATCH** | HOLD | $650(不变) | −36.1% | PASS |
| NBIS | 226.39 | −11.0%¹ | **WATCH**(第三次) | HOLD | $150–180 · no-chase **≥$250** | −20.5% ~ −33.7% | PASS |
| GEV | 941.95 | −15.1% | **WATCH** | HOLD | **$786**($950 STARTER 线**作废**) | −16.6% | PASS |

¹ 相对 08-12 卡的真实参照收盘 $254.40(08-13),非相对 07-10。

**新钱 STARTER = 0 个。** 唯一触发机械入场线的是 GEV($941.95 < $950),但该锚被 Q2 的 10-Q 证伪,
未予兑现 —— 详见 `gev/2026-09-05/valuation.md` 与本批 `synthesis.md`。

## 5. 本批方法论产出(可复用,非个股结论)

1. **"机械触发 ≠ 可执行入场"**:GEV 展示了一条陈旧锚上的价格触发。规则:**触发时先重算锚,
   再决定是否兑现**;锚的输入被新披露证伪时,应下修锚而不是买入。
2. **现金流质量是本批共同瓶颈**,且三家形态不同:
   - **GEV** —— FCF ≈ 2.2× EBITDA,来自客户预付款(合同负债 +$118 亿),是浮存不是盈利
   - **SNDK** —— capex 仅占收入 0.9%,产能在 Kioxia 合资表外,报表 FCF 低估真实资本强度
   - **NVDA** —— OCF 仅为 GAAP 净利的 40%,且 GAAP EPS 反超 non-GAAP,OE 桥断裂待 10-Q
   → 建议把**"报表现金流的构成检验"**升为常规模块(当前散在 M4 里,没有固定检查项)。
3. **"跌了不少"必须用标的自身历史校准**:MU 自 2006 年的五次大回撤中位数 −54%,本轮 −19%。
   建议 M6 增加一个机械字段 `own_history_drawdown_percentile`。

## 6. 下一步(按优先级)

1. **2026-09-30 MU Q4 FY26** —— 本批最高价值的单一事件。第一份能验证"合约价涨幅衰减是否落到报表"
   的数据,同时交叉检验 SNDK 的 80% 毛利率叙事。
2. **NVDA Q2 FY27 10-Q** —— 解开 OE 桥。若闭合,NVDA 是本书在此复合体里的第一个 STARTER 候选。
3. **2026-10-21 GEV Q3** —— 看调整后 EBITDA 利润率是否向 2028 路径收敛(现 11.3% vs 需约 20%)。
4. **NBIS Q3** —— ARR 是否从 $30 亿 走向 $70–90 亿(六个月 2.3–3.0×);active MW 是否终于披露。
5. 补一次**真正独立的 Checker**,消除本批 §3 的协议偏离。
