import datetime, hashlib, io, json, pathlib, urllib.request, zipfile
BASE=pathlib.Path(__file__).resolve().parents[1]
OUT=BASE/'data/industry_raw'
FILES={'ff49':'49_Industry_Portfolios_CSV.zip','factors':'F-F_Research_Data_Factors_CSV.zip','definitions':'Siccodes49.zip'}
if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    manifest=[]
    for name,filename in FILES.items():
        url='https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/'+filename
        path=OUT/filename
        if not path.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=45) as response: path.write_bytes(response.read())
        raw=path.read_bytes()
        z=zipfile.ZipFile(io.BytesIO(raw))
        txt=z.read(z.namelist()[0]).decode('utf-8-sig',errors='replace')
        (OUT/(name+'.txt')).write_text(txt,encoding='utf-8')
        manifest.append({'name':name,'url':url,'sha256':hashlib.sha256(raw).hexdigest(),'downloaded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        print(name,len(raw),txt[:1200])
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
