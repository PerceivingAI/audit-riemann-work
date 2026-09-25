"""Retain Kuber comparator history and original-content text blobs, without executing it.

The local mirror is deliberately outside the audited source. Third-party PDFs and
binary experiment data are not copied into evidence. Repeated collection must use
another evidence directory rather than overwrite a provenance snapshot.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.error
import urllib.request
ROOT = Path(__file__).resolve().parents[1]
MIRROR = ROOT / ".audit-cache/phase1/kuber-repo/.git"
OUT = ROOT / "evidence/phase1/kuber"
MANDATORY = ["UPDATES.md", "CONTINUATION.md", "FINDINGS.md", "logs/LOG.md",
             "experiments/weil_positivity/", "formal/"]
TEXT_SUFFIXES = {".md", ".py", ".lean", ".txt", ".json", ".toml", ".cff"}


def git(*args: str) -> bytes:
    return subprocess.run(["git", "--git-dir", str(MIRROR), *args], cwd=ROOT,
                          env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"),
                          capture_output=True, check=True).stdout


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"Refusing to overwrite evidence: {path}")
    else:
        path.write_bytes(data)


def save_json(path: Path, data: object) -> None:
    save(path, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def relevant(path: str) -> bool:
    if path in {"LICENSE", "CITATION.cff"}:
        return True
    if "/" not in path and path.endswith(".md"):
        return True
    return (path.startswith(("logs/", "experiments/weil_positivity/", "formal/"))
            and Path(path).suffix in TEXT_SUFFIXES
            and Path(path).name != "zeros1.txt")


def http_record(url: str, name: str) -> dict:
    started = datetime.now(timezone.utc).isoformat()
    request = urllib.request.Request(url, headers={"User-Agent": "Riemann-Audit-Pass4", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
            status = response.status
            headers = dict(response.headers)
            final_url = response.url
    except urllib.error.HTTPError as error:
        data = error.read(); status = error.code
        headers = dict(error.headers); final_url = error.url
    save(OUT / name, data)
    return {"url": url, "retrieved_at_start": started,
            "retrieved_at_end": datetime.now(timezone.utc).isoformat(),
            "http_status": status, "response_headers": headers, "final_url": final_url,
            "path": (OUT / name).relative_to(ROOT).as_posix(), "raw_file_sha256": sha(data)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collect", action="store_true", required=True)
    parser.parse_args()
    if (OUT / "MANIFEST.json").exists():
        raise SystemExit("Refusing to replace a completed comparator collection")
    started = datetime.now(timezone.utc).isoformat()
    refs_raw = git("show-ref")
    save(OUT / "refs.txt", refs_raw)
    head = git("rev-parse", "HEAD").decode().strip()
    shallow = git("rev-parse", "--is-shallow-repository").decode().strip()
    raw_log = git("log", "--all", "--reverse", "--topo-order",
                  "--format=%H%x09%P%x09%aI%x09%cI%x09%s")
    save(OUT / "all-commits.tsv", raw_log)
    commits = []
    blobs = {}
    path_history = {}
    for line in raw_log.decode("utf-8").splitlines():
        oid, parents, author_time, committer_time, subject = line.split("\t", 4)
        changes_raw = git("diff-tree", "--root", "--no-commit-id", "--raw", "--no-abbrev", "-r", "-M", "-z", oid)
        fields = changes_raw.split(b"\0")
        changes = []
        pos = 0
        while pos < len(fields) and fields[pos]:
            meta = fields[pos].decode(); pos += 1
            path = fields[pos].decode("utf-8"); pos += 1
            previous = None
            status = meta.split()[-1]
            if status.startswith(("R", "C")):
                previous = path
                path = fields[pos].decode("utf-8"); pos += 1
            if not relevant(path) and not (previous and relevant(previous)):
                continue
            parts = meta.split()
            old_blob, new_blob = parts[2], parts[3]
            change = {"status": status, "path": path, "previous_path": previous,
                      "old_blob_oid": old_blob, "new_blob_oid": new_blob}
            if new_blob != "0" * 40 and relevant(path):
                if new_blob not in blobs:
                    data = git("cat-file", "blob", new_blob)
                    suffix = Path(path).suffix or ".txt"
                    destination = OUT / "objects" / (new_blob + suffix)
                    save(destination, data)
                    blobs[new_blob] = {"stored_path": destination.relative_to(ROOT).as_posix(),
                                       "raw_file_sha256": sha(data), "size": len(data),
                                       "license_scope": "Comparator original content; Apache-2.0; see retained LICENSE"}
                change["retained_object"] = blobs[new_blob]["stored_path"]
            changes.append(change)
            path_history.setdefault(path, []).append({"commit": oid, "status": status,
                "author_timestamp": author_time, "committer_timestamp": committer_time,
                "blob_oid": new_blob, "previous_path": previous})
        commits.append({"sha": oid, "parents": parents.split(), "author_timestamp": author_time,
                        "committer_timestamp": committer_time, "subject": subject, "changes": changes})
    tip_tree = []
    for row in git("ls-tree", "-rz", head).split(b"\0"):
        if not row: continue
        meta, path = row.split(b"\t", 1)
        path = path.decode("utf-8")
        if relevant(path):
            mode, kind, oid = meta.decode().split()
            tip_tree.append({"path": path, "type": kind, "blob_oid": oid,
                             "stored_path": blobs.get(oid, {}).get("stored_path")})
    http = [http_record("https://api.github.com/repos/Kuberwastaken/riemann", "github-repository.json"),
            http_record("https://api.github.com/repos/Kuberwastaken/riemann/branches?per_page=100", "github-branches.json"),
            http_record("https://api.github.com/repos/Kuberwastaken/riemann/tags?per_page=100", "github-tags.json")]
    save_json(OUT / "history.json", {"commits": commits, "path_history": path_history, "tip_files": tip_tree})
    manifest = {"started_at": started, "completed_at": datetime.now(timezone.utc).isoformat(),
                "remote": git("remote", "get-url", "origin").decode().strip(),
                "head": head, "refs": refs_raw.decode().splitlines(), "shallow": shallow,
                "commit_count": len(commits), "scoped_commit_count": sum(bool(c["changes"]) for c in commits),
                "mandatory_paths": MANDATORY,
                "scope": "All root Markdown, original logs, text/code artifacts under weil_positivity and formal; omit third-party PDFs, zero table, binary arrays and images.",
                "history_limit": "All commits reachable from fetched advertised refs; no claim about deleted, private, unreachable or unadvertised history. Partial clone omits unexamined blobs, not reachable commit history.",
                "hash_domain": "SHA-256 of exact stored bytes; git_blob_oid is Git object identity, not a SHA-256 digest.",
                "http_records": http, "objects": blobs,
                "files": {name: {"raw_file_sha256": sha((OUT / name).read_bytes())}
                          for name in ("refs.txt", "all-commits.tsv", "history.json")}}
    save_json(OUT / "MANIFEST.json", manifest)
    print(json.dumps({"head": head, "refs": manifest["refs"], "shallow": shallow,
                      "commit_count": len(commits), "scoped_commit_count": manifest["scoped_commit_count"],
                      "retained_original_content_blobs": len(blobs), "http_statuses": [r["http_status"] for r in http]}, indent=2))


if __name__ == "__main__":
    main()
