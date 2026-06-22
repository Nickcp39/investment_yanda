# NVDA Value Chain Map (M3) — as_of 2026-06-19

## AI 算力价值链中的位置
```
[HBM 内存: SK海力士/三星/美光] ─┐
[晶圆+先进封装 CoWoS: TSMC]   ─┼─► [NVIDIA: GPU设计+CUDA+互联+系统整合] ─► [ODM/OEM 整机] ─► [Hyperscaler/AI Cloud/主权/企业] ─► [终端 AI 应用]
[网络: 自有 InfiniBand/Spectrum-X]┘
```

## NVDA 的捕获位
- **上游依赖（议价对手）**: TSMC（CoWoS 先进封装是产能瓶颈）、HBM 三家。NVDA 是其最大客户，议价强，但**供应是真实约束**（存货升至 $25.8B 反映备货）。
- **NVDA 自身环节**: GPU 架构设计 + CUDA 软件栈 + NVLink/InfiniBand/Spectrum-X 网络 + 系统/机柜整合（"AI 工厂")。这是价值链中**利润最厚、最难替代**的一段（GM ~75%）。
- **下游客户**: Hyperscale ~50% DC（集中度风险，且这些客户同时在自研 ASIC = 又是客户又是潜在竞争者）；另 50% 多元化（AI Clouds、主权、企业）。

## 利润池归属（Q1 FY27）
- DC Compute $60.4B + Networking $14.8B = $75.2B/季，GM ~75% → NVDA 捕获了 AI 训练/推理价值链中**最大的单一利润池**。
- 网络 +199% Y/Y 说明 NVDA 正把利润池从"卖芯片"扩到"卖互联+系统"，**加深护城河、抬高单系统 ASP**。

## 价值链风险
- **客户=竞争者悖论**: 最大客户（hyperscaler）正自研 custom silicon（TPU/Trainium/MTIA）以降低对 NVDA 的依赖 → 长期份额侵蚀的结构性来源（O4 OPEN，未取定量份额）。
- **上游瓶颈**: CoWoS/HBM 产能限制既是护城河（对手也受限）也是供给约束（影响交付节奏）。
- **China 节点关闭**: 出口管制已使 China DC 出货归零，价值链一个区域市场被永久切断（已在情景压低）。
