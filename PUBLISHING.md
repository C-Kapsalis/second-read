# Packaging and publishing

This repository contains source, package builders and marketplace metadata for
distribution. The GitHub release workflow builds archives for each `v*` tag.
Vendor-directory submissions are a separate manual review process; recheck the
vendor's current requirements before submission.

## Build archives

```sh
sh .github/package.sh
```

The ignored `dist/` directory contains:

| Archive | Use |
|---|---|
| `second-read.zip` | Standalone Agent Skill folder for compatible skill upload/install flows. |
| `second-read-plugin.zip` | Claude plugin archive for Customize > Plugins. |
| `second-read-openai.zip` | Portable, skills-only plugin package for ChatGPT/Codex public directory review. |

The archive builder copies the root skill, required references and scripts,
plugin metadata and icon. It excludes repository-only files and generated
Python cache files. The skill's scripts require Python 3; script execution
must be enabled in the host for file export and helper workflows.

## GitHub release

Review the version in `plugin.json` and `.claude-plugin/plugin.json`, update
`RELEASE-NOTES.md`, commit and push, then create and push a matching `vX.Y.Z`
tag. `.github/workflows/release.yml` builds all archives and attaches them to
the GitHub release. Do not commit `dist/`; it is generated from the tag.

## OpenClaw / ClawHub

The repository root is one Agent Skill (`SKILL.md`). In ClawHub's GitHub
importer, import the repository root as a **skill**. `.clawhubignore` keeps
other-host plugin manifests, release documentation and tests out of the
published skill while retaining `references/`, `scripts/` and `assets/` used
by the skill.

Once the listing is public, OpenClaw users can install it with:

```sh
openclaw skills install @c-kapsalis/second-read
```

ClawHub currently requires skills published there to use MIT-0; the GitHub
repository's separate LICENSE remains MIT. If ClawHub reports that a security
check could not complete and says it is waiting for another attempt, do not
re-upload solely to retry that check; use the dashboard diagnostics or contact
ClawHub support if the state persists.

## Marketplaces and directories

Claude Code users can add the GitHub marketplace and install the plugin:

```text
/plugin marketplace add C-Kapsalis/second-read
/plugin install second-read@second-read
```

Agent Skills clients can install from the public repository with
`npx skills add C-Kapsalis/second-read` or download `second-read.zip` from a
GitHub release. The plugin follows the Agent Skills format.

For ChatGPT/Codex's public directory, upload `dist/second-read-openai.zip` in
the vendor portal. The archive is skills-only and has no MCP server or
lifecycle hooks. Complete identity checks, listing fields and policy
attestations in the portal, submit for review, and publish after approval.
Passing package checks does not guarantee approval.

For Claude's public plugin directory, submit the public repository through
Claude's plugin submission portal. The maintainer must answer the data
handling, contact and compliance questions directly in that portal. Read the
current [Claude directory guidance](https://claude.com/resources/articles/build-plugins-for-claude)
before submission.
