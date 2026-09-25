# Riemann conjecture research audit

An independent, multi-pass audit of the mathematical, methodological, verification, and priority claims in [PerceivingAI/riemann-conjecture](https://github.com/PerceivingAI/riemann-conjecture).

## Current status

**Pass 4 Phase 1 technical gates passed: comparator histories and primary-source reconstruction.** Phases 2 through 6 have not been executed. Pass 4 examines whether the audit's classifications have sufficient evidence; earlier reports are records to inspect, not authorities.

- [FOURTH_AUDIT.md](FOURTH_AUDIT.md) is the preserved execution-plan authority. Its originating commit is `c2a305a60f8eb1819a685896196dfb880d0325c0`; the preservation manifest records its exact bytes.
- [AUDIT_PASS_4.md](AUDIT_PASS_4.md) remains the initial plan document, not a completed report. Final Pass 4 report publication is reserved for synthesis.
- [AUDIT_LEDGER.md](AUDIT_LEDGER.md) retains the 66 candidates' Pass 3 classification hypotheses, separately labeled from current verification provenance.
- [EVIDENCE_COVERAGE.md](EVIDENCE_COVERAGE.md) records current evidence and remaining obligations for every candidate.
- [Candidate mapping review](evidence/phase0/PASS4-CANDIDATE-MAPPING.md) records source locations, semantic mapping findings, and missing historical dossier references.
- [Phase 0 report](reports/interim/PASS_4_PHASE_0_REPORT.md) records restorations, mapping findings, exercised validation, and remaining evidence obligations.
- [Phase 1 report](reports/interim/PASS_4_PHASE_1_REPORT.md) records commit-level comparator history, primary arXiv paper reconstruction, and prior-art collision analysis.

No new mathematical, novelty, formal-soundness, or priority verdict is claimed by Phase 0. Located source assertions are not independent verification. The audit must not describe localized positivity or certificate acceptance as a proof of RH.

## Governing records

| Record | Purpose |
| --- | --- |
| [AUDIT_PROTOCOL.md](AUDIT_PROTOCOL.md) | Five evidentiary axes plus one disposition field; provenance and promotion rules |
| [CLAIMS_TO_AUDIT.md](CLAIMS_TO_AUDIT.md) | Exact 66-candidate inventory across 10 ID families |
| [EVIDENCE_STANDARDS.md](EVIDENCE_STANDARDS.md) | Primary-source dossiers, reproducible searches, execution records, and hash domains |
| [TIMELINE_RULES.md](TIMELINE_RULES.md) | Content-specific public event evidence |
| [SOURCE.md](SOURCE.md) | Frozen source identity and read-only execution boundary |
| [Preservation manifest](evidence/phase0/PRESERVATION_MANIFEST.json) | Historical completion commits, blobs, path mappings, and retained versions |

## Historical passes

| Pass | Report | Plan | Additive corrections |
| --- | --- | --- | --- |
| 1 | [FINAL_AUDIT.md](FINAL_AUDIT.md) | [archive/AUDIT_PLAN.md](archive/AUDIT_PLAN.md) | [ERRATA_PASS_1.md](archive/ERRATA_PASS_1.md) |
| 2 | [AUDIT_PASS_2.md](AUDIT_PASS_2.md) | [archive/SECOND_AUDIT.md](archive/SECOND_AUDIT.md) | [ERRATA_PASS_2.md](archive/ERRATA_PASS_2.md) |
| 3 | [reports/AUDIT_PASS_3.md](reports/AUDIT_PASS_3.md) | [archive/THIRD_AUDIT.md](archive/THIRD_AUDIT.md) | [ERRATA_PASS_3.md](archive/ERRATA_PASS_3.md) |

Pass 1/2 artifacts are restored to their own completion versions, including historical errors. Pass 3 artifacts are frozen. Living-document versions and changed later historical versions are preserved under `archive/baselines/`. Do not repair historical links or malformed characters in place; consult the errata.

## Audit-owned tooling

From the audit root, with Python 3.11+ and Git on PATH:

```text
python -B scripts/pass4_validate.py
python -B scripts/pass4_validate.py --self-test
python -B scripts/pass4_validate.py --completion
```

The first command checks Phase 0 accounting, source preservation, historical bytes, active links, and retained hash records. `--self-test` also exercises deliberate missing/duplicate IDs, wrong propositions, broken links/anchors, incorrect rationale subjects, and unsupported promotions. `--completion` is expected to fail while candidate evidence obligations remain unresolved; it is not the Phase 0 gate.

Use `scripts/pass4_run.py` to retain new executions with a unique output prefix. Existing raw stdout, stderr, exit codes, machine timestamps, and hash-domain records are under `evidence/computation-logs/PASS4-*`. The one-time `scripts/pass4_preserve.py --apply` command refuses to overwrite established baseline evidence; do not rerun restoration to update the baseline.

## Repository boundary

`source/riemann-conjecture/` is pinned to `51feb3d176e4a53773c22dc157567cc0486f4c71` and strictly read-only, including ignored files and Git history. All audit evidence and execution outputs belong outside that checkout. No extension beyond T=0.54, p=3 research, source correction, or new source Lean proof is part of Pass 4.
