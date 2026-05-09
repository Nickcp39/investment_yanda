# Raw Block: &lt;Ticker&gt; Block&lt;N&gt; — &lt;Block Name&gt;

按 [frameworks/info_collection_pipeline.md](../frameworks/info_collection_pipeline.md)
执行阶段 Stage 2 产出。每个 block 一份。Stage 3 综合时从这里抽事实进 facts.md。

## Status

- Block: __
- Plan ref: [step0_plan.md](step0_plan.md)#block-__
- Started: YYYY-MM-DD
- Completed: YYYY-MM-DD (or 🟡 / ❌ / ⏭)
- Tier 总评: A1 / B2 / C3 / D4 (本 block 主要来源 tier)

## Calls made

按时间顺序记录所有调用。失败的也记。

1. WebSearch "..." → 简述返回内容 (3-5 行) + 关键 URL
2. WebFetch &lt;URL&gt; with prompt "..." → 简述返回 (3-5 行)
3. ...

## Verbatim / close-paraphrase 输出

来自调用的具体内容。**优先 verbatim 引用** (尤其是 SEC filings / 财报数字 / 监管原文)。
长段可截断，但保留事实数字 / 时间 / 主体的精确表述。

按主题或时间分小节。

### &lt;主题/段名&gt;

> _verbatim 段_

来源: &lt;URL or path&gt;
日期: YYYY-MM-DD
Tier: A1/B2/C3/D4

### &lt;主题/段名&gt;

...

## 提取 claim (供 Stage 3 综合)

每条 claim 一行。inline 标 tier。这是 Stage 3 综合时直接搬进 facts.md 的素材。

- [A1] _claim_
      Source:
      Date retrieved:
      Path:
      Reliability note:
      Goes to facts.md section: EVIDENCE / 业务模式 (例)

- [B2] _claim_
      Source:
      ...
      Goes to facts.md section: INTERPRETATION (例)

- [D4] _vibe_
      ...
      Goes to facts.md section: SENTIMENT (例)

## Open questions / next-block dependencies

本 block 没回答 / 部分回答的，可能影响后续 block:

- [ ] _问题_
  - 候选解决: 后续 block N / L3 触发 / 接受缺口

## Raw block 自查

- [ ] block 的 target 全部回答 (或标 ❌/⏭)
- [ ] verbatim/close 段填了
- [ ] claim 提取段填了
- [ ] open questions 段填了
- [ ] step0_plan.md 中本 block status 已回写
