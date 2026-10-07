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
    h1=ParagraphStyle("h1", fontName="CN", wordWrap="CJK", fontSize=17, leading=23, textColor=INK, spaceBefore=2, spaceAfter=6),
    h2=ParagraphStyle("h2", fontName="CN", wordWrap="CJK", fontSize=12.5, leading=17, textColor=INK, spaceBefore=11, spaceAfter=5),
    h3=ParagraphStyle("h3", fontName="CN", wordWrap="CJK", fontSize=10.4, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4),
    p=ParagraphStyle("p", fontName="CN", wordWrap="CJK", fontSize=8.5, leading=13, textColor=INK, spaceAfter=5),
    li=ParagraphStyle("li", fontName="CN", wordWrap="CJK", fontSize=8.5, leading=13, textColor=INK,
                      leftIndent=9, bulletIndent=2, spaceAfter=2),
    quote=ParagraphStyle("q", fontName="CN", wordWrap="CJK", fontSize=8.3, leading=12.8, textColor=INK, leftIndent=7,
                         borderPadding=(5, 5, 5, 7), backColor=SOFT, spaceAfter=6),
    code=ParagraphStyle("code", fontName="Courier", fontSize=7.6, leading=10.4, textColor=INK,
                        leftIndent=7, borderPadding=(5, 5, 5, 6), backColor=SOFT, spaceAfter=6),
    cell=ParagraphStyle("c", fontName="CN", wordWrap="CJK", fontSize=7.4, leading=10.2, textColor=INK),
    cellr=ParagraphStyle("cr", fontName="CN", wordWrap="CJK", fontSize=7.4, leading=10.2, textColor=INK, alignment=2),
)


LINK = r"\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)"  # URL may hold one level of parens (Wikipedia "X_(Y)")


def inline(t):
    """Markdown inline -> reportlab mini-HTML."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("−", "-")  # SimHei has no glyph for U+2212 (math minus) -> renders as a box
    t = t.replace("¥", "￥").replace("£", "￡")  # SimHei lacks ¥ / £; fullwidth forms render
    t = t.replace("æ", "ae").replace("Æ", "Ae")  # nor the ae ligature
    t = t.translate(str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789"))  # subscript digits (OE₀) are boxes in SimHei
    for e in ("🔴", "🟢", "🟡", "⚪", "✅", "❌", "⚠️", "⚠", "🥇", "🥈"):  # emoji only drive row_tint; SimHei draws them as boxes
        t = t.replace(e, "")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"~~(.+?)~~", r"<strike>\1</strike>", t)
    # code spans: Courier has no CJK glyphs, so spans containing non-ASCII text keep the CN font
    t = re.sub(r"`([^`]+?)`", lambda m: (f"<font face='Courier'>{m.group(1)}</font>" if m.group(1).isascii()
                                         else f"<font color='#5b6472'>{m.group(1)}</font>"), t)
    t = re.sub(LINK, lambda m: f'<link href="{m.group(2)}" color="#0b5cad">{m.group(1)}</link>', t)
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
        aligns.append("r" if j > 0 and vals and num >= max(1, len(vals) * 0.6) else "l")  # first column = labels
    # widths by content: a short column gets its natural (unwrapped) width; long-text columns share the rest
    # in proportion to (average length)^0.75. 7.4pt cell font ~ 1.42 mm per half-width unit, + padding.
    def dlen(c):
        c = re.sub(LINK, r"\1", re.sub(r"\*\*|`", "", c))
        return sum(2 if ord(ch) > 0x2E80 or ch in "–—·→" else 1 for ch in c)
    lens = [[dlen(rows[i][j]) for i in range(len(rows))] for j in range(n)]
    nat = [max(l) * 1.42 * mm + 3.5 * mm for l in lens]
    short = [nat[j] <= width * 0.22 for j in range(n)]
    fixed = sum(nat[j] for j in range(n) if short[j])
    if all(short) or fixed > width * 0.7:
        widths = [width * x / sum(nat) for x in nat]
    else:
        avg = [max(lens[j][0], sum(lens[j][1:] or lens[j]) / max(1, len(lens[j]) - 1)) ** 0.75 for j in range(n)]
        flex = sum(avg[j] for j in range(n) if not short[j])
        widths = [nat[j] if short[j] else (width - fixed) * avg[j] / flex for j in range(n)]
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
