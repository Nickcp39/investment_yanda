# Situational Awareness Analysis Pack

Source: Leopold Aschenbrenner, `Situational Awareness: The Decade Ahead`, June 2024.

This folder is the organized working copy for the local PDF and existing Chinese analysis.

## Contents

- `analysis_zh.md` - recovered Chinese analysis from the existing HTML summary.
- `analysis_zh.docx` - Word version generated from the recovered analysis.
- `fixed_summary_zh.html` - repaired HTML version of the existing summary.
- `extracted_text/outline.md` - PDF bookmark outline with page numbers.
- `extracted_text/full_text.txt` - local-only full text extracted from the 165-page PDF.
- `extracted_text/sections_by_bookmark/` - local-only split text using the PDF's built-in bookmarks.
- `overleaf/` - Overleaf-ready LaTeX project.
- `overleaf_situational_awareness_analysis.zip` - zip upload package for Overleaf.

## Build

```powershell
python scripts/build_aschenbrenner_pack.py
cd "I:\yc_research\2026 investment yanda\sources\papers\aschenbrenner_situational-awareness_2024-06_analysis\overleaf"
.\build.ps1
```

The Overleaf package is designed for XeLaTeX. If local MiKTeX hangs while loading
`fontspec` / `xeCJK`, upload `overleaf_situational_awareness_analysis.zip` to
Overleaf or refresh the local MiKTeX font/package cache before compiling.

## Notes

The existing HTML summary had mojibake-style encoding, so this pack repairs it before producing Markdown, Word, and LaTeX files. The split text is a mechanical PDF extraction and should be treated as a local reading aid, not a clean publication transcript. Full-text extraction artifacts are intentionally ignored by git.
