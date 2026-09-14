#!/usr/bin/env python
"""Build the INTU cash-flow forensics addendum PDF.
Source: companies/intu/2026-09-13/addendum_cashflow_forensics.md
Output: output/pdf/intu_addendum_cashflow_2026-09-13.pdf
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, ".pdf_deps"))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUT = os.path.join(REPO, "output", "pdf", "intu_addendum_cashflow_2026-09-13.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))

INK, MUTED, LINE = colors.HexColor("#1a1d24"), colors.HexColor("#5b6472"), colors.HexColor("#d8dee8")
SOFT, HEAD = colors.HexColor("#f4f7fb"), colors.HexColor("#eef2f8")
RED, GRN, YEL = colors.HexColor("#fdeeee"), colors.HexColor("#eaf6f3"), colors.HexColor("#fdf6e8")

ss = getSampleStyleSheet()
S = dict(
    title=ParagraphStyle("t", parent=ss["Title"], fontName="CN", fontSize=18, leading=24, textColor=INK,
                         alignment=0, spaceAfter=3),
    sub=ParagraphStyle("s", fontName="CN", fontSize=8.4, leading=12.4, textColor=MUTED, spaceAfter=10),
    h1=ParagraphStyle("h1", fontName="CN", fontSize=12.5, leading=17, textColor=INK, spaceBefore=12, spaceAfter=5),
    h2=ParagraphStyle("h2", fontName="CN", fontSize=10.4, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4),
    p=ParagraphStyle("p", fontName="CN", fontSize=8.5, leading=13, textColor=INK, spaceAfter=5),
    quote=ParagraphStyle("q", fontName="CN", fontSize=8.3, leading=12.6, textColor=INK, leftIndent=7,
                         borderPadding=(5, 5, 5, 7), backColor=SOFT, spaceAfter=6),
    cell=ParagraphStyle("c", fontName="CN", fontSize=7.4, leading=10, textColor=INK),
    cellr=ParagraphStyle("cr", fontName="CN", fontSize=7.4, leading=10, textColor=INK, alignment=2),
)


def P(t, k="p"):
    return Paragraph(t, S[k])


def tbl(rows, widths, aligns=None, hi=None):
    aligns = aligns or ["l"] * len(rows[0])
    data = [[Paragraph(str(c), S["cellr"] if (i and aligns[j] == "r") else S["cell"])
             for j, c in enumerate(r)] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cm = [("BACKGROUND", (0, 0), (-1, 0), HEAD), ("GRID", (0, 0), (-1, -1), 0.3, LINE),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 3),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
          ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    for ri, col in (hi or {}).items():
        cm.append(("BACKGROUND", (0, ri), (-1, ri), col))
    t.setStyle(TableStyle(cm))
    return t


def footer(c, d):
    c.saveState(); c.setFont("CN", 7); c.setFillColor(MUTED)
    c.drawString(18 * mm, 11 * mm, "INTU 现金流量表法证附录 · FY2026 10-K 一手 · 2026-09-13")
    c.drawRightString(A4[0] - 18 * mm, 11 * mm, "第 %d 页" % d.page)
    c.setStrokeColor(LINE); c.line(18 * mm, 14.5 * mm, A4[0] - 18 * mm, 14.5 * mm); c.restoreState()


W = A4[0] - 36 * mm
F = [P("INTU 附录:现金流量表法证", "title"),
     P("闭合主报告 §5.1「OCF 是净利的 194%,缺口来源未查清」<br/>"
       "一手来源:FY2026 10-K(0000896878-26-000037)现金流量表 R9、所得税附注 R19 / R75 / R79 / R80", "sub")]

F.append(Paragraph(
    "🔴 <b>结论先行:9.72% 的自由现金流收益率是假的。</b><br/><br/>"
    "FY2026 的 $8,838M 经营现金流里,约 <b>$1,170M 来自一次性税务事件</b> —— 不是经营性的,不会重复。<br/>"
    "主报告的 <b>P/FCF 10.3x / 收益率 9.72% 必须作废</b>。正常化后 <b>12.0x / 8.36%</b>;"
    "再扣股权激励 <b>16.5x / 6.05%</b>。<br/><br/>"
    "<b>这把 buy_below 的方向从「上修」翻转为「下修」。主报告 §6.3 的结论作废。</b>", S["quote"]))

F.append(P("一、OCF 桥:$6,207M → $8,838M 的增量来自哪", "h1"))
F.append(tbl([
    ["调节项", "FY2026", "FY2025", "FY2024", "YoY 变化"],
    ["净利润", "4,566", "3,869", "2,963", "+697"],
    ["折旧", "187", "172", "159", "+15"],
    ["收购无形资产摊销", "659", "637", "630", "+22"],
    ["非现金经营租赁成本", "106", "75", "81", "+31"],
    ["股权激励", "2,056", "1,968", "1,940", "+88"],
    ["预期信用损失准备", "237", "134", "118", "<b>+103</b>"],
    ["<b>递延所得税</b> 🔴", "<b>1,279</b>", "<b>(435)</b>", "<b>(554)</b>", "<b>+1,714</b>"],
    ["其他", "(248)", "(7)", "(26)", "−241"],
    ["营运资产负债变化合计", "(4)", "(206)", "(429)", "+202"],
    ["<b>经营现金流</b>", "<b>8,838</b>", "<b>6,207</b>", "<b>4,884</b>", "<b>+2,631</b>"],
], [52 * mm, 26 * mm, 26 * mm, 26 * mm, W - 130 * mm], ["l", "r", "r", "r", "r"], hi={7: RED}))
F.append(Spacer(1, 4))
F.append(P("<b>递延所得税单项贡献 +$1,714M,占 OCF 增量 $2,631M 的 65%。</b>"
           "而且是符号翻转:FY2024 −554、FY2025 −435 → <b>FY2026 +1,279</b>。", "p"))

F.append(P("二、为什么:OBBBA / Section 174 —— 公司 10-K 原文", "h1"))
F.append(Paragraph(
    "“On July 4, 2025, the U.S. federal government enacted the <b>One Big Beautiful Bill Act (OBBBA)</b>, which "
    "includes significant tax changes, most notably the <b>reinstatement of the immediate expensing of domestic "
    "research and development expenditures, effective in fiscal 2026</b>. The deductibility of these expenditures, "
    "<b>including the election to deduct the prior year unamortized, capitalized research and development expenses, "
    "reduced the deferred tax assets and income taxes payable for fiscal 2026.</b>”", S["quote"]))
F.append(tbl([
    ["递延税资产", "FY2026", "FY2025", "变化"],
    ["<b>资本化研发</b> 🔴", "<b>673</b>", "<b>1,895</b>", "<b>−1,222</b>"],
    ["其他各项合计", "804", "775", "+29"],
    ["递延税资产总额(毛)", "1,477", "2,670", "−1,193"],
    ["估值备抵", "(257)", "(290)", "+33"],
    ["<b>净递延税资产 / (负债)</b>", "<b>(67)</b>", "<b>1,202</b>", "<b>−1,269</b>"],
], [50 * mm, 26 * mm, 26 * mm, W - 102 * mm], ["l", "r", "r", "r"], hi={1: RED}))
F.append(Spacer(1, 4))
F.append(P("<b>资本化研发的递延税资产一年消耗 $1,222M(64%),与现金流量表 +$1,279M 的递延税加回几乎完全对应。</b>", "p"))

F.append(P("三、现金税 vs 账面税 —— 缺口的直接证据", "h1"))
F.append(tbl([
    ["", "FY2026", "FY2025", "FY2024"],
    ["<b>美国联邦现金所得税</b> 🔴", "<b>$(6)M</b>", "$1,105M", "$1,659M"],
    ["州与地方 / 海外", "287", "303", "222"],
    ["<b>实付所得税合计(净退税后)</b>", "<b>$281M</b>", "$1,408M", "$1,881M"],
    ["当期所得税费用(账面)", "179", "1,481", "1,222"],
    ["<b>递延所得税费用(账面)</b>", "<b>1,272</b>", "(516)", "(635)"],
    ["<b>所得税费用合计(账面)</b>", "<b>$1,451M</b>", "$965M", "$587M"],
], [56 * mm, 28 * mm, 28 * mm, W - 112 * mm], ["l", "r", "r", "r"], hi={1: RED, 3: RED}))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>FY2026 账面税费 $1,451M,实际掏出去 $281M —— 缺口 $1,170M。"
                   "美国联邦层面实际是净退税 $6M;FY2024 同口径交了 $1,659M。</b>", S["quote"]))

F.append(PageBreak())
F.append(P("四、正常化", "h1"))
F.append(P("<b>稳态判断:</b>OBBBA 永久恢复研发费用即时抵扣,所以 FY2027 起稳态是"
           "<b>现金税 ≈ 账面税费</b>,但<b>不会再有追补扣除</b>。剩余资本化研发递延税资产 <b>$673M</b> "
           "会在 FY2027+ 继续释放,速率远低于 FY2026 —— <b>是递减的尾巴,不是悬崖。</b>", "p"))
F.append(tbl([
    ["", "报告值", "正常化"],
    ["经营现金流", "$8,838M", "<b>$7,668M</b>(剔除 $1,170M 税务缺口)"],
    ["资本开支", "$175M(仅 PP&amp;E)", "<b>$221M</b>(PP&amp;E 175 + 资本化自用软件 46)"],
    ["<b>自由现金流</b>", "<b>$8,617M</b>", "<b>$7,447M</b>"],
    ["股权激励", "$2,056M", "$2,056M"],
    ["<b>FCF − SBC</b>", "$6,561M", "<b>$5,391M</b>"],
], [34 * mm, 38 * mm, W - 72 * mm], ["l", "r", "l"], hi={3: YEL, 5: YEL}))
F.append(Spacer(1, 4))
F.append(P("<b>正常化后 FCF 比报告值低 13.6%。</b>", "p"))

F.append(P("4.1 修正后的估值(市值 $89.1B)", "h2"))
F.append(tbl([
    ["口径", "基数", "倍数", "收益率", ""],
    ["报告 FCF", "$8,617M", "10.3x", "9.67%", "❌ <b>作废</b>"],
    ["<b>正常化 FCF</b>", "<b>$7,447M</b>", "<b>12.0x</b>", "<b>8.36%</b>", "上限"],
    ["报告 FCF − SBC", "$6,561M", "13.6x", "7.36%", ""],
    ["<b>正常化 FCF − SBC</b>", "<b>$5,391M</b>", "<b>16.5x</b>", "<b>6.05%</b>", "<b>建议 base</b>"],
    ["GAAP 净利润", "$4,566M", "19.5x", "5.12%", ""],
], [40 * mm, 26 * mm, 22 * mm, 24 * mm, W - 112 * mm], ["l", "r", "r", "r", "l"],
    hi={1: RED, 4: GRN}))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>主报告说「9.72%,建议 base 用 7.42%」。修正后:上限 8.36%,建议 base 6.05%。"
                   "整条区间往下挪了约 1.4 个百分点。</b>", S["quote"]))

F.append(P("五、顺带修正主报告的两处错误", "h1"))
F.append(tbl([
    ["错误", "修正"],
    ["<b>❌ 写了「无股息」</b>",
     "<b>INTU FY2026 派息 $1,347M</b>(FY25 $1,189M、FY24 $1,034M)。修正后股东总回报:"
     "回购 $5,412M(6.07%)+ 股息 $1,347M(1.51%)= <b>$6,759M = 7.59%</b>。<b>这一项对多头有利。</b>"],
    ["<b>❌ capex 漏了一项</b>",
     "主报告用 $175M(仅 PP&amp;E)。投资活动里还有 <b>资本化自用软件 $46M</b>。"
     "<b>真实 capex = $221M</b>,占营收 1.0%(非 0.8%)。量级小,但口径应统一。"],
], [34 * mm, W - 34 * mm]))

F.append(P("六、新发现:藏在 OCF 下面的放贷业务", "h1"))
F.append(tbl([
    ["投资活动", "FY2026", "FY2025", "FY2024"],
    ["<b>发放及购买持有至到期应收票据</b>", "<b>$(6,755)M</b>", "$(3,992)M", "$(2,538)M"],
    ["出售原分类为持有至到期的应收票据", "2,210", "562", "234"],
    ["本金回收", "4,253", "2,706", "2,068"],
    ["<b>净现金流出</b>", "<b>(292)</b>", "(724)", "(236)"],
], [58 * mm, 28 * mm, 26 * mm, W - 112 * mm], ["l", "r", "r", "r"], hi={1: YEL}))
F.append(Spacer(1, 4))
F.append(P("<b>FY2026 发放了 $6,755M 贷款,同比 +69%</b>(Credit Karma / QuickBooks Capital)。"
           "<b>全部走投资活动,OCF 完全看不到。</b>净流出只有 $292M(被回收和出售抵消),"
           "但<b>毛发放规模 $6.8B 说明这不是一家纯粹的 capital-light 软件公司</b> —— 它内嵌了一个快速扩张的信贷业务。<br/>"
           "<b>佐证:预期信用损失准备从 $134M 跳到 $237M(+77%)。</b>贷款簿在长大,信用风险敞口也在长大。", "p"))
F.append(Paragraph("⚠️ <b>应成为新的监控项。</b>软件公司的估值框架不适用于信贷业务:"
                   "一个在信用周期上行期扩张的贷款簿,盈利会被前置、损失会被后置。", S["quote"]))

F.append(PageBreak())
F.append(P("七、对裁决的影响", "h1"))
F.append(tbl([
    ["项", "主报告", "修正后"],
    ["K-C 盈利质量", "🟡 未核实", "<b>🔴 已核实,是一次性税务事件</b>"],
    ["建议 base 收益率", "7.42%", "<b>6.05%</b>"],
    ["<b>buy_below 方向</b>", "「上修但被减速抵消 → 维持 $328」", "<b>🔴 下修</b>"],
    ["binding_constraint", "盈利质量可验证性", "<b>价格 —— 重新变回价格约束</b>"],
    ["new_money_verdict", "STARTER", "<b>STARTER,但需重推 buy_below 后才可执行</b>"],
], [34 * mm, 50 * mm, W - 84 * mm], hi={3: RED}))
F.append(Spacer(1, 4))
F.append(P("<b>逻辑:</b>卡的 buy_below $328 来自「base 10y IRR = 10%」,那个 base 用的是 FY2026 之前的数字。"
           "现在我们知道 FY2026 现金流被一次性事件抬高 13.6%,<b>而且 FY2027 营收指引减速到 +9~10%</b>。"
           "<b>两个因素同向,都指向 base 下调 → buy_below 下调。</b><br/>"
           "主报告 §6.3 判断「两股力量方向相反、量级相当,维持 $328 不动」—— 那个判断建立在 $8,663M FCF 是真实的假设上。"
           "<b>假设被推翻,两股力量变成同向。$328 需要正式下修。</b>", "p"))

F.append(P("八、生意本身没有变坏 —— 必须说清楚", "h1"))
F.append(P("这份法证否定的是<b>现金流的质量口径</b>,不是生意:<br/>"
           "• 营收 +13.9%、营业利润率 27.4%(+1.3pp)、GAAP EPS +20% —— <b>全部是真的</b><br/>"
           "• TurboTax 单量 −2% 而营收 +7% —— <b>机制仍然成立</b><br/>"
           "• QuickBooks Online Accounting +23% —— <b>最硬那条腿没松</b><br/>"
           "• 股东总回报 7.59%(含股息)—— <b>比原报告还好</b>", "p"))
F.append(Paragraph("<b>变的只有一件事:那 9.72% 里有约 1.4 个百分点是税法改革送的一次性红利,"
                   "不是这门生意每年能产生的。</b><br/>"
                   "一个 6% owner-earnings 收益率 + 9~10% 增长的生意,仍然<b>可能</b>是好投资 —— "
                   "但它不是「10 倍自由现金流的白菜价」。<b>这两个判断之间隔着一次建仓决策。</b>", S["quote"]))

F.append(P("九、下一步", "h1"))
F.append(tbl([
    ["#", "动作"],
    ["<b>1</b>", "<b>正式重推 buy_below</b> —— 用正常化 FCF $7,447M(或 FCF−SBC $5,391M)+ FY2027 +9~10% 增速,重算 10y IRR"],
    ["2", "把放贷业务(§6)单独建模或至少列为监控项 —— 现有软件估值框架不覆盖它"],
    ["3", "监控 FY2027 Q1 现金税:若联邦现金税回到 $300M+/季,确认 §4 的稳态判断"],
    ["4", "监控剩余 $673M 资本化研发递延税资产的释放速率"],
], [8 * mm, W - 8 * mm], hi={1: GRN}))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>在 1 完成之前,INTU 不构成可执行的建仓标的。</b>", S["quote"]))
F.append(P("<b>诚实状态</b>:本附录闭合了主报告 §5.1,证据为 10-K 一手(现金流量表 + 所得税附注,公司原文引用)。"
           "<b>未做</b>:10y IRR 模型重算、buy_below 正式下修的具体数字、放贷业务建模。", "p"))

SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                  topMargin=16 * mm, bottomMargin=18 * mm,
                  title="INTU 现金流量表法证附录 2026-09-13", author="yc_research"
                  ).build(F, onFirstPage=footer, onLaterPages=footer)
print("PDF ->", OUT, os.path.getsize(OUT), "bytes")
