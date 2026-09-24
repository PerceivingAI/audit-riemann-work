# Literature Dossier: LIT-2026-CHUK-WEILPOS

```yaml
id: "LIT-2026-CHUK-WEILPOS"
title: "Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law"
authors: ["Marcus Chuk"]
year: 2026
venue: "arXiv Preprint"
arxiv_id: "2608.24827"
submission_date: "2026-08-25T00:00:00Z"
manuscript_date: "2026-09-04"
license: "arXiv.org perpetual non-exclusive license"
```

---

## 1. Summary of Work

Marcus Chuk investigates the minimum Rayleigh quotient $\lambda^*(L) = \inf \frac{Q(f)}{\|f\|_2^2}$ for Weil's quadratic form on functions supported in the compact interval $[-L, L]$ (autocorrelation support $[-2L, 2L]$).

The paper provides an unconditional certified positivity result at $L = 0.8$:
$$Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2 \qquad (f \in L^2([-0.8, 0.8])).$$

### Computational & Mathematical Strategy
* Uses a full Legendre polynomial modal expansion on $[-L, L]$.
* Discretizes operator entries using Gauss–Legendre quadrature and spherical-Bessel recurrences.
* Formulates a conjectural Landau–Widom decay law for the smallest eigenvalue:
  $$-\log \lambda^*(L) \sim 2\pi^2 \frac{N(T^*)}{\log N(T^*)}, \qquad T^* = 2\pi e^{2L}.$$

---

## 2. Comparison with `riemann-conjecture` Repository

| Dimension | Marcus Chuk (arXiv:2608.24827) | `riemann-conjecture` (C-0050..C-0057) |
| :--- | :--- | :--- |
| **First Public Timestamp** | 2026-08-25 (arXiv submission) | 2026-08-21 (`6dd1d8f0`, C-0050 at $T=0.35$) |
| **Support Parameter** | $L = 0.8$ (autocorrelation width $1.6$) | $T = 0.35 \to 0.54$ (Support $T$ on $[-T, T]$) |
| **First-Prime Treatment** | Global full matrix discretization | Exact $p=2$ compressed translation operator isolated |
| **High-Mode Tail Bound** | Legendre mode decay envelope | Exact Legendre harmonic coercivity $J(P_n) = H_n\|P_n\|_2^2$ |
| **Reduction Method** | Matrix eigenvalue bounds with interval quad | Exact 3-factor component tail-Gram Schur reduction |
| **Certificate Format** | Numerical interval enclosures | Exact-rational certificates + zero-float Rust verifier |

---

## 3. Key Findings for Audit

1. **Chronology**: The source repository's first certified exact-prime theorem C-0050 was committed on **2026-08-21T14:05:13Z** in public commit `6dd1d8f0`, preceding Chuk's arXiv submission on **2026-08-25**.
2. **Methodological Independence**: Chuk's approach relies on full Gauss-Legendre discretization at $L=0.8$, whereas `riemann-conjecture` developed the exact-prime component Schur complement reduction and harmonic coercivity mechanism.
