"""Turn a `claude plugin eval` text log into the benchmark results page.

Usage:
  python3 benchmarks/report.py LOG [--date YYYY-MM-DD] [--out-dir DIR]
                                   [--assets-dir DIR] [--readme PATH]
                                   [--no-readme]

Reads the per-run lines of the log, for example

    sr-email-01 run 2/3 [with]: score 0.75  $0.03
      ✓ flaw-recall (weight 3): judge votes: PASS PASS FAIL

and writes:

  benchmarks/results/<date>.md     per-format and overall tables, with and
                                   without the plugin, with run counts
  assets/benchmark-hero-{light,dark}.svg     with vs without, per metric
  assets/benchmark-formats-{light,dark}.svg  mean score per format

and fills the {{PLACEHOLDER}} values in README.md. A filled value is wrapped
in <!--NAME-->...<!--/NAME--> markers, so running the script again on a new
log updates it in place.

A grader counts as passed for a run when its line starts with ✓ (the
majority of the judge votes). Stdlib only; Python 3.9 or later.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

REPO = Path(__file__).resolve().parents[1]

# (key, label for tables, short label for charts, grader slugs that feed it)
METRICS = [
    ("recall", "Planted flaws found (flaw recall)", "Flaws found",
     ("flaw-recall",)),
    ("gate", "Send- or publish-blocking flaws ranked first", "Blockers ranked first",
     ("gate-flaws-first", "blockers-first")),
    ("decoy", "Correct details (decoys) left alone", "Decoys left alone",
     ("decoys-left-alone",)),
    ("nofab", "Rewrites with no invented facts", "No invented facts",
     ("no-invented-facts",)),
    ("control", "Clean controls called clean", "Clean controls clean",
     ("control-verdict",)),
]
FORMATS = ["email", "social", "landing", "blog", "docs"]
FORMAT_LABEL = {"email": "Email", "social": "Social", "landing": "Landing page",
                "blog": "Blog", "docs": "Docs", "other": "Other"}
ARMS = ("with", "without")

RUN_RE = re.compile(r"^\s+(\S+) run (\d+)/(\d+) \[(with|without)\]: score ([\d.]+)")
GRADER_RE = re.compile(r"^\s+([✓✗]) ([\w-]+) (?:\(weight (\d+)\)|\[[^\]]*\]): (.*)$")
REPORT_RE = re.compile(r"results/(\d{4}-\d{2}-\d{2})T")


def case_format(name: str) -> str:
    m = re.match(r"sr-(email|social|landing|blog|docs)-\d+", name)
    if m:
        return m.group(1)
    if name.startswith("email-score"):
        return "email"
    return "other"


def parse(text: str) -> dict:
    """Return {"runs": [...], "date": str|None}. Each run:
    {"case", "arm", "run", "score", "graders": {slug: bool}, "votes": {slug: str}}"""
    runs, current = [], None
    date = None
    for line in text.splitlines():
        m = RUN_RE.match(line)
        if m:
            current = {"case": m.group(1), "run": int(m.group(2)), "arm": m.group(4),
                       "score": float(m.group(5)), "graders": {}, "votes": {}}
            runs.append(current)
            continue
        g = GRADER_RE.match(line)
        if g and current is not None:
            slug = g.group(2)
            if slug == "skill-fired":
                current["skill_fired"] = g.group(1) == "✓"
            else:
                current["graders"][slug] = g.group(1) == "✓"
                current["votes"][slug] = g.group(4).strip()
            continue
        current = None  # any other line ends the run's grader block
        d = REPORT_RE.search(line)
        if d:
            date = d.group(1)
    return {"runs": runs, "date": date}


def tally(runs: list) -> dict:
    """{(fmt, arm): {"metric": [passed, total], "score": [sum, n], "cases": set}}"""
    out = defaultdict(lambda: {"score": [0.0, 0], "cases": set(),
                               "skill": [0, 0], **{k: [0, 0] for k, *_ in METRICS}})
    for r in runs:
        for fmt in (case_format(r["case"]), "all"):
            t = out[(fmt, r["arm"])]
            t["score"][0] += r["score"]
            t["score"][1] += 1
            t["cases"].add(r["case"])
            if "skill_fired" in r:
                t["skill"][0] += r["skill_fired"]
                t["skill"][1] += 1
            for key, _, _, slugs in METRICS:
                for slug in slugs:
                    if slug in r["graders"]:
                        t[key][0] += r["graders"][slug]
                        t[key][1] += 1
    return out


def rate(pair) -> float | None:
    return pair[0] / pair[1] if pair[1] else None


def pct(pair) -> str:
    r = rate(pair)
    return "n/a" if r is None else f"{round(100 * r)}%"


def cell(pair) -> str:
    return "n/a" if not pair[1] else f"{pct(pair)} ({pair[0]}/{pair[1]})"


def mean(pair) -> str:
    return "n/a" if not pair[1] else f"{pair[0] / pair[1]:.2f}"


def table(t: dict, fmt: str) -> list[str]:
    w, wo = t[(fmt, "with")], t[(fmt, "without")]
    lines = ["| Metric | With Second Read | Without | Difference |", "|---|--:|--:|--:|"]
    for key, label, _, _ in METRICS:
        if not w[key][1] and not wo[key][1]:
            continue
        a, b = rate(w[key]), rate(wo[key])
        diff = "n/a" if a is None or b is None else f"{round(100 * (a - b)):+d} pts"
        lines.append(f"| {label} | {cell(w[key])} | {cell(wo[key])} | {diff} |")
    a, b = w["score"], wo["score"]
    diff = "n/a" if not a[1] or not b[1] else f"{a[0] / a[1] - b[0] / b[1]:+.2f}"
    lines.append(f"| Mean score (0 to 1) | {mean(a)} | {mean(b)} | {diff} |")
    lines.append(f"| Cases / runs | {len(w['cases'])} / {w['score'][1]} | "
                 f"{len(wo['cases'])} / {wo['score'][1]} | |")
    return lines


def results_markdown(t: dict, runs: list, log: Path, date: str, model: str) -> str:
    fmts = [f for f in FORMATS + ["other"] if t[(f, "with")]["score"][1] or t[(f, "without")]["score"][1]]
    cases = sorted({r["case"] for r in runs})
    per_case = defaultdict(lambda: {"with": [], "without": []})
    for r in runs:
        per_case[r["case"]][r["arm"]].append(r["score"])
    sk = t[("all", "with")]["skill"]
    out = [
        f"# Benchmark results, {date}",
        "",
        f"Source log: `{log.name}`. Model under test: {model}. Judge: Claude Haiku "
        "(the `claude plugin eval` default), three votes per grader; a grader passes "
        "on a majority. Generated by `benchmarks/report.py`; method in "
        "[METHOD.md](../METHOD.md).",
        "",
        f"{len(cases)} cases, {len(runs)} runs in all. Each percentage is passed runs "
        "over graded runs for that metric, with the counts in brackets. Small counts "
        "mean wide uncertainty: one run is several points.",
        "",
    ]
    if sk[1]:
        out += [f"The plugin's skill fired in {cell(sk)} of the with-plugin runs.", ""]
    out += ["## Overall", ""] + table(t, "all") + [""]
    for f in fmts:
        out += [f"## {FORMAT_LABEL[f]}", ""] + table(t, f) + [""]
    out += ["## Per case", "", "| Case | With (mean) | Without (mean) | Runs with / without |",
            "|---|--:|--:|--:|"]
    for c in cases:
        a, b = per_case[c]["with"], per_case[c]["without"]
        fa = f"{sum(a) / len(a):.2f}" if a else "n/a"
        fb = f"{sum(b) / len(b):.2f}" if b else "n/a"
        out.append(f"| {c} | {fa} | {fb} | {len(a)} / {len(b)} |")
    return "\n".join(out) + "\n"


# ---------- SVG charts ----------

THEMES = {
    "light": {"bg": "#ffffff", "text": "#1f2328", "muted": "#59636e", "grid": "#d1d9e0",
              "with": "#2a78d6", "without": "#a8a59c"},
    "dark": {"bg": "#0d1117", "text": "#f0f6fc", "muted": "#9198a1", "grid": "#3d444d",
             "with": "#3987e5", "without": "#6b6a64"},
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def bar_chart(rows: list, title: str, desc: str, theme: str, as_pct: bool) -> str:
    """rows: [(label, with_value or None, without_value or None)], values in 0..1."""
    c = THEMES[theme]
    width, left, right = 820, 210, 70
    bar, gap, group_gap = 16, 2, 22
    top = 92
    plot_w = width - left - right
    height = top + len(rows) * (2 * bar + gap + group_gap) + 30
    fmt = (lambda v: f"{round(100 * v)}%") if as_pct else (lambda v: f"{v:.2f}")
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
         f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
         f'<title id="t">{escape(title)}</title>',
         f'<desc id="d">{escape(desc)}</desc>',
         f'<rect width="{width}" height="{height}" fill="{c["bg"]}"/>',
         f'<g font-family="{FONT}">',
         f'<text x="24" y="34" font-size="20" font-weight="600" fill="{c["text"]}">{escape(title)}</text>']
    # legend
    lx = 24
    for arm, label in (("with", "With Second Read"), ("without", "Without")):
        p.append(f'<rect x="{lx}" y="52" width="14" height="14" rx="3" fill="{c[arm]}"/>')
        p.append(f'<text x="{lx + 20}" y="64" font-size="14" fill="{c["muted"]}">{label}</text>')
        lx += 170
    # gridlines at 0, 50, 100%
    base_y = top - 8
    for frac in (0, 0.5, 1):
        x = left + frac * plot_w
        p.append(f'<line x1="{x:.1f}" y1="{base_y}" x2="{x:.1f}" y2="{height - 26}" '
                 f'stroke="{c["grid"]}" stroke-width="1"/>')
        p.append(f'<text x="{x:.1f}" y="{height - 8}" font-size="12" text-anchor="middle" '
                 f'fill="{c["muted"]}">{fmt(frac)}</text>')
    y = top
    for label, a, b in rows:
        p.append(f'<text x="{left - 12}" y="{y + bar + gap / 2 + 5:.1f}" font-size="14" '
                 f'text-anchor="end" fill="{c["text"]}">{escape(label)}</text>')
        for arm, v in (("with", a), ("without", b)):
            if v is None:
                p.append(f'<text x="{left + 6}" y="{y + 12}" font-size="12" fill="{c["muted"]}">n/a</text>')
            else:
                w = max(v * plot_w, 2)
                p.append(f'<rect x="{left}" y="{y}" width="{w:.1f}" height="{bar}" rx="4" fill="{c[arm]}">'
                         f'<title>{escape(label)}, {"with" if arm == "with" else "without"} Second Read: {fmt(v)}</title></rect>')
                p.append(f'<text x="{left + w + 6:.1f}" y="{y + 12.5}" font-size="12" '
                         f'font-weight="{600 if arm == "with" else 400}" fill="{c["text"] if arm == "with" else c["muted"]}">{fmt(v)}</text>')
            y += bar + gap
        y += group_gap
    p += ["</g>", "</svg>"]
    return "\n".join(p) + "\n"


def charts(t: dict, assets: Path, n_cases: int, runs_per_arm: int) -> dict:
    hero_rows = []
    for key, _, short, _ in METRICS:
        a, b = rate(t[("all", "with")][key]), rate(t[("all", "without")][key])
        if a is not None or b is not None:
            hero_rows.append((short, a, b))
    hero_desc = "Pass rate with and without Second Read. " + "; ".join(
        f"{lab}: {'n/a' if a is None else round(100 * a)}% with, "
        f"{'n/a' if b is None else round(100 * b)}% without" for lab, a, b in hero_rows) + "."
    fmt_rows = []
    for f in FORMATS + ["other"]:
        w, wo = t[(f, "with")]["score"], t[(f, "without")]["score"]
        if w[1] or wo[1]:
            fmt_rows.append((FORMAT_LABEL[f], w[0] / w[1] if w[1] else None,
                             wo[0] / wo[1] if wo[1] else None))
    fmt_desc = "Mean grader score (0 to 1) per format, with and without Second Read. " + "; ".join(
        f"{lab}: {'n/a' if a is None else f'{a:.2f}'} with, {'n/a' if b is None else f'{b:.2f}'} without"
        for lab, a, b in fmt_rows) + "."
    sub = f"{n_cases} cases, {runs_per_arm} runs per arm"
    assets.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        (assets / f"benchmark-hero-{theme}.svg").write_text(
            bar_chart(hero_rows, f"With vs without Second Read ({sub})", hero_desc, theme, True))
        (assets / f"benchmark-formats-{theme}.svg").write_text(
            bar_chart(fmt_rows, "Mean score per format (0 to 1)", fmt_desc, theme, False))
    return {"HERO_ALT": hero_desc, "FORMATS_ALT": fmt_desc}


# ---------- README placeholders ----------

def fill_readme(path: Path, values: dict) -> list:
    """Replace {{NAME}} (first run) or <!--NAME-->old<!--/NAME--> (later runs)."""
    text = path.read_text()
    filled = []
    for name, value in values.items():
        wrapped = f"<!--{name}-->{value}<!--/{name}-->"
        token = "{{" + name + "}}"
        n = text.count(token)
        text = text.replace(token, wrapped)
        text, m = re.subn(rf"<!--{name}-->.*?<!--/{name}-->", lambda _: wrapped, text, flags=re.S)
        if n or m:
            filled.append(name)
    path.write_text(text)
    return filled


def check_case_table(text: str, runs: list) -> list:
    """Compare per-case means with the log's own CASE table; return mismatches."""
    ours = defaultdict(lambda: {"with": [], "without": []})
    for r in runs:
        ours[r["case"]][r["arm"]].append(r["score"])
    bad = []
    for m in re.finditer(r"^(\S+)\s+(\d\.\d\d)\s+(\d\.\d\d)\s+[+-]?\d\.\d\d\s+\d+\s+\$", text, re.M):
        case, w, wo = m.group(1), float(m.group(2)), float(m.group(3))
        for arm, logged in (("with", w), ("without", wo)):
            xs = ours[case][arm]
            if xs and abs(sum(xs) / len(xs) - logged) > 0.011:
                bad.append(f"{case} {arm}: log {logged:.2f}, runs {sum(xs) / len(xs):.3f}")
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("log", type=Path)
    ap.add_argument("--date", help="results date (default: from the log's report path, else today)")
    ap.add_argument("--model", default="Claude Haiku", help="model under test, for the results page")
    ap.add_argument("--out-dir", type=Path, default=REPO / "benchmarks" / "results")
    ap.add_argument("--assets-dir", type=Path, default=REPO / "assets")
    ap.add_argument("--readme", type=Path, default=REPO / "README.md")
    ap.add_argument("--no-readme", action="store_true", help="do not touch README.md")
    ap.add_argument("--facts", type=Path, help="check_facts.py JSON: replaces the LLM-judged "
                    "'no invented facts' metric with the deterministic check")
    args = ap.parse_args(argv)

    text = args.log.read_text(encoding="utf-8", errors="replace")
    parsed = parse(text)
    runs = parsed["runs"]
    if not runs:
        print(f"no run lines found in {args.log}", file=sys.stderr)
        return 1
    date = args.date or parsed["date"] or dt.date.today().isoformat()
    model = args.model
    t = tally(runs)
    if args.facts:
        import json
        facts = json.loads(args.facts.read_text())["stats"]
        for key, v in facts.items():
            fmt, arm = key.split("|")
            if (fmt, arm) in t:
                # Rewrites that add no new fact, over runs that produced a fenced rewrite.
                t[(fmt, arm)]["nofab"] = [v["clean"], v["rewrites"]]
    n_cases = len({r["case"] for r in runs})
    per_arm = defaultdict(int)
    for r in runs:
        per_arm[(r["case"], r["arm"])] += 1
    runs_per_arm = max(per_arm.values())

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir / f"{date}.md"
    out.write_text(results_markdown(t, runs, args.log, date, model))
    for b in check_case_table(text, runs):
        print(f"warning: per-case mean differs from the log's CASE table: {b}", file=sys.stderr)
    charts(t, args.assets_dir, n_cases, runs_per_arm)

    w, wo = t[("all", "with")], t[("all", "without")]
    values = {
        "CASE_COUNT": str(n_cases),
        "RUNS": str(runs_per_arm),
        "RUN_TOTAL": str(len(runs)),
        "RESULTS_DATE": date,
        "RESULTS_FILE": f"benchmarks/results/{date}.md",
        "SCORE_WITH": mean(w["score"]),
        "SCORE_WITHOUT": mean(wo["score"]),
            }
    for key, *_ in METRICS:
        values[f"{key.upper()}_WITH"] = pct(w[key])
        values[f"{key.upper()}_WITHOUT"] = pct(wo[key])
        values[f"{key.upper()}_N"] = str(w[key][1])
    for f in FORMATS:
        values[f"{f.upper()}_SCORE_WITH"] = mean(t[(f, "with")]["score"])
        values[f"{f.upper()}_SCORE_WITHOUT"] = mean(t[(f, "without")]["score"])
        values[f"{f.upper()}_CASES"] = str(len(t[(f, "with")]["cases"] | t[(f, "without")]["cases"]))

    print(f"wrote {out}")
    print(f"wrote {args.assets_dir}/benchmark-{{hero,formats}}-{{light,dark}}.svg")
    if not args.no_readme and args.readme.exists():
        filled = fill_readme(args.readme, values)
        left = sorted(set(re.findall(r"\{\{([A-Z_]+)\}\}", args.readme.read_text())))
        print(f"README: filled {len(filled)} placeholders" + (f"; still open: {', '.join(left)}" if left else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
