# -*- coding: utf-8 -*-
"""Siemens Healthineers (SHL.DE) 估值模型 — dossier 2026-10-28
10 年派付现金流 + 终值 IRR。OE0 = FY2026E 经调整净利。EUR 十亿。
"""
PRICE = 42.04           # 2026-10-28 Xetra 盘中 (CNBC)
SHARES_B = 1.13
MCAP = PRICE * SHARES_B  # ~47.5
OE0 = 2.6               # FY2026E adj 净利: adj EPS 指引 2.35-2.45 x 1.13B ≈ 2.7; mwb 2.613; FY25 报告净利 2.2

# (名, p, g, 退出倍数, 派付率)  — 派付含股息( payout ~50-55%) + 回购
SCEN = [("bear", 0.25, 0.00, 14, 0.55),   # Diagnostics 结构性萎缩 + 中国 VBP 扩散 + 关税常驻
        ("base", 0.50, 0.05, 17, 0.60),   # Imaging/PT 中单-digit + Varian 高单-digit + 诊断企稳/剥离
        ("bull", 0.25, 0.08, 20, 0.60)]   # 分拆去悬顶 + 诊断翻盘/出售 + Varian 新平台放量

def irr(cfs, cost):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        npv = sum(cf / (1 + mid) ** (i + 1) for i, cf in enumerate(cfs)) - cost
        if npv > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def build(g, x, po):
    out = []
    for t in range(1, 11):
        oe = OE0 * (1 + g) ** t
        out.append(oe * po + (oe * x if t == 10 else 0))
    return out

def pv_at(h, g, x, po):
    return sum(cf / (1 + h) ** (i + 1) for i, cf in enumerate(build(g, x, po)))

print(f"市值 = EUR {MCAP:.1f}B ; OE0 = EUR {OE0}B ; P/OE = {MCAP/OE0:.1f}x")
print("-" * 60)
w_tv = 0
for name, p, g, x, po in SCEN:
    r = irr(build(g, x, po), MCAP)
    tv = OE0 * (1 + g) ** 10 * x
    w_tv += p * tv
    print(f"{name:4s} p={p:.0%} g={g:.0%} exit={x}x payout={po:.0%}  TV=EUR{tv:5.1f}B  IRR={r:+.2%}")
w_irr = irr([sum(p * build(g, x, po)[t] for _, p, g, x, po in SCEN) for t in range(10)], MCAP)
print("-" * 60)
print(f"加权TV = EUR {w_tv:.0f}B  加权IRR(按现金流加权) = {w_irr:+.2%}")
for h in (0.08, 0.10, 0.12):
    print(f"base @ {h:.0%} 门槛价 = EUR {pv_at(h, 0.05, 17, 0.60)/SHARES_B:.2f}")
print(f"bull @ 8% 门槛价 = EUR {pv_at(0.08, 0.08, 20, 0.60)/SHARES_B:.2f}")
