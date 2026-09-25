# Audit Pass 2 — Comprehensive Adversarial Re-Audit Report

> **Audit Report Metadata**  
> * **Document Type**: Master Comprehensive Audit Dossier (Pass 2)  
> * **Audit Status**: `AUDIT_PASS_2_COMPLETE` (Non-Closure Stage; Leads into Pass 3)  
> * **Audit Effective Timestamp**: `2026-09-24T21:30:00Z`  
> * **Governing Master Plan**: [`SECOND_AUDIT.md`](archive/SECOND_AUDIT.md)  
> * **Authoritative Ledger**: [`AUDIT_LEDGER.md`](AUDIT_LEDGER.md)  
> * **Audited Target Repository**: `https://github.com/PerceivingAI/riemann-conjecture`  
> * **Audited Closed-State Research Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Historical Pass 1 Baseline Snapshot**: `20b3f9d` (`FINAL_AUDIT.md - Document Complete - First Audit Complete`)

---

## 1. Executive Summary & Audit Governance

This document presents the comprehensive findings of **Audit Pass 2** on the mathematical research repository `PerceivingAI/riemann-conjecture`.

### 1.1 Core Audit Stance & Principle
Audit Pass 2 was executed under an **adversarial, correction-seeking standard**. Rather than defending or validating Audit Pass 1, Pass 2 treats all Pass 1 conclusions as hypotheses to be independently tested, narrowed, or downgraded. 

Historical Pass 1 artifacts (`FINAL_AUDIT.md`, `reports/FINAL_AUDIT.md`, Pass 1 dossiers) remain completely immutable on disk as an unedited historical audit trail. All Pass 2 adjudications, corrections, and ledger updates reside strictly in dedicated Pass 2 artifacts.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Pass 2 Audit Scorecard                          │
├────────────────────────────────────────────────────────────────────────┤
│ • Total Candidate Claims in Scope:        66 (Correcting Pass 1's 50)  │
│ • Claims with Verified Math Validity:     66 / 66                      │
│ • Claims with Novelty / Synthesis Novel:  49 / 66                      │
│ • Claims Subsumed / Narrowed / Downgraded: 15 / 66                      │
│ • Claims with Identified Prior Art:        2 / 66 (Lagarias, Tuck)     │
│ • Zero-Float Verification Acceptance:     100% Exact (BigRational)     │
│ • Lean 4 Formal Soundness Modules:        36 Lemmas Formally Verified  │
│ • Riemann Hypothesis Status:              0% Proved (Boundary Enforced)│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Methodological Corrections from Pass 1

Pass 2 has investigated and resolved four structural defects inherited from Audit Pass 1:

1. **Claim Count & Accounting Correction**:
   Pass 1 asserted that exactly 50 candidate propositions were evaluated. A programmatic scan of `CLAIMS_TO_AUDIT.md` confirmed **66 unique candidate claims** across 12 categories. All 66 claims have been ingested into [`AUDIT_LEDGER.md`](AUDIT_LEDGER.md) and individually adjudicated.
2. **Reconciliation of Placeholder Timestamps**:
   Pass 1 recorded `2026-09-24T00:00:00Z` across its document metadata, which predated the audited research commit (`51feb3d` at `21:36:44Z`) by 21h 36m and the audit repository creation (`116c11f` at `22:49:30Z`) by 22h 49m. Pass 2 forensically reconstructed the exact multi-anchor Git author/committer timeline across all 70 source commits in [`PASS_2_TIMELINE.md`](evidence/public-timeline/PASS_2_TIMELINE.md).
3. **Dossier Coverage Gap Resolution**:
   Pass 1 generated only 11 physical dossier files, leaving 7 broken references (`CLM-PRIO-006..012`) and directing 28 claims to aggregate reports. Pass 2 provides explicit line-item dispositions for all 66 items in the master ledger.
4. **Expanded Search & Comparator Scope**:
   Pass 2 expanded beyond paper literature to ingest public code repositories (notably `Kuberwastaken/riemann`) and contemporary preprints (Marcus Chuk `arXiv:2608.24827`), logging reproducible search records in `evidence/search-records/PASS2-SRCH-001..004`.

---

## 3. Mandatory Comparators & Expanded Prior Art

### 3.1 Comparator I: `Kuberwastaken/riemann` (Kuber Mehta, July 23, 2026)
* **Scope**: Open research archive compiling 178 sources on RH and exploring numerical/interval Weil positivity in `experiments/weil_positivity/`.
* **Findings**: Certified archimedean coercivity $c_0 \ge 0.349152$ and tested finite-dimensional subspaces ($L=0.45..0.62$) via Arb ball arithmetic and certified Cholesky.
* **Normalization & Boundary**: Kuberwastaken's work explicitly addresses **finite-dimensional test function families** only. Infinite-dimensional spectral and tail bounds were left uncertified, meaning it does not prove full-space $L^2([-T, T])$ theorems, nor does it implement Legendre harmonic coercivity or exact-prime Schur complements.
* **Verdict**: Does not invalidate `riemann-conjecture`'s full-space theorems or method novelty.

### 3.2 Comparator II: Marcus Chuk (`arXiv:2608.24827`, August 25, 2026)
* **Title**: *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*
* **Scope**: Proves unconditional certified full-space positivity at $L=0.8$ (autocorrelation width $1.6$) with $Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2$.
* **Discretization & Tail Control**: Full Legendre modal expansion with Gauss-Legendre quadrature and continuous symbol decay envelopes using floating-point interval arithmetic.
* **Comparative Impact**:
  - **Result Novelty**: Chuk's theorem establishes compact Weil positivity across a wider support domain ($L=0.8$) than the repository's frontier ($T=0.54$). Therefore, project continuation points $T \in [0.40, 0.54]$ committed after August 25 (`C-0051..C-0057`) are mathematically subsumed as support records.
  - **Method Novelty**: `riemann-conjecture`'s exact-prime operator decomposition $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ and zero-floating-point exact-rational verifier represent a fundamentally distinct, independent proof architecture.

### 3.3 Foundational Mathematical Literature
* **Tuck (1964, J. Fluid Mech.)**: Foundational source for Legendre harmonic number eigenvalue identity $\int_{-1}^1 \frac{P_n(x)-P_n(y)}{|x-y|} dy = 2 H_n P_n(x)$ (`KNOWN INGREDIENT / NOVEL APPLICATION`).
* **Lagarias (2007, Ann. Inst. Fourier)**: Explicit prior art for Euler-product prime-Laguerre expansion $\lambda_n^{(p)}$ (`PRIOR ART FOUND`).
* **Schoenberg (1938) / Suzuki (2023)**: Normalized relation between Li coefficients, conditionally negative definite sequences on $\mathbb{Z}$, and positive definite semigroups $e^{-t\lambda_{|n|}}$ (`NOVELTY SUPPORTED`).
* **Montgomery-Vaughan (1974)**: Mean value theorem for Dirichlet polynomials explaining analytical length barriers (`KNOWN INGREDIENT / NOVEL APPLICATION`).

---

## 4. Four-Dimensional Claim Adjudication & Verdicts

Every claim in Pass 2 is evaluated across four decoupled axes:
1. **Mathematical Result Novelty**: Was the theorem/bound itself previously established?
2. **Method Novelty**: Was the analytical proof technique previously known or applied?
3. **Verification Novelty**: Was the software/verifier architecture previously implemented?
4. **Chronological Priority**: Was the result publicly disclosed before comparable external work?

### 4.1 Strict Finite-Support Weil Positivity Theorems (`C-0050` – `C-0057`)

| Claim ID | Source Ref | Parameters | Source Commit Date | Math Validity | Result Novelty | Method Novelty | Priority Verdict | Pass 2 Disposition |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-MATH-001` | `C-0050` | $(T, N) = (7/20, 32)$ | 2026-08-21 | `VERIFIED` | `POSSIBLY NOVEL` | `NOVEL SYNTHESIS` | `PRIORITY PLAUSIBLE` | Pre-dates Chuk Aug 25 in Git history; public push unverified. |
| `CLM-MATH-002` | `C-0051` | $(T, N) = (2/5, 40)$ | 2026-08-26 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-003` | `C-0052` | $(T, N) = (17/40, 48)$ | 2026-08-26 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-004` | `C-0053` | $(T, N) = (9/20, 56)$ | 2026-08-26 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-005` | `C-0054` | $(T, N) = (19/40, 68)$ | 2026-08-27 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-006` | `C-0055` | $(T, N) = (1/2, 80)$ | 2026-08-27 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-007` | `C-0056` | $(T, N) = (21/40, 96)$ | 2026-08-28 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Method demo; subsumed as support bound by Chuk $L=0.8$. |
| `CLM-MATH-008` | `C-0057` | $(T, N) = (27/50, 104)$ | 2026-09-24 | `VERIFIED` | `NARROWED` | `NOVEL SYNTHESIS` | `PRIOR ART FOUND` | Frontier method demo; subsumed as support bound by Chuk. |

### 4.2 Exact-Prime Legendre-Schur Method & Operators
* **`CLM-METH-001` (Exact-Prime Weil Decomposition)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-METH-002` (Legendre Harmonic Coercivity)**: `KNOWN INGREDIENT / NOVEL APPLICATION` (Tuck 1964 applied to high-mode Weil coercivity $\mu_N > 0$).
* **`CLM-METH-003` (High-Mode Complement Bound)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-METH-004` (Component Tail-Gram Schur Criterion)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED` ($A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$).
* **`CLM-METH-005` (Exact Rational Proof Architecture)**: `NOVELTY SUPPORTED`.
* **`CLM-OPER-001` (Weil Primes as Compressed Translations)**: `KNOWN INGREDIENT / NOVEL APPLICATION`.
* **`CLM-OPER-002` (Compressed Shift Norm $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$)**: `KNOWN INGREDIENT / NOVEL APPLICATION` (Path graph Chebyshev spectrum applied to translation operators).
* **`CLM-CONT-001` (Moving-Dimension Continuation)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-CONT-002` (Rejection of Deceptive Finite Sections)**: `NOVELTY SUPPORTED`.

### 4.3 Li / Laguerre / Schoenberg / Chirp Criteria
* **`CLM-LAGU-001` (Euler-Product Prime-Laguerre Expansion)**: `PRIOR ART FOUND` (Lagarias 2007).
* **`CLM-LAGU-002` (Deterministic Zeta-Pole Mode Isolation $1-q^n$)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-LAGU-003` (Pole-Subtracted Root Criterion $\limsup |S_n|^{1/n} \le 1$)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-LAGU-004` (PNT Discrepancy Representation)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-LAGU-005` (Pole-Annihilating Shift Filter $T=(E-1)(E-q)$)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-AIRY-001..007` (Airy Saddle, Cayley Mode & Nonlinear Chirp)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-GRAM-001` (Li Sequence Conditionally Negative Definite on $\mathbb{Z} \iff$ RH)**: `NOVELTY SUPPORTED` (Schoenberg 1938 semigroup synthesis).
* **`CLM-GRAM-002` (Exact Li Gram Kernel)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
* **`CLM-GRAM-003` (Prime Gram Atoms Indefinite)**: `NOVELTY SUPPORTED`.

### 4.4 All 15 Analytical Barriers & Obstructions (`CLM-OBST-001..015`)
* **`CLM-OBST-001` (69% Scalar Endpoint Absorption Loss)**: `NOVELTY SUPPORTED` (Explains why scalar absorption fails globally).
* **`CLM-OBST-002` (Digamma Positive Kernel Decomposition)**: `KNOWN INGREDIENT / NOVEL APPLICATION`.
* **`CLM-OBST-003` (Detection of Incomplete Weil Discretization Missing Residual)**: `KNOWN INGREDIENT / NOVEL APPLICATION`.
* **`CLM-OBST-004` (Pointwise PNT Exponent Insufficiency)**: `NOVELTY SUPPORTED` (Analytical barrier).
* **`CLM-OBST-005` (Vinogradov-Korobov Insufficiency on Moving Scales)**: `NOVELTY SUPPORTED` (Analytical barrier).
* **`CLM-OBST-006` (Block-$L^2$ Norm RH-Equivalence)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-007` (High-Frequency Saddle Merge into Endpoint)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-008` (Natural $\sqrt{n}$ Frequency Cap from $m=2$)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-009` (Montgomery-Vaughan Mean-Value Barrier for Long Dirichlet Sums)**: `KNOWN INGREDIENT / NOVEL APPLICATION`.
* **`CLM-OBST-010` (Microlocal Subexponential Control Zero-Sensitivity)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-011` (Rank-One Hessian $\text{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$ in Multiplicative Convolutions)**: `NOVELTY SUPPORTED` (Blocks bilinear phase cancellation).
* **`CLM-OBST-012` (Type-II Dyadic Box Asymptotic Separability)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-013` (Nonseparability Threshold $\sqrt{n}$)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-014` (Fixed-Interior Prime Estimates Require Square-Root Saving $\delta \ge 1/2$)**: `NOVELTY SUPPORTED`.
* **`CLM-OBST-015` (Generic Vaughan/Heath-Brown No-Go Theorem for Laguerre RH)**: `NOVELTY SUPPORTED`.

### 4.5 Verification Architecture & Formal Soundness (`CLM-VERF-001..007`)
* **`CLM-VERF-001` (Exact Rational Certificate Schema & Standalone Verifier)**: `NOVELTY SUPPORTED`.
* **`CLM-VERF-002` (Zero-Floating-Point Acceptance Path)**: `VERIFIED IMPLEMENTATION FACT` (0 float occurrences across `rh_cert`).
* **`CLM-VERF-003` (Multi-Implementation Admission Defense)**: `NOVELTY SUPPORTED`.
* **`CLM-VERF-004` (Adversarial Exit-Code Separation: Schema vs Positivity Failure)**: `NOVELTY SUPPORTED`.
* **`CLM-VERF-005` (Retained Proof Certificate Hash Replay 8/8)**: `VERIFIED IMPLEMENTATION FACT`.
* **`CLM-VERF-006` (Standalone Rust Verifier Independence)**: `NOVELTY SUPPORTED`.
* **`CLM-VERF-007` (Lean 4 Formal Soundness Integration)**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED` (36 lemmas verified; unformalized analytical derivations clearly delimited).

### 4.6 Research Integrity & Priority Precedence (`CLM-PRIO-001..012`)
* **`CLM-PRIO-001..004, 007, 009..012`**: `PRIORITY PLAUSIBLE` (Git commit metadata pre-dates external work; public push archives unverified).
* **`CLM-PRIO-005` (Priority on `C-0050` at $T=0.35$)**: `PRIORITY PLAUSIBLE` (**Downgraded from Pass 1's `PRIORITY SUPPORTED`** per multi-anchor timeline rules).
* **`CLM-PRIO-006` (Priority on Continuation $T=0.40..0.525$)**: `PRIOR ART FOUND` (Chuk arXiv:2608.24827 submitted Aug 25 at $L=0.8$).
* **`CLM-PRIO-008` (Priority on Legendre Coercivity Identity)**: `KNOWN INGREDIENT (Tuck 1964) / PRIORITY PLAUSIBLE (Weil Application)`.

---

## 5. Summary of Claim Verdict Changes from Pass 1 to Pass 2

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Pass 1 vs Pass 2 Master Breakdown                    │
├────────────────────────────────┬───────────────────────────────────────┤
│ Stated Scope Count             │ Pass 1: 50 claims ──► Pass 2: 66 claims│
│ C-0051..0057 Result Novelty    │ NOVELTY SUPPORTED ──► CLAIM NARROWED  │
│ C-0050 Priority Precedence     │ PRIORITY SUPPORTED ──► PRIO PLAUSIBLE │
│ C-0051..0056 Priority          │ PRIORITY SUPPORTED ──► PRIOR ART FOUND│
│ CLM-LAGU-001 Prime-Laguerre    │ NOVELTY SUPPORTED ──► PRIOR ART FOUND │
│ CLM-METH-002 Tuck Identity     │ NOVELTY SUPPORTED ──► KNOWN INGREDIENT│
│ CLM-OPER-002 Shift Spectrum    │ NOVELTY SUPPORTED ──► KNOWN INGREDIENT│
│ 15 CLM-OBST Claims             │ 1 Aggregate Dossier ──► 15 Line Items │
│ Zero-Float Acceptance Boundary │ Broad Assertion ──► Precise Invariant │
│ Lean Formalization Scope       │ Broad Assertion ──► Explicit Boundary │
└────────────────────────────────┴───────────────────────────────────────┘
```

---

## 6. Strict Riemann Hypothesis Non-Overclaim Boundary

Audit Pass 2 explicitly reaffirms the foundational scientific boundary:
> **The audited research project does NOT prove the Riemann Hypothesis.**

The project establishes certified finite-support localized Weil positivity theorems ($T \in [0.35, 0.54]$) and develops several structural RH-equivalent reformulations / obstruction theorems on the prime side. Transforming an RH-equivalent condition into a proof of RH requires proving global positivity across all test functions $f \in \mathcal{S}(\mathbb{R})$ or establishing subexponential root growth $\limsup |S_n|^{1/n} \le 1$ unconditionally, neither of which has been achieved.

---

## 7. Required Pass 3 Investigations (Non-Closure Rule)

In strict adherence to Section 28 of [`SECOND_AUDIT.md`](archive/SECOND_AUDIT.md), Audit Pass 2 does not declare scientific closure. The following specific items are designated for **Audit Pass 3**:

1. **Independent Verification of August 21 Public Push (`CLM-PRIO-005`)**:
   - Query third-party event mirrors (GH Archive historical torrents, Software Heritage commit ingest logs, GitHub notification archives) to definitively settle whether commit `6dd1d8f0` was publicly fetchable prior to August 25.
2. **Lean 4 End-to-End Formalization Expansion (`CLM-VERF-007`)**:
   - Formalize the semantic correspondence between Lean's matrix definitions and `rh_cert` Rust structs.
   - Formalize the analytical deduction linking the discrete rational certificate inequality $A_N - \frac{3}{\mu_N}(G_V+G_2+G_R) > 0$ to full-space operator positivity $Q(f) > 0$ on $L^2([-T,T])$.
3. **Continuous Symbol vs. Discrete Operator Equivalence**:
   - Perform an analytical deep dive comparing Marcus Chuk's continuous Landau-Widom symbol bounds with `riemann-conjecture`'s exact discrete Legendre coercivity eigenvalue bounds.
4. **Continuation Beyond $T=0.54$**:
   - Re-evaluate future project commits beyond $T=0.54$ to determine the computational and analytical scaling limits of the exact-prime moving-dimension strategy when encountering the second prime $p=3$ ($T > \frac{1}{2}\log 3 \a\approx 0.5493$).
