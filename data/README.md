# Data

Use this folder for documented data inputs and derived datasets.

## Policy

- Keep source, retrieval date, license, and transformation notes with each
  dataset.
- Do not commit private brokerage exports, credentials, or sensitive portfolio
  data.
- Avoid committing large raw datasets. Use `data/raw/`, `data/interim/`, and
  `data/processed/` locally when needed; these paths are ignored by git.
- Prefer scripts that can reproduce derived data from documented sources.

## Suggested Local Layout

- `raw/` - original downloaded files
- `interim/` - cleaned but not final data
- `processed/` - analysis-ready outputs
