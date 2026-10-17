---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Windrose CLI 2.1; `windrose login`; Windrose 3.4; **Workspace owner**; **Auditor**; **Settings > Security > Audit log**; **Date range**; 365 days; **Export CSV**; several minutes; **Export ready**; **Download**; `audit-log-<workspace_id>-<date>.csv`; `windrose audit export --workspace <workspace_id> --from 2026-01-01 --to 2026-03-31 --format csv`; `Saved audit-log-ws_4821-2026-04-02.csv`; `timestamp`, `actor`, `action`, `target`; the two Related topics URLs.


PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
