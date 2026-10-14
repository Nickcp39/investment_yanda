# 李录 · 哥大第 36 届 Graham & Dodd 论坛（2026-10-05）· 字幕与笔记

- `总结.md` / `output/pdf/李录_哥大GD论坛2026_笔记_2026-10-14.pdf`：按主题去重的笔记、时间轴、与本仓库研究的交叉点、可核对数字清单
- `subs/youtube_FwDKCNfHHtY_en_asr.{json3,srt,txt}`：YouTube 英文自动字幕（13,839 词，1:45:24），txt 每分钟一个时间戳
- 来源：YouTube FwDKCNfHHtY（原声）；B 站 BV1FFpw6hEXY 原声版未登录无 CC；虎嗅转载的中文整理稿可交叉核对
- 取字幕方法：yt-dlp 对 YouTube 报「page needs to be reloaded」、对 B 站报 412；改在内置浏览器打开视频页，hook fetch/XHR 拿到带 pot 参数的 timedtext 链接，再用 curl（带 Referer/Origin）下载 json3
