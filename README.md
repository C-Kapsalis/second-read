<p align="center">
  <img src=".claude-plugin/icon.png" width="140" alt="Second Read logo: a reader in glasses with an open book">
</p>

<h1 align="center">Second Read</h1>

<p align="center"><em>Read it twice. Send it once.</em></p>

Second Read is an agent skill for editing a draft before you publish it. Give
your agent the draft and what it is for: who reads it, what it must do, what
you can prove. Second Read reads it the way that reader will, in order, and
hands back the edits it would make, each tied to the exact words it changes.

1. **Reads in the reader's order.** It groups related passages into labeled
   threads (claim, evidence, example, counterargument) so you can see how the
   argument travels.
2. **Proposes the smallest edit that fixes a real problem:** replace, insert,
   move or delete, each anchored to a verbatim quote and marked required (a
   checkable error) or optional (style or flow).
3. **Asks where a reader could go another way.** At most three questions,
   placed right after the passage where a first-time reader might take
   something other than what you meant. No quiz at the end, no score for you.
4. **Assembles the version you approve** and proofreads the new order again.
   It keeps your voice and invents no facts. A clean draft gets zero changes.

## How to ask

Paste your brief and the draft in this shape. Second Read asks for any part
you leave out, because the review is measured against what you meant, not
against what the draft happens to say:

```
My actual intention: Argue that the city should run a six-month pilot to
make late-night buses reliable before deciding anything about fares.
Audience: Residents who know little about transport policy.
Voice: Direct, thoughtful, memorable. Not academic or promotional.
Constraints: Keep my strongest sentences. Invent no statistics or policies.
Draft:
...
```

It picks its checks from what the draft does, not from its length: essays and
explanations, policy arguments, fiction and narrative, copy and branding, and
documentation after [Diátaxis](https://diataxis.fr).

## Install

### Claude Code

```
/plugin marketplace add C-Kapsalis/second-read
```
```
/plugin install second-read@second-read
```

Then share a draft: "Give this a second read before I publish it."

### Claude (web and Desktop) and ChatGPT

Download `second-read.zip` from the
[latest release](https://github.com/C-Kapsalis/second-read/releases/latest)
and upload it as a skill (Claude: Customize > Skills; ChatGPT: the Skills
tab). In Claude you can instead upload `second-read-plugin.zip` under
Customize > Plugins. Code execution must be on for the scripts.

### OpenCode, OpenClaw, Codex, Gemini CLI, Cursor, Copilot, Goose, Cline, Windsurf and other agents

Second Read follows the open [Agent Skills](https://agentskills.io) format,
so one command installs it into the agents you choose (needs Node.js):

```
npx skills add C-Kapsalis/second-read
```

Add `-g` to install it for your user instead of the current project, or
`-a opencode` (or another agent's name) to pick the agent.

To install by hand, download `second-read.zip` from the
[latest release](https://github.com/C-Kapsalis/second-read/releases/latest)
and unzip it so the `second-read/` folder sits in your agent's skills
folder:

| Agent | Project folder | Your user's folder |
|---|---|---|
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` |
| OpenClaw | `skills/` | `~/.openclaw/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` | `~/.gemini/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` |
| Goose | `.goose/skills/` | `~/.config/goose/skills/` |
| Cline | `.cline/skills/` | `~/.cline/skills/` |
| Kiro | `.kiro/skills/` | `~/.kiro/skills/` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |

Paths are from each agent's documentation on 2026-10-22; check yours if the
skill does not load. I have checked the Claude Code plugin locally; the other
installs are untested, so please open an issue with what happened.

## The scripts (optional)

The skill works in plain chat. Two scripts, Python standard library only,
add a reproducible trail:

```sh
python3 scripts/edit_review.py validate review.json
python3 scripts/edit_review.py render review.json --output second-read.html
python3 scripts/edit_review.py apply review.json --accept e1 e3 --output revised.md
```

`edit_review.py` checks that every proposed edit quotes your draft verbatim,
renders a private offline page where you accept or reject each change, and
applies the accepted set. [`assets/review.example.json`](assets/review.example.json)
shows the format.

```sh
python3 scripts/product_verify.py --root ./your-product --manifest claims.json --document README.md
```

`product_verify.py` checks product claims in a document against a checkout
and reports each as `corroborated`, `contradicted` or `unknown`. It runs
commands only with `--allow-exec` and makes network requests only with
`--allow-network`; read
[`references/PRODUCT-VERIFICATION.md`](references/PRODUCT-VERIFICATION.md)
first.

## License

MIT. Personal project of Christoforos Kapsalis.
