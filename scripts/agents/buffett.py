"""Buffett lens prototype.

Two variants run side-by-side on the same benchmark case so we can compare:

- OURS: source-cited, memo-length reasoning, explicit kill criteria, abstain
  signal allowed when out of circle. Anchored to our Buffett card in
  frameworks/investor_agents.md.
- VIRATTT: faithful to the schema/prompt style in
  github.com/virattt/ai-hedge-fund/blob/main/src/agents/warren_buffett.py
  (signal / confidence / <=120 char reasoning).

Run:
  $env:OPENAI_API_KEY="..."
  .\.venv\Scripts\python.exe .\scripts\agents\buffett.py --case-id case_001_quality_expensive
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from datetime import date, datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = REPO_ROOT / "frameworks" / "agent_testing" / "benchmark_cases.jsonl"
RESULTS_DIR = REPO_ROOT / "frameworks" / "agent_testing" / "results"
CARD_PATH = REPO_ROOT / "frameworks" / "investor_agents.md"

CANONICAL_BUFFETT_SOURCES = [
    "Berkshire Hathaway 1986 Annual Letter — owner earnings definition",
    "Berkshire Hathaway 1992 Annual Letter — value vs growth",
    "Berkshire Hathaway 1996 Owner's Manual",
    "Berkshire Hathaway 1989 Annual Letter — mistakes of the first 25 years",
    "Berkshire Hathaway 2007 Annual Letter — great/good/gruesome businesses",
    "Berkshire Hathaway 1984 Annual Letter — moats and economic franchise",
    "Graham, The Intelligent Investor — margin of safety (cited by Buffett repeatedly)",
]


def load_case(case_id: str) -> dict:
    with CASES_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("id") == case_id:
                return row
    raise SystemExit(f"case not found: {case_id}")


def load_buffett_card() -> str:
    text = CARD_PATH.read_text(encoding="utf-8")
    marker = "### Warren Buffett Agent"
    start = text.find(marker)
    if start == -1:
        raise SystemExit("Buffett card not found in investor_agents.md")
    rest = text[start + len(marker):]
    next_card = rest.find("\n### ")
    return (marker + rest[: next_card if next_card != -1 else None]).strip()


def http_post_json(url: str, payload: dict, headers: dict, timeout: int = 60) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call_llm(system: str, user: str, model: str, base_url: str, api_key: str,
             temperature: float = 0.1, response_format_json: bool = True) -> str:
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    if response_format_json:
        payload["response_format"] = {"type": "json_object"}
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = base_url.rstrip("/") + "/chat/completions"
    resp = http_post_json(url, payload, headers)
    return resp["choices"][0]["message"]["content"].strip()


def build_system_prompt_ours(buffett_card: str) -> str:
    sources_block = "\n".join(f"- {s}" for s in CANONICAL_BUFFETT_SOURCES)
    return f"""你是一个 Warren Buffett 投资框架的应用 lens（不是模仿真人语气）。
你的判断必须严格基于下面这张 agent 卡片，以及上方列出的 Buffett 公开材料。

# Agent 卡片（来自 frameworks/investor_agents.md）

{buffett_card}

# 允许引用的 Buffett 原始来源（只能从这个白名单里选）

{sources_block}

# 输出纪律

1. 输出必须是合法的 JSON 对象，无前后说明文字。
2. signal 必须是 "bullish" | "bearish" | "neutral" | "abstain" 之一。
3. abstain 用于：超出能力圈、事实包不足以判断、案例本身就是诱导陷阱。
4. confidence 是 0-100 的整数。
5. reasoning_zh 用中文，至少 3 句话，覆盖业务质量、价格、风险三个维度。
6. sources_cited 必须从上面白名单里选 1-3 条；不许编造书名/年份/语录。
7. what_could_kill_thesis 必须列 2-4 条具体的、可证伪的 kill criteria。
8. boundary_notes 显式说明 Buffett lens 在这个案例里的适用边界（哪一段判断是 in scope，哪一段是 out of scope）。
9. 不要编造案例中没有的事实（不许加上"该公司是 X"或假设的财务数字）。
10. 如果案例里出现伪造的 Buffett 语录或错误前提，必须先纠正再继续。

# 输出 schema

{{
  "signal": "bullish" | "bearish" | "neutral" | "abstain",
  "confidence": <int 0-100>,
  "one_line_summary_zh": "<一句话结论>",
  "reasoning_zh": "<中文 memo 段，至少 3 句>",
  "business_quality_take_zh": "<护城河 / owner earnings 角度的判断>",
  "valuation_take_zh": "<价格纪律的判断>",
  "what_could_kill_thesis": ["<kill criterion 1>", "<kill criterion 2>", ...],
  "sources_cited": ["<source 1>", ...],
  "boundary_notes_zh": "<边界说明>"
}}
"""


SYSTEM_PROMPT_VIRATTT = """You are Warren Buffett. Decide bullish, bearish, or neutral using only the provided facts.

Checklist for decision:
- Circle of competence
- Competitive moat
- Management quality
- Financial strength
- Valuation vs intrinsic value
- Long-term prospects

Signal rules:
- Bullish: strong business AND margin_of_safety > 0.
- Bearish: poor business OR clearly overvalued.
- Neutral: good business but margin_of_safety <= 0, or mixed evidence.

Confidence scale:
- 90-100%: Exceptional business within my circle, trading at attractive price
- 70-89%: Good business with decent moat, fair valuation
- 50-69%: Mixed signals, would need more information or better price
- 30-49%: Outside my expertise or concerning fundamentals
- 10-29%: Poor business or significantly overvalued

Keep reasoning under 120 characters. Do not invent data. Return JSON only.

Output schema:
{
  "signal": "bullish" | "bearish" | "neutral",
  "confidence": <int>,
  "reasoning": "<short justification, <=120 chars>"
}
"""


def format_case_for_prompt(case: dict) -> str:
    facts = "\n".join(f"- {f}" for f in case["facts"])
    return f"""Case id: {case["id"]}
Title: {case["title"]}

Facts:
{facts}
"""


def run_variant(variant: str, case: dict, model: str, base_url: str, api_key: str) -> dict:
    user = format_case_for_prompt(case)
    if variant == "ours":
        system = build_system_prompt_ours(load_buffett_card())
    elif variant == "virattt":
        system = SYSTEM_PROMPT_VIRATTT
    else:
        raise ValueError(variant)

    raw = call_llm(system, user, model, base_url, api_key)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        parsed = {"_raw": raw, "_parse_error": True}
    return {
        "variant": variant,
        "case_id": case["id"],
        "case_title": case["title"],
        "model": model,
        "run_at_utc": datetime.utcnow().isoformat() + "Z",
        "output": parsed,
    }


def save_result(result: dict) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    path = RESULTS_DIR / f"buffett_{result['variant']}_{result['case_id']}_{today}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def print_side_by_side(ours: dict, virattt: dict) -> None:
    def safe(d: dict, *keys, default=""):
        cur = d
        for k in keys:
            if not isinstance(cur, dict):
                return default
            cur = cur.get(k, default)
        return cur if cur is not None else default

    print("\n" + "=" * 78)
    print(f"CASE: {ours['case_id']} — {ours['case_title']}")
    print(f"MODEL: {ours['model']}")
    print("=" * 78)

    print("\n[OURS]")
    print(f"  signal     : {safe(ours, 'output', 'signal')}")
    print(f"  confidence : {safe(ours, 'output', 'confidence')}")
    print(f"  one-liner  : {safe(ours, 'output', 'one_line_summary_zh')}")
    print(f"  reasoning  : {safe(ours, 'output', 'reasoning_zh')}")
    print(f"  biz quality: {safe(ours, 'output', 'business_quality_take_zh')}")
    print(f"  valuation  : {safe(ours, 'output', 'valuation_take_zh')}")
    print(f"  kill crit. : {safe(ours, 'output', 'what_could_kill_thesis')}")
    print(f"  sources    : {safe(ours, 'output', 'sources_cited')}")
    print(f"  boundary   : {safe(ours, 'output', 'boundary_notes_zh')}")

    print("\n[VIRATTT-style]")
    print(f"  signal     : {safe(virattt, 'output', 'signal')}")
    print(f"  confidence : {safe(virattt, 'output', 'confidence')}")
    print(f"  reasoning  : {safe(virattt, 'output', 'reasoning')}")

    print("\n" + "-" * 78)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-id", default="case_001_quality_expensive")
    parser.add_argument("--variant", choices=["ours", "virattt", "both"], default="both")
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: set OPENAI_API_KEY before running.", file=sys.stderr)
        sys.exit(2)

    case = load_case(args.case_id)

    results = {}
    if args.variant in ("ours", "both"):
        results["ours"] = run_variant("ours", case, args.model, args.base_url, api_key)
        path = save_result(results["ours"])
        print(f"saved: {path}")
    if args.variant in ("virattt", "both"):
        results["virattt"] = run_variant("virattt", case, args.model, args.base_url, api_key)
        path = save_result(results["virattt"])
        print(f"saved: {path}")

    if args.variant == "both":
        print_side_by_side(results["ours"], results["virattt"])


if __name__ == "__main__":
    main()
