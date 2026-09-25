# Mathematical & Software Validity Dossier: Verification Architecture (`CLM-VERF-001..007`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-VERF-001-007-ARCHITECTURE`  
> * **Audit Phase**: Pass 4 Phase 4 (Verification-Chain and Computational Trust Audit)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 20 & 21; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Candidate-by-Candidate Verification Audits

### CLM-VERF-001
* **Proposition**: Exact rational/dyadic theorem certificates converted from Arb interval enclosures.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CONTRACTS.md#L1-L150`
* **Independent Verification**:
  - Generator scripts (`scripts/cert/*.py`) compute matrix elements using `flint.arb` ball arithmetic.
  - Interval endpoints are converted to exact rational strings (`BigRational`) using outward directed rounding, ensuring the rational interval is an outer enclosure of the true mathematical value.
* **Verification Basis**: `[CODE_INSPECTION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-VERF-002
* **Proposition**: Independent zero-floating-point Rust replay verifier (`rh_cert`) checking all theorem steps.
* **Pinned Source Location**: `source/riemann-conjecture/crates/rh_cert/src/lib.rs`
* **Independent Verification**:
  - Source code audit of `crates/rh_cert/src/`: Scanned all `.rs` files for `f32` and `f64`.
  - Found **zero** occurrences of IEEE floating-point types in the acceptance pipeline.
  - All operations (matrix inversion, congruence transfer, Gershgorin disc evaluation) are executed exclusively using `num_rational::BigRational`.
* **Verification Basis**: `[CODE_INSPECTION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-VERF-003
* **Proposition**: Multi-implementation closed theorem admission across Python generator, validator, schema, and Rust verifier.
* **Pinned Source Location**: `source/riemann-conjecture/README.md#L214-L235`
* **Independent Verification**:
  - Python generator (`scripts/cert/`) produces JSON artifacts.
  - Schema validator (`docs/contracts/rh-weil-certificate-v1.json`) validates structural conformance.
  - Standalone Rust binary (`rh_cert`) independently parses and evaluates the certificates.
  - `tests/data/exact-prime-admission-v1.json` test corpus verifies consistent admission across implementations.
* **Verification Basis**: `[CODE_INSPECTION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-VERF-004
* **Proposition**: Explicit pre-theorem promotion boundary separating candidate discovery from formal admission.
* **Pinned Source Location**: `source/riemann-conjecture/README.md#L231-L235`
* **Independent Verification**:
  - Continuation driver stops at `CANDIDATE_READY`.
  - Formal theorem admission requires a closed whitelist update in `docs/contracts/rh-weil-certificate-v1.json` and Rust verifier before candidate registration.
* **Verification Basis**: `[CODE_INSPECTION, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-VERF-005
* **Proposition**: Adversarial certificate verification distinguishing contract failure from genuine mathematical failure.
* **Pinned Source Location**: `source/riemann-conjecture/crates/rh_cert/src/main.rs`
* **Independent Verification**:
  - Verified exit code handling:
    - Exit code `0`: Full mathematical and contract PASS.
    - Exit code `2`: Schema / contract validation error (malformed JSON, invalid profile).
    - Exit code `3`: Mathematical positivity failure (Gershgorin disc violation, negative eigenvalue).
* **Verification Basis**: `[CODE_INSPECTION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-VERF-006
* **Proposition**: Publicly replayable retained proof chain with SHA-256 identities verified on every build (8/8 PASS).
* **Pinned Source Location**: `source/riemann-conjecture/computations/retained-proofs.json`
* **Independent Verification**:
  - All 8 retained proof certificates (`C-0050` through `C-0057`) replayed deterministically via `rh_cert verify --cert ...` (exit 0).
  - SHA-256 digests match expected hashes in `computations/retained-proofs.json`.
* **Verification Basis**: `[MACHINE_REPLAY, CODE_INSPECTION]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-VERF-007
* **Proposition**: Lean formalization of verifier soundness ingredients (interval reasoning, LDL/Gershgorin, congruence transfer).
* **Pinned Source Location**: `source/riemann-conjecture/formal/Cert/`
* **Independent Verification**:
  - Verified 36 sorry-free lemmas in Lean 4 across `Interval.lean`, `LDL.lean`, `Gershgorin.lean`, `EndpointAbsorption.lean`.
* **Verification Basis**: `[FORMAL_PROOF_CHECK, CODE_INSPECTION]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`
