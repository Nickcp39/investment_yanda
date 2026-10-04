#!/usr/bin/env python3
"""fetch_filings.py — 石油批次：下载每家最新 10-K、最新 10-Q、最新财报 8-K（EX-99.x）原文到各 dossier 的 raw/。

吸取 2026-09-28 批次 UBER 的教训（摘要工具漏掉 Delivery Hero 收购）：10-K/10-Q 一律下载全文，本地检索，不用摘要。
文件选择由 SEC submissions API 自动完成；XOM 同时查新旧两个 CIK。
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-09-30"
ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
CIKS = {"XOM": [2115436, 34088], "CVX": [93410], "OXY": [797468], "COP": [1163165], "KMI": [1506307]}


def get(url, as_json=False):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                b = r.read()
                return json.loads(b.decode("utf-8")) if as_json else b
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def to_text(raw: bytes) -> str:
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)  # 去掉 inline XBRL 头部，避免上次 VST 那种满屏标签
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def pick(cik):
    j = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", as_json=True)
    r = j["filings"]["recent"]
    rows = [dict(form=r["form"][i], date=r["filingDate"][i], acc=r["accessionNumber"][i], doc=r["primaryDocument"][i],
                 items=(r.get("items") or [""] * len(r["form"]))[i]) for i in range(len(r["form"]))]
    return rows


def save(tk, cik, row, label, doc=None):
    base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{row['acc'].replace('-', '')}"
    url = f"{base}/{doc or row['doc']}"
    txt = to_text(get(url))
    out = ROOT / tk.lower() / AS_OF / "raw"
    out.mkdir(parents=True, exist_ok=True)
    fn = out / f"{row['date']}_{row['form']}_{label}_{Path(doc or row['doc']).stem}.txt"
    fn.write_text(f"SOURCE: {url}\nFILED: {row['date']} {row['form']}\n\n{txt}\n", encoding="utf-8")
    print(f"{tk:4} {row['date']} {row['form']:5} {label:12} {len(txt):>9,} chars -> {fn.name}")


def main():
    only = set(sys.argv[1:])
    for tk, ciks in CIKS.items():
        if only and tk not in only:
            continue
        rows = []
        for c in ciks:
            rows += [dict(x, cik=c) for x in pick(c)]
        rows.sort(key=lambda x: x["date"], reverse=True)
        tenk = next(x for x in rows if x["form"] == "10-K")
        tenq = next(x for x in rows if x["form"] == "10-Q")
        er = next(x for x in rows if x["form"] == "8-K" and "2.02" in x["items"])
        save(tk, tenk["cik"], tenk, "10K_FY")
        save(tk, tenq["cik"], tenq, "10Q_latest")
        idx = get(f"https://www.sec.gov/Archives/edgar/data/{er['cik']}/{er['acc'].replace('-', '')}/index.json", as_json=True)
        docs = [it["name"] for it in idx["directory"]["item"] if it["name"].lower().endswith((".htm", ".html"))]
        ex = [n for n in docs if re.search(r"ex-?99|exhibit99|ex99|ex991|ex992", n, re.I)] or docs[:1]
        for n in ex[:2]:
            save(tk, er["cik"], er, "earnings_8K", doc=n)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
