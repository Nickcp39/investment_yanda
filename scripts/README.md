# Scripts

Use this folder for repeatable data collection, cleaning, analysis, and charting
scripts.

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
