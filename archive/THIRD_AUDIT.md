# Master Audit Plan — Audit Pass 3: Evidence Infrastructure Repair, Methodological Completion & Multi-Axis Convergence

## Executive Summary & Governance

This document establishes the operational execution plan, methodological standards, quality gates, and milestone roadmap for **Audit Pass 3** of the public research repository [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

While Audit Pass 2 resolved core structural defects of Pass 1 (expanding candidate accounting to 66 claims, decoupling novelty dimensions, identifying missing comparators, and narrowing overconfident verdicts), it exposed internal evidence infrastructure weaknesses:
* Timestamp and timezone conversion inconsistencies in manual timeline tables.
* Search records lacking full reproducibility criteria (missing returned-result counts, filters, and null-search logs).
* Comparator analysis based on repository snapshots rather than full commit histories.
* Ledger ID-to-rationale mapping shifts in specific sections.
* Absence of raw, hashed machine execution logs for independent computational replays.
* Artifact hygiene defects (control characters, broken relative paths in root copies).
* Stale root navigation stating the audit was concluded.

**Audit Pass 3 is primarily an evidence-infrastructure repair, rigorous multi-axis evaluation, and methodological completion pass.** Its objective is to build an unassailable, fully reproducible evidentiary record.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Audit Pass 3 Core Mandate                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Machine-Generated Chronology: Full Git log automation, local vs UTC │
│ 2. Real-Time Search Logging: Total hits, filters, shortlists, nulls    │
│ 3. Deep Comparator Histories: Commit-by-commit trace of Kuber & Chuk   │
│ 4. Authoritative 4-Axis Schema: Explicit 7-column matrix for all 66 IDs │
│ 5. Raw Replay Artifacts: Captured CLI outputs, exit codes, log hashes  │
│ 6. Protocol & Taxonomy Governance: Versioned standardized taxonomy     │
│ 7. Living Navigation & Hygiene: Clean relative paths, 0 control chars  │
│ 8. Non-Closure Principle: Explicit INCONCLUSIVE standard for gaps      │
│ 9. Immutable Past: Preserve Pass 1 and Pass 2 historical artifacts     │
│ 10. Strict RH Boundary: Enforce finite-support / criterion boundary    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Repository Boundaries & Historical Immutability

### 1.1 Target Research Repository Boundary
* **Target Repository**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Audited Closed-State Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Source Snapshot Path**: `source/riemann-conjecture/` (Strict Read-Only; no modification to research history, findings, tests, or code).

### 1.2 Historical Audit Passes Preservation
* **Pass 1 Head**: Commit `20b3f9d` (`FINAL_AUDIT.md - Document Complete - First Audit Complete`).
* **Pass 2 Head**: Commit `66d70cd` (`SECOND_AUDIT.md - Adversarial audit complete`).
* **Preservation Rule**: Pass 1 and Pass 2 artifacts remain permanent, immutable records of their respective audit stages.
* **Non-Overwriting Policy**: No historical reports (`FINAL_AUDIT.md`, `reports/FINAL_AUDIT.md`, `AUDIT_PASS_2.md`, `reports/AUDIT_PASS_2.md`) will be overwritten. All Pass 3 work generates dedicated Pass 3 artifacts (`reports/AUDIT_PASS_3.md`, `AUDIT_PASS_3.md`, `evidence/search-records/PASS3-*.md`, etc.).

---

## 2. The Twelve Core Workstreams of Pass 3

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Twelve Corrective Workstreams (Pass 3)               │
├────────────────────────────────────────────────────────────────────────┤
│ WS-01: Machine-Generated Chronology Reconstruction                     │
│ WS-02: Programmatic Ledger Rebuilding & ID Mapping Verification        │
│ WS-03: Full 4-Axis Decoupled Ledger Implementation (All 66 Claims)     │
│ WS-04: Fully Reproducible Literature & Repository Search Logs          │
│ WS-05: Deep Commit-by-Commit Comparator History Tracking (Kuber/Chuk)  │
│ WS-06: Structured Primary Literature & Comparator Dossiers             │
│ WS-07: Preserved Raw Independent Computational Replay Evidence         │
│ WS-08: Formalized Audit Protocol & Taxonomy Versioning (v2.0.0)        │
│ WS-09: Phased Git Commit Granularity                                   │
│ WS-10: Synchronized Navigation & Governance (README.md)                │
│ WS-11: Automated Artifact Hygiene & Link Integrity Gate                │
│ WS-12: Disciplined Application of the INCONCLUSIVE Standard            │
└────────────────────────────────────────────────────────────────────────┘
```

### WS-01: Machine-Generated Chronology Reconstruction
1. Automate chronology generation using Python scripts parsing `git log --format="%h|%an|%ad|%cn|%cd|%s" --date=iso-strict`.
2. Explicitly output and retain both the original author timezone offset (e.g. `-05:00`) and the computed UTC timestamp (`Z`).
3. Reconcile internal metadata timestamps from Pass 2, categorizing them as unverified internal metadata rather than execution evidence.
4. Correct commit hash associations (e.g. ensure `CLM-PRIO-004` points to `fab5933` at `2026-08-20T22:45:23-05:00` / `2026-08-21T03:45:23Z`).

### WS-02 & WS-03: Programmatic Ledger Rebuilding & 4-Axis Evaluation Schema
1. Programmatically parse `CLAIMS_TO_AUDIT.md` to extract exact proposition statements for all 66 claims.
2. Verify one-to-one correspondence between Claim ID, Category, Proposition Summary, Anchor Commit, and Pass 3 Adjudication (resolving Pass 2 row shifts in `CLM-GRAM-001..002` and `CLM-VERF-004..006`).
3. Replace single-verdict columns in `AUDIT_LEDGER.md` with an explicit **7-column multi-axis evaluation schema**:
   * **Col 1**: Claim ID & Category
   * **Col 2**: Proposition Summary & Source Anchor
   * **Col 3**: Mathematical Validity / Factual Status (`VERIFIED`, `FALSIFIED`, `UNTESTED`)
   * **Col 4**: Mathematical Result Novelty (`NOVEL`, `SUBSUMED`, `KNOWN`, `N/A`)
   * **Col 5**: Method Novelty (`NOVEL SYNTHESIS`, `NOVEL APPLICATION`, `KNOWN METHOD`, `N/A`)
   * **Col 6**: Software / Verification Novelty (`NOVEL ARCHITECTURE`, `STANDARD`, `N/A`)
   * **Col 7**: Chronological Priority Status (`PRIORITY SUPPORTED`, `PRIORITY PLAUSIBLE`, `PRIOR ART FOUND`, `N/A`)
   * **Col 8**: Evidence Completeness & Disposition (`COMPLETE`, `INCONCLUSIVE — REQUIRES PASS 4`, `NARROWED`)

### WS-04: Literature Search Standards & Reproducibility
Every search log in `evidence/search-records/PASS3-*.md` must strictly record:
* Execution timestamp (ISO-8601 with actual execution time).
* Database / Engine / Repository searched (MathSciNet, zbMATH, arXiv, Crossref, Google Scholar, GitHub, Software Heritage, etc.).
* Exact query string and all Boolean/syntax permutations.
* Exact filters applied (date ranges, subject classifications, language).
* **Total result count returned**.
* **Shortlisted items inspected** with full citations.
* **Null / zero-hit searches** explicitly documented.
* Detailed rejection or equivalence rationale for candidate prior art.

### WS-05 & WS-06: Deep Comparator History & Structured Dossiers
1. **`Kuberwastaken/riemann`**:
   * Perform commit-level analysis across its history from July 23, 2026 onward.
   * Trace the evolution of `experiments/weil_positivity/`, Arb ball certificates, and finite-dimensional vs full-space boundary discussions.
2. **Marcus Chuk (`arXiv:2608.24827`)**:
   * Document exact arXiv submission timestamp (`2026-08-25T11:42:00Z`), version history (v1, v2), and detailed error-bound derivations.
3. Build formal dossiers in `evidence/literature/` containing stable URLs, DOIs, math notations mapped to project variables, and comparative proofs.

### WS-07: Preserved Raw Independent Computational Replay Evidence
1. Execute clean, independent verifier runs and tests against `source/riemann-conjecture/`:
   * `cargo test --all` in `crates/rh_cert` and `crates/rh_engine`.
   * Replay all 8 retained proof certificates (`C-0050` through `C-0057`).
   * Adversarial contract rejection tests (invalid certificates, corrupt schemas).
2. Capture and store raw machine logs in `evidence/computation-logs/PASS3-REPLAY-*.log` including:
   * Execution start/end timestamps.
   * Host architecture, OS, Rust/Cargo/Python toolchain versions.
   * Working directory and git commit SHA of the audited checkout.
   * Exact invocation command line.
   * Complete exit code, stdout, and stderr.
   * SHA-256 hash of the generated log artifact.

### WS-08: Formalized Audit Protocol & Taxonomy Versioning
Establish `AUDIT_PROTOCOL.md` Version 2.0.0 defining the standardized closed set of evaluation outcomes across all dimensions.

### WS-09: Phased Git Commit Granularity
Commit each audit phase independently to ensure the repository's Git history provides a verifiable chronological audit trail.

### WS-10: Synchronized Public Navigation (`README.md`)
Update the root `README.md` to reflect the active, multi-pass governance:
* Document Pass 1 as completed/historical.
* Document Pass 2 as completed/intermediate.
* Document Pass 3 as active/in-progress.
* Provide direct navigational links to `AUDIT_PASS_2.md`, `AUDIT_PASS_3.md`, `AUDIT_LEDGER.md`, and `THIRD_AUDIT.md`.

### WS-11: Automated Artifact Hygiene & Link Verification Gate
Implement an automated pre-commit check verifying:
* Zero non-printing control characters (`\f`, `\u0007`, etc.).
* Zero malformed LaTeX macros (e.g. proper raw escaping of `\frac`, `\approx`, `\times`).
* All relative markdown links resolve correctly from their specific directory depth.
* Consistency between root convenience copies and `reports/` master dossiers.

### WS-12: Strict Enforcement of `INCONCLUSIVE` and RH Boundary
* Enforce `INCONCLUSIVE — REQUIRES PASS 4` whenever evidence is incomplete (e.g. unverified public push archives).
* Enforce zero overclaim on the Riemann Hypothesis across all reports.

---

## 3. Four-Dimensional Evaluation Taxonomy (v2.0.0)

Every claim in Pass 3 must be evaluated using the versioned 4-axis taxonomy:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Versioned 4-Axis Taxonomy                       │
├─────────────────────────────────┬──────────────────────────────────────┤
│ Axis 1: Mathematical Validity   │ • VERIFIED                           │
│                                 │ • FALSIFIED                          │
│                                 │ • UNTESTED / THEORETICAL             │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 2: Mathematical Result     │ • NOVEL SUPPORT BOUND                │
│         Novelty                 │ • RESULT SUBSUMED BY PRIOR ART       │
│                                 │ • PRIOR ART FOUND                    │
│                                 │ • N/A (Method / Tool / Barrier)      │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 3: Method Novelty          │ • NOVEL SYNTHESIS SUPPORTED          │
│                                 │ • KNOWN INGREDIENT / NOVEL APPL.     │
│                                 │ • KNOWN METHOD                       │
│                                 │ • N/A (Pure Math Result / Verifier)  │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 4: Software / Verification │ • NOVEL VERIFICATION ARCHITECTURE    │
│         Novelty                 │ • STANDARD IMPLEMENTATION            │
│                                 │ • N/A (Analytical Claim)             │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 5: Chronological Priority  │ • PRIORITY SUPPORTED (Public Push)   │
│                                 │ • PRIORITY PLAUSIBLE (Commit Only)   │
│                                 │ • PRIOR ART FOUND (External Earlier) │
│                                 │ • INCONCLUSIVE                       │
└─────────────────────────────────┴──────────────────────────────────────┘
```

---

## 4. Phased Execution Roadmap

```text
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5
Machine     Search &    4-Axis      Raw Replay  Priority    Synthesis &
Chronology  Comparator  Ledger      & Lean      Matrix      Pass 3 Report
& Nav Sync  Histories   Rebuild     Artifacts   Archives    & Hygiene Gate
```

### Phase 0: Machine Chronology Reconstruction & Governance Synchronization
* Programmatically extract commit logs for `riemann-conjecture` and `riemann-conjecture-audit` with explicit local and UTC timestamps.
* Reconcile Pass 2 internal metadata timestamps.
* Update `README.md` navigation to reflect active Pass 3 governance.
* **Exit Gate**: Machine chronology generated; `README.md` synchronized.

### Phase 1: Search Protocol Re-Execution & Deep Comparator Histories
* Re-execute all literature and repository searches with complete hit counts, query variants, filters, and null-search records in `evidence/search-records/PASS3-*.md`.
* Trace commit-by-commit history of `Kuberwastaken/riemann` and version history of Marcus Chuk (`arXiv:2608.24827`).
* Generate structured prior art dossiers in `evidence/literature/`.
* **Exit Gate**: Search records compliant with `EVIDENCE_STANDARDS.md`; comparator commit traces complete.

### Phase 2: Authoritative 4-Axis Ledger Reconstruction
* Programmatically join candidate propositions from `CLAIMS_TO_AUDIT.md` to `AUDIT_LEDGER.md`.
* Eliminate ID/rationale shifts and populate all 7 evaluation columns for all 66 claims.
* Validate individual adjudications across Theorems, Methods, Operators, Barriers, Criteria, and Software.
* **Exit Gate**: 66/66 claims populated across all 4 axes with zero ID misalignments.

### Phase 3: Raw Computational Replay & Lean Boundary Verification
* Execute `cargo test --all`, exact-rational certificate replays, and adversarial error tests.
* Archive raw command outputs, environment metadata, exit codes, and SHA-256 hashes in `evidence/computation-logs/`.
* Audit Lean 4 formalization modules and verify explicit boundaries.
* **Exit Gate**: Raw machine logs captured and hashed; verification boundaries confirmed.

### Phase 4: Multi-Anchor Priority Cross-Examination
* Search third-party public archives (GH Archive, Software Heritage, Wayback Machine) for public push evidence for `C-0050` (`6dd1d8f0`).
* Construct multi-anchor priority matrix in `evidence/public-timeline/PASS_3_TIMELINE.md`.
* Adjudicate all 12 priority claims (`CLM-PRIO-001..012`).
* **Exit Gate**: Priority matrix complete with decoupled public push evidence.

### Phase 5: Synthesis, Artifact Hygiene Gate & Master Report
* Compile master report `reports/AUDIT_PASS_3.md` and copy to root `AUDIT_PASS_3.md`.
* Run automated artifact hygiene checks:
  1. Scan for control characters.
  2. Verify all relative links.
  3. Verify LaTeX macro escaping.
  4. Validate consistency between root and `reports/` files.
* Establish Required Pass 4 Investigations.
* **Exit Gate**: Master report complete; hygiene gate verified with 0 errors.

---

## 5. Deliverable Matrix

```text
riemann-conjecture-audit/
├── THIRD_AUDIT.md                      # This master execution plan
├── AUDIT_LEDGER.md                     # Reconstructed 4-axis 66-claim master ledger
├── AUDIT_PASS_3.md                     # Master comprehensive report (Root copy)
├── README.md                           # Synchronized public navigation & governance
├── reports/
│   ├── AUDIT_PASS_3.md                 # Master comprehensive audit report (Pass 3)
│   └── interim/
│       ├── PASS_3_PHASE_0_REPORT.md    # Machine Chronology & Governance Dossier
│       ├── PASS_3_PHASE_1_REPORT.md    # Search Reproducibility & Comparators Dossier
│       ├── PASS_3_PHASE_2_REPORT.md    # 4-Axis Claim Adjudication Dossier
│       ├── PASS_3_PHASE_3_REPORT.md    # Raw Replay & Lean Soundness Dossier
│       └── PASS_3_PHASE_4_REPORT.md    # Multi-Anchor Priority Dossier
├── evidence/
│   ├── computation-logs/
│   │   ├── PASS3-REPLAY-RUST-TESTS.log # Captured raw test execution log
│   │   ├── PASS3-REPLAY-CERT-8OF8.log  # Captured raw certificate replay log
│   │   └── PASS3-REPLAY-MANIFEST.json  # SHA-256 manifest of all raw run logs
│   ├── literature/
│   │   ├── PASS_3_PRIOR_ART.md         # Comprehensive prior art & comparator dossier
│   │   ├── LIT-2026-CHUK-V2.md         # Dedicated Chuk arXiv analysis dossier
│   │   └── LIT-2026-KUBER-HISTORY.md   # Dedicated Kuber Mehta commit trace dossier
│   ├── public-timeline/
│   │   └── PASS_3_TIMELINE.md          # Machine-generated multi-anchor chronology
│   └── search-records/
│       ├── PASS3-SRCH-001-COMPARATORS.md
│       ├── PASS3-SRCH-002-MATHEMATICAL-METHOD.md
│       ├── PASS3-SRCH-003-LI-LAGUERRE-SCHOENBERG.md
│       └── PASS3-SRCH-004-OBSTRUCTIONS-AND-VERIFICATION.md
└── archive/
    ├── AUDIT_PLAN.md                   # Preserved First Audit Plan
    ├── AUDIT_PASS_2.md                 # Preserved Second Audit Report (Root copy)
    └── reports/
        └── AUDIT_PASS_2.md             # Preserved Second Audit Report
```

---

## 6. Non-Closure Rule & Pass 4 Transition

Audit Pass 3 strictly maintains that convergence requires complete, unassailable evidence. Any claim where third-party public archives or mathematical reductions remain incomplete will be explicitly assigned `INCONCLUSIVE — REQUIRES PASS 4` and listed under **Required Pass 4 Investigations** in `reports/AUDIT_PASS_3.md`.
