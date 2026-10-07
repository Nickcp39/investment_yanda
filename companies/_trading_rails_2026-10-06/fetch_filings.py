#!/usr/bin/env python3
"""fetch_filings.py — 交易通道批次：下载每家最新 10-K（FUTU 为 20-F）、最新 10-Q、最新财报 8-K / 6-K（EX-99.x）原文到各 dossier 的 raw/。
（由 _oil_2026-09-30/fetch_filings.py 复制；缺某类文件的新上市公司跳过该类，并打印 MISSING）

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

AS_OF = "2026-10-06"
ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
CIKS = {"IBKR": [1381197], "HOOD": [1783879], "COIN": [1679788], "FUTU": [1754581], "VIRT": [1592386],
        "CBOE": [1374310], "CME": [1156375], "ICE": [1571949], "NDAQ": [1120193], "BR": [1383312],
        "CRCL": [1876042], "BTGO": [1740604], "SECZ": [2094496]}
FOLDER = {"CRCL": "circle"}  # 仓库里 Circle 已有 companies/circle/（2026-05 dry-run 计划）


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


def _row(m):
    """一个 <tr> 压成一行：去空单元格、把单独的 "$" / ")" / "%" 并进相邻单元格。"""
    cells = []
    for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0)):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c)).replace("\xa0", " ")).strip()
        if not t or t == "$":
            continue
        if t in (")", "%", ")%") and cells:
            cells[-1] += t
            continue
        cells.append(t)
    return "\n" + " | ".join(cells) + "\n" if cells else "\n"


def to_text(raw: bytes) -> str:
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)  # 去掉 inline XBRL 头部，避免上次 VST 那种满屏标签
    s = re.sub(r"(?is)<tr[^>]*>.*?</tr>", _row, s)  # 表格逐行压平（本批新增：交易所 / 券商财报几乎全是表）
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
    out = ROOT / FOLDER.get(tk, tk.lower()) / AS_OF / "raw"
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
        rows = [x for x in rows if x["date"] <= "2026-10-07"]
        annual = next((x for x in rows if x["form"] in ("10-K", "20-F")), None)
        tenq = next((x for x in rows if x["form"] == "10-Q"), None)
        if annual:
            save(tk, annual["cik"], annual, "annual_FY")
        else:
            print(f"{tk:4} MISSING annual report")
        if tenq and (not annual or tenq["date"] > annual["date"]):
            save(tk, tenq["cik"], tenq, "10Q_latest")
        er = next((x for x in rows if x["form"] == "8-K" and "2.02" in x["items"]), None)
        if tk == "FUTU":  # 6-K 没有 items 字段：取最近一份附 EX-99.1 的 6-K（季度业绩新闻稿）
            for x in rows:
                if x["form"] != "6-K":
                    continue
                idx = get(f"https://www.sec.gov/Archives/edgar/data/{x['cik']}/{x['acc'].replace('-', '')}/index.json", as_json=True)
                names = [it["name"] for it in idx["directory"]["item"]]
                if any(re.search(r"ex-?99", n, re.I) for n in names) and x["date"] >= "2026-08-01":
                    t = to_text(get(f"https://www.sec.gov/Archives/edgar/data/{x['cik']}/{x['acc'].replace('-', '')}/"
                                    + next(n for n in names if re.search(r"ex-?99", n, re.I))))
                    if "Total revenues" in t or "total revenues" in t:
                        er = x
                        break
                time.sleep(0.3)
        if not er:
            print(f"{tk:4} MISSING earnings release")
        else:
            idx = get(f"https://www.sec.gov/Archives/edgar/data/{er['cik']}/{er['acc'].replace('-', '')}/index.json", as_json=True)
            docs = [it["name"] for it in idx["directory"]["item"] if it["name"].lower().endswith((".htm", ".html"))]
            ex = [n for n in docs if re.search(r"ex-?99|exhibit99|ex99|ex991|ex992|q\d.*(release|letter|deck)", n, re.I)] or docs[:1]
            for n in ex[:3]:
                save(tk, er["cik"], er, "earnings", doc=n)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
