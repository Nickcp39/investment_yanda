# SaaS 去泡沫批次 — 运行计划 (PLAN)

**批次 ID**: `saas_derate_2026-09-01`
**as_of**: 2026-09-01 · **pipeline_version**: `lean-6module-v1.1` · **weights_version**: `none`
**主目录**: `companies/_saas_derate_2026-09-01/`

---

## 0. 本批范围与选股

用户点名五家：**XYZ(Block) / SNOW / NFLX / ADBE / ORCL**，并指定
**「先跑没跑过的，跑过的先等等」**。

| Ticker | 库内状态 | 本批动作 |
|---|---|---|
| **XYZ (Block)** | ❌ 从未覆盖 | ✅ **全建** `companies/xyz/2026-09-01/` |
| **SNOW** | ❌ 从未覆盖 | ✅ **全建** `companies/snow/2026-09-01/` |
| NFLX | ✅ `2026-08-07` WATCH 0% | ⏸ 等（卡未过期） |
| ADBE | ✅ `2026-08-07` STARTER 3% | ⏸ 等（卡未过期） |
| ORCL | ✅ `2026-08-07` WATCH 0% | ⏸ 等（卡未过期） |

> 三家已有卡距今 25 天，`buy_below` 与 verdict 均未被事件推翻，**重跑等于花一轮换一个已知答案**
> （沿用 `_derated_bigtech_2026-08-07/PLAN.md` §0 的同一条筛选原则）。

### 为什么这两家值得单独跑

- **SNOW**：本库**第一个 consumption 计费**的标的。此前所有 SaaS 观察都建立在
  「收入 ∝ 人头（被杀）vs 收入 ∝ 机器用量（被买）」这条分界线上，而 SNOW 属于后者
  **却在 2026 年被杀过一轮（4/10 见底，最大回撤 −56%）** —— 是这条线的**反例**。
- **XYZ**：**−71% from ATH（$281.81 @2021-08-05 → $82.02 @2026-08-31）**，
  但**当前贴 52 周高**。也就是说它是「五年前崩掉、崩完之后生意继续复合、
  倍数一直没回来」的样本 —— 与 ADBE/INTU 的「一年内崩掉」是**不同的时间结构**。
  本库没有这一类。

---

## 1. 本批要回答的 thesis

上一批把「崩的是倍数还是生意」升级成了两步分解（倍数崩了，账上找不找得到匹配的损伤）。
本批要答的是**上一批答不了的两个**：

### T1（主命题）：分界线要不要改写？

> 上一批的分界线是 **「收入 ∝ 人头 vs 收入 ∝ 机器用量」**。
> SNOW / DDOG / MDB 三家全是 usage 计费，**三家全被杀过**。
> 候选改写：**不是「人头 vs 机器」，而是「用量来自谁」——
> 来自分散的企业（可续），还是来自少数几家 AI 公司（DDOG 的九位数单一客户）。**

**每家必须显式回答**：这家公司的收入，有多大比例的边际增量来自
**AI 原生公司**（而不是传统企业 IT 预算）？拿不到披露就明确写 OPEN，不许推测。

### T2：「往返」是不是第三类？

本库现有两类：**倍数崩 + 有损伤（别接）** / **倍数崩 + 无损伤（错杀候选）**。
SNOW（−56% → 基本收复）和 CRM（−60% → 距 52 周高 −4%）提示可能有第三类：
**倍数根本没被永久重定价，只是被流动性甩了一轮。**
若成立，则「跌了 50%」这个筛选条件本身在这一类上**不产生任何信息**。

### T3（每家必答，沿用上批）
1. 把跌幅拆成 (i) 倍数压缩 (ii) 盈利/FCF 基数变化，**给算术不给叙事**。
2. **点名 owner-earnings 锚并做敏感性**（META 教训：换个锚就跨过 8% 门槛）。
3. 护城河做 BSX 式检验：**结构性锁定 vs 在位惯性**。
4. **股东权益方向**：股数在增还是在减？SBC 占收入多少？——本批两家在这一项上
   预期是**相反方向**，是最干净的对照。

### 各家专属命题

- **SNOW**：① SBC = 收入的 35–36%，GAAP 净亏 $1.329B ≈ SBC —— 「非 GAAP 10% 经营利润率」
  和「GAAP −31%」之间那 41pp 到底是不是 owner earnings 的真实成本，必须给出**三锚敏感性**。
  ② AI 产品**毛利率更低**（产品毛利 76%→75%），增长越快毛利越薄，这是与 ADBE/INTU
  完全不同的增长质量问题。③ **2026-09-02（明日）出 Q2 FY2027 财报** —— 见 §3 特别条款。
- **XYZ**：① 生意是**两个**（Square 商户 + Cash App 消费者），必须**分部判**，禁止混合结论
  （沿用 INTU 四分部的处理）。② **9,117 BTC 长期持仓 + 299 BTC 运营** + Proto 矿机业务
  —— 估值里 BTC 是资产还是噪声，必须单独剥离，不许混进经营价值。
  ③ 连续 4–5 个季度 beat + 抬指引而股价不动 —— 这是「市场不给倍数」的纯样本。

---

## 2. 🔴 INC-004：freshness 门本批**不可用**（开跑前必须先读）

**现象**：本环境的出口代理封掉了**全部**行情源。实测：

```
query1.finance.yahoo.com   403 CONNECT rejected (gateway policy denial)
stockanalysis.com          EGRESS_BLOCKED
stooq.com / finviz.com / api.nasdaq.com / marketwatch.com / wsj.com   000
www.sec.gov / data.sec.gov / efts.sec.gov / s26.q4cdn.com / IR 站点    000
```

**后果**：`scripts/verify_freshness.py` 的第 1 步就是用
`market_data_download.fetch_yahoo` **独立重取价格**——取不到即 exit 2。
因此本批**无法产出 `freshness_check.json` status=PASS**。

按 INC-001 立下的规则原文：

> *A dossier may be marked CLEAN only if this validator exits 0 and a committed
> freshness_check.json with "status":"PASS" exists for that (ticker, as_of).*

**⇒ 本批两个 dossier 一律不得标 CLEAN。**

### 本批的替代处理（不是绕过，是降级并声明）

1. 所有行情类事实（价格 / 52周带 / 市值 / 股数）状态一律 **`unverified_secondary`**，
   来源记为「WebSearch 二手摘要」，**不得进入任何 BUY 依据**。
2. **M6 定价模块输出「区间」不输出「点」**，且必须写明价格不确定性对 IRR 的传导。
3. **verdict 上限按完整度封顶**（<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER）。
   行情不可验证会直接压低完整度 —— 预期本批两家**都到不了 STARTER**。
4. 财报口径数字（营收/毛利/SBC/RPO/NRR）来自公司自己的季报新闻稿转述，
   tier 高于行情，但**仍未见一手 8-K 原文**，同样标 `unverified_secondary`。
5. **T1 tripwire「current ≈ 52wk high/low」本批预期在 XYZ 上触发**
   （$82.02 vs 52wk 高 $82.50，距离 0.6%），必须在卡上显式写出，不许压掉。

> **这条不是免责声明，是本批最重要的一条结论**：
> **在拿不到可机械验证价格的环境里，本框架只能产出"生意判断"，不能产出"买卖判断"。**
> 两者的分界线正好落在 M6。

---

## 3. SNOW 的特别条款：财报在明天

`SNOW` 于 **2026-09-02** 发 Q2 FY2027。市场预期营收约 **$1.48B**。

**不推迟。理由是这恰好是本库最缺的东西：**

> 全库 40 张 decision_card，**没有一张是在事件发生前写下可证伪预测、事后再对账的**。
> `trading-desk/journal/TEMPLATE.md` 立的规矩是「事前写死什么情况算我错了」，
> 但从来没在公司研究上执行过一次。

因此 SNOW 这张卡**必须包含一个事前预测块**（写进 `decision_card.md` 和 `monitor.md`），
内容为可证伪的具体陈述，9/2 盘后直接对账，产物落
`companies/snow/2026-09-01/prediction_2026-09-02.md`。

**这张卡的价值不在裁决，在于它是本库第一个 pre-registered prediction。**

---

## 4. 铁律（沿用，含上批 INC-002 教训）

- **禁止 spawn 子 agent 做取数**（INC-002：7 agent 并发打爆 session 限额，连坐整批）。
- **先落盘再分析**：取到的数据立刻写 `raw/`，不攒到最后。
- **写入优先级**：`raw/` → `facts` + `claim_ledger` → `decision_card` → 核心命题模块 → 其余。
- 一手优先；KOL 只作线索，不进 facts、永不直接支撑 BUY。
- **verdict 上限 = 完整度**。
- 诚实状态标签：一轮跑完的诚实目标是 `DECISION_DRAFT`，**禁称 COMPLETE**
  （`frameworks/research_completion_checker.md` 的 Non-Negotiable Language Rule）。
- IC 五灵魂（段永平主审 + 巴菲特/芒格/Marks/Klarman），**无伪造引语**。
- `decision_card.json` 必须带版本戳。

---

## 5. 进度

| Ticker | Runner | Checker | 状态 | verdict | 倍数 vs 生意 | buy_below | 备注 |
|---|---|---|---|---|---|---|---|
| SNOW | ✅ | 自检(45%) | DECISION_DRAFT | **WATCH 0%** | **第三类：往返，未被永久重定价** | **~$173**（距 −48%） | 卡点=**价格 + owner-earnings 锚不存在**；三锚 98x/负/310x；附本库第一张 pre-registered prediction |
| XYZ | ✅ | 自检(48%) | DECISION_DRAFT | **WATCH 0%** | **第四类：损伤未知**（倍数 162.3% / 每股毛利 −62.3%） | **~$62**（观察线 $74，距 −10%） | 卡点=**完整度（坏账 O-X7），非价格**；⚠️ T1 tripwire 触发 |

> **批次结论见 [synthesis.md](synthesis.md)。** 一句话：
> **跌了 71% 的那家在回购股票，创新高的那家在发股票 ——
> 「跌得凶不凶」和「股东权益方向」完全不相关，
> 这是对「跌了 50% 才值得看」这个筛选逻辑最直接的反例。**

## 6. 批次外遗留（有时效，不在本批范围）

- **MSFT 卡仍过期**（上批 §5 已记，至今未处理）。
- **NBIS no-chase ≥$250 已于 08-13 触发**（$254.40），待拍板。
- **INTU 卡的 2026-02-03 「−10.9% 无公司事件」OPEN 已可关闭**：
  当日是 "SaaSpocalypse" 一词被 Jefferies 交易员 Jeffrey Favuzza 造出的日子，
  2026 年 1 月中→2 月中软件板块蒸发约 $1T，标普北美软件指数创 2008 年以来最差单月。
  **那是板块重定价日，不是公司事件日。** 待回填。
