---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 4 planted problems:
- 4.1: Preheader repeats the subject word for word
- 4.2: Sender is a bare no-reply address on an unfamiliar domain, replacing the known "Coach Mia at Stridewell"; the body is signed by Mia
- 4.3: The most urgent news and the only registration CTA live inside an image with no alt text
- 4.4: First article paragraph is about 150 words with no break

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
