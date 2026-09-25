# Primary Literature Dossier: Connes, Consani, Moscovici (2025)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-2025-CCM-SPECTRAL`  
> * **Title**: *Zeta Spectral Triples*  
> * **Authors**: Alain Connes, Caterina Consani, Henri Moscovici  
> * **Preprint**: `arXiv:2511.22755` (Submitted `2025-11-27T21:01:11Z`, 34 pages)  
> * **DOI**: [`10.48550/arXiv.2511.22755`](https://doi.org/10.48550/arXiv.2511.22755)  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-MATH-001..008`, `CLM-VERF-007`.

---

## 1. Primary Mathematical Framework

CCM construct self-adjoint operators $D_{\log}^{(\lambda, N)}$ obtained as rank-one perturbations of the spectral triple associated with the scaling operator on the interval $[\lambda^{-1}, \lambda]$ ($\lambda = e^L$).

### 1.1 Theorem 1.1 (Spectral Triples on Finite Sections)
Let $QW_\lambda^N$ denote the restriction of the Weil quadratic form to the span of the $2N+1$ lowest scaling-operator eigenfunctions $V_n$ on $[\lambda^{-1}, \lambda]$. Assuming:
1. The lowest eigenvalue $\varepsilon_N$ of $QW_\lambda^N$ is **simple**.
2. The corresponding eigenfunction $\xi$ is **even** (invariant under $u \mapsto u^{-1}$).

Then $D_{\log}^{(\lambda, N)} := D_{\log}^{(\lambda)} - |D_{\log}^{(\lambda)}\xi\rangle\langle\delta_N|$ is self-adjoint on $E'_N \oplus E_N^\perp$, and its regularized determinant satisfies:
$$\operatorname{det}_{\mathrm{reg}}(D_{\log}^{(\lambda, N)} - z) = -i \lambda^{-iz} \hat{\xi}(z)$$
whose zeros are all real.

### 1.2 Open Convergence Obstacles (§7–8)
* **Obstacle (a)**: Proving that for all $(\lambda, N)$, $\varepsilon_N$ is simple with even eigenvector.
* **Obstacle (b)**: Proving that the ground state $\xi_\lambda$ converges to the prolate surrogate $k_\lambda$ uniformly on substrips as $\lambda \to \infty$.

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Technical Dimension | Connes, Consani, Moscovici (2025) | `riemann-conjecture` (`51feb3d`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Primary Goal** | Constructing spectral triples whose eigenvalues converge to zeros of $\zeta(1/2+is)$. | Establishing certified localized Weil positivity theorems on compact windows $T \le 0.54$. | Complementary mathematical programs. |
| **Finite Reduction** | Galerkin truncation $QW_\lambda^N$ on periodic exponential basis. | Component tail-Gram Schur criterion $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ on Legendre polynomial basis. | **Distinct discretization and reduction frameworks**. |
| **Verification Engine** | Analytical operator theory + heuristic numerics. | Zero-floating-point standalone Rust verifier (`rh_cert`) + Lean 4 formal soundness lemmas. | Exact rational certification vs. theoretical operator construction. |

---

## 3. Disposition & Novelty Verdict

* **Disposition**: `DIFFERENT FUNCTION SPACE / OPERATOR FRAME`. CCM (2025) provides the spectral triple operator-theoretic program for zeta zeros.
* **Audit Impact**: `riemann-conjecture`'s localized positivity theorems on $T \in [0.35, 0.54]$ represent finite-support certificates on physical intervals, independent of CCM's spectral triple convergence program.
