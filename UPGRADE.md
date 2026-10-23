# Second Read — research-led revision

This release remains one **skill**, not an MCP plugin. It does not change the interactive editor, output volume or editing tools. The root `SKILL.md` is a compact control plane; specialist references load on demand.

## New and refined behavior

- Text-as-code project context: scoped Obsidian/Markdown discovery, available Notion connectors, public-site fallback, then one consequential question if needed. No universal vault format is imposed.
- Read-only `scripts/knowledge_context.py` shortlist; no credentials or vault writes.
- Distinct PR/media relations and independent journalism pathways.
- Canonical's official guide is the **only documentation writing style**, and is not applied outside documentation.
- Corrected SEO/ad/email heuristics; marketing framework scores remain internal optional diagnostics, not user-facing scorecards.
- A compact editorial-judgment layer, separate brand positioning, and anti-formulaic prose checks (no AI-authorship accusation).
- Author-approved edits remain the outcome; chat self-questions remain alongside their exact original passage.

## Verification

Run `python3 -m unittest discover -s tests -q` and `python3 scripts/edit_review.py validate assets/review.example.json`.

Tests prove deterministic behavior and reference structure only. They do not demonstrate that an LLM's proposed revisions are correct or that Notion/Claude integrations are connected. The public repository is not modified automatically by the package.
