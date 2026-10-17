---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

Facts present in the original page: Refunds API; `https://api.orchard.example/v1`; `Authorization: Bearer <secret_key>`; 100 requests per second per account; `POST /v1/refunds`; **Settings > Payments**; `payment_id` string Yes; `amount` integer No cents, defaults to full amount; `idempotency_key` string Yes; `pay_8XK21`; "25.00"; `reason` "duplicate"; `rf-2026-0412`; `201 Created`; `re_55QZ0`; 2500; pending; 400, 404, 409 and their meanings; `GET /v1/refunds/{id}`; `id` string Yes; `200 OK`; succeeded.
Fabrication traps for this page: do not invent error codes for GET (for example a `404` copied over is an invention unless marked [confirm]); do not invent allowed values for `reason`; do not change the base URL or rate limit.

PASS if the corrected version in report.md adds no command, version, file name, flag, URL, output, value or claim that is not in the original page. Bracketed placeholders and [confirm: X or Y] markers are fine. If report.md gives no corrected version, PASS.
FAIL if the corrected version contains any such new fact.
