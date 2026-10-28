# -*- coding: utf-8 -*-
"""Siemens AG (SIE.DE) 估值模型 — dossier 2026-10-28
10 年现金流年金 + 终值 IRR。OE0 = FY2025 净利剔一次性与 FCF 之间的三角。EUR 十亿。
"""
PRICE = 266.20          # 2026-10-27 (CNBC, Xetra 口径)
SHARES_B = 0.763        # 流通 763M (extraetf)
MCAP = PRICE * SHARES_B  # ~203.1
OE0 = 9.5               # FY2025 净利 10.4 剔一次性 ~8.6 与 FCF 10.8 之间

SCEN = [("bear", 0.25, 0.00, 14, 0.50),
        ("base", 0.50, 0.04, 16, 0.55),
        ("bull", 0.25, 0.07, 20, 0.60)]

def irr(cashflows, cost):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        npv = sum(cf / (1 + mid) ** (i + 1) for i, cf in enumerate(cashflows)) - cost
        if npv > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def build(g, exit_x, payout):
    cfs = []
    for t in range(1, 11):
        oe = OE0 * (1 + g) ** t
        cf = oe * payout
        if t == 10:
            cf += oe * exit_x
        cfs.append(cf)
    return cfs

def pv_at(hurdle, g, exit_x, payout):
    return sum(cf / (1 + hurdle) ** (i + 1) for i, cf in enumerate(build(g, exit_x, payout)))

print(f"市值 = EUR {MCAP:.1f}B ; OE0 = EUR {OE0}B ; P/OE = {MCAP/OE0:.1f}x")
print("-" * 60)
w_tv = 0
for name, p, g, x, po in SCEN:
    r = irr(build(g, x, po), MCAP)
    tv = OE0 * (1 + g) ** 10 * x
    w_tv += p * tv
    print(f"{name:4s} p={p:.0%} g={g:.0%} exit={x}x payout={po:.0%}  TV=EUR{tv:.0f}B  IRR={r:+.2%}")
w_irr = irr([sum(p * build(g, x, po)[t] for _, p, g, x, po in SCEN) for t in range(10)], MCAP)
print("-" * 60)
print(f"加权TV = EUR {w_tv:.0f}B  加权IRR(按现金流加权) = {w_irr:+.2%}")
for h in (0.08, 0.10, 0.12):
    pv = pv_at(h, 0.04, 16, 0.55)
    print(f"base @ {h:.0%} 门槛价 = EUR {pv / SHARES_B:.0f}")
print(f"bull @ 8% 门槛价 = EUR {pv_at(0.08, 0.07, 20, 0.60) / SHARES_B:.0f}")
