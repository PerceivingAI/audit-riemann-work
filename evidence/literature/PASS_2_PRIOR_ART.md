# Pass 2 Comparative Prior Art & Literature Baseline Dossier

> **Dossier Metadata**  
> * **Document Initialized**: `2026-09-24T20:45:00Z` (Pass 2 Phase 1)  
> * **Standard**: 4-Dimensional Prior Art Evaluation per [`SECOND_AUDIT.md`](../../archive/SECOND_AUDIT.md)  
> * **Scope**: Comprehensive analysis of mandatory comparators (`Kuberwastaken/riemann`, Marcus Chuk `arXiv:2608.24827`) and primary mathematical literature.

---

## 1. Mandatory Comparator I: `Kuberwastaken/riemann` (Kuber Mehta, July 2026)

```yaml
id: "COMP-2026-KUBER"
repository: "https://github.com/Kuberwastaken/riemann"
author: "Kuber Mehta"
release_date: "2026-07-23"
license: "MIT / Open Access Research Archive"
```

### 1.1 Ingestion & Technical Architecture
`Kuberwastaken/riemann` is an open research archive compiling 178 primary sources on the Riemann Hypothesis alongside computer-assisted numerical experiments on localized Weil positivity located under `experiments/weil_positivity/`.

Key structural components include:
* **Archimedean Coercivity Bound**: Certified lower bound $c_0 \ge 0.349152$ on the continuous archimedean component.
* **Finite-Dimensional Positivity Verification**: Computer-assisted Arb ball arithmetic verifying positive definiteness for truncated finite-dimensional subspaces at $L = 0.45, 0.50, 0.545, 0.60$.
* **Arithmetic Rescue Demonstration**: A 22-dimensional numerical subspace at $L = 0.62$ demonstrating that the negative archimedean form is rescued by prime contributions.

### 1.2 Mathematical Normalization & Comparative Matrix

| Technical Feature | `Kuberwastaken/riemann` (July 2026) | `PerceivingAI/riemann-conjecture` (Aug–Sep 2026) | Mathematical Significance |
| :--- | :--- | :--- | :--- |
| **Theorem Scope** | **Finite-Dimensional Subspaces Only** | **Full Space $L^2([-T, T])$ Unconditional Theorems** | Crucial mathematical distinction. Kuber's repo leaves infinite-dimensional tail bounds uncertified. |
| **High-Mode Tail Control** | None (Acknowledged in `UPDATES.md`) | **Exact Legendre Harmonic Coercivity** $J(q) \ge H_N \|q\|_2^2$ | `riemann-conjecture` proves coercivity for all orthogonal complement modes $n > N$. |
| **Prime-Entry Formulation** | Global discrete evaluation on test grid | **Thresholded Compressed Translation Operator** $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ | Analytical operator isolation allowing closed spectral norms $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$. |
| **Reduction Strategy** | Direct certified Cholesky on finite matrix | **3-Factor Component Tail-Gram Schur Reduction** $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ | Converts infinite-dimensional problem to finite matrix inequality with rigorous tail margin. |
| **Arithmetic Precision** | Arb ball interval floating-point | **Exact Arbitrary-Precision Rational** (`BigRational` via `rh_cert`) | Zero-floating-point verifier execution. |
| **Formal Soundness** | Partial Lean exploration | **Lean 4 Formal Proofs** (`LDL.lean`, `Gershgorin.lean`, `Interval.lean`) | Standalone verification theorems. |

### 1.3 Adjudication Impact
`Kuberwastaken/riemann` represents important contemporaneous prior exploratory work on finite-dimensional numerical Weil positivity, but **does not anticipate or invalidate** `riemann-conjecture`'s full-space theorems (`C-0050..C-0057`), exact Legendre harmonic coercivity method (`CLM-METH-002`), or exact-prime Schur reduction architecture (`CLM-METH-004`).

---

## 2. Mandatory Comparator II: Marcus Chuk (`arXiv:2608.24827`, August 25, 2026)

```yaml
id: "COMP-2026-CHUK"
title: "Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law"
author: "Marcus Chuk"
venue: "arXiv:2608.24827 [math.NT]"
submission_date: "2026-08-25T11:42:00Z"
```

### 2.1 Technical Architecture
Marcus Chuk establishes the first unconditional computer-assisted full-space certificate of Weil positivity on compact support $L = 0.8$ (autocorrelation support width $1.6$):
$$Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2 \qquad \forall f \in L^2([-0.8, 0.8]).$$

Key mathematical techniques:
* **Discretization**: Modal expansion on Legendre polynomials using Gauss-Legendre quadrature and spherical Bessel recurrences.
* **Tail Control**: Discretization error bounded via continuous symbol pointwise decay envelopes.
* **Certificate Engine**: Floating-point interval arithmetic matrix enclosure.

### 2.2 Comparative Matrix with `riemann-conjecture`

| Dimension | Marcus Chuk (`arXiv:2608.24827`) | `riemann-conjecture` (`C-0050..C-0057`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Support Parameter** | $L = 0.8$ ($[-0.8, 0.8]$) | $T = 0.35 	o 0.54$ ($[-T, T]$) | Chuk proves positivity on a wider support domain than the project's frontier $T=0.54$. |
| **Proof Architecture** | Full numerical matrix discretization + continuous envelope | Exact-prime operator decomposition + Tuck harmonic coercivity + Schur complement | **Two fundamentally different proof architectures.** |
| **First-Prime Handling** | Embedded in global symbol quadrature | Explicit rank/shift decomposition of $p=2$ operator | `riemann-conjecture` isolates analytical prime geometry. |
| **Verification Engine** | Interval arithmetic floating-point | Standalone zero-floating-point exact rational Rust verifier (`rh_cert`) | Distinct verification paradigms. |
| **Priority vs. C-0050** | August 25, 2026 (Public arXiv) | August 21, 2026 (`6dd1d8f0` Git commit) | Pre-dates Chuk in local Git commit; public push verification evaluated in Phase 4. |
| **Priority vs. C-0051..C-0057** | August 25, 2026 (Public arXiv) | August 26–September 24, 2026 | Chuk's theorem post-dates `C-0050`, but pre-dates `C-0051..C-0057`. |

### 2.3 Adjudication Impact
* **Mathematical Result Novelty**: Chuk's public August 25 theorem at $L=0.8$ established compact Weil positivity beyond the prime-free threshold ($T > \frac{1}{2}\log 2 \approx 0.34657$). Therefore, project continuation points $T \in [0.40, 0.54]$ registered after August 25 (`C-0051..C-0057`) are **valid certified demonstrations of the exact-prime method**, but are mathematically subsumed by Chuk's wider support bound.
* **Method & Software Novelty**: `riemann-conjecture`'s exact-prime Legendre-Schur synthesis and zero-floating-point exact rational verifier remain **fully independent and novel methodologies**.

---

## 3. Foundational Literature Normalization

### 3.1 Legendre Harmonic Coercivity & Tuck's Identity (1964)
* **Primary Citation**: E. O. Tuck, *Some methods for flows past blunt slender bodies*, J. Fluid Mech. 18(4), 619–635 (1964).
* **Identity**: $\int_{-1}^1 \frac{P_n(x)-P_n(y)}{|x-y|} dy = 2 H_n P_n(x)$.
* **Classification**: `KNOWN INGREDIENT / NOVEL APPLICATION`. Tuck's 1964 identity is the foundational mathematical ingredient; applying it to establish high-mode Weil positivity coercivity $\mu_N > 0$ is an original synthesis.

### 3.2 Li / Laguerre Formulations & Lagarias Baseline (2007)
* **Primary Citation**: J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Ann. Inst. Fourier 57(5), 1689–1740 (2007).
* **Classification**:
  - Euler-product prime-Laguerre expansion $\lambda_n^{(p)}$: `PRIOR ART FOUND` (Lagarias 2007).
  - Exact deterministic pole mode extraction $1-q^n$ and shift filter $T=(E-1)(E-q)$: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.

### 3.3 Li Coefficients as Conditionally Negative Definite (Schoenberg 1938)
* **Primary Citations**:
  - I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44(3), 522–536 (1938).
  - K. Gröchenig, *Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function*, arXiv:2007.12889 (2020).
  - M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. (2023).
* **Classification**: `NOVELTY SUPPORTED`. While Schoenberg established the equivalence between conditionally negative definite sequences and positive definite semigroups $e^{-t\psi}$, applying this to $\psi(n)=\lambda_{|n|}$ on $\mathbb{Z}$ as an RH criterion is original.

### 3.4 Multiplicative Bilinear Phase Barriers & Montgomery-Vaughan (1974)
* **Primary Citations**:
  - H. L. Montgomery & R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (1974).
* **Classification**: `NOVELTY SUPPORTED`. Proving that the Hessian matrix of the phase function in multiplicative prime convolutions has rank 1 ($\text{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$) rigorously establishes why Type-II Vaughan/Heath-Brown sums are asymptotically separable and cannot beat the $\delta \ge 1/2$ square-root barrier.
