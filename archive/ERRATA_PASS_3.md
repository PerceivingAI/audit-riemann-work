# Pass 3 errata recorded during Pass 4

Freeze baseline: `99e2afc5742b1ebae9987eabdda22f9ee844de61`, the last commit of the Pass 3 execution series before `c2a305a60f8eb1819a685896196dfb880d0325c0` added the Pass 4 plan and moved `THIRD_AUDIT.md` to `archive/THIRD_AUDIT.md`. The preservation manifest records that path mapping and all baseline versions. No Pass 3 report, literature dossier, search log, timeline, or replay log is corrected in place.

## Historical integrity

Pass 3 altered 15 Pass 1/2 artifact contents after their completion versions. Phase 0 restored those original versions. Their Pass 3 versions remain in `archive/baselines/pass-3/` where distinct, and in Git history. The file-specific interpretations are in [Pass 1 errata](ERRATA_PASS_1.md) and [Pass 2 errata](ERRATA_PASS_2.md).

The later plan relocation did not authorize link repairs inside historical reports. Living navigation now points to archived plans explicitly. Historical links remain as originally recorded.

## Candidate mapping and scope findings

Discovery pass for the following Phase 0 semantic findings: Pass 4. Evidence is the exact proposition/rationale pair in the [preserved Pass 3 ledger](baselines/pass-3/AUDIT_LEDGER.md), compared with the [preserved inventory](baselines/pass-3/CLAIMS_TO_AUDIT.md) and pinned source locations recorded in the [mapping dossier](../evidence/phase0/PASS4-CANDIDATE-MAPPING.md).

| Candidate | Defect or limitation | Corrective interpretation |
| --- | --- | --- |
| `CLM-PRIO-001` | Prime-trace zero-mode rationale attached to public-record proposition | Investigate public availability from creation, not prime-trace priority |
| `CLM-PRIO-002` | Shift-filter rationale attached to negative-result history | Investigate the public negative-result and obstruction trail |
| `CLM-PRIO-003` | Stationary-mode rationale attached to correction history | Investigate correction history and the limits of evidence about rewriting |
| `CLM-PRIO-004` | Compressed-translation/fab5933 rationale attached to Legendre-Schur construction | Retain the inventory's construction proposition; establish its own first appearance and public evidence |
| `CLM-PRIO-006` | Rationale stops at T=0.525 while proposition reaches T=0.54 | Include the final theorem and its own chronology |
| `CLM-PRIO-007` | Tail-Gram rationale attached to pole-annihilating shift filter | Investigate the exact filter under this ID |
| `CLM-PRIO-008` | Legendre coercivity rationale attached to pole-subtracted root criterion | Investigate the root criterion under this ID |
| `CLM-PRIO-009` | Hessian rationale attached to nonlinear Mellin chirp | Investigate the chirp under this ID |
| `CLM-PRIO-010` | PNT barrier rationale attached to Hessian/separability | Investigate the Hessian/separability proposition under this ID |
| `CLM-PRIO-012` | Zero-float verifier rationale attached to compressed translations | Investigate prime-entry thresholds and shift norm under this ID |
| `CLM-OBST-001` | Rationale describes loss at larger support; source C-0046 describes failure of the absorbed lower bound already at T=7/20 | Resolve the local/global scope during analytical review; do not silently strengthen the obstruction |
| `CLM-CONT-001` | General-sounding continuation wording exceeds the finite examples located in the source finding | Check the exact quantified scope; do not infer arbitrary-support continuation |
| `CLM-VERF-002` | Floating-token count is not proof of checking every theorem step | Separate exact acceptance from generator and analytical trust |
| `CLM-VERF-007` | Lemma count is not certificate-to-Lean correspondence | Trace definitions, hypotheses, certificate fields, and actual verifier connection |
| `CLM-MATH-001` | Inherited `COMPLETE` coexists with an unverified public push | Keep inherited values visible, but do not promote them to Pass 4 completeness |

There are nine priority subject mismatches, one additional priority scope gap, two software proof-scope gaps, and two analytical scope questions. The remaining aligned rationales are still unverified hypotheses. This is semantic inspection by the coding assistant, not independent human approval or mathematical validation.

Seven inventory dossier references, `claims/priority/CLM-PRIO-006.md` through `CLM-PRIO-012.md`, do not exist at the baseline. No replacement historical dossiers are fabricated. Every ID now has an existing Phase 0 mapping section and an explicit not-run search-status section.

## Taxonomy and policy

The prior four-axis label described five evidentiary dimensions plus a disposition. Living documents now use that terminology. The old policy's default non-novelty verdict and implication that negative search hits establish novelty boundaries are replaced by evidence-led investigation. All inherited classification values remain unchanged in the ledger's hypothesis columns; Phase 0 provenance and unresolved evidence are recorded separately.

## Replay hash domain

All four digests in the Pass 3 replay manifest match the stored logs after CRLF-to-LF byte replacement, and none match the raw Windows working-tree bytes examined in Phase 0. This is a domain distinction, not evidence that the replay failed.

[PASS3_HASH_DOMAINS.json](../evidence/phase0/PASS3_HASH_DOMAINS.json) records both digests for each log. [Hash-domain execution](../evidence/computation-logs/PASS4-PHASE0-HASH-DOMAINS.run.json) records the exact command and output. Original logs and manifest remain unchanged. Mathematical replay and verifier trust analysis belong to Phase 4, not this byte-domain examination.

## Deferred investigations

Comparator histories, official arXiv versions, per-database searches, analytical proofs, formal correspondence, and independent public-availability witnesses remain for Phases 1 through 5. Existing conclusions are neither endorsed nor reversed by documenting these gaps.
