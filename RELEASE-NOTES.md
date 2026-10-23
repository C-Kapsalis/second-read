# Second Read editorial-depth upgrade — 23 October 2026

Scope: **deeper editorial decision references**, project/campaign-aware rules, a context validator, and reproducible regression-case infrastructure. Original skill identity, five core review stages, offline editing UI, edit-operation schema, and product verification script are preserved.

## What changed

- Added project identity and house-rule provenance with validation (`references/PROJECT-CONTEXT.md`, `AUTHOR-RULESETS.md`, `assets/project-context.example.json`, `scripts/project_context.py`).
- Added semantic, reader-sequence, restraint and natural-voice references used across genres.
- Expanded essay, policy, fiction, brand, and Diátaxis documentation references with **edit/leave** counterexamples.
- Added specific pathways for marketing email, SEO blog, landing-page text, ads, journalism, data-journalism visual recommendations and the conditionally applied Canonical guide.
- Added 41 **synthetic** editorial decision cases and a CLI to score model decision agreement and source anchoring; no live model was called and no model-quality score is claimed.
- Added 40 deterministic tests including unapproved execution as `unknown` and source corroboration as insufficient for runtime claims.

## What this release does not do

- Does not include the author's specific email/content marketing rule packs, which have not yet been provided. Their future use is supported without inventing them.
- Does not automatically infer project identity from a brand name, crawl a website without authorization, fetch or verify the latest platform policy, or use an API model autonomously.
- Does not modify any JavaScript/HTML editor interface, change CLI edit operations, create visual media, or convert the skill into a plugin or SaaS.
- Does not prove editorial correctness with 40 deterministic tests; qualitative model/human evaluation is required.

## Install

Upload `skill.zip` through a **Skills** upload interface, not the Claude Plugins upload interface. The archive root is `second-read/` with `SKILL.md` and references; it is one skill.

To use it in a repo, apply `second-read-editorial-depth.patch` to a clean checkout of `C-Kapsalis/second-read` at the baseline version and rebuild the repo's release packages using `sh .github/package.sh`.

### Verify

```sh
python3 -m unittest discover -s tests -q
python3 scripts/project_context.py assets/project-context.example.json
python3 scripts/edit_review.py validate assets/review.example.json
```
