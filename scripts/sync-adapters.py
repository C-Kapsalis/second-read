"""Copy AGENTS.md into every rules-file adapter, with each agent's frontmatter,
and the skills' reference files into adapters/chatgpt/knowledge/.

AGENTS.md is the one source, except for Windsurf, which caps a rule file at
6,000 characters: its file is a compact copy of adapters/windsurf/second-read.md.
Run this after editing either:

  python3 scripts/sync-adapters.py          # write the copies
  python3 scripts/sync-adapters.py --check  # exit 1 if any copy is stale

Stdlib only.
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DESC = ("Second Read: a second read for marketing copy and technical docs "
        "before they go out. Proves every fix with a quote and a rule, "
        "leaves correct details alone, invents no facts.")

ADAPTERS = {
    ".cursor/rules/second-read.mdc":
        f"---\ndescription: {DESC}\nglobs:\nalwaysApply: true\n---\n\n",
    ".clinerules/second-read.md": "",
    ".github/copilot-instructions.md": "",
    ".kiro/steering/second-read.md":
        "---\ntitle: Second Read, read it twice, send it once\ninclusion: always\n---\n\n",
    ".openclaw/skills/second-read/SKILL.md":
        f'---\nname: second-read\ndescription: "{DESC} Use when the user asks for a second read, '
        'or to review, proofread, check or rewrite an email, post, landing page, blog post, '
        'README, tutorial or release notes."\n'
        "homepage: https://github.com/C-Kapsalis/second-read\nlicense: MIT\n---\n\n",
}


# Windsurf rejects rule files over 6,000 characters, so it gets the compact source.
WINDSURF_SRC = REPO / "adapters" / "windsurf" / "second-read.md"
WINDSURF_DST = ".windsurf/rules/second-read.md"
WINDSURF_LIMIT = 6000


# ChatGPT knowledge files (Custom GPT or Project fallback): the copy and docs
# skills' references. The editor skill needs its scripts, so it ships as a skill only.
KNOWLEDGE = REPO / "adapters" / "chatgpt" / "knowledge"
KNOWLEDGE_SKILLS = ("second-read", "docs")


def knowledge_copies():
    for skill in KNOWLEDGE_SKILLS:
        for ref in sorted(REPO.glob(f"skills/{skill}/references/*.md")):
            yield KNOWLEDGE / ref.name, ref.read_text()


def main() -> int:
    body = (REPO / "AGENTS.md").read_text()
    stale = []
    for path, want in knowledge_copies():
        rel = path.relative_to(REPO)
        if "--check" in sys.argv:
            if not path.exists() or path.read_text() != want:
                stale.append(str(rel))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(want)
        print(f"wrote {rel}")
    targets = [(rel, head + body) for rel, head in ADAPTERS.items()]
    compact = WINDSURF_SRC.read_text()
    if len(compact) >= WINDSURF_LIMIT:
        print(f"too long: {WINDSURF_SRC.relative_to(REPO)} is {len(compact)} characters "
              f"(Windsurf limit {WINDSURF_LIMIT})")
        return 1
    targets.append((WINDSURF_DST, compact))
    for rel, want in targets:
        path = REPO / rel
        if "--check" in sys.argv:
            if not path.exists() or path.read_text() != want:
                stale.append(rel)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(want)
        print(f"wrote {rel}")
    for rel in stale:
        print(f"stale: {rel} (run python3 scripts/sync-adapters.py)")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
