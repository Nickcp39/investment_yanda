"""保存带元数据的原始 Yahoo 响应；不覆盖原始研究快照。Python 标准库。"""
import concurrent.futures, datetime as dt, hashlib, json, pathlib, time, urllib.request
from urllib.parse import quote

BASE = pathlib.Path(__file__).resolve().parents[1]
OUT = BASE / 'data' / 'audit_raw'
ASOF = dt.datetime(2026, 9, 24, tzinfo=dt.timezone.utc)
EXTRA = ['ASML', 'LRCX', 'KLAC', 'HEI', 'WAB', 'FLR', 'ROK', 'DE']

def fetch(ticker, interval='1mo'):
    url = ('https://query1.finance.yahoo.com/v8/finance/chart/' + quote(ticker, safe='')
           + '?interval=' + interval + '&period1=0&period2=' + str(int(ASOF.timestamp()))
           + '&events=div%2Csplit%2CcapitalGains')
    filename = 'KRW_daily.json' if ticker == 'KRW=X' and interval == '1d' else ticker.replace('^', '_').replace('=', '_') + '.json'
    path = OUT / filename
    if path.exists():
        return {'ticker': ticker, 'status': 'cached', 'path': str(path.relative_to(BASE)),
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'url': url,
                'snapshot_file_mtime_utc': dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc).isoformat()}
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=25) as response:
                raw = response.read()
            parsed = json.loads(raw)
            if not parsed.get('chart', {}).get('result'):
                raise ValueError(str(parsed)[:200])
            path.write_bytes(raw)
            return {'ticker': ticker, 'status': 'ok', 'path': str(path.relative_to(BASE)),
                    'sha256': hashlib.sha256(raw).hexdigest(), 'url': url,
                    'retrieved_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        except Exception as exc:
            error = str(exc)
            time.sleep(1 + attempt)
    return {'ticker': ticker, 'status': 'error', 'error': error, 'url': url}

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    original = json.loads((BASE / 'data/shovel_prices.json').read_text(encoding='utf-8'))
    tickers = list(original) + EXTRA + ['GBPUSD=X', 'EURUSD=X', 'JPY=X', 'KRW=X']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, tickers))
    results.append(fetch('KRW=X', '1d'))
    (BASE / 'data/audit_fetch_manifest.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    for r in results:
        print(r['ticker'], r['status'], r.get('error', ''))
