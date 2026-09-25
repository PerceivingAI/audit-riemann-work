# Master Audit Plan: Riemann Conjecture Research

This document outlines the phased execution strategy, prioritization matrix, verification gates, and milestone roadmap for the independent audit of [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).
> **Audit Execution Metadata**  
> * **Master Plan Version**: `1.0.0`  
> * **Effective Date**: `2026-09-24T00:00:00Z`  
> * **Current Phase**: `Phase 1: Literature Baseline & Prior Art Mapping`  
> * **Audited Target Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`


---

## 1. Audit Tiering & Execution Priority

The 50 candidate propositions in [`CLAIMS_TO_AUDIT.md`](../CLAIMS_TO_AUDIT.md) are prioritized into four sequential tiers based on mathematical significance, methodology impact, and priority exposure:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ Tier A: Core Weil Positivity & Exact-Prime Legendre-Schur Method       │
│ (C-0050..C-0057, Coercivity, Tail-Gram Schur, Rational Certificates)   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Tier B: Li/Laguerre Prime-Side, Stationary-Map & Nonlinear Chirp       │
│ (Pole Subtraction, Shift Filters, Cayley Modes, Airy Saddles)          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Tier C: Independent Verification & Computational Assurance             │
│ (Rust rh_cert Replay, Lean Formalization, Retained Hash Chain)         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Tier D: Barriers, Obstructions & Negative Results                      │
│ (Vaughan/Rank-1 Hessian, Lossy Absorption, Gram Atom Obstructions)    │
└────────────────────────────────────────────────────────────────────────┘
```

### Tier Definitions
* **Tier A (Highest Impact — Core Theorems & Method)**:
  * Claims: `CLM-MATH-001` through `CLM-MATH-008`, `CLM-METH-001` through `CLM-METH-005`, `CLM-CONT-001`, `CLM-PRIO-004` through `CLM-PRIO-006`.
  * Focus: Validity and novelty of localized Weil positivity beyond the prime-free regime; Legendre harmonic coercivity $J(P_n)=H_n\|P_n\|_2^2$; component tail-Gram Schur reduction; moving-dimension continuation.
* **Tier B (Mathematical Novelty — Prime-Side Criteria)**:
  * Claims: `CLM-LAGU-001` through `CLM-LAGU-005`, `CLM-AIRY-001` through `CLM-AIRY-007`, `CLM-GRAM-001`, `CLM-GRAM-002`, `CLM-PRIO-007` through `CLM-PRIO-009`, `CLM-PRIO-011`.
  * Focus: Exact zeta-pole mode extraction ($1-q^n$), pole-annihilating shift filter $T=(E-1)(E-q)$, stationary-phase Cayley reproduction, nonlinear Mellin chirp interpretation, Schoenberg-Herglotz characterization.
* **Tier C (Verification & Software Assurance)**:
  * Claims: `CLM-VERF-001` through `CLM-VERF-007`.
  * Focus: Zero-floating-point Rust replay verifier (`rh_cert`), exact rational interval certificates, multi-implementation admission guards, Lean soundness proof integration.
* **Tier D (Obstructions & Negative Results)**:
  * Claims: `CLM-OBST-001` through `CLM-OBST-015`, `CLM-OPER-001`, `CLM-OPER-002`, `CLM-GRAM-003`, `CLM-PRIO-010`, `CLM-PRIO-012`.
  * Focus: Rank-one Hessian $\text{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$ in multiplicative convolutions, PNT pointwise exponent barriers, Montgomery-Vaughan length obstructions, compressed shift norm $\|S_{T,a}\|=2\cos\frac{\pi}{L+1}$.

---

## 2. Phased Roadmap & Workflow

```text
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5
Target      Literature  Math &      Verifier    Priority    Synthesis &
Ingestion   Baseline    Methodology Replay      Timeline    Final Report
```

### Phase 0: Target Ingestion & Baseline Verification
* **Goal**: Establish the local read-only checkout of `PerceivingAI/riemann-conjecture` pinned to commit `51feb3d176e4a53773c22dc157567cc0486f4c71`.
* **Tasks**:
  1. Initialize Git submodule / clone at `source/riemann-conjecture`.
  2. Verify repository tree integrity and check out commit `51feb3d`.
  3. Validate cryptographic commit hashes and timestamps corresponding to all historical anchors listed in `SOURCE.md`.
* **Exit Gate**: All source files accessible locally; commit hashes verified; read-only boundary enforced.

### Phase 1: Literature Baseline & Prior Art Mapping
* **Goal**: Build the comparative prior art foundation across both pre-2026 literature and contemporaneous 2026 public work.
* **Key Literature Domains**:
  1. *Weil Positivity*: Weil, Bombieri, Connes, Consani, Suzuki, Burnol, Lagarias.
  2. *Li Criterion & Generalizations*: Li, Keiper, Coffey, Sekatskii, Arias de Reyna, Voros.
  3. *Spectral & Coercivity Methods*: Orthogonal polynomials, Legendre coercivity bounds, Schur complements, path graph spectra.
  4. *2026 Contemporaneous Work*: arXiv preprints (math.NT, math.CA, math.SP) from 2026.
* **Tasks**:
  1. Execute systematic queries logging every search in `evidence/search-records/`.
  2. Construct bibliographic metadata files in `evidence/literature/` per `EVIDENCE_STANDARDS.md`.
* **Exit Gate**: Comprehensive literature matrix establishing state-of-the-art baselines prior to individual claim evaluations.

### Phase 2: Mathematical & Methodological Audit (Tiers A, B, D)
* **Goal**: Perform rigorous claim-by-claim mathematical normalization, structural comparison, and outcome verdict assignment.
* **Tasks**:
  1. Process Tier A claims: normalize notation ($T, L, N$), inspect proofs in `source/riemann-conjecture/`, compare against literature baselines, draft dossiers in `claims/mathematical/` and `claims/methodology/`.
  2. Process Tier B claims: evaluate Li/Laguerre, shift-filter, and chirp formulations against generalized Li literature.
  3. Process Tier D claims: evaluate structural no-go theorems and obstruction proofs.
* **Exit Gate**: Completed audit dossiers for all mathematical and methodological claims, terminating in standardized verdicts from `AUDIT_PROTOCOL.md`.

### Phase 3: Verification & Certificate Independent Replay (Tier C)
* **Goal**: Audit computational reproducibility, exact rational arithmetic, and formal soundness.
* **Tasks**:
  1. Evaluate Rust verifier (`rh_cert`) source code and independent arithmetic engine.
  2. Replay all 8 retained proof certificates ($T=0.35$ through $T=0.54$) and verify SHA-256 hashes.
  3. Verify adversarial contract-failure tests (ensure malformed inputs fail contract vs. theorem verification).
  4. Review Lean formalization files for coverage of verifier soundness lemmas.
  5. Draft dossiers in `claims/verification/`.
* **Exit Gate**: Verified reproducibility status for computational claims and certificate replay.

### Phase 4: Priority & Chronological Cross-Examination
* **Goal**: Evaluate precedence claims by comparing public Git commit timestamps against external disclosure dates.
* **Tasks**:
  1. Query public GitHub API / commit archives for earliest push timestamps ($T_{\text{public\_push}}$).
  2. Map external preprint announcement timestamps ($T_{\text{ext\_post}}$) for all related 2026 work.
  3. Construct multi-anchor timeline tables in `evidence/public-timeline/` and `claims/priority/` per `TIMELINE_RULES.md`.
  4. Assign formal priority verdicts (`PRIORITY SUPPORTED`, `PRIORITY PLAUSIBLE`, `PRIOR ART FOUND`, etc.).
* **Exit Gate**: Definitive chronological comparison tables and priority verdicts for all priority claims.

### Phase 5: Synthesis & Final Audit Report Delivery
* **Goal**: Synthesize all individual dossiers into interim and final audit deliverables.
* **Tasks**:
  1. Compile interim audit report in `reports/interim/`.
  2. Synthesize final comprehensive findings in `reports/FINAL_AUDIT.md`.
  3. Update `CLAIMS_TO_AUDIT.md` status table to reflect all final verdicts.
* **Exit Gate**: Completed, self-contained `FINAL_AUDIT.md` presenting complete evidentiary records, verdicts, and limitations.

---

## 3. Quality Gates & Adversarial Checks

To prevent confirmation bias, every claim evaluation must pass three mandatory checks:

1. **Adversarial Prior Art Search**: Before concluding `NOVELTY SUPPORTED` or `POSSIBLY NOVEL — NO PRIOR ART FOUND`, at least three distinct query permutations across multiple databases (MathSciNet, zbMATH, arXiv, Google Scholar) must be executed and logged.
2. **Mathematical Normalization Sign-Off**: No claim may be judged novel based on notation or coordinate differences alone; equivalence to known formulations must be explicitly tested.
3. **Primary Source Integrity**: Every cited prior art paper must reference exact page/theorem numbers and verified bibliographic metadata.

---

## 4. Deliverable Matrix

| Deliverable | Location | Target Phase |
| :--- | :--- | :--- |
| Pinned Source Snapshot | `source/riemann-conjecture/` | Phase 0 |
| Literature Database Query Logs | `evidence/search-records/*.md` | Phase 1 |
| External Literature Dossiers | `evidence/literature/*.md` | Phase 1 |
| Mathematical Claim Dossiers | `claims/mathematical/CLM-MATH-*.md` | Phase 2 |
| Methodology Claim Dossiers | `claims/methodology/CLM-METH-*.md` | Phase 2 |
| Obstruction Claim Dossiers | `claims/mathematical/CLM-OBST-*.md` | Phase 2 |
| Verification Claim Dossiers | `claims/verification/CLM-VERF-*.md` | Phase 3 |
| Timeline & Priority Dossiers | `claims/priority/CLM-PRIO-*.md` | Phase 4 |
| Multi-Anchor Chronology Logs | `evidence/public-timeline/*.md` | Phase 4 |
| Interim Audit Report | `reports/interim/INTERIM_REPORT.md` | Phase 4/5 |
| Final Comprehensive Audit Report | `reports/FINAL_AUDIT.md` | Phase 5 |
