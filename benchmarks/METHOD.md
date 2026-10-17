# How the benchmark is measured

This page says what I measure, how, and where the numbers can mislead you. If
you find a case where a grader is wrong, or a flaw that is not really a flaw,
please open an issue: that is the most useful feedback this project can get.

## The question

Does a small model review copy and docs better with Second Read loaded than
without it? "Better" means five things a careful colleague does:

1. finds the problems that are really there,
2. ranks the ones that should stop the send or the publish first,
3. leaves correct details alone,
4. rewrites without inventing facts,
5. calls good work good.

## Setup

- **Model under test:** Claude Haiku, in Claude Code, through `claude plugin
  eval`. I chose the small model on purpose: a checklist should help most
  where the model has the least slack.
- **Two arms:** the same prompt and the same files, once with the plugin
  loaded and once without it (`claude plugin eval` ablation, `with-without`).
  Nothing else changes between the arms.
- **The prompt:** every case asks for a review and, if the piece needs
  changes, "a fixed version too, as one fenced code block I can paste" (docs
  cases add: four backticks if the page contains code). Both arms get this
  same request, so both arms are asked for a rewrite in the same shape, and
  the rewrite can be found mechanically.
- **Runs:** 3 per case per arm, so 6 runs per case and 234 runs for the full
  suite.
- **Judge:** Claude Haiku (the `claude plugin eval` default judge) for the
  LLM graders. Each LLM grader asks the judge three times; the grader passes
  on a majority of the three votes. The log keeps every vote.
- **Invented facts:** measured by a script, not the judge. See below.
- **Cases:** 39, in five formats.

| Format | Cases | Flawed | Clean controls | Source |
|---|--:|--:|--:|---|
| Email | 10 | 9 | 1 | [builder/email-benchmark.md](builder/email-benchmark.md) |
| Social post | 7 | 6 | 1 | [builder/second-read-benchmark.md](builder/second-read-benchmark.md) |
| Landing page | 7 | 6 | 1 | same |
| Blog post | 7 | 6 | 1 | same |
| Docs page | 8 | 7 | 1 | [builder/second-read-docs-benchmark.md](builder/second-read-docs-benchmark.md) |

## What a case contains

Each case is one piece of realistic writing from a fictional brand or
product, written for this benchmark:

- **Planted flaws (3-6 per flawed case).** Each one is objectively checkable:
  a count, a calendar, a sum, two places that disagree, a missing element, a
  hard platform limit. Some are marked **gate** (copy) or **Blocker** (docs):
  the piece should not go out until they are fixed.
- **Decoys (1-3 per case).** Correct details that a careless reviewer flags:
  an emoji in a casual post, a real deadline with a reason, "we" in a
  tutorial, a command repeated in two sections.
- **A fact list.** Every fact in the original, so the judge can tell whether
  a rewrite invented one.
- **Clean controls (one per format).** Well-built pieces with no planted
  flaw. They check that the reviewer does not invent problems to look busy.

The answer sheets are the three Markdown files in [builder/](builder/). The
case files in [cases/](cases/) are generated from them.

## Graders

Every case runs the graders that apply to it. Each is judged on the
`report.md` the agent writes.

| Grader | Weight | Passes when |
|---|--:|---|
| `flaw-recall` | 3 | At least 80% of the planted flaws are named with evidence (a quote, count or element). Vague remarks do not count. |
| `gate-flaws-first` (copy), `blockers-first` (docs) | 2 | The verdict says do not send / publish, and every gate or Blocker flaw is among the first five fixes. |
| `decoys-left-alone` | 1 | No decoy is presented as an error or a fix. Asking for a source is fine. |
| `no-invented-facts` | 2 | The rewrite adds no price, count, date, name, link, claim, command, version or output that is not in the fact list. Placeholders and questions are fine. Still in the cases and in each run's score, but not used for the headline metric (see below). |
| `control-verdict` | 3 | (Controls only.) The verdict is positive and no serious problem is invented. |
| `skill-fired` | not scored | With-plugin arm only: the Skill tool was called. It shows the plugin actually loaded. |

A run's score is the weighted share of its graders that passed. The results
page reports each grader as a pass rate over runs (passed runs / graded
runs), per format and overall, with the counts next to every percentage.

## Invented facts: a script, not the judge

The Haiku judge was unreliable on long rewrites, so the headline "rewrites
with no invented facts" comes from [check_facts.py](check_facts.py), which
needs no model:

1. For each kept run it takes the last `report.md` the model wrote and the
   largest fenced code block in it: the rewrite every prompt asks for. A run
   with no fenced block has no rewrite and is not counted (this is why the
   rewrite counts differ between arms).
2. It removes bracketed placeholders (`[expiry date]`, `[confirm: X or Y]`),
   since they are the right way to mark a missing fact, and lengths, scores
   and counts a reviewer writes about the copy (character and word counts,
   `N/100`).
3. It lists every checkable token left: inline code, URLs, email addresses,
   prices, percentages, versions and decimals, ISO dates, and numbers of two
   or more digits. A token that does not appear in the original counts as
   invented, and the rewrite fails.

It cannot see a new claim without a number in it ("my skin feels calmer"),
so it undercounts invention. The LLM grader still runs on every case and
its votes are in the log.

**Audit.** I read every flagged rewrite before using the numbers.

- Rewrite length is not the difference. The median rewrite is about the
  length of the original in both arms: 1.02x with Second Read (99
  rewrites), 1.10x without (79).
- Genuine flags without Second Read: computed savings in a sale email
  (`$51.60`, `$35.60`, `$23.60`, none in the original, sr-email-01, 2 runs);
  "£15 off every month, or £180 over a year" in a gym post (sr-social-04);
  a sender address `hello@embergrind.com` the email never gave
  (sr-email-03).
- Genuine flags with Second Read: an API path shortened from
  `POST /v1/refunds` to `POST /refunds` (sr-docs-06, 1 run; 1 run without
  did the same); a referral link changed from `http://` to `https://`
  (sr-email-09, all 3 runs in both arms). The `https://` version may not
  exist, so it counts.
- Known false positive: a code span split by a placeholder, as in
  ``[confirm: the `[logging]` section and `log_format` ...]``. Removing the
  placeholder leaves stray backticks, and the text between them reads as an
  invented code token. It happened once (sr-docs-03) and counts against
  Second Read.

The JSON for the 2026-10-17 run, with every flagged token and run folder,
is [results/facts-2026-10-17.json](results/facts-2026-10-17.json).

## Reproduce it

You need Claude Code with `claude plugin eval`, and Python 3.9 or later for
the scripts (stdlib only). From the repo root:

```bash
# 1. Optional: rebuild the cases from the answer sheets.
python3 benchmarks/builder/build_all.py

# 2. Run both arms (39 cases x 3 runs x 2 arms) and keep each run's folder.
claude plugin eval . --eval-dir benchmarks/cases --scaffold --allow-tools Write Bash --model haiku -j 6 --runs 3 --trust-plugin --no-publish --keep-temp | tee benchmarks/eval.log

# 3. Check every rewrite for invented facts.
python3 benchmarks/check_facts.py benchmarks/eval.log --json benchmarks/results/facts.json

# 4. Write benchmarks/results/<date>.md, the charts in assets/, and the
#    numbers in README.md.
python3 benchmarks/report.py benchmarks/eval.log --facts benchmarks/results/facts.json
```

`--scaffold` runs each case's `scaffold.sh`, which only writes the fixture
file into the run's workspace; read one before you run it. `--trust-plugin`
skips the trust prompt for this repo. `--keep-temp` keeps each run's folder
(its `out/trace.jsonl` holds the report the model wrote), which
`check_facts.py` needs; the log lists each folder as `kept temp: <path>`.
The judge defaults to Haiku. The log prints the API cost of every run and
the total at the end.

## Limits

I would rather you know these before you quote a number.

- **Synthetic fixtures.** Every piece was written for this benchmark, with
  flaws planted on purpose. Real drafts have messier problems, and some of
  them are not checkable at all (is the offer good?). The benchmark measures
  the checkable part.
- **Three runs per arm.** One run moves a case's pass rate by 33 points.
  The per-format tables pool 21 to 30 runs per arm, from 7 to 10 cases, so
  the per-format n is small; treat a difference of a few points as noise.
- **A Haiku judge for the other graders.** Flaw recall, ranking, decoys and
  controls are judged by a small model. The log shows split votes (PASS PASS
  FAIL), and long reports are harder for it to grade. A majority of three
  reduces this; it does not remove it. I have not yet measured agreement
  with a human grader.
- **Judge votes, not ground truth.** A pass is "the judge said so twice".
  If you think a verdict is wrong, the report is in the run's kept folder.
- **The fact check is narrow.** `check_facts.py` sees numbers, links, code
  and dates, not new claims in words, and it has the one false positive
  described above.
- **Where it did worse or did little.** On blog posts, flaw recall was 94%
  (17/18) with Second Read and 100% (18/18) without: one missed flaw. Docs
  is the weakest format: a mean score of 0.72 with Second Read, and 1 of 3
  docs control runs called clean.
- **One model, one host.** The numbers are for Claude Haiku in Claude Code.
  The adapters for other agents load the same prompt, but I have not
  benchmarked them.
- **The same person wrote the cases and the skill.** A benchmark written by
  the person who wrote the prompt can flatter it, even when the flaws are
  objective. New cases from other people are the best fix; see
  [CONTRIBUTING.md](../CONTRIBUTING.md).
