"""Planted-flaw benchmark for Second Read's docs skill: one case per page in
second-read-docs-benchmark.md (7 flawed pages and 1 clean control). Graded on
flaw recall, blockers first, decoys left alone, the expected verdict, and no
invented facts in the corrected version."""

import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from common import write_case  # noqa: E402

text = (HERE / "second-read-docs-benchmark.md").read_text()
pages = re.split(r"^## Page (\d+): (.+)$", text, flags=re.M)

ASK = {
    "tutorial": "our getting-started tutorial",
    "how-to": "a how-to guide for our docs",
    "reference": "a reference page for our docs",
    "explanation": "an explanation page for our docs",
    "readme": "our README",
    "api": "an API reference page",
    "release": "our release notes",
}


def ask_for(kind: str) -> str:
    k = kind.lower()
    for key, phrase in ASK.items():
        if key in k:
            return phrase
    return "a docs page"


for i in range(1, len(pages), 3):
    num, title, body = int(pages[i]), pages[i + 1].strip(), pages[i + 2]
    doc = re.search(r"````(?:markdown|md)?\n(.*?)\n````", body, re.S).group(1)
    key = body[body.find("### Grading key"):]
    flaws = [
        (m.group(1), m.group(2).strip(), m.group(5).strip())
        for m in re.finditer(r"^\| (\d+\.\d+) \| (.+?) \| (.+?) \| (.+?) \| (Blocker|Major|Minor) \|", key, re.M)
    ]
    decoys = [
        (m.group(1), m.group(2).strip(), m.group(3).strip())
        for m in re.finditer(r"^\| (D\d+\.\d+) \| (.+?) \| (.+?) \|", key, re.M)
    ]
    verdict = re.search(r"Expected verdict:\s*\*\*(.+?)\*\*", key)
    verdict = verdict.group(1) if verdict else None
    facts = re.search(r"Fact list:(.+?)(?:\n\n|\Z)", key, re.S)
    facts = facts.group(1).replace("\n", " ").strip() if facts else ""
    traps = re.search(r"Fabrication traps:(.+?)(?:\n\n|\Z)", key, re.S)
    traps = traps.group(1).replace("\n", " ").strip() if traps else ""
    name = f"sr-docs-{num:02d}"

    prompt = f"""
resources/page.md is {ask_for(title)}. Can you give it a second read before we publish it?
Tell me what to fix first, and if it needs changes, send me a corrected version too, as one fenced code block I can paste (use four backticks around it if the page itself contains code blocks).
"""
    graders = []
    if flaws:
        need = max(1, int(0.8 * len(flaws) + 0.5))  # 80%, rounded to the nearest flaw
        listing = "\n".join(f"- {fid}: {desc}" for fid, desc, _ in flaws)
        graders.append(("flaw-recall", 3, f"""
The page has {len(flaws)} planted problems:
{listing}

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least {need} of the {len(flaws)} problems are found.
FAIL otherwise.
"""))
        blockers = [f"{fid}: {desc}" for fid, desc, sev in flaws if sev == "Blocker"]
        if blockers:
            graders.append(("blockers-first", 2, f"""
These problems block publishing:
{chr(10).join('- ' + b for b in blockers)}

PASS if report.md says the page should not be published as is (do not publish / fix first / not ready) AND each listed problem is among its top-ranked fixes (the first five).
FAIL if it says the page is ready, or any listed problem is missing from the top fixes.
"""))
    if decoys:
        listing = "\n".join(f"- {did}: {quote} ({why})" for did, quote, why in decoys)
        graders.append(("decoys-left-alone", 2, f"""
These parts of the page are correct and must NOT be reported as problems:
{listing}
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
"""))
    if not flaws:
        graders.append(("control-verdict", 3, f"""
This page is a well-built control with no planted problems. Expected verdict: {verdict or 'Ready to publish'}.

PASS if report.md's verdict is positive (ready to publish, or only optional polish) and it raises no blocking or major problem.
FAIL if it says the page should not be published or must be fixed first, or invents a serious problem.
"""))
    graders.append(("no-invented-facts", 2, f"""
Facts present in the original page: {facts or '(see the page)'}
{('Fabrication traps for this page: ' + traps) if traps else ''}

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
"""))
    write_case(name, {"resources/page.md": doc + "\n"}, prompt, graders,
               skill_match=r'"skill"\s*:\s*"second-read:[\w-]+"')
    print(f"{name}: {title}; {len(flaws)} flaws, {sum(s == 'Blocker' for *_, s in flaws)} blockers, {len(decoys)} decoys")
