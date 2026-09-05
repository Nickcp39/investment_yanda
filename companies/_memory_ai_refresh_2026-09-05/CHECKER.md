# 批次质量门 (CHECKER) — memory_ai_refresh_2026-09-05

活体质量门(≠ 回测的 lookahead QA)。每家跑完 Runner 后过这套检查,输出
`companies/<ticker>/2026-09-05/checker_report.md`,判 `CLEAN` / `FIX-NEEDED`。

---

## ⚠️ 本批的角色隔离状态(先读这条)

`PROTOCOL.md §3` / `PIPELINE.md` 要求 **Checker ≠ Runner**。**本批未满足** ——
同一 agent 兼任两角(用户已明确不要擅自派生 subagent)。因此:

- 本批的通过标签是 **`CLEAN (self-checked)`**,**不等同于** mega7 批次的 `CLEAN`。
- **仍然独立的部分**:`verify_freshness.py` 是机械验证器 —— 它自己重抓价格、自己跑 T1–T6,
  完全不读 runner 的判断。这一层的独立性是真的。
- **不独立的部分**:C3/C6/C8/C9 这类判断性检查抓不到 runner 自身的系统性偏见。
- **硬约束**:**任何一张卡从 WATCH 升 STARTER 之前,必须先补一次真正独立的 Checker。**
  本批全为 WATCH,无卡因此偏离被放行 → 偏离未造成决策后果。

---

## A. 机械门(不过就是 FIX-NEEDED,无例外)

| 门 | 要求 | 本批结果 |
|---|---|---|
| **A0 基准新鲜度** 🆕 | 跑批前 `git fetch`;refresh 卡的 `refresh_of` 必须是该 ticker 下**最新**目录 | ⚠️ **本批初次违反(NBIS)**,已修正 → INC-002 |
| **A1 freshness** | `freshness_check.json` 存在且 `status == "PASS"`(`verify_freshness.py` exit 0) | **5/5 PASS** |
| A2 双源 | 每个量化 LIVE 字段(price / market_cap / 52wk_high / 52wk_low / shares_out)≥2 独立源 | 5/5 |
| A3 市值恒等 | `price × shares` 对上卡内 `as_of_market_cap`,容差 0.5% | 5/5,全部 0.00% |
| A4 单一真值 | `as_of_price` 逐字出现在 facts.md / valuation.md / model CSV / decision_card.md | 5/5(T5) |
| A5 距高点自洽 | 叙述里的"距高点 −X%" 与 `price / 52wk_high` 相符,容差 1.0pt | 5/5(T4),全部 0.0pt |

> **A1 的一次真实拦截**:NVDA 首跑 **BLOCK on T2**(价格距 52 周高点 2.61%,落在 3% 警戒带内)。
> 处理方式**不是**直接翻 `low_high_hug_justified`,而是先确认验证器**自己独立回抓**的结果是
> 230.36 / 2026-09-04 —— 与卡内值同值同日,直接排除了 INC-001 那个"抓到极值当收盘价"的失效模式。
> 确认后才置标志位并写入 `hug_justification`。**证据先行,标志位在后。**

## B. 结构门

| 门 | 要求 | 本批结果 |
|---|---|---|
| B1 | 恰好 6 个 module_signals,每个 ∈ [−2, +2] | 5/5 |
| B2 | 两轴 verdict 分开出(新钱 / 存量) | 5/5 |
| B3 | `runner_dissent` 存在且实质(>200 字符,不是"无异议") | 5/5 |
| B4 | ≥1 个 A1 一手源 | 5/5 |
| B5 | 情景模型 CSV 能重算出卡内 headline(buy_below / 公允) | 5/5 |

## C. 裁决门(本批的核心)

**C1 verdict 上限 = 信息完整度**:`<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER / >80 CORE`。
本批完整度 60–70% → 完整度上限为 STARTER。

**C2 价格先于完整度封顶**(`PIPELINE.md` 明文):对价格已无安全边际的名字,
**M6 先封顶,补完整度也不翻盘**。

**C3 不得在价格高于 buy_below 时出 STARTER。** 机械检查,5/5 通过。

**C4 ⭐ 机械触发 ≠ 可执行入场(本批新增,由 GEV 逼出来的)**

> 价格穿过某条 buy_below 线时,**先重算那条线的锚,再决定是否兑现**。
> 若锚的承重输入已被新披露证伪 → **下修锚,不得买入**。
>
> GEV 实例:941.95 穿过 $950 STARTER 线;但 2Q26 10-Q 显示 H1 经营现金流增量主要来自
> 合同负债 +$118 亿(客户预付款),而旧模型把 ~$180 亿"净现金"加进了 2028 权益价值 ——
> 那是针对未交付涡轮机的浮存,与它预付的未来收入重复计算。
> → $950 作废,按 8% hurdle 重推为 **$786**,现价高出约 20% → **不兑现**。
> 交叉印证:$786 与旧卡 **$756 CORE**(同为 8% hurdle 推导)收敛 —— 去掉错误后两法自洽。

**C5 现金流构成检验(本批新增,建议升为常规)**
报表 FCF 必须能被解释来源。本批三家在此失分,形态各异:
GEV(浮存)· SNDK(合资表外 capex)· NVDA(OCF 仅为 GAAP 净利 40% + GAAP EPS 反超 non-GAAP)。

**C6 自身历史回撤校准(本批新增)**
出现"已经跌了不少"类判断时,必须用**标的自身**的回撤历史校准,不用体感。
MU:2006 年以来五次大回撤中位数 **−54%**,本轮 −19%。

## D. 来源纪律

- 每条载荷性 claim 带 来源名 + 公开日期 + link + tier。
- primary(10-K/10-Q/8-K/6-K/财报电话)> 高质量 secondary > commentary(**仅情绪**)> 社媒(**仅线索**)。
- **本批特别标注**:2026-09-04 板块大涨(SNDK +11.9% 收在全日最高、MU +6.1%、NBIS +7.5%)
  由 **BofA 上调 + UBS 报告 + 希捷财报**驱动,**无一家自身新披露** →
  全部记为 **C1 tier(SENTIMENT ONLY)**,不得进入任何 buy_below 推导。

## E. 诚实标签

- 状态一律 `DECISION_DRAFT`,完整度如实写,**不得谎称 COMPLETE**。
- 未做的模块要说没做(本批未重写 business_model / moat / operator / ic_panel)。
- 机械结论感觉不对 → 写 `runner_dissent`,**不要偷偷改数**。
  本批 MU 与 SNDK 各有一处"标记但不修改"的判断张力,均已入卡。

---

## 本批结果

| Ticker | A 机械 | B 结构 | C 裁决 | D 来源 | 判定 |
|---|---|---|---|---|---|
| NVDA | PASS(T2 拦截后以证据解除)| PASS | PASS | PASS | **CLEAN (self-checked)** |
| SNDK | PASS | PASS | PASS | PASS | **CLEAN (self-checked)** |
| MU | PASS(T6 告警保留,如实)| PASS | PASS | PASS | **CLEAN (self-checked)** |
| NBIS | ⚠️→PASS(**A0 违反后重建**,基准 07-10 → **08-12**)| PASS | PASS | PASS | **CLEAN (self-checked, rebuilt)** |
| GEV | PASS | PASS | PASS(C4 触发并正确不兑现)| PASS | **CLEAN (self-checked)** |

**0 FIX-NEEDED。新钱 STARTER = 0。**


---

## 附:A0 基准新鲜度门的由来(INC-002)

本批最初在一个**落后 `origin/main` 29 个提交**的本地库上起跑,NBIS 因此拿 `2026-07-10` 当上一版,
而远端已有 `2026-08-12`(Q2'26 事件重跑)。

**关键教训:`verify_freshness.py` 覆盖不到这个轴。** 它验证的是 LIVE **行情**数据(INC-001 的失效模式),
没有"我的基准档案是不是最新的"这个概念。**用错基准和用对基准的两张 NBIS 卡都干净地过了门 ——
而且过得对**,因为价格从来没错。

→ 所以 A0 是一道**独立的门**,不能靠 A1 顺带覆盖。
