# card_watch — 卡片价格巡检

**一句话**：把 `companies/` 里每家公司最新一张决策卡的买入线，和今天的价格放在一张表里，告诉你**哪些卡需要重跑**。

- 双击仓库根目录的 `run_card_watch.bat`（或 `python scripts/card_watch/card_watch.py`）。
- 产物：`scripts/card_watch/out/card_watch_<日期>.md`（分四组）和 `.csv`（全字段）。按日期出新文件，不覆盖旧的。
- 耗时约 1–2 分钟（逐个代码抓 Yahoo 即时价）。

## 四组

| 组 | 含义 | 该做什么 |
|---|---|---|
| A | 现价 ≤ 买入线（或在带内） | **重跑这张卡**。不是买入信号 |
| B | 现价高于线 ≤10% | 排进下一次重跑队列 |
| C | 现价高于线 >10% | 不动 |
| D | 没有买入线 / 抓不到价 | 卡本身缺线（INFO-GAP、无股本等），或代码映射要修 |

## 规矩（写在每份输出的头部）

1. **价格过线 ≠ 可执行入场**（C4）。裁决上限由完整度决定；runner 提议的 STARTER 在独立 Checker 之前一律 WATCH。
2. **不按距线远近排名**。组内按代码字母序。
3. **卡龄 > 90 天**（`旧卡` 标记）的线可能已经过时：财报换了、股本换了、锚换了。先重跑再看。
4. 非美股按**本币**比较（日元、港币、人民币、英镑便士、欧元）；卡里币种与 Yahoo 返回币种不一致的行会标 `币种`。

## 数据来源与退路

- 买入线：`decision_card.json` 的 `buy_below_price` 或 `buy_below`。没有 JSON、或 JSON 缺线时，退回 `decision_card.md` 第一行含 `buy_below` / `buy-below` 的第一个 `$数字`（标 `线来自 md`，要人眼核一下）。
- 价格：Yahoo chart API `meta.regularMarketPrice`，盘中就是盘中价，盘后是收盘价；抓取时间写在 csv 的 `price_time`。
- 代码映射：卡里的 `ticker` 直接用；`601857.SH` 这类改成 Yahoo 的 `.SS`；`A / B` 双代码取第一个。特殊情况写在 `overrides.json`。
- 同一代码多个文件夹（如 `gehc/` 与 `ge_healthcare/`）只取最新那张，表里标 `替代旧文件夹`。

## 邮件提醒（GitHub Actions → Issue → 邮件）

`.github/workflows/card_watch.yml` 每个美股交易日 21:45 UTC（收盘后）在 GitHub 上跑一遍，然后 `alert.py` 把今天的 A/B 组和 `state.json` 里上一次的比：

- **有卡新进 A 组**（上次在线上、今天在线下）→ 开一个 Issue 并指派给仓库所有者 → GitHub 把 Issue 内容发到所有者的通知邮箱。
- **每周一**另发一封全表周报（A 组、B 组全列）。
- 其余日子不发。`state.json` 变了才由 bot 提交一次；当天的完整表作为 Actions artifact 保存 90 天。
- 手动测试：GitHub → Actions → card-watch → Run workflow（勾 digest 可强制发全表）。

要收到邮件只需一件事：GitHub → Settings → Notifications，确认通知邮箱是你常看的那个，"Participating" 勾了 Email。
注意：仓库是公开的，Issue 也是公开的；内容只有买入线和现价，和仓库里已公开的卡一致。要改成私密邮件，得用 SMTP（需要你自己在仓库 Secrets 里放发件账号的应用密码），脚本可以加。

首次部署时用 `python scripts/card_watch/alert.py --seed` 把当天 A/B 组写进 `state.json`，否则第一封信会把已经在线下的 20 多张全列出来。

## 已知限制

- 只看买入线一个数。带状卡（NVDA、NBIS）用带顶当线，带底要看卡。
- 不抓盘前盘后，不做汇率换算，不发通知。要定时跑，用 Windows 任务计划调用 `run_card_watch.bat`。
