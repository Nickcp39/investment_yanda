# 佩洛西持仓批次 · 2026-09-28 — 运行计划 (PLAN)

**批次 ID** `pelosi_book_2026-09-28` · **as_of** 2026-09-28（价格 = 2026-09-25 周五收盘；周一开盘前）
`lean-6module-v1.1` · weights `none` · run_type = **首次建档**（8 家均无旧 dossier）

---

## 0. 选股来源与定位

**来源**：用户贴入的一张「佩洛西持仓表」（13 个名字，含占比与持仓形式）。
**本库对这张表的定位 = 线索，不是证据**（沿用"KOL 只作线索，不进 facts、永不直接支撑 BUY"）。
表里的每一项持仓都没有进入任何一家的 facts；本批研究的是**这些公司**，不是佩洛西。

**范围**：13 名中**已跑过的 5 名不重跑**（NVDA 2026-09-05 · GOOGL 2026-07-24 · AMZN 2026-09-26 · AAPL 2026-09-26 · TEM 2026-07-04），
**本批跑没跑过的 8 名**：

| 组 | Ticker | 角色 | 这张卡回答什么 |
|---|---|---|---|
| **配对一 · AI 芯片** | **AVGO** | 已兑现的赢家（TTM FCF $39.4B） | 市场为「已交付」付多少 |
| | **INTC** | 转型中（TTM FCF $2.8B，刚增发 $20B） | 市场为「希望」付多少 |
| **配对二 · 给数据中心卖电** | **BE** | 新技术（燃料电池，12 个月 +311%） | 被定价为未来 |
| | **VST** | 老电厂（核电 + 燃气，12 个月 −33%） | 被定价为过去 |
| **配对三 · AI 安全** | **CRWD** | 有机增长（股数 +2%） | 2 月 24 日同日见底后 +173% |
| | **PANW** | 并购平台（股数 +20%，CyberArk 以股换股） | 同日见底后 +155% |
| **配对四 · 表里两个"非 AI"** | **UBER** | 自动驾驶的潜在受害者（−31% 距高） | 佩洛西表中是「余量」 |
| | **AB** | 资管合伙企业（9.7% 分配率） | 佩洛西表中是「余量」 |

四组配对都是同一时间、同一需求来源、市场给出相反定价的自然实验 —— 与 `_pharma_cliff_2026-09-05` 同一设计思路。

## 1. 本批必答的命题

- **T1（主命题）：照抄一位政客的持仓表，能得到什么？** 分三层答：
  ① 生意层（8 张卡各自的 6 模块）；② 价格层（base IRR 是否过 8%）；
  ③ 工具层 —— 她的持仓形式大量是 LEAPS 深度实值看涨期权 = 杠杆，**本库铁律"不借钱、不裸期权"**，
  用户即使认同标的也只能用正股表达；且披露有 26–45 天滞后。
- **T2：单因子检查。** 13 个名字里有几个押的是同一件事（AI 资本开支）？
  用户现持仓 BTC / GOOGL / NBIS 已是同一因子（METHODOLOGY §5），**加任一 AI 名字 = 加倍而非分散**。
- **T3（与价格正交的前置筛，2026-09-01 SaaS 批次提出）：股数方向 + SBC/收入。** 8 家逐一给数。
- **T4（沿用铁律）**：跌/涨幅拆成倍数 vs 基数；点名 owner-earnings 锚；SBC 是真实股东成本，必须扣。

## 2. A0 基准新鲜度门（INC-002）

```
git fetch origin  ->  本地落后 4 个提交（均为 studies/ 财经博主报告，无 companies/ 变动）
git pull --ff-only ->  已同步
ls companies/{avgo,be,intc,crwd,vst,ab,uber,panw}  ->  全部不存在  ->  8 家均为首次建档，无 refresh_of
```

## 3. 数据与脚本（全部可原地重跑）

| 脚本 | 产物 | 源 |
|---|---|---|
| `fetch_data.py` | `data/snapshot_2026-09-28.{json,md}` | Yahoo chart + Nasdaq historical（价格双源）；SEC XBRL companyfacts（TTM） |
| `fetch_filings.py` | 各 dossier `raw/*.txt` | SEC Archives 8-K EX-99.1 / 10-Q / 8-K 原文 |
| `valuation_model.py` | `data/valuation_2026-09-28.{json,md}` | 统一 M6 模型（三情景 10 年 IRR + 门槛价） |
| `make_freshness.py` | 各 dossier `freshness.json` | Yahoo + Nasdaq summary |

SEC 请求使用通用 User-Agent（未使用用户邮箱）。INC-004（行情/SEC 被封）**本批不成立**：所有源均 HTTP 200。

## 4. 估值口径（本批统一，与库内差异须声明）

- **IRR 含中期分配**（股息 + 回购 = p × OE）。理由：本批有两家高分配标的（AB 分配率 ~100%、VST 70%），
  库内 MSFT 公式（不计中期分配）会把 AB 的 13% 算成 3.5%，**对分配型标的是错的**。
- 为可比，每张卡**并列给出库口径 IRR**（MSFT 公式）。
- **门槛价 = base 情景 IRR 恰为 8% 的每股价 = buy_below**（与 `_mega7_refresh_2026-09-26` 一致）；10% / 12% 给加仓 / core 区。
- OE：成熟现金流公司用 **FCF − SBC**（或公司自身"扣维护后"口径并声明）；OE≈0 的转型股用 `ramp`；
  SBC 吃掉 FCF 的高增长软件用 `rev`（收入 × 利润率路径）。三种模式在同一脚本里，公式一致。

## 5. 铁律（沿用）

- 一手优先（SEC 原文 + XBRL）；二手新闻只作背景并标 `secondary`
- **verdict 上限 = 完整度**（<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER / >80 CORE）
- **价格先于完整度封顶**：对价格无安全边际的名字，补完整度不翻盘 → 这 5 家只做 lean 深度；
  **价格友好的名字（AB / UBER / VST）加做一手深度**（10-Q、Form 4、qualified notice）
- **Checker ≠ Runner（PROTOCOL §3）本批未满足**（用户明确不要擅自派生 subagent）→
  所有卡 `clean=false`；**runner 提议为 STARTER 的卡一律以 WATCH 落锁，写明 `runner_proposed_verdict`，
  待独立 Checker 通过后才可生效**（沿用 2026-09-05 "任一卡升 STARTER 前须补独立 Checker"）
- 不跨名排名"距 buy_below 百分比"（各家门槛松紧不同）
- 诚实标签：一轮跑完 = `DECISION_DRAFT`，禁称 COMPLETE

## 6. 进度

| Ticker | Runner | 完整度 | verdict（落锁） | runner 提议 | base IRR | buy_below（8%） | binding_constraint |
|---|---|---:|---|---|---:|---:|---|
| AVGO | ✅ | 60% | WATCH 0% | WATCH | +2.5% | $220.99 | 价格 |
| INTC | ✅ | 55% | WATCH 0% | WATCH | −1.8% | $47.33 | 价格（bull 也不过线） |
| BE | ✅ | 55% | WATCH 0% | WATCH | +2.9% | $178.80 | 价格 |
| VST | ✅ | 62% | WATCH 0% | **STARTER 3%** | **+10.4%** | $164.49 | 独立 Checker + 杠杆/电价体制 |
| CRWD | ✅ | 55% | WATCH 0% | WATCH | −4.5% | $73.76 | 价格（bull 也不过线） |
| PANW | ✅ | 55% | WATCH 0% | WATCH | −1.4% | $150.06 | 价格（bull 也不过线） |
| UBER | ✅ | 65% | WATCH 0% | **STARTER 3%** | **+12.8%** | $101.71 | 独立 Checker + AV 去中介化 |
| AB | ✅ | 62% | WATCH 0% | **STARTER 3%** | **+13.1%** | $49.72 | 独立 Checker + 持有载体（PTP 税务） |

批次结论见 [synthesis.md](synthesis.md)，验收见 [CHECKER.md](CHECKER.md)。
