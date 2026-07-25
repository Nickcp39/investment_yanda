# -*- coding: utf-8 -*-
"""生成自包含 HTML 报告 v2: output/east_asia_pir_report.html
结构: 结论 → 一对一PIR绝对值对比×5 → 售租比×2 → 综合表 → 附录总览 → 方法来源
"""
import base64

def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode()

def img(p, alt=''):
    return f'<img src="data:image/png;base64,{b64(p)}" alt="{alt}" loading="lazy">'

PAIR_SECTIONS = [
    ('output/pir_cn_vs_us.png', '① 中国 vs 美国(2008):同样的下坡,不同的海拔',
     """美国泡沫最疯的旧金山,峰值也只有 <b>9.2 倍</b>——不到中国出清 5 年后水平(17-24 倍)的一半。
     美国 3-6 年跌到 4-5 倍是<b>真便宜</b>(洛杉矶人 5 年收入买房),所以能 V 型反弹并创新高;
     中国跌完 5 年还悬在美国泡沫顶的 2-3 倍高度。<b>V 型反弹是低起点的特权,中国没有。</b>"""),
    ('output/pir_cn_vs_jp.png', '② 中国 vs 日本(1990):唯一在同一海拔的对手',
     """全场只有东京圈(峰 18.1)和中国一线在同一个量级对话。东京 18.1 → 6.8 跌掉 62%,用了 <b>14 年</b>;
     名义收复用了 35 年,还只有核心区。中国峰后 5 年的跌速(-27%~-39%)与日本同期相当——
     <b>行政托底改变的是波动形状,不是累计跌幅</b>。日本给中国的真正预告不是深度,是时间。"""),
    ('output/pir_cn_vs_kr.png', '③ 中国 vs 韩国首尔(2021):同年见顶,两种命运',
     """首尔和中国一线同在 2021 见顶。首尔 2022 加息急跌约 25%,但 2025-26 又暴涨收复到峰值九成——
     靠的是<b>首都圈供给硬短缺 + 人口持续流入</b>。中国一线四城里只有深圳部分具备这个引擎,广州完全没有。
     首尔是"能 V 的东亚样本",但它的前提条件中国抄不了。"""),
    ('output/pir_cn_vs_tw.png', '④ 中国 vs 台湾台北(2024):软着陆模板,但起点差一倍',
     """台北 30 年没崩过盘:2014 顶部阴跌 5 年 -12%,2024Q3 见顶后被打炒房政策压着连续 5 季回落。
     这是"中国理想软着陆"的模板——每年磨掉约 1 倍 PIR,社会无痛。
     但注意:<b>台北峰值 16.6,从来没上过深圳那种 38 倍的高度</b>。软着陆的前提是起点没那么高;
     中国即便完美复制台北斜率,深圳回到 15 倍也要 5-8 年。"""),
    ('output/pir_cn_vs_sg.png', '⑤ 中国 vs 新加坡:双轨制的降维打击',
     """新加坡把 80% 人口装进组屋轨道,PIR 全程压在 4-6 倍的世行合理区间——民生被制度性隔离在泡沫之外;
     私宅轨道 15.9 → 12.9,<b>名义价格还在创新高,倍数全靠收入年化 4-5% 涨了 18 年消化</b>。
     中国若走"不跌价靠收入"路线,需要收入增速稳定跑赢房价 20 年,而且没有组屋那条兜底轨。
     新加坡是制度答案,不是周期答案——现在建轨道,来不及救这轮周期。"""),
]

RENT_HTML = f"""
<h2>第二部分 · 售租比:比 PIR 更狠的口径</h2>
<p>售租比 = 房价 ÷ 年租金,即"买下这套房要收多少年租金"。它剔除了收入统计的口径差,
直接回答一个问题:<b>这个价格租金撑不撑得住?</b>国际"租金定价"市场在 15-25 倍(回报率 4-6.7%)。</p>
{img('output/p2r_china_trend.png', '中国一线售租比')}
{img('output/p2r_dumbbell.png', '全球售租比对比')}
<ol>
<li><b>中国的泡沫在售租比口径下比 PIR 更极端。</b>深圳峰值 95 倍(租金回报率 1.1%),
是美国 2006 泡沫顶(推算约 33 倍)的近 3 倍,也高于日本 1990 的估计区间(40-60)。
持有逻辑从来不是租金现金流,纯靠涨价预期——这是泡沫的定义本身。</li>
<li><b>修复比 PIR 慢,因为租金在同跌。</b>深圳 PIR 已从峰值挤掉 38%,售租比只挤掉 26%(95→70):
房价跌,租金也跌(人口流出+就业压力),分子分母一起缩。
<b>美国当年修复靠租金上涨,中国这条腿现在是断的</b>——所以租金企稳是比房价环比更硬的底部信号,盯它。</li>
<li><b>东亚共性,但中国在最极端一档。</b>首尔(94-102,全租制扭曲口径)、台北(76-97)、中国一线(59-96)
全在国际正常区间的 3-5 倍——低持有成本(没有房产税)、资本管制、低利率是共同土壤。
而同为东亚的东京(41)、新加坡(34)证明:这不是宿命,是政策选择。</li>
<li><b>广州的信号意义:</b>售租比 96→64 修复最快(租金相对稳、价格跌最狠),
和它 PIR 10.4 一起指向同一结论——广州最先接近"可着陆区",可能是观察中国出清终点形态的第一个样本。</li>
</ol>
"""

TABLE_ROWS = [
    # 地区, PIR峰(时), PIR现, 售租比峰(时), 售租比现, 回报率, 状态
    ('深圳', '38.0 (2020-21)', '23.7', '95 (2022)', '70', '1.4%', '双口径全场最高;未见底', 'cn'),
    ('北京', '25.0 (2021)', '17.7', '67 (2022)', '59', '1.7%', '未见底;2026上半年环比转正', 'cn'),
    ('上海', '24.0 (2021)', '17.4', '66 (2024)', '64', '1.6%', '售租比几乎没修复', 'cn'),
    ('广州', '17.0 (2021)', '10.4', '96 (2023)', '64', '1.6%', '双口径修复最快;最先接近着陆区', 'cn'),
    ('首尔', '19.0 (2021Q4)', '17.2', '94 (2022)', '102*', '~1.0%*', '价格收复九成;*全租制扭曲口径', 'ea'),
    ('台北', '16.6 (2024Q3)', '14.6', '97 (2020)', '76', '1.3%', '30年未崩;政策压降中', 'ea'),
    ('新加坡私宅', '15.9 (2008)', '12.9', '43 (2020)', '34', '2.9%', '18年收入消化;名义价新高', 'ea'),
    ('新加坡组屋', '4.9 (2013)', '4.3', '—', '—', '≈5-6%', '民生轨,全程合理区间', 'ea'),
    ('香港', '—', '—', '63 (2022)', '44', '2.3%', '2021后大幅出清(参考)', 'ea'),
    ('东京(现)', '—', '—', '41 (2019)', '41', '2.4%', '正常化后的日本', 'bg'),
    ('旧金山', '9.2 (2006)', '8.4', '20 (2021)', '15', '6.6%', '谷4.4(-52%,3年)后V型', 'bg'),
    ('纽约', '7.0 (2006)', '6.1', '22 (2022)', '21', '4.8%', '谷4.3(-39%,6年)后V型', 'bg'),
    ('东京圈1990', '18.1 (1990)', '谷6.8(2004)', '40-60(估计)', '—', '—', '深跌14年,名义收复35年', 'bg'),
]

rows_html = ''
for r in TABLE_ROWS:
    cls = {'cn': 'row-cn', 'ea': 'row-ea', 'bg': 'row-bg'}[r[7]]
    tds = ''.join(f'<td>{v}</td>' for v in r[:6])
    rows_html += f'<tr class="{cls}">{tds}<td class="small">{r[6]}</td></tr>\n'

pair_html = ''
for png, title, text in PAIR_SECTIONS:
    pair_html += f'<h3>{title}</h3>\n{img(png, title)}\n<p>{text}</p>\n'

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>东亚房价双口径对比:房价收入比 × 售租比</title>
<style>
  :root {{ --ink:#1a1a1a; --ink2:#555; --muted:#888; --line:#e5e3de;
          --cn:#2a78d6; --bg:#fcfcfb; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font-family:'Microsoft YaHei','PingFang SC',sans-serif; line-height:1.8; }}
  .wrap {{ max-width:1080px; margin:0 auto; padding:36px 28px 80px; }}
  h1 {{ font-size:25px; margin:0 0 4px; }}
  .sub {{ color:var(--muted); font-size:13px; margin-bottom:26px; }}
  h2 {{ font-size:19px; margin:46px 0 12px; border-left:4px solid var(--cn); padding-left:10px; }}
  h3 {{ font-size:16.5px; margin:34px 0 8px; }}
  .verdict {{ background:#f2f6fc; border:1px solid #d5e2f5; border-radius:10px;
             padding:18px 22px; font-size:15.5px; margin:18px 0 8px; }}
  .verdict b {{ color:#1a4f9c; }}
  img {{ max-width:100%; border:1px solid var(--line); border-radius:8px; margin:8px 0 4px; }}
  p {{ margin:8px 0 0; font-size:14.5px; }}
  table {{ border-collapse:collapse; width:100%; font-size:13px; margin:12px 0; }}
  th,td {{ border-bottom:1px solid var(--line); padding:7px 9px; text-align:left; white-space:nowrap; }}
  td.small,th.small {{ white-space:normal; }}
  th {{ background:#f4f3ef; font-size:12px; color:var(--ink2); }}
  .row-cn td:first-child {{ font-weight:700; color:var(--cn); }}
  .row-ea td:first-child {{ font-weight:700; }}
  .row-bg {{ color:#999; }}
  td.small {{ font-size:12px; color:var(--ink2); }}
  ol li {{ margin-bottom:10px; font-size:14.5px; }}
  .caveat {{ font-size:12.5px; color:var(--ink2); background:#faf8f2; border:1px solid #eee5cf;
            border-radius:8px; padding:12px 16px; }}
  .src {{ font-size:12px; color:var(--muted); }}
  .tablewrap {{ overflow-x:auto; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#e8e6e1; --ink2:#b5b2ab; --muted:#8a877f; --line:#3a3936; --bg:#1a1a19; }}
    .verdict {{ background:#20293a; border-color:#2e3f5c; }}
    .verdict b {{ color:#8ab4f0; }}
    th {{ background:#262624; }}
    .caveat {{ background:#26241d; border-color:#3d3826; }}
    img {{ opacity:.92; }}
  }}
</style>
</head>
<body><div class="wrap">

<h1>东亚房价双口径对比:房价收入比 × 售租比</h1>
<div class="sub">中国一线在泡沫周期中的位置 · 一对一绝对值对比 · 数据截至 2026 年中 · 更新 2026-07-22</div>

<div class="verdict">
<b>一句话结论:两个口径指向同一件事——中国一线是全场最高的山,且售租比口径比收入口径更狠。</b><br>
收入口径(PIR):深圳峰 38,挤了 5 年(-38%)后的 23.7 仍高于所有东亚邻居的历史峰值;
租金口径(售租比):深圳峰 95 倍(回报率 1.1%),是美国泡沫顶的近 3 倍,而且因为<b>租金和房价在同跌</b>,只修复了 26%。
最可能路径 = 台湾式缓降 × 日本式时间 × 新加坡式收入消化;
真正的底部信号是三件事同时出现:<b>一线二手成交量连续 12 个月放大 + PIR 降到 15 倍以内 + 租金企稳</b>。
</div>

<h2>第一部分 · 一对一对比(绝对值,峰值对齐)</h2>
<p>横轴 = 距各自峰值的年数(美国峰 2006、日本峰 1990、中国峰 2020-21、首尔峰 2021、台北峰 2024),
纵轴 = 房价收入比绝对倍数,所有图统一 0-40 刻度,高度可以直接比。</p>
{pair_html}

{RENT_HTML}

<h2>综合对比表(双口径)</h2>
<div class="tablewrap">
<table>
<tr><th>地区</th><th>PIR峰(时间)</th><th>PIR现</th><th>售租比峰(时间)</th><th>售租比现</th><th>租金回报率</th><th class="small">状态</th></tr>
{rows_html}
</table>
</div>

<h2>附录 · 总览图</h2>
{img('output/pir_east_asia_aligned.png', '峰值对齐总览')}
{img('output/pir_east_asia_absolute.png', '绝对水平总览')}

<h2>方法与口径说明</h2>
<div class="caveat">
<b>PIR:</b>PIR(t) = 官方锚点 × [价格指数(t)/锚点期] ÷ [收入指数(t)/锚点期]。
中国=易居锚点(2015/2021)+统计局70城二手房年度链(峰前收入增速由两端锚点校准1.5-4.3%/年,峰后4%/年);
韩国=KB首尔公寓指数+KB中位收入,锚KB PIR 2021年12月=19.0(KB 2022年末换收入口径后官方值断崖至~10.5,<b>首尔绝对倍数看形状别看绝对值</b>);
台湾=内政部改版口径,锚点经政大信义中心+央社/自由时报交叉核实(2022-23为插值段);
新加坡=HDB/URA指数+SingStat中位收入,2025锚:组屋S$62.8万(4.35倍)/私宅公寓S$187.5万(13.0倍);
美国=Case-Shiller,峰值锚旧金山9.2/纽约7.0,收入3%/年;日本=节点插值仅背景。<br>
<b>售租比:</b>Numbeo 历年榜市中心口径(2009-2026,众包数据有噪音,看趋势与量级);
美国2006泡沫顶≈33为推算值(Numbeo2009 × Case-Shiller 2006/2009 指数比,租金近似不变);
日本1990为文献估计区间40-60,仅作参考,未获一手数据确认;
首尔受全租制(전세)扭曲,月租样本稀薄,绝对值偏高。<br>
<b>总原则:跨经济体比形状与相对量级,不比精确绝对值。</b>
中国高储蓄率+六个钱包+无房产税会让"可承受倍数"天然偏高,但打完折扣,与租金定价市场 3-5 倍的差距仍是实打实的。
</div>

<h2>数据源</h2>
<p class="src">
中国:国家统计局70城历月发布(stats.gov.cn;2016年经中房学cirea.org.cn镜像)· 易居研究院房价收入比报告(2015/2021锚点)·
韩国:KB국민은행 데이터허브 开放接口(1986-2026)·
台湾:内政部「房价负担能力统计」经政大信义不动产研究中心/央社/自由时报交叉核实 ·
新加坡:data.gov.sg(HDB RPI · URA PPI · SingStat收入)·
美国:S&amp;P Case-Shiller(datahub,1987-2026.02)·
售租比:Numbeo Property Investment 历年榜(2009-2026)·
日本:不动产研究所/国交省口径锚点(交接文档)+文献估计。<br>
数据文件与脚本:<code>房价分析/data/</code> · <code>build_east_asia_pir.py</code> · <code>build_rent_charts.py</code> ·
序列明细 <code>data/computed_pir_series.csv</code> · <code>data/numbeo_p2r_history.csv</code>
</p>

</div></body></html>"""

open('output/east_asia_pir_report.html', 'w', encoding='utf-8').write(html)
print('report written:', len(html))
