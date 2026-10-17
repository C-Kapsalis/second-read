# Examples

Before/after examples taken verbatim from benchmark runs: the original
piece, the review the same model wrote without Second Read, and the review
and rewrite it wrote with Second Read. Same case, same model, same prompt.
Each names the case and the run it came from, so you can find the case in
[../benchmarks/cases/](../benchmarks/cases/) and reproduce it with the
commands in [../benchmarks/METHOD.md](../benchmarks/METHOD.md).

| Example | Format | Without | With |
|---|---|--:|--:|
| [sr-social-03](sr-social-03.md): a paid skincare caption | Instagram | 0.38 | 1.00 |

These are synthetic fixtures written for the benchmark, not real drafts. I
picked this one because the baseline's failure is the typical one (two of
four flaws missed, a new claim in the rewrite), not because it is the
widest gap.

To keep a run's workspace (and its `report.md`) for an example, add
`--keep-temp` to the `claude plugin eval` command.
