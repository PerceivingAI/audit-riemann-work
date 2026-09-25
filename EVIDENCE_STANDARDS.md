# Evidence standards and citation policy

## Primary evidence and provenance

Use exact mathematical texts, versioned papers, source artifacts, reproducible execution records, and authoritative event records for their appropriate purposes. Secondary summaries and comparator self-audits are leads, not sole support for novelty or priority. A Git hash identifies content; even a signed commit does not by itself prove when that content became public.

Every evidence item names its candidate IDs, exact proposition or proposition digest, inspected version, scope, limitations, and verification basis. [AUDIT_PROTOCOL.md](AUDIT_PROTOCOL.md) defines the five axes, evidence strengths, and promotion requirements. Historical evidence is not upgraded merely by linking it from Pass 4.

## Literature dossiers

Record complete citation and BibTeX, DOI, arXiv identifier/version, MR number, zbMATH identifier, stable URL, license, and exact page/section/theorem/proposition/equation wherever available. State unavailable fields without inventing identifiers. Record support, function space, normalization, regime, and the comparison to each affected candidate.

If a file was legally obtained, identify the exact examined bytes with SHA-256. Do not commit proprietary or paywalled PDFs. Redistribute a paper only with an appropriate license or permission; otherwise retain bibliographic and examination evidence without redistributing the file.

Every shortlisted item receives an explained disposition: `EQUIVALENT`, `PARTIAL OVERLAP`, `KNOWN INGREDIENT`, `STRONGER RESULT / DIFFERENT METHOD`, `WEAKER RESULT / SAME METHOD`, `DIFFERENT NORMALIZATION`, `DIFFERENT FUNCTION SPACE`, `DIFFERENT REGIME`, `IRRELEVANT AFTER INSPECTION`, or `UNRESOLVED`.

## Reproducible searches

Record each database independently: execution time, actual accepted query syntax, filters, coverage dates, result count if exposed, approximate-count flag, pagination/retrieval limits, inspected subset, shortlist, and rejection/equivalence reasons. Preserve query URLs, API requests, scripts, or response artifacts. Never aggregate counts from different engines as one search count.

Use multiple semantic query families for strong novelty claims, including mathematical equivalents and citation chains. A zero-hit exact phrase provides only a bounded search observation. Unavailable access, an unavailable count, and zero results are distinct states. `NOT_RUN` is an explicit work status, never an executed search.

## Computational execution record

Retain command as an argument array, working directory, source commit/tree, clean/dirty state before and after, execution-copy identity if needed, OS/architecture, tool/dependency versions, harness-generated start/end timestamps, exact stdout and stderr bytes, and exit code. Source builds, caches, and outputs must not be written into the frozen checkout. Certificates require individual paths and raw SHA-256 identities.

The audit-owned harness is `scripts/pass4_run.py`. It runs from the audit root, sets `PYTHONDONTWRITEBYTECODE=1` and `GIT_OPTIONAL_LOCKS=0`, retains raw streams, and refuses to overwrite an existing run prefix. Its basic tool metadata covers Python and Git; later Rust/Lean/Arb runs must also record those actual toolchain and dependency versions. The harness captures evidence; it is not a filesystem sandbox and does not make a source-mutating command safe.

Example for the audit validator:

```text
python -B scripts/pass4_run.py --output evidence/computation-logs/PASS4-NEW-VALIDATION -- python -B scripts/pass4_validate.py
```

Choose a new descriptive prefix for each run. A nonzero result and its raw evidence are preserved, not replaced by a later successful run.

## Hash domains

- `raw_file_sha256`: SHA-256 over the exact stored bytes, including encoding, BOM, line endings, whitespace, and final newline.
- `normalized_sha256`: SHA-256 after byte replacement of CRLF with LF only. Lone carriage returns, encoding, whitespace, BOM, and final newline are otherwise unchanged.
- `baseline_blob_sha256`: SHA-256 over the bytes returned by `git cat-file blob <object-id>`.
- `git_blob_oid`: Git's object identity, not a SHA-256 content digest. Never relabel it as SHA-256.
- `proposition_sha256`: SHA-256 over the UTF-8 canonical proposition string from the inventory, before Markdown table escaping. No mathematical or whitespace normalization is allowed.

Every manifest declares its domain. Preserve original raw streams even when a normalized digest is also recorded. Recompute digests independently from stored bytes and retain the check result. A manifest does not hash itself; validation-run stream hashes belong to the enclosing run record.

Historical Pass 1/2 restoration targets and archived version snapshots are checked against exact Git blob bytes, including original CRLF where present. Pass 3-only working-tree artifacts retain their pre-execution bytes; the manifest records both their raw working-tree hashes and their baseline Git blob hashes. Their Git-normalized content must match the completion version. Ordinary checkout line-ending conversion is not a new scientific correction, but any raw-byte change must be reported with its domain rather than hidden.

Pass 3 replay hashes are investigated additively in `evidence/phase0/PASS3_HASH_DOMAINS.json`; the original logs and manifest remain frozen. Matching hashes establish byte identity within the domain, not correctness of the execution or theorem.

## Preservation and time

[Preservation manifest](evidence/phase0/PRESERVATION_MANIFEST.json) records each historical path, current path, pass-completion commit, blob identity, stored version, and later alterations. [Pass 1](archive/ERRATA_PASS_1.md), [Pass 2](archive/ERRATA_PASS_2.md), and [Pass 3](archive/ERRATA_PASS_3.md) errata carry corrections without rewriting those artifacts.

Only reconcile timestamps used as evidence. Preserve the exact authoritative value, offset/precision, represented event, and stable identifier. A derived UTC value is an additional field, not a replacement for the source value. Machine run time is not source publication time.
