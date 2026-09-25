# Public Chronology & Multi-Anchor Priority Timeline: Pass 4 Synthesis

> **Timeline Governance & Provenance Metadata**  
> * **Audit Phase**: Pass 4 Phase 5 (Priority & Public Availability Evidence — Verified Security Audit)  
> * **Document Type**: Master Chronological & Multi-Anchor Priority Dossier  
> * **Target Repository**: `https://github.com/PerceivingAI/riemann-conjecture`  
> * **Audited Closed-State Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Audit Date**: `2026-09-25`  
> * **Authoritative Provenance Record**: [`evidence/phase5/github-security-audit-provenance.json`](../phase5/github-security-audit-provenance.json)  
> * **Governing Protocol**: [`TIMELINE_RULES.md`](../../TIMELINE_RULES.md); [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 16 & 17.

---

## 1. Multi-Anchor Evidence Sources & Verification Status

Priority and public disclosure are evaluated across four independent evidentiary anchors:
1. **$T_{\text{repo\_init}}$**: Repository creation date on GitHub (`2026-08-20T20:39:44.018Z`).
2. **$T_{\text{public\_vis}}$**: Repository visibility changed from private to **`PUBLIC`** on GitHub (`2026-08-20T20:43:29.135Z`, verified via GitHub security audit log export `export-PerceivingAI-1790321329.json`).
3. **$T_{\text{commit}}$**: Author and committer timestamps cryptographically sealed in Git commit objects.
4. **$T_{\text{ext\_post}}$**: Official external preprint submission/announcement timestamps (`arXiv:2608.24827v1` submitted `2026-08-25T17:07:51Z`).

### Verified Server-Side Provenance Findings:
* **Public Repository Access**: GitHub's server-side security audit log records that `PerceivingAI/riemann-conjecture` was made **PUBLIC on 2026-08-20T20:43:29.135Z** (3m 45s after creation).
* **Public Commit Visibility**: Because the repository was publicly accessible from August 20, 2026 onward, all commits pushed to `main` during August 20–21, 2026 were publicly visible from their push times:
  - Commit `cc57e70` ($T_{\text{commit}} = \text{2026-08-20T21:17:21Z}$)
  - Commit `64e884b` ($T_{\text{commit}} = \text{2026-08-20T22:44:14Z}$)
  - Commit `1752f19` ($T_{\text{commit}} = \text{2026-08-21T02:26:25Z}$)
  - Commit `fab5933` ($T_{\text{commit}} = \text{2026-08-21T03:45:23Z}$)
  - Commit `3111acc` ($T_{\text{commit}} = \text{2026-08-21T10:28:45Z}$)
  - Commit `6dd1d8f` ($T_{\text{commit}} = \text{2026-08-21T14:05:13Z}$, $T=0.35$ Theorem `C-0050`)
* **Precedence over arXiv:2608.24827**: Public availability of `C-0050` on August 21, 2026 pre-dates Marcus Chuk / Xuefeng Zhu's `arXiv:2608.24827v1` submission (`2026-08-25T17:07:51Z`) by **4.1 days**.

---

## 2. Master Multi-Anchor Priority Table (`CLM-PRIO-001..012` & `CLM-MATH-001`)

| Claim ID | Audited Proposition | Target Anchor Commit | $T_{\text{commit}}$ (UTC) | $T_{\text{public\_vis}}$ (UTC) | External Comparator Anchor | $T_{\text{ext\_post}}$ (UTC) | Priority Verdict (Axis 5) | Final Evidence Disposition (Axis 6) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-PRIO-001` | Fully public open-science research record since creation date | `[Repo Creation]` | `2026-08-20T20:39:44Z` | `2026-08-20T20:43:29Z` (GitHub Public) | N/A (Research Integrity Fact) | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — GitHub security log confirms public visibility since August 20, 2026 at `20:43:29Z`. |
| `CLM-PRIO-002` | Public negative-result and obstruction trail preserved alongside theorems | `[Continuous]` | `2026-08-20` to `2026-09-24` | `2026-08-20T20:43:29Z` (Public) | N/A (Methodological Fact) | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Negative results and obstructions preserved in public Git history. |
| `CLM-PRIO-003` | Public scientific correction trail without history rewriting | `[Continuous]` | `2026-08-20` to `2026-09-24` | `2026-08-20T20:43:29Z` (Public) | N/A (Methodological Fact) | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Linear history with branch protection (`protect-main`) verified in security audit log. |
| `CLM-PRIO-004` | Earliest public exact-prime Legendre-Schur proof of strict localized Weil positivity | `3111accb...` | `2026-08-21T10:28:45Z` | `2026-08-21T10:28:45Z` (Public) | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Public on GitHub on August 21; pre-dates Chuk (Aug 25) by 4.3 days. |
| `CLM-PRIO-005` | Earliest public finite-support Weil positivity theorem at $T=7/20$ (C-0050) | `6dd1d8f0...` | `2026-08-21T14:05:13Z` | `2026-08-21T14:05:13Z` (Public) | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Theorem C-0050 public on GitHub on August 21; pre-dates Chuk (Aug 25) by 4.1 days. |
| `CLM-PRIO-006` | Earliest public sequence of certified localized Weil positivity extending through $T=27/50$ | `51feb3d1...` | `2026-08-26` to `2026-09-24` | `2026-08-26` (Public) | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | **`PRIOR ART FOUND`** | **`COMPLETE`** — Continuation sequence $T \in [0.40, 0.54]$ post-dates Marcus Chuk's August 25 public submission at $L=0.8$. |
| `CLM-PRIO-007` | First exact pole-annihilating shift filter for generalized prime-Laguerre Li sequences | `cc57e703...` | `2026-08-20T21:17:21Z` | `2026-08-20T21:17:21Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Shift filter $T=(E-1)(E-q)$ public on GitHub since August 20, 2026. |
| `CLM-PRIO-008` | First prime-Laguerre RH root criterion after exact zeta-pole subtraction | `cc57e703...` | `2026-08-20T21:17:21Z` | `2026-08-20T21:17:21Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Pole-subtracted root criterion public on GitHub since August 20, 2026. |
| `CLM-PRIO-009` | First interpretation of generalized Li prime kernel as critical-half-weight nonlinear Mellin chirp | `64e884b8...` | `2026-08-20T22:44:14Z` | `2026-08-20T22:44:14Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Mellin chirp formulation public on GitHub since August 20, 2026. |
| `CLM-PRIO-010` | First rank-one Hessian / separability obstruction for Vaughan/Heath-Brown decompositions | `1752f19d...` | `2026-08-21T02:26:25Z` | `2026-08-21T02:26:25Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Rank-1 Hessian obstruction public on GitHub since August 21, 2026. |
| `CLM-PRIO-011` | First conditional-negative-definite / Schoenberg characterization of RH from Li coefficients | `fab5933f...` | `2026-08-21T03:45:23Z` | `2026-08-21T03:45:23Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Schoenberg CND equivalence public on GitHub since August 21, 2026. |
| `CLM-PRIO-012` | First compressed-translation operator treatment making Weil prime-entry thresholds explicit | `fab5933f...` | `2026-08-21T03:45:23Z` | `2026-08-21T03:45:23Z` (Public) | None found in prior literature | N/A | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Compressed translation analysis public on GitHub since August 21, 2026. |
| `CLM-MATH-001` | Strict localized Weil positivity at $(T, N) = (7/20, 32) = (0.35, 32)$ (C-0050) | `6dd1d8f0...` | `2026-08-21T14:05:13Z` | `2026-08-21T14:05:13Z` (Public) | Marcus Chuk (arXiv:2608.24827v1) | `2026-08-25T17:07:51Z` | **`PRIORITY SUPPORTED`** | **`COMPLETE`** — Theorem C-0050 verified and public on August 21, 2026; pre-dates Chuk (Aug 25) by 4.1 days. |
