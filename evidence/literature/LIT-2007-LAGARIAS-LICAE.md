# Literature Dossier: LIT-2007-LAGARIAS-LICAE

```yaml
id: "LIT-2007-LAGARIAS-LICAE"
title: "Li Coefficients for Automorphic L-Functions"
authors: ["Jeffrey C. Lagarias"]
year: 2007
venue: "Annales de l'Institut Fourier 57 (2007), no. 5, 1689–1740"
doi: "10.5802/aif.2311"
license: "Open Access (Numdam)"
```

---

## 1. Summary of Work

Jeffrey C. Lagarias generalizes the Li criterion to automorphic $L$-functions and constructs explicit test functions for the Weil explicit formula.

### Key Mathematical Content
* Proves that the test polynomials in the Li criterion are generalized Laguerre polynomials:
  $$P_n(x) = \sum_{j=1}^n \binom{n}{j} \frac{x^{j-1}}{(j-1)!} = L_{n-1}^{(1)}(-x).$$
* Establishes the relationship between Li coefficients and Weil quadratic forms.
* Develops asymptotics of Li coefficients for principal automorphic $L$-functions.

---

## 2. Comparison with `riemann-conjecture` Repository

| Concept | Lagarias (2007) | `riemann-conjecture` (C-0006..C-0012) |
| :--- | :--- | :--- |
| **Laguerre Polynomial Link** | $P_n(x) = L_{n-1}^{(1)}(-x)$ established as standard | Reuses standard Lagarias identity for Euler product representation |
| **Zeta Pole Mode** | Handled analytically in asymptotic expansion | Identifies exact discrete mode $1 - q^n$ ($q = -s_0/(s_0-1)$) |
| **Pole Removal Mechanism** | Classical residue subtraction | Exact discrete shift filter $T = (E-1)(E-q)$ |
| **Criterion Type** | Sign positivity $\lambda_n \ge 0$ | Subexponential root growth after pole removal: $\limsup |S_n|^{1/n} \le 1$ |

---

## 3. Key Findings for Audit

* The presence of $L_{n-1}^{(1)}$ in Li coefficients is standard prior art originating from Lagarias (2007).
* The discrete pole-annihilating shift filter $T=(E-1)(E-q)$ and the pole-subtracted root growth criterion represent specialized discrete operator adaptations to the prime-side sequence.
