"""Run an audit-owned command, retaining raw streams and an explicit hash domain."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(data: bytes) -> dict:
    return {"raw_file_sha256": hashlib.sha256(data).hexdigest(),
            "normalized_sha256": hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True,
                          env=dict(os.environ, GIT_OPTIONAL_LOCKS="0")).stdout.decode().strip()


def source_state() -> dict:
    base = ("-C", "source/riemann-conjecture")
    return {"commit": git(*base, "rev-parse", "HEAD"),
            "tree": git(*base, "rev-parse", "HEAD^{tree}"),
            "status_porcelain": git(*base, "status", "--porcelain=v1", "--untracked-files=all")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="New repository-relative evidence prefix")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a command is required")
    prefix = (ROOT / args.output).resolve()
    if not prefix.is_relative_to(ROOT) or prefix.is_relative_to(ROOT / "source"):
        parser.error("output must be inside the audit repository and outside source")
    paths = {name: Path(str(prefix) + suffix) for name, suffix in
             (("stdout", ".stdout.log"), ("stderr", ".stderr.log"), ("record", ".run.json"))}
    if any(path.exists() for path in paths.values()):
        parser.error("refusing to overwrite retained execution evidence")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    record = {"schema_version": 1, "command": command, "working_directory": str(ROOT),
              "audit_head": git("rev-parse", "HEAD"), "source_before": source_state(),
              "host": {"os": platform.platform(), "architecture": platform.machine()},
              "tools": {"python": sys.version, "python_executable": sys.executable, "git": git("--version")},
              "environment_overrides": {"PYTHONDONTWRITEBYTECODE": "1", "GIT_OPTIONAL_LOCKS": "0"},
              "start_time": datetime.now(timezone.utc).isoformat()}
    record["audit_tool_hashes"] = {
        path.relative_to(ROOT).as_posix(): digest(path.read_bytes())
        for path in sorted((ROOT / "scripts").glob("pass4_*.py"))
    }
    record["audit_input_hashes"] = {
        path.relative_to(ROOT).as_posix(): digest(path.read_bytes())
        for path in sorted((ROOT / "evidence/phase0").glob("*.json"))
    }
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", GIT_OPTIONAL_LOCKS="0")
    try:
        with paths["stdout"].open("xb") as out, paths["stderr"].open("xb") as err:
            result = subprocess.run(command, cwd=ROOT, env=env, stdout=out, stderr=err)
        code = result.returncode
    except OSError as exc:
        code = 127
        paths["stderr"].write_bytes(str(exc).encode("utf-8"))
    record.update(end_time=datetime.now(timezone.utc).isoformat(), exit_code=code,
                  source_after=source_state(), hash_domain="exact raw file bytes",
                  line_ending_normalization="normalized_sha256 replaces CRLF bytes with LF only")
    record["streams"] = {name: {"path": path.relative_to(ROOT).as_posix(), **digest(path.read_bytes())}
                         for name, path in paths.items() if name != "record"}
    paths["record"].write_bytes((json.dumps(record, indent=2) + "\n").encode("utf-8"))
    print(paths["stdout"].read_bytes().decode("utf-8", errors="replace"), end="")
    print(paths["stderr"].read_bytes().decode("utf-8", errors="replace"), end="", file=sys.stderr)
    print(f"Retained execution record: {paths['record'].relative_to(ROOT)}; exit={code}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
