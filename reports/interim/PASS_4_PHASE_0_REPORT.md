# Pass 4 Phase 0: historical integrity and audit tooling

## Status and scope

**Phase 0 technical exit gate: PASS. Pass 4 remains in progress.** Phases 1 through 6 have not been executed. This is an interim phase report, not the Pass 4 synthesis or a consolidated final audit.

The work establishes preservation, governance, candidate mapping, evidence coverage, and executable validation. It does not verify mathematical propositions, external prior art, comparator histories, formal correspondence, or public priority.

Execution-plan authority: [FOURTH_AUDIT.md](../../FOURTH_AUDIT.md), preserved exactly from audit commit `c2a305a60f8eb1819a685896196dfb880d0325c0`. The root `AUDIT_PASS_4.md` remains explicitly a plan document.

## 1. Historical integrity

| Baseline | Full commit |
| --- | --- |
| Pass 1 completion | `20b3f9d8ccbfe469861b85bf77a0053522c6a87a` |
| Pass 2 completion | `66d70cd1d1de4e31cfacc902eddb225ba1b77c79` |
| Pass 3 freeze | `99e2afc5742b1ebae9987eabdda22f9ee844de61` |

The Pass 3 baseline is the last commit of that execution series before the next commit added the Pass 4 plan and relocated the Pass 3 plan. No completion timestamp was invented from document metadata.

- Restored 15 historical artifact contents: two Pass 1 artifacts and thirteen Pass 2 artifacts.
- Examined all 11 intervening audit commits from the Pass 1 completion through the initial Pass 4 plan commit. Sixteen historical paths were touched; the additional path is the unchanged-content relocation of `SECOND_AUDIT.md` to `archive/SECOND_AUDIT.md`.
- Retained 181 baseline path/version records, including six repository-control records; the validator checked 175 stored historical/living-snapshot versions.
- Preserved distinct later versions and living-document baselines under `archive/baselines/`. Earlier mistakes remain in the restored files.
- Added three errata documents rather than correcting historical text in place.
- Added exact-byte Git attributes for restoration targets, archived snapshots, the preserved plan, and new raw evidence artifacts.

[Preservation manifest](../../evidence/phase0/PRESERVATION_MANIFEST.json) records original/current paths, full commits, Git blob IDs, byte hashes, stored paths, and later changes. [Historical change events](../../evidence/phase0/HISTORICAL_CHANGE_EVENTS.json) records the complete intervening change list, including relocation events. The [restoration run](../../evidence/computation-logs/PASS4-PHASE0-PRESERVATION.run.json) retains its exact command, timestamps, streams, and exit status.

Corrections: [Pass 1 errata](../../archive/ERRATA_PASS_1.md), [Pass 2 errata](../../archive/ERRATA_PASS_2.md), [Pass 3 errata](../../archive/ERRATA_PASS_3.md).

## 2. Source preservation

The source checkout is still at commit `51feb3d176e4a53773c22dc157567cc0486f4c71`, tree `8a1dd144a90a4121601ea839d048860bd724b413`.

The initial Git status was clean, but ignored build outputs and caches already existed. They were not removed or regenerated. The validator compared all 3,948 captured file/directory entries, including 3,444 files and their raw SHA-256 identities, together with commit, tree, refs, and Git status. The comparison passed.

[Source baseline](../../evidence/phase0/SOURCE_BEFORE.json) defines this local preservation check. No source code, certificate, derivation, finding, retained computation, or Git ref was changed. No source build or theorem replay was performed.

## 3. Taxonomy and evidence policy

Living documents now use five evidentiary axes plus one disposition field. The old scientific classification values remain unchanged in the ledger's explicitly labeled Pass 3 hypothesis columns. New Phase 0 review fields do not silently reinterpret those values as current verification.

The protocol now distinguishes verification basis, per-axis evidence strength, applicable evidence obligations, source assertions, independent checks, and public event evidence. It no longer begins with a predetermined novelty/non-novelty outcome. Null search results and local commit timestamps cannot close novelty or priority questions.

Updated living documents are the README, protocol, inventory metadata, ledger, evidence standards, timeline rules, and source provenance record. Historical versions are preserved. Current navigation points to the actual archived plan locations.

## 4. Candidate accounting and semantic findings

All 66 unique IDs are represented in the inventory, structured map, ledger, coverage matrix, mapping dossier, and explicit search-status records. Counts are MATH 8, METH 5, OPER 2, CONT 2, OBST 15, LAGU 5, AIRY 7, GRAM 3, VERF 7, and PRIO 12.

[Structured candidate map](../../evidence/phase0/CANDIDATE_MAP.json) binds each canonical proposition, category, historical anchor, source location, inherited classification, reviewed rationale, and evidence reference. Source excerpts are pinned and hashed with a declared UTF-8/LF text domain. Historical commit resolution proves object identity only, not first appearance or public availability.

The [semantic mapping dossier](../../evidence/phase0/PASS4-CANDIDATE-MAPPING.md) records:

- Nine priority subject mismatches: `CLM-PRIO-001..004`, `007..010`, and `012`.
- Three partial-scope rationales: `CLM-PRIO-006`, `CLM-VERF-002`, and `CLM-VERF-007`.
- Two further analytical scope questions: `CLM-OBST-001` and `CLM-CONT-001`.
- Fifty-two subject-aligned but unverified rationales, including the explicit completeness/public-push gap on `CLM-MATH-001`.
- Seven nonexistent inherited dossier references: `claims/priority/CLM-PRIO-006.md` through `CLM-PRIO-012.md`.

No rationale was silently shifted to another ID, no source proposition was rewritten to match a rationale, and no missing historical dossier was invented. Every candidate has an actual Phase 0 mapping section. [Search status](../../evidence/search-records/PASS4-PHASE0-SEARCH-STATUS.md) explicitly says `NOT_RUN`; it is not an external query log.

[EVIDENCE_COVERAGE.md](../../EVIDENCE_COVERAGE.md) records 46 relevant source assertions at validity evidence E1 and 20 candidates at E0 with only related source leads. Every candidate has `NOT_INDEPENDENTLY_VERIFIED` as its current basis. No candidate has been independently verified in Phase 0; comparison and priority dimensions remain E0. All current reviews are unadjudicated, with explicit pending obligations.

Semantic inspection was performed by the coding assistant, not by the parser. No independent human sign-off is claimed. The plan's call for human semantic checking must not be read as evidence that an external human has approved these mappings; that additional review remains distinguishable from the completed technical accounting gate.

## 5. Hash domains and execution evidence

Raw SHA-256 and CRLF-to-LF-normalized SHA-256 are now separate fields with explicit byte domains. Git blob IDs and proposition/source-excerpt digests are separately defined. The harness retains command arguments, working directory, source identity/status, tool/host metadata, machine start/end times, stdout, stderr, exit code, and raw/normalized stream hashes. Later runs also record audit-tool and structured-input hashes.

All four inherited Pass 3 replay hashes match LF-normalized log bytes and differ from the raw Windows working-tree bytes. [Hash-domain examination](../../evidence/phase0/PASS3_HASH_DOMAINS.json) records both values per log; [execution record](../../evidence/computation-logs/PASS4-PHASE0-HASH-DOMAINS.run.json) preserves the check. Original replay logs and their manifest remain unchanged. This check establishes byte-domain identity, not mathematical replay correctness.

## 6. Exercised validation

| Check | Observed result | Evidence |
| --- | --- | --- |
| Restoration command | Exit 0; 15 content restorations recorded | [Preservation run](../../evidence/computation-logs/PASS4-PHASE0-PRESERVATION.run.json) |
| First integrated validation | Exit 1; detected encoding corruption in newly generated mapping data, while historical/source integrity passed | [Initial validation](../../evidence/computation-logs/PASS4-PHASE0-VALIDATION.run.json) |
| Corrected integrated validation with negative cases | Exit 0; 66 candidates, 175 stored versions, no errors, source unchanged | [Corrected validation](../../evidence/computation-logs/PASS4-PHASE0-VALIDATION-CORRECTED.run.json) |
| Premature completion gate | Exit 1 as expected; all 66 candidates rejected for pending evidence obligations | [Completion gate](../../evidence/computation-logs/PASS4-PHASE0-COMPLETION-GATE.run.json) |
| Final publication validation | Exit 0; active report/navigation links, all mappings, historical integrity, prior execution hashes, and source preservation pass | [Publication validation](../../evidence/computation-logs/PASS4-PHASE0-PUBLICATION.run.json) |
| Independent stream-hash recomputation | All 12 streams across six closed runs match both declared hash domains, including the final publication output | [Final hash check](../../evidence/computation-logs/PASS4-PHASE0-FINAL-HASH-CHECK.json) |

The first validation failure was in the audit's one-time data generation, not the research source. Windows-default CP1252 decoding corrupted UTF-8 punctuation and produced inconsistent excerpt digests. Regenerating the affected baseline rationales, disposition text, and excerpt hashes with explicit UTF-8 fixed the cause. The failed output remains preserved; the validator's checks were not weakened to make it pass.

Nine negative cases passed: missing ID, duplicate ID, wrong canonical proposition, missing evidence link, nonexistent file, missing section anchor, wrong rationale subject, unsupported `VERIFIED`, and unsupported `COMPLETE`. The fixtures mutate data in memory and do not alter repository artifacts. Validation cannot itself decide mathematical meaning; it checks the recorded semantic subject/digest bindings and detects inconsistent edits.

## 7. Exit gate and remaining scope

| Phase 0 obligation | Result |
| --- | --- |
| Historical artifacts classified against their own completion versions | PASS |
| Exact Pass 1/2 restoration and separately preserved later versions | PASS |
| Pass 3 freeze and additive errata | PASS |
| Source identity and local byte inventory unchanged | PASS |
| Plan authority and living navigation established | PASS |
| Taxonomy naming corrected without scientific reclassification | PASS |
| All 66 mappings, coverage rows, source references, and explicit gaps accounted for | PASS |
| Executable mapping/preservation/hash gates and negative cases exercised | PASS |

Independent human review is not supplied. No external access is needed to finish the technical Phase 0 work, but later phases may face primary-source or archive-access limitations that must be recorded when encountered.

The next planned work is Phase 1 comparator history and primary-source reconstruction. This report does not start that work or authorize publication of a final Pass 4 report. Candidate-level `COMPLETE` remains blocked until all relevant evidence obligations are met.
