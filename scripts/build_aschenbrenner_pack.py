from __future__ import annotations

import re
import shutil
import subprocess
import zipfile
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources" / "papers"
PDF_PATH = SOURCE_DIR / "aschenbrenner_situational-awareness_2024-06.pdf"
HTML_PATH = SOURCE_DIR / "aschenbrenner_situational-awareness_summary_zh.html"
OUT_DIR = SOURCE_DIR / "aschenbrenner_situational-awareness_2024-06_analysis"


@dataclass
class Bookmark:
    level: int
    title: str
    page_index: int


def recover_mojibake(text: str) -> str:
    """Recover Chinese mojibake only when the input is actually mojibake."""
    cjk_count = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    if cjk_count > 100:
        fixed = text
    else:
        fixed = text.encode("cp1252", errors="ignore").decode("utf-8", errors="replace")
    fixed = fixed.replace(
        r"D:\work\investment\financial-analysis-lab\sources\papers\aschenbrenner_situational-awareness_2024-06.pdf",
        str(PDF_PATH),
    )
    return fixed


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=str(cwd or ROOT), check=True)


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90] or "section"


def flatten_outline(reader: PdfReader) -> list[Bookmark]:
    out: list[Bookmark] = []

    def walk(items, level: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, level + 1)
                continue
            title = str(item.get("/Title", "Untitled")).strip()
            try:
                page_index = reader.get_destination_page_number(item)
            except Exception:
                continue
            out.append(Bookmark(level=level, title=title, page_index=page_index))

    walk(reader.outline, 1)
    out.sort(key=lambda b: (b.page_index, b.level, b.title))
    return out


def page_text(reader: PdfReader, start: int, end: int) -> str:
    chunks: list[str] = []
    for idx in range(start, end):
        text = reader.pages[idx].extract_text() or ""
        chunks.append(f"\n\n--- PDF page {idx + 1} ---\n\n{text.strip()}\n")
    return "\n".join(chunks).strip() + "\n"


def write_outline(bookmarks: list[Bookmark], path: Path) -> None:
    lines = [
        "# Situational Awareness PDF Outline",
        "",
        f"Source PDF: `{PDF_PATH}`",
        "",
    ]
    for b in bookmarks:
        indent = "  " * max(0, b.level - 1)
        lines.append(f"{indent}- p.{b.page_index + 1}: {b.title}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_section_files(reader: PdfReader, bookmarks: list[Bookmark], sections_dir: Path) -> None:
    sections_dir.mkdir(parents=True, exist_ok=True)
    for i, b in enumerate(bookmarks):
        next_page = bookmarks[i + 1].page_index if i + 1 < len(bookmarks) else len(reader.pages)
        end = max(b.page_index + 1, next_page)
        filename = f"{i + 1:02d}_p{b.page_index + 1:03d}_{slugify(b.title)}.md"
        body = page_text(reader, b.page_index, end)
        header = [
            f"# {b.title}",
            "",
            f"- Source PDF page: {b.page_index + 1}",
            f"- Extracted page range: {b.page_index + 1}-{end}",
            f"- Outline level: {b.level}",
            "",
        ]
        (sections_dir / filename).write_text("\n".join(header) + body, encoding="utf-8")


def build_readme(path: Path) -> None:
    text = f"""# Situational Awareness Analysis Pack

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
cd "{OUT_DIR / 'overleaf'}"
.\\build.ps1
```

The Overleaf package is designed for XeLaTeX. If local MiKTeX hangs while loading
`fontspec` / `xeCJK`, upload `overleaf_situational_awareness_analysis.zip` to
Overleaf or refresh the local MiKTeX font/package cache before compiling.

## Notes

The existing HTML summary had mojibake-style encoding, so this pack repairs it before producing Markdown, Word, and LaTeX files. The split text is a mechanical PDF extraction and should be treated as a local reading aid, not a clean publication transcript. Full-text extraction artifacts are intentionally ignored by git.
"""
    path.write_text(text, encoding="utf-8")


def write_extracted_gitignore(extracted_dir: Path) -> None:
    (extracted_dir / ".gitignore").write_text(
        "full_text.txt\nsections_by_bookmark/\n",
        encoding="utf-8",
    )


def build_overleaf(overleaf_dir: Path) -> None:
    overleaf_dir.mkdir(parents=True, exist_ok=True)
    main_tex = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\setmainfont{Latin Modern Roman}
\setCJKmainfont{FandolSong-Regular}
\setCJKsansfont{FandolHei-Regular}
\setCJKmonofont{FandolFang-Regular}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{titlesec}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlist{itemsep=2pt,topsep=4pt}
\titleformat{\section}{\Large\bfseries}{\thesection}{0.75em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{0.75em}{}

\title{Situational Awareness: The Decade Ahead\\中文分析与投资约束框架}
\author{Local research digest}
\date{Generated 2026-06-25}

\begin{document}
\maketitle
\tableofcontents
\newpage
\input{body.tex}
\nocite{*}
\bibliographystyle{plain}
\bibliography{references}
\end{document}
"""
    refs = r"""@misc{aschenbrenner2024situational,
  author = {Aschenbrenner, Leopold},
  title = {Situational Awareness: The Decade Ahead},
  year = {2024},
  month = {June},
  url = {https://situational-awareness.ai/},
  note = {Local archive and Chinese research digest}
}
"""
    build_ps1 = r"""$ErrorActionPreference = "Stop"
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
"""
    (overleaf_dir / "main.tex").write_text(main_tex, encoding="utf-8")
    (overleaf_dir / "references.bib").write_text(refs, encoding="utf-8")
    (overleaf_dir / "build.ps1").write_text(build_ps1, encoding="utf-8")
    (overleaf_dir / "README.md").write_text(
        "# Overleaf package\n\nCompile with XeLaTeX: `xelatex main`, `bibtex main`, `xelatex main`, `xelatex main`.\n\nThis package uses `xeCJK` and Fandol CJK fonts, which are standard in Overleaf/TeX Live. If local MiKTeX hangs during font initialization, upload the zip to Overleaf instead.\n",
        encoding="utf-8",
    )


def zip_overleaf(overleaf_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in overleaf_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(overleaf_dir))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    extracted_dir = OUT_DIR / "extracted_text"
    sections_dir = extracted_dir / "sections_by_bookmark"
    overleaf_dir = OUT_DIR / "overleaf"
    extracted_dir.mkdir(parents=True, exist_ok=True)

    raw_html = HTML_PATH.read_text(encoding="utf-8")
    fixed_html = recover_mojibake(raw_html)
    fixed_html_path = OUT_DIR / "fixed_summary_zh.html"
    fixed_html_path.write_text(fixed_html, encoding="utf-8")

    analysis_md = OUT_DIR / "analysis_zh.md"
    analysis_docx = OUT_DIR / "analysis_zh.docx"
    html_reader = "html-native_divs-native_spans"
    run(["pandoc", str(fixed_html_path), "-f", html_reader, "-t", "gfm", "--wrap=none", "-o", str(analysis_md)])
    run(["pandoc", str(fixed_html_path), "-f", html_reader, "-o", str(analysis_docx)])

    reader = PdfReader(str(PDF_PATH))
    bookmarks = flatten_outline(reader)
    write_extracted_gitignore(extracted_dir)
    write_outline(bookmarks, extracted_dir / "outline.md")
    (extracted_dir / "full_text.txt").write_text(page_text(reader, 0, len(reader.pages)), encoding="utf-8")
    if sections_dir.exists():
        shutil.rmtree(sections_dir)
    write_section_files(reader, bookmarks, sections_dir)

    build_overleaf(overleaf_dir)
    run(["pandoc", str(fixed_html_path), "-f", html_reader, "-t", "latex", "--wrap=none", "-o", str(overleaf_dir / "body.tex")])
    build_readme(OUT_DIR / "README.md")
    zip_overleaf(overleaf_dir, OUT_DIR / "overleaf_situational_awareness_analysis.zip")

    print(f"Built: {OUT_DIR}")
    print(f"Bookmarks: {len(bookmarks)}")
    print(f"Pages: {len(reader.pages)}")


if __name__ == "__main__":
    main()
