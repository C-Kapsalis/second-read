# Second Read installed

Paste a draft, or point at a file, and name the job:

- "Give this email a second read before I send it."
- "Is this LinkedIn post ready to go?"
- "Can you give this README a second read before I publish it?"

You get a verdict (Ready to send, Fix first, Do not send; for docs, Ready to
publish, Fix first, Do not publish), a score, the 3-5 fixes that matter most
with a quote and a rule for each, and a rewrite that uses only the facts you
gave it. Missing facts come back as `[placeholders]`.

Skills, where the host supports them:

- `second-read:second-read`: copy (email, social, landing page, blog)
- `second-read:docs`: documentation (README, tutorial, how-to, reference,
  release notes)

Commands, where the host supports them (Gemini CLI, OpenCode, Copilot CLI):
`/second-read` and `/second-read-docs`.

To check it loaded in Claude Code, start a new session and ask "Is Second
Read active?". The session hook adds its five core rules to every session.

Found a review that was wrong? Please open an issue with the draft (or a
version with private details removed) and what it got wrong:
https://github.com/C-Kapsalis/second-read/issues
