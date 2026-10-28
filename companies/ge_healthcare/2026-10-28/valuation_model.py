# -*- coding: utf-8 -*-
"""GE HealthCare (GEHC, NASDAQ) 估值模型 — dossier 2026-10-28
10 年派付现金流 + 终值 IRR。OE0 = 2026E 经调整净利。USD 十亿。
"""
PRICE = 76.16           # 2026-10-28 盘中 ~10:08 ET (CNBC; Q3 财报日 +6.9%)
SHARES_B = 0.452        # Morningstar 452.14M (2026-10-28)
MCAP = PRICE * SHARES_B  # ~34.4
OE0 = 2.25              # 2026E adj 净利: adj EPS 指引中值 ~5.00 x ~0.45B diluted ≈ 2.25
                        # (Q3 含 IEEPA 关税退款一次性; FY25 adj EPS 4.59)

# (名, p, g, 退出倍数, 派付率)  — 派付含股息(yield~0.2%) + 回购(2026 计划 $1.0B)
SCEN = [("bear", 0.25, 0.00, 13, 0.55),   # PCS 烂尾 + 中国持续下滑 + 关税/通胀常驻 + FCF 转化率恶化
        ("base", 0.50, 0.05, 16, 0.60),   # AIS/PDx 中单-digit + 订单簿转化 + PCS 处置 + 还债/回购
        ("bull", 0.25, 0.08, 19, 0.60)]   # 核药(Flyrcado)放量 + Photonova CT 周期 + PCS 出售增值 + 中国企稳

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

print(f"市值 = USD {MCAP:.1f}B ; OE0 = USD {OE0}B ; P/OE = {MCAP/OE0:.1f}x")
print("-" * 60)
w_tv = 0
for name, p, g, x, po in SCEN:
    r = irr(build(g, x, po), MCAP)
    tv = OE0 * (1 + g) ** 10 * x
    w_tv += p * tv
    print(f"{name:4s} p={p:.0%} g={g:.0%} exit={x}x payout={po:.0%}  TV=USD{tv:5.1f}B  IRR={r:+.2%}")
w_irr = irr([sum(p * build(g, x, po)[t] for _, p, g, x, po in SCEN) for t in range(10)], MCAP)
print("-" * 60)
print(f"加权TV = USD {w_tv:.0f}B  加权IRR(按现金流加权) = {w_irr:+.2%}")
for h in (0.08, 0.10, 0.12):
    print(f"base @ {h:.0%} 门槛价 = USD {pv_at(h, 0.05, 16, 0.60)/SHARES_B:.2f}")
print(f"bull @ 8% 门槛价 = USD {pv_at(0.08, 0.08, 19, 0.60)/SHARES_B:.2f}")
