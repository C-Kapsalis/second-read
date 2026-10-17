---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Kestrel Gateway 5.x; Kestrel CLI 5.2; **Key admin**; `billing-2025`; `billing-2026`; `kestrel keys create --name billing-2026 --expire 30d`; 90 days; `kestrel keys revoke billing-2025`; `X-Kestrel-Key`; Kestrel Vault; Kestrel console; **Keys**; **Active**; https://docs.kestrel.example/reference/cli/keys/; client certificates.
Fabrication traps for this page: do not choose 30 or 90 days; do not invent the button's label; do not add a revoke grace-period flag or any new CLI flag; do not add output for `kestrel keys revoke`.

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
