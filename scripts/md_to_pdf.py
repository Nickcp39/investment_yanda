#!/usr/bin/env python
"""Generic Markdown -> PDF renderer for research reports (Chinese-safe, A4).

Usage:
    python scripts/md_to_pdf.py <input.md> <output.pdf> ["Footer text"]

Supports: # / ## / ### headings, GFM tables, > blockquotes, bullet lists,
fenced code blocks, **bold**, `code`, and --- rules. Deliberately small —
enough for the decision cards and research reports in this repo.
"""
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.join(REPO, ".pdf_deps"))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))

INK, MUTED, LINE = colors.HexColor("#1a1d24"), colors.HexColor("#5b6472"), colors.HexColor("#d8dee8")
SOFT, HEAD = colors.HexColor("#f4f7fb"), colors.HexColor("#eef2f8")
RED, GRN, YEL = colors.HexColor("#fdeeee"), colors.HexColor("#eaf6f3"), colors.HexColor("#fdf6e8")

ss = getSampleStyleSheet()
S = dict(
    h1=ParagraphStyle("h1", fontName="CN", fontSize=17, leading=23, textColor=INK, spaceBefore=2, spaceAfter=6),
    h2=ParagraphStyle("h2", fontName="CN", fontSize=12.5, leading=17, textColor=INK, spaceBefore=11, spaceAfter=5),
    h3=ParagraphStyle("h3", fontName="CN", fontSize=10.4, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4),
    p=ParagraphStyle("p", fontName="CN", fontSize=8.5, leading=13, textColor=INK, spaceAfter=5),
    li=ParagraphStyle("li", fontName="CN", fontSize=8.5, leading=13, textColor=INK,
                      leftIndent=9, bulletIndent=2, spaceAfter=2),
    quote=ParagraphStyle("q", fontName="CN", fontSize=8.3, leading=12.8, textColor=INK, leftIndent=7,
                         borderPadding=(5, 5, 5, 7), backColor=SOFT, spaceAfter=6),
    code=ParagraphStyle("code", fontName="Courier", fontSize=7.6, leading=10.4, textColor=INK,
                        leftIndent=7, borderPadding=(5, 5, 5, 6), backColor=SOFT, spaceAfter=6),
    cell=ParagraphStyle("c", fontName="CN", fontSize=7.4, leading=10.2, textColor=INK),
    cellr=ParagraphStyle("cr", fontName="CN", fontSize=7.4, leading=10.2, textColor=INK, alignment=2),
)


def inline(t):
    """Markdown inline -> reportlab mini-HTML."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"~~(.+?)~~", r"<strike>\1</strike>", t)
    t = re.sub(r"`([^`]+?)`", r"<font face='Courier'>\1</font>", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t


def row_tint(cells):
    """Tint a table row by the status emoji it carries."""
    j = " ".join(cells)
    if "🔴" in j or "❌" in j:
        return RED
    if "✅" in j or "🥇" in j:
        return GRN
    if "⚠️" in j or "🟡" in j or "🥈" in j:
        return YEL
    return None


def build_table(block, width):
    rows = []
    for ln in block:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return None
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    # right-align columns that are mostly numeric
    aligns = []
    for j in range(n):
        vals = [rows[i][j] for i in range(1, len(rows))]
        num = sum(1 for v in vals if re.search(r"[\d,.]{2,}", v) and not re.search(r"[\u4e00-\u9fff]{3,}", v))
        aligns.append("r" if vals and num >= max(1, len(vals) * 0.6) else "l")
    # widths: first column wider, rest even
    first = min(width * 0.34, max(22 * mm, width / n * 1.5))
    rest = (width - first) / (n - 1) if n > 1 else width
    widths = [first] + [rest] * (n - 1)
    data = [[Paragraph(inline(c), S["cellr"] if (i and aligns[j] == "r") else S["cell"])
             for j, c in enumerate(r)] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [("BACKGROUND", (0, 0), (-1, 0), HEAD), ("GRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    for i in range(1, len(rows)):
        c = row_tint(rows[i])
        if c:
            cmds.append(("BACKGROUND", (0, i), (-1, i), c))
    t.setStyle(TableStyle(cmds))
    return t


def render(md, width):
    out, i, lines = [], 0, md.split("\n")
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s or set(s) <= set("-—_*") and len(s) >= 3:
            i += 1
            continue
        if s.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i].replace(" ", "&nbsp;"))
                i += 1
            i += 1
            out.append(Paragraph("<br/>".join(buf), S["code"]))
            continue
        if s.startswith("|"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i])
                i += 1
            t = build_table(buf, width)
            if t:
                out += [t, Spacer(1, 5)]
            continue
        if s.startswith(">"):
            buf = []
            while i < len(lines) and (lines[i].strip().startswith(">") or
                                      (buf and lines[i].strip().startswith("|"))):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = [x for x in buf if x.strip() and not x.strip().startswith("|")]
            if inner:
                out.append(Paragraph("<br/>".join(inline(x) for x in inner), S["quote"]))
            tb = [x for x in buf if x.strip().startswith("|")]
            if tb:
                t = build_table(tb, width)
                if t:
                    out += [t, Spacer(1, 5)]
            continue
        m = re.match(r"^!\[[^\]]*\]\(([^)]+)\)", s)
        if m:
            src = m.group(1)
            path = src if os.path.isabs(src) else os.path.join(os.path.dirname(os.path.abspath(SRC_PATH)), src)
            if os.path.exists(path):
                from reportlab.lib.utils import ImageReader
                iw, ih = ImageReader(path).getSize()
                w = min(width, 170 * mm); h = w * ih / iw
                out += [Image(path, width=w, height=h), Spacer(1, 6)]
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            lvl = min(len(m.group(1)), 3)
            out.append(Paragraph(inline(m.group(2)), S["h%d" % lvl]))
            i += 1
            continue
        m = re.match(r"^[-*+]\s+(.*)", s) or re.match(r"^(\d+)\.\s+(.*)", s)
        if m:
            txt = m.group(m.lastindex)
            bullet = "•" if not s[0].isdigit() else s.split(".")[0] + "."
            out.append(Paragraph(inline(txt), S["li"], bulletText=bullet))
            i += 1
            continue
        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^([#>|`]|[-*+]\s|\d+\.\s)", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        out.append(Paragraph(inline(" ".join(buf)), S["p"]))
    return out


SRC_PATH = None


def main():
    global SRC_PATH
    src, dst = sys.argv[1], sys.argv[2]
    SRC_PATH = src
    foot = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(src)
    md = open(src, encoding="utf-8").read()
    title = next((l.lstrip("# ").strip() for l in md.split("\n") if l.startswith("# ")), foot)
    W = A4[0] - 36 * mm

    def footer(c, d):
        c.saveState(); c.setFont("CN", 7); c.setFillColor(MUTED)
        c.drawString(18 * mm, 11 * mm, foot)
        c.drawRightString(A4[0] - 18 * mm, 11 * mm, "第 %d 页" % d.page)
        c.setStrokeColor(LINE); c.line(18 * mm, 14.5 * mm, A4[0] - 18 * mm, 14.5 * mm)
        c.restoreState()

    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    SimpleDocTemplate(dst, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                      topMargin=16 * mm, bottomMargin=18 * mm, title=title, author="yc_research"
                      ).build(render(md, W), onFirstPage=footer, onLaterPages=footer)
    print("PDF ->", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
