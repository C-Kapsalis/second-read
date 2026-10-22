# Install

Pick your agent below. Not listed? Most agents read [`AGENTS.md`](AGENTS.md):
copy it into your project, or ask your agent to install
[`skills/second-read/SKILL.md`](skills/second-read/SKILL.md) and
[`skills/docs/SKILL.md`](skills/docs/SKILL.md) as skills, and
[`skills/editor/SKILL.md`](skills/editor/SKILL.md) with its `scripts/` if you
want the editor.

Every adapter loads the same prompt. `AGENTS.md` is the source for the
rules-file copies; `python3 scripts/sync-adapters.py` regenerates them.

## What I have tested

I have run the benchmark only in Claude Code. Everywhere else, the file
formats copy those of a working multi-agent plugin
([Ponytail](https://github.com/DietrichGebert/ponytail)), but I have not
installed Second Read there myself. If you try one, please open an issue
with what happened, working or not.

| Agent | Adapter | Status |
|---|---|---|
| Claude Code (CLI, Desktop Code tab) | `.claude-plugin/`, `skills/`, `hooks/` | Tested: `claude plugin validate` and the benchmark |
| Claude (web and Desktop chat) | `dist/second-read-plugin.zip`, skill zips | Zip structure checked locally; upload untested |
| ChatGPT | `adapters/chatgpt/` | Untested |
| Codex | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Untested |
| GitHub Copilot CLI | `.github/plugin/`, `hooks/copilot-hooks.json` | Untested |
| GitHub Copilot Chat (editor) | `.github/copilot-instructions.md` | Untested |
| Gemini CLI | `gemini-extension.json`, `commands/*.toml` | Untested |
| OpenCode | `AGENTS.md`, `.opencode/command/` | Untested |
| Cursor | `.cursor/rules/second-read.mdc` | Untested |
| Windsurf | `.windsurf/rules/second-read.md` | Untested |
| Cline | `.clinerules/second-read.md` | Untested |
| Kiro | `.kiro/steering/second-read.md` | Untested |
| OpenClaw | `.openclaw/skills/second-read/` | Untested |

Menu labels in the Claude and ChatGPT apps change between versions. If a
label below does not match what you see, look for the nearest equivalent.

## Claude Code

As two separate prompts:

```
/plugin marketplace add C-Kapsalis/second-read
```
```
/plugin install second-read@second-read
```

The same two commands work in the Code tab of the Claude Desktop app, which
behaves like Claude Code. A session hook loads Second Read's five core rules
at the start of every session, and the skills load when you share copy or
docs, or ask for edits.

## Claude (web and Desktop chat)

Code execution and file creation must be on (in Settings; Capabilities in
the versions I have seen), or skills will not run. Then pick one of three routes.

**a. Add the marketplace.** In Customize > Plugins, choose Add marketplace,
enter `C-Kapsalis/second-read`, then install `second-read`.

**b. Upload the plugin.** Download `second-read-plugin.zip` from the
[latest release](https://github.com/C-Kapsalis/second-read/releases) (or
build it: `sh scripts/package.sh`) and upload it in Customize > Plugins.

**c. Upload the skills.** Download `second-read-skill.zip`,
`second-read-docs-skill.zip` and, for the editor,
`second-read-editor-skill.zip`, and upload each in Customize > Skills. Each zip
holds one folder with its `SKILL.md` and `references/`.

The session hook does not run in chat. The skill loads when your message
matches its description, so name the job: "Give this email a second read",
"Can you give this README a second read before I publish it?". Anthropic's
help article on custom skills gives a 200-character limit for a skill
description, while the Agent Skills format allows 1,024. The skill zips
therefore carry a short description (under 200 characters) that keeps the
trigger phrases; the plugin keeps the longer one. If an upload is still
rejected, please open an issue.

## ChatGPT

OpenAI is moving ChatGPT from custom GPTs to plugins, and ChatGPT plugins can
carry Agent Skills (the same `SKILL.md` folders). That makes the plugin the
main route; the custom GPT and Project setups below are fallbacks. I have not
tested any of them.

**Plugin or skills (main route).**

1. Build the assets: `sh scripts/package.sh`, or download them from the
   latest release.
2. To add Second Read as skills: in ChatGPT, open Plugins in the sidebar,
   then the Skills tab (earlier versions: Skills > Create), and upload
   `second-read-skill.zip`, `second-read-docs-skill.zip` and
   `second-read-editor-skill.zip`. ChatGPT scans an
   uploaded skill first and may mark it "Needs Review". On Enterprise and
   Edu, an admin has to allow skill uploads.
3. `second-read-chatgpt.zip` is the package for the ChatGPT Plugin Directory
   (a `plugin.json` plus `skills/`, no hooks). Listing it is a separate step;
   see [PUBLISHING.md](PUBLISHING.md).

**Custom GPT (fallback).** OpenAI's help center says personal plans (Free,
Go, Plus, Pro) can no longer create new GPTs and that GPTs are being retired
in favor of plugins, so this only fits a workspace that still allows them.

1. Explore GPTs > Create > Configure.
2. Name: Second Read. Description: "A second read for your copy and your
   docs before you hit send."
3. Instructions: paste
   [`adapters/chatgpt/custom-gpt-instructions.md`](adapters/chatgpt/custom-gpt-instructions.md)
   (about 6,700 characters; the commonly cited 8,000-character limit comes
   from community posts, not from OpenAI's docs).
4. Knowledge: upload the ten files in
   [`adapters/chatgpt/knowledge/`](adapters/chatgpt/knowledge/). OpenAI's
   pages give both 10 and 20 as the file limit; ten fits both.
5. Conversation starters: "Give this email a second read", "Is this landing
   page ready to publish?", "Review this README before I publish it".
6. Visibility: keep it to Only me or Anyone with the link. A public listing
   in the GPT Store is your choice to make; it needs a builder profile.

**Project (fallback, every plan).**

1. Create a project, open its settings, and paste
   [`adapters/chatgpt/project-instructions.md`](adapters/chatgpt/project-instructions.md)
   into the instructions.
2. Add the files from `adapters/chatgpt/knowledge/`. Free plans allow 5
   files per project: add the ones for your formats (for example
   `email.md`, `social.md`, `landing-page.md`, `blog.md`, `style.md`).
3. Start each review in that project.

## Codex

```bash
codex plugin marketplace add C-Kapsalis/second-read
codex plugin add second-read@second-read
```

Run `codex`, open `/hooks`, review and trust the session hook, and start a
new thread. Codex also reads `AGENTS.md` from the project root, so copying it
into a project works without the plugin.

## GitHub Copilot CLI

```bash
copilot plugin marketplace add C-Kapsalis/second-read
copilot plugin install second-read@second-read
```

Commands are namespaced by plugin: `/second-read:second-read` and
`/second-read:second-read-docs`.

## GitHub Copilot Chat (VS Code, JetBrains, Visual Studio)

Copy [`.github/copilot-instructions.md`](.github/copilot-instructions.md) to
the same path in your repository.

## Gemini CLI

```bash
gemini extensions install https://github.com/C-Kapsalis/second-read
```

Loads `AGENTS.md` as always-on context and adds `/second-read` and
`/second-read-docs`. The Claude session hook lives at
`hooks/claude-hooks.json`, not `hooks/hooks.json`, so Gemini does not try to
load it.

## OpenCode

OpenCode reads `AGENTS.md` from the project root: copy it into your project.
For the `/second-read` and `/second-read-docs` commands, copy
[`.opencode/command/`](.opencode/command/) into your project's
`.opencode/command/`.

## Cursor

Copy [`.cursor/rules/second-read.mdc`](.cursor/rules/second-read.mdc) into
your project's `.cursor/rules/`.

## Windsurf

Copy [`.windsurf/rules/second-read.md`](.windsurf/rules/second-read.md) into
your project's `.windsurf/rules/`. Windsurf caps a rule file at 6,000
characters, so this one is a compact version of `AGENTS.md` (about 4,500
characters): the checks, fact ledger, decoy guard, verdicts, rewrite rules
and output format, with pointers to the full skills.

## Cline

Copy [`.clinerules/second-read.md`](.clinerules/second-read.md) into your
project's `.clinerules/`.

## Kiro

Copy [`.kiro/steering/second-read.md`](.kiro/steering/second-read.md) to
`~/.kiro/steering/` (every project) or `.kiro/steering/` in one project.

## OpenClaw

Copy [`.openclaw/skills/second-read`](.openclaw/skills/) into
`~/.openclaw/skills/`. It is not on ClawHub.

## Any other agent

Copy [`AGENTS.md`](AGENTS.md) into the agent's rules or instructions file.
For agents that support Agent Skills, install `skills/second-read/` and
`skills/docs/` as skills.

## Uninstall

| Host | Command |
|---|---|
| Claude Code | `/plugin remove second-read` |
| Claude (web, Desktop) | Customize > Plugins or Customize > Skills, then remove |
| ChatGPT | Remove the skills, the GPT or the project |
| Codex | `codex plugin remove second-read` |
| Copilot CLI | `copilot plugin uninstall second-read` |
| Gemini CLI | `gemini extensions uninstall second-read` |
| Rules files (Cursor, Windsurf, Cline, Kiro, Copilot Chat, OpenCode, OpenClaw) | Delete the copied file |

Second Read writes no state outside its own folder.
