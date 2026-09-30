"""Compact, Chinese research edition. Run with bundled Python (ReportLab)."""
import pathlib,re,html,json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate,PageTemplate,Frame,Paragraph,Table,TableStyle,Spacer,PageBreak,Image,KeepTogether,CondPageBreak
from PIL import Image as PILImage
BASE=pathlib.Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
OUT=ROOT/'output/pdf/铲子百年实证_深研版_2026-09-23.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('CN','C:/Windows/Fonts/msyh.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('CNBold','C:/Windows/Fonts/msyhbd.ttc',subfontIndex=0))
pdfmetrics.registerFontFamily('CN',normal='CN',bold='CNBold',italic='CN',boldItalic='CNBold')
ink=colors.HexColor('#202c39');blue=colors.HexColor('#235e7c');muted=colors.HexColor('#5e6b76');line=colors.HexColor('#cdd8e0');soft=colors.HexColor('#edf3f7')
W,H=A4;M=18*mm;WIDTH=W-2*M
styles={
 'p':ParagraphStyle('body',fontName='CN',fontSize=9.1,leading=14.2,textColor=ink,spaceAfter=6,wordWrap='CJK',allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('title',fontName='CNBold',fontSize=30,leading=40,textColor=blue,spaceBefore=35,spaceAfter=20,wordWrap='CJK',keepWithNext=1),
 'h2':ParagraphStyle('section',fontName='CNBold',fontSize=14,leading=20,textColor=blue,spaceBefore=16,spaceAfter=9,wordWrap='CJK',keepWithNext=1),
 'h3':ParagraphStyle('subsection',fontName='CNBold',fontSize=10.6,leading=16,textColor=ink,spaceBefore=10,spaceAfter=5,wordWrap='CJK',keepWithNext=1),
 'cell':ParagraphStyle('cell',fontName='CN',fontSize=8.0,leading=11.8,textColor=ink,wordWrap='CJK'),
 'cellr':ParagraphStyle('number',fontName='CN',fontSize=8.0,leading=11.8,textColor=ink,wordWrap='CJK',alignment=2),
 'head':ParagraphStyle('head',fontName='CNBold',fontSize=8.0,leading=11.8,textColor=blue,wordWrap='CJK'),
 'caption':ParagraphStyle('caption',fontName='CN',fontSize=7.8,leading=11.8,textColor=muted,spaceAfter=7,wordWrap='CJK'),
 'quote':ParagraphStyle('quote',fontName='CN',fontSize=9,leading=14,textColor=blue,leftIndent=8,borderPadding=7,backColor=soft,spaceAfter=8,wordWrap='CJK'),
}
def inline(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:'<a href="'+m[2].replace('"','%22')+'" color="#235e7c">'+m[1]+'</a>',s)
    s=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<font color="#235e7c">\1</font>',s)
    return s
def P(t,kind='p'): return Paragraph(inline(t),styles[kind])
class Doc(BaseDocTemplate):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw);self.chapter='';self.entries=[]
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='section':
            title=f.getPlainText();key='sec'+str(len(self.entries));self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level=0,closed=False);self.entries.append({'title':title,'page':self.page});self.chapter=title
def page(canvas,doc):
    canvas.saveState();canvas.setTitle('铲子百年实证：产业扩张的钱，究竟留在了谁手里？');canvas.setAuthor('Financial Analysis Lab');canvas.setSubject('1926-2026 行业实证、经营案例与 AI 电力研究')
    if doc.page>1:
        canvas.setFont('CN',7.2);canvas.setFillColor(muted);canvas.drawString(M,H-11*mm,'铲子百年实证  /  深研版');canvas.drawRightString(W-M,H-11*mm,'1926-2026  ·  2026.09.23')
        canvas.setStrokeColor(line);canvas.setLineWidth(.5);canvas.line(M,H-13.5*mm,W-M,H-13.5*mm)
    else:
        canvas.setFillColor(blue);canvas.rect(M,H-22*mm,32*mm,2*mm,fill=1,stroke=0)
    canvas.setStrokeColor(line);canvas.line(M,14*mm,W-M,14*mm);canvas.setFont('CN',7.2);canvas.setFillColor(muted);canvas.drawString(M,9.7*mm,'行业回报与案例研究  |  事实、计算与推论分别标示');canvas.drawRightString(W-M,9.7*mm,str(doc.page));canvas.restoreState()
def build_table(block):
    rows=[]
    for s in block:
        row=[v.strip() for v in s.strip('| ').split('|')]
        if all(re.fullmatch(r':?-+:?',v) for v in row):continue
        rows.append(row)
    n=len(rows[0]);assert all(len(r)==n for r in rows)
    head=rows[0]
    if n==7 and head[0]=='标的' and '可用区间' in head:
        widths=[.12,.19,.075,.075,.075,.105,.36]
    elif n==7 and head[0]=='标的':widths=[.14,.10,.10,.10,.13,.13,.30]
    elif n==7:widths=[.19]+[.135]*6
    elif n==5:widths=[.28,.18,.18,.18,.18]
    elif n==4:widths=[.19,.27,.27,.27] if not any('十亿' in x or '百万' in x for x in head) else [.43,.19,.19,.19]
    elif n==3:widths=[.19,.405,.405]
    elif n==2:widths=[.32,.68]
    else:widths=[1/n]*n
    widths=[WIDTH*x/sum(widths) for x in widths]
    numeric=[sum(bool(re.match(r'^[+\-]?\d',r[j])) for r in rows[1:])>len(rows[1:])*.65 for j in range(n)]
    cells=[[P(v,'head' if i==0 else 'cellr' if numeric[j] and j else 'cell') for j,v in enumerate(row)] for i,row in enumerate(rows)]
    t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT',spaceBefore=4,spaceAfter=10)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),soft),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.65,blue),('LINEBELOW',(0,1),(-1,-1),.3,line),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#fafcfd')])]))
    return t
def make_story():
    lines=(BASE/'report.md').read_text(encoding='utf-8').splitlines();story=[];i=0
    while i<len(lines):
        s=lines[i].strip()
        if not s:i+=1;continue
        if s=='<!-- PAGEBREAK -->':
            following=next((x.strip() for x in lines[i+1:] if x.strip()),'')
            story.append(CondPageBreak(130) if re.match(r'^## (4\.|11\.|14\.)',following) else PageBreak());i+=1;continue
        if s.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i].strip());i+=1
            story.append(build_table(block));continue
        if s.startswith('!['):
            target=re.search(r'\]\(([^)]+)\)',s)[1];p=BASE/target
            with PILImage.open(p) as im:w,h=im.size
            ww=WIDTH;hh=ww*h/w
            if hh>104*mm:ww*=104*mm/hh;hh=104*mm
            story.append(KeepTogether([Image(str(p),width=ww,height=hh,hAlign='CENTER'),Spacer(1,7)]));i+=1;continue
        if s.startswith('# '):story.append(P(s[2:],'h1'));i+=1;continue
        if s.startswith('## '):story.append(CondPageBreak(65));story.append(P(s[3:],'h2'));i+=1;continue
        if s.startswith('### '):story.append(CondPageBreak(48));story.append(P(s[4:],'h3'));i+=1;continue
        if s.startswith('> '):story.append(P(s[2:],'quote'));i+=1;continue
        if s.startswith('- '):story.append(P('• '+s[2:]));i+=1;continue
        para=[s];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||!\[|>|- |<!--)',lines[i].strip()):para.append(lines[i].strip());i+=1
        txt=' '.join(para);kind='caption' if txt.startswith(('来源：','图 4 金额','表内除','原始下载：')) else 'p';story.append(P(txt,kind))
    return story
doc=Doc(str(OUT),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=19*mm,bottomMargin=19*mm,title='铲子百年实证')
frame=Frame(M,19*mm,WIDTH,H-38*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='research',frames=frame,onPage=page)])
doc.build(make_story())
(BASE/'data/pdf_structure.json').write_text(json.dumps({'path':str(OUT),'pages':doc.page,'sections':doc.entries},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'path':str(OUT),'pages':doc.page,'bytes':OUT.stat().st_size},ensure_ascii=False))
