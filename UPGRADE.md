# Second Read — editorial depth upgrade

This is a **single updated skill**, not a new plugin or a SaaS. It is additive to the existing root `SKILL.md` and preserves all existing editing/verification executables and the interactive HTML template.

## Added

- Project-context and supplied author-rules precedence, with traceable source references and a stdlib validator.
- Shared editorial references: semantic precision, reader knowledge, self-rejection of bad edits, and non-diagnostic checks for formulaic prose.
- Distinct pathway references for emails, SEO articles, conversion landing pages, textual ads, journalism, data storytelling, and conditional Canonical documentation style.
- Expanded reference examples distinguishing edit / leave / ask.
- Deterministic regression tests, plus paired editorial cases for **future live-model evaluation**. No live-model or human evaluation is claimed by these fixtures.

## Quick checks

```sh
python3 scripts/project_context.py assets/project-context.example.json
python3 -m unittest discover -s tests -v
python3 scripts/edit_review.py validate assets/review.example.json
```

## Author usage

Supply the author brief and draft following the existing `SKILL.md`. If the text belongs to a company, product or campaign, add relevant **existing** project style/rules and earlier assets, or provide the sample `assets/project-context.example.json` as a shape to fill in. No invented project identity. Content rules are loaded based on the real communication goal, not word count.

## Licensing and source boundary

Canonical documentation style, Oxford University style, Google Search Central, Diátaxis, FTC advertising guidance and data journalism sources are linked for versioned reference. This package contains original editorial procedures and **does not copy external style guides wholesale**. Official guidance can change; respect user-selected house rules and verify current versions when needed.
