#!/usr/bin/env python3
"""assemble_source.py — sections/*.md → report_source.md（按阅读顺序拼接）。

第 3 章与第 6 章写在同一个文件 timeline_company.md 里，按“## 6.”切开。
"""
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SEC = BASE / "sections"


def read(name):
    p = SEC / name
    return p.read_text(encoding="utf-8").strip() if p.exists() else f"<!-- 缺少 {name} -->"


tc = read("timeline_company.md")
cut = tc.index("## 6. ")
ch3 = tc[:cut].replace("<!-- PAGEBREAK -->", "").strip()
ch6 = tc[cut:].strip()

order = [read("front.md"), read("method.md"), "<!-- PAGEBREAK -->", ch3, "<!-- PAGEBREAK -->", read("layers.md"),
         "<!-- PAGEBREAK -->", ch6]
for e in ("e1", "e2", "e3", "e4", "e5a", "e5b", "e6"):
    order += ["<!-- PAGEBREAK -->", read(f"{e}.md")]
order += ["<!-- PAGEBREAK -->", read("patterns.md"), read("appendix.md")]
(BASE / "report_source.md").write_text("\n\n".join(order) + "\n", encoding="utf-8")
print("report_source.md", sum(len(x) for x in order), "chars")
