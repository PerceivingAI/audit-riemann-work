# Verification Trust Chain & Formal Soundness Dossier (`PASS4-VERF-TRUST-CHAIN`)

> **Trust Chain Governance Metadata**  
> * **Dossier ID**: `PASS4-VERF-TRUST-CHAIN`  
> * **Audit Phase**: Pass 4 Phase 4 (Verification-Chain and Computational Trust Audit)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Protocol**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 20 & 21; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).  
> * **Associated Candidate IDs**: `CLM-VERF-001` through `CLM-VERF-007`, `CLM-MATH-001..008`, `CLM-METH-005`.

---

## 1. The 6-Layer Verification Trust Boundary

The theorem verification architecture of `riemann-conjecture` separates the infinite-dimensional analytical reduction from finite-dimensional certificate generation, schema admission, exact-rational replay, and formal algebraic soundness:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        6-Layer Trust Chain                             │
├────────────────────────────────────────────────────────────────────────┤
│ Layer 1: Analytic Continuous Theorem (Q_T > 0 on L^2[-T, T])           │
│    │                                                                   │
│    ▼ [Edge 1-2: Tuck coercivity + Cauchy-Schwarz + Schur complement]   │
│ Layer 2: Finite Operator Reduction (A_N - 3/mu_N (G_V+G_2+G_R) > 0)    │
│    │                                                                   │
│    ▼ [Edge 2-3: Python / python-flint (Arb) interval assembly]         │
│ Layer 3: Generator Assembly & Outward Rational Conversion              │
│    │                                                                   │
│    ▼ [Edge 3-4: JSON Schema Validation & Admission Whitelist]          │
│ Layer 4: Strict Certificate Contract (rh-weil-certificate-v1.json)     │
│    │                                                                   │
│    ▼ [Edge 4-5: Zero-floating-point BigRational Rust verifier]         │
│ Layer 5: Standalone Verifier Engine (crates/rh_cert)                   │
│    │                                                                   │
│    ▼ [Edge 5-6: Machine-checked algebraic soundness lemmas in Lean 4] │
│ Layer 6: Formal Mathematical Soundness (formal/Cert/*.lean, Mathlib)   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Trust Chain Edge Analysis Matrix

| Edge | Transition | Input Artifact / Premise | Output Artifact / Target | Method of Verification | Trust Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1 $\to$ 2** | Continuous Theorem $\to$ Finite Reduction | Quadratic form $Q_T(w)$ on admissible $L^2[-T,T]$ | Discrete matrix inequality $A_N - \frac{3}{\mu_N}(G_V+G_2+G_R) \succ 0$ | Independent mathematical derivation; Tuck (1964) eigenvalue analysis; Schur complement reduction. | `INDEPENDENTLY_CHECKED` |
| **2 $\to$ 3** | Finite Reduction $\to$ Generator Assembly | Exact analytical matrix integrals and tail bounds | Python generator (`scripts/cert/*.py`) using `flint.arb` ball arithmetic | Code review of outward interval rounding; multi-precision validation. | `TESTED_GENERATOR` |
| **3 $\to$ 4** | Generator $\to$ Certificate Contract | Python-assembled interval data | JSON Certificate (`rh-weil-certificate-v1.json`) | Schema validation; closed parameter whitelist check (`(T, N)` admitted pairs). | `CHECKED_CONTRACT` |
| **4 $\to$ 5** | Certificate $\to$ Rust Verifier | JSON certificate file (exact rational strings) | Standalone verification in `crates/rh_cert` | Zero-float execution; `num_rational::BigRational` arithmetic; exact LDL and Gershgorin isolation. | `MACHINE_REPLAYED` |
| **5 $\to$ 6** | Verifier Logic $\to$ Formal Soundness | Rust algebraic algorithm logic | Lean 4 formal proofs (`formal/Cert/*.lean`) | Lean 4 compiler + Mathlib v4.33.0 machine verification (36 lemmas sorry-free). | `FORMALLY_PROVED` |

---

## 3. Explicit Trust Boundaries

### 3.1 What `rh_cert` Proves
1. **Exact Rational Matrix Positivity**: Proves that the discrete rational matrix $M = A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R)$ specified in the certificate is strictly positive definite via an exact rational LDL decomposition $M = L D L^T$ where all diagonal elements $D_{ii} > 0$.
2. **Complement Coercivity**: Verifies that $\mu_N = H_N - c_T - c_2 - \rho_R > 0$ using exact harmonic number summation $H_N = \sum_{k=1}^N 1/k$.
3. **Gershgorin Disc Isolation**: Computes exact row sums $\sum_{j \ne i} |M_{ij}|$ and confirms $M_{ii} - \sum_{j \ne i} |M_{ij}| > 0$.
4. **Zero-Floating-Point Guarantee**: Verified zero occurrences of IEEE floating-point types (`f32`, `f64`) across the entire acceptance path of `rh_cert`.

### 3.2 What Must Be Trusted (Outside Rust Verifier)
1. **Analytic Reduction**: The mathematical proof connecting the continuous functional $Q_T(w) > 0$ on $L^2[-T,T]$ to the finite matrix inequality $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) \succ 0$ (verified in [`PASS4-MATH-001-008-THEOREMS.md`](PASS4-MATH-001-008-THEOREMS.md)).
2. **Analytical Constants**: The analytical upper bounds for $c_T$, $c_2 = \frac{\log 2}{\sqrt{2}}$, and $\rho_R = 2T \sup |r_0''(u)|$.

---

## 4. Lean 4 Formal Correspondence Table

The Lean 4 formalization under `formal/Cert/` (pinned to Mathlib `v4.33.0-rc2`) formalizes the algebraic soundness of the verifier's core algorithms:

| Lean 4 Module | Proved Lemma Count | Mathematical Concept Formalized | Corresponding Rust / Python Object | Formal Status |
| :--- | :--- | :--- | :--- | :--- |
| `formal/Cert/Interval.lean` | 10 lemmas | Strict rational interval arithmetic, outward rounding bounds, monotonicity | `rh_cert::interval::RationalInterval` | `PROVEN_SORRY_FREE` |
| `formal/Cert/LDL.lean` | 6 lemmas | Soundness of LDL matrix decomposition for positive definiteness | `rh_cert::ldl::ldl_decompose` | `PROVEN_SORRY_FREE` |
| `formal/Cert/Gershgorin.lean` | 4 lemmas | Gershgorin circle theorem for eigenvalue lower bounds of symmetric matrices | `rh_cert::gershgorin::check_margins` | `PROVEN_SORRY_FREE` |
| `formal/Cert/EndpointAbsorption.lean` | 16 lemmas | Analytical bound proofs for prime translation absorption constants ($\log 2$, $\sqrt{2}$, $\tau$, $\kappa_{\text{edge}}$, $c_2$) | `scripts/cert/weil_exact_constants.py` | `PROVEN_SORRY_FREE` |

**Total Proved Lemmas**: **36 sorry-free lemmas** verified by the Lean 4 compiler against Mathlib.
