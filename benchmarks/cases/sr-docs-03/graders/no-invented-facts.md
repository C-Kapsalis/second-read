---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Quillstack; `quill.toml`; restart; `port` integer `8080`; `workers` integer `4`; `max_connections` integer `100`; 200; `[server]`; `cache_ttl` integer `300`; 600 seconds; `cache_size` integer `10000`; `[cache]`; `[logging]`; `log_format = "json"`; CPU cores.
Fabrication traps for this page: do not invent a type, default or allowed values for `log_format` (placeholders only); do not keep or relocate "200" as a recommendation in the reference; do not pick 300 or 600.

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
