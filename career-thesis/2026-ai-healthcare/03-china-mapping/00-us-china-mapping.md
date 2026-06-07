---
title: US ↔ China 公司对应关系总图
generated: 2026-05-16
us_companies: 70 (companies.csv)
china_companies: 25 (china_companies.csv)
status: Phase 3 v1
---

# Phase 3: US ↔ China 公司对应映射

## 整体结构

- **US 端**: 70 家公司 in `data/companies.csv`（7 段全覆盖 + 4 死亡 cautionary tales）
- **China 端**: 25 家公司 in `data/china_companies.csv`（覆盖 7 段 + 中国独有的 LLM 大厂医疗 vertical）
- **互引用**: US row 的 `china_counterpart` ↔ China row 的 `us_counterpart`
- **Phase 3 重点发现:** 不是每个段都有 1:1 中国对应——S2 段中国是大厂 vertical (无 startup)、S6 段中国是 legacy HIS 厂 (非 AI-native)、S1 段中国市场太小 (只有云知声)

## 段级对应表

### S5 Medical Imaging AI（最对应 + Nick 主线）

| US | 中国对应 | 出海状态 | Nick entry path |
|----|----------|---------|----------------|
| HeartFlow ($1.54B IPO) | **数坤科技** (preparing HK IPO) | planning | 数坤 北京 R&D |
| Aidoc ($238M raised) | **联影智能** (急诊 AI) / **推想医疗** (肺) | planning | ⭐ **联影智能 = 主线 A** |
| Viz.ai (1,700 hosp deployed) | 联影智能 (卒中) | planning | 同上 |
| PathAI / Paige | **透彻影像** (病理) | none | 透彻早期 |
| Cleerly | 数坤 | planning | 数坤 |
| Lunit (Korea KOSDAQ) | 联影智能 (乳腺) | planning | 联影智能 |
| Annalise.ai (Australia) | 深睿医疗 / 联影智能 | planning | 联影智能 |
| Rad AI (NLP) | (中国 RIS NLP 落后，无直接对应) | — | — |
| Subtle Medical (中美双总部!) | 联影集团 MR | active | ⭐ Subtle 已是中美双总部 |
| Neko Health (whole-body) | (中国无直接对应) | — | — |

**S5 段 Nick 核心洞察:**
- **联影智能 = 主线 A**：profile match + 上海 HQ + 16 NMPA 三类证（行业第一）+ Series A 2025-06 $100亿估值刚拿到
- **数坤科技 = 主线 A2**：preparing HK IPO 2025-2026，HeartFlow 直接对标
- 中国 S5 头部公司 (联影智能/数坤/推想/深睿) 国内已站住，**出海正在起步** — Nick entry timing 正好

### S3 Precision Medicine（Nick 主线 B）

| US | 中国对应 | 出海状态 | Nick entry path |
|----|----------|---------|----------------|
| Tempus AI ($12.8B / $1.3B 营收) | **燃石医学** + **MGI 华大智造** | mixed | ⭐ MGI = 主线 B |
| Guardant Health ($982M 营收) | **燃石医学** (液体活检) | planning | 燃石 (但红旗 3/6) |
| Foundation Medicine (Roche 收购) | **燃石医学 OncoScreen** | none | — |
| Caris Life Sciences ($412M) | **世和基因** | none | 世和 IPO 失败 |
| GRAIL Galleri ($120M, 67x mult!) | **诺辉健康** (Cologuard 中国版) | none | 诺辉 HK 停牌 — 红旗 5/6 |
| Natera ($1.7B) | **贝瑞和康** (产前) | none | 贝瑞 A 股 |
| Exact Sciences | 诺辉 + 凯莱英 | none | — |
| Freenome | 鹍远基因 | none | — |
| (Illumina) | **MGI 华大智造** | active | ⭐ **MGI 是 Illumina 直接竞争对手 + 出海最强** |

**S3 段 Nick 核心洞察:**
- **MGI 华大智造 = 主线 B**：A 股上市 + 76 国覆盖 + 海外营收 33%。但 2025 H1 海外营收 YoY -9%（中美脱钩压力）。"国际业务部门"持续 hiring，对你 profile 估值高
- 中国 NGS 公司（燃石/世和/诺辉）几乎全部经历"美股 IPO → 退市 / HK IPO → 财务质疑"，红旗密集，**除 MGI 外其他段内公司风险高**

### S4 Drug Discovery AI（Insilico = Nick 出海范本）

| US | 中国对应 | 关键说明 |
|----|----------|---------|
| Isomorphic Labs (Alphabet) | **晶泰科技** (XtalPi HK 2228.HK) | XtalPi 2024-06 IPO，HK Ch 18A 路径 |
| Recursion (RXRX, $74.7M 营收, -$644M 亏损) | (无中国对应规模玩家) | — |
| Xaira ($1B Series A) | 晶泰科技 (规模差距大) | — |
| Insilico Medicine | **= Insilico 自身（HK IPO 2025-12）** | ⭐ **中港双总部 + Phase 2 阳性 = Nick 出海唯一已实证范本** |
| Genesis Therapeutics | 晶泰 | — |

**S4 段 Nick 核心洞察:**
- Insilico **不是中国 vs 美国对立**，它本身就是 multi-shore 跨国架构 (SH + Suzhou + Boston + AbuDhabi + Montreal)
- 晶泰科技和 Insilico 是中国 AI biotech 双旗舰，都通过 HK 路径 IPO
- biology reskill 成本高，Nick 不入主线但 **必须 follow 这两家 case study** for elevator map 设计

### S2 Clinical Decision Support / Medical LLM（中国 = 大厂 vertical，无 startup 对应）

| US | 中国对应 | 关键说明 |
|----|----------|---------|
| OpenEvidence ($12B / $150M ARR 19x YoY!) | **字节小荷AI医生 / 豆包医疗** + **蚂蚁阿福** + **百度文心健康管家** | 中国是 LLM 大厂 vertical，不是独立 startup |
| Hippocratic AI ($3.5B, agentic) | **京东健康康康 / 京医千询** + 蚂蚁医疗大模型 | 同 |
| Glass Health | (无对应) | 中国大厂通用聊天助手集成医学，不是独立产品 |
| Atropos Health | (无对应) | 中国 RWE 工具市场弱 |
| Hippocratic (patient-facing) | 平安好医生 + LLM | — |

**S2 段 Nick 核心洞察:**
- 这是 **PM path** 段（不是 engineer path）：详见 `04-synthesis/pm-pathways.md`
- Plan B (PM): 字节豆包医疗 / 阿里通义医疗
- Plan C (PM): 腾讯觅影
- engineer path 在中国 = leetcode 关卡

### S1 Clinical Documentation（中国市场太小）

| US | 中国对应 | 关键说明 |
|----|----------|---------|
| Abridge ($5.3B) | **云知声** (山海大模型) | 云知声更广泛做语音 AI，医疗只是一部分 |
| Nuance DAX | (无对应) | 中国医生不口述病历，模式不成立 |
| Ambience / Heidi / Suki | (无对应) | — |

### S6 RCM / Admin AI（中国 = legacy HIS 厂 + AI 增量）

| US | 中国对应 | 关键说明 |
|----|----------|---------|
| Innovaccer ($3.45B) | **卫宁健康** + **创业慧康** | 中国是 HIS legacy 厂加 AI 模块，不是 AI-native |
| Commure ($6B) | 卫宁 + 东软 | — |
| Cohere Health (prior auth) | (中国无对应) | 中国 prior auth 在医保局手里 |
| Olive AI ⚰️ / Babylon ⚰️ | (无中国对应死亡案例) | 中国 admin AI 没出现过 unicorn 级别死亡 |

### S7 Consumer Virtual Care

| US | 中国对应 | 关键说明 |
|----|----------|---------|
| Hims & Hers ($2.5B 营收) | **京东健康 / 阿里健康** | 中国是巨头垂直，不是 startup |
| Ro | 京东健康 + 微医 | — |
| Spring Health (mental health) | (无对应规模玩家) | — |
| Forward Health ⚰️ / Pear ⚰️ | (无中国对应死亡) | — |

---

## 元发现：中国 vs 美国结构差异

| 段 | 美国结构 | 中国结构 | Nick 含义 |
|----|---------|----------|----------|
| S1 Scribe | startup 主导（Abridge/Nuance/Ambience）| 大厂语音 vertical（云知声）| 中国市场窄 |
| S2 Medical LLM | startup 主导（OpenEvidence/Hippocratic）| **大厂 vertical**（字节/阿里/京东/蚂蚁/腾讯/百度）| **PM path 入口在中国**|
| S3 Precision Med | 公开市场主导（Tempus/Guardant/Caris）| 中国头部全部经历美股退市潮，**MGI 是唯一 healthy 出海者** | MGI = 主线 B |
| S4 Drug Disc AI | 私募狂热 + Insilico HK IPO 范本 | **晶泰 + Insilico** 双 HK IPO 范本 | follow case |
| S5 Imaging AI | 国际化最强（10+ 国家头部并存）| 联影集团 / 数坤 / 推想 / 深睿 (国内站住，出海起步) | **主线 A**|
| S6 RCM/Admin | startup 蓬勃 + 大型死亡（Olive）| HIS legacy 厂 + AI 增量 | 不走 |
| S7 Consumer | startup + 公开市场（Hims/Ro）| **巨头垂直**（京东/阿里/平安）| 不优先 |

## 关键 "电梯方向" 信号

### 出海 active 的中国公司（按出海强度）

| 公司 | 出海状态 | 已覆盖区域 | Nick entry value |
|------|---------|-----------|-----------------|
| MGI 华大智造 | active | 76 国（SEA + EU + LATAM + MEA + Africa）| ⭐⭐⭐ |
| Insilico Medicine | active | SH + Suzhou + Boston + AbuDhabi + Montreal | ⭐⭐⭐ |
| 晶泰科技 XtalPi | active | 深圳 + 波士顿 | ⭐⭐ |
| 联影医疗 (母公司) | active | SEA + MEA + EU + LATAM | ⭐⭐⭐ |
| 联影智能 | planning | SEA + MEA | ⭐⭐⭐ (准备阶段)|
| 数坤科技 | planning | SEA | ⭐⭐ |
| 推想医疗 | planning | EU + SEA | ⭐ |
| 字节小荷 | planning | follow Bytedance global | ⭐⭐ (PM path) |
| 阿里通义医疗 | planning | SEA via Alibaba | ⭐ |
| 腾讯觅影 | planning | SEA | ⭐⭐ (PM path) |

### 中国 unicorn+ 估值 ($1B+)

| 公司 | 估值 ($M) | 段 | 状态 |
|------|-----------|-----|-----|
| 联影医疗 (母) | 15,000 | S5 | A 股上市 |
| 京东健康 | 12,000 | S7+S2 | HK 上市 |
| 阿里健康 | 8,000 | S2+S7 | HK 上市 |
| MGI 华大智造 | 3,000 | S3 | A 股上市 |
| Insilico Medicine | 2,700 | S4 | HK 上市 |
| 晶泰科技 XtalPi | 2,000 | S4 | HK 上市 |
| 平安好医生 | 1,500 | S7+S2 | HK 上市 |
| 卫宁健康 | 1,500 | S6 | A 股上市 |
| 联影智能 | 1,400 | S5 | 准备 IPO |
| 云知声 | 1,000 | S1+S2 | HK 上市 |

### 红旗集中的中国公司（≥ 3 个红旗 — 不建议作为 entry candidate）

| 公司 | 段 | 红旗数 | 主要问题 |
|------|-----|--------|---------|
| 诺辉健康 | S3 | 5/6 | HK 停牌 + 财务造假传闻 |
| 平安好医生 | S7+S2 | 4/6 | 估值倒挂 70%+ |
| 燃石医学 | S3 | 3/6 | NASDAQ 退市边缘 + 销售费用率 > 50% |
| 微医 | S7 | 3/6 | HK IPO 推迟 4 年+ |

---

## Nick 主线候选 final list（基于 Phase 1-3 全部数据）

### 工程师/技术路径

| 优先级 | 公司 | 段 | Entry signal |
|--------|------|-----|--------------|
| ⭐⭐⭐ 主线 A | **联影智能** | S5 | algorithm engineer / research scientist / 临床应用专家 |
| ⭐⭐⭐ 主线 A2 | **联影医疗** | S5 (硬件母公司) | 国际业务部门 + 海外 R&D |
| ⭐⭐⭐ 主线 B | **MGI 华大智造** | S3 | international business 深圳 + MGI Americas/Europe/LATAM |

### PM 路径（不是 engineer）

| 优先级 | 公司 | 段 | Entry signal |
|--------|------|-----|--------------|
| ⭐⭐ 主线 C | **GPS 中国 AI 部门** | S5 (外资) | clinical PM |
| ⭐⭐ Plan B | **字节小荷AI医生** | S2 | 医疗产品经理 |
| ⭐⭐ Plan C | **腾讯觅影** | S2+S5 | AI 影像 PM (双重对口) |

### 不建议

- 数坤/推想/深睿 国内研发岗 → 红旗 1-2/6，慎选
- 燃石/诺辉/微医 → 红旗 3-5/6，不进
- 平安好医生/阿里健康 PM → 估值倒挂或 PhD 不加分

---

## 数据补充建议（下一轮 refresh）

- MGI 海外业务 hiring page 实时拉取
- 联影智能 Series A 后具体团队结构 + 国际业务部门人头
- 字节小荷 / 阿里通义 医疗 vertical 招聘活跃度（脉脉拉数据）
- 晶泰科技 美国波士顿团队结构
- 中国新兴 AI biotech（除 Insilico/XtalPi 外）

## 来源
- [一财 - AI影像医疗 2025](https://www.yicai.com/news/102405013.html)
- [华大智造 2025 H1 报告](http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2025/2025-8/2025-08-23/11343694.PDF)
- [华大智造 海外营收占比 33%](https://m.gxfin.com/article/finance/zq/ssgs/2025-05-08/6239617.html)
- [字节小荷AI医生上线 2025-07](https://www.bianews.com/news/details?id=215625)
- [大厂AI医疗 2025 布局](https://m.huxiu.com/article/4840662.html)
- [燃石医学 NASDAQ 退市边缘](https://finance.sina.com.cn/stock/relnews/us/2024-11-22/doc-incwxxhh0570656.shtml)
- [世和基因 IPO 终止](https://bydrug.pharmcube.com/news/detail/be514f69954b646974d2c37dbd9c723d)
- [Insilico HK IPO 2025-12](https://insilico.com/news/p010170up1-insilico-medicine-lists-on-hong-kong-sto)
