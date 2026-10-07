#!/usr/bin/env python3
"""verify_report.py — 发布前自检（只读本地文件）。

1. 关键数字用独立代码路径从原始价格文件重算，与报告引用值比对；
2. report.md 无残留占位符；每个主题都有结局表；来源链接计数；
3. PDF 书签覆盖所有一级章节。
结果写入 data/verification.json，任何一项失败则退出码 1。
"""
import csv
import datetime as dt
import gzip
import io
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, detail=""):
    checks.append({"check": name, "ok": bool(ok), "detail": detail})


def closes(tk):
    fn = BASE / "data/raw/prices" / (tk.replace("^", "IDX_") + ".csv.gz")
    rows = csv.DictReader(io.StringIO(gzip.decompress(fn.read_bytes()).decode()))
    return [(r["date"], float(r["close"])) for r in rows]


def first_close_above(px, level, after):
    return next((d for d, c in px if d > after and c > level), None)


def years(a, b):
    return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days / 365.25


# 1) 独立重算：峰值 → 第一次严格高于峰值的日期
cases = [  # (代码, 峰值搜索区间, 报告里写的收复年数)
    ("^IXIC", ("2000-01-01", "2000-12-31"), 15.1),
    ("CSCO", ("2000-01-01", "2000-12-31"), 25.7),
    ("INTC", ("2000-01-01", "2000-12-31"), 25.6),
    ("MSFT", ("1999-06-01", "2000-12-31"), 16.8),
    ("GLW", ("2000-01-01", "2000-12-31"), 25.4),
    ("FCX", ("2008-01-01", "2008-12-31"), 17.7),
    ("GS", ("2007-01-01", "2007-12-31"), 9.3),
    ("MS", ("2007-01-01", "2007-12-31"), 13.9),
]
for tk, (a, b), claimed in cases:
    px = closes(tk)
    win = [x for x in px if a <= x[0] <= b]
    pk = max(win, key=lambda x: x[1])
    rec = first_close_above(px, pk[1], pk[0])
    got = round(years(pk[0], rec), 1) if rec else None
    check(f"收复用时 {tk}", got is not None and abs(got - claimed) <= 0.15, f"峰值 {pk[0]} {pk[1]:.2f} → {rec}，{got} 年（报告 {claimed}）")

# 2) report.md
md = (BASE / "report.md").read_text(encoding="utf-8")
left = [x for x in re.findall(r"\{\{[^}]+\}\}", md) if "…" not in x]
check("无残留占位符", not left, str(left[:5]))
T = json.loads((BASE / "data/themes_computed.json").read_text(encoding="utf-8"))
src = (BASE / "report_source.md").read_text(encoding="utf-8")
missing = [t["id"] for t in T["themes"] if f"{{{{TABLE:theme:{t['id']}}}}}" not in src]
check("每个主题都有结局表", not missing, str(missing))
links = re.findall(r"\]\((https?://[^)\s]+)\)", md)
check("来源链接数量", len(links) > 300, f"{len(links)} 个链接，{len(set(links))} 个不同网址")
check("无 Yahoo 代码复用拒绝", all("rejected" not in (c.get("price") or {}) for c in T["companies"]),
      str([c["name"] for c in T["companies"] if "rejected" in (c.get("price") or {})]))

# 3) PDF 书签
st = json.loads((BASE / "data/pdf_structure.json").read_text(encoding="utf-8"))
heads = [l[3:].strip() for l in md.splitlines() if l.startswith("## ")]
marks = [e["title"] for e in st["sections"]]
check("PDF 书签覆盖所有章节", len(heads) == len(marks), f"{len(heads)} 个章节 / {len(marks)} 个书签，{st['pages']} 页")

(BASE / "data/verification.json").write_text(json.dumps(checks, ensure_ascii=False, indent=1), encoding="utf-8")
for c in checks:
    print(("PASS " if c["ok"] else "FAIL ") + c["check"] + " — " + c["detail"])
sys.exit(0 if all(c["ok"] for c in checks) else 1)
