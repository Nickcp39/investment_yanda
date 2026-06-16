# 美股投资网（TradesMax）微信公众号 抓取计划

- 目标主体: 微信公众号「美股投资网」(= YouTube 频道 TradesMax 同一主体)
- 范围: **历史全部 + 持续追新**（用户 2026-06-09 确认）
- 拿列表方式: **PC 微信客户端抓包**拿登录态凭证，脚本翻页批量拉（用户 2026-06-09 确认）
- slug: `meigutouzi-wechat`
- 状态: 🟡 Stage 0 待用户抓包回传凭证

---

## 技术现实与硬约束（重要）

微信公众号**没有公开 API / RSS**。文章列表接口需要微信登录态凭证才能调。

1. **凭证有时效**: `key` / `pass_ticket` / `appmsg_token` 通常 **几十分钟~几小时** 过期。
   → "历史全量"必须在凭证有效期内一口气翻完（脚本断点续传 + 限速）。
2. **必须限速**: 翻页太快会触发"操作频繁，请稍后再试"，甚至短时封该 key。
   → 每次请求间隔 3-8s 随机，失败指数退避。
3. **"持续追新"≠ 完全无人值守**: 因为 key 会过期，没法做成长期自动 cron。
   现实做法: 每隔 N 天（如每周）用户**重抓一次包喂新 key**，脚本只跑增量（1 分钟）。
   备选: 后续评估自建 wechat2rss 类服务做轻量追新（要部署，二期再说）。
4. 单篇文章正文（`mp.weixin.qq.com/s/xxx`）公开可读，抓取不难；难的只在"拿全量列表"。

---

## 阶段划分

### Stage 0 — 拿公众号身份 + 登录态凭证（用户配合，当前）
- **Input**: 用户在 PC 微信打开「美股投资网」任意一篇文章并下滑，用 Fiddler 抓包
- **用户回传**: 那条带 `__biz=` 和 `appmsg_token=`（或 `action=getmsg`）的请求，**Copy as cURL** 发回
- **我解析出**: `__biz`(公众号唯一ID) / `appmsg_token` / `pass_ticket` / Cookie(`wap_sid2` 等)
- **附加**: 用户先发 1 篇文章链接 → 我确认号身份 + 验证单篇正文抓取
- **Success**: 凭证齐全，单篇抓取跑通
- **Hand-off**: 进 Stage 1

### Stage 1 — 全量文章列表（脚本 `scripts/wechat_mp_list.py`）
- 用凭证调列表接口，`offset` 翻页直到 `can_msg_continue=0`
- 收集每篇: `{title, link, datetime, digest, author, cover}`
- 断点续传（checkpoint per offset）、限速、key 失效时优雅停下并提示重抓
- **Output**:
  - `sources/channels/meigutouzi-wechat/manifests/articles_<date>.csv|jsonl|md`
  - `sources/channels/meigutouzi-wechat/runs/<ts>/progress.csv`

### Stage 2 — 逐篇正文（脚本 `scripts/wechat_mp_fetch.py`）
- 按 manifest 逐篇抓 `mp.weixin.qq.com/s/xxx`，正文转 Markdown
- 处理图片防盗链（可选下载到本地 / 或保留链接）、去广告尾部
- 断点续传、限速
- **Output**:
  - `sources/channels/meigutouzi-wechat/articles/<id>.md`（带 metadata header）
  - `sources/channels/meigutouzi-wechat/articles/<id>.html`（原始留底，可选）

### Stage 3 — 增量追新（`wechat_mp_list.py --incremental`）
- 重新喂 key 后只拉 offset 0 → 已知最新 link，去重合并
- 跑完自动触发 Stage 2 抓新文章正文

### Stage 4（可选）— 接入分析 pipeline
- 把文章喂进现有 notes / souls 流程，做结构化投资笔记
- 与 YouTube transcript 同源（都是美股投资网），可交叉

---

## 要建的脚本

| 脚本 | 作用 | 依赖 |
|---|---|---|
| `scripts/wechat_mp_list.py` | 翻页拉全量/增量文章列表 | requests |
| `scripts/wechat_mp_fetch.py` | 逐篇抓正文转 md | requests + (lxml/bs4) |

风格对齐现有 `youtube_channel_queue.py`: argparse + 断点续传 + 限速 + dry-run + export-only。

---

## 合规 / 安全
- 用户对自己可正常访问的公众号做**个人研究归档**，合理使用。
- 抓包仅在用户自己机器上对自己微信流量操作。
- cURL 凭证 = 临时登录令牌，仅用于本任务、几小时内自动失效；不外传不入库（脚本运行时用，不写进 git）。
- 严格限速，不高频请求，不滥用。

---

## 修订记录
- 2026-06-09 v1: 首发，确认范围(历史全量+追新) + 方式(抓包)，定 4 阶段 + 2 脚本
