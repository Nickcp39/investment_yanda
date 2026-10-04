#!/usr/bin/env python3
"""fetch_filings.py — 下载各公司一手财报原文到 dossier raw/，并用 PyMuPDF 抽成 .txt 本地检索（吸取 UBER 教训：不依赖摘要工具）。

日本：決算短信（FY3/2026 全年 + FY3/2027 Q1），来源 = 公司官网；东电官网对脚本返回 403，改用雅虎日本金融的 TDnet 镜像（同一份适时披露 PDF）。
英国：National Grid = SEC EDGAR（6-K 全年业绩公告 + 20-F 年报）；SSE = 公司官网全年业绩 PDF + Q1 交易声明网页。
中国：A 股 = 巨潮资讯（cninfo）年报 / 半年报原文；H 股 = 港交所披露易（hkexnews）中文公告；个别镜像（雪球 / 阿思达克）为同一份交易所文件。
只保存 .txt（PDF 不入库）；PDF 依次用 pdfplumber → pdftotext -layout → PyMuPDF 抽取。
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".pdf_deps"))
import fitz  # noqa: E402  PyMuPDF

AS_OF = "2026-10-03"
ROOT = Path(__file__).resolve().parents[1]
WEB = {"User-Agent": "Mozilla/5.0"}
SEC = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
YJ = "https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure"
NG = "https://www.sec.gov/Archives/edgar/data/1004315"

DOCS = {  # folder: [(文件名, url, headers)]
    "tepco": [("2026-04-30_tanshin_FY3-2026", f"{YJ}/20260430/20260427512236.pdf", WEB),
              ("2026-07-29_tanshin_Q1_FY3-2027", f"{YJ}/20260729/20260724599600.pdf", WEB)],
    "kansai": [("2026-04-30_tanshin_FY3-2026", "https://www.kepco.co.jp/ir/brief/disclosure/pdf/kaiji20260430_1.pdf", WEB),
               ("2026-07-31_tanshin_Q1_FY3-2027", "https://www.kepco.co.jp/ir/brief/disclosure/pdf/kaiji20260731_1.pdf", WEB)],
    "kyushu": [("2026-04-30_tanshin_FY3-2026", "https://www.kyuden.co.jp/var/rev0/0842/4374/0Oebsb62.pdf", WEB),
               ("2026-07-31_tanshin_Q1_FY3-2027_a", "https://www.kyuden.co.jp/var/rev0/0888/5399/ms6vNzB3.pdf", WEB),
               ("2026-07-31_tanshin_Q1_FY3-2027_b", "https://www.kyuden.co.jp/var/rev0/0888/5400/fbYEeqt2.pdf", WEB),
               ("2026-07-31_tanshin_Q1_FY3-2027_c", "https://www.kyuden.co.jp/var/rev0/0888/5401/6BsZ4Gi3.pdf", WEB),
               ("2026-03-26_holding_company_share_transfer_plan_EN", "https://www.fse.or.jp/files/lis_tkj/26032695084.pdf", WEB)],
    "jpower": [("2026-04-30_tanshin_FY3-2026", "https://www.jpower.co.jp/news/pdf/kessan2026-4/all.pdf", WEB),
               ("2026-05-12_presentation_FY3-2026", "https://www.jpower.co.jp/ir/pdf/260512presentation_1.pdf", WEB),
               ("2026-07-31_tanshin_Q1_FY3-2027", "https://www.jpower.co.jp/news/pdf/kessan2027-1/all.pdf", WEB)],
    "nationalgrid": [("2026-05-14_6-K_FY2026_results", f"{NG}/000165495426004849/a2416e.htm", SEC),
                     ("2026-06-03_20-F_FY2026", f"{NG}/000100431526000006/nggtf-20260331.htm", SEC),
                     ("2026-08-03_6-K_operating_model", f"{NG}/000165495426007117/a8707o.htm", SEC),
                     ("2026-07-23_6-K_total_voting_rights", f"{NG}/000165495426006813/a6117n.htm", SEC)],
    "sse": [("2026-05-28_FY26_results", "https://www.sse.com/media/jjzbfm1e/fy26-full-year-results-statement-vfinal2.pdf", WEB),
            ("2026-07-16_Q1_trading_statement", "https://www.sse.com/news-and-views/2026/07/sse-has-published-its-q1-trading-statement/", WEB)],
    "cypc": [("2026-04-30_annual_report_2025_summary", "https://static.cninfo.com.cn/finalpage/2026-04-30/1225262042.PDF", WEB),
             ("2026-04-30_annual_report_2025_full", "https://static.cninfo.com.cn/finalpage/2026-04-30/1225262036.PDF", WEB),
             ("2026-08-30_interim_report_2026_summary", "http://dataclouds.cninfo.com.cn/shgonggao/hsomarket/2026/20260830/550f09b5470c45d9ac6240951d9f70fb.PDF", WEB),
             ("2026-08-30_interim_report_2026_full", "http://dataclouds.cninfo.com.cn/shgonggao/hsomarket/2026/20260830/ee373d6d0d9347cdb810847c08bf39f7.PDF", WEB)],
    "cgnpower": [("2026-03-26_annual_report_2025_summary_A", "http://static.cninfo.com.cn/finalpage/2026-03-26/1225030277.PDF", WEB),
                 ("2026-03-25_annual_results_2025_hkex", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032501034_c.pdf", WEB),
                 ("2026-08-25_interim_results_2026_hkex", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0825/2026082500980_c.pdf", WEB),
                 ("2026-08-25_interim_report_2026_A_full_via_hkex", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0825/2026082501294_c.pdf", WEB)],
    "huaneng": [("2026-03-25_annual_report_2025_full", "https://cniis.aastocks.com/CNSESH_STOCK/2026/2026-3/2026-03-25/12015930.pdf", WEB),
                ("2026-08-19_interim_report_2026_full", "https://stockmc.xueqiu.com/202608/600011_20260819_APXK.pdf", WEB)],
    # 港股公告链接由港交所披露易标题检索（titleSearchServlet，stockId 6732 / 115406 / 2131）确认，不用搜索引擎结果
    "crpower": [("2026-03-18_annual_results_2025_hkex", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800238_c.pdf", WEB),
                ("2026-08-26_interim_results_2026_hkex", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600196_c.pdf", WEB)],
}


def get(url, headers):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def to_text(b: bytes) -> str:
    if b[:4] == b"%PDF":
        # 首选 pdfplumber（日文決算短信的现金流量表只有它能保持"科目 + 两期数字"同一行）；
        # 其次 pdftotext -layout；最后 PyMuPDF
        try:
            import io
            import pdfplumber
            with pdfplumber.open(io.BytesIO(b)) as pdf:
                pages = [f"\n=== page {i + 1} ===\n" + (p.extract_text() or "") for i, p in enumerate(pdf.pages)]
            if sum(len(x) for x in pages) > 500:
                return "\n".join(pages)
        except Exception:  # noqa: BLE001
            pass
        with tempfile.TemporaryDirectory() as td:
            pdf = Path(td) / "x.pdf"
            pdf.write_bytes(b)
            try:
                r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, timeout=180)
                if r.returncode == 0 and len(r.stdout) > 500:
                    return r.stdout.decode("utf-8", "replace").replace("\f", "\n=== page break ===\n")
            except (OSError, subprocess.TimeoutExpired):
                pass
        with fitz.open(stream=b, filetype="pdf") as doc:
            return "\n".join(f"\n=== page {i + 1} ===\n" + p.get_text() for i, p in enumerate(doc))
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[ \t\xa0]+", " ", re.sub(r"\n\s*\n+", "\n", t))


def main():
    only = set(sys.argv[1:])
    for folder, docs in DOCS.items():
        if only and folder not in only:
            continue
        raw = ROOT / folder / AS_OF / "raw"
        raw.mkdir(parents=True, exist_ok=True)
        for name, url, hd in docs:
            out = raw / f"{name}.txt"
            if out.exists():
                print("skip", out.name)
                continue
            try:
                txt = to_text(get(url, hd))
            except Exception as e:  # noqa: BLE001
                print("FAIL", folder, name, str(e)[:100])
                continue
            out.write_text(f"SOURCE: {url}\nFETCHED: {AS_OF}\n\n{txt}", encoding="utf-8")
            print(f"{folder:13} {name:38} {len(txt):>9,} chars")
            time.sleep(0.6)


if __name__ == "__main__":
    main()
