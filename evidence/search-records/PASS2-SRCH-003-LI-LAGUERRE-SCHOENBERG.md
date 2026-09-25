# Pass 2 Search Record: PASS2-SRCH-003-LI-LAGUERRE-SCHOENBERG

> **Search Execution Metadata**  
> * **Search ID**: `PASS2-SRCH-003-LI-LAGUERRE-SCHOENBERG`  
> * **Date Executed**: `2026-09-24T20:35:00Z`  
> * **Auditor / Scope**: Li Coefficients, Schoenberg Semigroups, Shift Filters & Chirp Formulations  
> * **Databases Queried**: arXiv (math.NT, math.CA), MathSciNet, zbMATH, Wiley Online Library, Google Scholar

---

## 1. Query Formulations & Findings

### Topic 1: Li Coefficients & Schoenberg Conditional Negative Definiteness
* **Query**: `"Li coefficients" "conditionally negative definite" OR "negative definite" OR "Schoenberg" OR "Herglotz" "Riemann"`
* **Findings**:
  - Li (1997), Bombieri–Lagarias (1999), Lagarias (2007) establish $	ext{RH} \iff \lambda_n \ge 0$.
  - Gröchenig (2020, arXiv:2007.12889) relates RH to Schoenberg's theory of *totally positive functions* (minors of Toeplitz kernels), not conditional negative definiteness.
  - Suzuki (2023, J. London Math. Soc.) connects screw functions to Hermitian positive-semidefinite forms and Li moments.
  - The specific statement in `CLM-GRAM-001` that $\psi(n) = \lambda_{|n|}$ is conditionally negative definite on $\mathbb{Z}$ iff RH (and therefore $e^{-t\lambda_{|n|}}$ is positive definite for all $t > 0$ via Schoenberg 1938) represents a **novel structural characterization** connecting Li's criterion to Schoenberg metric embeddings and Herglotz/Bochner semigroups on $\mathbb{Z}$.

### Topic 2: Deterministic Pole Mode & Shift Filter
* **Query**: `"Li coefficients" "pole" "shift operator" OR "E-1" OR "Laguerre" "discrepancy"`
* **Findings**:
  - Euler-product prime-Laguerre expansion $\lambda_n^{(p)}$ is known from Lagarias (2007) (`LIT-2007-LAGARIAS-LICAE`).
  - Isolating the exact geometric progression $1 - q^n$ ($q = -s_0/(s_0-1)$) produced by the $\zeta(s)$ pole at $s=1$ and designing the second-order shift filter $T = (E-1)(E-q)$ to annihilate the pole while strictly preserving the RH root-growth criterion $\limsup |S_n|^{1/n} \le 1$ is original to `riemann-conjecture`.
  - **Verdict**: `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`.
