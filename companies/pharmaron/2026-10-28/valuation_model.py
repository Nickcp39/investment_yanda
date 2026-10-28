# -*- coding: utf-8 -*-
"""康龙化成 (300759.SZ / 3759.HK) 估值模型 — dossier 2026-10-28
10 年派付现金流 + 终值 IRR。OE0 = 2026E Non-IFRS 经调整净利。RMB 亿。
A/H 双重上市分别计价：A 为 card 主价，H 折人民币单列。
"""
import json, urllib.request

PRICE_A = 39.60          # 2026-10-28 收盘 (CNBC/东财, 三季报次日 +6.31%)
PRICE_H = 26.96          # 2026-10-28 收盘 HKD
SHARES = 18.3728         # 总股本 亿 (东财 f84)
def fx():
    try:
        req = urllib.request.Request(
            "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=HKDCNY&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json",
            headers={"User-Agent": "Mozilla/5.0"})
        d = json.load(urllib.request.urlopen(req, timeout=15))
        return float(d["FormattedQuoteResult"]["FormattedQuote"][0]["last"])
    except Exception:
        return 0.915
HKDCNY = fx()
MCAP_A = PRICE_A * SHARES                 # 727.6 亿 (A 口径, 与东财一致)
MCAP_H = PRICE_H * HKDCNY * SHARES        # H 口径全股本折算
OE0 = 21.5               # 2026E Non-IFRS 经调整归母净利 (券商一致预期; 9M26 实际 14.96 +22%)

# (名, p, g, 退出倍数, 派付率)
SCEN = [("bear", 0.30, 0.00, 15, 0.20),   # 地缘:BCC名单纳入+美国客户去风险化
        ("base", 0.45, 0.10, 20, 0.25),   # 漏斗兑现+GLP-1商业化, 26-28约19%渐降到10%
        ("bull", 0.25, 0.14, 25, 0.30)]   # 渗透率65%+大分子扭亏+CXO份额向中国集中

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
        cf = oe * po + (oe * x if t == 10 else 0)
        out.append(cf)
    return out

def pv_at(h, g, x, po):
    return sum(cf / (1 + h) ** (i + 1) for i, cf in enumerate(build(g, x, po)))

for label, mc in (("A股口径", MCAP_A), ("H股口径", MCAP_H)):
    print(f"== {label}: 市值 {mc:.0f} 亿, P/OE {mc/OE0:.1f}x")
    for name, p, g, x, po in SCEN:
        print(f"  {name:4s} p={p:.0%} g={g:.0%} exit={x}x  TV={OE0*(1+g)**10*x:6.0f}亿  IRR={irr(build(g,x,po), mc):+.2%}")
    w = irr([sum(p*build(g,x,po)[t] for _,p,g,x,po in SCEN) for t in range(10)], mc)
    print(f"  加权IRR = {w:+.2%}")
    print()
print(f"HKDCNY = {HKDCNY:.4f}")
for h in (0.08, 0.10, 0.12):
    pv = pv_at(h, 0.10, 20, 0.25)
    print(f"base @ {h:.0%}: 每股 CNY {pv/SHARES:.2f} = HKD {pv/SHARES/HKDCNY:.2f}")
print(f"bull @ 8%: 每股 CNY {pv_at(0.08,0.14,25,0.30)/SHARES:.2f}")
print(f"A股现价 vs base 8% 线: {PRICE_A/(pv_at(0.08,0.10,20,0.25)/SHARES)-1:+.1%}")
print(f"H股现价 vs base 8% 线: {PRICE_H*HKDCNY/(pv_at(0.08,0.10,20,0.25)/SHARES)-1:+.1%}")
