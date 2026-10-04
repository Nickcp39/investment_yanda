#!/usr/bin/env python3
"""fetch_letters.py — 下载伯克希尔致股东信（一手）并抽取文本，检索石油相关段落。

源：https://www.berkshirehathaway.com/letters/ （1998–2002 命名为 YYYYpdf.pdf，2003 起为 YYYYltr.pdf）
输出：
  raw/letters/<YYYY>.txt          每封信的全文文本（PyMuPDF 抽取）
  data/letters_oil_hits.json      每年命中的关键词段落（前后各约 600 字符）
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parents[1]
RAW = HERE / "raw" / "letters"
UA = {"User-Agent": "Mozilla/5.0"}
YEARS = range(2002, 2026)
KEYS = ["PetroChina", "ConocoPhillips", "Conoco", "Exxon", "Chevron", "Occidental", "OxyChem", "Suncor",
        "Phillips 66", "oil and gas", "oil price", "price of oil", "Permian", "Vicki", "Hollub"]


def download(year):
    for name in (f"{year}ltr.pdf", f"{year}pdf.pdf"):
        url = f"https://www.berkshirehathaway.com/letters/{name}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                b = r.read()
            if b[:4] == b"%PDF":
                return url, b
        except Exception:  # noqa: BLE001
            continue
    return None, None


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    hits = {}
    for y in YEARS:
        p = RAW / f"{y}.txt"
        if not p.exists():
            url, b = download(y)
            if not b:
                print(y, "not found")
                continue
            doc = fitz.open(stream=b, filetype="pdf")
            txt = "\n".join(page.get_text() for page in doc)
            p.write_text(f"SOURCE: {url}\n\n{txt}", encoding="utf-8")
            time.sleep(0.5)
        t = re.sub(r"\s+", " ", p.read_text(encoding="utf-8"))
        yh = []
        for k in KEYS:
            for m in re.finditer(re.escape(k), t):
                yh.append({"key": k, "pos": m.start(), "ctx": t[max(0, m.start() - 600): m.start() + 600]})
        # 合并同一位置附近的重复片段
        merged, last = [], -10_000
        for h in sorted(yh, key=lambda x: x["pos"]):
            if h["pos"] - last > 500:
                merged.append(h)
                last = h["pos"]
        hits[str(y)] = merged
        print(y, len(t), "chars;", "hits:", sorted({h["key"] for h in merged}))
    (HERE / "data" / "letters_oil_hits.json").write_text(json.dumps(hits, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
