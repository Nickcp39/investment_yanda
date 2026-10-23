#!/usr/bin/env python
"""Optional AI step: call Claude Code headless (`claude -p`) to (1) explain the last two weeks' move with sources,
(2) fill the data items the fetch layer could not get (needs_ai.json), (3) write a short reading of the numbers.
It writes <folder>/ai_notes.md and never touches the computed files. Costs money: capped by --budget (USD)."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import OUT, REPO, log, write_json  # noqa: E402

ALLOWED = ["WebFetch", "WebSearch", "Read", "Write", "Glob", "Grep", "Edit"]


def build_prompt(folder: Path, S, needs):
    rel = folder.relative_to(REPO).as_posix()
    Q, NE, L = S["qqq"], S["ndx_eras"], S["levels"]
    hist = OUT / "history.csv"
    prev = ""
    if hist.exists():
        lines = hist.read_text(encoding="utf-8-sig").strip().splitlines()
        if len(lines) >= 3:
            prev = f"上一轮（history.csv 倒数第二行）：{lines[-2]}\n列名：{lines[0]}"
    summary = {
        "as_of": S["as_of"], "QQQ": {"close": round(Q["close"], 2), "距历史最高%": round(Q["drawdown_pct"], 1), "1月%": round(Q["ret_1m_pct"], 1), "vs200dma%": round(Q["vs_200dma_pct"], 1)},
        "纳指四把尺子 偏离%/分位": {k: [round(NE[k]["dev"], 1), round(NE[k]["pct"], 0)] for k in NE},
        "估值": {"NDX前瞻PE": L["fwd_pe"], "CAPE": L["cape"], "10y": L["tnx"], "VIX": L["vix"], "金": L["gold"]},
        "热度": S["heat_by_group"], "总热度": round(S["heat_overall"], 0),
        "QQQ σ通道": {k: round(v, 2) for k, v in S["dca_channel"]["QQQ"].items() if k in ("cur_sigma", "minus1sd", "to_minus1sd_pct")},
    }
    needs_txt = "\n".join(f"- {n['key']}（状态 {n['status']}，最后日期 {n['last'] or '无'}，阈值 {n['threshold_days']} 天）：{n['what']}" for n in needs) or "- 无"
    return f"""你在投资研究 lab（当前目录就是仓库根目录）里做「市场体温」流水线的 AI 补充步骤。数值已由 Python 算好并写在 {rel}/temp.md 与 temp.json；**不要修改任何已生成的数字文件，不要改 data/ 下的缓存**。只新建或覆盖一个文件：`{rel}/ai_notes.md`。

已算好的读数摘要（JSON）：
{json.dumps(summary, ensure_ascii=False)}
{prev}

请在 `{rel}/ai_notes.md` 里写三节，中文，每个数字都带来源 URL 和日期，不给买卖建议：

## 1. 近两周美股为什么这样动
用 WebSearch / WebFetch 查最近两周（截至 {S['as_of']}）美股、纳指、QQQ 大跌或大涨的原因，写 3–5 条，每条一句话 + 来源（优先 Reuters / Bloomberg / WSJ / FT / CNBC / FactSet / 美联储与 BLS 原文）+ 日期。只写有来源的事实，不写推测。

## 2. 数据补齐
下面这些数据项本机抓取失败或已过期。请逐项去官方或可靠来源找最新值，写成表：数据项 | 最新值 | 数据日期 | 来源 URL | 备注。找不到就写「未核实」。
{needs_txt}

## 3. 读数怎么读
用 lab 一贯的口吻（简短、克制、不预测）写 5–8 行：价格 / 估值 / 经济 / 流动性 / 黄金五组热度各自说明什么；和上一轮比变了什么；哪一项最值得下次盯。结尾一句：「以上是体温读数，不是建议。」

规则：不确定就写「未核实」；不编造数字；不做买卖建议；完成后只输出一行「done」。"""


def find_claude():
    """locate the Claude Code CLI: env override, PATH (with Windows .cmd shim), then the npm global folder"""
    import os
    cands = [os.environ.get("MARKET_TEMP_CLAUDE"), shutil.which("claude"), shutil.which("claude.cmd")]
    appdata = os.environ.get("APPDATA")
    if appdata:
        npm = Path(appdata) / "npm"
        cands += [str(npm / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"), str(npm / "claude.cmd"), str(npm / "claude")]
    cands += [str(Path.home() / ".local" / "bin" / "claude.exe"), str(Path.home() / ".local" / "bin" / "claude")]
    for c in cands:
        if c and Path(c).exists():
            return c
    return None


def run_ai(folder: Path, S, needs, model="sonnet", budget=3.0, max_turns=30):
    exe = find_claude()
    if not exe:
        log("ai: claude CLI not found (PATH, npm global dir, ~/.local/bin, env MARKET_TEMP_CLAUDE); skipped. Install: npm i -g @anthropic-ai/claude-code")
        return None
    prompt = build_prompt(folder, S, needs)
    (folder / "ai_prompt.md").write_text(prompt, encoding="utf-8")
    cmd = [exe, "-p", "--model", model, "--max-turns", str(max_turns), "--max-budget-usd", str(budget), "--output-format", "json",
           "--permission-mode", "acceptEdits", "--allowedTools", *ALLOWED]
    log("ai: calling", Path(exe).name, "model", model, "budget", budget)
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(REPO), timeout=1500,
                           shell=exe.lower().endswith(".cmd"))
    except subprocess.TimeoutExpired:
        log("ai: timed out")
        return None
    out = {"returncode": r.returncode, "stderr_tail": r.stderr[-1500:]}
    try:
        js = json.loads(r.stdout)
        out.update({k: js.get(k) for k in ("total_cost_usd", "duration_api_ms", "num_turns", "is_error", "stop_reason", "session_id")})
        out["result_tail"] = (js.get("result") or "")[-800:]
    except Exception:  # noqa: BLE001
        out["stdout_tail"] = r.stdout[-1500:]
    write_json(folder / "ai_run.json", out)
    notes = folder / "ai_notes.md"
    if not notes.exists():
        notes.write_text("# AI notes\n\n(模型没有写入文件，以下是其输出原文)\n\n" + (out.get("result_tail") or out.get("stdout_tail") or ""), encoding="utf-8")
    log(f"ai: rc={r.returncode} cost=${out.get('total_cost_usd', '?')} turns={out.get('num_turns', '?')} -> {notes.relative_to(REPO)}")
    return out
