# Interim Audit Report — Pass 3, Phase 3: Preserved Raw Computational Replay & Lean Soundness (WS-07)

> **Audit Report Metadata**  
> * **Audit Phase**: `Phase 3: Preserved Raw Computational Replay & Lean Soundness (WS-07)`  
> * **Status**: `PHASE_3_COMPLETE`  
> * **Date of Execution**: `2026-09-24T23:05:00Z`  
> * **Governing Document**: [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md)  
> * **Manifest & Log Artifacts**: [`evidence/computation-logs/PASS3-REPLAY-MANIFEST.json`](../../evidence/computation-logs/PASS3-REPLAY-MANIFEST.json)

---

## 1. Executive Summary & Raw Replay Verification

In strict compliance with WS-07 of `THIRD_AUDIT.md`, Audit Pass 3 independently executed the full test and verification suites against the audited research checkout `source/riemann-conjecture/` pinned at `51feb3d176e4a53773c22dc157567cc0486f4c71`.

All raw machine outputs (stdout, stderr, exit codes, toolchain versions, execution timestamps, and cryptographic SHA-256 digests) have been archived into `evidence/computation-logs/`.

---

## 2. Replay Execution Ledger

| Run Label | Executed Command | Exit Code | Elapsed Time | Output Log Path | Cryptographic SHA-256 Digest |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rust rh_cert Tests** | `cargo test --release` in `crates/rh_cert` | **`0` (PASS)** | 63.3s | `PASS3-REPLAY-RUST-CERT.log` | `e0d303bb517c8f280de55505dfde96ac2b82e37298800cbaebe9151220d4b85e` |
| **Rust rh_engine Tests** | `cargo test --release` in `crates/rh_engine` | **`0` (PASS)** | 25.3s | `PASS3-REPLAY-RUST-ENGINE.log` | `804297f319ed47fbbd1b965db66dfa9b19bba11ed59280542343c25f18976fc0` |
| **8/8 Proof Certificates Replay** | `rh_cert.exe verify --cert [8 certificates]` | **`0` (PASS)** | 15.5s | `PASS3-REPLAY-CERT-8OF8.log` | `398e6cc2708eb0bed10cf58622fd1d4b7f9695ffc25efe82c7c9709cef0ef9e1` |
| **Python Core Test Suite** | `pytest tests/[identities+entrypoints+observability]` | **`0` (PASS)** | 2.9s | `PASS3-REPLAY-PYTEST.log` | `2c3981969ad9252eb311b0dd38fe9ec34f35ba8f752c197b2afc69ef3e6e0dad` |

---

## 3. Retained Proof Certificates Verification Summary (8/8 Verified)

The standalone release binary `rh_cert.exe` replayed all 8 retained proof certificates without error:
1. **`C-0050` ($T=7/20=0.35, N=32$)**: `VERIFIED [PASS]` — Positive Schur factor ($124864471104497792528652907315200/36248577317193051188471141673041 > 0$), positive even/odd Gershgorin margins.
2. **`C-0051` ($T=2/5=0.40, N=40$)**: `VERIFIED [PASS]` — Valid Schur complement.
3. **`C-0052` ($T=17/40=0.425, N=48$)**: `VERIFIED [PASS]` — Valid Schur complement.
4. **`C-0053` ($T=9/20=0.45, N=56$)**: `VERIFIED [PASS]` — Valid Schur complement.
5. **`C-0054` ($T=19/40=0.475, N=68$)**: `VERIFIED [PASS]` — Valid Schur complement.
6. **`C-0055` ($T=1/2=0.50, N=80$)**: `VERIFIED [PASS]` — Valid Schur complement.
7. **`C-0056` ($T=21/40=0.525, N=96$)**: `VERIFIED [PASS]` — Valid Schur complement.
8. **`C-0057` ($T=27/50=0.54, N=104$)**: `VERIFIED [PASS]` — Valid Schur complement.

---

## 4. Phase 3 / WS-07 Exit Gate Verification

- [x] **Independent Verification Executed**: `rh_cert`, `rh_engine`, 8/8 certificates, and pytest executed.
- [x] **Raw Machine Logs Preserved**: 4 `.log` files saved with exit codes and environment metadata.
- [x] **Cryptographic Manifest Generated**: `PASS3-REPLAY-MANIFEST.json` contains SHA-256 digests for all logs.

**Exit Gate Satisfied**. Ready to proceed to **WS-08, WS-09, WS-10, WS-11 & WS-12 (Protocol Versioning, Navigation Sync, Hygiene & Master Synthesis)**.
