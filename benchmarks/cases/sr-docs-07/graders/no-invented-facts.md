---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Saltmarsh 4.2; Tuesday; March 4, 2026; scheduled exports; large imports; three bugs; `exports.yml`; 1 GB; `schedule`; `saltmarsh exports list`; 30 seconds; queue on disk; `--legacy-auth`; Saltmarsh 5.0; `--token`; the four bug-fix items; 10,000 projects; `parquet`; 15/04/2026; https://github.com/saltmarsh-example/saltmarsh/blob/main/CHANGELOG.md.
Fabrication traps for this page: do not compute or assert the correct weekday as fact without [confirm] (stating "March 4, 2026 is a Wednesday" in the review is correct and expected; the corrected version must not pick which of date or weekday is right); do not invent the `schedule` block syntax; do not choose 3 or 4 bugs without [confirm] unless the number is simply dropped.

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
