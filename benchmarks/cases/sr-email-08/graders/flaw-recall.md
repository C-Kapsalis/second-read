---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 4 planted problems:
- 8.1: Preheader is just the brand name (default-style)
- 8.2: Weekday and date disagree: 14 November 2026 is a Saturday
- 8.3: "Our new location" with no address for an in-person event (the footer gives the registered address, not the venue)
- 8.4: Forced account creation plus a 9-question form to RSVP

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
