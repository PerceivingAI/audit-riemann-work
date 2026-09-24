# Claim Audit: CLM-VERF-001 - Exact Rational Certificate Format

> **Audit Metadata**  
> * **Claim ID**: `CLM-VERF-001`  
> * **Audit Date**: `2026-09-24T00:00:00Z`  
> * **Audited Source Commit**: `6dd1d8f07e23dd39fcd2e36974c53a5054f810ec` (`2026-08-21T14:05:13Z`)  
> * **Audited Files**: `crates/rh_cert/`, `computations/retained-proofs.json`

---

## 1. Claim Specification

* **Category**: Verification / Computational Architecture
* **Candidate Statement**:
  > Finite-support localized Weil positivity proofs are represented as machine-checkable exact rational/dyadic certificate JSON files converting rigorous Arb outward interval enclosures into exact congruence witnesses and rational Gershgorin bounds without relying on floating-point eigenvalues.
* **Source Anchor Commit**: `6dd1d8f07e23dd39fcd2e36974c53a5054f810ec` (2026-08-21)

---

## 2. Technical Audit & Code Verification

* **Inspection**: Inspected `crates/rh_cert/src/interval.rs`, `ldl.rs`, `gershgorin.rs`, and `cert.rs`.
* **Arithmetic Engine**: All matrices, tail-Gram reductions, and congruence tests operate over exact arbitrary-precision rationals (`num_rational::BigRational`) and integer numerators/denominators.
* **Soundness Guarantee**: Does not trust runtime floating-point linear algebra; replaces floating eigenvalue checks with exact rational LDL congruence decompositions $M = L D L^T$ and rational interval Gershgorin disc margins.

---

## 3. Audit Verdict & Justification

* **Final Verdict**: `NOVELTY SUPPORTED` (Certificate Architecture)
* **Detailed Rationale**:
  * Prior certified computational work in Weil positivity (Chuk 2026, Connes–Consani 2021) reports interval floating bounds or numerical Rayleigh quotient bounds.
  * The conversion to standalone, independently checkable, zero-float exact-rational JSON certificate files is an original computational proof architecture.
