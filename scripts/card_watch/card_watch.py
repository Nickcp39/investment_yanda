#!/usr/bin/env python3
"""card_watch.py — 把仓库里每家公司最新一张 decision_card 的买入线，和今天的价格放在一起看。

它只回答一个问题：**哪些卡的价格已经到了线下、或者快到了，需要重跑一次卡。**
它不回答"能不能买"：价格过线 ≠ 可执行入场（C4）。裁决上限、完整度、Checker≠Runner、卡的年龄，都不在价格里。

用法：
    python scripts/card_watch/card_watch.py            # 抓价、写 out/card_watch_<日期>.md / .csv、打印摘要
    python scripts/card_watch/card_watch.py --no-fetch # 只读卡不抓价（检查解析）

数据：
    买入线：companies/<folder>/<最新日期>/decision_card.json 的 buy_below_price 或 buy_below；
            没有 JSON 或 JSON 缺线时，退回 decision_card.md 里第一行含 buy_below / buy-below 的 $数字（来源标 md）。
    价格：  Yahoo chart API（regularMarketPrice，本币）。非美股代码按卡里的 ticker 映射（.SH→.SS，"A / B" 取第一个）。
    例外：  overrides.json（同目录，可选）—— {"<folder>": {"symbol": ..., "buy_below": ..., "note": ...}}
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
COMPANIES = ROOT / "companies"
OUT = HERE / "out"
UA = {"User-Agent": "Mozilla/5.0"}
STALE_DAYS = 90        # 超过这个天数的卡，线本身可能已经过时
NEAR_PCT = 10.0        # 现价高于线 ≤10% 算"快到了"


def latest_dated(folder: Path):
    ds = sorted(d for d in os.listdir(folder) if re.match(r"\d{4}-\d{2}-\d{2}", d) and (folder / d).is_dir())
    return ds[-1] if ds else None


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    m = re.search(r"[\d,]+(?:\.\d+)?", str(x))
    return float(m.group(0).replace(",", "")) if m else None


def md_buy_below(md: Path):
    """退路：decision_card.md 里第一行含 buy_below / buy-below 的第一个 $数字。"""
    if not md.exists():
        return None, ""
    for line in md.read_text(encoding="utf-8", errors="ignore").splitlines():
        if re.search(r"buy[_-]below", line, re.I):
            m = re.search(r"\$\s*~?\s*([\d,]+(?:\.\d+)?)", line)
            if m:
                return float(m.group(1).replace(",", "")), line.strip()[:160]
    return None, ""


def to_yahoo(ticker: str) -> str:
    t = ticker.split("/")[0].strip()
    if t.endswith(".SH"):
        t = t[:-3] + ".SS"
    return t


def load_cards():
    overrides = {}
    op = HERE / "overrides.json"
    if op.exists():
        overrides = json.loads(op.read_text(encoding="utf-8"))
    cards = []
    for folder in sorted(os.listdir(COMPANIES)):
        p = COMPANIES / folder
        if not p.is_dir() or folder.startswith("_"):
            continue
        d = latest_dated(p)
        if not d:
            continue
        jp, mp = p / d / "decision_card.json", p / d / "decision_card.md"
        c = {}
        if jp.exists():
            try:
                c = json.loads(jp.read_text(encoding="utf-8"))
            except Exception as ex:  # noqa: BLE001
                c = {"_err": str(ex)[:60]}
        ov = overrides.get(folder, {})
        ticker = ov.get("symbol") or c.get("ticker") or folder.upper()
        bb = num(ov.get("buy_below")) if "buy_below" in ov else num(c.get("buy_below_price", c.get("buy_below")))
        src = "override" if "buy_below" in ov else ("json" if bb is not None else "")
        note = ov.get("note", "")
        if bb is None:
            bb, line = md_buy_below(mp)
            if bb is not None:
                src = "md"
                note = (note + " " if note else "") + "md: " + line
        as_of = c.get("as_of") or c.get("as_of_date") or d
        cards.append({
            "folder": folder, "ticker": ticker, "symbol": to_yahoo(ticker), "card_date": d, "as_of": str(as_of)[:10],
            "verdict": c.get("new_money_verdict") or c.get("verdict") or "", "completeness": c.get("completeness_pct", ""),
            "card_price": num(c.get("as_of_price")), "currency": c.get("currency") or "", "buy_below": bb, "bb_source": src,
            "note": note, "has_json": jp.exists(), "has_md": mp.exists(),
        })
    # 同一代码多个文件夹（如 gehc / ge_healthcare）只留最新
    best = {}
    for c in cards:
        k = c["symbol"]
        if k not in best or c["card_date"] > best[k]["card_date"]:
            if k in best:
                c["note"] = (c["note"] + " " if c["note"] else "") + f"替代旧文件夹 {best[k]['folder']}/{best[k]['card_date']}"
            best[k] = c
        else:
            best[k]["note"] = (best[k]["note"] + " " if best[k]["note"] else "") + f"替代旧文件夹 {c['folder']}/{c['card_date']}"
    return sorted(best.values(), key=lambda x: x["symbol"])


def fetch_price(symbol: str):
    hosts = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
    err = ""
    for attempt in range(3):
        url = f"https://{hosts[attempt % 2]}/v8/finance/chart/{symbol}?range=5d&interval=1d"
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20))["chart"]["result"][0]
            m = d["meta"]
            ts = m.get("regularMarketTime")
            return {"price": m.get("regularMarketPrice"), "ccy": m.get("currency"),
                    "time": dt.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%MZ") if ts else ""}
        except Exception as ex:  # noqa: BLE001
            err = str(ex)[:60]
            time.sleep(1.5 * (attempt + 1))
    return {"price": None, "ccy": "", "time": "", "err": err}


SEC_UA = {"User-Agent": "YandaResearchLab/1.0 (contact: admin@yanda-research-lab.example)", "Accept-Encoding": "identity"}
SEC_FORMS = {"10-Q", "10-K", "20-F", "40-F"}   # 季报 / 年报；6-K 太频繁不算


def sec_ticker_map():
    """SEC 官方 ticker → CIK 表（约 1MB，每次下载）。失败返回空 dict，后面只按卡龄判断。"""
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request("https://www.sec.gov/files/company_tickers.json", headers=SEC_UA), timeout=30))
        return {v["ticker"].upper(): f"{int(v['cik_str']):010d}" for v in d.values()}
    except Exception as ex:  # noqa: BLE001
        print("SEC ticker map failed:", str(ex)[:80])
        return {}


def sec_new_filing(cik: str, as_of: str):
    """卡 as_of 之后有没有新的 10-Q / 10-K / 20-F / 40-F。返回 'form date' 或 ''。"""
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/submissions/CIK{cik}.json", headers=SEC_UA), timeout=30))
        r = d["filings"]["recent"]
        hits = [(r["filingDate"][i], r["form"][i]) for i in range(len(r["form"])) if r["form"][i] in SEC_FORMS and r["filingDate"][i] > as_of]
        if hits:
            dte, form = max(hits)
            return f"{form} {dte}"
        return ""
    except Exception as ex:  # noqa: BLE001
        return "ERR " + str(ex)[:40]


def classify(c, today):
    p, bb = c.get("price"), c.get("buy_below")
    if p is None:
        return "D", None
    if bb is None:
        return "D", None
    pct = (p / bb - 1) * 100
    if pct <= 0:
        return "A", pct
    if pct <= NEAR_PCT:
        return "B", pct
    return "C", pct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--no-sec", action="store_true", help="不查 SEC 新财报，只按卡龄判断是否重跑")
    a = ap.parse_args()
    today = dt.date.today()
    cards = load_cards()
    print(f"cards: {len(cards)} (latest folder per symbol)")
    if not a.no_fetch:
        for i, c in enumerate(cards, 1):
            q = fetch_price(c["symbol"])
            c.update(price=q["price"], yccy=q["ccy"], ptime=q["time"], err=q.get("err", ""))
            print(f"  {i:2d}/{len(cards)} {c['symbol']:<12} {q['price']}", flush=True)
    else:
        for c in cards:
            c.update(price=None, yccy="", ptime="", err="")
    # 财报后 / 超过一季度 → 提示重跑
    tmap = {} if (a.no_sec or a.no_fetch) else sec_ticker_map()
    for c in cards:
        c["age_days"] = (today - dt.date.fromisoformat(c["as_of"])).days if re.match(r"\d{4}-\d{2}-\d{2}$", c["as_of"]) else None
        c["cik"] = tmap.get(c["symbol"].upper(), "") if "." not in c["symbol"] else ""
        c["new_filing"] = sec_new_filing(c["cik"], c["as_of"]) if c["cik"] else ""
        if c["cik"]:
            time.sleep(0.12)
        if c["new_filing"] and not c["new_filing"].startswith("ERR"):
            c["rerun"] = f"财报后（{c['new_filing']}）"
        elif c["age_days"] is not None and c["age_days"] > STALE_DAYS:
            c["rerun"] = f"超过一季度（{c['age_days']} 天" + ("，未查到新财报）" if c["cik"] else "，非 SEC 申报或无 CIK）")
        else:
            c["rerun"] = ""
    for c in cards:
        c["group"], c["pct_vs_line"] = classify(c, today)
        c["pct_since_card"] = (c["price"] / c["card_price"] - 1) * 100 if (c.get("price") and c.get("card_price")) else None
        flags = []
        if c["group"] == "A" and c.get("card_price") and c["buy_below"] and c["card_price"] > c["buy_below"]:
            flags.append("新过线（写卡时在线上）")
        if c["age_days"] is not None and c["age_days"] > STALE_DAYS:
            flags.append(f"旧卡 {c['age_days']}d")
        if c["currency"] and c.get("yccy") and c["currency"].upper() != str(c["yccy"]).upper().replace("GBP", "GBP"):
            if not (c["currency"].upper() == "GBP" and str(c["yccy"]).lower() == "gbp"):
                flags.append(f"币种 卡{c['currency']}/Yahoo{c['yccy']}")
        if c["bb_source"] == "md":
            flags.append("线来自 md")
        if c.get("err"):
            flags.append("抓价失败 " + c["err"])
        if not c["has_json"]:
            flags.append("无 json")
        c["flags"] = "；".join(flags)

    OUT.mkdir(exist_ok=True)
    stamp = today.isoformat()
    csv_path = OUT / f"card_watch_{stamp}.csv"
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["group", "folder", "symbol", "card_date", "as_of", "age_days", "verdict", "completeness", "currency",
                    "buy_below", "bb_source", "card_price", "price", "yahoo_ccy", "price_time", "pct_vs_line", "pct_since_card",
                    "rerun", "new_filing", "cik", "flags", "note"])
        for c in cards:
            w.writerow([c["group"], c["folder"], c["symbol"], c["card_date"], c["as_of"], c["age_days"], c["verdict"], c["completeness"],
                        c["currency"], c["buy_below"], c["bb_source"], c["card_price"], c.get("price"), c.get("yccy"), c.get("ptime"),
                        None if c["pct_vs_line"] is None else round(c["pct_vs_line"], 1),
                        None if c["pct_since_card"] is None else round(c["pct_since_card"], 1),
                        c["rerun"], c["new_filing"], c["cik"], c["flags"], c["note"]])

    titles = {"A": "A. 现价已在买入线之下（或带内）—— 需要重跑卡，不是买入信号",
              "B": f"B. 现价高于线 ≤{NEAR_PCT:.0f}% —— 快到了",
              "C": f"C. 现价高于线 >{NEAR_PCT:.0f}%",
              "D": "D. 没有买入线 / 抓不到价"}
    md = [f"# 卡片价格巡检 · {stamp}", "",
          f"读取 `companies/<folder>/<最新日期>/decision_card.json|md` 共 {len(cards)} 家（同一代码只留最新文件夹）；价格 = Yahoo 本币即时价（抓取时间见表）。",
          "",
          "> **规矩**：① 价格过线 ≠ 可执行入场（C4）。每张卡的裁决上限由完整度决定，runner 提议的 STARTER 在独立 Checker 之前一律 WATCH；"
          "② 本表**不按距线远近排名**，组内按代码字母序；③ 卡龄 > 90 天的线可能已过时，先重跑再看；④ 非美股按本币比较，币种不一致的行已标出。",
          ""]
    rr = [c for c in cards if c["rerun"]]
    md += [f"## 需要重跑的卡（财报后 / 超过一季度）（{len(rr)}）", "",
           "美股按 SEC 申报判断：卡 as_of 之后出了 10-Q / 10-K / 20-F 就该重跑；非美股或查不到 CIK 的按卡龄 > 90 天。", ""]
    if rr:
        md += ["| 公司 | 代码 | 卡 as_of | 卡龄 | 原因 | 价格组 | 现价/线 |", "|---|---|---|---:|---|:--:|---:|"]
        for c in rr:
            pl = "" if c["pct_vs_line"] is None else f"{c['pct_vs_line']:+.1f}%"
            md.append(f"| {c['folder']} | {c['symbol']} | {c['as_of']} | {c['age_days']} | {c['rerun']} | {c['group']} | {pl} |")
        md.append("")
    else:
        md += ["（无）", ""]
    for g in "ABCD":
        rows = [c for c in cards if c["group"] == g]
        md += [f"## {titles[g]}（{len(rows)}）", ""]
        if not rows:
            md += ["（无）", ""]
            continue
        md += ["| 公司 | 代码 | 卡 as_of | 卡龄 | 裁决 | 完整度 | 买入线 | 现价 | 现价/线 | 自卡以来 | 标记 |", "|---|---|---|---:|---|---:|---:|---:|---:|---:|---|"]
        for c in rows:
            md.append("| {f} | {s} | {d} | {age} | {v} | {cp} | {bb} | {p} | {pl} | {pc} | {fl} |".format(
                f=c["folder"], s=c["symbol"], d=c["as_of"], age=c["age_days"] if c["age_days"] is not None else "",
                v=c["verdict"], cp=f"{c['completeness']}%" if c["completeness"] != "" else "",
                bb="" if c["buy_below"] is None else f"{c['buy_below']:,.2f}",
                p="" if c.get("price") is None else f"{c['price']:,.2f}",
                pl="" if c["pct_vs_line"] is None else f"{c['pct_vs_line']:+.1f}%",
                pc="" if c["pct_since_card"] is None else f"{c['pct_since_card']:+.1f}%",
                fl=c["flags"]))
        md.append("")
    md_path = OUT / f"card_watch_{stamp}.md"
    md_path.write_text("\n".join(md), encoding="utf-8")
    print()
    print("需要重跑（财报后 / 超过一季度）", len(rr))
    for c in rr:
        print(f"   {c['symbol']:<12} {c['as_of']}  {c['rerun']}")
    for g in "ABCD":
        rows = [c for c in cards if c["group"] == g]
        print(titles[g], len(rows))
        if g in "AB":
            for c in rows:
                print(f"   {c['symbol']:<12} line {c['buy_below']:>10,.2f}  now {c['price']:>10,.2f}  {c['pct_vs_line']:+6.1f}%  {c['verdict']:<10} {c['flags']}")
    print(f"\nwrote {md_path}\n      {csv_path}")


if __name__ == "__main__":
    main()
