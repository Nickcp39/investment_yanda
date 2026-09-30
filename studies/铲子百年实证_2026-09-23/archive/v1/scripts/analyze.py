# -*- coding: utf-8 -*-
"""铲子百年实证 · 分析脚本
计算每个铲子标的的全期年化回报(CAGR)、相对标普500(^GSPC)的超额收益、
以及关键分段回报。核心验证：带锁的铲子 vs 裸铲子 的长期回报差异。
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(BASE, "data", "shovel_prices.json"), encoding="utf-8"))

def cagr(rows, start_date=None, end_date=None):
    """rows: [[date, adjclose], ...] 返回 (cagr, 倍数, 月数)"""
    pts = [(r[0], r[1]) for r in rows]
    if start_date:
        pts = [p for p in pts if p[0] >= start_date]
    if end_date:
        pts = [p for p in pts if p[0] <= end_date]
    if len(pts) < 2:
        return None, None, 0
    f, l = pts[0][1], pts[-1][1]
    if f <= 0 or l <= 0:
        return None, None, 0
    months = (int(pts[-1][0][:4]) - int(pts[0][0][:4])) * 12 + (int(pts[-1][0][5:7]) - int(pts[0][0][5:7]))
    if months <= 0:
        return None, None, 0
    mult = l / f
    return (mult ** (12.0 / months) - 1) * 100, mult, months

def align_bench(bench_rows, date):
    """找到基准在给定日期(或之后)的 adjclose"""
    for r in bench_rows:
        if r[0] >= date:
            return r[0], r[1]
    return None, None

bench = DATA["^GSPC"]["rows"]

def excess(ticker):
    d = DATA[ticker]
    rows = d["rows"]
    if not rows:
        return None
    start, end = rows[0][0], rows[-1][0]
    c, m, mo = cagr(rows)
    # 同期基准
    bdate, bval = align_bench(bench, start)
    bend, bval_end = align_bench(bench, end)
    bc = None
    if bval and bval_end and bval > 0:
        bmonths = (int(bend[:4]) - int(bdate[:4])) * 12 + (int(bend[5:7]) - int(bdate[5:7]))
        if bmonths > 0:
            bc = ((bval_end / bval) ** (12.0 / bmonths) - 1) * 100
    return {"cagr": c, "mult": m, "months": mo, "bench_cagr": bc,
            "excess": (c - bc) if (c is not None and bc is not None) else None,
            "start": start, "end": end, "name": d["name"], "case": d["case"], "lock": d["lock"]}

print("=" * 100)
print("全期回报表（按锁类型分组）")
print("=" * 100)
order = ["AFTERMARKET", "OLIGOPOLY", "MIXED", "WINDOW", "BARE"]
for lock in order:
    group = [(t, excess(t)) for t in DATA if DATA[t].get("lock") == lock and t not in ("SPY", "^GSPC") and DATA[t].get("rows")]
    if not group:
        continue
    print(f"\n【{lock}】")
    group.sort(key=lambda x: -(x[1]["cagr"] or 0))
    for t, e in group:
        ex = f"{e['excess']:+.1f}pp" if e['excess'] is not None else "  n/a"
        print(f"  {t:10s} {e['name'][:26]:26s} CAGR={e['cagr']:6.1f}%  基准={e['bench_cagr']:6.1f}%  超额={ex:8s}  倍数={e['mult']:8.1f}x  {e['start'][:4]}-{e['end'][:4]}")

print("\n" + "=" * 100)
print("关键分段回报")
print("=" * 100)

def seg(ticker, d1, d2, label):
    rows = DATA[ticker]["rows"]
    c, m, mo = cagr(rows, d1, d2)
    if c is None:
        print(f"  {ticker:10s} {label:40s} 无数据")
        return
    print(f"  {ticker:10s} {label:40s} CAGR={c:7.1f}%  倍数={m:6.1f}x  ({d1}->{d2})")

# Cisco 泡沫
seg("CSCO", "1990-03-01", "2000-03-01", "建设期(1990-2000,泡沫顶)")
seg("CSCO", "2000-03-01", "2026-09-01", "建设期后(2000-今)")
seg("CSCO", "1990-03-01", "2026-09-01", "全期(1990-今)")
# 发动机 vs 结构件
seg("GE", "1970-01-01", "2026-09-01", "GE 全期(1970-今)")
seg("RTX", "1985-01-01", "2026-09-01", "RTX/Pratt 全期(1985-今)")
seg("RR.L", "1988-06-01", "2026-09-01", "劳斯莱斯 全期(1988-今)")
seg("SAF.PA", "2000-01-01", "2026-09-01", "赛峰 全期(2000-今)")
# 造船 vs 挖矿
seg("010140.KS", "2000-01-01", "2026-09-01", "三星重工 全期(2000-今)")
seg("042660.KS", "2001-01-01", "2026-09-01", "韩华海洋(大宇) 全期(2001-今)")
seg("6301.T", "2000-01-01", "2026-09-01", "小松 全期(2000-今)")
seg("CAT", "1985-01-01", "2026-09-01", "卡特彼勒 全期(1985-今)")
# 光伏设备
seg("AMAT", "1985-01-01", "2026-09-01", "AMAT 全期(1985-今)")
seg("SEDG", "2015-03-01", "2026-09-01", "SolarEdge 全期(2015-今)")
seg("ENPH", "2012-03-01", "2026-09-01", "Enphase 全期(2012-今)")
# 油服
seg("SLB", "1985-01-01", "2026-09-01", "斯伦贝谢 全期(1985-今)")
seg("HAL", "1985-01-01", "2026-09-01", "哈里伯顿 全期(1985-今)")
# 当前 AI 电力铲子
seg("GEV", "2024-03-01", "2026-09-01", "GE Vernova (2024拆分至今)")
seg("VRT", "2018-08-01", "2026-09-01", "Vertiv (2018至今)")
seg("ETN", "2023-01-01", "2026-09-01", "伊顿 Eaton (AI电力期2023-今)")
# 基准
seg("^GSPC", "1985-01-01", "2026-09-01", "标普500 全期(1985-今)")
seg("^GSPC", "2000-01-01", "2026-09-01", "标普500 (2000-今)")
