---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- L4.1: Weekday and date disagree: 10 March 2027 is a Wednesday, not a Thursday
- L4.2: Live stream "starts at 9:00" with no time zone, for an audience across Europe
- L4.3: "Early bird pricing available" with no price or deadline (no ticket price anywhere)
- L4.4: Four CTAs to four goals in the hero (register, sponsor, agenda, Slack)
- L4.5: Unsupported superlative: "Europe's #1 marketing conference"

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the page.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
