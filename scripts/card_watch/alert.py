#!/usr/bin/env python3
"""alert.py — 把 card_watch 的当天结果和上一次的状态比，决定要不要"发邮件"。

发邮件的方式：GitHub Actions 开一个 Issue 并指派给仓库所有者，GitHub 自己把 Issue 内容邮件发到所有者的通知邮箱。
本脚本只负责两件事：
  1. 比较今天的 A/B 组和 state.json 里上一次的 A/B 组，算出"新到线"（进 A）、"离线"（出 A）、"快到线"（进 B）；
  2. 写 out/alert_title.txt + out/alert_body.md，并把 alert=true/false 写进 $GITHUB_OUTPUT。
触发规则：有卡**新进 A 组**就发；每周一发一次全表周报（DIGEST=1 也可强制）。其余日子不发。

用法：
    python scripts/card_watch/alert.py          # 正常比较
    python scripts/card_watch/alert.py --seed   # 只把今天的 A/B 写进 state.json，不发（首次部署用）
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
STATE = HERE / "state.json"


def latest_csv():
    fs = sorted(OUT.glob("card_watch_*.csv"))
    if not fs:
        sys.exit("no card_watch_*.csv in out/ — run card_watch.py first")
    return fs[-1]


def load_rows(p: Path):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def fmt(v, nd=2):
    try:
        return f"{float(v):,.{nd}f}"
    except (TypeError, ValueError):
        return v or ""


def row_line(r):
    pct = r.get("pct_vs_line") or ""
    pct = f"{float(pct):+.1f}%" if pct not in ("", None) else ""
    return (f"| {r['folder']} | {r['symbol']} | {r['as_of']} | {r['age_days']} | {r['verdict']} | "
            f"{(r['completeness'] + '%') if r['completeness'] else ''} | {fmt(r['buy_below'])} | {fmt(r['price'])} | {pct} | {r['flags']} |")


HDR = ["| 公司 | 代码 | 卡 as_of | 卡龄 | 裁决 | 完整度 | 买入线 | 现价 | 现价/线 | 标记 |",
       "|---|---|---|---:|---|---:|---:|---:|---:|---|"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--digest", action="store_true")
    a = ap.parse_args()
    today = dt.date.today()
    p = latest_csv()
    rows = load_rows(p)
    date = p.stem.replace("card_watch_", "")
    by = {r["symbol"]: r for r in rows}
    A = sorted(r["symbol"] for r in rows if r["group"] == "A")
    B = sorted(r["symbol"] for r in rows if r["group"] == "B")
    fetched = sum(1 for r in rows if r.get("price"))
    if fetched < len(rows) * 0.5:
        sys.exit(f"only {fetched}/{len(rows)} prices fetched — not trusting this run")

    prev = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"A": [], "B": []}
    new_state = {"A": A, "B": B, "updated": date, "cards": len(rows)}
    if a.seed:
        STATE.write_text(json.dumps(new_state, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"seeded state.json: A={len(A)} B={len(B)} from {p.name}")
        return

    entered_A = [s for s in A if s not in prev["A"]]
    exited_A = [s for s in prev["A"] if s not in A]
    entered_B = [s for s in B if s not in prev["B"] and s not in prev["A"]]
    digest = a.digest or os.environ.get("DIGEST") == "1" or today.weekday() == 0
    alert = bool(entered_A) or digest

    title = (f"卡片巡检 {date}：{len(entered_A)} 张新到买入线" if entered_A
             else f"卡片巡检周报 {date}：A 组 {len(A)} 张、B 组 {len(B)} 张")
    body = [f"# 卡片巡检 · {date}", "",
            "> 价格过线 ≠ 可执行入场（C4）：裁决上限由完整度决定，runner 提议的 STARTER 在独立 Checker 之前一律 WATCH。"
            "这封信只说明**哪些卡要重跑**。组内按代码排序，不按距线远近排名。卡龄 > 90 天的线可能已过时。", ""]
    if entered_A:
        body += [f"## 新到买入线（{len(entered_A)}）—— 上次巡检还在线上，今天在线下", ""] + HDR + [row_line(by[s]) for s in entered_A] + [""]
    if exited_A:
        body += [f"## 离开线下（{len(exited_A)}）—— 上次在线下，今天涨回线上", "", "、".join(exited_A), ""]
    if entered_B:
        body += [f"## 新进入 10% 以内（{len(entered_B)}）", ""] + HDR + [row_line(by[s]) for s in entered_B] + [""]
    if digest:
        body += [f"## 全表 · A 组（现价 ≤ 线，{len(A)}）", ""] + HDR + [row_line(by[s]) for s in A] + [""]
        body += [f"## 全表 · B 组（高于线 ≤10%，{len(B)}）", ""] + HDR + [row_line(by[s]) for s in B] + [""]
    body += ["---", f"共 {len(rows)} 张卡，抓到价格 {fetched} 张。完整表：本仓库 `run_card_watch.bat`，或本次 Actions 运行的 artifact。"]

    OUT.mkdir(exist_ok=True)
    (OUT / "alert_title.txt").write_text(title, encoding="utf-8")
    (OUT / "alert_body.md").write_text("\n".join(body), encoding="utf-8")
    STATE.write_text(json.dumps(new_state, ensure_ascii=False, indent=1), encoding="utf-8")
    gh = os.environ.get("GITHUB_OUTPUT")
    if gh:
        with open(gh, "a", encoding="utf-8") as f:
            f.write(f"alert={'true' if alert else 'false'}\ntitle={title}\n")
    print(f"alert={alert} entered_A={entered_A} exited_A={exited_A} entered_B={entered_B} digest={digest}")


if __name__ == "__main__":
    main()
