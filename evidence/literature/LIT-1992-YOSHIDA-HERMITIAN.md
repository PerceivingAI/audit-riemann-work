# Primary Literature Dossier: Hiroyuki Yoshida (1992)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-1992-YOSHIDA-HERMITIAN`  
> * **Title**: *On Hermitian forms attached to zeta functions*  
> * **Authors**: Hiroyuki Yoshida  
> * **Publication**: *Zeta Functions in Geometry*, Advanced Studies in Pure Mathematics, Vol. 21 (1992), pp. 281–325  
> * **DOI / Stable URL**: [`10.2969/aspm/02110281`](https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/Zeta-Functions-in-Geometry/chapter/On-Hermitian-Forms-attached-to-Zeta-Functions/10.2969/aspm/02110281.pdf)  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-MATH-001`, `CLM-METH-001`, `CLM-PRIO-004`.

---

## 1. Primary Mathematical Theorems

In this foundational paper, Yoshida constructs and analyzes the explicit-formula Hermitian/quadratic form for the Riemann zeta function and general automorphic $L$-functions.

### 1.1 Theorem 1 (p. 310): Prime-Free Compact Positivity
Yoshida establishes that for the Riemann zeta function, the explicit-formula quadratic form $H(f)$ (in the pole-inclusive normalization) is strictly positive definite on the space of test functions supported in the prime-free compact window:
$$\text{supp} f \subseteq [-a, a], \qquad a \le \frac{1}{2}\log 2 \approx 0.34657359$$
* **Proof Method**: 200-mode Fourier series expansion on the interval $[-a, a]$ with rigorous analytical error bounds on the truncation remainder.
* **Significance**: First unconditional rigorous proof of compact Weil positivity beyond the trivial point $a=0$.

### 1.2 Proposition 6 & Theorem 2: Failure Thresholds & Nondegeneracy
* **Proposition 6**: Analyzes the failure threshold $a^* = \sup \{a : H \text{ is positive semidefinite on } [-a, a]\}$.
* **Theorem 2**: Establishes that the Riemann Hypothesis is equivalent to the non-degeneracy / positive definiteness of the Hermitian form for all $a > 0$.

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Dimension | H. Yoshida (1992) | `riemann-conjecture` (`CLM-MATH-001..008`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Support Window** | $a \le \frac{1}{2}\log 2 \approx 0.34657$ (Prime-Free Window). | $T = 0.35 \dots 0.54$ ($T > \frac{1}{2}\log 2$, First Prime $p=2$ Active). | `riemann-conjecture` proves positivity **beyond the prime-free threshold** ($0.35 > 0.34657$). |
| **First-Prime Handling** | Inactive (support strictly excludes $\log 2$). | Explicit active compressed translation operator $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$. | `riemann-conjecture` addresses the first prime power analytically. |
| **Proof Architecture** | 200-mode Fourier discretization + error bounds. | Exact-prime Legendre decomposition + Tuck coercivity + 3-factor Schur complement. | **Distinct proof architectures**. |

---

## 3. Disposition & Novelty Verdict

* **Disposition**: `WEAKER RESULT / SAME PHENOMENON`. Yoshida (1992) establishes unconditional compact positivity up to $a = \frac{1}{2}\log 2$.
* **Audit Impact**: `riemann-conjecture`'s $T=0.35$ theorem (`CLM-MATH-001`) exceeds Yoshida's support bound ($0.35 > 0.34657$), representing the entry into the active-prime regime.
