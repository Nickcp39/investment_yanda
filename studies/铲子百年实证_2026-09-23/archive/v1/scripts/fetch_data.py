# -*- coding: utf-8 -*-
"""铲子百年实证 · 数据采集脚本
从 Yahoo Finance chart API 批量抓取"铲子"标的的长期复权月线(adjclose)。
标的清单 = 从《电力需求与电力公司盈利_百年实证_2026-09-16》11 个案例中
提取的"上游工具商/供应商/服务商"(卖铲子的人)。
"""
import urllib.request, json, os, time, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 标的清单：ticker -> (名称, 案例归属, 锁类型初判)
# 锁类型：AFTERMARKET=售后锁定  OLIGOPOLY=寡头/专利  LICENSE=监管牌照
#         WINDOW=窗口稀缺(供给在扩)  BARE=裸铲子(可替换)  MIXED=混合
TICKERS = {
    # ---- 航空：发动机 + 零部件（"带锁铲子"最硬的案例）----
    "GE":      ("通用电气/GE Aerospace", "航空/电力", "AFTERMARKET"),
    "RTX":     ("雷神技术(Pratt & Whitney)", "航空", "AFTERMARKET"),
    "RR.L":    ("劳斯莱斯 Rolls-Royce", "航空", "AFTERMARKET"),
    "SAF.PA":  ("赛峰 Safran", "航空", "AFTERMARKET"),
    "TDG":     ("TransDigm 专有零部件", "航空", "OLIGOPOLY"),
    "HWM":     ("Howmet 专有零部件", "航空", "OLIGOPOLY"),
    "SPR":     ("Spirit AeroSystems 机身结构件", "航空", "BARE"),
    "AER":     ("AerCap 飞机租赁", "航空", "MIXED"),
    # ---- 电力设备 + 当前 AI 电力铲子 ----
    "ETN":     ("伊顿 Eaton 电力设备/变压器", "电力/AI电力", "MIXED"),
    "HUBB":    ("Hubbell 变压器/电网", "电力/AI电力", "MIXED"),
    "ENR.DE":  ("西门子能源 Siemens Energy", "电力/AI电力", "WINDOW"),
    "7011.T":  ("三菱重工 MHI 燃气轮机", "电力/AI电力", "WINDOW"),
    "6501.T":  ("日立 Hitachi 变压器/电网", "电力/AI电力", "MIXED"),
    "GEV":     ("GE Vernova 燃气轮机", "AI电力", "WINDOW"),
    "VRT":     ("Vertiv 散热/电力设备", "AI电力", "WINDOW"),
    # ---- 油服（石油 + 页岩案例）----
    "SLB":     ("斯伦贝谢 Schlumberger 油服", "石油/页岩", "MIXED"),
    "HAL":     ("哈里伯顿 Halliburton 油服压裂", "石油/页岩", "BARE"),
    "BKR":     ("贝克休斯 Baker Hughes 油服", "石油/页岩", "BARE"),
    "NOV":     ("NOV 钻井设备", "石油", "BARE"),
    # ---- 光纤/网络设备（光纤案例）----
    "CSCO":    ("思科 Cisco 网络设备", "光纤", "WINDOW"),
    "GLW":     ("康宁 Corning 光纤/玻璃", "光纤", "MIXED"),
    "CIEN":    ("Ciena 光网络设备", "光纤", "BARE"),
    # ---- 挖矿/工程设备（钢铁/矿业案例）----
    "CAT":     ("卡特彼勒 Caterpillar 挖矿设备", "钢铁/矿业", "OLIGOPOLY"),
    "6301.T":  ("小松 Komatsu 挖矿设备", "钢铁/矿业", "OLIGOPOLY"),
    # ---- 光伏设备（光伏案例）----
    "AMAT":    ("应用材料 AMAT 半导体/光伏设备", "光伏/半导体", "OLIGOPOLY"),
    "SEDG":    ("SolarEdge 光伏逆变器", "光伏", "BARE"),
    "ENPH":    ("Enphase 光伏逆变器", "光伏", "BARE"),
    # ---- 造船（航运案例）----
    "010140.KS": ("三星重工 造船", "航运", "BARE"),
    "329180.KS": ("HD现代重工 造船", "航运", "BARE"),
    "042660.KS": ("韩华海洋(原大宇造船) 造船", "航运", "BARE"),
    # ---- 汽车零部件（汽车案例）----
    "6902.T":  ("电装 Denso 汽车零部件", "汽车", "MIXED"),
    "MGA":     ("麦格纳 Magna 汽车零部件", "汽车", "BARE"),
    "APTV":    ("安波福 Aptiv(原德尔福) 汽车零部件", "汽车", "BARE"),
    # ---- 基准 ----
    "SPY":     ("标普500 ETF", "基准", "-"),
    "^GSPC":   ("标普500指数", "基准", "-"),
}

def fetch(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1mo&period1=0&period2=9999999999&events=div%2Csplit"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    r = urllib.request.urlopen(req, timeout=30)
    d = json.loads(r.read().decode())
    res = d["chart"]["result"][0]
    ts = res.get("timestamp", [])
    adj = res["indicators"]["adjclose"][0]["adjclose"]
    out = []
    for t, a in zip(ts, adj):
        if a is None:
            continue
        dt = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        out.append([dt, round(a, 4)])
    return out

def main():
    results = {}
    for tk, (name, case, lock) in TICKERS.items():
        try:
            rows = fetch(tk)
            results[tk] = {"name": name, "case": case, "lock": lock, "rows": rows}
            first = rows[0][0]
            last = rows[-1][0]
            print(f"OK  {tk:12s} {name[:24]:24s} {len(rows):4d}月 {first} -> {last}")
        except Exception as e:
            results[tk] = {"name": name, "case": case, "lock": lock, "rows": [], "error": repr(e)[:100]}
            print(f"FAIL {tk:12s} {name[:24]:24s} {repr(e)[:80]}")
        time.sleep(0.4)

    with open(os.path.join(DATA_DIR, "shovel_prices.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print("\nSaved ->", os.path.join(DATA_DIR, "shovel_prices.json"))

if __name__ == "__main__":
    main()
