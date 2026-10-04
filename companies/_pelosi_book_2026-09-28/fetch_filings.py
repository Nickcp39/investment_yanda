#!/usr/bin/env python3
"""fetch_filings.py — 下载每家最新财报新闻稿(8-K EX-99.1)及近期重大 8-K，转成纯文本存入各 dossier 的 raw/。

一手源只从 sec.gov/Archives 取；文件名 = <提交日>_<表格>_<附件名>.txt，首行写原始 URL。
用法: python companies/_pelosi_book_2026-09-28/fetch_filings.py
"""
from __future__ import annotations

import html
import json
import re
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-09-28"
ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}

# (ticker, cik, accession, filing_date, form, label) —— 取自 SEC submissions API（2026-09-28 查询）
FILINGS = [
    ("AVGO", 1730168, "0001730168-26-000076", "2026-09-02", "8-K", "q3fy26_earnings"),
    ("AVGO", 1730168, "0001193125-26-295589", "2026-07-06", "8-K", "item801"),
    ("BE", 1664703, "0001628280-26-050150", "2026-07-28", "8-K", "q2_2026_earnings"),
    ("BE", 1664703, "0001628280-26-047734", "2026-07-09", "8-K", "item701"),
    ("BE", 1664703, "0001628280-26-024896", "2026-04-13", "8-K", "item101_302"),
    ("INTC", 50863, "0000050863-26-000155", "2026-07-23", "8-K", "q2_2026_earnings"),
    ("INTC", 50863, "0001193125-26-346806", "2026-08-12", "8-K", "item701_801"),
    ("CRWD", 1535527, "0001535527-26-000029", "2026-08-26", "8-K", "q2fy27_earnings"),
    ("VST", 1692819, "0001692819-26-000017", "2026-08-07", "8-K", "q2_2026_earnings"),
    ("VST", 1692819, "0001140361-26-037577", "2026-09-24", "8-K", "item101_801"),
    ("AB", 1109448, "0001109448-26-000194", "2026-07-28", "8-K", "q2_2026_earnings"),
    ("AB", 1109448, "0001109448-26-000278", "2026-09-10", "8-K", "aum_aug"),
    ("AB", 1109448, "0001109448-26-000281", "2026-09-25", "8-K", "item502_701"),
    ("UBER", 1543151, "0001543151-26-000027", "2026-08-05", "8-K", "q2_2026_earnings"),
    ("UBER", 1543151, "0001552781-26-000486", "2026-09-15", "8-K", "item801"),
    ("PANW", 1327567, "0001327567-26-000019", "2026-09-01", "8-K", "q4fy26_earnings"),
]


def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def to_text(raw: bytes) -> str:
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main():
    for tk, cik, acc, fdate, form, label in FILINGS:
        base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}"
        idx = json.loads(get(base + "/index.json"))
        docs = [it["name"] for it in idx["directory"]["item"] if it["name"].lower().endswith((".htm", ".html"))
                and "index" not in it["name"].lower()]
        # 优先 EX-99.1（通常文件名含 99 / ex99 / exhibit991）；否则取主文档
        ex = [n for n in docs if re.search(r"ex-?99|exhibit99|ex991|q\d.*press|pr", n, re.I)]
        targets = ex if ex else docs[:1]
        outdir = ROOT / tk.lower() / AS_OF / "raw"
        outdir.mkdir(parents=True, exist_ok=True)
        for name in targets[:3]:
            url = f"{base}/{name}"
            txt = to_text(get(url))
            fn = outdir / f"{fdate}_{form}_{label}_{Path(name).stem}.txt"
            fn.write_text(f"SOURCE: {url}\nFILED: {fdate} {form}\n\n{txt}\n", encoding="utf-8")
            print(f"{tk:5} {fdate} {name:40} -> {fn.name} ({len(txt):,} chars)")
        if not ex:
            print(f"      (no EX-99 found; saved primary doc; all docs: {docs[:6]})")
        time.sleep(0.4)


if __name__ == "__main__":
    main()
