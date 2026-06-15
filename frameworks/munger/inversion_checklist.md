# Munger Inversion Checklist

创建: 2026-06-15

用途: 在任何公司 memo 完成前，先问反问题: 如果我要让这家公司失败，我会攻击哪里？这不是悲观，而是防止 thesis 只会自我证明。

---

## 1. Core Prompt

假设我是一个资源充足、耐心很长、没有历史包袱的竞争者/监管者/技术替代者/内部破坏者。我要让这家公司十年内失去超额利润，我会怎么做？

输出必须具体到机制，不能只写“竞争加剧”。

---

## 2. Failure Map

| Failure path | Attacker | Mechanism | Time horizon | Evidence today | Early warning |
|---|---|---|---|---|---|

至少覆盖:

- 客户离开
- 定价权丧失
- 技术替代
- 分销入口被绕过
- 监管/诉讼
- 资本配置错误
- 文化/人才恶化
- 财务杠杆或稀释
- 估值过高导致长期回报差

---

## 3. “How Would I Kill It?” Questions

### Customer

- 我能否让客户用更低成本完成同一任务？
- 我能否降低 switching cost？
- 我能否从一个边缘使用场景切入，再扩展到核心？
- 客户最讨厌这家公司什么？这个痛点是否足够大？

### Product / Technology

- 新技术是否把旧产品变成 feature，而不是 platform？
- 开源、标准化、AI 自动化是否降低护城河？
- 技术路线是否换轨，导致旧资产折旧加速？
- 公司是否为了保护旧利润而慢于新技术？

### Distribution

- 我能否绕过它的默认入口？
- 我能否控制新入口，比如 agent、OS、浏览器、社交、企业 workflow？
- 监管是否会迫使它开放入口或取消默认协议？

### Economics

- 我能否迫使它提高 capex 才能维持旧利润？
- 我能否发起价格战，打掉超额利润？
- 它的高毛利是否来自客户懒惰，而不是不可替代？
- 规模变大后，incremental ROIC 是否下降？

### Organization

- 关键人才是否在离开？
- 激励是否鼓励 empire building 而不是 owner earnings？
- 创始人控制权是长期主义，还是缺乏外部约束？
- 职业经理人是否在优化短期共识而非长期产品？

### Regulation

- 是否存在一个政治上容易攻击的利润池？
- 是否有默认、捆绑、数据、隐私、内容、劳动、税务风险？
- 如果被拆分、限制分销、限制数据使用，核心利润会怎样？

---

## 4. Google Failure Paths

Google 的 inversion 不能只写“AI 威胁搜索”。至少拆成:

| Failure path | Mechanism |
|---|---|
| AI answer interface 替代搜索页 | 用户不再点击传统搜索结果，广告库存和点击归因下降 |
| 默认搜索分销被监管削弱 | iOS/Chrome/Android 默认入口价值下降，TAC 或流量结构恶化 |
| 高意图广告迁移 | Amazon、TikTok、AI commerce、垂直搜索分走商业查询 |
| AI capex 军备竞赛 | 收入增长但 depreciation/capex 吃掉 owner earnings |
| Cloud 竞争压价 | AWS/Azure/开源模型/自建芯片压低 GCP 回报率 |
| 组织迟缓 | 大公司流程和风险厌恶让产品迭代慢于 OpenAI/Anthropic/Meta/xAI 等 |
| 监管拆分或限制数据 | 广告、Android、Chrome、Play、隐私数据被限制 |
| 文化流失 | 最强 AI/产品人才流向更激进的团队 |

---

## 5. Verdict Discipline

如果 inversion 找到的失败路径:

- 已经有强证据发生，且没有对冲: `REJECT` 或 `WATCH`。
- 只是可能发生，但有明确监控指标: 可以继续研究。
- 影响巨大但证据不足: 必须进入 `KILL CRITERIA`。

