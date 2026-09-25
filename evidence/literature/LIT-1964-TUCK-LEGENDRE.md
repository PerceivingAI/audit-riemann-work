# Primary Literature Dossier: E. O. Tuck (1964)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-1964-TUCK-LEGENDRE`  
> * **Title**: *Some methods for flows past blunt slender bodies*  
> * **Authors**: E. O. Tuck  
> * **Publication**: *Journal of Fluid Mechanics*, Vol. 18, Issue 4 (1964), pp. 619–635  
> * **DOI**: [`10.1017/S0022112064000453`](https://doi.org/10.1017/S0022112064000453)  
> * **Governing Protocol**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-METH-002`, `CLM-METH-003`, `CLM-PRIO-008`.

---

## 1. Primary Mathematical Identity

In Section 2 (p. 624, Equation 2.12), Tuck establishes the singular integral eigenvalue identity for Legendre polynomials $P_n(x)$ on the interval $[-1, 1]$:
$$\int_{-1}^1 \frac{P_n(x) - P_n(y)}{|x - y|} \, dy = 2 H_n P_n(x)$$
where $H_n = \sum_{k=1}^n \frac{1}{k}$ is the $n$-th harmonic number ($H_0 = 0$).

### 1.1 Normalization & Integral Operator Form
The logarithmic Dirichlet quadratic form associated with this singular kernel is:
$$J(w) = \frac{1}{4}\int_{-1}^1 \int_{-1}^1 \frac{|w(x) - w(y)|^2}{|x - y|} \, dx \, dy$$
Because the Legendre polynomials $P_n(x)$ form an orthogonal basis of $L^2[-1, 1]$ with $\|P_n\|_2^2 = \frac{2}{2n+1}$, applying Tuck's identity yields the exact diagonal form:
$$J(P_n) = H_n \|P_n\|_2^2$$

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Technical Aspect | E. O. Tuck (1964) | `riemann-conjecture` (`CLM-METH-002`, `CLM-METH-003`) | Audit Evaluation |
| :--- | :--- | :--- | :--- |
| **Domain / Field** | Fluid dynamics (slender body aerodynamics). | Number theory / Weil quadratic form positivity on $[-T, T]$. | Application to Weil positivity is completely outside Tuck's context. |
| **Eigenvalue Identity** | $J(P_n) = H_n \|P_n\|_2^2$ on $[-1, 1]$. | Coordinate-scaled identity $J(P_n) = H_n \|P_n\|_2^2$ on normalized interval. | **Identical mathematical identity** (`PRIOR ART FOUND` on formula alone). |
| **High-Mode Coercivity** | None (used for aerodynamic drag calculations). | High-mode orthogonal complement bound: $\mu_N = H_N - c_T - c_2 - \rho_R > 0$ for $n \ge N$. | **Novel analytical synthesis** (`KNOWN INGREDIENT / NOVEL APPLICATION`). |

---

## 3. Disposition & Novelty Verdict

* **Formula Status**: `PRIOR ART FOUND` (Tuck 1964).
* **Application Status**: `KNOWN INGREDIENT / NOVEL APPLICATION`. Using Tuck's harmonic number identity to establish uniform spectral coercivity for high-mode orthogonal complements in localized Weil positivity is an original analytical synthesis not present in prior literature.
