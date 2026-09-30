"""Independent arithmetic and PDF structure checks; visual QA is separate."""
import pathlib,json,math,re,csv,hashlib
from pypdf import PdfReader
import pdfplumber
BASE=pathlib.Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
d=json.loads((BASE/'data/industry_analysis.json').read_text(encoding='utf-8'))
checks=[]
def check(ok,label):
 checks.append({'pass':bool(ok),'check':label})
 if not ok: print('FAIL',label)
def independent_table(file,marker=None):
 lines=(BASE/'data/industry_raw'/file).read_text().splitlines()
 if marker:lines=lines[next(i for i,s in enumerate(lines) if marker in s)+1:]
 lines=[s for s in lines if s.strip()];head=next(i for i,s in enumerate(lines) if s.startswith(','));records={}
 keys=next(csv.reader([lines[head]]))[1:]
 for s in lines[head+1:]:
  row=next(csv.reader([s]));date=row[0].strip()
  if not re.fullmatch(r'\d{6}',date):break
  records[date]={k.strip():float(v)/100 for k,v in zip(keys,row[1:])}
 return records
raw=independent_table('ff49.txt','Average Value Weighted Returns -- Monthly');fac=independent_table('factors.txt')
check(len(d['dates'])==1201,'1,201 consecutive monthly returns')
offsets=[int(s[:4])*12+int(s[4:]) for s in d['dates']]
check(all(b-a==1 for a,b in zip(offsets,offsets[1:])),'No missing months')
for k,summary in d['summary'].items():
 r=[fac[s]['Mkt-RF']+fac[s]['RF'] if k=='Market' else raw[s][k] for s in d['dates']]
 check(all(abs(a-b)<1e-12 for a,b in zip(r,d['monthly'][k])),'Raw table reconciliation '+k)
 wealth=math.prod(1+x for x in r);cg=(wealth**(12/len(r))-1)*100
 check(abs(cg-summary['cagr'])<1e-9,'Product based independent CAGR '+k)
 w=peak=1;dd=0
 for x in r:w*=1+x;peak=max(peak,w);dd=min(dd,w/peak-1)
 check(abs(dd*100-summary['maxdd'])<1e-8,'Independent drawdown '+k)
 if k!='Market':
  wins=0
  for window in d['rolling'][k]:
   i=d['dates'].index(window['start']); j=d['dates'].index(window['end']);check(j-i+1==120,'120 month window '+k+window['start'])
   a=math.prod(1+x for x in r[i:j+1])**.1-1;b=math.prod(1+x for x in d['monthly']['Market'][i:j+1])**.1-1
   check(abs((a-b)*100-window['excess'])<1e-8,'Rolling excess '+k+window['start']);wins+=a>b
  check(wins==summary['win_count'] and len(d['rolling'][k])==91,'Rolling counts '+k)
pdf=ROOT/'output/pdf/铲子百年实证_深研版_2026-09-23.pdf';reader=PdfReader(pdf)
check(len(reader.pages)==22,'Final PDF page count')
annots=sum(len(p.get('/Annots',[])) for p in reader.pages)
check(annots>=41,'Clickable source annotations')
texts=[p.extract_text() for p in reader.pages]
check(all(len(t)>150 for t in texts),'No blank or almost blank pages')
check(not any('\ufffd' in t for t in texts),'No replacement glyphs in extracted text')
check('{{' not in (BASE/'report.md').read_text(encoding='utf-8'),'No unexpanded report fields')
with pdfplumber.open(pdf) as p:
 for n,page in enumerate(p.pages,1):
  # ReportLab CJK layout permits end punctuation to hang by up to one em.
  bad=[c for c in page.chars if c['x0']<47 or c['x1']>page.width-(40 if c['text'] in '。，、；：！？）”' else 47) or c['top']<12 or c['bottom']>page.height-16]
  check(not bad,'Text bounds allowing CJK hanging punctuation '+str(n))
report=(BASE/'report.md').read_text(encoding='utf-8')
for v in ['10.35','10.97','11.23','12.76','9.21','8.73','9.22']:
 check(v in report,'Century figure in report '+v)
out={'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL','checks':len(checks),'pages':len(reader.pages),'source_annotations':annots,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'scope':'Independent arithmetic from archived raw industry files and PDF structure. Not causal validation or complete securities corporate-action audit.','details':checks}
(BASE/'data/research_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='details'},ensure_ascii=False,indent=2))
raise SystemExit(out['status']!='PASS')
