# Literature & Repository Dossier: LIT-2026-KUBER-HISTORY

> **Comparator Metadata**  
> * **Dossier ID**: `LIT-2026-KUBER-HISTORY`  
> * **Target Repository**: `https://github.com/Kuberwastaken/riemann`  
> * **Author / Principal**: Kuber Mehta  
> * **First Public Release**: `2026-07-23` (Citation CFF)  
> * **Standard**: Deep Commit & Chronological Module Audit per [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md)

---

## 1. Overview & Repository Architecture

`Kuberwastaken/riemann` is an open-access public research repository compiling an annotated bibliography of 178 primary sources on the Riemann Hypothesis alongside computational experiments investigating localized Weil positivity located under `experiments/weil_positivity/`.

### Key Repository Modules & Files:
* `CITATION.cff`: Release date `2026-07-23`, identifying Kuber Mehta as author.
* `FINDINGS.md`: Consolidated experimental conclusions, noting explicit caveat that the repo proves no new mathematics about RH.
* `experiments/weil_positivity/PROOF-c0.md`: Certified lower bound $c_0 \ge 0.349152$ on the continuous archimedean coercivity form.
* `experiments/weil_positivity/certify.py` / `certify_L045.py`: Python script utilizing Arb interval ball arithmetic (`flint.arb`) and certified Cholesky decomposition to verify positive definiteness of truncated finite-dimensional subspaces.
* `experiments/weil_positivity/rescue_certify.py`: 22-dimensional subspace certificate at $L = 0.62$ demonstrating arithmetic rescue where prime terms rescue negative archimedean forms.
* `logs/LOG.md`: Experiment journal recording Odlyzko zero validation errors ($10^{-5}$–$10^{-7}$) and numerical Rayleigh quotients.
* `UPDATES.md`: Technical distinction between finite-dimensional verified test families and full-space $L^2([-T, T])$ theorems.

---

## 2. Chronological & Commit Evolution Analysis

```text
2026-07-23 (Release) ────► 2026-08-05 (Arb Certs) ────► 2026-08-20 (Rescue) ────► 2026-09-01 (Updates)
Initial Archive &         Finite-Dimensional         Arithmetic Rescue          Full-Space Boundary
Bibliographies            L=0.45..0.60 Subspaces      22D Subspace at L=0.62     Spectral Caps Open
```

### 2.1 Chronological Development of Comparable Constructions:
1. **July 23, 2026 (`Initial Release`)**:
   - Comprehensive literature collection established.
   - Core problem identified: numerical Weil quadratic form evaluation on compact support.
2. **August 5, 2026 (`Finite-Dimensional Arb Certification`)**:
   - Introduction of `certify.py` using Arb ball arithmetic.
   - Certified positive definiteness for finite-dimensional subspaces (e.g. 14-dimensional subspace at $L=0.45$, yielding $W(f) \ge 0.072606 \|f\|^2$).
3. **August 20, 2026 (`Arithmetic Rescue Demonstration`)**:
   - Demonstration in `rescue_certify.py` that at $L=0.62$, the continuous archimedean form is strictly negative, but addition of prime powers $p \le 13$ restores positive definiteness on a 22-dimensional test subspace.
4. **September 1, 2026 (`Boundary Delimitation in UPDATES.md`)**:
   - `UPDATES.md` explicitly addresses the gap between finite-dimensional numerical verification and full-space theorems:
     > *"Finite-dimensional certified results prove positivity only on the tested subspace. Turning the $L=0.40$ pilot into an unconditional full-space theorem requires certifying the high-frequency spectral caps, which remain open."*

---

## 3. Mathematical Normalization & Comparative Matrix

| Mathematical Feature | `Kuberwastaken/riemann` (Kuber Mehta) | `PerceivingAI/riemann-conjecture` (`C-0050..0057`) | Comparative Audit Finding |
| :--- | :--- | :--- | :--- |
| **Theorem Scope** | **Finite-Dimensional Subspaces Only** | **Full Space $L^2([-T, T])$ Unconditional Theorems** | Fundamental distinction: Kuber leaves infinite-dimensional tails uncertified; `riemann-conjecture` proves full-space theorems. |
| **High-Mode Tail Bound** | Uncertified (Spectral caps open in `UPDATES.md`) | **Exact Legendre Harmonic Coercivity** $J(q) \ge H_N \|q\|_2^2$ | `riemann-conjecture` uses Tuck's identity to rigorously bound all orthogonal modes $n > N$. |
| **First-Prime Handling** | Discrete sum over prime evaluations | **Thresholded Compressed Translation Operator** $P_2 = -rac{\log 2}{\sqrt{2}} S_{T, \log 2}$ | Analytical operator isolation with exact norm $\|S_{T,a}\| = 2\cosrac{\pi}{L+1}$. |
| **Reduction Method** | Direct certified Cholesky on finite grid | **3-Factor Tail-Gram Schur Reduction** $A_N - rac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ | Rigorous analytic reduction from infinite-dimensional operator to finite matrix inequality. |
| **Verification Engine** | Python + Arb ball interval floating-point | **Zero-Floating-Point Standalone Rust Verifier** (`rh_cert`, `BigRational`) | Distinct exact rational certificate architecture. |
| **Formalization** | Lean exploratory scripts | **Lean 4 Verified Soundness Lemmas** (`LDL.lean`, `Interval.lean`, etc.) | Standalone machine-checked algebraic lemmas. |

---

## 4. Audit Adjudication Impact

1. **Prior Art Boundary**: `Kuberwastaken/riemann` established public prior art on **finite-dimensional numerical Weil positivity experiments** on July 23, 2026.
2. **Non-Anticipation of Full-Space Theorems**: It did **not** anticipate or invalidate `riemann-conjecture`'s full-space theorems (`C-0050..0057`), exact Legendre harmonic coercivity (`CLM-METH-002`), or exact-prime component Schur reductions (`CLM-METH-004`), because it explicitly left infinite-dimensional tail bounds uncertified.
