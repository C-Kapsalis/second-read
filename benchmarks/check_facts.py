"""Deterministic check for invented facts in rewrites.

An LLM judge is unreliable on long rewrites, so this script checks them
mechanically. For every kept run of a `claude plugin eval --keep-temp` log it
finds the report the model wrote, takes the rewritten or corrected version,
and lists every checkable token in it (inline code, URLs, email addresses,
numbers, prices, percentages, versions and dates). A token that does not
appear in the original input counts as invented. Bracketed placeholders such
as [expiry date] or [confirm: X or Y] are ignored, because they are the
correct way to mark a missing fact.

Usage:
  python3 benchmarks/check_facts.py benchmarks/eval.log [more.log ...] --json facts.json

The JSON holds, per format and arm, how many runs produced a rewrite and how
many of those rewrites added no new token, plus every flagged token for audit.
report.py --facts facts.json uses it for the "no invented facts" metric.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CASES = REPO / "benchmarks" / "cases"

KEPT_RE = re.compile(r"kept temp: (\S+)")
SKILL_RE = re.compile(r'"skill"\s*:\s*"second-read:')
HEREDOC_RE = re.compile(r"cat > (resources/\S+) <<'(\w+)'\n(.*?)\n\2\n", re.S)
REWRITE_HEAD_RE = re.compile(
    r"^#{1,4} .*\b(rewrite|rewritten|corrected|revised|fixed version|improved version|new version|suggested version|final version)\b.*$",
    re.I | re.M)
STOP_HEAD_RE = re.compile(
    r"^(#{1,4} .*\b(fact[- ]?check|checks?|self[- ]check|score|scorecard|verdict|fix(es)?|changes|what (i|we) changed|notes|move to another page|why|sources?|ledger|passed|failed)\b.*"
    r"|(\*\*)?(self[- ]check|fact[- ]?check|checks|passed|failed)\b.*"
    r"|\|\s*(in the rewrite|item|fact|claim)\s*\|.*)$",
    re.I | re.M)
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]*\]")
TOKEN_RES = [
    re.compile(r"`([^`\n]+)`"),                                  # inline code
    re.compile(r"https?://[^\s)>\]]+"),                          # URLs
    re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"),                  # emails
    re.compile(r"[$€£]\s?\d[\d,]*(?:\.\d+)?"),                   # prices
    re.compile(r"\b\d[\d,]*(?:\.\d+)?\s?%"),                     # percentages
    re.compile(r"\bv?\d+\.\d+(?:\.\d+)?\b"),                     # versions, decimals
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),                        # ISO dates
    re.compile(r"\b\d{2,}[\d,]*\b"),                             # numbers of 2+ digits
]
# Lengths, scores and counts a reviewer adds about the copy, not to it.
META_RE = re.compile(r"\b\d+\s*(characters?|chars|words?)\b|\b\d+/100\b|\bH[1-6]\b", re.I)


def case_inputs() -> dict:
    out = {}
    for scaffold in sorted(CASES.glob("*/scaffold.sh")):
        text = scaffold.read_text()
        bodies = [m.group(3) for m in HEREDOC_RE.finditer(text)]
        if bodies:
            out[scaffold.parent.name] = "\n".join(bodies)
    return out


def case_format(name: str) -> str:
    m = re.match(r"sr-(email|social|landing|blog|docs)-\d+", name)
    return m.group(1) if m else "other"


def signature(text: str) -> str:
    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 25]
    return max(lines, key=len) if lines else text.strip()[:60]


def trace_parts(path: Path):
    """(raw text, last report.md content written) from a trace.jsonl."""
    raw = path.read_text(errors="replace")
    report = None
    for line in raw.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = event.get("message")
        content = msg.get("content") if isinstance(msg, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if block.get("type") == "tool_use" and block.get("name") == "Write":
                inp = block.get("input") or {}
                if str(inp.get("file_path", "")).endswith("report.md"):
                    report = inp.get("content", "")
    return raw, report


FENCE_RE = re.compile(r"^(`{3,}|~{3,})[^\n]*\n(.*?)^\1[ \t]*$", re.S | re.M)


def rewrite_section(report: str):
    """The rewrite is the largest fenced code block in the report: every prompt
    asks for the fixed version as one fenced block. Without a fence there is
    no rewrite to check."""
    blocks = [m.group(2) for m in FENCE_RE.finditer(report)]
    return max(blocks, key=len) if blocks else None


def rewrite_section_by_heading(report: str):
    heads = list(REWRITE_HEAD_RE.finditer(report))
    if not heads:
        return None
    start = heads[-1].end()
    rest = report[start:]
    stop = STOP_HEAD_RE.search(rest)
    return rest[: stop.start()] if stop else rest


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower().replace(",", "")


def new_tokens(rewrite: str, original: str) -> list:
    body = PLACEHOLDER_RE.sub(" ", rewrite)
    body = META_RE.sub(" ", body)
    orig = norm(original)
    found = []
    for rx in TOKEN_RES:
        for m in rx.finditer(body):
            tok = m.group(1) if rx.groups else m.group(0)
            tok = tok.strip().rstrip(".,;:")
            if not tok or norm(tok) in orig:
                continue
            found.append(tok)
    return sorted(set(found))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("logs", nargs="+")
    ap.add_argument("--json", default=None, help="write results here")
    args = ap.parse_args(argv)

    inputs = case_inputs()
    sigs = {case: signature(text) for case, text in inputs.items()}
    dirs = []
    for log in args.logs:
        for m in KEPT_RE.finditer(Path(log).read_text(errors="replace")):
            if m.group(1) not in dirs:
                dirs.append(m.group(1))

    stats = defaultdict(lambda: {"runs": 0, "rewrites": 0, "clean": 0})
    flagged = []
    for d in dirs:
        trace = Path(d) / "out" / "trace.jsonl"
        if not trace.exists():
            continue
        raw, report = trace_parts(trace)
        case = next((c for c, s in sigs.items() if s and s.replace('"', '\\"') in raw or s in raw), None)
        if case is None:
            continue
        arm = "with" if SKILL_RE.search(raw) else "without"
        fmt = case_format(case)
        for key in ((fmt, arm), ("all", arm)):
            stats[key]["runs"] += 1
        section = rewrite_section(report or "")
        if not section:
            continue
        toks = new_tokens(section, inputs[case])
        for key in ((fmt, arm), ("all", arm)):
            stats[key]["rewrites"] += 1
            stats[key]["clean"] += not toks
        if toks:
            flagged.append({"case": case, "arm": arm, "dir": d, "tokens": toks})

    out = {"stats": {f"{f}|{a}": v for (f, a), v in sorted(stats.items())}, "flagged": flagged}
    for (f, a), v in sorted(stats.items()):
        rate = f"{100 * v['clean'] / v['rewrites']:.0f}%" if v["rewrites"] else "n/a"
        print(f"{f:8s} {a:8s} runs {v['runs']:3d}  rewrites {v['rewrites']:3d}  clean {v['clean']:3d}  ({rate})")
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
