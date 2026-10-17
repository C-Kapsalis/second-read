---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 4 planted problems:
- L3.1: Placeholder text left in: "[INSERT SHIPPING DETAILS]" and a "Lorem ipsum" story
- L3.2: Two prices for the same mug: $34 in the hero, $39 on the button
- L3.3: Contradictory claim: hot for 24 hours in the hero, up to 12 hours in the specs
- L3.4: Fake urgency: "Today only! Sale ends at midnight" contradicts "Offer valid until 31 December 2026"

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the page.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
