#!/usr/bin/env python3
"""render_pdf.py — report.md → PDF（中文 YaHei，A4；来源链接可点击，## 章节生成书签）。

改编自 studies/铲子百年实证_2026-09-23/scripts/render_pdf.py：表格列宽按内容自动分配，支持编号列表、
<!-- PAGEBREAK -->、“来源：/注：”开头的段落用小字说明样式。
用法：python scripts/render_pdf.py   →  <study>/美股风气40年_兴衰统计_2026-10-06.pdf
"""
import html
import json
import pathlib
import re

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Frame, Image, KeepTogether, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

BASE = pathlib.Path(__file__).resolve().parents[1]
NAME = BASE.name
OUT = BASE / f"{NAME}.pdf"
pdfmetrics.registerFont(TTFont("CN", "C:/Windows/Fonts/msyh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("CNBold", "C:/Windows/Fonts/msyhbd.ttc", subfontIndex=0))
pdfmetrics.registerFontFamily("CN", normal="CN", bold="CNBold", italic="CN", boldItalic="CNBold")
ink, blue, muted = colors.HexColor("#202c39"), colors.HexColor("#235e7c"), colors.HexColor("#5e6b76")
line, soft = colors.HexColor("#cdd8e0"), colors.HexColor("#edf3f7")
W, H = A4
M = 17 * mm
WIDTH = W - 2 * M
st = {
    "p": ParagraphStyle("body", fontName="CN", fontSize=9.0, leading=14.0, textColor=ink, spaceAfter=6, wordWrap="CJK"),
    "li": ParagraphStyle("li", fontName="CN", fontSize=9.0, leading=14.0, textColor=ink, spaceAfter=3, wordWrap="CJK",
                         leftIndent=11, bulletIndent=1),
    "h1": ParagraphStyle("title", fontName="CNBold", fontSize=26, leading=34, textColor=blue, spaceBefore=26,
                         spaceAfter=14, wordWrap="CJK", keepWithNext=1),
    "h2": ParagraphStyle("section", fontName="CNBold", fontSize=14, leading=20, textColor=blue, spaceBefore=14,
                         spaceAfter=8, wordWrap="CJK", keepWithNext=1),
    "h3": ParagraphStyle("subsection", fontName="CNBold", fontSize=10.6, leading=15.5, textColor=ink, spaceBefore=9,
                         spaceAfter=5, wordWrap="CJK", keepWithNext=1),
    "cell": ParagraphStyle("cell", fontName="CN", fontSize=7.6, leading=10.8, textColor=ink, wordWrap="CJK"),
    "cellr": ParagraphStyle("num", fontName="CN", fontSize=7.6, leading=10.8, textColor=ink, wordWrap="CJK", alignment=2),
    "head": ParagraphStyle("head", fontName="CNBold", fontSize=7.6, leading=10.8, textColor=blue, wordWrap="CJK"),
    "caption": ParagraphStyle("caption", fontName="CN", fontSize=7.6, leading=11.4, textColor=muted, spaceAfter=7,
                              wordWrap="CJK"),
    "code": ParagraphStyle("code", fontName="Courier", fontSize=7.6, leading=11, textColor=ink, leftIndent=6,
                           borderPadding=6, backColor=soft, spaceAfter=8, spaceBefore=3),
    "quote": ParagraphStyle("quote", fontName="CN", fontSize=9.0, leading=14, textColor=blue, leftIndent=8,
                            borderPadding=7, backColor=soft, spaceAfter=9, spaceBefore=3, wordWrap="CJK"),
}


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
               lambda m: '<a href="' + m[2].replace('"', "%22") + '" color="#235e7c">' + m[1] + "</a>", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r'<font color="#235e7c">\1</font>', s)
    return s


def P(t, kind="p", **kw):
    return Paragraph(inline(t), st[kind], **kw)


class Doc(BaseDocTemplate):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.entries = []

    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name == "section":
            t = f.getPlainText()
            key = "sec%d" % len(self.entries)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(t, key, level=0, closed=False)
            self.entries.append({"title": t, "page": self.page})


def page(canvas, doc):
    canvas.saveState()
    canvas.setTitle("美股风气四十年：兴衰、存活与用时（1986–2026）")
    canvas.setAuthor("yc_research")
    if doc.page > 1:
        canvas.setFont("CN", 7.2)
        canvas.setFillColor(muted)
        canvas.drawString(M, H - 11 * mm, "美股风气四十年  /  兴衰统计")
        canvas.drawRightString(W - M, H - 11 * mm, "1986–2026  ·  数据截至 2026-10-05")
        canvas.setStrokeColor(line)
        canvas.setLineWidth(0.5)
        canvas.line(M, H - 13.5 * mm, W - M, H - 13.5 * mm)
    else:
        canvas.setFillColor(blue)
        canvas.rect(M, H - 13 * mm, 32 * mm, 2 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(line)
    canvas.line(M, 14 * mm, W - M, 14 * mm)
    canvas.setFont("CN", 7.2)
    canvas.setFillColor(muted)
    canvas.drawString(M, 9.7 * mm, "研究资料，不构成投资建议  |  事实带来源，计算可复跑，推论单独标示")
    canvas.drawRightString(W - M, 9.7 * mm, str(doc.page))
    canvas.restoreState()


def visible_len(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return sum(2 if ord(ch) > 0x2E80 else 1 for ch in s)


def build_table(block):
    rows = []
    for s in block:
        row = [v.strip() for v in s.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", v) for v in row):
            continue
        rows.append(row)
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    weight = []
    for j in range(n):
        body = sorted(visible_len(r[j]) for r in rows[1:]) or [0]
        p80 = body[max(0, int(len(body) * 0.8) - 1)]
        head = min(visible_len(rows[0][j]), 12)  # 表头最多按 6 个汉字宽度计，其余换行
        datey = sum(bool(re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?", r[j].strip())) for r in rows[1:]) > len(rows[1:]) * 0.5
        weight.append(max(min(max(p80, head, 8), 34), 10 if datey else 0))  # 日期列至少放得下 2000-03；长文本列封顶
    weight[0] = max(weight[0], 14)  # 第一列（公司/行业名）不要被挤到逐字换行
    widths = [WIDTH * x / sum(weight) for x in weight]
    # 数字列：多数单元格短且以数字/正负号开头（长文本即使以日期开头也不算）
    numeric = [sum(bool(re.match(r"^[+\-−]?[\d.]", r[j])) and visible_len(r[j]) <= 16 for r in rows[1:]) > len(rows[1:]) * 0.65
               for j in range(n)]
    cells = [[P(v, "head" if i == 0 else "cellr" if numeric[j] and j else "cell") for j, v in enumerate(r)]
             for i, r in enumerate(rows)]
    t = Table(cells, colWidths=widths, repeatRows=1, hAlign="LEFT", spaceBefore=3, spaceAfter=9)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), soft), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LINEBELOW", (0, 0), (-1, 0), 0.65, blue), ("LINEBELOW", (0, 1), (-1, -1), 0.3, line),
                           ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                           ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#fafcfd")])]))
    return t


def make_story():
    lines = (BASE / "report.md").read_text(encoding="utf-8").splitlines()
    story, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s == "<!-- PAGEBREAK -->":
            story.append(PageBreak())
            i += 1
            continue
        if s.startswith("<!--"):
            i += 1
            continue
        if s.startswith("```"):  # 代码块：等宽字体逐行
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i]).replace(" ", "&nbsp;"))
                i += 1
            i += 1
            story.append(Paragraph("<br/>".join(buf), st["code"]))
            continue
        if s.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            story.append(build_table(block))
            continue
        if s.startswith("!["):
            p = BASE / re.search(r"\]\(([^)]+)\)", s)[1]
            with PILImage.open(p) as im:
                w, h = im.size
            ww = WIDTH
            hh = ww * h / w
            cap = 225 * mm if h > w else 150 * mm  # 竖长图（时间轴、结局图）允许占满一页，否则标签太小
            if hh > cap:
                ww *= cap / hh
                hh = cap
            story.append(KeepTogether([Image(str(p), width=ww, height=hh, hAlign="CENTER"), Spacer(1, 6)]))
            i += 1
            continue
        if s.startswith("# "):
            story.append(P(s[2:], "h1"))
            i += 1
            continue
        if s.startswith("## "):
            nxt = next((x.strip() for x in lines[i + 1:] if x.strip()), "")
            story.append(CondPageBreak(130 * mm if nxt.startswith("![") else 70))
            story.append(P(s[3:], "h2"))
            i += 1
            continue
        if s.startswith("### "):
            nxt = next((x.strip() for x in lines[i + 1:] if x.strip()), "")
            story.append(CondPageBreak(120 * mm if nxt.startswith("![") else 50))  # 标题后紧跟图：标题和图同页
            story.append(P(s[4:], "h3"))
            i += 1
            continue
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]).strip())
                i += 1
            story.append(Paragraph("<br/>".join(inline(x) for x in buf if x), st["quote"]))
            continue
        m = re.match(r"^(- |\d+\. )(.*)", s)
        if m:
            bullet = "•" if m[1] == "- " else m[1].strip()
            story.append(Paragraph(inline(m[2]), st["li"], bulletText=bullet))
            i += 1
            continue
        para = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||!\[|>|- |\d+\. |<!--)", lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        txt = " ".join(para)
        story.append(P(txt, "caption" if txt.startswith(("来源：", "注：", "口径：")) else "p"))
    return story


if __name__ == "__main__":
    doc = Doc(str(OUT), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=19 * mm, bottomMargin=19 * mm,
              title="美股风气四十年")
    frame = Frame(M, 19 * mm, WIDTH, H - 38 * mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="r", frames=frame, onPage=page)])
    doc.build(make_story())
    (BASE / "data/pdf_structure.json").write_text(json.dumps({"path": str(OUT), "pages": doc.page, "sections": doc.entries},
                                                             ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"path": str(OUT), "pages": doc.page, "bytes": OUT.stat().st_size}, ensure_ascii=False))
