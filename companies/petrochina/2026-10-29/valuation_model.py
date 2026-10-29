# -*- coding: utf-8 -*-
"""中国石油 PetroChina (601857.SH / 0857.HK) 估值模型 — dossier 2026-10-29
10 年派付现金流 + 终值 IRR。OE0 = 2026E 归母净利。RMB 亿元。
同一天对 A 股与 H 股两个价格分别求解（同股同权，汇率 HKD/CNY=0.917）。
"""
SHARES_YI = 1830.21        # 总股本 1830.21 亿股 (A 1619.22 + H 211.0)
PRICE_A = 13.69            # 2026-10-29 收盘，+3.24%，52周新高=近18年新高 (东财/富途)
PRICE_H_HKD = 10.24        # 2026-10-29 盘中 (东财)
HKDCNY = 0.917
PRICE_H = PRICE_H_HKD * HKDCNY   # ~9.39 RMB
MCAP_A = PRICE_A * SHARES_YI     # ~25056 亿
MCAP_H = PRICE_H * SHARES_YI     # ~17186 亿
OE0 = 1860                 # 2026E 归母: 券商一致预期 1863.63 亿 (EPS 1.02); 9M26 已 1557.76
                           # 注意: 9M 实现油价 77.65 美元/桶 含战争溢价, Brent 现货 ~106-112,
                           # 一致预期隐含 2027-28 油价回落后盈利走平 (中银: 26-28E 1822/1826/1838)

# (名, p, g, 退出PE, 派付率) — 派付 = 股息 (2025 派息率 54.7%, 无回购)
SCEN = [("bear", 0.25, -0.02, 10, 0.55),  # 油价回落至 60-65 (EIA 2027 布油 83.74 再下探), 盈利中枢下移
        ("base", 0.50, 0.00, 11, 0.55),   # 油价 70-80 中枢, 盈利走平 (券商 26-28E 三年 flat), 天然气/新材料对冲
        ("bull", 0.25, 0.03, 13, 0.55)]   # 战争溢价常态化 + 天然气市场化提价 + 新材料放量

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

def report(label, mcap, price_fx):
    print(f"\n=== {label}: 市值 = RMB {mcap:.0f} 亿 ; OE0 = {OE0} 亿 ; P/OE = {mcap/OE0:.1f}x ===")
    w_irr = irr([sum(p * build(g, x, po)[t] for _, p, g, x, po in SCEN) for t in range(10)], mcap)
    for name, p, g, x, po in SCEN:
        r = irr(build(g, x, po), mcap)
        print(f"  {name:4s} p={p:.0%} g={g:+.0%} exit={x}x payout={po:.0%}  IRR={r:+.2%}")
    print(f"  加权IRR = {w_irr:+.2%}")
    for h in (0.08, 0.10, 0.12):
        print(f"  base @ {h:.0%} 门槛价 = RMB {pv_at(h, 0.00, 11, 0.55)/SHARES_YI:.2f} ({price_fx})")
    return w_irr

report("A股 601857 @13.69", MCAP_A, "A股价")
r_h = report("H股 0857 @HK$10.24", MCAP_H, "折RMB")
print(f"\nH股 8%/10%/12% 门槛折 HKD: "
      f"{pv_at(0.08,0.00,11,0.55)/SHARES_YI/HKDCNY:.2f} / "
      f"{pv_at(0.10,0.00,11,0.55)/SHARES_YI/HKDCNY:.2f} / "
      f"{pv_at(0.12,0.00,11,0.55)/SHARES_YI/HKDCNY:.2f}")
