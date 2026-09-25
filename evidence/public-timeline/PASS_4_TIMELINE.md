# Public Chronology & Multi-Anchor Priority Timeline: Pass 4 Synthesis

> **Timeline Governance & Provenance Metadata**  
> * **Audit Phase**: Pass 4 Phase 5 (Priority & Public Availability Evidence)  
> * **Document Type**: Master Chronological & Multi-Anchor Priority Dossier  
> * **Target Repository**: `https://github.com/PerceivingAI/riemann-conjecture`  
> * **Audited Closed-State Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Audit Date**: `2026-09-25`  
> * **Governing Protocol**: [`TIMELINE_RULES.md`](../../TIMELINE_RULES.md); [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 16 & 17.

---

## 1. Multi-Anchor Evidence Sources & Verification Status

Priority and public disclosure are evaluated across four independent evidentiary anchors:
1. **$T_{\text{repo\_init}}$**: Repository creation date on GitHub (`2026-08-20T20:39:42Z`, verified via GitHub API).
2. **$T_{\text{commit}}$**: Author and committer timestamps cryptographically sealed in Git commit objects.
3. **$T_{\text{public\_push}}$**: Independent public push witness records (GH Archive, Software Heritage, Wayback Machine, public forks).
4. **$T_{\text{ext\_post}}$**: Official external preprint submission/announcement timestamps (e.g. arXiv records).

### Summary of Third-Party Archive Search Results:
* **GitHub REST API**: Verified repository `created_at` (`2026-08-20T20:39:42Z`) and commit log of 70 public commits (`evidence/phase5/github-repo-meta.json`).
* **GH Archive Datasets**: Downloaded and scanned hourly datasets for August 20, 2026 (hours 20, 21, 22) and August 21, 2026 (hour 14, 37,815 events scanned). No matching `PushEvent` was captured in the archive datasets for `PerceivingAI/riemann-conjecture`.
* **Software Heritage**: Visited API endpoint `https://archive.softwareheritage.org/api/1/origin/.../visits/` (Status `404 Not Found`, unarchived origin).
* **Wayback Machine**: Queried Internet Archive availability API (Status `200`, `archived_snapshots: {}`, no historical web crawls captured).

**Evidentiary Standard**: Per [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 16, a null search indicates that the queried archive did not record the event; it does not prove the event did not occur. However, without third-party push witnesses, local Git commit timestamps can only establish **`PRIORITY PLAUSIBLE`** rather than `PRIORITY SUPPORTED`.

---

## 2. Master Multi-Anchor Priority Table (`CLM-PRIO-001..012`)

| Claim ID | Audited Proposition | Target Anchor Commit | $T_{\text{commit}}$ (UTC) | $T_{\text{public\_push}}$ Status | External Comparator Anchor | $T_{\text{ext\_post}}$ (UTC) | Priority Verdict (Axis 5) | Final Evidence Disposition (Axis 6) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-PRIO-001` | Fully public open-science research record since creation date | `[Repo Creation]` | `2026-08-20T20:39:42Z` | Unverified by 3rd party archives | N/A (Research Integrity Fact) | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — GitHub API records creation at `20:39:42Z`. Third-party public push logs unverified. |
| `CLM-PRIO-002` | Public negative-result and obstruction trail preserved alongside theorems | `[Continuous]` | `2026-08-20` to `2026-09-24` | Unverified by 3rd party archives | N/A (Methodological Fact) | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Negative results preserved in Git history; external push timestamps unverified. |
| `CLM-PRIO-003` | Public scientific correction trail without history rewriting | `[Continuous]` | `2026-08-20` to `2026-09-24` | Unverified by 3rd party archives | N/A (Methodological Fact) | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Preserved linear Git history; third-party push unverified. |
| `CLM-PRIO-004` | Earliest public exact-prime Legendre-Schur proof of strict localized Weil positivity | `3111accb...` | `2026-08-21T10:28:45Z` | Unverified by 3rd party archives | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `3111accb` (Aug 21) pre-dates Chuk (Aug 25) by 4.3 days; public push unverified. |
| `CLM-PRIO-005` | Earliest public finite-support Weil positivity theorem at $T=7/20$ (C-0050) | `6dd1d8f0...` | `2026-08-21T14:05:13Z` | Unverified by 3rd party archives | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `6dd1d8f` (Aug 21) pre-dates Chuk (Aug 25) by 4.1 days; public push unverified. |
| `CLM-PRIO-006` | Earliest public sequence of certified localized Weil positivity extending through $T=27/50$ | `51feb3d1...` | `2026-08-26` to `2026-09-24` | Public on GitHub | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | **`PRIOR ART FOUND`** | **`COMPLETE`** — Continuation sequence $T \in [0.40, 0.54]$ post-dates Marcus Chuk's August 25 public submission at $L=0.8$. |
| `CLM-PRIO-007` | First exact pole-annihilating shift filter for generalized prime-Laguerre Li sequences | `cc57e703...` | `2026-08-20T21:17:21Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `cc57e70` (Aug 20); public push unverified. |
| `CLM-PRIO-008` | First prime-Laguerre RH root criterion after exact zeta-pole subtraction | `cc57e703...` | `2026-08-20T21:17:21Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `cc57e70` (Aug 20); public push unverified. |
| `CLM-PRIO-009` | First interpretation of generalized Li prime kernel as critical-half-weight nonlinear Mellin chirp | `64e884b8...` | `2026-08-20T22:44:14Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `64e884b` (Aug 20); public push unverified. |
| `CLM-PRIO-010` | First rank-one Hessian / separability obstruction for Vaughan/Heath-Brown decompositions | `1752f19d...` | `2026-08-21T02:26:25Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `1752f19` (Aug 21); public push unverified. |
| `CLM-PRIO-011` | First conditional-negative-definite / Schoenberg characterization of RH from Li coefficients | `fab5933f...` | `2026-08-21T03:45:23Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `fab5933` (Aug 21); public push unverified. |
| `CLM-PRIO-012` | First compressed-translation operator treatment making Weil prime-entry thresholds explicit | `fab5933f...` | `2026-08-21T03:45:23Z` | Unverified by 3rd party archives | None found in prior literature | N/A | `PRIORITY PLAUSIBLE` | **`INCONCLUSIVE — REQUIRES LATER PASS`** — Git commit `fab5933` (Aug 21); public push unverified. |
