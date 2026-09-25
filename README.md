# Riemann Conjecture Research Audit

An independent, evidentiary, and multi-pass adversarial audit of the mathematical, methodological, verification, and priority claims in [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

> **Audit Governance & Navigation Metadata**  
> * **Audit Status**: **`AUDIT_PASS_4_COMPLETE`** (Comprehensive Evidence-Depth & Multi-Axis Synthesis Completed)  
> * **Current Master Execution Plan**: [`archive/FOURTH_AUDIT.md`](archive/FOURTH_AUDIT.md)  
> * **Current Comprehensive Report**: [`AUDIT_PASS_4.md`](AUDIT_PASS_4.md) (Master copy in [`reports/AUDIT_PASS_4.md`](reports/AUDIT_PASS_4.md))  
> * **Authoritative 5-Axis Ledger**: [`AUDIT_LEDGER.md`](AUDIT_LEDGER.md) (66 Candidate Claims)  
> * **Master Evidence Coverage Matrix**: [`EVIDENCE_COVERAGE.md`](EVIDENCE_COVERAGE.md) (66/66 Claims Tracked)  
> * **Target Pinned Research Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Preserved Historical Passes**:  
>   * Pass 1 Master Report: [`reports/FINAL_AUDIT.md`](reports/FINAL_AUDIT.md) | Plan: [`archive/AUDIT_PLAN.md`](archive/AUDIT_PLAN.md) | Errata: [`archive/ERRATA_PASS_1.md`](archive/ERRATA_PASS_1.md)  
>   * Pass 2 Master Report: [`reports/AUDIT_PASS_2.md`](reports/AUDIT_PASS_2.md) | Plan: [`archive/SECOND_AUDIT.md`](archive/SECOND_AUDIT.md) | Errata: [`archive/ERRATA_PASS_2.md`](archive/ERRATA_PASS_2.md)  
>   * Pass 3 Master Report: [`reports/AUDIT_PASS_3.md`](reports/AUDIT_PASS_3.md) | Plan: [`archive/THIRD_AUDIT.md`](archive/THIRD_AUDIT.md) | Errata: [`archive/ERRATA_PASS_3.md`](archive/ERRATA_PASS_3.md)

---

## 1. Objective & Scope

This repository provides an evidentiary record investigating the novelty, rigor, reproducibility, and priority of results produced by the `riemann-conjecture` project.

The audit evaluates candidate hypotheses against established mathematical literature, historical records, and contemporary preprints under an adversarial, skeptical standard.

### Core Audit Principles

1. **Strict Read-Only Stance**: The source repository snapshot under `source/riemann-conjecture/` is strictly read-only. No changes or pull requests are made upstream. All findings and artifacts reside entirely within this audit repository.
2. **Adversarial & Skeptical Default**: Claims are treated as unverified hypotheses until exhaustive literature searches, machine-checked replay, and mathematical normalization demonstrate otherwise.
3. **Five-Dimensional Decoupled Evaluation**: Mathematical validity, result comparison, method comparison, software/verification comparison, and chronological priority are assessed independently, producing a final evidence disposition.
4. **Historical Pass Preservation**: Historical audit artifacts from Pass 1, Pass 2, and Pass 3 are immutably preserved; all subsequent passes build additive, transparent corrections through versioned errata files.
5. **Non-Closure Standard**: Where third-party external evidence is unverified (such as public push timestamps), claims are designated `INCONCLUSIVE` rather than forced into premature closure.
6. **Strict Non-Overclaim Boundary**: The project establishes certified localized Weil positivity theorems on compact support ($T \in [0.35, 0.54]$) and prime-side criteria; it does **not** prove the Riemann Hypothesis.

---

## 2. Directory Structure

```text
riemann-conjecture-audit/
├── README.md                           # Living public overview, governance, and navigation
├── FOURTH_AUDIT.md                     # Active Master Audit Plan (Pass 4)
├── AUDIT_LEDGER.md                     # Authoritative 5-axis 66-claim master ledger
├── EVIDENCE_COVERAGE.md                # Full 66-claim evidence completeness & strength matrix
├── AUDIT_PASS_4.md                     # Master Comprehensive Audit Report (Pass 4, root copy)
├── AUDIT_PASS_3.md                     # Preserved Pass 3 Master Report (Historical)
├── AUDIT_PASS_2.md                     # Preserved Pass 2 Master Report (Historical)
├── FINAL_AUDIT.md                      # Preserved Pass 1 Master Report (Historical)
├── AUDIT_PROTOCOL.md                   # Governing Methodological Protocol (v3.0.0)
├── SOURCE.md                           # Source repo provenance and commit mapping
├── CLAIMS_TO_AUDIT.md                  # Complete inventory of 66 candidate claims
├── EVIDENCE_STANDARDS.md               # Citation rules, hit logging, and reproducibility policy
├── TIMELINE_RULES.md                   # Multi-anchor priority & timestamp evaluation framework
├── archive/
│   ├── AUDIT_PLAN.md                   # Preserved Pass 1 Execution Plan
│   ├── SECOND_AUDIT.md                 # Preserved Pass 2 Execution Plan
│   ├── THIRD_AUDIT.md                  # Preserved Pass 3 Execution Plan
│   ├── ERRATA_PASS_1.md                # Pass 1 Additive Errata & Restoration Log
│   ├── ERRATA_PASS_2.md                # Pass 2 Additive Errata & Restoration Log
│   ├── ERRATA_PASS_3.md                # Pass 3 Additive Errata & Replay Domain Log
│   └── baselines/                      # Immutably preserved historical version snapshots
├── source/
│   └── riemann-conjecture/             # Frozen research snapshot pinned to commit 51feb3d
├── evidence/
│   ├── computation-logs/               # Preserved raw machine execution logs & SHA-256 manifests
│   │   ├── PASS4-REPLAY-MANIFEST.json  # Manifest of Pass 4 independent replays & certificate hashes
│   │   ├── PASS4-REPLAY-RUST-CERT.stdout.log
│   │   ├── PASS4-REPLAY-RUST-ENGINE.stdout.log
│   │   ├── PASS4-REPLAY-CERT-8OF8.stdout.log
│   │   └── PASS4-REPLAY-PYTEST-IDENTITIES.stdout.log
│   ├── literature/                     # Primary literature and comparator dossiers
│   │   ├── PASS_4_PRIOR_ART.md         # Master comparative prior art dossier (Pass 4 synthesis)
│   │   ├── PASS4-KUBER-COMMIT-HISTORY.md # Kuber Mehta commit-by-commit Git history audit
│   │   ├── PASS4-CHUK-PRIMARY-SOURCE.md  # Marcus Chuk / Xuefeng Zhu arXiv:2608.24827 analysis
│   │   ├── LIT-1964-TUCK-LEGENDRE.md   # E. O. Tuck (1964) Legendre eigenvalue identity
│   │   ├── LIT-1992-YOSHIDA-HERMITIAN.md # H. Yoshida (1992) prime-free compact positivity
│   │   ├── LIT-2000-BOMBIERI-WEIL.md   # E. Bombieri (2000) variational & radical theory
│   │   ├── LIT-2020-CC-ARCHIMEDEAN.md  # A. Connes & C. Consani (2020/2021) Sonin trace
│   │   ├── LIT-2025-CCM-SPECTRAL.md    # A. Connes, C. Consani, H. Moscovici (2025) triples
│   │   ├── LIT-2026-SUZUKI-SCREW.md    # M. Suzuki (2026) screw function & residual kernel
│   │   ├── LIT-2026-GROSKIN-FINITE.md  # A. Groskin (2026) truncated Weil form bounds
│   │   └── LIT-2007-LAGARIAS-LICAE.md  # J. C. Lagarias (2007) prime-Laguerre expansion
│   ├── phase0/                         # Preservation manifests, source baselines, and candidate map
│   │   ├── CANDIDATE_MAP.json          # Canonical structured 66-candidate mapping records
│   │   ├── PASS4-CANDIDATE-MAPPING.md  # Semantic mapping and source reference review
│   │   ├── PRESERVATION_MANIFEST.json  # Byte-level historical preservation manifest
│   │   └── SOURCE_BEFORE.json          # Captured baseline snapshot of source checkout
│   ├── phase1/                         # Comparator mirrors, manifests, and primary paper HTML/tar
│   ├── phase2/                         # Multi-family API search responses (Crossref, GitHub, arXiv)
│   ├── phase5/                         # Public archive query responses (GH Archive, Software Heritage, Wayback)
│   ├── public-timeline/                # Multi-anchor priority timelines
│   │   └── PASS_4_TIMELINE.md          # Source-by-source multi-anchor priority timeline
│   ├── search-records/                 # Database-by-database query logs with hit counts & dispositions
│   │   ├── PASS4-SRCH-001-WEIL-THEOREMS-AND-CONTINUATION.md
│   │   ├── PASS4-SRCH-002-LEGENDRE-SCHUR-OPERATORS.md
│   │   ├── PASS4-SRCH-003-LI-LAGUERRE-SCHOENBERG.md
│   │   ├── PASS4-SRCH-004-AIRY-CHIRP-ASYMPTOTICS.md
│   │   ├── PASS4-SRCH-005-ANALYTICAL-OBSTRUCTIONS.md
│   │   └── PASS4-SRCH-006-VERIFICATION-AND-FORMAL.md
│   └── validity/                       # Mathematical derivations, checks, and trust boundary dossiers
│       ├── PASS4-MATH-001-008-THEOREMS.md
│       ├── PASS4-METH-OPER-CONT-VALIDITY.md
│       ├── PASS4-LAGU-GRAM-VALIDITY.md
│       ├── PASS4-AIRY-001-007-ASYMPTOTICS.md
│       ├── PASS4-OBST-A-ENDPOINT-COERCIVITY.md
│       ├── PASS4-OBST-B-PNT-MOVING-SCALE.md
│       ├── PASS4-OBST-C-BLOCK-NORMS-FREQUENCY-CAP.md
│       ├── PASS4-OBST-D-BILINEAR-HESSIAN-VAUGHAN.md
│       ├── PASS4-VERF-TRUST-CHAIN.md
│       └── PASS4-VERF-001-007-ARCHITECTURE.md
├── reports/
│   ├── AUDIT_PASS_4.md                 # Master Comprehensive Pass 4 Audit Report
│   ├── AUDIT_PASS_3.md                 # Preserved Pass 3 Master Report
│   ├── AUDIT_PASS_2.md                 # Preserved Pass 2 Master Report
│   ├── FINAL_AUDIT.md                  # Preserved Pass 1 Master Report
│   └── interim/                        # Phased Pass 4 interim reports (Phases 0 through 5)
│       ├── PASS_4_PHASE_0_REPORT.md    # Historical Integrity & Tooling (Phase 0)
│       ├── PASS_4_PHASE_1_REPORT.md    # Comparator Histories & Primary Sources (Phase 1)
│       ├── PASS_4_PHASE_2_REPORT.md    # Claim-Specific Search Re-Execution (Phase 2)
│       ├── PASS_4_PHASE_3_REPORT.md    # Independent Mathematical Validity Audit (Phase 3)
│       ├── PASS_4_PHASE_4_REPORT.md    # Verification-Chain & Computational Replay (Phase 4)
│       └── PASS_4_PHASE_5_REPORT.md    # Public Chronology & Priority Audit (Phase 5)
└── scripts/
    ├── pass4_preserve.py               # Historical restoration and manifest generation tool
    ├── pass4_run.py                    # Deterministic execution wrapper with raw stream capture
    ├── pass4_kuber.py                  # Comparator Git object provenance extractor
    ├── pass4_chuk.py                   # Official arXiv paper and metadata collector
    ├── pass4_search.py                 # Multi-family API search runner
    ├── pass4_math_checks.py            # Independent algebraic and numerical check harness
    ├── pass4_replay_certs.py           # Standalone certificate replay harness
    ├── pass4_priority.py               # Public archive and GH Archive dataset scanner
    └── pass4_validate.py               # Automated repository-wide integrity and mapping validator
```

---

## 3. Audited Target Reference

* **Repository**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Closed State Target Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Provenance Details**: See [`SOURCE.md`](SOURCE.md) for commit anchors, submodules, and cryptographic logs.
