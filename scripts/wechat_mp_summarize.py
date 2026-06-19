# -*- coding: utf-8 -*-
"""Quick analysis of the wechat_mp archive (美股投资网). Read-only."""
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSONL = ROOT / "sources/news/wechat_mp/manifest.jsonl"

rows = []
for line in JSONL.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line:
        rows.append(json.loads(line))

def pdate(s):
    try:
        return datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None

dated = [(pdate(r.get("publish_time", "")), r) for r in rows]
dated = [(d, r) for d, r in dated if d]
dated.sort(key=lambda x: x[0])

print(f"总篇数: {len(rows)}  (有有效发布时间: {len(dated)})")
if dated:
    print(f"时间跨度: {dated[0][0].date()}  →  {dated[-1][0].date()}")

# Monthly distribution
months = Counter(d.strftime("%Y-%m") for d, _ in dated)
print("\n月度分布:")
for m in sorted(months):
    print(f"  {m}: {months[m]:3d}  {'#' * months[m]}")

# Text length
tl = [r.get("text_length", 0) or 0 for r in rows]
print(f"\n正文长度: 总计 {sum(tl):,} 字 | 平均 {sum(tl)//max(len(tl),1):,} | 最短 {min(tl)} | 最长 {max(tl)}")

# Largest day gaps (potential missing articles)
print("\n相邻文章最大间隔 (>5 天, 可能有缺口):")
gaps = []
for i in range(1, len(dated)):
    gap = (dated[i][0] - dated[i-1][0]).days
    if gap > 5:
        gaps.append((gap, dated[i-1][0].date(), dated[i][0].date()))
for gap, a, b in sorted(gaps, reverse=True)[:15]:
    print(f"  {gap:3d} 天: {a} → {b}")

# Ticker extraction from title + description
STOP = {
    "AI","IPO","US","USA","VIP","ETF","CEO","CFO","SEC","FED","PC","GPU","CPU",
    "AWS","API","UI","UX","SAAS","MSCI","PE","PS","EPS","FSD","ALL","STOCKWE",
    "VC","ETF","II","III","IV","TD","DRAM","HBM","LLM","DC","TV","OK","AM","PM",
    "QE","QT","GDP","CPI","PPI","FOMC","Q1","Q2","Q3","Q4","NO","OF","TO","IN",
    "ON","AT","BY","OR","AND","THE","FOR","DOW","SPX","ETN",
}
tick = Counter()
for r in rows:
    blob = (r.get("title","") or "") + " " + (r.get("description","") or "")
    for tok in re.findall(r"[A-Z]{2,6}", blob):
        if tok not in STOP:
            tick[tok] += 1
print("\n标题/摘要中出现最多的代码/标的 (Top 30):")
for t, c in tick.most_common(30):
    print(f"  {t:6s} {c}")

# Author / account
print("\n账号分布:")
for a, c in Counter(r.get("account_name","") for r in rows).most_common():
    print(f"  {a}: {c}")
print("\n作者字段分布:")
for a, c in Counter(r.get("author","") for r in rows).most_common():
    print(f"  {a}: {c}")
