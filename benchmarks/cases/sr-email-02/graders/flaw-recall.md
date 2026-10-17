---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 4 planted problems:
- 2.1: Raw merge token in the greeting: "Hi {{first_name}},"
- 2.2: Template phrasing: "In today's fast-paced world", "thrilled", "unlock", "seamless", "elevate", "game-changer"
- 2.3: Four CTAs to four different goals (register, ebook, demo, LinkedIn)
- 2.4: "4 PM" with no time zone for a remote webinar

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
