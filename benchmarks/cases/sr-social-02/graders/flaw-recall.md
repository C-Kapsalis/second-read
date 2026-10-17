---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The post has 5 planted problems:
- 2.1: Weekday and date disagree: 19 November 2026 is a Thursday, not a Wednesday
- 2.2: The news (the benchmark) only starts after about 300 characters, past LinkedIn's "see more" cut of about 210; the opening is throat-clearing
- 2.3: Template phrasing: "ever-evolving landscape", "delve", "thrilled to announce", "game-changer", "unlock"
- 2.4: Unsourced statistic: "Industry research shows 87% of CFOs..." with no source, sample or date
- 2.5: Nine hashtags against LinkedIn's norm of 3-5

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the post.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
