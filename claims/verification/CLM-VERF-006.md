# Claim Audit: CLM-VERF-006 - Replay of Retained 8/8 Proof Chain

> **Audit Metadata**  
> * **Claim ID**: `CLM-VERF-006`  
> * **Audit Date**: `2026-09-24T00:00:00Z`  
> * **Audited Source Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71` (`2026-09-24`)  
> * **Audited Files**: `computations/retained-proofs.json`, `crates/rh_cert/`

---

## 1. Claim Specification

* **Category**: Verification & Reproducibility
* **Candidate Statement**:
  > The repository retains eight exact theorem certificates (C-0050 through C-0057) by file path, claim identity, and cryptographic SHA-256 hash, and all 8 certificates pass full independent zero-floating-point verification (8/8 PASS).
* **Source Anchor Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71` (2026-09-24)

---

## 2. Independent Replay & Hash Verification Results

Every certificate was independently hashed and verified against `retained-proofs.json`:

| Claim | Support $T$ | Dim $N$ | Retained SHA-256 Hash | Local Hash Match | Rust Verifier Test (`rh_cert`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `C-0050` | $7/20 = 0.35$ | $32$ | `99ed74cc8fdb96ae...` | `PASS (MATCH)` | `PASS` (`test_cert.rs`) |
| `C-0051` | $2/5 = 0.40$ | $40$ | `8f9fa235beb9b4ee...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_t_two_fifths`) |
| `C-0052` | $17/40 = 0.425$ | $48$ | `6c74a386097bb30c...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_seventeen_fortieths`) |
| `C-0053` | $9/20 = 0.45$ | $56$ | `98f2b839d7f52c97...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_nine_twentieths`) |
| `C-0054` | $19/40 = 0.475$ | $68$ | `d9ba45f0026de31d...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_nineteen_fortieths`) |
| `C-0055` | $1/2 = 0.50$ | $80$ | `95dd6c7a497ad605...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_one_half`) |
| `C-0056` | $21/40 = 0.525$ | $96$ | `a455dcb995a56f6d...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_twenty_one_fortieths`) |
| `C-0057` | $27/50 = 0.54$ | $104$ | `75187f3be283ca95...` | `PASS (MATCH)` | `PASS` (`exact_prime_profile_accepts_twenty_seven_fiftieths`) |

* **Rust Replay Suite**: Executed `cargo test --manifest-path source/riemann-conjecture/crates/rh_cert/Cargo.toml` $\to$ **48/48 unit, property, and integration tests passed**.

---

## 3. Audit Verdict & Justification

* **Final Verdict**: `NOVELTY SUPPORTED` / `VERIFIED`
* **Detailed Rationale**:
  * 8 out of 8 historical theorem certificates match their cryptographic hashes exactly and pass all verification checks in the zero-floating-point Rust replay engine.
