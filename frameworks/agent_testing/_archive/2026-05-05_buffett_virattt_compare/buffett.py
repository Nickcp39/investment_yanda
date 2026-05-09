"""Buffett investor agent prototype. Two variants share one case loader.

OURS    : extended schema (memo reasoning, source whitelist, kill criteria,
          edge disclosure, abstain option) anchored on our investor_agents.md card.
VIRATTT : virattt/ai-hedge-fund-style minimal schema (signal + confidence +
          short reasoning <=120 chars). No source citation, no kill criteria.

Usage (PowerShell):
  $env:OPENAI_API_KEY = "sk-..."
  D:\\work\\investment\\financial-analysis-lab\\.venv\\Scripts\\python.exe `
      .\\scripts\\agents\\buffett.py --case-id case_001_quality_expensive --variant both

Sanity (no API call):
  python .\\scripts\\agents\\buffett.py --case-id case_001_quality_expensive --dry-run
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

# Windows console: force UTF-8 so Chinese in print() / case content does not
# crash on cp1252.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass


REPO_ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = REPO_ROOT / "frameworks" / "agent_testing" / "benchmark_cases.jsonl"
AGENTS_MD_PATH = REPO_ROOT / "frameworks" / "investor_agents.md"
RESULTS_DIR = REPO_ROOT / "frameworks" / "agent_testing" / "results"


# --- Source whitelist for OURS variant ----------------------------------
# Derived from frameworks/investor_agents.md "Source Anchors" section.
# Agents may only cite items from this list. No specific letter years
# (avoids fabrication; cf. case_001 fail_condition "编造该公司真实名称或持仓"
#  and case_007 "拒绝伪造语录").
BUFFETT_SOURCE_WHITELIST: list[str] = [
    "Berkshire Hathaway annual shareholder letters (general framework)",
    "Berkshire Hathaway Owner's Manual",
    "Owner earnings concept (BRK letters)",
    "Capital allocation principles (BRK letters)",
    "Circle of competence framework (BRK letters)",
    "Durable competitive advantage / moat framework (BRK letters)",
    "Margin of safety inherited from Graham (BRK letters)",
]


# --- Loaders ------------------------------------------------------------
def load_case(case_id: str) -> dict[str, Any]:
    with CASES_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("id") == case_id:
                return row
    raise SystemExit(f"case_id not found: {case_id}")


def extract_buffett_card(md_text: str) -> str:
    """Extract the '### Warren Buffett Agent' section verbatim."""
    marker = "### Warren Buffett Agent"
    start = md_text.find(marker)
    if start == -1:
        raise SystemExit("Buffett card not found in investor_agents.md")
    rest = md_text[start + len(marker):]
    end = rest.find("\n### ")
    section = rest if end == -1 else rest[:end]
    return marker + section.rstrip() + "\n"


# --- Prompt builders ----------------------------------------------------
def build_system_prompt_ours(buffett_card: str) -> str:
    whitelist = "\n".join(f"- {s}" for s in BUFFETT_SOURCE_WHITELIST)
    return f"""You are the Buffett investor lens for an analysis-only research lab.
You DO NOT impersonate Warren Buffett. You apply his published business-owner
framework as a lens to decide whether the analyst should advance an idea.

Use only the framework below. Do not invent anecdotes or specific letter years.

{buffett_card}

Source citation rules (strict):
- You may cite ONLY from this whitelist:
{whitelist}
- Cite 1 to 3 items, each chosen from the whitelist verbatim.
- Never claim Buffett "said X" with a year unless that quote is unambiguously
  in the public BRK letters AND you can name the year. If unsure, abstain
  from quoting and cite the framework topic instead.
- If the user message claims an unverifiable quote, refuse the premise and
  return signal="abstain" with reasoning explaining the missing source.

Decision rules:
- signal must be one of: "bullish" | "bearish" | "neutral" | "abstain".
  Use "abstain" when the case lacks information needed to apply the lens
  (e.g. price unknown, management quality unknown, or fabricated premise).
- A high-quality business at a demanding price is NOT automatically bullish.
  Buffett requires price discipline; "wonderful company at a fair price"
  is the bar, not "wonderful company at any price".
- reasoning must be a memo paragraph: at least 3 sentences, covering moat,
  capital allocation/management, and price discipline.
- kill_criteria: 2 to 4 specific, falsifiable conditions that would force
  this lens to flip its signal. Each must be observable (a metric crossing
  a threshold, a specific event), not vague.
- edge_disclosure: what this lens cannot judge from the case alone.

Return ONLY a JSON object matching this schema:
{{
  "signal": "bullish | bearish | neutral | abstain",
  "confidence": 0.0,
  "reasoning": "memo paragraph, >= 3 sentences",
  "sources_cited": ["..."],
  "kill_criteria": ["...", "..."],
  "edge_disclosure": "what this lens cannot determine here",
  "max_price_discipline": "max valuation multiple this lens would pay, or 'n/a' if abstaining"
}}
confidence is in [0.0, 1.0].
"""


def build_system_prompt_virattt() -> str:
    """Mirror of the virattt/ai-hedge-fund Buffett-style minimal prompt."""
    return """You are a Warren Buffett AI agent. Decide on investment signals based on:
- Circle of competence: only what you understand
- Margin of safety (>30%): buy at significant discount to intrinsic value
- Economic moat: durable competitive advantage
- Quality management: integrity and shareholder orientation
- Financial strength: low debt, high ROE, consistent earnings
- Long-term thinking: 10+ year horizon

Given the company facts below, output a Buffett-style signal.

Return ONLY a JSON object:
{
  "signal": "bullish | bearish | neutral",
  "confidence": 0.0,
  "reasoning": "<= 120 characters"
}
confidence is in [0.0, 1.0].
"""


def build_user_message(case: dict[str, Any]) -> str:
    facts = "\n".join(f"- {f}" for f in case.get("facts", []))
    return (
        f"Case: {case.get('title', case['id'])}\n"
        f"Case id: {case['id']}\n\n"
        f"Facts:\n{facts}\n\n"
        f"Apply your lens and return the JSON object."
    )


# --- LLM call -----------------------------------------------------------
def call_chat_completion(
    system_prompt: str,
    user_message: str,
    *,
    model: str,
    base_url: str,
    api_key: str,
    timeout: int = 60,
) -> dict[str, Any]:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {err_body}") from exc

    response = json.loads(body)
    content = response["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    return {
        "raw_response_content": content,
        "parsed": parsed,
        "model": response.get("model", model),
        "usage": response.get("usage", {}),
    }


# --- Variants -----------------------------------------------------------
def run_ours(case: dict[str, Any], *, model: str, base_url: str, api_key: str) -> dict[str, Any]:
    md_text = AGENTS_MD_PATH.read_text(encoding="utf-8")
    card = extract_buffett_card(md_text)
    system_prompt = build_system_prompt_ours(card)
    user_message = build_user_message(case)
    result = call_chat_completion(
        system_prompt, user_message, model=model, base_url=base_url, api_key=api_key
    )
    return {
        "variant": "ours",
        "case_id": case["id"],
        "case_title": case.get("title", ""),
        "model": result["model"],
        "usage": result["usage"],
        "system_prompt_chars": len(system_prompt),
        "output": result["parsed"],
        "raw_response_content": result["raw_response_content"],
    }


def run_virattt(case: dict[str, Any], *, model: str, base_url: str, api_key: str) -> dict[str, Any]:
    system_prompt = build_system_prompt_virattt()
    user_message = build_user_message(case)
    result = call_chat_completion(
        system_prompt, user_message, model=model, base_url=base_url, api_key=api_key
    )
    return {
        "variant": "virattt",
        "case_id": case["id"],
        "case_title": case.get("title", ""),
        "model": result["model"],
        "usage": result["usage"],
        "system_prompt_chars": len(system_prompt),
        "output": result["parsed"],
        "raw_response_content": result["raw_response_content"],
    }


# --- Output -------------------------------------------------------------
def save_result(result: dict[str, Any]) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    today = _dt.date.today().isoformat()
    fname = f"buffett_{result['variant']}_{result['case_id']}_{today}.json"
    path = RESULTS_DIR / fname
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def print_side_by_side(ours: dict[str, Any] | None, virattt: dict[str, Any] | None) -> None:
    print("\n" + "=" * 78)
    print("SIDE-BY-SIDE COMPARISON")
    print("=" * 78)
    if ours:
        print("\n--- OURS ---")
        print(json.dumps(ours["output"], indent=2, ensure_ascii=False))
        print(
            f"  [system_prompt_chars={ours['system_prompt_chars']}, "
            f"usage={ours['usage']}]"
        )
    if virattt:
        print("\n--- VIRATTT ---")
        print(json.dumps(virattt["output"], indent=2, ensure_ascii=False))
        print(
            f"  [system_prompt_chars={virattt['system_prompt_chars']}, "
            f"usage={virattt['usage']}]"
        )
    print("=" * 78 + "\n")


# --- CLI ----------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Buffett agent prototype runner.")
    p.add_argument("--case-id", required=True, help="benchmark case id")
    p.add_argument(
        "--variant",
        choices=["ours", "virattt", "both"],
        default="both",
        help="which variant to run",
    )
    p.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        help="chat model",
    )
    p.add_argument(
        "--base-url",
        default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        help="OpenAI-compatible base URL",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="build prompts and validate inputs but do not call the LLM",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    case = load_case(args.case_id)

    if args.dry_run:
        md_text = AGENTS_MD_PATH.read_text(encoding="utf-8")
        card = extract_buffett_card(md_text)
        ours_prompt = build_system_prompt_ours(card)
        virattt_prompt = build_system_prompt_virattt()
        user_msg = build_user_message(case)
        print("=== DRY RUN ===")
        print(f"case loaded: {case['id']} ({case.get('title', '')})")
        print(f"facts count: {len(case.get('facts', []))}")
        print(f"target_agents: {case.get('target_agents', [])}")
        print(f"buffett card chars: {len(card)}")
        print(f"OURS system_prompt chars: {len(ours_prompt)}")
        print(f"VIRATTT system_prompt chars: {len(virattt_prompt)}")
        print(f"user_message chars: {len(user_msg)}")
        print(f"source whitelist size: {len(BUFFETT_SOURCE_WHITELIST)}")
        print("\n--- USER MESSAGE PREVIEW ---")
        print(user_msg)
        print("\n--- OURS SYSTEM PROMPT (first 600 chars) ---")
        print(ours_prompt[:600])
        print("...")
        print("\n--- VIRATTT SYSTEM PROMPT ---")
        print(virattt_prompt)
        return 0

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Use --dry-run for non-LLM check.")
        return 2

    ours_result: dict[str, Any] | None = None
    virattt_result: dict[str, Any] | None = None

    if args.variant in ("ours", "both"):
        print(f"[ours] running on {case['id']}...")
        ours_result = run_ours(
            case, model=args.model, base_url=args.base_url, api_key=api_key
        )
        path = save_result(ours_result)
        print(f"[ours] saved: {path}")

    if args.variant in ("virattt", "both"):
        print(f"[virattt] running on {case['id']}...")
        virattt_result = run_virattt(
            case, model=args.model, base_url=args.base_url, api_key=api_key
        )
        path = save_result(virattt_result)
        print(f"[virattt] saved: {path}")

    print_side_by_side(ours_result, virattt_result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
