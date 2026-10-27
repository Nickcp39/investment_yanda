# -*- coding: utf-8 -*-
"""云迹科技 (2670.HK) 估值模型 — dossier 2026-10-27
10 年期权 IRR，无分红假设。单位: RMB 百万(除股价/股本)。
情景: bear/base/bull, 加权 buy_below = base 8% IRR 门槛价。
"""
import json, urllib.request

# ---- 股本与现价 ----
SHARES_M = 697.94          # 总股本(百万股, 1拆10后), 由支涛 8.62% / 60,161,930 股反推
PRICE_HKD = 3.135          # 2026-10-27 盘中 (Yahoo chart API, regularMarketTime 1793085375)

def fx_hkdcny():
    try:
        with urllib.request.urlopen(
            "https://query1.finance.yahoo.com/v8/finance/chart/HKDCNY=X?range=1d&interval=1d",
            timeout=15) as r:
            d = json.load(r)
        return float(d["chart"]["result"][0]["meta"]["regularMarketPrice"])
    except Exception:
        return 0.92

HKDCNY = fx_hkdcny()
MKT_CAP_RMB_M = SHARES_M * PRICE_HKD * HKDCNY

CASH_NET_M = 640.0  # 2026-06-30 现金2.55亿+定期3.85亿, 近似净现金(债务忽略)

# ---- 情景: (概率, 终值TV RMB百万) ----
# bear: 2035 收入6亿 GM25% OE~0, 终值=残值8亿
# base: 2035 收入18亿(2025起CAGR19.6%), 净利率10% -> OE1.8亿 x 15x = 27亿
# bull: 平台化, 2035 收入45亿, 净利率15% -> 6.75亿 x 20x = 135亿
SCEN = [("bear", 0.30, 800), ("base", 0.50, 2700), ("bull", 0.20, 13500)]
YEARS = 10

def irr(tv_m, cost_m):
    return (tv_m / cost_m) ** (1 / YEARS) - 1

rows = []
w_tv = 0.0
for name, p, tv in SCEN:
    r = irr(tv, MKT_CAP_RMB_M)
    w_tv += p * tv
    rows.append((name, p, tv, r))

w_irr = irr(w_tv, MKT_CAP_RMB_M)

def price_for(target_irr, tv_m):
    pv = tv_m / (1 + target_irr) ** YEARS          # RMB 百万
    return pv / (SHARES_M * HKDCNY)                # HKD/股

print(f"HKDCNY = {HKDCNY:.4f}")
print(f"市值 = {MKT_CAP_RMB_M:.0f} RMB百万 ≈ {MKT_CAP_RMB_M/100:.1f} 亿 (HK${PRICE_HKD} x {SHARES_M}M)")
print("-" * 56)
for name, p, tv, r in rows:
    print(f"{name:4s} p={p:.0%}  TV={tv/100:5.1f}亿  IRR={r:+.2%}")
print("-" * 56)
print(f"加权TV = {w_tv/100:.1f}亿  加权IRR = {w_irr:+.2%}")
print("-" * 56)
for t in (0.08, 0.10, 0.12):
    print(f"base TV 27亿 @ {t:.0%} 门槛价 = HK${price_for(t, 2700):.2f}")
print(f"bull TV 135亿 @ 8% 门槛价 = HK${price_for(0.08, 13500):.2f}")
