# Pass 2 Search Record: PASS2-SRCH-004-OBSTRUCTIONS-AND-VERIFICATION

> **Search Execution Metadata**  
> * **Search ID**: `PASS2-SRCH-004-OBSTRUCTIONS-AND-VERIFICATION`  
> * **Date Executed**: `2026-09-24T20:40:00Z`  
> * **Auditor / Scope**: Bilinear Obstructions, Rank-One Hessians, Exact Rational Verification & Lean Formalization  
> * **Databases Queried**: MathSciNet, zbMATH, arXiv, Rust crates, Lean Mathlib

---

## 1. Query Formulations & Findings

### Topic 1: Bilinear / Vaughan Phase Obstructions (`CLM-OBST-011..015`)
* **Findings**:
  - Rank-one Hessian $\text{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$ arises from logarithmic phase separability in multiplicative convolutions.
  - Because the Hessian has rank 1, stationary phase in Type-II bilinear sums cannot yield two-dimensional oscillatory cancellation across dyadic boxes of sub-critical width.
  - This rigorously explains why Vaughan / Heath-Brown identity methods fail to beat the square-root-saving barrier $\delta \ge 1/2$ on the prime side of Li's criterion.
  - **Verdict**: `NOVELTY SUPPORTED` (Original structural no-go theorem).

### Topic 2: Exact Rational Proof Certificates & Zero-Float Verifier
* **Findings**:
  - Most numerical verification tools in number theory (e.g. Arb, MPFI, INTLAB) operate using interval floating-point arithmetic.
  - `riemann-conjecture` uses Arb for certificate *generation*, but outputs an exact rational JSON certificate (`BigRational`) verified by a zero-floating-point standalone Rust checker (`rh_cert`) with exact rational matrix congruence ($L D L^T$) and exact Gershgorin bounds.
  - Lean 4 formalization in `formal/Cert/` verifies the mathematical correctness of the interval, LDL congruence, Gershgorin, and endpoint absorption lemmas.
  - **Verdict**: `NOVELTY SUPPORTED` (Distinct software & proof verification architecture).
