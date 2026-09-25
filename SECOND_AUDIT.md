# Master Audit Plan — Audit Pass 2: Adversarial Re-Audit of `riemann-conjecture`

## Executive Summary & Governance

This document establishes the operational execution plan, methodological protocol, verification gates, and milestone roadmap for **Audit Pass 2** of the public research repository [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

Audit Pass 2 is an independent, adversarial re-audit. Its primary mission is to **audit Audit Pass 1** rather than defend it. Every conclusion, verdict, and baseline established in Pass 1 is treated as a testable hypothesis subject to confirmation, narrowing, downgrading, or outright rejection based on primary evidence.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Audit Pass 2 Core Mandate                       │
├────────────────────────────────────────────────────────────────────────┤
│ • Skeptical & Adversarial Default: Seek evidence that disproves Pass 1 │
│ • Complete Claim Accounting: Adjudicate all 66 candidate claims        │
│ • Expanded Prior Art: Include public repos (e.g. Kuberwastaken/riemann)│
│ • Primary Paper Re-Audits: Exact comparison with Chuk (arXiv:2608.24827)│
│ • Decoupled Novelty: Math Result vs. Method vs. Software vs. Priority  │
│ • Strict Priority Standards: Cryptographic commit ≠ verified public push│
│ • Exact Boundary Scopes: Zero-FP verification & Lean proof boundaries  │
│ • Preservation of History: Pass 1 immutable; Pass 2 builds new record  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Governance, Repositories & Historical Boundaries

### 1.1 Target Repository Boundaries
* **Target Research Repository**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Audited Closed-State Research Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Source Snapshot Path**: `source/riemann-conjecture/` (Strict Read-Only; no modifications to history, certificates, findings, or code).

### 1.2 Pass 1 Historical Immutability
* **Pass 1 Public Head**: Commit `20b3f9d` (`FINAL_AUDIT.md - Document Complete - First Audit Complete`).
* **Preservation Rule**: Pass 1 artifacts (`FINAL_AUDIT.md`, `reports/FINAL_AUDIT.md`, Pass 1 dossiers, search records) remain unaltered as historical audit evidence.
* **Non-Authoritative Status**: Pass 1 conclusions cannot be cited as evidence for underlying scientific claims. All claims must be evaluated against primary sources.
* **Corrections in New Artifacts**: All Pass 2 adjudications, corrections, and ledger updates reside in dedicated Pass 2 files (`AUDIT_LEDGER.md`, `reports/AUDIT_PASS_2.md`, `evidence/search-records/PASS2-*.md`, etc.).

---

## 2. Core Methodological Corrections from Pass 1

Pass 2 directly resolves four fundamental shortcomings identified in Pass 1:

| Deficiency in Pass 1 | Required Pass 2 Investigation & Correction |
| :--- | :--- |
| **Claim Under-Counting** (50 stated vs. 66 actual) | Programmatic inventory of all 66 claim IDs in `CLAIMS_TO_AUDIT.md`. Every claim receives an explicit Pass 2 disposition in `AUDIT_LEDGER.md`. |
| **Timestamp Inconsistencies** (Placeholder timestamps `2026-09-24T00:00:00Z`) | Reconstruct exact repository chronology. Distinguish metadata placeholders, Git author time, committer time, local commit time, and public push timestamps. |
| **Incomplete Dossier Coverage** (Selective individual dossiers) | Audit exact dossier counts vs. aggregate reports; generate missing dossiers for high-impact claims; guarantee individual ledger adjudication for all 66 items. |
| **Narrow Literature Search Logs** (Limited search records) | Expand multi-database queries (MathSciNet, zbMATH, arXiv, Crossref, Google Scholar) and public code repository scans with timestamped execution logs. |

---

## 3. Four-Dimensional Evaluation Taxonomy

Every claim in Pass 2 must be evaluated across four orthogonal dimensions without inferring one from another:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Four Novelty Dimensions                         │
├────────────────────────────────┬───────────────────────────────────────┤
│ A. Mathematical Result Novelty │ Was the mathematical theorem/bound     │
│                                │ itself previously established?        │
├────────────────────────────────┼───────────────────────────────────────┤
│ B. Method Novelty              │ Was the analytical technique / proof   │
│                                │ reduction previously known or applied?│
├────────────────────────────────┼───────────────────────────────────────┤
│ C. Verification / Arch Novelty │ Was the software / certificate checker│
│                                │ architecture previously implemented?  │
├────────────────────────────────┼───────────────────────────────────────┤
│ D. Chronological Priority      │ Was this result/method publicly        │
│                                │ disclosed prior to external works?    │
└────────────────────────────────┴───────────────────────────────────────┘
```

### Standardized Verdict Set
* `PRIOR ART FOUND`
* `INDEPENDENT REDISCOVERY`
* `KNOWN INGREDIENT / NOVEL APPLICATION`
* `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`
* `POSSIBLY NOVEL — NO PRIOR ART FOUND`
* `NOVELTY SUPPORTED`
* `PRIORITY SUPPORTED` (Requires verified public push / disclosure evidence)
* `PRIORITY PLAUSIBLE` (Commit metadata verified; external push date unconfirmed)
* `PRIORITY NOT SUPPORTED`
* `CLAIM REQUIRES NARROWER WORDING`
* `CLAIM NOT SUPPORTED`
* `INCONCLUSIVE — REQUIRES PASS 3`

---

## 4. Mandatory Comparators & Expanded Prior Art Scope

### 4.1 Contemporary Code Repository: `Kuberwastaken/riemann`
* **Target**: `https://github.com/Kuberwastaken/riemann`
* **Audit Objectives**:
  1. Determine commit/push timeline and earliest relevant public commits.
  2. Normalize mathematical statements: finite-dimensional vs. full-space, conditional vs. unconditional, numerical vs. certified.
  3. Inspect operator formulation, prime-entry handling, Arb/interval arithmetic usage, finite sections, and tail control.
  4. Assess method overlap with compressed translations, Legendre harmonic coercivity, exact-prime treatment, and continuation.

### 4.2 Contemporary Preprint: Marcus Chuk (`arXiv:2608.24827`)
* **Target**: *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law* (Aug 25, 2026).
* **Audit Objectives**:
  1. Detailed analysis of primary text, theorems, and version history.
  2. Compare support window normalization ($T$ vs. Chuk's coordinates).
  3. Inspect proof architecture: Legendre expansions, quadrature certification, Cholesky/residual bounds, interval arithmetic vs. exact rational arithmetic.
  4. Compare theorem strength vs. `C-0050..C-0057` across chronological checkpoints.

### 4.3 Expanded Multi-Source Literature & Code Search
Search across arXiv, journal databases, zbMATH, MathSciNet, Google Scholar, Semantic Scholar, GitHub, GitLab, Zenodo, OSF, Software Heritage, and GH Archive.

---

## 5. Specific Target Investigations

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Pass 2 High-Impact Target Matrix                     │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Individual Re-Audit of Theorems C-0050 through C-0057               │
│ 2. Priority & Public Disclosure Verification for C-0050 (Aug 21)       │
│ 3. Decomposed Analysis of Exact-Prime Legendre-Schur Method            │
│ 4. Deep Literature Mapping of Li / Laguerre / Chirp / Herglotz Claims  │
│ 5. Systematic Adjudication of All 15 Obstruction Claims (CLM-OBST)     │
│ 6. Precise Boundary Audit for Zero-FP and Lean Formal Verification     │
│ 7. Strict Non-Overclaim Policy on Riemann Hypothesis (RH)              │
└────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Individual Audit of Eight Theorem Points (`C-0050` – `C-0057`)
* Separate mathematical validity from result novelty.
* Evaluate whether `C-0051..C-0057` post-date Chuk's August 25 wider-support theorem, distinguishing independent method demonstration from novel support boundary records.

### 5.2 Deep Priority Audit for `C-0050`
* Source commit `6dd1d8f07e23dd39fcd2e36974c53a5054f810ec` carries author timestamp `2026-08-21T14:05:13Z`.
* Investigate independent external public accessibility evidence (PushEvents, GH Archive, Software Heritage, Wayback Machine, fork trees).
* Enforce verdict standard: `PRIORITY SUPPORTED` only with verified public availability; otherwise `PRIORITY PLAUSIBLE`.

### 5.3 Method Deconstruction: Exact-Prime Legendre-Schur
Dissect the synthesis $J(q) \ge H_N \|q\|_2^2$ and $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ into constituent components:
1. Legendre harmonic coercivity identity $J(P_n) = H_n \|P_n\|_2^2$.
2. High-mode Weil positivity coercivity application.
3. Compressed prime translation operator treatment.
4. Componentwise tail Gram matrix decomposition and factor-3 Schur estimate.
5. Outward rationalization and exact LDL/Gershgorin certificate pipeline.
6. Adaptive moving-dimension continuation.

### 5.4 Li / Laguerre / Nonlinear Chirp Claims
Conduct deep equivalence searches for:
* Deterministic pole mode $1-q^n$ and pole-subtracted sequence.
* Shift filter $T = (E-1)(E-q)$.
* Li coefficient conditional negative definiteness ($\psi(n) = \lambda_{|n|}$ cnd $\iff$ RH, Schoenberg/Herglotz semigroups).
* Discrepancy representation $d(\psi(x)-x)$, Airy saddle pole reproduction, Cayley zero modes, and bilinear chirp separability.

### 5.5 Obstruction Claims (`CLM-OBST-001` – `CLM-OBST-015`)
Individually adjudicate all 15 obstruction claims (PNT error barriers, rank-one Hessian preservation, Montgomery-Vaughan length barrier, 69% absorption loss, Type-II separability).

### 5.6 Verification Architecture & Lean Scope Boundaries
* **Zero-Floating-Point Scope**: Confirm exact boundaries (verifier acceptance path vs. certificate generator / parsers / diagnostics).
* **Lean Formalization Scope**: State exactly which modules/lemmas are proved (LDL, Gershgorin, Interval, Endpoint Absorption) vs. parts outside Lean (generator, analytical derivation, full theorem chain).

### 5.7 RH Scope Enforcement
Confirm that all findings represent finite-support localized Weil positivity or RH-equivalent criteria, with zero unproved leaps to full RH.

---

## 6. Phased Execution Roadmap

```text
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5
Inventory   Expanded    Math &      Verifier    Chronology  Ledger &
& Baseline  Prior Art   Methodology & Formal    & Priority  Pass 2 Dossier
```

### Phase 0: Claim Inventory & Chronology Reconstruction
* Run programmatic count and extract all 66 claim IDs from `CLAIMS_TO_AUDIT.md`.
* Map Pass 1 dossier coverage gaps.
* Reconstruct commit and metadata chronology for both `riemann-conjecture` and `riemann-conjecture-audit`.
* **Exit Gate**: Complete 66-claim inventory mapped; baseline chronology documented.

### Phase 1: Expanded Prior Art & Comparator Ingestion
* Ingest and mathematically normalize `Kuberwastaken/riemann`.
* Ingest and dissect Marcus Chuk (`arXiv:2608.24827`).
* Execute multi-database searches across all claim clusters; write query records to `evidence/search-records/PASS2-*.md`.
* **Exit Gate**: Comparative analysis dossiers for Chuk and Kuberwastaken; search logs logged.

### Phase 2: Mathematical, Methodological & Obstruction Re-Audit
* Re-evaluate `C-0050..C-0057` validity vs. result novelty.
* Deconstruct Exact-Prime Legendre-Schur method components.
* Evaluate Li/Laguerre and Schoenberg/Herglotz equivalence.
* Adjudicate all 15 `CLM-OBST` claims individually.
* **Exit Gate**: Drafted claim assessments for all math, method, and obstruction claims.

### Phase 3: Verification Architecture & Formal Soundness Audit
* Verify `rh_cert` Rust replay behavior and certificate hashes.
* Audit precision boundaries: verify that acceptance decisions use exact rational arithmetic without floating-point dependencies.
* Audit Lean formalization files (`source/riemann-conjecture/formal/`) and explicitly delimit proved lemmas vs. unformalized components.
* **Exit Gate**: Precise verification scope dossier drafted.

### Phase 4: Priority & Chronological Cross-Examination
* Search public GitHub events, archives, and mirrors for `C-0050` public push verification.
* Build multi-anchor timeline matrix in `evidence/public-timeline/PASS_2_TIMELINE.md`.
* Assign decoupled priority verdicts (`PRIORITY SUPPORTED`, `PRIORITY PLAUSIBLE`, etc.).
* **Exit Gate**: Chronology matrix complete with primary timestamp citations.

### Phase 5: Synthesis, Authoritative Ledger & Deliverables
* Construct `AUDIT_LEDGER.md` with explicit rows for all 66 claims.
* Compile master report `reports/AUDIT_PASS_2.md`.
* Identify unresolved items and establish "Required Pass 3 Investigations".
* **Exit Gate**: Full Pass 2 deliverable suite delivered without overwriting Pass 1 artifacts.

---

## 7. Deliverable Matrix

```text
riemann-conjecture-audit/
├── SECOND_AUDIT.md                     # This master execution plan
├── AUDIT_LEDGER.md                     # Authoritative 66-claim verdict & change ledger
├── reports/
│   ├── AUDIT_PASS_2.md                 # Master Pass 2 comprehensive audit report
│   └── interim/
│       └── PASS_2_INTERIM_REPORT.md    # Mid-pass progress dossier
├── evidence/
│   ├── public-timeline/
│   │   └── PASS_2_TIMELINE.md          # Multi-anchor priority & disclosure timeline
│   ├── literature/
│   │   └── PASS_2_PRIOR_ART.md         # Normalized comparative prior art & comparator dossier
│   └── search-records/
│       └── PASS2-*.md                  # Reproducible search logs with real execution timestamps
└── claims/
    └── [category]/                     # New and updated Pass 2 claim dossiers
```

---

## 8. Non-Closure Principle & Pass 3 Transition

Audit Pass 2 is an intermediate adversarial stage aimed at scientific convergence. It must not declare itself the final audit or overwrite consolidated final templates. Any claim lacking definitive primary evidence or requiring deeper formalization review will be marked `INCONCLUSIVE — REQUIRES PASS 3` and listed under **Required Pass 3 Investigations** in `reports/AUDIT_PASS_2.md`.
