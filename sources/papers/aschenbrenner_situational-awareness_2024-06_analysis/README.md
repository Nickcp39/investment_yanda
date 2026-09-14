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
- `full_read_2026-09-13.md` - **全文精读补齐**：第 II、IIIb-d、IV、V 章（原分析自述未逐页读的 120 页）。
- `epilogue_2026.md` - **2026 结果核对 + 作者本人基金爆仓**，及其对本库 risk_limits / 归因四象限的含义。
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

**2026-09-13 更新**：容器内用 pypdf 重新抽取了 165 页全文与分章文本
(`extracted_text/full_text.txt` 31.3 万字符 + `sections_by_bookmark/` 10 章)，
补齐了 `analysis_zh.md` 自述未精读的章节，产出 `full_read_2026-09-13.md`。
抽取产物仍按原设定 gitignore，只入库分析结论。

The existing HTML summary had mojibake-style encoding, so this pack repairs it before producing Markdown, Word, and LaTeX files. The split text is a mechanical PDF extraction and should be treated as a local reading aid, not a clean publication transcript. Full-text extraction artifacts are intentionally ignored by git.
