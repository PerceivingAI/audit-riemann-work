"""Capture Phase 0 baselines and restore historical Git blobs without text conversion.

Run once with --apply. Existing evidence is never overwritten. Validation is separate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "1": "20b3f9d8ccbfe469861b85bf77a0053522c6a87a",
    "2": "66d70cd1d1de4e31cfacc902eddb225ba1b77c79",
    "3": "99e2afc5742b1ebae9987eabdda22f9ee844de61",
}
PLAN_COMMIT = "c2a305a60f8eb1819a685896196dfb880d0325c0"
SOURCE_PIN = "51feb3d176e4a53773c22dc157567cc0486f4c71"
LIVING = {"README.md", "AUDIT_PROTOCOL.md", "CLAIMS_TO_AUDIT.md",
          "EVIDENCE_STANDARDS.md", "TIMELINE_RULES.md", "SOURCE.md", "AUDIT_LEDGER.md"}
RENAMES = {"AUDIT_PLAN.md": "archive/AUDIT_PLAN.md",
           "SECOND_AUDIT.md": "archive/SECOND_AUDIT.md",
           "THIRD_AUDIT.md": "archive/THIRD_AUDIT.md"}


def git(*args: str) -> bytes:
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    return subprocess.run(["git", *args], cwd=ROOT, env=env,
                          capture_output=True, check=True).stdout


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hashes(data: bytes) -> dict:
    return {"raw_file_sha256": sha(data),
            "normalized_sha256": sha(data.replace(b"\r\n", b"\n"))}


def save_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def tree(commit: str) -> dict:
    result = {}
    for row in git("ls-tree", "-rz", commit).split(b"\0"):
        if row:
            meta, path = row.split(b"\t", 1)
            mode, kind, oid = meta.decode().split()
            result[path.decode()] = {"mode": mode, "type": kind, "git_blob_oid": oid}
    return result


def file_inventory(directory: Path) -> dict:
    result = {}
    for path in sorted(directory.rglob("*")):
        key = path.relative_to(directory).as_posix()
        if path.is_symlink():
            result[key] = {"type": "symlink", "target": os.readlink(path)}
        elif path.is_file():
            with path.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            result[key] = {"type": "file", "size": path.stat().st_size, "sha256": digest}
        elif path.is_dir():
            result[key] = {"type": "directory"}
    return result


def source_snapshot() -> dict:
    prefix = ("-C", "source/riemann-conjecture")
    return {
        "commit": git(*prefix, "rev-parse", "HEAD").decode().strip(),
        "tree": git(*prefix, "rev-parse", "HEAD^{tree}").decode().strip(),
        "status_porcelain": git(*prefix, "status", "--porcelain=v1", "--untracked-files=all").decode(),
        "refs": git(*prefix, "show-ref").decode(),
        "files_including_ignored": file_inventory(ROOT / "source/riemann-conjecture"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", required=True)
    parser.parse_args()
    out = ROOT / "evidence/phase0"
    if (out / "PRESERVATION_MANIFEST.json").exists() or (out / "SOURCE_BEFORE.json").exists():
        raise SystemExit("Refusing to overwrite established Phase 0 preservation evidence")
    started = datetime.now(timezone.utc).isoformat()
    snapshot = source_snapshot()
    if snapshot["commit"] != SOURCE_PIN or snapshot["status_porcelain"]:
        raise SystemExit("Source pin or tracked/untracked state does not satisfy the clean baseline")
    save_json(out / "SOURCE_BEFORE.json", snapshot)
    versions = {p: tree(c) for p, c in PINS.items()}
    pre_tree = tree(PLAN_COMMIT)
    owner = {}
    for pass_id, entries in versions.items():
        for old_path, item in entries.items():
            current = RENAMES.get(old_path, old_path)
            if item["type"] == "blob" and old_path not in LIVING and old_path != ".gitmodules":
                owner.setdefault(current, (pass_id, item["git_blob_oid"]))
    records, writes = [], {}
    for pass_id, entries in versions.items():
        for old_path, item in entries.items():
            current = RENAMES.get(old_path, old_path)
            record = {"pass": pass_id, "baseline_commit": PINS[pass_id],
                      "historical_path": old_path, "current_path": current, **item}
            if item["type"] != "blob" or old_path == ".gitmodules":
                record["classification"] = "repository_control"
                records.append(record)
                continue
            data = git("cat-file", "blob", item["git_blob_oid"])
            record["baseline_blob_sha256"] = sha(data)
            before = (ROOT / current).read_bytes() if (ROOT / current).exists() else None
            record["working_tree_before"] = hashes(before) if before is not None else None
            record["changed_in_git_after_completion"] = (
                pre_tree.get(current, {}).get("git_blob_oid") != item["git_blob_oid"])
            if old_path in LIVING:
                record["classification"] = "living_document_snapshot"
                stored = f"archive/baselines/pass-{pass_id}/{old_path}"
                retained = data
            elif owner[current][1] != item["git_blob_oid"]:
                record["classification"] = "later_historical_version_snapshot"
                stored = f"archive/baselines/pass-{pass_id}/{old_path}"
                retained = data
            else:
                record["classification"] = "historical_artifact"
                stored = current
                # Pass 1/2 restore Git blob bytes. Pass 3-only files retain their
                # existing raw working-tree bytes, with a separate normalized hash.
                retained = before if owner[current][0] == "3" else data
                if retained is None or retained.replace(b"\r\n", b"\n") != data.replace(b"\r\n", b"\n"):
                    if owner[current][0] == "3":
                        raise RuntimeError(f"Unexpected Pass 3 content change: {current}")
            record["stored_path"] = stored
            record["stored_hashes"] = hashes(retained)
            if stored in writes and writes[stored] != retained:
                raise RuntimeError(f"Conflicting preservation targets: {stored}")
            writes[stored] = retained
            if record["changed_in_git_after_completion"]:
                record["later_history"] = git("log", "--format=%H %s", "--follow",
                    f"{PINS[pass_id]}..{PLAN_COMMIT}", "--", current).decode().splitlines()
            records.append(record)
    # All reads and conflict checks precede mutations of historical files.
    for stored, data in writes.items():
        path = ROOT / stored
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    plan = git("show", f"{PLAN_COMMIT}:AUDIT_PASS_4.md")
    (ROOT / "FOURTH_AUDIT.md").write_bytes(plan)
    manifest = {
        "schema_version": 1, "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "baseline_commits": PINS, "pre_execution_commit": PLAN_COMMIT,
        "pass3_selection_basis": "Last commit of the completed Pass 3 series; next commit adds the Pass 4 plan and relocates THIRD_AUDIT.md.",
        "plan_origin": {"commit": PLAN_COMMIT, "path": "AUDIT_PASS_4.md", "preserved_path": "FOURTH_AUDIT.md", "raw_file_sha256": sha(plan)},
        "hash_domain": "raw_file_bytes; normalized_sha256 is CRLF-to-LF byte replacement only",
        "line_ending_normalization": "CRLF -> LF; no other byte changes",
        "records": records,
    }
    save_json(out / "PRESERVATION_MANIFEST.json", manifest)
    changed = sorted({r["current_path"] for r in records if r["pass"] in ("1", "2")
                      and r.get("changed_in_git_after_completion") and r["classification"] == "historical_artifact"})
    print(json.dumps({"historical_content_restorations": changed,
                      "preserved_version_records": len(records), "stored_paths": len(writes),
                      "source_files_and_directories": len(snapshot["files_including_ignored"]),
                      "source_pin": snapshot["commit"], "source_clean": not snapshot["status_porcelain"]}, indent=2))


if __name__ == "__main__":
    main()
