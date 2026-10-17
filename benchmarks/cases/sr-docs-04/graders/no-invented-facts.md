---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Tidepool; synchronous; asynchronous; WAL; primary; replica; master; slave; "seconds instead of hours"; "few hundred milliseconds"; `tidepool stop`; `tidepool.conf`; `replication_mode = sync`; `tidepool start`; https://docs.tidepool.example/reference/replication-settings; payments.
Fabrication traps for this page: do not invent the how-to URL; do not expand WAL to anything but write-ahead log (the standard expansion is acceptable; any other is a fabrication); do not add a third replication mode or new settings.

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
