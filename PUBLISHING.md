# Publishing

How Second Read gets into the public plugin directories. Nothing here has
been submitted yet. Each step is something the maintainer does by hand; the
requirements below are what the vendors' docs said on 2026-10-17, and they
change.

## Before any submission

1. The GitHub repo `C-Kapsalis/second-read` is public.
2. Validate the Claude plugin and marketplace:
   ```bash
   claude plugin validate --strict .claude-plugin/plugin.json
   claude plugin validate --strict .claude-plugin/marketplace.json
   claude plugin validate --strict skills
   ```
3. Check the rules copies are current: `python3 scripts/sync-adapters.py --check`.
4. Build the release assets and attach them to a GitHub Release:
   `sh scripts/package.sh` (writes `dist/`).
5. The README numbers come from a real run (`python3 benchmarks/report.py
   <log>`), with no `{{PLACEHOLDER}}` left.

## Claude plugin directory

Source: <https://claude.com/docs/plugins/submit> and
<https://claude.com/docs/directory/publish>. The short link
`clau.de/plugin-directory-submission` redirects there. The GitHub repo
`anthropics/claude-plugins-community` is a read-only mirror of the
directory: pull requests there are not the way in.

Who can submit: anyone on a paid Claude plan (Pro, Max, Team, Enterprise).
On Team and Enterprise, an Owner, or a role with the Directory permission.

Where: claude.ai/directory/manage > Submit new > Plugin bundle. Your GitHub
account must be connected and able to push to the repo. The repo can stay
private during review (with the Claude GitHub App installed and consent to
upload the source), but it must be public before the listing goes live.

What the form asks for:

1. **Source:** repository (URL or `owner/repo`), plugin path (optional; leave
   empty, the plugin is the repo root), branch or tag (optional), then
   Validate.
2. **Listing details:** read-only, taken from `.claude-plugin/plugin.json`
   and `README.md`.
3. **Data handling:** whether the plugin reads or stores personal data,
   sends data to services it does not declare, how long it keeps data, and
   whether it is meant for people under 18. For Second Read: it reads only
   the text you give it, stores nothing, calls no service, and is not aimed
   at minors.
4. **Compliance:** a contact email and four acknowledgements.
5. **Review and submit:** update method (GitHub push webhook, or scheduled
   check only), an auto-publish toggle, then Submit for review.

Review: every version gets automated validation and a security scan; a
person reviews a new listing, and a version can be held for a reviewer. The
limit is 10 submissions per organization per 24 hours.

## ChatGPT Plugin Directory

Source: <https://developers.openai.com/plugins/build/plugins>,
<https://developers.openai.com/plugins/deploy/submission> and
<https://developers.openai.com/plugins/guides/submit-claude-plugin>. OpenAI's
help center (<https://help.openai.com/en/articles/8798878>) describes the
retirement of custom GPTs in favor of plugins.

Second Read is a skills-only plugin: no MCP server, no app. That is the
simpler review path; the MCP materials (server URL, domain verification,
test cases, demo video) do not apply.

Package: `dist/second-read-chatgpt.zip`, built by `scripts/package.sh`:

```
plugin.json                    # adapters/chatgpt/plugin.json
skills/second-read/SKILL.md    # + references/
skills/second-read-docs/SKILL.md
LICENSE
```

`plugin.json` declares the Agent Plugins schema
(`https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`) with `name`,
`version` and `description`. OpenAI's guide for existing Claude plugins says
the portal also accepts a Claude plugin zip and converts it, as long as the
hooks are removed; the dedicated zip avoids that step.

Who can submit: an organization owner, or a member with Apps Management
write access, after identity verification.

Steps:

1. Open the plugin submission portal linked from the submission page above.
2. Upload `second-read-chatgpt.zip`.
3. Fill in the listing (name, description, links: use the GitHub repo for
   the website and support).
4. Submit for review. After approval, you choose when to publish.

Before submitting, read the skills once for any wording that assumes a
specific host. Today they name no vendor or tool.

## Other directories

- **Codex:** the repo already works as a Codex marketplace
  (`.agents/plugins/marketplace.json`); no submission needed for
  `codex plugin marketplace add C-Kapsalis/second-read`.
- **Gemini CLI extensions, ClawHub (OpenClaw), skills.sh:** not submitted.
  Each has its own listing process; check its docs before you publish.
