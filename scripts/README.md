# Scripts

Use this folder for repeatable data collection, cleaning, analysis, and charting
scripts.

## Market Slope Scan

Rank the latest QQQ rally speed against its own history:

```powershell
python .\scripts\qqq_slope_scan.py --symbol QQQ --windows 5,10,20,40,60,120
```

Default outputs are written under `data/processed/market_slope/`:

- rolling slope data
- top non-overlapping rally episodes
- a Markdown summary report
- a PNG chart when `matplotlib` is installed

## Video Notes

Create a timestamped investment note from a YouTube URL:

```powershell
.\.venv\Scripts\python.exe .\scripts\video_note.py "https://www.youtube.com/watch?v=RCh6v_Ao6mY"
```

By default, the script fetches YouTube captions and creates:

- `sources/videos/*_transcript.md`
- `notes/videos/*_note.md`

One-time local setup:

```powershell
python -m venv .\.venv
.\.venv\Scripts\python.exe -m pip install yt-dlp youtube-transcript-api
```

To use an OpenAI-compatible model for a full structured research note:

```powershell
$env:OPENAI_API_KEY="..."
.\.venv\Scripts\python.exe .\scripts\video_note.py "https://www.youtube.com/watch?v=RCh6v_Ao6mY" --llm
```

Optional environment variables:

- `OPENAI_MODEL`
- `OPENAI_BASE_URL`

## YouTube Channel Metadata Queue

Use `youtube_channel_queue.py` after freezing a flat channel manifest. It fetches
one video at a time, stores one checkpoint per `video_id`, and can be re-run
until every video has either a success checkpoint or a visible failure report.

Example for the TradesMax flat manifest:

```powershell
.\.venv\Scripts\python.exe .\scripts\youtube_channel_queue.py `
  --input .\sources\channels\tradesmax_videos_flat_2026-05-01.csv `
  --channel-slug tradesmax `
  --start-date 2024-01-01 `
  --end-date 2026-12-31
```

Useful options:

- `--dry-run` - validate the plan without fetching or writing.
- `--export-only` - rebuild CSV/JSONL/Markdown from existing checkpoints.
- `--limit 5` - smoke test the first five videos.
- `--force` - re-fetch even when `<video_id>.info.json` already exists.
- `--cache-dir` - override the checkpoint folder.
- `--output-dir` - override the exported manifest folder.

Default outputs for `--channel-slug tradesmax`:

- `sources/channels/tradesmax/metadata/<video_id>.info.json`
- `sources/channels/tradesmax/metadata/<video_id>.error.json`
- `sources/channels/tradesmax/manifests/*.csv`
- `sources/channels/tradesmax/manifests/*.jsonl`
- `sources/channels/tradesmax/manifests/*.md`
- `sources/channels/tradesmax/runs/<timestamp>/progress.csv`
- `sources/channels/tradesmax/runs/<timestamp>/failed.csv`
- `sources/channels/tradesmax/runs/<timestamp>/missing.csv`

## Channel Video Index

Create an index of a YouTube channel's videos:

```powershell
.\.venv\Scripts\python.exe .\scripts\channel_video_index.py "https://www.youtube.com/@TradesMax/videos" --detailed --date-after 2024-01-01 --name tradesmax_videos_2024_to_2026_2026-05-01
```

The script writes CSV, JSONL, and Markdown files under `sources/channels/`.

## Bilibili Space Metadata Queue

First freeze a flat Bilibili space manifest:

```powershell
.\.venv\Scripts\python.exe .\scripts\channel_video_index.py "https://space.bilibili.com/1039025435" --name bilibili_1039025435_flat_2026-05-05
```

Then fetch per-video metadata with checkpointing:

```powershell
.\.venv\Scripts\python.exe .\scripts\bilibili_channel_queue.py `
  --input .\sources\channels\bilibili_1039025435_flat_2026-05-05.csv `
  --channel-slug bilibili-1039025435
```

Default outputs:

- `sources/channels/bilibili-1039025435/metadata/<BVID>.info.json`
- `sources/channels/bilibili-1039025435/metadata/<BVID>.error.json`
- `sources/channels/bilibili-1039025435/manifests/*.csv`
- `sources/channels/bilibili-1039025435/runs/<timestamp>/*.csv`

## YouTube ASR Queue

Use this when YouTube videos do not expose official subtitles or automatic
captions. It downloads best-audio only, then writes one ASR transcript per
video.

```powershell
.\.venv\Scripts\python.exe .\scripts\youtube_asr_queue.py `
  --input .\sources\channels\zhanguoshidai_videos_detailed_2026-05-05.csv `
  --channel-slug zhanguoshidai `
  --model base
```

Default outputs:

- `sources/channels/zhanguoshidai/audio/<video_id>.*`
- `sources/channels/zhanguoshidai/transcripts/<video_id>_asr.md`
- `sources/channels/zhanguoshidai/transcripts/<video_id>_asr.json`
- `sources/channels/zhanguoshidai/runs/asr_<timestamp>/*.csv`

## Local Transcript Polish

Use this after ASR when you want a conservative local cleanup pass without
calling external LLM CLIs. It preserves every timestamped line and writes QC
reports comparing source and polished text.

```powershell
.\.venv\Scripts\python.exe .\scripts\transcript_local_polish.py `
  --input-dir .\sources\channels\zhanguoshidai\transcripts `
  --output-dir .\sources\channels\zhanguoshidai\polished_transcripts `
  --qc-dir .\sources\channels\zhanguoshidai\polish_qc `
  --force
```

Outputs:

- `sources/channels/zhanguoshidai/polished_transcripts/<video_id>_polished.md`
- `sources/channels/zhanguoshidai/polish_qc/polish_summary_*.csv`
- `sources/channels/zhanguoshidai/polish_qc/polish_changes_*.csv`
- `sources/channels/zhanguoshidai/polish_qc/polish_low_similarity_*.md`

## TradesMax Public Articles

Collect public article pages from the TradesMax website for research archiving:

```powershell
.\.venv\Scripts\python.exe -m pip install requests beautifulsoup4 lxml
.\.venv\Scripts\python.exe .\scripts\tradesmax_public_articles.py --limit 10
```

The script scans the public homepage and public category pages, then writes:

- `sources/news/tradesmax/manifest.csv`
- `sources/news/tradesmax/manifest.jsonl`
- `sources/news/tradesmax/articles/*.md`

Useful options:

- `--dry-run` - list discovered links without fetching article bodies.
- `--limit 5` - smoke test a small number of articles.
- `--pages 3` - scan more category pages using K2 `?start=` pagination.
- `--delay 2` - wait between requests.
- `--index-url URL` - scan a specific public index page; can be repeated.

## WeChat MP Articles

Collect public WeChat official-account articles that are already visible in the
local WeChat client/browser cache. This avoids asking for WeChat passwords,
cookies, tokens, or other session secrets; cached URLs are canonicalized before
being fetched or saved.

```powershell
.\.venv\Scripts\python.exe .\scripts\wechat_mp_local_history.py --limit 20
```

Default outputs:

- `sources/news/wechat_mp/manifest.csv`
- `sources/news/wechat_mp/manifest.jsonl`
- `sources/news/wechat_mp/articles/*.md`

Useful options:

- `--dry-run` - parse and filter cache links without writing files.
- `--limit 5` - stop after five matching target-account articles.
- `--candidate-offset 50` - resume from a later discovered candidate when running in batches.
- `--max-candidates 50` - only test the first 50 discovered WeChat article URLs.
- `--recent 5` - print the latest matching titles after the run.
- `--show-candidates` - print sanitized public WeChat article URLs discovered in cache.

For one manually copied WeChat article link, use the clipboard collector:

```powershell
.\.venv\Scripts\python.exe .\scripts\wechat_mp_clipboard_collector.py --once "https://mp.weixin.qq.com/s/..."
```

To drive the visible WeChat official-account profile and archive opened cards
semi-automatically, keep the target account page open in WeChat, then run:

```powershell
.\.venv\Scripts\python.exe .\scripts\wechat_mp_gui_archiver.py `
  --until-date 2025-01-01 `
  --max-articles 50 `
  --max-scrolls 80
```

Start small before a long run:

```powershell
.\.venv\Scripts\python.exe .\scripts\wechat_mp_gui_archiver.py --max-cards 3 --max-articles 3
```

The GUI archiver clicks visible article cards, waits for WeChat to record the
opened public article URL in local WebView history, then saves only matching
`美股投资网` articles. It reuses the same manifest, so it can be stopped and
re-run without re-saving already collected public URLs.

Coordinate tuning options:

- `--plan-only` - print the click points without clicking.
- `--card-x-offset 220` - move click points horizontally from the profile window left edge.
- `--card-y-offsets 285,525,765` - visible card slots from the profile window top edge.
