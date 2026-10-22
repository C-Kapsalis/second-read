# Changelog

## 0.2.0 (2026-10-22)

- **Editor skill** (`skills/editor/`, shipped as `second-read-editor`). Reads a
  draft in the reader's order, proposes source-anchored edits (replace,
  insert after, move after, delete), places at most three "questions to
  yourself" where a cold reading diverges from the brief, and assembles the
  draft the author approves, then proofreads it again. References for
  essays, policy arguments, fiction, copy and branding, and docs.
- `skills/editor/scripts/edit_review.py`: validate a `review.json`, render an
  offline editing page, apply the accepted edits.
- `skills/editor/scripts/product_verify.py`: check product claims against a
  checkout; commands and HTTP checks run only with `--allow-exec` or
  `--allow-network`.
- New command: `second-read-edit` (Gemini CLI, Copilot CLI, OpenCode).
- New release asset: `second-read-editor-skill.zip`; the ChatGPT zip carries
  the editor too. The ChatGPT knowledge files stay the copy and docs
  references (ten files).
- Logo: `.claude-plugin/icon.png` (the plugin directory listing icon) and
  `assets/logo.png` (README).
- The editor is not benchmarked yet. The README numbers are for the review
  skills and are unchanged.

## 0.1.0 (2026-10-17)

- First release: copy review (`second-read`) and docs review (`docs`), the
  39-case Claude Haiku benchmark and the adapters for other agents.
