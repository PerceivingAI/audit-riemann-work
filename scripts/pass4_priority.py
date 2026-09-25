"""Query and document public chronology and third-party archive witnesses for Phase 5.

Queries:
1. GitHub REST API (repo metadata, commit endpoints).
2. GH Archive public event datasets for August 20-21, 2026.
3. Software Heritage API origin visits.
4. Internet Archive / Wayback Machine availability API.

Saves raw response artifacts, query URLs, returned timestamps, and SHA-256 hashes.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/phase5"
CACHE = ROOT / ".audit-cache/phase5"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"Refusing to overwrite existing evidence: {path}")
    else:
        path.write_bytes(data)


def save_json(path: Path, data: object) -> None:
    save(path, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def fetch_url(url: str, dest_name: str, cache_only: bool = False, delay: float = 1.0) -> dict:
    started = datetime.now(timezone.utc).isoformat()
    time.sleep(delay)
    req = urllib.request.Request(url, headers={"User-Agent": "Riemann-Audit-Pass4 (academic-audit; mailto:audit@example.org)", "Accept": "application/json, */*"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            status = resp.status
            headers = dict(resp.headers)
            final_url = resp.url
    except urllib.error.HTTPError as err:
        data = err.read()
        status = err.code
        headers = dict(err.headers)
        final_url = err.url
    except Exception as exc:
        data = str(exc).encode("utf-8")
        status = 599
        headers = {}
        final_url = url
    target_dir = CACHE if cache_only else OUT
    target_path = target_dir / dest_name
    save(target_path, data)
    return {
        "url": url,
        "final_url": final_url,
        "retrieved_at_start": started,
        "retrieved_at_end": datetime.now(timezone.utc).isoformat(),
        "http_status": status,
        "size_bytes": len(data),
        "raw_file_sha256": sha(data),
        "stored_path": target_path.relative_to(ROOT).as_posix(),
        "cache_only": cache_only,
    }


def search_gharchive_hourly(hour_str: str, repo_name: str) -> dict:
    """Download and query an hourly GH Archive dataset for repository events."""
    url = f"https://data.gharchive.org/{hour_str}.json.gz"
    dest_gz = CACHE / f"gharchive-{hour_str}.json.gz"
    print(f"Querying GH Archive dataset: {url}...")
    
    started = datetime.now(timezone.utc).isoformat()
    req = urllib.request.Request(url, headers={"User-Agent": "Riemann-Audit-Pass4 (academic-audit)"})
    matching_events = []
    total_events_in_hour = 0
    download_success = False
    http_status = 0
    gz_bytes = b""
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            gz_bytes = resp.read()
            http_status = resp.status
            download_success = True
            save(dest_gz, gz_bytes)
            
            # Decompress and scan line by line
            decompressed = gzip.decompress(gz_bytes)
            for line in decompressed.decode("utf-8", errors="replace").splitlines():
                if not line.strip(): continue
                total_events_in_hour += 1
                try:
                    event = json.loads(line)
                    event_repo = event.get("repo", {}).get("name", "")
                    if repo_name.lower() in event_repo.lower():
                        matching_events.append(event)
                except Exception:
                    pass
    except urllib.error.HTTPError as err:
        http_status = err.code
        gz_bytes = err.read()
    except Exception as exc:
        http_status = 599
        gz_bytes = str(exc).encode()

    result_json = {
        "hour": hour_str,
        "url": url,
        "http_status": http_status,
        "download_success": download_success,
        "dataset_sha256": sha(gz_bytes) if download_success else None,
        "dataset_size_bytes": len(gz_bytes),
        "total_events_scanned": total_events_in_hour,
        "matching_events_count": len(matching_events),
        "matching_events": matching_events,
    }
    
    out_file = OUT / f"gharchive-{hour_str}-results.json"
    save_json(out_file, result_json)
    return result_json


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", required=True)
    parser.parse_args()
    if (OUT / "MANIFEST.json").exists():
        raise SystemExit("Refusing to overwrite completed Phase 5 priority manifest")

    started = datetime.now(timezone.utc).isoformat()
    repo_target = "PerceivingAI/riemann-conjecture"
    records = []

    # 1. GitHub API Queries
    print("1. Querying GitHub API...")
    records.append(fetch_url(f"https://api.github.com/repos/{repo_target}", "github-repo-meta.json"))
    records.append(fetch_url(f"https://api.github.com/repos/{repo_target}/commits?per_page=100", "github-repo-commits.json"))
    records.append(fetch_url(f"https://api.github.com/repos/{repo_target}/events?per_page=100", "github-repo-events.json"))
    records.append(fetch_url(f"https://api.github.com/repos/{repo_target}/tags", "github-repo-tags.json"))
    records.append(fetch_url(f"https://api.github.com/repos/{repo_target}/releases", "github-repo-releases.json"))

    # 2. Software Heritage API Queries
    print("2. Querying Software Heritage API...")
    sh_origin = f"https://archive.softwareheritage.org/api/1/origin/https://github.com/{repo_target}/visits/"
    records.append(fetch_url(sh_origin, "software-heritage-visits.json"))

    # 3. Wayback Machine Availability API
    print("3. Querying Wayback Machine Availability API...")
    wayback_url = f"https://archive.org/wayback/available?url=https://github.com/{repo_target}"
    records.append(fetch_url(wayback_url, "wayback-availability.json"))

    # 4. GH Archive Datasets for Target UTC Hours (August 20, 21, 2026)
    print("4. Querying GH Archive event datasets...")
    target_hours = [
        "2026-08-20-20", # Repo creation hour (2026-08-20T20:39:42Z)
        "2026-08-20-21", # First commit series (cc57e703 at 2026-08-20T21:17:21Z)
        "2026-08-20-22", # Second commit series (64e884b8 at 2026-08-20T22:44:14Z)
        "2026-08-21-03", # fab5933 at 2026-08-21T03:45:23Z
        "2026-08-21-14", # 6dd1d8f at 2026-08-21T14:05:13Z (C-0050 theorem)
    ]
    
    gharchive_results = []
    for h in target_hours:
        res = search_gharchive_hourly(h, repo_target)
        gharchive_results.append(res)

    manifest = {
        "manifest_version": 1,
        "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "target_repository": repo_target,
        "http_records": records,
        "gharchive_hours_scanned": gharchive_results,
    }
    
    save_json(OUT / "MANIFEST.json", manifest)
    print(json.dumps({
        "status": "PASS",
        "target_repository": repo_target,
        "records_count": len(records),
        "gharchive_scans_count": len(gharchive_results),
        "manifest_path": (OUT / "MANIFEST.json").relative_to(ROOT).as_posix()
    }, indent=2))


if __name__ == "__main__":
    main()
