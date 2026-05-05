# Channel Sources

Channel-level inputs live here. A channel folder should contain stable
manifests, resumable metadata checkpoints, and run reports.

## Recommended Layout

```text
sources/channels/
  tradesmax/
    manifests/
      tradesmax_videos_flat_YYYY-MM-DD.csv
      tradesmax_videos_detailed_YYYY-MM-DD.csv
      tradesmax_videos_2024_to_2026_YYYY-MM-DD.csv
    metadata/
      <video_id>.info.json
      <video_id>.error.json
    runs/
      YYYYMMDD_HHMMSS/
        progress.csv
        failed.csv
        missing.csv
        run_summary.json
  wall-street-news/
    manifests/
    metadata/
    runs/
```

Keep `video_id` as the primary key. Titles can change, repeat, or get corrupted
by terminal encoding; video IDs are the checkpoint boundary.

## Workflow

1. Freeze a flat manifest for the channel.
2. Run `scripts/youtube_channel_queue.py` against that manifest.
3. Re-run the same command whenever it stops; existing `<video_id>.info.json`
   files are skipped.
4. Inspect the latest `runs/*/missing.csv` and `failed.csv`.
5. Use exported manifests from `manifests/` as source lists for transcripts,
   notes, and thesis work.
