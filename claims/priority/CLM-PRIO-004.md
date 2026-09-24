# Claim Audit: CLM-PRIO-004 - Earliest Exact-Prime Legendre-Schur Method Disclosure

> **Audit Metadata**  
> * **Claim ID**: `CLM-PRIO-004`  
> * **Audit Date**: `2026-09-24T00:00:00Z`  
> * **Audited Source Commit**: `3111accb59df57d7976540bef29d38c817b80825` (`2026-08-21T08:52:52Z`)  
> * **Audited Files**: `findings/2026-08-21T085252Z-component-tail-gram-schur-reduction.md`, `findings/2026-08-21T085252Z-legendre-jump-harmonic-coercivity.md`

---

## 1. Claim Specification

* **Category**: Priority / Public Precedence
* **Candidate Statement**:
  > Earliest public disclosure of an exact-prime Legendre-Schur method combining Legendre harmonic coercivity $J(q) \ge H_N \|q\|_2^2$ with component tail-Gram Schur complement reduction to rigorously prove localized Weil positivity beyond the prime-free regime.
* **Source Anchor Commit**: `3111accb59df57d7976540bef29d38c817b80825` (2026-08-21)

---

## 2. Multi-Anchor Chronology Analysis

| Channel / Repository | Entity | Timestamp (UTC) | Reference |
| :--- | :--- | :--- | :--- |
| Public GitHub Commit | `riemann-conjecture` | `2026-08-21T08:52:52Z` | Commit `3111accb` |
| External arXiv Submission | Marcus Chuk | `2026-08-25T00:00:00Z` | arXiv:2608.24827 |

* **Comparison**: The project's public commit on 2026-08-21 predates external arXiv submissions on certified compact-window Weil positivity.

---

## 3. Audit Verdict & Justification

* **Final Verdict**: `PRIORITY SUPPORTED`
* **Detailed Rationale**:
  * The public Git history confirms that the exact-prime component Schur complement decomposition and Legendre harmonic coercivity were published and accessible on GitHub on 2026-08-21, prior to external preprint postings.
