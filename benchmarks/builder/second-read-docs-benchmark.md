# Benchmark: Second Read for docs

Eight documentation pages for fictional products: seven with planted flaws
(tutorial, how-to, reference, explanation, README, API reference, release
notes) and one clean control. Every flaw is objectively checkable: two places
that disagree, a count, a calendar, a missing element, a quoted rule from
the skill's references. Every page has at least one mode mix and one style
breach, and two decoys: correct details a careless reviewer flags.

Products, domains and URLs are invented (`.example` domains). Rule IDs refer
to SKILL.md (A#, M#, S#) and the references (T#, H#, R#, X#, RM#, AP#, RN#).

## How to grade

For each run, record:

| Measure | Pass when |
|---|---|
| Recall | A planted flaw is found: the review quotes it (or names its location exactly) and the fix addresses it. Any listed alternative rule ID is accepted; the rule ID itself is not graded, the finding is |
| Mode mix found | Every planted M-flaw is found and the content is moved out (link plus "Move to another page"), not silently deleted |
| Type | The page is classified as the expected type |
| Decoy false positive | A decoy is listed as a fix, a failed check, or changed in the corrected version as a correction. Mentioning it as passed is fine |
| Verdict | Matches the expected verdict exactly |
| Score | Within +/-10 of the expected score (merging judgment varies) |
| Fabrication | The corrected version contains a command, flag, version, default, value, output, file name, URL or claim that is not in the page's fact list and is not a [placeholder]. One invented item fails the run |
| Conflict handling | Each planted A1 conflict appears as [confirm: X or Y] (or equivalent) in the corrected version, not silently resolved |

Severity scoring used for the expected scores: Blocker -25, Major -10,
Minor -3, from 100.

Extra true findings (not planted, not decoys) are neither rewarded nor
penalized, unless they are fabricated or wrong.

---

## Page 1: Tutorial (Brookline)

### Text

````markdown
# Build your first pipeline with Brookline

In this tutorial, we will build a small pipeline that reads a CSV file of orders and writes a daily summary table. By the end, you will have a pipeline that runs from the command line and reports how many rows it wrote.

## Before you begin

You need:

- Python 3.9 or later
- A terminal
- The sample file `orders.csv` from the [Brookline sample data repository](https://github.com/brookline-example/sample-data) on GitHub

## Step 1: Install Brookline

Create a virtual environment and install Brookline:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install brookline==2.3.0
```

We use a virtual environment so the install does not change your system Python.

## Step 2: Create a project

```bash
brook init orders-demo
cd orders-demo
```

Brookline creates a folder called `orders-demo` with a file named `pipeline.yaml` inside it.

## Step 3: Choose a storage backend

Brookline needs somewhere to write results. You can use either SQLite or PostgreSQL. If you prefer PostgreSQL, install the `brookline[postgres]` extra and set `BROOK_DB_URL` to your connection string. Alternatively, keep the default SQLite file, which needs no setup.

## How Brookline scheduling works

Brookline models every pipeline as a directed acyclic graph (DAG). Each node is a task, and each edge is a dependency. The scheduler performs a topological sort before every run, which guarantees that no task starts before its inputs exist. This design comes from the dataflow systems of the 1970s, where engineers needed to reason about long chains of batch jobs. Because of it, Brookline can run independent branches in parallel, retry failed nodes without rerunning the whole graph, and cache intermediate results between runs.

## Step 4: Add a source and a sink

Copy `orders.csv` into the `orders-demo` folder. Open `pipeline.yaml` and replace its contents with:

```yaml
source:
  type: csv
  path: orders.csv
sink:
  type: table
  name: daily_orders
```

> **Note:** Brookline requires Python 3.11 or later for CSV sources.

## Run Your First Pipeline

Run the pipeline:

```bash
brook run pipeline.yml
```

You will see a line that ends with `rows written: 120`.

## Next steps

You have built a pipeline that loads a CSV file into a table. To learn more, click [here](https://docs.brookline.example/how-to/).
````

### Grading key

Expected type: tutorial. Expected verdict: **Do not publish**, score about
24 (2 Blockers, 2 Majors, 2 Minors).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 1.1 | File name changes | "a file named `pipeline.yaml`" and "Open `pipeline.yaml`" vs "brook run pipeline.yml" | A1, A2 | Blocker | [confirm: pipeline.yaml or pipeline.yml], one name everywhere |
| 1.2 | Python version conflict, stated after install | "Python 3.9 or later" vs "requires Python 3.11 or later for CSV sources" (in step 4, after the install in step 1) | A1, A3 | Blocker | One version in "Before you begin": [confirm: Python 3.9 or 3.11]; remove the late note |
| 1.3 | Mode mix: tutorial offers choices | "You can use either SQLite or PostgreSQL. If you prefer PostgreSQL ... Alternatively, keep the default SQLite file" | M1, T3 | Major | Keep one path (the default SQLite file, which the page says needs no setup); move PostgreSQL to a how-to link |
| 1.4 | Mode mix: theory inside a tutorial | Section "How Brookline scheduling works" (5 sentences of DAG theory and history) | M2, T6 | Major | Replace with one line plus [link to explanation page]; list under "Move to another page" |
| 1.5 | Style: title case heading | "Run Your First Pipeline" | S2 | Minor | "Step 5: Run your first pipeline" or "Run your first pipeline" |
| 1.6 | Style: non-descriptive link text | "click [here](...)" | S9 | Minor | Link text naming the target, for example "see the [Brookline how-to guides]" |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D1.1 | "In this tutorial, we will build a small pipeline" | "We" and future tense are the tutor's voice in a tutorial (decoy list, S1) |
| D1.2 | "We use a virtual environment so the install does not change your system Python." | One sentence of why in a tutorial is allowed (M2 threshold is more than two sentences) |

Fabrication traps: do not add expected output for steps 1-4; do not pick a
Python version; do not invent a how-to URL for PostgreSQL (use a
placeholder); keep `rows written: 120` and `brookline==2.3.0` exactly.

Fact list: Brookline; brook; Python 3.9; Python 3.11; `python3 -m venv
.venv`; `source .venv/bin/activate`; `pip install brookline==2.3.0`; `brook
init orders-demo`; `cd orders-demo`; `orders-demo`; `pipeline.yaml`;
`pipeline.yml`; `orders.csv`; SQLite; PostgreSQL; `brookline[postgres]`;
`BROOK_DB_URL`; the YAML block (csv, orders.csv, table, daily_orders); `brook
run`; `rows written: 120`; https://github.com/brookline-example/sample-data;
https://docs.brookline.example/how-to/; DAG; 1970s.

---

## Page 2: How-to guide (Kestrel Gateway)

### Text

````markdown
# Key Rotation

This guide is for administrators of Kestrel Gateway 5.x who need to replace an API key without downtime.

## What is an API key?

An API key is a secret string that identifies a client application to the gateway. Keys were introduced in the earliest versions of Kestrel as a lighter alternative to client certificates. Unlike passwords, keys are meant for machines rather than people, which is why they are long and random. Every request that reaches the gateway carries a key in the `X-Kestrel-Key` header, and the gateway looks it up before routing the request. Understanding this lookup is the first step to understanding rotation.

## Before you begin

- Kestrel CLI 5.2 or later, logged in with an account that has the **Key admin** role
- The name of the key you are replacing, for example `billing-2025`

## Rotate the key

1. Create the new key. It expires after 90 days:

   ```bash
   kestrel keys create --name billing-2026 --expire 30d
   ```

   The command prints the new key value once. Store it in your secrets manager.

2. Revoke the old key:

   ```bash
   kestrel keys revoke billing-2025
   ```

3. Update each service that calls the gateway so that it sends the new key in the `X-Kestrel-Key` header, then redeploy the services. If your services read the key from Kestrel Vault, skip this step: Vault delivers the new key automatically.

4. In the Kestrel console, open **Keys** and click the blue button on the right to confirm that `billing-2026` shows as **Active**.

For the full list of flags, see the [keys command reference](https://docs.kestrel.example/reference/cli/keys/).

To finish, make sure your organisation's audit policy is followed and that any service accounts are authorised to read the new key.
````

### Grading key

Expected type: how-to guide. Expected verdict: **Do not publish**, score
about 24 (2 Blockers, 2 Majors, 2 Minors; 21 if the title is split into two
Minors).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 2.1 | Expiry conflict | "It expires after 90 days" vs `--expire 30d` | A1 | Blocker | [confirm: 90 days or 30d] in both the text and the flag |
| 2.2 | Steps out of order | Step 2 revokes `billing-2025` before step 3 moves services to the new key: services fail between the two steps (and the revoke has no warning) | A2, A7, H4 | Blocker | Update and redeploy services first, then revoke; warning before the revoke |
| 2.3 | Mode mix: how-to teaches basics | Section "What is an API key?" (5 sentences of definition and history for a competent admin) | M2, H3 | Major | Remove from the guide; one link to [link to explanation or glossary page]; "Move to another page" |
| 2.4 | Title is a feature noun, in title case | "# Key Rotation" | H1, S2 | Minor | "Rotate an API key" or "How to rotate an API key" |
| 2.5 | Position and color-only direction | "click the blue button on the right" | S4, S8 | Major | Name the control: [button label] in bold |
| 2.6 | UK spelling | "organisation's", "authorised" | S3 | Minor | "organization's", "authorized" |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D2.1 | "If your services read the key from Kestrel Vault, skip this step" | Conditional branches belong in how-to guides (decoy list; H5) |
| D2.2 | "For the full list of flags, see the [keys command reference](...)" | A how-to links to reference instead of listing every option; descriptive link text |

Fabrication traps: do not choose 30 or 90 days; do not invent the button's
label; do not add a revoke grace-period flag or any new CLI flag; do not add
output for `kestrel keys revoke`.

Fact list: Kestrel Gateway 5.x; Kestrel CLI 5.2; **Key admin**;
`billing-2025`; `billing-2026`; `kestrel keys create --name billing-2026
--expire 30d`; 90 days; `kestrel keys revoke billing-2025`;
`X-Kestrel-Key`; Kestrel Vault; Kestrel console; **Keys**; **Active**;
https://docs.kestrel.example/reference/cli/keys/; client certificates.

---

## Page 3: Reference (Quillstack configuration)

### Text

````markdown
# Configuration reference: quill.toml

Quillstack reads its settings from `quill.toml` in the working directory at startup. Changes take effect after a restart.

### Server options

| Option | Type | Default | Description |
|---|---|---|---|
| `port` | integer | `8080` | TCP port the server listens on. |
| `workers` | integer | `4` | Number of worker processes. |
| `max_connections` | integer | `100` | Maximum open client connections per worker. |

You must not set `workers` above the number of CPU cores on the host.

We recommend setting `max_connections` to 200, which is the best value for most teams. To change it, first open `quill.toml` in your editor, then find the `[server]` section, then edit the value and save the file.

### Cache options

| Option | Type | Default | Description |
|---|---|---|---|
| `cache_ttl` | integer | `300` | Seconds an entry stays in the cache. |
| `cache_size` | integer | `10000` | Maximum number of entries, i.e. the eviction threshold. |

If `cache_ttl` is not set, entries expire after the default of 600 seconds.

### Example

```toml
[server]
port = 8080
workers = 4
max_connections = 100

[cache]
cache_ttl = 300
cache_size = 10000

[logging]
log_format = "json"
```
````

### Grading key

Expected type: reference. Expected verdict: **Do not publish**, score about
49 (1 Blocker, 2 Majors, 2 Minors).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 3.1 | Mode mix: reference instructs and opines | "We recommend setting `max_connections` to 200, which is the best value for most teams. To change it, first open..." | M3, R1 | Major | Remove; link to [link to how-to page: tune connections]; "Move to another page" |
| 3.2 | Default conflict | Table: `cache_ttl` default `300`; text: "the default of 600 seconds" | A1, R4 | Blocker | [confirm: 300 or 600] in both places |
| 3.3 | Undocumented option | `[logging]` and `log_format = "json"` appear in the example but in no table | R3 | Major | Add a "Logging options" table with [type], [default], [allowed values] placeholders, or remove from the example [confirm] |
| 3.4 | Latin abbreviation | "i.e. the eviction threshold" | S5 | Minor | "that is, the eviction threshold" |
| 3.5 | Skipped heading level | H1 "Configuration reference" followed by H3 "Server options" | S2 | Minor | H2 for the section headings |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D3.1 | "You must not set `workers` above the number of CPU cores on the host." | Warnings belong in reference (decoy list; Diátaxis reference language) |
| D3.2 | `8080`, `10000` without commas | Code values and ports take no commas (S6) |

Fabrication traps: do not invent a type, default or allowed values for
`log_format` (placeholders only); do not keep or relocate "200" as a
recommendation in the reference; do not pick 300 or 600.

Fact list: Quillstack; `quill.toml`; restart; `port` integer `8080`;
`workers` integer `4`; `max_connections` integer `100`; 200; `[server]`;
`cache_ttl` integer `300`; 600 seconds; `cache_size` integer `10000`;
`[cache]`; `[logging]`; `log_format = "json"`; CPU cores.

---

## Page 4: Explanation (Tidepool replication)

### Text

````markdown
# About replication in Tidepool

Tidepool copies every write from one node to others so that a cluster survives the loss of a machine. This page explains why Tidepool offers two replication modes and how to think about the trade-off between them.

## Why replicate at all

A single node is a single point of failure. If its disk fails, every write since the last backup is gone. Replication keeps a live copy on other nodes, so a replica can take over in seconds instead of hours.

## Synchronous and asynchronous replication

Tidepool writes each change to its WAL before it applies the change. In synchronous mode, the master waits until at least one slave confirms it has stored the WAL entry before it tells the client the write succeeded. In asynchronous mode, the primary replies at once and replicas catch up in the background.

Synchronous mode means you can't lose an acknowledged write, but every write is as slow as the slowest network round trip to a replica. Asynchronous mode is fast, but a crash can lose the last few hundred milliseconds of writes.

We think asynchronous replication is the better default for most teams, because most applications can tolerate losing a fraction of a second of data far more easily than they can tolerate slow writes on every request. Teams that store payments or other records they cannot recreate often prefer synchronous mode, and that's a sound choice.

## Enable synchronous mode

1. Stop the primary: `tidepool stop`
2. Edit `tidepool.conf` and set `replication_mode = sync`.
3. Start the primary: `tidepool start`

## Further reading

Read more at https://docs.tidepool.example/reference/replication-settings
````

### Grading key

Expected type: explanation. Expected verdict: **Fix first** (no Blocker),
score about 74 (2 Majors, 2 Minors).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 4.1 | Mode mix: steps in an explanation | Section "Enable synchronous mode" with three numbered commands | M4, X3 | Major | Replace with one line linking to [link to how-to page: enable synchronous replication]; "Move to another page" |
| 4.2 | Non-inclusive terms, inconsistent with the page's own terms | "the master waits until at least one slave confirms" (the page elsewhere says "primary" and "replica") | S4, S12 | Major | "the primary waits until at least one replica confirms" |
| 4.3 | Abbreviation not expanded | "WAL" on first use | S5 | Minor | "write-ahead log (WAL)" |
| 4.4 | Bare URL as link text | "Read more at https://docs.tidepool.example/reference/replication-settings" | S9 | Minor | "See the [replication settings reference](...)" |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D4.1 | "We think asynchronous replication is the better default for most teams, because..." | Opinion with reasons is what explanation is for (decoy list; X5) |
| D4.2 | "you can't lose", "that's a sound choice" | Contractions are fine in explanation (S1) |

Fabrication traps: do not invent the how-to URL; do not expand WAL to
anything but write-ahead log (the standard expansion is acceptable; any
other is a fabrication); do not add a third replication mode or new
settings.

Fact list: Tidepool; synchronous; asynchronous; WAL; primary; replica;
master; slave; "seconds instead of hours"; "few hundred milliseconds";
`tidepool stop`; `tidepool.conf`; `replication_mode = sync`; `tidepool
start`; https://docs.tidepool.example/reference/replication-settings;
payments.

---

## Page 5: README (Ferrule)

### Text

````markdown
# ferrule

![npm version](https://img.shields.io/badge/npm-v1.4.0-blue) ![node](https://img.shields.io/badge/node-%3E%3D18-green)

Ferrule is a command-line linter for YAML files. It checks indentation, duplicate keys, and schema rules, and it is built for teams that keep configuration in Git.

## Requirements

- Node.js 20 or later

## Install

```bash
$ npm install -g ferrule
```

## Quickstart

1. Install Ferrule:

   ```bash
   npm install -g ferrule
   ```

2. Check a file. You can pass a single file, a glob such as `"config/**/*.yaml"`, or a directory. If you prefer to lint only staged files, run `ferrule check --staged` instead, or set up the pre-commit hook described in `docs/hooks.md`. Windows users can also install the standalone binary.

   ```bash
   ferule check config.yaml
   ```

   The command prints:

   ```text
   config.yaml: 0 problems
   ```

## Configuration

TODO: document `.ferrule.yml` options.

## License

MIT. See [LICENSE](LICENSE).
````

### Grading key

Expected type: README (quickstart section is a tutorial). Expected verdict:
**Do not publish**, score about 12 (3 Blockers, 1 Major, 1 Minor).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 5.1 | Node version conflict | Badge "node >=18" vs "Node.js 20 or later" | A1, RM6 | Blocker | [confirm: Node.js 18 or 20] in badge and Requirements |
| 5.2 | Command name typo | `ferule check config.yaml` vs package and command `ferrule` | A1 | Blocker | `ferrule check config.yaml` |
| 5.3 | Mode mix: quickstart offers choices | "You can pass a single file, a glob..., or a directory. If you prefer to lint only staged files... or set up the pre-commit hook... Windows users can also install the standalone binary." | M1, RM3, T3 | Major | One path (check `config.yaml`); move options to [link to usage docs] |
| 5.4 | Unfinished | "TODO: document `.ferrule.yml` options." | A6 | Blocker | Remove the section or [link to configuration reference]; do not invent options |
| 5.5 | Prompt mark breaks copying | "$ npm install -g ferrule" | S7 | Minor | `npm install -g ferrule` |

Note on 5.2: the typo `ferule` is a fix, not a conflict to leave open,
because the package, the install command and the `--staged` example all
say `ferrule`. Either a direct fix or [confirm] passes.

| Decoy | Quote | Why it is correct |
|---|---|---|
| D5.1 | `npm install -g ferrule` in both Install and Quickstart | Some repetition keeps sections self-contained (decoy list) |
| D5.2 | "The command prints:" between command and output | Command and output separated with prose (S7) |

Fabrication traps: do not invent `.ferrule.yml` options; do not add a docs
URL, a contributing file or a Windows binary link (placeholders only); do
not change `config.yaml: 0 problems`.

Fact list: ferrule; Ferrule; npm v1.4.0 badge; node >=18 badge; Node.js 20;
YAML; indentation; duplicate keys; schema rules; Git; `npm install -g
ferrule`; `"config/**/*.yaml"`; `ferrule check --staged`; `docs/hooks.md`;
standalone binary; `ferule check config.yaml`; `config.yaml: 0 problems`;
`.ferrule.yml`; MIT; LICENSE.

---

## Page 6: API reference (Orchard Payments)

### Text

````markdown
# Refunds API

Base URL: `https://api.orchard.example/v1`

All requests require a secret key in the `Authorization: Bearer <secret_key>` header. Replace `<secret_key>` with a key from your dashboard. Rate limit: 100 requests per second per account.

## Create A Refund

`POST /v1/refunds`

Before you call this endpoint, you should first log in to the dashboard, go to **Settings > Payments**, and turn on refunds. Then come back here and try the example below. We recommend starting with a small amount.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `payment_id` | string | Yes | ID of the payment to refund. |
| `amount` | integer | No | Amount to refund, in cents. Defaults to the full payment amount. |
| `idempotency_key` | string | Yes | Unique key for this request. |

You must not retry a failed request with a new `idempotency_key`. Reuse the original key so the refund is not issued twice.

Request:

```json
{
  "payment_id": "pay_8XK21",
  "amount": "25.00",
  "reason": "duplicate",
  "idempotency_key": "rf-2026-0412"
}
```

Response `201 Created`:

```json
{
  "id": "re_55QZ0",
  "payment_id": "pay_8XK21",
  "amount": 2500,
  "status": "pending"
}
```

| Status | Meaning |
|---|---|
| `400` | A parameter is missing or invalid. |
| `404` | No payment matches `payment_id`. |
| `409` | The payment is already fully refunded. |

## Retrieve a refund

`GET /v1/refunds/{id}`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | ID of the refund, in the path. |

Response `200 OK`:

```json
{
  "id": "re_55QZ0",
  "payment_id": "pay_8XK21",
  "amount": 2500,
  "status": "succeeded"
}
```
````

### Grading key

Expected type: reference (API reference). Expected verdict: **Do not
publish**, score about 42 (1 Blocker, 3 Majors, 1 Minor).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 6.1 | Mode mix: tutorial and opinion in reference | "Before you call this endpoint, you should first log in... Then come back here and try the example below. We recommend starting with a small amount." | M3, AP7, R1 | Major | Neutral statement of the requirement ("Refunds must be enabled in **Settings > Payments**.") plus [link to how-to]; drop the recommendation |
| 6.2 | Example type contradicts the table | `"amount": "25.00"` (string, decimal) vs `amount` integer in cents; response shows `2500` | A4, AP4 | Blocker | `"amount": 2500` is supported by the response, or [confirm amount value]; either passes. Not "25.00" |
| 6.3 | Undocumented field | `"reason": "duplicate"` in the request, not in the parameter table | R3, AP3 | Major | Add a `reason` row with [type], [required], [allowed values], or remove [confirm] |
| 6.4 | Inconsistent endpoint shape: no errors for GET | "Retrieve a refund" has no status or error table; "Create a refund" has one | R2, AP2, AP5 | Major | Add a status table with [error codes for this endpoint] |
| 6.5 | Title case heading, inconsistent with the next heading | "Create A Refund" vs "Retrieve a refund" | S2 | Minor | "Create a refund" |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D6.1 | "You must not retry a failed request with a new `idempotency_key`." | A warning in reference (decoy list) |
| D6.2 | `"amount": 2500` without a comma | JSON values take no commas (S6) |

Fabrication traps: do not invent error codes for GET (for example a `404`
copied over is an invention unless marked [confirm]); do not invent allowed
values for `reason`; do not change the base URL or rate limit.

Fact list: Refunds API; `https://api.orchard.example/v1`; `Authorization:
Bearer <secret_key>`; 100 requests per second per account; `POST
/v1/refunds`; **Settings > Payments**; `payment_id` string Yes; `amount`
integer No cents, defaults to full amount; `idempotency_key` string Yes;
`pay_8XK21`; "25.00"; `reason` "duplicate"; `rf-2026-0412`; `201 Created`;
`re_55QZ0`; 2500; pending; 400, 404, 409 and their meanings; `GET
/v1/refunds/{id}`; `id` string Yes; `200 OK`; succeeded.

---

## Page 7: Release notes (Saltmarsh 4.2)

### Text

````markdown
# Saltmarsh 4.2 release notes

Released Tuesday, March 4, 2026.

Saltmarsh 4.2 adds scheduled exports, speeds up large imports, and fixes three bugs.

## New features

- **Scheduled exports.** Exports can now run on a schedule set in `exports.yml`.
- **Faster imports.** Imports over 1 GB run in parallel by default.

### Try scheduled exports

Let's set up your first scheduled export together! First, open `exports.yml` in your editor. Then add a `schedule` block under your export, save the file, and run `saltmarsh exports list` to see it. Scheduled exports work by placing a job on Saltmarsh's internal queue, which the worker polls every 30 seconds. This design lets exports survive restarts, because the queue is stored on disk rather than in memory.

## Deprecations

- The `--legacy-auth` flag is deprecated and will be removed in Saltmarsh 5.0. Use `--token` instead.

## Upgrade notes

- `--legacy-auth` was removed in this release. Update any scripts that use it before upgrading.

## Bug fixes

- Fixed a crash when an import file had an empty header row.
- Fixed exports that skipped the last row of a page.
- Fixed a timeout when listing more than 10,000 projects.
- Fixed wrong time zones in audit log timestamps.

## Known issues

- Scheduled exports do not yet support the `parquet` format. A fix is planned for 15/04/2026.

For the full list of changes, see the [Saltmarsh changelog](https://github.com/saltmarsh-example/saltmarsh/blob/main/CHANGELOG.md) on GitHub.
````

### Grading key

Expected type: release notes (reference record). Expected verdict: **Do
not publish**, score about 12 (3 Blockers, 1 Major, 1 Minor).

| # | Planted flaw | Quote | Rules accepted | Severity | Expected fix |
|---|---|---|---|---|---|
| 7.1 | Weekday does not match date | "Tuesday, March 4, 2026" (March 4, 2026 is a Wednesday) | A1, RN1 | Blocker | [confirm release date] or drop the weekday and keep "March 4, 2026" [confirm]. Do not substitute a new date |
| 7.2 | Count mismatch | "fixes three bugs" vs four items under "Bug fixes" | A1, RN2 | Blocker | Drop the number or [confirm count] |
| 7.3 | Deprecated vs removed | "deprecated and will be removed in Saltmarsh 5.0" vs "`--legacy-auth` was removed in this release" | A1, RN3 | Blocker | [confirm: deprecated in 4.2 or removed in 4.2]; keep "Use `--token` instead" |
| 7.4 | Mode mix: tutorial and explanation inside release notes | Section "Try scheduled exports" ("Let's set up your first scheduled export together!... This design lets exports survive restarts...") | M2, M5, RN6 | Major | One line linking to [link to scheduled exports how-to]; "Move to another page" |
| 7.5 | Numeric date | "15/04/2026" | S6 | Minor | "April 15, 2026" |

| Decoy | Quote | Why it is correct |
|---|---|---|
| D7.1 | "more than 10,000 projects" | Comma in a prose number over 999 is the house rule (S6) |
| D7.2 | "see the [Saltmarsh changelog](...) on GitHub" | Descriptive link text, external source named, upstream repo link (S9) |

Fabrication traps: do not compute or assert the correct weekday as fact
without [confirm] (stating "March 4, 2026 is a Wednesday" in the review is
correct and expected; the corrected version must not pick which of date or
weekday is right); do not invent the `schedule` block syntax; do not
choose 3 or 4 bugs without [confirm] unless the number is simply dropped.

Fact list: Saltmarsh 4.2; Tuesday; March 4, 2026; scheduled exports; large
imports; three bugs; `exports.yml`; 1 GB; `schedule`; `saltmarsh exports
list`; 30 seconds; queue on disk; `--legacy-auth`; Saltmarsh 5.0;
`--token`; the four bug-fix items; 10,000 projects; `parquet`; 15/04/2026;
https://github.com/saltmarsh-example/saltmarsh/blob/main/CHANGELOG.md.

---

## Page 8: Clean control (Windrose how-to)

### Text

````markdown
# Export audit logs from Windrose

This guide shows how to export the audit log for a workspace as a CSV file, for example to hand it to an external auditor.

## Before you begin

- Windrose 3.4 or later
- The **Workspace owner** or **Auditor** role in the workspace you want to export
- For the command-line export: the Windrose CLI 2.1 or later, signed in with `windrose login`

## Export the log

1. In Windrose, go to **Settings > Security > Audit log**.
2. In **Date range**, enter the first and last day you need. The export can cover up to 365 days.
3. Select **Export CSV**.

   Windrose prepares the file in the background. Large exports can take several minutes.

4. When the notification **Export ready** appears, select **Download**.

The file is named `audit-log-<workspace_id>-<date>.csv`, where `<workspace_id>` is your workspace ID and `<date>` is the day you ran the export.

## Export from the command line

If you prefer to script the export, use the Windrose command-line interface (CLI). Replace `<workspace_id>` with your workspace ID:

```bash
windrose audit export --workspace <workspace_id> --from 2026-01-01 --to 2026-03-31 --format csv
```

The command saves the file in the current folder and prints its name, for example:

```text
Saved audit-log-ws_4821-2026-04-02.csv
```

## Check the export

Open the file and confirm that the first row holds the column headers `timestamp`, `actor`, `action`, and `target`, and that the last row falls on or before the end date you chose.

## Related topics

- [Audit log reference](https://docs.windrose.example/reference/audit-log/)
- [How to set an audit log retention period](https://docs.windrose.example/how-to/audit-retention/)
````

### Grading key

Expected type: how-to guide. Expected verdict: **Ready to publish**, score
91-100 (at most two optional notes, no Blocker or Major).

No planted flaws. Passing behavior: verdict "Ready to publish", no
corrected version (changed lines only for optional notes), no fabricated
changes.

| Decoy | Quote | Why it is correct |
|---|---|---|
| D8.1 | "If you prefer to script the export, use the Windrose command-line interface (CLI)." | An alternative path in a how-to is fine; M1 applies to tutorials only |
| D8.2 | "for example to hand it to an external auditor" and the sample output "for example: Saved audit-log-ws_4821-2026-04-02.csv" | Plain English, not "e.g."; an example output labelled as an example |
| D8.3 | "up to 365 days", `2026-01-01` | Digits for 10 and up; ISO dates inside code are values, not prose dates (S6) |

Any Blocker or Major on this page is a false positive. A Minor is tolerated
only if it quotes the page and names a rule it really breaks; the grader
checks the quote.

Fact list: Windrose CLI 2.1; `windrose login`; Windrose 3.4; **Workspace owner**; **Auditor**; **Settings >
Security > Audit log**; **Date range**; 365 days; **Export CSV**; several
minutes; **Export ready**; **Download**;
`audit-log-<workspace_id>-<date>.csv`; `windrose audit export --workspace
<workspace_id> --from 2026-01-01 --to 2026-03-31 --format csv`; `Saved
audit-log-ws_4821-2026-04-02.csv`; `timestamp`, `actor`, `action`,
`target`; the two Related topics URLs.

---

## Coverage of the benchmark

| Page | Mode mix | Accuracy | Structure | Style |
|---|---|---|---|---|
| 1 Tutorial | M1, M2 | A1 x2 (A3) | T3, T6 | S2, S9 |
| 2 How-to | M2 | A1, A2 | H1, H3 | S3, S4 |
| 3 Reference | M3 | A1 | R3 | S2, S5 |
| 4 Explanation | M4 | none (Fix first case) | X3 | S4, S5, S9 |
| 5 README | M1 | A1 x2, A6 | RM3, RM6 | S7 |
| 6 API reference | M3 | A4 | R2, R3, AP2-AP5 | S2 |
| 7 Release notes | M2/M5 | A1 x3 | RN1-RN3, RN6 | S6 |
| 8 Control | none | none | none | none |

Totals: 36 planted flaws, 17 decoys (2 per flawed page, 3 on the control),
verdict spread: 6 Do not publish, 1 Fix first, 1 Ready to publish.
