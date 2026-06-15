# Research OS Flowchart

创建: 2026-06-15

这张图是小型买方研究部的完整流程。它不是一次性完美流程，而是可迭代的工作系统。

```mermaid
flowchart TD
  A["Idea Intake<br/>ticker / theme / rumor"] --> B["Research Queue<br/>stage + priority + decision question"]
  B --> C{"Triage<br/>5-8 high-quality sources"}
  C -->|not worth time| R["Reject / Park<br/>记录为什么不做"]
  C -->|worth studying| D["Research Status + Plan<br/>scope / batches / stop conditions"]

  D --> E["Collect Raw Evidence<br/>filings / transcripts / news / expert / local notes"]
  E --> F["Claim Ledger<br/>source_id / claim / value / date / tier"]
  F --> G["Facts.md<br/>Evidence / Interpretation / Sentiment"]

  G --> H1["Moat Technical Analysis<br/>mechanism / evidence / attack surface"]
  G --> H2["Operator Underwriting<br/>founder / CEO / board / incentives / culture"]
  G --> H3["Munger Inversion<br/>how would this fail?"]
  G --> H4["Valuation<br/>owner earnings / 10y IRR / margin of safety"]
  G --> H5["Bottleneck Module<br/>supply chain / scarce layer / capacity"]

  H1 --> I["Audit / Quality Gates"]
  H2 --> I
  H3 --> I
  H4 --> I
  H5 --> I

  I --> J{"Investment Committee<br/>Buffett / Munger / Duan / Marks / Klarman"}
  J -->|evidence weak| K1["INFO-GAP<br/>补资料"]
  J -->|bad business or bad price| K2["REJECT"]
  J -->|interesting, not enough MOS| K3["WATCH"]
  J -->|small research position possible| K4["STARTER"]
  J -->|rare, high conviction| K5["CORE"]

  K1 --> D
  K2 --> L["Archive<br/>keep changed-mind trigger"]
  K3 --> M["Monitor Plan<br/>price / earnings / regulation / technology"]
  K4 --> M
  K5 --> M
  M --> N["Memory Update<br/>long / medium / short-term thesis"]
  N --> B
```

---

## Institutional Mapping

```mermaid
flowchart LR
  S["Sell-side banks / brokers<br/>coverage, models, ratings, industry reports"] --> OS["Our Research OS"]
  B["Buy-side funds<br/>internal memo, IC, position sizing, risk"] --> OS
  D["Data platforms<br/>filings, transcripts, broker research, expert calls"] --> OS
  P["PE / consulting diligence<br/>customers, suppliers, operators, unit economics"] --> OS
  C["FICC / commodities / futures<br/>supply-demand, inventory, curves, capacity"] --> OS

  OS --> O1["Facts + Claim Ledger"]
  OS --> O2["Moat / Operator / Inversion"]
  OS --> O3["Valuation + Margin of Safety"]
  OS --> O4["IC Verdict + Monitoring"]
```

---

## Why This Flow Exists

| Flow step | Institutional analogue | Why it exists |
|---|---|---|
| Research queue | Buy-side idea funnel | 注意力和时间是稀缺资源，不是每个故事都值得深研 |
| Triage | Desk analyst quick screen | 快速排除明显没有证据、明显不懂、明显太贵的 idea |
| Raw evidence | Sell-side / buy-side source gathering | 防止先有结论后找证据 |
| Claim ledger | Data platform / compliance discipline | 每个数字和判断可追溯 |
| Facts split | Research report content control | 事实、解读、情绪不能混 |
| Moat analysis | Fundamental equity research | 判断十年后利润池还在不在 |
| Operator underwriting | PE/buy-side diligence | 资本交给谁配置很重要 |
| Inversion | Risk committee / behavioral process | 主动找会让自己错的路径 |
| Valuation | Equity research / PM decision | 好公司不等于好价格 |
| IC verdict | Buy-side investment committee | 把研究变成行动或不行动 |
| Monitor/memory | Portfolio management | 研究不是一次性报告，要跟踪和复盘 |

