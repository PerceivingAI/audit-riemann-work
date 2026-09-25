# Pass 1 errata recorded during Pass 4

Historical baseline: `20b3f9d8ccbfe469861b85bf77a0053522c6a87a`. These corrections do not amend historical files or validate their mathematical conclusions.

## Historical restoration

| Historical file | Defect or later alteration | Corrective interpretation | Discovery / evidence |
| --- | --- | --- | --- |
| `AUDIT_PLAN.md`, now `archive/AUDIT_PLAN.md` | Pass 3 changed the inventory link after relocation | Original bytes are restored. From the archive, use the living root inventory through `../CLAIMS_TO_AUDIT.md`; do not repair the historical link in place | Alteration identified in Pass 4 by baseline-to-Pass-3 Git blob comparison |
| `evidence/search-records/SRCH-2026-002.md` | Pass 3 replaced the journal abbreviation `Funct. Approx.` with `Funct. A\approx.` | Restore the original abbreviation. This is a restoration of bibliographic text, not independent verification of the cited article | Pass 4 comparison of baseline and `99e2afc5742b1ebae9987eabdda22f9ee844de61` |
| `CLAIMS_TO_AUDIT.md`, `AUDIT_PLAN.md` | Metadata describes 50 candidates | The inventory contains 66 unique candidate IDs across 10 ID families. Historical text remains unchanged; the living inventory is corrected | The discrepancy was already reported in Pass 2; Phase 0 now counts the exact IDs programmatically |

The preservation manifest inventories all historical artifacts, not only the two files with later content changes. Pass 1 reports, dossiers, search records, timelines, interim reports, templates, and marker files are retained at their completion bytes. Living governance versions are stored under `archive/baselines/pass-1/`.

## Reading historical evidence

Historical verdicts and metadata timestamps are not newly verified evidence. Candidate counts, current navigation, and Pass 4 evidence status must be read in the living inventory and coverage matrix. Broken links caused by historical placement remain part of the historical record.

Evidence: [preservation manifest](../evidence/phase0/PRESERVATION_MANIFEST.json), [preservation execution](../evidence/computation-logs/PASS4-PHASE0-PRESERVATION.run.json), and [preserved Pass 1 inventory](baselines/pass-1/CLAIMS_TO_AUDIT.md).
