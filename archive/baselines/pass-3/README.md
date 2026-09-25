# Riemann Conjecture Research Audit

A public, independent, evidentiary, and multi-pass adversarial audit of the mathematical, methodological, and priority claims originating from [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

> **Audit Governance & Navigation Metadata**  
> * **Audit Status**: Active Multi-Pass Investigation (`AUDIT_PASS_3_COMPLETE` — Leading to Pass 4)  
> * **Current Master Execution Plan**: [`THIRD_AUDIT.md`](THIRD_AUDIT.md)  
> * **Current Comprehensive Report**: [`AUDIT_PASS_3.md`](AUDIT_PASS_3.md) (Master copy in [`reports/AUDIT_PASS_3.md`](reports/AUDIT_PASS_3.md))  
> * **Authoritative 4-Axis Ledger**: [`AUDIT_LEDGER.md`](AUDIT_LEDGER.md) (66 Candidate Claims)  
> * **Target Pinned Research Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Preserved Historical Passes**:  
>   * Pass 1 Master Report: [`FINAL_AUDIT.md`](FINAL_AUDIT.md) | Plan: [`archive/AUDIT_PLAN.md`](archive/AUDIT_PLAN.md)  
>   * Pass 2 Master Report: [`AUDIT_PASS_2.md`](AUDIT_PASS_2.md) | Plan: [`archive/SECOND_AUDIT.md`](archive/SECOND_AUDIT.md)

---

## 1. Objective & Scope

This repository provides an evidentiary record investigating the novelty, rigor, reproducibility, and priority of results produced by the `riemann-conjecture` project.

The audit evaluates candidate hypotheses against established mathematical literature, historical records, and contemporary preprints under an adversarial, skeptical standard.

### Core Audit Principles

1. **Strict Read-Only Stance**: The source repository snapshot under `source/riemann-conjecture/` is strictly read-only. No changes or pull requests are made upstream. All findings and artifacts reside entirely within this audit repository.
2. **Adversarial & Skeptical Default**: Claims are treated as unverified hypotheses until exhaustive literature searches, machine-checked replay, and mathematical normalization demonstrate otherwise.
3. **Four-Dimensional Decoupled Evaluation**: Mathematical result novelty, method novelty, software/verification novelty, and chronological priority are assessed independently.
4. **Historical Pass Preservation**: Historical audit artifacts from Pass 1 and Pass 2 are immutably preserved; all subsequent passes build additive, transparent corrections.
5. **Non-Closure Standard**: Where third-party external evidence is unverified (such as public push timestamps), claims are designated `INCONCLUSIVE` rather than forced into premature closure.
6. **Strict Non-Overclaim Boundary**: The project establishes certified localized Weil positivity theorems on compact support ($T \in [0.35, 0.54]$) and prime-side criteria; it does **not** prove the Riemann Hypothesis.

---

## 2. Directory Structure

```text
riemann-conjecture-audit/
├── README.md                           # Living public overview, governance, and navigation
├── THIRD_AUDIT.md                      # Active Master Audit Plan (Pass 3)
├── AUDIT_LEDGER.md                     # Authoritative 4-axis 66-claim master ledger
├── AUDIT_PASS_3.md                     # Master Comprehensive Audit Report (Pass 3, root copy)
├── AUDIT_PASS_2.md                     # Preserved Pass 2 Master Report (Historical)
├── FINAL_AUDIT.md                      # Preserved Pass 1 Master Report (Historical)
├── AUDIT_PROTOCOL.md                   # Governing Methodological Protocol (v2.0.0)
├── SOURCE.md                           # Source repo provenance and commit mapping
├── CLAIMS_TO_AUDIT.md                  # Complete inventory of 66 candidate claims
├── EVIDENCE_STANDARDS.md               # Citation rules, hit logging, and reproducibility policy
├── TIMELINE_RULES.md                   # Multi-anchor priority & timestamp evaluation framework
├── archive/
│   ├── AUDIT_PLAN.md                   # Preserved Pass 1 Execution Plan
│   └── SECOND_AUDIT.md                 # Preserved Pass 2 Execution Plan
├── source/
│   └── riemann-conjecture/             # Frozen research snapshot pinned to commit 51feb3d
├── evidence/
│   ├── computation-logs/               # Preserved raw machine execution logs & SHA-256 manifest
│   │   ├── PASS3-REPLAY-RUST-CERT.log  # rh_cert 48/48 unit & integration test log
│   │   ├── PASS3-REPLAY-RUST-ENGINE.log# rh_engine 15/15 test log
│   │   ├── PASS3-REPLAY-CERT-8OF8.log  # 8/8 Retained proof certificates verification log
│   │   ├── PASS3-REPLAY-PYTEST.log     # Core Python test suite log
│   │   └── PASS3-REPLAY-MANIFEST.json  # Cryptographic manifest of all run logs
│   ├── literature/                     # Primary literature and comparator dossiers
│   │   ├── PASS_3_PRIOR_ART.md         # Master comparative prior art dossier
│   │   ├── LIT-2026-CHUK-V2.md         # Marcus Chuk arXiv:2608.24827 analysis
│   │   └── LIT-2026-KUBER-HISTORY.md   # Kuber Mehta commit-level history trace
│   ├── public-timeline/                # Reconstructed multi-anchor Git chronologies
│   │   └── PASS_3_TIMELINE.md          # Machine-generated commit timeline
│   └── search-records/                 # Reproducible query logs with hit counts & null searches
│       ├── PASS3-SRCH-001-COMPARATORS.md
│       ├── PASS3-SRCH-002-MATHEMATICAL-METHOD.md
│       ├── PASS3-SRCH-003-LI-LAGUERRE-SCHOENBERG.md
│       ├── PASS3-SRCH-004-PUBLIC-ARCHIVES-AND-PRIORITY.md
│       └── PASS3-SRCH-005-OBSTRUCTIONS-AND-VERIFICATION.md
└── reports/
    ├── AUDIT_PASS_3.md                 # Master Comprehensive Pass 3 Audit Report
    ├── AUDIT_PASS_2.md                 # Preserved Pass 2 Master Report
    ├── FINAL_AUDIT.md                  # Preserved Pass 1 Master Report
    └── interim/                        # Phased progress dossiers
        ├── PASS_3_PHASE_0_REPORT.md    # Machine Chronology Reconstruction (WS-01)
        ├── PASS_3_PHASE_1_REPORT.md    # Literature Search Reproducibility (WS-04)
        ├── PASS_3_PHASE_2_REPORT.md    # 4-Axis Ledger Reconstruction (WS-02 & WS-03)
        ├── PASS_3_PHASE_3_REPORT.md    # Raw Computational Replay (WS-07)
        └── PASS_3_PHASE_4_REPORT.md    # Priority Cross-Examination (WS-01 & WS-04)
```

---

## 3. Audited Target Reference

* **Repository**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Closed State Target Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Provenance Details**: See [`SOURCE.md`](SOURCE.md) for detailed commit anchors and cryptographic logs.
