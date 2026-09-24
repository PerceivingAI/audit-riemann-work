# Literature Dossier: LIT-2026-SUZUKI-WEILSCREW

```yaml
id: "LIT-2026-SUZUKI-WEILSCREW"
title: "Weil’s quadratic form via the screw function"
authors: ["Masatoshi Suzuki"]
year: 2026
venue: "arXiv Preprint"
arxiv_id: "2606.09096"
submission_date: "2026-06-08T00:00:00Z"
license: "arXiv.org perpetual non-exclusive license"
```

---

## 1. Summary of Work

Masatoshi Suzuki reformulates Weil's quadratic form for the Riemann zeta function through the theory of "screw functions," replacing the distributional framework with continuous integral transformations.

### Key Contributions
* Relates the Weil quadratic form unconditionally to screw functions on the real line.
* Generalizes prior positivity frameworks by Yoshida, Bombieri, and Connes–Consani–Moscovici.
* Investigates Hilbert and de Branges spaces associated with the Weil distribution.

---

## 2. Comparison with `riemann-conjecture` Repository

| Dimension | Suzuki (arXiv:2606.09096, June 2026) | `riemann-conjecture` (Aug–Sep 2026) |
| :--- | :--- | :--- |
| **Focus** | Operator-theoretic screw function formulation | Finite-support certified numerical & analytical theorems |
| **Support Restriction** | General / continuous real line | Strict localized compact intervals $[-T, T]$ |
| **Prime Treatment** | Global distribution representation | Explicit compressed translation operator $P_T(U_a + U_a^*)P_T$ |
| **Proof Output** | Structural operator-theoretic equivalences | Explicit certified theorems (C-0050..C-0057) + Rust verifier |

---

## 3. Key Findings for Audit

* Suzuki's work is a foundational continuous reformulator of Weil's quadratic form.
* The discrete path-graph compressed translation formula and Legendre harmonic coercivity used in `riemann-conjecture` are distinct constructive tools designed for certified finite-dimensional reduction.
