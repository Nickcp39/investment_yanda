# -*- coding: utf-8 -*-
"""
2008 年以来：通胀(CPI) vs 核心城市房价(Case-Shiller) vs 美股(SPY/QQQ)
- 房价仅取一线核心城市：纽约、波士顿、旧金山、洛杉矶、圣地亚哥
- 基准 2008-01=100
- 图1：名义累计涨幅（对数刻度）
- 图2：扣除通胀后的实际涨幅（线性刻度，CPI 恒为 100 作基准）
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/backtests/房价_通胀_美股对比_2008起'
os.makedirs(OUT, exist_ok=True)

CPI_PATH = r'D:/work/investment/financial-analysis-lab/backtests/黄金_货币供应_估值_2026-08-07/data/us_cpi_monthly.csv'
CS_PATH  = r'D:/work/investment/financial-analysis-lab/房价分析/data/us_case_shiller.csv'
GSPC_PATH = r'D:/work/investment/financial-analysis-lab/studies/美股风气40年_兴衰统计_2026-10-06/data/raw/prices/IDX_GSPC.csv.gz'
NDX_PATH = r'D:/work/investment/financial-analysis-lab/studies/美股风气40年_兴衰统计_2026-10-06/data/raw/prices/IDX_NDX.csv.gz'

# ---- 读取 ----
cpi = pd.read_csv(CPI_PATH)
cpi['date'] = pd.to_datetime(cpi['month'])
cpi = cpi.set_index('date')['cpi_u_nsa'].sort_index()

cs = pd.read_csv(CS_PATH)
cs['date'] = pd.to_datetime(cs['Date'])
cs = cs.set_index('date').sort_index()

gspc = pd.read_csv(GSPC_PATH, parse_dates=['date']).set_index('date')['adjclose']
ndx = pd.read_csv(NDX_PATH, parse_dates=['date']).set_index('date')['adjclose']

# ---- 统一重采样到月末 ----
cpi_m = cpi.resample('ME').last()
cs_m = cs.resample('ME').last()
gspc_m = gspc.resample('ME').last()
ndx_m = ndx.resample('ME').last()

BASE = pd.Timestamp('2008-01-31')
START = pd.Timestamp('2008-01-31')
END = pd.Timestamp('2026-02-28')

CITIES = {
    'NY-New York': '纽约',
    'MA-Boston': '波士顿',
    'CA-San Francisco': '旧金山',
    'CA-Los Angeles': '洛杉矶',
    'CA-San Diego': '圣地亚哥',
}
COLORS = {
    '纽约': '#4da6ff',
    '波士顿': '#56d4a3',
    '旧金山': '#ffa64d',
    '洛杉矶': '#ff6b6b',
    '圣地亚哥': '#c792ea',
}
CPI_COLOR = '#9aa0a6'
SPY_COLOR = '#f0f6fc'
QQQ_COLOR = '#ffd166'


def norm(s):
    s = s.loc[(s.index >= START) & (s.index <= END)]
    return s / s.asof(BASE) * 100.0


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# ================= 图1：名义累计涨幅（对数刻度） =================
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.plot(norm(cpi_m).index, norm(cpi_m), color=CPI_COLOR, linewidth=2.4, linestyle='--', label='CPI 通胀')
for col, cn in CITIES.items():
    ax.plot(norm(cs_m[col]).index, norm(cs_m[col]), color=COLORS[cn], linewidth=1.9, label=f'{cn}房价')
ax.plot(norm(gspc_m).index, norm(gspc_m), color=SPY_COLOR, linewidth=2.8, label='SPY（标普500）')
ax.plot(norm(ndx_m).index, norm(ndx_m), color=QQQ_COLOR, linewidth=2.8, label='QQQ（纳斯达克100）')

ax.set_yscale('log')
ax.set_ylim(80, 1600)
ax.axhline(100, color='#6b7280', linewidth=1, linestyle='-', alpha=0.6)

ax.set_title('2008 年以来：通胀 vs 核心城市房价 vs 美股（名义，2008-01=100，对数刻度）',
             color='#e8eaed', fontsize=14, fontweight='bold', pad=14)
ax.set_ylabel('累计涨幅指数（2008-01=100）', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(pd.Timestamp('2008-01-01'), pd.Timestamp('2026-06-01'))
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7, which='both')
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

ax.legend(loc='upper left', facecolor='#1f2428', edgecolor='#3a4046',
          labelcolor='#e8eaed', fontsize=9.5, ncol=2)
plt.tight_layout()
p1 = os.path.join(OUT, '通胀_房价_美股_名义_2008起.png')
plt.savefig(p1, facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.close(fig)

# ================= 图2：扣除通胀后的实际涨幅（线性刻度） =================
cpi_n = norm(cpi_m)

fig, ax = plt.subplots(figsize=(13, 7.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.axhline(100, color=CPI_COLOR, linewidth=2.2, linestyle='--', label='CPI 通胀（基准=100）')
for col, cn in CITIES.items():
    real = norm(cs_m[col]) / cpi_n * 100.0
    ax.plot(real.index, real, color=COLORS[cn], linewidth=1.9, label=f'{cn}房价（实际）')
ax.plot(norm(gspc_m).index, norm(gspc_m) / cpi_n * 100.0, color=SPY_COLOR, linewidth=2.8, label='SPY（实际）')
ax.plot(norm(ndx_m).index, norm(ndx_m) / cpi_n * 100.0, color=QQQ_COLOR, linewidth=2.8, label='QQQ（实际）')

ax.set_ylim(60, 850)
ax.set_title('2008 年以来：扣除通胀后的实际购买力增长（2008-01=100，线性刻度）',
             color='#e8eaed', fontsize=14, fontweight='bold', pad=14)
ax.set_ylabel('实际价值指数（扣除 CPI，2008-01=100）', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(pd.Timestamp('2008-01-01'), pd.Timestamp('2026-06-01'))
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

ax.legend(loc='upper left', facecolor='#1f2428', edgecolor='#3a4046',
          labelcolor='#e8eaed', fontsize=9.5, ncol=2)
plt.tight_layout()
p2 = os.path.join(OUT, '通胀_房价_美股_实际_2008起.png')
plt.savefig(p2, facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.close(fig)

# ================= 导出汇总表 =================
def total_ret(s):
    return s.asof(END) / s.asof(BASE) - 1

cpi_ret = total_ret(cpi)
rows = [{'资产': 'CPI 通胀', '名义涨幅': cpi_ret, '实际涨幅': 0.0}]
for col, cn in CITIES.items():
    r = total_ret(cs[col])
    rows.append({'资产': f'{cn}房价', '名义涨幅': r, '实际涨幅': (1 + r) / (1 + cpi_ret) - 1})
for name, s in [('SPY（标普500）', gspc), ('QQQ（纳斯达克100）', ndx)]:
    r = total_ret(s)
    rows.append({'资产': name, '名义涨幅': r, '实际涨幅': (1 + r) / (1 + cpi_ret) - 1})

summ = pd.DataFrame(rows)
summ['名义涨幅%'] = (summ['名义涨幅'] * 100).round(1)
summ['实际涨幅%'] = (summ['实际涨幅'] * 100).round(1)
summ = summ[['资产', '名义涨幅%', '实际涨幅%']]
summ.to_csv(os.path.join(OUT, '通胀_房价_美股_涨幅汇总.csv'), index=False, encoding='utf-8-sig')

print('图1:', p1)
print('图2:', p2)
print('汇总表:', os.path.join(OUT, '通胀_房价_美股_涨幅汇总.csv'))
print()
print(summ.to_string(index=False))
