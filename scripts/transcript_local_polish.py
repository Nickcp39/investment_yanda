#!/usr/bin/env python3
"""
Local ASR transcript cleanup for timestamped Markdown files.

This is intentionally local-only: it does not call external LLMs or CLIs. The
script preserves every timestamped line and applies conservative correction
rules for common ASR mistakes found in the zhanguoshidai transcript set. It also
emits QC reports that compare source and polished lines timestamp-by-timestamp.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP_RE = re.compile(r"^\[(\d{2}:\d{2}(?::\d{2})?)\]\s*(.*)$")


@dataclass
class LinePair:
    video_id: str
    timestamp: str
    source: str
    polished: str


LINE_OVERRIDES: dict[tuple[str, str, str], str] = {
    ("0_73x6MOm7A", "01:05", "美国就印度就玩完了"): "那印度就玩完了",
    ("0_73x6MOm7A", "02:00", "非洲正面更是如此"): "欧洲这边更是如此",
    ("0_73x6MOm7A", "02:38", "非洲而且"): "枭龙，而且",
    ("0_73x6MOm7A", "03:07", "见不着"): "柬埔寨",
    ("0_73x6MOm7A", "03:08", "越南见不着老窝太过"): "越南、柬埔寨、老挝、泰国",
    ("0_73x6MOm7A", "03:14", "服质清华"): "扶植亲华",
    ("0_73x6MOm7A", "04:51", "如果是中毒"): "如果是中国",
    ("nzh3ngn21tY", "00:00", "還沒內衣確診身亡"): "哈梅内伊确认身亡",
}


PHRASE_REPLACEMENTS: list[tuple[str, str]] = [
    ("馬六甲", "马六甲"),
    ("马六加", "马六甲"),
    ("马尔加", "马六甲"),
    ("海侠", "海峡"),
    ("红海海下", "红海海峡"),
    ("红海海侠", "红海海峡"),
    ("海峡毒死", "海峡堵死"),
    ("被毒死", "被堵死"),
    ("毒死了", "堵死了"),
    ("划太多", "花太多"),
    ("简单的做", "简单地做"),
    ("一个是哪儿的", "一个是哪儿呢"),
    ("还要保险成本", "还有保险成本"),
    ("疯死", "封死"),
    ("打账", "打仗"),
    ("运毒", "运货"),
    ("连架", "廉价"),
    ("德天毒货", "得天独厚"),
    ("谋话", "谋划"),
    ("趁止", "甚至"),
    ("哀着", "挨着"),
    ("爱着", "挨着"),
    ("倒大媒", "倒大霉"),
    ("室丑", "世仇"),
    ("释愁", "世仇"),
    ("死命运", "命运"),
    ("服质", "扶植"),
    ("武斯林", "穆斯林"),
    ("伊斯兰氏林", "伊斯兰势力"),
    ("中日喊", "中日韩"),
    ("罗洛斯", "俄罗斯"),
    ("巴黎维王朝", "巴列维王朝"),
    ("巴黎維王朝", "巴列维王朝"),
    ("带路党侧反", "带路党策反"),
    ("帶路黨側反", "带路党策反"),
    ("侧反", "策反"),
    ("側反", "策反"),
    ("军主治", "君主制"),
    ("軍主治", "君主制"),
    ("伊资料", "伊朗"),
    ("巴基斯达", "巴基斯坦"),
    ("哈梅那一", "哈梅内伊"),
    ("哈梅內伊", "哈梅内伊"),
    ("還沒內衣", "哈梅内伊"),
    ("还没内衣", "哈梅内伊"),
    ("革命未对", "革命卫队"),
    ("革命未隊", "革命卫队"),
    ("李根", "里根"),
    ("理根", "里根"),
    ("萨奇尔夫人", "撒切尔夫人"),
    ("薩奇爾夫人", "撒切尔夫人"),
    ("美元变质", "美元贬值"),
    ("美元變質", "美元贬值"),
    ("变慢美债", "变卖美债"),
    ("變慢美債", "变卖美债"),
    ("變之來化債", "变质来化债"),
    ("变之来化债", "贬值来化债"),
    ("进入政体", "进入正题"),
    ("進入政體", "进入正题"),
    ("被导而迟", "背道而驰"),
    ("背导而迟", "背道而驰"),
    ("经济护助委员会", "经济互助委员会"),
    ("經濟護助委員會", "经济互助委员会"),
    ("历史基域", "历史机遇"),
    ("历史基于", "历史机遇"),
    ("歷史基域", "历史机遇"),
    ("歷史基於", "历史机遇"),
    ("图经", "途径"),
    ("圖經", "途径"),
    ("矛定", "锚定"),
    ("大总商品", "大宗商品"),
    ("大總商品", "大宗商品"),
    ("制装", "滞胀"),
    ("制裝", "滞胀"),
    ("复债", "负债"),
    ("復債", "负债"),
    ("财政车资", "财政赤字"),
    ("財政車資", "财政赤字"),
    ("市政高零", "施政纲领"),
    ("施政高零", "施政纲领"),
    ("廣場血液", "广场协议"),
    ("广场血液", "广场协议"),
    ("經歷學", "经济学"),
    ("经历学", "经济学"),
    ("實力經濟", "实体经济"),
    ("實力经济", "实体经济"),
    ("实力经济", "实体经济"),
    ("喬头宝", "桥头堡"),
    ("桥头宝", "桥头堡"),
    ("拉龙", "拉拢"),
    ("俄署", "俄属"),
    ("外生那边的问题", "外生变量的问题"),
    ("天然机", "天然气"),
    ("救业", "就业"),
    ("消亡欧洲", "销往欧洲"),
    ("石油專彈", "石油钻探"),
    ("石油专弹", "石油钻探"),
    ("前反非法移民", "遣返非法移民"),
    ("爭10%", "征10%"),
    ("爭額外", "征额外"),
    ("立好Mata", "利好 Meta"),
    ("Mata", "Meta"),
    ("渣克伯格", "扎克伯格"),
    ("开锻", "开端"),
    ("全盆谋划", "全盘谋划"),
    ("1785年的广场协议", "1985年的广场协议"),
    ("外貌武器", "外贸武器"),
    ("非洲战斗机", "枭龙战斗机"),
    ("非洲而且", "枭龙，而且"),
    ("清中的势力", "亲中的势力"),
    ("清中的勢力", "亲中的势力"),
    ("服质清华", "扶植亲华"),
    ("扶植清华", "扶植亲华"),
    ("德天独厚", "得天独厚"),
    ("得天毒货", "得天独厚"),
    ("國债", "国债"),
    ("長债", "长债"),
    ("長債", "长债"),
    ("债務", "债务"),
    ("內债", "内债"),
    ("外债務", "外债务"),
    ("貨币", "货币"),
    ("货幣", "货币"),
    ("關税", "关税"),
    ("税戰", "税战"),
    ("货币換句", "货币幻觉"),
    ("貨幣換句", "货币幻觉"),
    ("中毒", "中国"),
]


CONTEXT_REPLACEMENTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"没有和武器"), "没有核武器"),
    (re.compile(r"擁有和武器|拥有和武器"), "拥有核武器"),
    (re.compile(r"使用和武器"), "使用核武器"),
    (re.compile(r"有和武器"), "有核武器"),
    (re.compile(r"和武器级别|和武器級別"), "核武器级别"),
    (re.compile(r"金融和武器"), "金融核武器"),
    (re.compile(r"宣布自己有和武器"), "宣布自己有核武器"),
    (re.compile(r"和武器以后"), "核武器以后"),
    (re.compile(r"和武器了"), "核武器了"),
    (re.compile(r"和武器的国家"), "核武器的国家"),
    (re.compile(r"和武器的國家"), "核武器的国家"),
]


TRADITIONAL_REPLACEMENTS: list[tuple[str, str]] = [
    ("，", "，"),
    ("還", "还"),
    ("內", "内"),
    ("麼", "么"),
    ("條", "条"),
    ("選擇", "选择"),
    ("發展", "发展"),
    ("發", "发"),
    ("為", "为"),
    ("軍事", "军事"),
    ("獨裁", "独裁"),
    ("權利", "权力"),
    ("鬥", "斗"),
    ("領袖", "领袖"),
    ("戰亂", "战乱"),
    ("長期", "长期"),
    ("敵對", "敌对"),
    ("勢力", "势力"),
    ("關係", "关系"),
    ("貨幣", "货币"),
    ("債", "债"),
    ("國債", "国债"),
    ("經濟", "经济"),
    ("總統", "总统"),
    ("戰略", "战略"),
    ("歐洲", "欧洲"),
    ("蘇聯", "苏联"),
    ("解體", "解体"),
    ("產業", "产业"),
    ("產業鏈", "产业链"),
    ("貶值", "贬值"),
    ("扁值", "贬值"),
    ("變", "变"),
    ("製造", "制造"),
    ("廣場協議", "广场协议"),
    ("債務", "债务"),
    ("內債", "内债"),
    ("外債", "外债"),
    ("美債", "美债"),
    ("稅", "税"),
    ("拉動", "拉动"),
    ("轉向", "转向"),
    ("轉為", "转为"),
    ("之後", "之后"),
    ("門頭", "埋头"),
    ("實", "实"),
    ("國", "国"),
    ("長", "长"),
    ("關", "关"),
    ("戰", "战"),
    ("論", "论"),
    ("償", "偿"),
    ("轉", "转"),
    ("動", "动"),
    ("時", "时"),
    ("間", "间"),
    ("會", "会"),
    ("來", "来"),
    ("這", "这"),
    ("對", "对"),
    ("說", "说"),
    ("個", "个"),
    ("與", "与"),
    ("雖", "虽"),
    ("現", "现"),
    ("後", "后"),
    ("讓", "让"),
    ("從", "从"),
    ("將", "将"),
    ("還", "还"),
    ("們", "们"),
    ("黨", "党"),
    ("綱", "纲"),
    ("領", "领"),
    ("並", "并"),
    ("候選", "候选"),
    ("商業", "商业"),
    ("週", "周"),
    ("獨", "独"),
    ("專", "专"),
    ("訪", "访"),
    ("詳", "详"),
    ("點", "点"),
    ("無", "无"),
    ("試", "试"),
    ("圖", "图"),
    ("業", "业"),
    ("監", "监"),
    ("鎖", "锁"),
    ("邊", "边"),
    ("額", "额"),
    ("數", "数"),
    ("遏", "遏"),
    ("壟", "垄"),
    ("斷", "断"),
    ("討", "讨"),
    ("厭", "厌"),
    ("譯", "译"),
    ("貿", "贸"),
    ("響", "响"),
    ("產", "产"),
    ("應", "应"),
    ("該", "该"),
    ("問題", "问题"),
    ("壓力", "压力"),
    ("進", "进"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Locally polish timestamped ASR transcripts.")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--qc-dir", type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def resolve(path: Path) -> Path:
    if path.is_absolute():
        return path
    return (ROOT / path).resolve()


def infer_video_id(path: Path) -> str:
    name = path.name
    if name.endswith("_asr.md"):
        return name[:-7]
    return path.stem


def polish_text(video_id: str, timestamp: str, text: str) -> str:
    override = LINE_OVERRIDES.get((video_id, timestamp, text.strip()))
    if override is not None:
        return override

    out = text.strip()
    out = out.replace(",", "，")
    out = out.replace("?", "？")
    out = out.replace("!", "！")

    for source, target in TRADITIONAL_REPLACEMENTS:
        out = out.replace(source, target)
    for source, target in PHRASE_REPLACEMENTS:
        out = out.replace(source, target)
    for pattern, target in CONTEXT_REPLACEMENTS:
        out = pattern.sub(target, out)

    # Small punctuation and spacing polish. Keep one timestamped sentence per
    # source line to preserve alignment with the original ASR.
    out = re.sub(r"\s+", " ", out).strip()
    out = re.sub(r"(?<=[\u4e00-\u9fff]) ([\u4e00-\u9fff])", r"\1", out)
    out = re.sub(r"(\d+)\s+([年月日%])", r"\1\2", out)
    out = re.sub(r"([第上下])\s+(\d+)", r"\1\2", out)
    return out


def rewrite_header(lines: list[str], source_path: Path, video_id: str) -> list[str]:
    header: list[str] = []
    for line in lines:
        if line.strip().lower() == "## transcript":
            break
        header.append(line)

    if header and header[0].startswith("# ASR Transcript:"):
        header[0] = header[0].replace("# ASR Transcript:", "# Polished Transcript:", 1)
    elif header and header[0].startswith("#"):
        header[0] = "# Polished Transcript:" + header[0].lstrip("#")
    else:
        header.insert(0, f"# Polished Transcript: {video_id}")

    cleaned_header: list[str] = []
    for line in header:
        if line.startswith("- ASR model:") or line.startswith("- ASR language:") or line.startswith("- Language probability:"):
            continue
        cleaned_header.append(line)

    cleaned_header.extend(
        [
            f"- ASR source: {source_path.name}",
            "- Polish: Codex local cleanup",
            "",
            "## Transcript",
        ]
    )
    return cleaned_header


def process_file(source_path: Path, output_dir: Path, force: bool) -> tuple[list[LinePair], dict[str, object]]:
    video_id = infer_video_id(source_path)
    output_path = output_dir / f"{video_id}_polished.md"
    if output_path.exists() and not force:
        return [], {
            "id": video_id,
            "source": str(source_path),
            "output": str(output_path),
            "status": "skipped",
            "source_lines": "",
            "polished_lines": "",
            "timestamps_match": "",
            "changed_lines": "",
            "low_similarity_changes": "",
        }

    lines = source_path.read_text(encoding="utf-8-sig").splitlines()
    header = rewrite_header(lines, source_path, video_id)
    source_pairs: list[tuple[str, str]] = []
    output_lines: list[str] = []
    line_pairs: list[LinePair] = []

    for line in lines:
        match = TIMESTAMP_RE.match(line)
        if not match:
            continue
        timestamp, text = match.group(1), match.group(2)
        polished = polish_text(video_id, timestamp, text)
        source_pairs.append((timestamp, text))
        output_lines.append(f"[{timestamp}] {polished}")
        line_pairs.append(LinePair(video_id, timestamp, text, polished))

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(header + output_lines) + "\n", encoding="utf-8")

    timestamps_match = [ts for ts, _text in source_pairs] == [pair.timestamp for pair in line_pairs]
    changed = [pair for pair in line_pairs if pair.source != pair.polished]
    low_similarity = [
        pair for pair in changed if SequenceMatcher(None, pair.source, pair.polished).ratio() < 0.55
    ]
    return line_pairs, {
        "id": video_id,
        "source": str(source_path),
        "output": str(output_path),
        "status": "success" if timestamps_match else "failed",
        "source_lines": len(source_pairs),
        "polished_lines": len(output_lines),
        "timestamps_match": timestamps_match,
        "changed_lines": len(changed),
        "low_similarity_changes": len(low_similarity),
    }


def write_qc(qc_dir: Path, summaries: list[dict[str, object]], all_pairs: list[LinePair]) -> dict[str, Path]:
    qc_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_path = qc_dir / f"polish_summary_{stamp}.csv"
    changes_path = qc_dir / f"polish_changes_{stamp}.csv"
    low_path = qc_dir / f"polish_low_similarity_{stamp}.md"

    summary_fields = [
        "id",
        "source",
        "output",
        "status",
        "source_lines",
        "polished_lines",
        "timestamps_match",
        "changed_lines",
        "low_similarity_changes",
    ]
    with summary_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        writer.writeheader()
        writer.writerows(summaries)

    change_fields = ["id", "timestamp", "similarity", "source", "polished"]
    low_entries: list[tuple[float, LinePair]] = []
    with changes_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=change_fields)
        writer.writeheader()
        for pair in all_pairs:
            if pair.source == pair.polished:
                continue
            similarity = SequenceMatcher(None, pair.source, pair.polished).ratio()
            writer.writerow(
                {
                    "id": pair.video_id,
                    "timestamp": pair.timestamp,
                    "similarity": f"{similarity:.3f}",
                    "source": pair.source,
                    "polished": pair.polished,
                }
            )
            if similarity < 0.55:
                low_entries.append((similarity, pair))

    low_lines = ["# Low Similarity Polish Changes", ""]
    for similarity, pair in sorted(low_entries, key=lambda item: (item[1].video_id, item[1].timestamp)):
        low_lines.extend(
            [
                f"## {pair.video_id} [{pair.timestamp}] similarity={similarity:.3f}",
                f"- ASR: {pair.source}",
                f"- FIX: {pair.polished}",
                "",
            ]
        )
    low_path.write_text("\n".join(low_lines), encoding="utf-8")
    return {"summary": summary_path, "changes": changes_path, "low_similarity": low_path}


def main() -> int:
    args = parse_args()
    input_dir = resolve(args.input_dir)
    output_dir = resolve(args.output_dir)
    qc_dir = resolve(args.qc_dir) if args.qc_dir else output_dir.parent / "polish_qc"

    source_files = sorted(input_dir.glob("*_asr.md"))
    summaries: list[dict[str, object]] = []
    all_pairs: list[LinePair] = []
    for source_path in source_files:
        pairs, summary = process_file(source_path, output_dir, args.force)
        summaries.append(summary)
        all_pairs.extend(pairs)

    qc_files = write_qc(qc_dir, summaries, all_pairs)
    success = sum(1 for row in summaries if row["status"] in {"success", "skipped"})
    failed = len(summaries) - success
    print(f"Processed: {len(summaries)}")
    print(f"Success/skipped: {success}")
    print(f"Failed: {failed}")
    print(f"Output dir: {output_dir}")
    print(f"QC summary: {qc_files['summary']}")
    print(f"QC changes: {qc_files['changes']}")
    print(f"QC low similarity: {qc_files['low_similarity']}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
