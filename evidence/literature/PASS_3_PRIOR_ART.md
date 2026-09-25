# Master Prior Art & Comparator Baseline Dossier — Audit Pass 3

> **Dossier Metadata**  
> * **Document Type**: Comprehensive External Literature & Repository Baseline  
> * **Audit Pass**: `Pass 3 (WS-05 & WS-06)`  
> * **Effective Date**: `2026-09-24T22:55:00Z`  
> * **Governing Standard**: [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md) & [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md)

---

## 1. Executive Summary

This dossier consolidates the normalized mathematical and methodological baseline across all contemporary comparators and historical literature relevant to the independent audit of `PerceivingAI/riemann-conjecture`.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                     Prior Art Baseline Architecture                    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Contemporary Comparator: Kuber Mehta (July 2026, Finite-Dim Arb)    │
│ 2. Contemporary Comparator: Marcus Chuk (August 2026, Full-Space L=0.8)│
│ 3. Foundational Coercivity: E. O. Tuck (1964, Legendre Harmonic Id.)   │
│ 4. Foundational Li Theory:  J. C. Lagarias (2007, Prime-Laguerre Exp.) │
│ 5. Foundational Semigroups: I. J. Schoenberg (1938, CND Sequences)     │
│ 6. Foundational Barriers:   Montgomery & Vaughan (1974, Mean Value)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Comparator Summary & Structural Mapping

### 2.1 Kuber Mehta (`Kuberwastaken/riemann`, July 23, 2026)
* **Status**: Public GitHub Research Archive.
* **Findings**: Certified finite-dimensional subspaces ($L=0.45..0.62$) using Arb ball arithmetic; infinite-dimensional spectral tail bounds left uncertified (`UPDATES.md`).
* **Audit Impact**: Validates that numerical localized Weil positivity was actively studied, but does not anticipate full-space theorems or exact-prime Schur methods. Full history documented in [`LIT-2026-KUBER-HISTORY.md`](LIT-2026-KUBER-HISTORY.md).

### 2.2 Marcus Chuk (`arXiv:2608.24827`, August 25, 2026)
* **Status**: Unconditional computer-assisted full-space certificate at $L=0.8$.
* **Findings**: $Q(f) \ge 8.9 	imes 10^{-18} \|f\|_2^2$ on $L^2([-0.8, 0.8])$. Discretized via Gauss-Legendre quadrature with continuous Fourier decay envelopes.
* **Audit Impact**: Subsumes mathematical support result novelty for project continuation points $T \in [0.40, 0.54]$ committed post-August 25 (`C-0051..C-0057`). Confirms distinct proof architecture. Full dossier in [`LIT-2026-CHUK-V2.md`](LIT-2026-CHUK-V2.md).

---

## 3. Foundational Primary Literature Mapping

### 3.1 Legendre Harmonic Coercivity & Tuck's Identity (1964)
* **Citation**: E. O. Tuck, *Some methods for flows past blunt slender bodies*, J. Fluid Mech. 18(4), 619–635 (1964), DOI: `10.1017/S0022112064000453`.
* **Mathematical Statement**: $\int_{-1}^1 rac{P_n(x)-P_n(y)}{|x-y|} dy = 2 H_n P_n(x)$, where $H_n = \sum_{k=1}^n 1/k$.
* **Project Mapping**: Scaled to $[-T, T]$, yielding singular operator eigenvalues $\lambda_n = 2 H_n$ and lower coercivity bound $J(q) \ge H_N \|q\|_2^2$.
* **Adjudication**: `KNOWN INGREDIENT / NOVEL APPLICATION` (Tuck 1964).

### 3.2 Prime-Laguerre Expansions & Lagarias Baseline (2007)
* **Citation**: J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Ann. Inst. Fourier 57(5), 1689–1740 (2007).
* **Mathematical Statement**: $\lambda_n^{(p)} = -A \sum_{m \ge 2} \Lambda(m) m^{-s_0} L_{n-1}^{(1)}(A \log m)$.
* **Project Mapping**: Identical expansion in `CLM-LAGU-001`.
* **Adjudication**: `PRIOR ART FOUND` (Lagarias 2007).

### 3.3 Li Coefficients & Schoenberg Conditionally Negative Definite Sequences (1938)
* **Citations**:
  - I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44(3), 522–536 (1938).
  - M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 107(4), 1363–1396 (2023).
* **Mathematical Statement**: A function $\psi$ on a group $G$ is conditionally negative definite iff $e^{-t\psi}$ is positive definite for all $t > 0$.
* **Project Mapping**: Identifying $\psi(n) = \lambda_{|n|}$ as conditionally negative definite on $\mathbb{Z} \iff 	ext{RH}$.
* **Adjudication**: `NOVEL SYNTHESIS SUPPORTED` (Schoenberg 1938 synthesis).

### 3.4 Multiplicative Convolutions & Bilinear Phase Rank-One Hessians
* **Citations**:
  - H. L. Montgomery & R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (1974).
  - D. R. Heath-Brown, *Prime numbers in short intervals...*, Can. J. Math. (1982).
* **Mathematical Statement**: In multiplicative convolutions $(u, v) \mapsto \Phi_n(u+v)$, $	ext{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$ has rank 1.
* **Project Mapping**: Proves Type-II dyadic bilinear sums are asymptotically separable and cannot beat the $\delta \ge 1/2$ square-root barrier.
* **Adjudication**: `NOVELTY SUPPORTED` (Original structural barrier).
