"""下载日本泡沫后 / 中国现在 对照所需的原始数据到 markets/data/（已有文件不重下）。

来源：Yahoo v8 chart（日线+分红）、东方财富 kline（上证综指日线）、中证指数公司 index-perf API、
日本财务省 jgbcm_all.csv、中债国债收益率曲线年度 xlsx、世界银行 CPI API、Ken French Data Library、
日经平均总回报指数 CSV、FRED（curl；2026-10-16 本机访问 FRED 超时，FRED 文件取自上级目录 ../data 的
2026-10-15/16 缓存：DEXJPUS INTDSRJPM193N IRSTCI01JPM156N QJPN628BIS QCNN628BIS 等）。
运行：python fetch_markets.py
"""
import subprocess
import time
import zipfile
from pathlib import Path

D = Path(__file__).resolve().parent / "data"
D.mkdir(exist_ok=True)
(D / "chinabond").mkdir(exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

YAHOO = ["^N225", "^HSI", "EWJ", "1306.T", "1308.T", "1343.T", "510880.SS", "1478.T", "1489.T", "7203.T", "4063.T",
         "6861.T", "7974.T", "9983.T", "8306.T", "8801.T", "1801.T", "0688.HK", "000002.SZ", "2007.HK", "JPY=X"]
FRED = ["IRLTLT01JPM156N", "INTDSRJPM193N", "IRSTCI01JPM156N", "QJPN628BIS", "QCNN628BIS", "DEXJPUS",
        "IR3TIB01CNM156N", "INTDSRCNM193N"]
CSI = ["000300", "H00300", "000922", "H00922"]
EM = ["1.000001", "1.000300", "1.000922", "1.000015"]
FRENCH = ["Japan_6_Portfolios_ME_BE-ME_CSV.zip", "Japan_3_Factors_CSV.zip", "F-F_International_Countries.zip"]
CHINABOND_ID = "2c9081e50a2f9606010a3068cae70001"  # 中债国债收益率曲线


def get(url, path, timeout=120):
    if path.exists() and path.stat().st_size > 500:
        return
    out = subprocess.run(["curl", "-s", "-L", "-m", str(timeout), "-A", UA, url], capture_output=True).stdout
    if len(out) > 500:
        path.write_bytes(out)
    print(f"{path.name}: {len(out)} bytes")
    time.sleep(0.3)


for tk in YAHOO:
    q = tk.replace("^", "%5E").replace("=", "%3D")
    get(f"https://query1.finance.yahoo.com/v8/finance/chart/{q}?period1=0&period2=9999999999&interval=1d&events=div%7Csplit",
        D / f"yahoo_{tk.replace('^', 'IDX_').replace('=', '_')}.json")
for s in EM:
    get(f"https://push2his.eastmoney.com/api/qt/stock/kline/get?secid={s}&fields1=f1,f2,f3&fields2=f51,f52,f53,f54,f55"
        f"&klt=101&fqt=0&beg=19900101&end=20261231", D / f"em_{s}.json")
for c in CSI:
    get(f"https://www.csindex.com.cn/csindex-home/perf/index-perf?indexCode={c}&startDate=20050101&endDate=20261016",
        D / f"csi_{c}.json")
get("https://www.mof.go.jp/jgbs/reference/interest_rate/data/jgbcm_all.csv", D / "mof_jgbcm_all.csv")
for y in range(2006, 2027):
    get(f"https://yield.chinabond.com.cn/cbweb-mn/yc/downYearBzqx?year={y}&&wrjxCBFlag=0&&zblx=txy&ycDefId={CHINABOND_ID}"
        f"&&locale=zh_CN", D / "chinabond" / f"cgb_{y}.xlsx")
get("https://api.worldbank.org/v2/country/JPN;CHN/indicator/FP.CPI.TOTL.ZG?format=json&per_page=300", D / "wb_cpi.json")
for z in FRENCH:
    get(f"https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/{z}", D / z)
for z, sub in [("Japan_6_Portfolios_ME_BE-ME_CSV.zip", "ff"), ("Japan_3_Factors_CSV.zip", "ff"), ("F-F_International_Countries.zip", "ff_intl")]:
    if (D / z).exists():
        zipfile.ZipFile(D / z).extractall(D / sub)
get("https://indexes.nikkei.co.jp/nkave/historical/nikkei_225_total_return_index_monthly_en.csv", D / "nikkei225_tr_monthly_en.csv")
get("https://indexes.nikkei.co.jp/nkave/historical/nikkei_225_total_return_index_daily_jp.csv", D / "nikkei225_tr_daily_jp.csv")
for sid in FRED:
    get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", D / f"{sid}.csv", timeout=60)
