#!/usr/bin/env python
"""Build the INTU detailed research report PDF (2026-09-13).

Source: companies/intu/2026-09-13/research_report.md
Output: output/pdf/intu_research_2026-09-13.pdf
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

OUT = os.path.join(REPO, "output", "pdf", "intu_research_2026-09-13.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))

INK, MUTED, LINE = colors.HexColor("#1a1d24"), colors.HexColor("#5b6472"), colors.HexColor("#d8dee8")
SOFT, HEAD = colors.HexColor("#f4f7fb"), colors.HexColor("#eef2f8")
GRN, RED, YEL = colors.HexColor("#eaf6f3"), colors.HexColor("#fdeeee"), colors.HexColor("#fdf6e8")

ss = getSampleStyleSheet()
S = dict(
    title=ParagraphStyle("t", parent=ss["Title"], fontName="CN", fontSize=19, leading=25,
                         textColor=INK, alignment=0, spaceAfter=3),
    sub=ParagraphStyle("s", fontName="CN", fontSize=8.6, leading=12.6, textColor=MUTED, spaceAfter=10),
    h1=ParagraphStyle("h1", fontName="CN", fontSize=13, leading=17.5, textColor=INK, spaceBefore=12, spaceAfter=5),
    h2=ParagraphStyle("h2", fontName="CN", fontSize=10.6, leading=14.5, textColor=INK, spaceBefore=9, spaceAfter=4),
    p=ParagraphStyle("p", fontName="CN", fontSize=8.5, leading=13, textColor=INK, spaceAfter=5),
    quote=ParagraphStyle("q", fontName="CN", fontSize=8.3, leading=12.6, textColor=INK,
                         leftIndent=7, borderPadding=(5, 5, 5, 7), backColor=SOFT, spaceAfter=6),
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
    cmds = [("BACKGROUND", (0, 0), (-1, 0), HEAD), ("GRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    for ri, col in (hi or {}).items():
        cmds.append(("BACKGROUND", (0, ri), (-1, ri), col))
    t.setStyle(TableStyle(cmds))
    return t


def footer(c, d):
    c.saveState(); c.setFont("CN", 7); c.setFillColor(MUTED)
    c.drawString(18 * mm, 11 * mm, "INTU 详细调研报告 · as_of 2026-09-11 收盘 · 生成 2026-09-13")
    c.drawRightString(A4[0] - 18 * mm, 11 * mm, "第 %d 页" % d.page)
    c.setStrokeColor(LINE); c.line(18 * mm, 14.5 * mm, A4[0] - 18 * mm, 14.5 * mm); c.restoreState()


W = A4[0] - 36 * mm
F = []

F += [P("Intuit (INTU) 详细调研报告", "title"),
      P("as_of 价格 $321.57(2026-09-11 收盘) · refresh_of companies/intu/2026-08-07<br/>"
        "触发:FY2026 10-K(period 2026-07-31)于 <b>2026-09-09 报送</b> —— 上一张卡点名等待的那份文件<br/>"
        "一手来源:SEC EDGAR 10-K(0000896878-26-000037)XBRL + 8-K(2026-08-25)EX-99.01 原文", "sub")]

F.append(Paragraph(
    "<b>上一张卡把 verdict 封在 STARTER,理由是「FY2026 全年业绩要到 2026-08-25 才出」。业绩出了,10-K 也报送了,"
    "而且比卡里假设的更好:营收 +13.9%、营业利润率再扩 1.3pp、FCF 暴增 41.5% 到 $8,663M。"
    "现价 10.3x FCF、9.72% 自由现金流收益率。封顶理由消失了,价格仍在 buy_below 线内。</b><br/><br/>"
    "<b>但有三件事必须先想清楚,否则这个 9.72% 是假的:</b><br/>"
    "① 经营现金流是净利的 <b>194%</b>,缺口来源没查清 &nbsp;② 商誉 $13,981M = 股东权益的 <b>74%</b>,而 Mailchimp 正被单独圈出来 "
    "&nbsp;③ 股权激励 $2,056M = 营收的 <b>9.6%</b>,这才是这家公司真正的「资本开支」", S["quote"]))

F.append(P("一、锁定结论", "h1"))
F.append(tbl([
    ["字段", "值"],
    ["as_of price / 摊薄股数 / 市值", "<b>$321.57</b> · 277M · <b>~$89.1B</b>(净负债 ~$1.7B → EV ~$90.8B)"],
    ["business_verdict", "<b>good</b>(维持)"],
    ["<b>new_money_verdict</b>", "<b>STARTER</b>(维持) · initial <b>2%</b> · max <b>6%</b>"],
    ["existing_position_verdict", "HOLD_TO_ADD"],
    ["<b>buy_below</b>", "<b>~$328 暂不改动</b> —— 证据指向上修,但被 FY2027 减速抵消(见 §6.3)"],
    ["<b>binding_constraint</b>", "<b>从「完整度」转为「盈利质量可验证性」</b> —— 价格仍不是约束"],
    ["completeness", "<b>~72%</b>(从 62% 上修:FY2026 全年 + 单量数据 + 10-K 到位)"],
], [46 * mm, W - 46 * mm], hi={4: GRN}))
F.append(Spacer(1, 4))
F.append(P("<b>verdict 未变,但封顶的理由换了。这是本次刷新最重要的结构性变化。</b>", "p"))

F.append(P("二、FY2026 实际交付(10-K 一手,$M)", "h1"))
yrs = ["2022", "2023", "2024", "2025", "<b>2026</b>"]
data = [
    ("营收", [12726, 14368, 16285, 18831, 21448]),
    ("营业利润", [2571, 3141, 3630, 4923, 5884]),
    ("<b>营业利润率</b>", ["20.2%", "21.9%", "22.3%", "26.1%", "<b>27.4%</b>"]),
    ("净利润", [2066, 2384, 2963, 3869, 4566]),
    ("经营现金流", [3889, 5046, 4884, 6207, 8838]),
    ("资本开支", [157, 210, 191, 84, 175]),
    ("<b>自由现金流</b>", [3732, 4836, 4693, 6123, 8663]),
    ("<b>FCF 利润率</b>", ["29.3%", "33.7%", "28.8%", "32.5%", "<b>40.4%</b>"]),
    ("股权激励 SBC", [1308, 1712, 1940, 1968, 2056]),
    ("<b>FCF − SBC</b>", [2424, 3124, 2753, 4155, 6607]),
    ("回购", [1861, 1967, 1988, 2772, 5412]),
    ("摊薄股数(M)", [284, 283, 284, 283, 277]),
    ("<b>摊薄 EPS</b>", ["7.28", "8.42", "10.43", "13.67", "<b>16.46</b>"]),
    ("商誉", [13736, 13780, 13844, 13980, 13981]),
    ("股东权益", [16441, 17269, 18436, 19710, 18992]),
]
rows = [["财年"] + yrs]
for lab, vals in data:
    rows.append([lab] + [(f"{v:,}" if isinstance(v, int) else v) for v in vals])
F.append(tbl(rows, [34 * mm] + [(W - 34 * mm) / 5] * 5, ["l"] + ["r"] * 5,
             hi={7: GRN, 10: GRN}))
F.append(Spacer(1, 4))
F.append(tbl([["四年复合 FY2022→FY2026", "营收", "摊薄 EPS", "自由现金流", "营业利润率"],
              ["CAGR", "<b>+13.9%</b>", "<b>+22.6%</b>", "<b>+23.4%</b>", "20.2% → <b>27.4%</b>"]],
             [46 * mm] + [(W - 46 * mm) / 4] * 4, ["l", "r", "r", "r", "r"]))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>这是一条教科书级的经营杠杆曲线:营收复合 14%,EPS 复合 23%,利润率四年扩了 7 个百分点,"
                   "而资本开支占营收只有 0.8%。生意本身没有任何问题。</b>", S["quote"]))

F.append(PageBreak())
F.append(P("三、分部拆解(FY2026 全年,8-K EX-99.01)", "h1"))
F.append(tbl([
    ["分部 / 产品线", "FY2026 营收", "YoY", "备注"],
    ["<b>Global Business Solutions</b>", "$12.9B", "+16%", "<b>ex-Mailchimp +18%</b>"],
    ["└ Online Ecosystem", "$9.9B", "+19%", "<b>ex-Mailchimp +23%</b>"],
    ["└ QuickBooks Online Accounting", "—", "<b>+23%</b>", "最硬的一条腿"],
    ["└ Online Services", "—", "+16%", "<b>ex-Mailchimp +24%</b>"],
    ["<b>Consumer</b>", "$8.6B", "+11%", ""],
    ["└ TurboTax", "$5.3B", "+7%", ""],
    ["└ TurboTax Live", "—", "<b>+37%</b>", "已占 TurboTax 营收 <b>53%</b>"],
    ["<b>Credit Karma</b>", "$2.6B", "+20%", ""],
    ["ProTax", "$647M", "+4%", ""],
    ["<b>总计</b>", "<b>$21.4B</b>", "<b>+14%</b>", "Big Bets 合计 +34%,占营收 30%"],
], [54 * mm, 24 * mm, 18 * mm, W - 96 * mm], ["l", "r", "r", "l"]))
F.append(Spacer(1, 4))
F.append(P("<b>每次出现 “ex-Mailchimp” 都是一次加速:</b>GBS +16%→<b>+18%</b>;Online Ecosystem +19%→<b>+23%</b>;"
           "Online Services +16%→<b>+24%</b>(差 <b>8pp</b>)。<br/>"
           "<b>Mailchimp 在系统性拖累每一个它所在的口径。</b>管理层从 FY2027 起把它拆成独立可报告分部 —— "
           "这是好事(透明度),但也等于承认这笔 $12B 收购需要被单独看待。", "p"))

F.append(P("四、上一张卡的三个 OPEN,逐条结算", "h1"))
F.append(tbl([
    ["OPEN", "结论", "依据"],
    ["<b>✅ O1 FY2026 全年</b>", "<b>已交付,好于假设</b>",
     "营收 +13.9%、GAAP 营业利润 +19.5%、GAAP EPS <b>+20%</b> 到 $16.46、非 GAAP EPS +20% 到 $24.27"],
    ["<b>✅ O2 TurboTax 单量</b>", "<b>机制被证实,非推翻</b>",
     "美国联邦总单量 <b>39.0M vs 39.9M = −2%</b>(Desktop −7%、Online −2%);而 TurboTax 营收 +7% → "
     "每单价值 +9%。TurboTax Live +37%,已占 53% —— 护城河从「分发」迁向「专家网络」"],
    ["<b>❌ O3 AI 变现</b>", "<b>仍然零披露</b>",
     "FY2026 全年与 10-K 中无任何 AI 收入单独拆分;completeness 封在 ~72% 的主因"],
], [30 * mm, 34 * mm, W - 64 * mm], hi={1: GRN, 2: GRN, 3: YEL}))
F.append(Spacer(1, 3))
F.append(P("⚠️ 注意:Desktop −7% 快于 Online −2%。<b>流失是真的,只是被 Live 的单价提升盖过去了。"
           "这个赛跑能持续多久,是 base case 的核心假设。</b>", "p"))

F.append(PageBreak())
F.append(P("五、质量审查 —— 三个必须盯住的", "h1"))
F.append(P("FY2026 的数字很漂亮,漂亮到需要检查是不是可持续。", "p"))

F.append(P("🔴 5.1 经营现金流 = 净利润的 194%,缺口来源未查清", "h2"))
F.append(tbl([["财年", "OCF", "净利润", "<b>OCF / NI</b>"],
              ["2023", "5,046", "2,384", "212%"], ["2024", "4,884", "2,963", "165%"],
              ["2025", "6,207", "3,869", "160%"], ["<b>2026</b>", "<b>8,838</b>", "<b>4,566</b>", "<b>194%</b>"]],
             [24 * mm, 26 * mm, 26 * mm, W - 76 * mm], ["l", "r", "r", "r"], hi={4: RED}))
F.append(Spacer(1, 3))
F.append(P("FY2026 OCF 单年跳 <b>+42.4%</b>,净利润只涨 +18.0%。部分可解释:SBC $2,056M(非现金)+ 摊销 + 递延税。"
           "<b>上一张卡记录过 FY2025 的 OCF 被「$1.4B 递延税一次性」推高。FY2026 有没有类似的一次性,我没有从 10-K 逐行核实。</b>", "p"))
F.append(Paragraph("<b>这是本报告最大的未闭合项。</b>若 $8,663M FCF 含几亿到十几亿一次性,9.72% 的收益率会被高估。<br/>"
                   "<b>保守替代口径:用 FCF − SBC = $6,607M → P/(FCF−SBC) 13.5x、收益率 7.42%。"
                   "建议用它做 base,把 9.72% 当上限。</b>", S["quote"]))

F.append(P("🟡 5.2 商誉 $13,981M = 股东权益的 73.6%", "h2"))
F.append(P("商誉主要来自 <b>Mailchimp(~$12B,2021)</b> 与 <b>Credit Karma(~$7B,2020)</b>。"
           "Credit Karma 是成功的(FY2026 $2.6B,+20%);<b>Mailchimp 不是</b> —— 每个含它的口径都慢 2–8pp。<br/>"
           "从 FY2027 起 Mailchimp 成为独立可报告分部 → 会计上<b>要独立做商誉减值测试</b>。"
           "<b>这实质提高了 FY2027 出现 Mailchimp 商誉减值的概率。</b>减值是非现金的、不影响 FCF,"
           "但会一次性打掉 GAAP EPS 和账面权益,并且是对「$12B 买贵了」的正式承认。", "p"))

F.append(P("🟡 5.3 SBC $2,056M —— 这才是真正的「资本开支」", "h2"))
F.append(tbl([["FY2026", "金额", "占营收"],
              ["资本开支", "$175M", "<b>0.8%</b>"],
              ["<b>股权激励</b>", "<b>$2,056M</b>", "<b>9.6%</b>"]],
             [30 * mm, 26 * mm, W - 56 * mm], ["l", "r", "r"], hi={2: YEL}))
F.append(Spacer(1, 3))
F.append(P("名义上 capital-light(capex 占营收 0.8%),但每年用近 10% 的营收以股权支付员工。"
           "回购 $5,412M = 市值的 <b>6.1%</b>,只换来摊薄股数从 283M 降到 277M(<b>−2.1%</b>)—— <b>差额被 SBC 吃掉了</b>。<br/>"
           "<b>任何用 FCF 而不扣 SBC 的估值,都会系统性高估这家公司。</b>", "p"))

F.append(PageBreak())
F.append(P("六、估值", "h1"))
F.append(P("6.1 当前多口径", "h2"))
F.append(tbl([["口径", "基数(FY2026)", "倍数", "收益率"],
              ["GAAP 净利润", "$4,566M", "P/E 19.5x", "5.12%"],
              ["自由现金流", "$8,663M", "<b>P/FCF 10.3x</b>", "<b>9.72%</b>"],
              ["<b>FCF − SBC(建议 base)</b>", "<b>$6,607M</b>", "<b>13.5x</b>", "<b>7.42%</b>"],
              ["EV / FCF(含净负债 $1.7B)", "$8,663M", "10.5x", "—"],
              ["股东回报(回购,无股息)", "$5,412M", "—", "<b>6.07%</b>"]],
             [50 * mm, 30 * mm, 32 * mm, W - 112 * mm], ["l", "r", "r", "r"], hi={3: GRN}))

F.append(P("6.2 同业对照 —— 为什么「线下百分比」不可比", "h2"))
F.append(tbl([
    ["", "现价", "市值", "base FCF", "<b>P/FCF</b>", "<b>FCF 收益率</b>", "距 buy_below"],
    ["<b>INTU</b>", "$321.57", "$89.1B", "$8,663M", "<b>10.3x</b>", "<b>9.72%</b>", "线内 2.0%"],
    ["ADBE", "$252.23", "$101.5B", "$9,852M", "10.3x", "9.71%", "线下 21.3%"],
    ["BSX", "$42.98", "$63.4B", "$3,658M", "17.3x", "5.77%", "线下 21.0%"],
    ["SYK", "$275.56", "$106.4B", "$4,283M", "24.8x", "4.03%", "线下 32.8%"],
    ["EW", "$84.37", "$48.7B", "$1,335M", "36.5x", "2.74%", "线下 9.0%"],
    ["ISRG", "$369.15", "$131.9B", "$2,491M", "<b>53.0x</b>", "<b>1.89%</b>", "线下 22.4%"],
], [16 * mm, 20 * mm, 20 * mm, 22 * mm, 20 * mm, 24 * mm, W - 122 * mm],
    ["l", "r", "r", "r", "r", "r", "r"], hi={1: GRN, 6: RED}))
F.append(Spacer(1, 4))
F.append(Paragraph("⚠️ <b>这张表推翻了上一份报告的排序方法。ISRG 跌破自己的 buy_below 22.4%,绝对估值仍是 53 倍 FCF、"
                   "1.89% 收益率;INTU 只在线内 2.0%,却是 10.3 倍。各家 buy_below 的宽松度差了 5 倍。</b><br/>"
                   "<b>「距 buy_below 的百分比」只能在同一个名字的时间序列上用,不能横向排名。</b>", S["quote"]))

F.append(P("6.3 buy_below 该往哪走?", "h2"))
F.append(tbl([["支持上修", "支持下修 / 抵消"],
              ["FY2026 FCF $8,663M,远高于卡写作时能看到的 FY2025 $6,123M(<b>+41.5%</b>)<br/>"
               "营业利润率再扩 1.3pp 到 27.4%,经营杠杆持续兑现<br/>"
               "TurboTax 单量侵蚀温和(−2%)而非崩塌<br/>回购从 $2,772M 提到 $5,412M",
               "<b>FY2027 指引 $23,279–23,512M,+9~10%</b>(按 10-K 营收算 +8.5~9.6%)—— 从 +13.9% 明显减速<br/>"
               "OCF/NI 194% 的缺口未闭合(§5.1),$8,663M 可能含一次性<br/>"
               "SBC 占营收 9.6%,真实 owner earnings 应取 $6,607M"]],
             [W / 2, W / 2]))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>结论:方向是上修,但幅度被 FY2027 减速和 §5.1 的疑点吃掉。本次刷新决定 buy_below 维持 ~$328 不动,"
                   "等 §5.1 闭合后再正式重推。把「不动」当成一个显式决定,不是省事 —— 两股力量方向相反且量级相当,"
                   "强行改一个数是伪精确。</b>", S["quote"]))

F.append(PageBreak())
F.append(P("七、FY2027 的三个变化(2026-08-01 起生效)", "h1"))
F.append(tbl([["变化", "内容", "影响"],
              ["<b>指引减速</b>", "全年营收 $23,279–23,512M = <b>+9~10%</b>",
               "base case 增速假设要从 ~14% 下调。<b>最实质的一条</b>"],
              ["<b>Mailchimp 独立分部</b>", "从 Global Business Solutions 拆出",
               "✅ 透明度提升;⚠️ 提高独立商誉减值测试概率(§5.2)"],
              ["<b>non-GAAP 口径变更</b>", "<b>SBC 不再从 non-GAAP 中剔除</b>",
               "✅ 会计诚实度实质提升;⚠️ 压低 non-GAAP,FY2027 与历史不可比"]],
             [34 * mm, 52 * mm, W - 86 * mm]))
F.append(Spacer(1, 4))
F.append(P("第三条值得单独表扬:<b>主动把 SBC 放回 non-GAAP,是极少数公司愿意做的自我约束。"
           "它同时说明 §5.3 那个问题管理层自己也认。</b>", "p"))

F.append(P("八、Kill Criteria(三态)", "h1"))
F.append(tbl([
    ["Kill", "阈值(可观测)", "现状", "触发后动作"],
    ["<b>K-A</b> TurboTax 单量", "总单量连 2 年降幅 &gt;5%,或 Online 单量转为 &gt;3% 降", "🟢 FY26 −2%", "机制破裂 → Consumer base 下调"],
    ["<b>K-B</b> 单价补偿失效", "TurboTax 营收增速 &lt; 单量降幅绝对值", "🟢 +7% vs −2%", "收割机制到头 → base 重估"],
    ["<b>K-C</b> 盈利质量", "FCF 持续 &gt;150% 净利且无法从调节项解释", "🟡 FY26 190%,<b>未核实</b>", "闭合前 base 取 FCF−SBC"],
    ["<b>K-D</b> Mailchimp 减值", "FY2027 出现商誉减值", "🟡 独立分部后概率上升", "非现金,不改 FCF;operator 记分卡下调"],
    ["<b>K-E</b> GBS 减速", "QuickBooks Online Accounting 连 2 季 &lt;15%", "🟢 FY26 +23%", "最硬那条腿松动 → 直接下调 verdict"],
    ["<b>K-F</b> 估值纪律", "买入价隐含 10y IRR &lt;8%", "🟢 现价在 buy_below 线内", "维持 0 仓位"],
], [26 * mm, 56 * mm, 30 * mm, W - 112 * mm], hi={3: YEL, 4: YEL}))
F.append(Spacer(1, 3))
F.append(P("<b>当前总览:K-A / K-B / K-E / K-F 绿;K-C / K-D 黄。无红。</b>", "p"))

F.append(P("九、结论与下一步", "h1"))
F.append(P("<b>本次刷新的净结果:</b><br/>"
           "① 卡里点名的封顶项(FY2026 全年)解除了,而且交付好于假设。<br/>"
           "② <b>但封顶没有消失,只是换了地方</b> —— 从「等财报」变成「盈利质量待验证」(OCF/NI 194% + SBC 9.6%)。<br/>"
           "③ verdict 维持 STARTER / 初始 2% / 上限 6%,价格仍不是约束。<br/>"
           "④ buy_below 维持 ~$328,<b>作为一个显式决定</b> —— 上修与减速两股力量量级相当。", "p"))
F.append(tbl([["#", "动作", "为什么"],
              ["<b>1</b>", "<b>逐行读 FY2026 10-K 现金流量表调节项</b>",
               "闭合 §5.1。<b>这一项决定 base 是 $8,663M 还是 $6,607M,直接决定 buy_below 往哪走</b>"],
              ["2", "把 FY2027 +9~10% 指引打进 10y IRR 模型", "卡的 +10.2% 是用旧增速算的"],
              ["3", "监控 FY2027 Q1(约 2026-11)Mailchimp 独立分部首次披露", "§5.2 减值信号 + Mailchimp 真实体量"],
              ["4", "若 1 的结论是「质量干净」→ 重开 IC panel 评实际建仓", "这是全表唯一走到这一步的名字"]],
             [8 * mm, 62 * mm, W - 70 * mm], hi={1: GRN}))

F.append(P("附:数据来源", "h1"))
F.append(P("• <b>年度财务 FY2022–FY2026</b>:SEC EDGAR XBRL companyconcept API,仅采 form=10-K / fp=FY 的 365 天期间<br/>"
           "• <b>FY2026 10-K</b>:accession 0000896878-26-000037,filed 2026-09-09,period 2026-07-31<br/>"
           "• <b>分部 / TurboTax 单量 / FY2027 指引</b>:8-K filed 2026-08-25,EX-99.01 新闻稿原文<br/>"
           "• <b>价格</b>:Yahoo Finance chart API,2026-09-11 收盘<br/>"
           "• <b>同业 FCF 对照</b>:各家最近一个完整财年 10-K", "p"))
F.append(Paragraph("<b>未做</b>:10-K 现金流量表逐行调节项核实(§5.1)、10y IRR 模型重算、claim ledger 回挂。<br/>"
                   "<b>本文件是 DECISION_DRAFT 级刷新,completeness ~72%,不是 COMPLETE。</b>", S["quote"]))

SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                  topMargin=16 * mm, bottomMargin=18 * mm,
                  title="INTU 详细调研报告 2026-09-13", author="yc_research"
                  ).build(F, onFirstPage=footer, onLaterPages=footer)
print("PDF ->", OUT, os.path.getsize(OUT), "bytes")
