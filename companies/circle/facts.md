# CRCL — Circle Internet Group, Facts (累积事实库)

按 [frameworks/info_collection_pipeline.md](../../frameworks/info_collection_pipeline.md)
的 3×3+3 框架收集。每条事实 inline 标 source tier (`[A1]` 一手 / `[B2]` 高质二手 /
`[C3]` 市场评论 / `[D4]` 社交媒体)。

**Snapshot**

- Company: Circle Internet Group, Inc. _[to verify legal entity name from S-1]_
- Ticker: CRCL _[to verify]_
- Exchange: NYSE _[to verify]_
- 上市日期 / IPO date: 2025 年 6 月 _[to verify exact date]_
- Sector / 子行业: Crypto / Stablecoin issuer (USDC)
- Last updated: 2026-05-05 (dry-run plan only — no real fetch yet)
- Look-back 范围: **since IPO 2025-06**, < 1 年。**触发"年轻公司例外路径"**：
  S-1 历史 exhibits 补 pre-IPO 3 年财务；母 / 创始人公开声明从 2013 年起作背景但不可直接外推。

⚠ 本文档为 **dry-run 模拟产出**——验证 framework 落地结构，**未实际 fetch**。
所有 EVIDENCE 区为空。每条 L1/L2 checklist 后附 "FETCH PLAN" 注释，说明
"该从哪拿、关键词、时间估算"。

---

## L1 完成度自查 (含 FETCH PLAN)

- [ ] **10 年 10-K 数字时间序列**
  - **FETCH PLAN**: 公司 < 1 年公开史，无 10 年 10-K。降级到：
    - S-1 / S-1/A (2025 春提交) 含 3 年 audited financials (FY2022-2024)
    - 10-K FY2025 (应已 2026 年 Q1 提交)
    - 拉数字: revenue / GM / OM / FCF / ROIC / 股本 / debt / capex / 回购 / 股息
    - URL: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<Circle CIK>&type=10-K`
    - **预计**: 30-45 min (含 S-1 + 10-K 通读 + 时间序列 manual extract)
  - **缺口**: 实际只有 4 年完整年度 + 部分 quarter；不够"完整周期 10 年"，灵魂 confidence 降 1 档

- [ ] **管理层叙事 3 个采样点 (latest / 5y ago / 10y ago)**
  - **FETCH PLAN**: 5y ago = 2021 年 (公司未上市)；10y ago = 2016 年 (远早于 IPO)。
    无传统 annual letter。**替代采样**:
    - latest: 10-K FY2025 "Letter from CEO" (若有) + 最近 earnings call CEO 开场
    - 5y proxy: Jeremy Allaire 2021 年 SPAC 拟上市时的投资者材料 + 公开访谈 (Concordia AM 2021 / Coindesk 长访)
    - 10y proxy: Allaire 2016 年的公开声明 + Circle 早期 funding round 公告 (TechCrunch / VentureBeat)
  - **预计**: 60 min (历史素材分散，比正常公司难)
  - **降级标注**: 2021/2016 采样为 secondary 来源 (不是公司一手 letter)，标 [B2]

- [ ] **最近 4 季 call transcripts verbatim**
  - **FETCH PLAN**: IPO 2025-06，到 2026-05-05 应有 3-4 次电话会
    - Q2 2025 (IPO 后首份): 2025-08 左右
    - Q3 2025: 2025-11 左右
    - Q4 / FY2025: 2026-02 左右
    - Q1 2026: 2026-05 左右 (可能刚发布或下周)
  - 来源: 公司 IR 站点 / Seeking Alpha (登录) / Tikr / Motley Fool transcript section
  - **预计**: 60 min (3-4 份 × ~15 min)

- [ ] **历史每年 1 季 call transcript 抽样**
  - **FETCH PLAN**: 公司 < 1 年，无历史抽样可做。**该项 N/A，标"年轻公司豁免"**

- [ ] **最近 1 份 10-Q**
  - **FETCH PLAN**: Q1 2026 10-Q (若已发) 或 Q4 2025 (作为最新)。EDGAR 直接拉。
  - **预计**: 15 min

- [ ] **最近 12 个月 8-K**
  - **FETCH PLAN**: EDGAR Circle 8-K 列表。重点：IPO 后管理层变动 / M&A / 监管事件 / 重大合同。
  - 预计件数: 10-20 份 (post-IPO 公司常见频率)
  - **预计**: 30 min (扫 + 标记重要的)

- [ ] **最近 1-2 份 proxy (DEF 14A)**
  - **FETCH PLAN**: 2026 年首份年度 proxy 应已提交 (annual meeting 通常 IPO 后 9-12 月)
    - 高管薪酬结构、董事会独立性、股权激励 plan、关联交易披露
    - URL: EDGAR DEF 14A 类型筛选
  - **预计**: 30 min

- [ ] **资本结构当前快照**
  - **FETCH PLAN**: 最新 10-Q 资产负债表 + 后续 8-K 任何融资 / 回购公告
    - 关键: 现金 / debt / 优先股 / 股本结构 (是否双层股权 / Allaire 控制权)
  - **预计**: 10 min

- [ ] **大股东 top 5 + 内部人持仓 %**
  - **FETCH PLAN**: 
    - 大股东: 13G filings (BlackRock / Vanguard / 早期 VC 转持) + WhaleWisdom / Dataroma
    - 内部人: proxy 披露 + Form 4 history
    - 预 IPO 关键持有: Goldman Sachs / GV / Accel / Breyer / IDG / FCMV / Fidelity (依稀记忆，要 verify)
  - **预计**: 20 min

- [ ] **审计师 + 重述历史**
  - **FETCH PLAN**: 
    - 审计师: 10-K 审计意见页 (大概率 Big 4 — 推测 Deloitte 因 USDC reserve attestation 是他们做)
    - 重述: < 1 年公开，重述概率低；但 S-1 vs 后续 10-K/Q 数字不一致点要标记
    - SEC 调查: 检查 SEC enforcement actions 数据库 + 公司过往与 SEC 的"USDC 是不是证券" 历史争议
  - **预计**: 20 min
  - **重要**: Circle 与 SEC 历史上有过 USDC 证券属性争议，proxy / 10-K 风险因素段必读

- [ ] **关键事件年表 (10 年)**
  - **FETCH PLAN**: 多源拼合：
    - 2013 创立 (Allaire / Neville)
    - ~2018 USDC 上线 (与 Coinbase 合资 Centre Consortium)
    - 2022 SPAC 拟上市失败 (Concord Acquisition Corp)
    - 2023-03 USDC 短暂 depeg (硅谷银行 SVB 倒闭，$3.3B reserve 在 SVB)
    - 2023 Centre Consortium 解散，Circle 全面收购 USDC 控制
    - 2025-06 IPO
    - 其他: GENIUS Act 2025 通过 (若已)、MiCA 2024-12 生效、Hong Kong 稳定币条例
  - **预计**: 30 min (公司官网 history page + Wikipedia 校对 + 重要 8-K)

**L1 总预计**: 30+60+60+0+15+30+30+10+20+20+30 = **305 min ≈ 5 h**

⚠ **超过 framework 估算的 2.5-4.5 h 上限**——年轻公司因为缺 10 年历史，反而要花更多时间
拼凑 pre-IPO + S-1 历史，**不是更省时**。

---

## L2 完成度自查 (含 FETCH PLAN)

- [ ] **Sell-side 一致预期**
  - **FETCH PLAN**: Yahoo Finance CRCL "Analysts" tab → consensus EPS / revenue / 目标价分布 + 评级分布
  - 推测: < 1 年标的，覆盖度可能稀疏 (5-8 家覆盖)
  - **预计**: 5 min

- [ ] **13F 流向最近 4 季扫描**
  - **FETCH PLAN**: WhaleWisdom CRCL / Dataroma — 季度 holder 变化
    - 关注: pre-IPO VC 减持节奏、机构买方 (Tiger / Coatue 等 crypto-friendly 基金) 进入节奏
  - **预计**: 15 min

- [ ] **近期 8-K + Form 4**
  - 与 L1 部分重叠，**重点**: Form 4 内部人 IPO 后大额抛售 / 内部人买入信号
  - **预计**: 10 min (在 L1 8-K 扫描时一并)

- [ ] **1-3 家直接竞品最近一次财报口径**
  - **FETCH PLAN**: 3 家:
    - **Coinbase (COIN)** — 每季 call 提 USDC 收入分成 + 持仓量
    - **PayPal (PYPL)** — 每季 call 提 PYUSD 流通量
    - **Tether (USDT)** — 私人公司，月度 attestation + 行业数据
  - 来源: 各家 IR transcript + Tether 月度报告
  - **预计**: 30 min

- [ ] **3-5 篇高质量专业报道 (过去 6 个月)**
  - **FETCH PLAN**: 关键词 "Circle CRCL" + 过去 6 个月 site:bloomberg.com OR reuters.com OR ft.com OR wsj.com OR theblock.co
  - 重点叙事: GENIUS Act 通过对 Circle 的影响、Tether 竞争、Reserve yield 下行
  - **预计**: 30 min (找 + 略读)

- [ ] **行业专属 dashboard (加密)**
  - **FETCH PLAN**: 
    - DeFi Llama: USDC 总流通 + 链分布历史
    - Dune Analytics: 公开 dashboards "USDC supply", "stablecoin market share"
    - CoinGecko / CoinMarketCap: USDC vs USDT 市值历史曲线
    - 链上 holder 集中度 (前 100 / 前 1000 占比)
  - **预计**: 20 min

- [ ] **监管 / 立法时间表**
  - **FETCH PLAN**:
    - **GENIUS Act** (US) — 2025 是否通过、final text 关键条款 (利息分成 / reserve 要求)
    - **MiCA** (EU) — 2024-12 生效，Circle Europe SA (法国持牌) 状态
    - **HK / SG / 日本** — 各自稳定币监管落地时间
    - **SEC enforcement** — Coinbase / Kraken 案件中是否涉及 USDC 论点
  - **预计**: 30 min

**L2 总预计**: 5+15+10+30+30+20+30 = **140 min ≈ 2.3 h**

**L1 + L2 合计**: 5 + 2.3 = **7.3 h**

⚠ 比 framework 估算的 2.5-4.5 h 上限多 50-100%。年轻公司 + 加密行业 + 监管复杂
是 3 个加成因子。

---

## EVIDENCE (事实区)

(空。本次为 dry-run，未实际 fetch。下次真跑时按 [companies/_facts_template.md](../_facts_template.md) 结构填入。)

### 业务模式 / 收入结构
*(待 fetch)*

### 财务时间序列
*(待 fetch)*

### 资本结构
*(待 fetch)*

### 管理层 / capital allocation 历史
*(待 fetch)*

### 大股东 + 内部人持仓
*(待 fetch)*

### 关键事件年表
*(待 fetch)*

### 行业 / 市场结构 / 竞争格局
*(待 fetch)*

### 监管 / 立法
*(待 fetch)*

### 行业专属 dashboard 数据 (链上)
*(待 fetch)*

---

## INTERPRETATION (解读区)

(空。本次未做。)

---

## SENTIMENT (情绪区)

(空。本次未做。)

---

## OPEN QUESTIONS (信息缺口 / L3 触发候选)

dry-run 阶段就能预判的几个 likely L3 触发：

- [ ] **管理层 capital allocation 历史不足 10 年** → L3: 拉 Allaire 公开访谈 (Concordia / Coindesk State of Crypto 等) 找战略表态连续性
- [ ] **未经历完整衰退周期** → L3: 用 SVB depeg (2023-03) 作为压力测试 proxy (虽不是 macro 衰退)
- [ ] **激励结构 (是否含期权 reload / 高估值 IPO 触发的 cliff)** → L3: proxy 详读 + Allaire / Neville 持股 lock-up 到期表
- [ ] **客户口碑 / 切换成本量化缺失** → L3: scuttlebutt 5 类 — 重点 CEX (Coinbase / Binance / Kraken) + DeFi (Aave / Uniswap / Curve) 的 USDC 替代成本访谈/资料
- [ ] **GENIUS Act 利息分成条款是否摧毁 reserve revenue 模式** → L3: 立法原文详读 + 行业 lobbying 影响估测
- [ ] **Tether 竞争动态 (USDT 4× USDC 流通规模) 是否结构性** → L3: 历史 6 年 USDT/USDC 比例曲线 + 各家在 emerging markets vs 美国合规市场的份额

---

## KILL CRITERIA

(待 Step 4 主审环节填。)

---

## FRAMEWORK FEEDBACK (本次 dry-run 发现的 framework 缺陷)

**1. 年轻公司处理路径不够细**
- 当前 framework 写"地板规则: since IPO"，但实际 < 1 年的公司很多 L1 项 N/A 或要 substitute
- 建议增补到 framework: "**年轻公司补丁清单**":
  - call transcripts 历史抽样 → N/A
  - 管理层叙事 5y/10y 采样 → 替换为创始人公开访谈 (降级 [B2] 标注)
  - 资本配置 10 年 → 替换为 funding round 历史 + 早期产品决策

**2. 加密 / 高度监管行业的 L1 缺一项**
- L1 现在有"审计师 + 重述历史"，但**漏了"与监管机构的历史互动"**
- Circle / 加密公司这个特别重要 (Coinbase 案、Binance 案、SEC 对 USDC 的态度史)
- 建议 L1 加: **监管历史 / 执法行动 / 公司针对监管的公开立场演变**
- 普通公司这条可能 N/A，但加密 / 银行 / 制药 / 国防 行业必查

**3. 时间估算过于乐观**
- framework 说 L1+L2 = 2.5-4.5 h
- 本次 Circle dry-run 算下来 = 7.3 h
- 加成因子: 公司年轻 (拼历史)、行业加密 (额外链上 + 监管)、本身复杂 (USDC + Centre 历史)
- 建议 framework 加**复杂度系数**:
  - 普通公司: 1.0× → 2.5-4.5 h
  - 年轻 (< 5 年公开): +30%
  - 加密 / 高度监管 / 跨境: +50%
  - 双因子叠加 ~ 7-8 h，与本次实测吻合

**4. EDGAR fetch 自动化优先级被验证**
- 手工拉 SEC filings (S-1 + 10-K + 多份 10-Q + 多份 8-K + proxy) 工作量很大
- info_collection_pipeline.md 工具路线图里 SEC EDGAR fetcher 排第 1，**dry-run 确认这个优先级正确**
- 写脚本投资时间 vs 节省: 单家公司省 30 min；3 家公司就 break-even

**5. INTERPRETATION 区里我们仓库播客 grep 没强调要做**
- L2 没单独列"grep notes/videos/ 看本仓库已有素材"
- 这是免费 + 高价值的步骤，建议 L2 显式加一项: **本仓库已有 transcripts / notes 扫描** (5 min)

**6. 行业 dashboard 表里"加密"行只列 3 个工具，但没说优先级**
- 实操中 DeFi Llama (免费) > Dune (公开 dashboard 免费) > Nansen (付费)
- 建议每行 dashboard 标注 (free/freemium/paid)
