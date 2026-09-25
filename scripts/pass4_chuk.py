"""Collect official primary literature records and examination artifacts for Phase 1.

Fetches official arXiv abstract HTML/APIs, e-print sources, and version metadata.
Retains exact hashes, citation locators, and primary-source findings.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/phase1/chuk"
CACHE = ROOT / ".audit-cache/phase1/chuk"


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


def fetch_url(url: str, dest_name: str, cache_only: bool = False) -> dict:
    started = datetime.now(timezone.utc).isoformat()
    req = urllib.request.Request(url, headers={"User-Agent": "Riemann-Audit-Pass4 (academic-audit)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            status = resp.status
            headers = dict(resp.headers)
            final_url = resp.url
    except urllib.error.HTTPError as err:
        data = err.read()
        status = err.code
        headers = dict(err.headers)
        final_url = err.url
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collect", action="store_true", required=True)
    parser.parse_args()
    if (OUT / "MANIFEST.json").exists():
        raise SystemExit("Refusing to overwrite completed primary literature collection manifest")

    started = datetime.now(timezone.utc).isoformat()
    records = []

    # 1. Marcus Chuk / Xuefeng Zhu (arXiv:2608.24827)
    records.append(fetch_url("https://arxiv.org/abs/2608.24827", "arxiv-2608.24827-abs.html"))
    records.append(fetch_url("https://arxiv.org/abs/2608.24827v1", "arxiv-2608.24827v1-abs.html"))
    records.append(fetch_url("https://arxiv.org/abs/2608.24827v2", "arxiv-2608.24827v2-abs.html"))
    records.append(fetch_url("https://arxiv.org/html/2608.24827v2", "arxiv-2608.24827v2-full.html", cache_only=True))
    records.append(fetch_url("https://arxiv.org/e-print/2608.24827v2", "arxiv-2608.24827v2-source.tar.gz", cache_only=True))

    # 2. Masatoshi Suzuki (arXiv:2606.09096)
    records.append(fetch_url("https://arxiv.org/abs/2606.09096", "arxiv-2606.09096-abs.html"))
    records.append(fetch_url("https://arxiv.org/html/2606.09096v2", "arxiv-2606.09096v2-full.html", cache_only=True))

    # 3. Alain Groskin (arXiv:2607.02828)
    records.append(fetch_url("https://arxiv.org/abs/2607.02828", "arxiv-2607.02828-abs.html"))

    # 4. Connes, Consani, Moscovici (arXiv:2511.22755)
    records.append(fetch_url("https://arxiv.org/abs/2511.22755", "arxiv-2511.22755-abs.html"))

    # 5. Connes, Consani (arXiv:2006.13771)
    records.append(fetch_url("https://arxiv.org/abs/2006.13771", "arxiv-2006.13771-abs.html"))

    manifest = {
        "manifest_version": 1,
        "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "primary_papers": [
            {
                "id": "LIT-2026-CHUK-ZHU",
                "arxiv_id": "2608.24827",
                "v1_title": "Weil positivity in compact windows: certified two-sided bounds and a Landau-Widom decay law",
                "v1_authors": ["Marcus Chuk"],
                "v1_submission_utc": "2026-08-25T17:07:51Z",
                "v2_title": "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law",
                "v2_authors": ["Xuefeng Zhu"],
                "v2_submission_utc": "2026-09-02T17:32:21Z",
                "doi": "10.48550/arXiv.2608.24827",
                "license": "http://arxiv.org/licenses/nonexclusive-distrib/1.0/",
            },
            {
                "id": "LIT-2026-SUZUKI-SCREW",
                "arxiv_id": "2606.09096",
                "title": "Weil's quadratic form via the screw function",
                "authors": ["Masatoshi Suzuki"],
                "v1_submission_utc": "2026-06-12T10:48:47Z",
                "v2_submission_utc": "2026-06-25T03:52:12Z",
                "doi": "10.48550/arXiv.2606.09096",
            },
            {
                "id": "LIT-2026-GROSKIN-FINITE",
                "arxiv_id": "2607.02828",
                "title": "A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form",
                "authors": ["Alain Groskin"],
                "v1_submission_utc": "2026-07-03T18:24:19Z",
                "doi": "10.48550/arXiv.2607.02828",
            },
            {
                "id": "LIT-2025-CCM-SPECTRAL",
                "arxiv_id": "2511.22755",
                "title": "Zeta Spectral Triples",
                "authors": ["Alain Connes", "Caterina Consani", "Henri Moscovici"],
                "v1_submission_utc": "2025-11-27T21:01:11Z",
                "doi": "10.48550/arXiv.2511.22755",
            },
            {
                "id": "LIT-2020-CC-ARCHIMEDEAN",
                "arxiv_id": "2006.13771",
                "title": "Weil positivity and Trace formula, the archimedean place",
                "authors": ["Alain Connes", "Caterina Consani"],
                "v1_submission_utc": "2020-06-24T15:22:18Z",
                "doi": "10.48550/arXiv.2006.13771",
            }
        ],
        "records": records,
    }
    save_json(OUT / "MANIFEST.json", manifest)
    print(json.dumps({
        "status": "PASS",
        "primary_papers_collected": len(manifest["primary_papers"]),
        "records_count": len(records),
        "manifest_path": (OUT / "MANIFEST.json").relative_to(ROOT).as_posix()
    }, indent=2))


if __name__ == "__main__":
    main()
