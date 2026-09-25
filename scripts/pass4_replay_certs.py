"""Replay and verify all 8 retained proof certificates using standalone rh_cert.

Computes exact raw SHA-256 for each certificate, invokes rh_cert verify,
and outputs deterministic verification summaries.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/riemann-conjecture"
RH_CERT_EXE = SOURCE / "target/release/rh_cert.exe"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    manifest_path = SOURCE / "computations/retained-proofs.json"
    with open(manifest_path, encoding="utf-8") as f:
        manifest_data = json.load(f)

    proofs = manifest_data.get("proofs", [])
    print(f"Replaying {len(proofs)} retained theorem certificates using {RH_CERT_EXE}...")

    all_passed = True
    results = []

    for i, proof in enumerate(proofs, 1):
        claim_id = proof["claim"]
        comp_id = proof["computation_id"]
        rel_path = proof["certificate_path"]
        expected_hash = proof["certificate_sha256"]
        support_t = proof["support_T"]
        dim = proof["dimension"]

        cert_full_path = SOURCE / rel_path
        cert_bytes = cert_full_path.read_bytes()
        actual_hash = sha(cert_bytes)
        hash_matches = actual_hash == expected_hash

        start_t = time.perf_counter()
        cmd = [str(RH_CERT_EXE), "verify", "--cert", str(cert_full_path)]
        res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        elapsed = time.perf_counter() - start_t

        passed = (res.returncode == 0) and hash_matches
        if not passed:
            all_passed = False

        status_str = "PASS" if passed else "FAIL"
        print(f"[{i}/{len(proofs)}] {claim_id} (T={support_t}, N={dim}) -> {status_str} in {elapsed:.3f}s (exit {res.returncode}, sha256: {actual_hash[:16]}...)")
        if res.stdout.strip():
            print(f"      stdout: {res.stdout.strip()[:200]}")

        results.append({
            "claim": claim_id,
            "computation_id": comp_id,
            "certificate_path": (SOURCE / rel_path).relative_to(ROOT).as_posix(),
            "support_T": support_t,
            "dimension": dim,
            "expected_sha256": expected_hash,
            "actual_sha256": actual_hash,
            "sha256_match": hash_matches,
            "exit_code": res.returncode,
            "elapsed_seconds": elapsed,
            "stdout": res.stdout.strip(),
            "stderr": res.stderr.strip(),
            "status": status_str,
        })

    print(f"\nSummary: {sum(r['status'] == 'PASS' for r in results)}/{len(proofs)} certificates verified successfully.")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
