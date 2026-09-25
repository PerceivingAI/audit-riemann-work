"""Validate Pass 4 accounting without treating inherited verdicts as new evidence."""
from __future__ import annotations

import argparse
import copy
import html
import json
from pathlib import Path
import re
from urllib.parse import unquote

from pass4_preserve import ROOT, SOURCE_PIN, git, hashes, save_json, sha, source_snapshot

FAMILIES = {"MATH": 8, "METH": 5, "OPER": 2, "CONT": 2, "OBST": 15,
            "LAGU": 5, "AIRY": 7, "GRAM": 3, "VERF": 7, "PRIO": 12}
EXPECTED = {f"CLM-{family}-{i:03d}" for family, count in FAMILIES.items() for i in range(1, count + 1)}
AXES = ("validity", "result", "method", "software", "priority")
BASES = {"MACHINE_REPLAY", "INDEPENDENT_DERIVATION", "FORMAL_PROOF_CHECK",
         "SOURCE_DERIVATION_REVIEW", "PRIMARY_LITERATURE_MATCH", "CODE_INSPECTION",
         "HISTORICAL_RECORD", "NOT_INDEPENDENTLY_VERIFIED"}


def cells(line: str) -> list[str]:
    """Split table delimiters outside inline code and $ math; retain TeX verbatim."""
    result, current = [], []
    code = 0
    math = False
    i = 0
    while i < len(line):
        c = line[i]
        escaped = (len(line[:i]) - len(line[:i].rstrip("\\"))) % 2 == 1
        if c == "`" and not escaped and not math:
            n = len(line[i:]) - len(line[i:].lstrip("`"))
            code = 0 if code == n else n if not code else code
            current.append(line[i:i+n]); i += n; continue
        if c == "$" and not escaped and not code:
            math = not math
        if c == "|" and not escaped and not math and not code:
            result.append(html.unescape("".join(current).strip())); current = []
        else:
            current.append(c)
        i += 1
    result.append(html.unescape("".join(current).strip()))
    return result[1:-1]


def rows(text: str) -> list[list[str]]:
    return [cells(line) for line in text.splitlines() if re.match(r"^\| `?CLM-[A-Z]+-\d{3}`? \|", line)]


def key(row: list[str]) -> str:
    return row[0].strip("`")


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_map() -> dict:
    return json.loads(read_text("evidence/phase0/CANDIDATE_MAP.json"))


def slug(text: str) -> str:
    text = text.strip().lower().replace("`", "")
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def reference_error(ref: str) -> str | None:
    if not isinstance(ref, str) or not ref:
        return "missing evidence link"
    path_string, _, anchor = ref.partition("#")
    path = (ROOT / unquote(path_string)).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        return f"missing or invalid referenced file: {ref}"
    if anchor:
        if re.fullmatch(r"L\d+(?:-L\d+)?", anchor):
            lines = path.read_text(encoding="utf-8").splitlines()
            nums = [int(n) for n in re.findall(r"\d+", anchor)]
            if not (1 <= nums[0] <= nums[-1] <= len(lines)):
                return f"invalid line anchor: {ref}"
        else:
            text = path.read_text(encoding="utf-8")
            anchors = {slug(m.group(1)) for m in re.finditer(r"^#{1,6} (.+)$", text, re.M)}
            anchors.update(re.findall(r'<a id="([^"]+)"', text))
            if unquote(anchor) not in anchors:
                return f"missing section anchor: {ref}"
    return None


def validate_candidates(data: dict, documents: dict[str, str], completion: bool = False) -> list[str]:
    errors = []
    tables = {name: rows(text) for name, text in documents.items()}
    for name, table in tables.items():
        ids = [key(row) for row in table]
        if len(ids) != 66 or len(set(ids)) != 66 or set(ids) != EXPECTED:
            errors.append(f"{name}: missing/duplicate/unexpected candidate ID")
    records = data.get("candidates", [])
    ids = [r.get("id") for r in records]
    if len(ids) != 66 or len(set(ids)) != 66 or set(ids) != EXPECTED:
        errors.append("candidate map: missing/duplicate/unexpected candidate ID")
    lookup = {name: {key(row): row for row in table} for name, table in tables.items()}
    baseline = {key(r): r for r in rows(read_text("archive/baselines/pass-3/AUDIT_LEDGER.md"))}
    original = {key(r): r for r in rows(read_text("archive/baselines/pass-3/CLAIMS_TO_AUDIT.md"))}
    for r in records:
        ident = r.get("id", "<missing>")
        inv = lookup["inventory"].get(ident)
        led = lookup["ledger"].get(ident)
        cov = lookup["coverage"].get(ident)
        if inv is None or led is None or cov is None or ident not in baseline or ident not in original:
            continue
        if len(inv) != 6 or len(led) != 14 or len(cov) != 10:
            errors.append(f"{ident}: malformed table row"); continue
        proposition = inv[2]
        digest = sha(proposition.encode("utf-8"))
        if r.get("proposition") != proposition or r.get("proposition_sha256") != digest or inv[2] != original[ident][2]:
            errors.append(f"{ident}: canonical proposition mismatch")
        if r.get("category") != ident.split("-")[1] or led[1] != r.get("category"):
            errors.append(f"{ident}: category mismatch")
        if led[2] != proposition or led[3:5] != inv[1:2] + inv[3:4]:
            errors.append(f"{ident}: ledger proposition/anchor mismatch")
        if r.get("source_ref") != inv[1] or r.get("historical_anchor") != inv[3]:
            errors.append(f"{ident}: source-reference mismatch")
        historical = r.get("baseline", {})
        raw = baseline[ident]
        inherited = [v.strip("`") for v in raw[3:8]] + [re.search(r"`([^`]+)`", raw[8]).group(1)]
        if historical.get("classifications") != inherited or led[5:11] != inherited:
            errors.append(f"{ident}: inherited classification changed")
        if historical.get("rationale") != raw[8]:
            errors.append(f"{ident}: historical rationale altered")
        review = r.get("semantic_review", {})
        if review.get("subject_id") != ident or review.get("proposition_sha256") != digest or not review.get("note"):
            errors.append(f"{ident}: rationale mapped to wrong proposition")
        current = r.get("current_review", {})
        basis = current.get("verification_basis", [])
        if not basis or not set(basis) <= BASES or led[11] != ", ".join(basis):
            errors.append(f"{ident}: invalid verification basis")
        if led[12] != current.get("status") or led[13] != r.get("mapping_record"):
            errors.append(f"{ident}: ledger review/reference mismatch")
        if current.get("status") == "NOT_ADJUDICATED" and cov[1] != "No independent check":
            errors.append(f"{ident}: coverage overstates verification")
        if not r.get("mapping_record") or not r.get("search_record"):
            errors.append(f"{ident}: missing evidence link")
        for ref in (r.get("mapping_record"), r.get("search_record")):
            error = reference_error(ref)
            if error:
                errors.append(f"{ident}: {error}")
            else:
                text = read_text(ref.partition("#")[0])
                section = re.search(rf"^## {re.escape(ident)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
                if not section or f"Subject ID: `{ident}`" not in section[1] or f"Proposition SHA-256: `{digest}`" not in section[1]:
                    errors.append(f"{ident}: dossier/search subject binding mismatch")
                elif ref == r.get("mapping_record") and review.get("note", "") not in section[1]:
                    errors.append(f"{ident}: mapping rationale differs from reviewed record")
        for lead in r.get("historical_leads", []):
            error = reference_error(lead)
            if error: errors.append(f"{ident}: {error}")
        for loc in r.get("source_locations", []):
            error = reference_error(loc.get("ref"))
            if error:
                errors.append(f"{ident}: {error}"); continue
            path = loc["ref"].split("#")[0]
            if not path.startswith("source/riemann-conjecture/") or loc.get("commit") != SOURCE_PIN:
                errors.append(f"{ident}: unpinned source location")
            source_lines = read_text(path).splitlines()
            excerpt = "\n".join(source_lines[loc["start_line"]-1:loc["end_line"]])
            if sha(excerpt.encode("utf-8")) != loc.get("excerpt_sha256"):
                errors.append(f"{ident}: source excerpt mismatch")
        full = r.get("resolved_historical_commit")
        if full and git("-C", "source/riemann-conjecture", "rev-parse", full).decode().strip() != full:
            errors.append(f"{ident}: invalid historical commit")
        strengths = current.get("strength", {})
        obligations = current.get("obligations", {})
        if set(strengths) != set(AXES) or any(v not in {f"E{i}" for i in range(6)} for v in strengths.values()):
            errors.append(f"{ident}: invalid per-axis evidence strength")
        if set(obligations) != set(AXES) or any(not v.get("required_work") for v in obligations.values()):
            errors.append(f"{ident}: missing axis obligation")
        for axis, obligation in obligations.items():
            evidence = obligation.get("evidence", [])
            if obligation.get("state") == "SATISFIED" and not evidence:
                errors.append(f"{ident}: satisfied obligation lacks evidence")
            for ref in evidence:
                error = reference_error(ref)
                if error: errors.append(f"{ident}: {error}")
        if current.get("status") == "VERIFIED":
            if "NOT_INDEPENDENTLY_VERIFIED" in basis or not obligations.get("validity", {}).get("evidence"):
                errors.append(f"{ident}: unsupported VERIFIED promotion")
        if current.get("disposition") == "COMPLETE" or completion:
            if current.get("status") == "NOT_ADJUDICATED" or any(v.get("state") != "SATISFIED" for v in obligations.values()):
                errors.append(f"{ident}: incomplete evidence obligations")
        if cov[2] != ", ".join(basis) or cov[7] != r["mapping_record"]:
            errors.append(f"{ident}: coverage provenance/reference mismatch")
        if cov[8] != "; ".join(f"{a}={strengths.get(a)}" for a in AXES):
            errors.append(f"{ident}: coverage strength mismatch")
        if not cov[9]: errors.append(f"{ident}: remaining work missing")
    return errors


def historical_checks() -> tuple[list[str], dict]:
    errors = []
    manifest = json.loads(read_text("evidence/phase0/PRESERVATION_MANIFEST.json"))
    checked = 0
    for r in manifest["records"]:
        blob = git("rev-parse", f"{r['baseline_commit']}:{r['historical_path']}").decode().strip()
        if blob != r["git_blob_oid"]: errors.append(f"historical blob mismatch: {r['historical_path']}")
        if "stored_path" not in r: continue
        data = (ROOT / r["stored_path"]).read_bytes()
        original = git("cat-file", "blob", blob)
        if sha(original) != r["baseline_blob_sha256"]:
            errors.append(f"historical digest mismatch: {r['stored_path']}")
        if hashes(data) != r["stored_hashes"]:
            errors.append(f"historical working bytes changed: {r['stored_path']}")
        if r["classification"] == "historical_artifact" and r["pass"] == "3":
            same = data.replace(b"\r\n", b"\n") == original.replace(b"\r\n", b"\n")
        else:
            same = data == original
        if not same: errors.append(f"historical completion bytes differ: {r['stored_path']}")
        checked += 1
    plan = manifest["plan_origin"]
    if sha((ROOT / plan["preserved_path"]).read_bytes()) != plan["raw_file_sha256"]:
        errors.append("preserved execution plan changed")
    return errors, {"version_records_checked": len(manifest["records"]), "stored_version_checks": checked}


def execution_hash_checks() -> tuple[list[str], dict]:
    errors, records = [], []
    for path in sorted((ROOT / "evidence/computation-logs").glob("PASS4-*.run.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("hash_domain") != "exact raw file bytes" or not record.get("line_ending_normalization"):
            errors.append(f"missing hash domain: {path.name}")
        for stream in record["streams"].values():
            actual = hashes((ROOT / stream["path"]).read_bytes())
            if any(actual[k] != stream[k] for k in actual):
                errors.append(f"execution stream hash mismatch: {stream['path']}")
        records.append(path.relative_to(ROOT).as_posix())
    return errors, {"execution_records_checked": records}


def pass3_hash_review() -> dict:
    original = json.loads(read_text("evidence/computation-logs/PASS3-REPLAY-MANIFEST.json"))
    records = []
    for run in original["runs"]:
        path = "evidence/computation-logs/" + run["log_file"]
        actual = hashes((ROOT / path).read_bytes())
        records.append({"path": path, "inherited_sha256": run["sha256"], **actual,
                        "matches_raw": run["sha256"] == actual["raw_file_sha256"],
                        "matches_crlf_to_lf": run["sha256"] == actual["normalized_sha256"]})
    return {"scope": "Additive byte-domain examination only; no theorem replay",
            "hash_domain": "raw bytes and CRLF-to-LF-only normalized bytes",
            "original_manifest": "evidence/computation-logs/PASS3-REPLAY-MANIFEST.json",
            "records": records}


def living_link_checks() -> list[str]:
    paths = ["README.md", "SOURCE.md", "AUDIT_PROTOCOL.md", "EVIDENCE_STANDARDS.md",
             "TIMELINE_RULES.md", "AUDIT_LEDGER.md", "EVIDENCE_COVERAGE.md",
             "archive/ERRATA_PASS_1.md", "archive/ERRATA_PASS_2.md", "archive/ERRATA_PASS_3.md",
             "evidence/phase0/PASS4-CANDIDATE-MAPPING.md",
             "evidence/search-records/PASS4-PHASE0-SEARCH-STATUS.md",
             "evidence/search-records/PASS4-PHASE1-CHUK-SOURCES.md",
             "evidence/search-records/PASS4-PHASE1-KUBER-HISTORY.md",
             "evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md",
             "evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md",
             "evidence/literature/PASS_4_PRIOR_ART.md",
             "reports/interim/PASS_4_PHASE_0_REPORT.md",
             "reports/interim/PASS_4_PHASE_1_REPORT.md", "AUDIT_PASS_4.md"]
    errors = []
    for name in paths:
        text = read_text(name)
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text):
            errors.append(f"{name}: invalid control character in a living document")
        for ref in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            if "://" in ref:
                continue
            relative = (Path(name).parent / ref).as_posix()
            error = reference_error(relative)
            if error:
                errors.append(f"{name}: {error}")
    return errors


def documents() -> dict[str, str]:
    return {"inventory": read_text("CLAIMS_TO_AUDIT.md"), "ledger": read_text("AUDIT_LEDGER.md"),
            "coverage": read_text("EVIDENCE_COVERAGE.md")}


def self_test(data: dict, docs: dict) -> list[str]:
    failures = []
    cases = ("missing_id", "duplicate_id", "wrong_proposition", "missing_link", "nonexistent_file",
             "missing_anchor", "wrong_rationale_subject", "unsupported_verified", "unsupported_complete")
    for case in cases:
        changed = copy.deepcopy(data)
        row = changed["candidates"][0]
        if case == "missing_id": changed["candidates"].pop()
        elif case == "duplicate_id": changed["candidates"].append(copy.deepcopy(row))
        elif case == "wrong_proposition": row["proposition"] = "An unrelated assertion"
        elif case == "missing_link": row["search_record"] = ""
        elif case == "nonexistent_file": row["search_record"] = "evidence/nonexistent-pass4-fixture.md"
        elif case == "missing_anchor": row["search_record"] += "-nonexistent"
        elif case == "wrong_rationale_subject": row["semantic_review"]["subject_id"] = "CLM-PRIO-012"
        elif case == "unsupported_verified": row["current_review"]["status"] = "VERIFIED"
        elif case == "unsupported_complete": row["current_review"]["disposition"] = "COMPLETE"
        result = validate_candidates(changed, docs)
        expected = {"missing_id": "missing/duplicate", "duplicate_id": "missing/duplicate",
                    "wrong_proposition": "canonical proposition mismatch", "missing_link": "missing evidence link",
                    "nonexistent_file": "missing or invalid referenced file", "missing_anchor": "missing section anchor",
                    "wrong_rationale_subject": "rationale mapped to wrong proposition",
                    "unsupported_verified": "unsupported VERIFIED promotion", "unsupported_complete": "incomplete evidence obligations"}[case]
        matching = [e for e in result if expected in e]
        print(json.dumps({"mutation": case, "rejected_for_expected_reason": bool(matching), "diagnostics": matching}))
        if not matching: failures.append(f"self-test did not reject {case}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--completion", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--hash-review", action="store_true",
                        help="Record the additive Pass 3 byte-domain examination once")
    args = parser.parse_args()
    if args.hash_review:
        path = ROOT / "evidence/phase0/PASS3_HASH_DOMAINS.json"
        if path.exists():
            parser.error("refusing to overwrite the retained hash-domain examination")
        review = pass3_hash_review()
        save_json(path, review)
        print(json.dumps(review, indent=2))
        return 0 if all(r["matches_raw"] or r["matches_crlf_to_lf"] for r in review["records"]) else 1
    data, docs = load_map(), documents()
    errors = validate_candidates(data, docs, args.completion)
    if args.self_test:
        errors.extend(self_test(data, docs))
    summary = {"candidate_count": len(data["candidates"]), "current_verified": sum(r["current_review"]["status"] == "VERIFIED" for r in data["candidates"]),
               "inherited_classifications_preserved": True, "completion_mode": args.completion}
    if not args.completion:
        hist_errors, hist = historical_checks(); errors.extend(hist_errors); summary.update(hist)
        run_errors, runs = execution_hash_checks(); errors.extend(run_errors); summary.update(runs)
        errors.extend(living_link_checks())
        if json.loads(read_text("evidence/phase0/PASS3_HASH_DOMAINS.json")) != pass3_hash_review():
            errors.append("Pass 3 hash-domain examination no longer matches frozen artifacts")
        before = json.loads(read_text("evidence/phase0/SOURCE_BEFORE.json"))
        after = source_snapshot()
        if before != after: errors.append("frozen source content, refs, or state changed")
        summary["source_unchanged"] = before == after
        summary["source_entries_checked"] = len(after["files_including_ignored"])
    summary["errors"] = errors
    summary["result"] = "FAIL" if errors else "PASS"
    print(json.dumps(summary, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
