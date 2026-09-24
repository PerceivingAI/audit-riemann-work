# Claim Audit: CLM-VERF-005 - Adversarial Contract vs. Theorem Failure Separation

> **Audit Metadata**  
> * **Claim ID**: `CLM-VERF-005`  
> * **Audit Date**: `2026-09-24T00:00:00Z`  
> * **Audited Source Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71` (`2026-09-24`)  
> * **Audited Files**: `crates/rh_cert/tests/test_cert.rs`, `test_exact_prime_schur.rs`

---

## 1. Claim Specification

* **Category**: Verification & Adversarial Robustness
* **Candidate Statement**:
  > The verification architecture explicitly separates contract validation failures (malformed inputs, schema violations, invalid profiles returning exit code 2) from genuine mathematical counterexample failures (structurally valid certificates that fail mathematical positivity returning exit code 1).
* **Source Anchor Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71` (2026-09-24)

---

## 2. Technical Audit & Code Verification

* **Adversarial Tests**: In `crates/rh_cert/tests/test_cert.rs` and `test_exact_prime_schur.rs`:
  * `cli_exit_codes_distinguish_theorem_failure_from_contract_error`: Verified that CLI correctly returns `ExitCode(2)` on malformed parameters and `ExitCode(1)` on mathematically false certificates.
  * Negative perturbations (e.g., negative diagonal modifications, singular congruence witnesses, nonpositive complement bounds) are tested and confirmed to fail mathematically (`passed: false`, exit `1`).
  * Schema/structure corruptions (e.g., mixed whitelist pairs, wrong factor, non-zero cross parity) fail the contract gate (`ExitCode(2)`).

---

## 3. Audit Verdict & Justification

* **Final Verdict**: `NOVELTY SUPPORTED` (Software Assurance & Verification Architecture)
* **Detailed Rationale**:
  * The adversarial test suite rigorously separates structural schema violations from genuine mathematical theorem failures, preventing malformed proofs from being mistakenly admitted or false counterexamples from masking bugs.
