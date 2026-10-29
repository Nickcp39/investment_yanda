# Mega7 Refresh 2026-10-29 — 验收 (CHECKER)

规则：每项必须可机器或人工复核。"感觉完成"不算。四张重跑卡由四个并行 runner 完成，本表是协调者的复核。

## P1 价格与新鲜度

| # | 检查项 | 标准 | 状态 |
|---|---|---|---|
| 1.1 | 价格双源 | 每名 ≥2 个独立源，差 <1% | ✔ Yahoo v8 chart + stockanalysis history，**7/7 差 0.00%**（10-28 收盘） |
| 1.2 | 价格日期 ≤ as_of | 2026-10-28；10-29 未收盘，排除 | ✔ |
| 1.3 | 股数口径 | 10-Q 封面在外流通股 | ✔ MSFT 7,426,194,552；GOOGL 12,294M（A+B+C）；META 2,556,241,253（A+B）；TSLA 3,952,757,946 |
| 1.4 | **`verify_freshness.py`** | exit 0 | ✔ **4/4 PASS，0 warning**（09-26 批次未跑，本批补上） |

## P2 财务一手性

| # | 检查项 | 状态 |
|---|---|---|
| 2.1 | 新季度数字来自 SEC 原文 | ✔ 4/4；MSFT 8-K + 10-Q + 424B2，GOOGL 8-K + 10-Q（10-29），META 8-K + EX-10.1 + 10-Q，TSLA 8-K ×3 + 10-Q + DEF 14A |
| 2.2 | 原文纯文本入库 | ✔ 各卡 `raw/`；MSFT 引用 `_earnings_msft_googl_2026-10-28/raw/` |
| 2.3 | 一次性项目识别并剔除 | ✔ 见 synthesis §3（GOOGL 股权重估、META 和解 $9.89B 与 CAMT $8.03B、TSLA SpaceX/加密/税、MSFT OpenAI 损益） |
| 2.4 | capex 合计口径 | ✔ MSFT（承重）、GOOGL（防御读）、META（含融资租赁本金）；TSLA 无重大租赁，沿用现金口径 |
| 2.5 | 电话会内容标为二手 | ✔ GOOGL capex 指引、META 部分指引标注；TSLA 只用 SEC 文件 |

## P3 估值一致性

| # | 检查项 | 状态 |
|---|---|---|
| 3.1 | 先用旧参数复现旧卡 | ✔ MSFT $440.7（旧 $441）；GOOGL $117 逐位一致；META $492 一致；TSLA $143.82 / $97.88（旧 $144 / $98） |
| 3.2 | 方法变更逐步拆解 | ✔ 四张卡都有"只换数据 → 每一处口径变更"的阶梯表 |
| 3.3 | 承重假设变更明示旧 → 新与理由 | ✔ MSFT 合计口径；GOOGL 合计口径 + SBC 全口径；META 股数恒定 → 年增 1.4%；TSLA OE 锚剔除后 $2.61B |
| 3.4 | 不跨名排名距买入线 | ✔ synthesis §0 注 |
| 3.5 | 不可计量时明确标注 | ✔ GOOGL 现金镜头、META 前瞻保守镜头 |

## P4 裁决完整性

| # | 检查项 | 状态 |
|---|---|---|
| 4.1 | 每名 refresh_note + valuation + decision_card.md + .json | ✔ 4/4 |
| 4.2 | supersedes 指向旧卡 | ✔ 4/4（GOOGL 指向 08-28） |
| 4.3 | kill criteria 逐条红/黄/绿 | ✔ 4/4；新增 MSFT K-G、META K-6/K-7、TSLA 三条 |
| 4.4 | verdict 翻转写明原因 | ✔ 无翻转，四张都写明 buy_below 变动的原因是量法还是生意 |

## P5 协调者对原文的抽查（runner 结论，不照单全收）

| 名字 | 抽查的说法 | 原文位置 | 结果 |
|---|---|---|---|
| MSFT | 尚未起租租约 $364.6B，起租到 FY2034 | 10-Q 租赁附注 | ✔ 原文一致 |
| MSFT | 服务器零部件代采应收 $35.7B（季初 $27.8B），供应商协议受限投资 $12.6B | 10-Q 附注 | ✔ 原文一致 |
| MSFT | 424B2 为初步说明书，金额空白 | 424B2 | ✔（runner 已存 raw） |
| TSLA | 董事会特别委员会探讨与 SpaceX 的交易，含业务合并 | 10-Q Part II Item 5 | ✔ 原文一致（runner 的 raw 文本里有，协调者另从 SEC 重抓核对） |
| TSLA | 4.237 亿股 2025 奖励是已发行限制股，未赚取部分按比例投票，到期退回 | 10-Q 股权激励附注 | ✔ 原文一致 → 09-26 synthesis §4 的 43.7 亿股说法作废 |
| META | 新设无投票权 C 类股，1:1 股息；Founder Alignment Agreement | 8-K Item 1.01 + EX-10.1 | ✔ 原文一致 |
| META | "We expect to use shares of the Class C common stock to conduct equity offerings" | 10-Q | ✔ 原文一致 |
| META | Q3 法律计提 $9.9B | EX-99.1 | ✔ 原文一致 |
| GOOGL | Crux AI（关联方合营）占积压 $16.8B | 10-Q | ✔ 原文一致 |
| GOOGL | 6.125% 票据 2126 年到期 | 10-Q 封面证券表 | ✔ 原文一致 |
| GOOGL | 桥 SBC 重复扣除 | `googl/2026-06-19/model/capex_owner_earnings_bridge_v2.csv` | ✔ 公式确为 NOPAT（取自营业利润）+ 折旧 − SBC − 维护 capex |

## P6 已知未闭合项

| 名字 | 未闭合 |
|---|---|
| MSFT | 424B2 规模与票息；零部件垫款最终是收回还是变资产（O5）；维护/成长 capex 拆分（O2） |
| GOOGL | SBC 重复扣除待用户拍板；Wiz 对 Cloud 增速的贡献；SpaceX 对账差 $14.1B；capex 指引只有电话会二手 |
| META | 2027 capex 数字；C 类股增发规模；Q3 电话会转录（404） |
| TSLA | robotaxi 车队与收入、FSD 独立收入、Optimus 销售、2026 交付目标；SpaceX 交易条款 |
| AMZN | **本批尚未重跑**，等 10-29 盘后 8-K |

## P7 未重跑的两家（理由）

| 名字 | 卡日期 | 理由 | 价格核对（10-28） |
|---|---|---|---|
| AAPL | 2026-09-26 | 9 月以来无新季报；FY26 Q4 定于 11-02 | 343.83 vs buy_below 241，+43%；原模型 base 5y +0.6% |
| NVDA | 2026-10-19 | 10 天前刚重跑；无新 SEC 文件；Q3 FY27 约 11-18 | 215.38，在 148.30–222.44 带内；base 5y +8.7%、现金口径 +0.2%；STEP 1 证据条件未到 |
