# Contributing

Thanks for reading this far. The most useful contributions, in order:

1. **A case where Second Read is wrong.** A real flaw it missed, a correct
   detail it flagged, a fact it invented in a rewrite, a good draft it
   called not ready. Open an issue with the draft (remove anything private),
   what it said, and what it should have said. If you can, include the host
   and model you used.
2. **A new benchmark case.** Add it to the answer sheet in
   `benchmarks/builder/` (`email-benchmark.md`, `second-read-benchmark.md`
   or `second-read-docs-benchmark.md`), following the pattern of the cases
   around it: the piece, its planted flaws (each objectively checkable:
   a count, a calendar, a sum, two places that disagree), one to three
   decoys, and the list of facts. Then rebuild and commit the generated
   files:
   ```bash
   python3 benchmarks/builder/build_all.py
   ```
   Use fictional brands and `.example` domains. Never use a client's or an
   employer's material.
3. **A report from another agent.** Most adapters are untested (see
   [INSTALL.md](INSTALL.md)). If you install one, tell me whether it loaded
   and whether the review followed the format.
4. **A change to a check.** Cite the source for a rule or threshold (a
   platform's own limit, a style guide, a regulation). A check without a
   source is a preference.

## Before you open a pull request

- Edit `AGENTS.md`, not the copies, then run
  `python3 scripts/sync-adapters.py` (CI-style check: `--check`).
- Edit the skills in `skills/`; the ChatGPT knowledge copies and the release
  zips are generated from them (`scripts/sync-adapters.py`,
  `scripts/package.sh`).
- Run `claude plugin validate --strict .claude-plugin/plugin.json` and
  `claude plugin validate --strict skills`.
- If you change a skill, say whether you re-ran the benchmark, on which
  cases, and paste the summary line from `benchmarks/report.py`.
- Plain writing: short sentences, no em-dashes, no hype words.

## Disagreeing

If you think a number in the README is wrong, say so in an issue with the
log or the case. I will try to reproduce it and update the README either way.
