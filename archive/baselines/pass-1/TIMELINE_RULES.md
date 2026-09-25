# Priority & Timeline Rules

This document establishes the multi-anchor chronological framework used to evaluate priority and public disclosure claims.

---

## 1. Multi-Anchor Chronology Framework

Priority comparisons must not compare disparate disclosure channels asymmetrically (e.g., comparing a private Git commit date against a peer-reviewed print date, or an arXiv submission date against a repository initial commit).

For any priority determination, the audit must capture and distinguish the following discrete timestamps:

```text
Source Repository Anchors:
  T_repo_init    : Public creation date of the source repository
  T_commit_orig  : Git commit timestamp (author & committer) introducing the exact result
  T_public_push  : First verifiable public push / availability of that commit
  T_public_snap  : Earliest independent web crawl (e.g., Wayback Machine, GitHub archive)

External Comparative Anchors:
  T_ext_sub      : External preprint/paper formal submission date
  T_ext_post     : External preprint first public posting date (e.g., arXiv announcement)
  T_ext_pub      : External formal journal publication date (online first or volume print)
  T_ext_code     : External public code repository disclosure timestamp
```

---

## 2. Priority Precedence Rules

To establish whether priority is `PRIORITY SUPPORTED`, `PRIORITY PLAUSIBLE`, or `PRIOR ART FOUND`:

### Rule 1: Public Availability is the Benchmark
* A private internal commit timestamp ($T_{\text{commit\_orig}}$) without public disclosure cannot claim priority over a public external posting ($T_{\text{ext\_post}}$).
* Priority requires $T_{\text{public\_push}} < T_{\text{ext\_post}}$.

### Rule 2: Symmetric Comparison
* If comparing against an arXiv preprint: Compare the arXiv public announcement date ($T_{\text{ext\_post}}$) against the public Git availability date ($T_{\text{public\_push}}$).
* If comparing against a journal article without preprint: Compare the official online publication date ($T_{\text{ext\_pub}}$) against $T_{\text{public\_push}}$.

### Rule 3: Content Specificity
* Priority applies only to the specific mathematical theorem, bound, or code implementation present in the earlier commit.
* Subsequent additions, refinements, or corrections in later commits carry their own later timestamps.

---

## 3. Timeline Verification Table Schema

Every priority evaluation in `claims/priority/` must include a multi-anchor timeline table:

| Event Description | Channel / Repository | Anchor Symbol | Timestamp (UTC) | Verification Source / Hash |
| :--- | :--- | :--- | :--- | :--- |
| Source Initial Public Creation | GitHub (`riemann-conjecture`) | $T_{\text{repo\_init}}$ | `YYYY-MM-DD HH:MM:SS` | Git commit / GitHub API log |
| Earliest Result Commit | GitHub (`riemann-conjecture`) | $T_{\text{commit\_orig}}$ | `YYYY-MM-DD HH:MM:SS` | Commit SHA `3111accb...` |
| First Verified Public Push | GitHub / Web Archive | $T_{\text{public\_push}}$ | `YYYY-MM-DD HH:MM:SS` | Public push log / archive URL |
| External Preprint Submission | arXiv | $T_{\text{ext\_sub}}$ | `YYYY-MM-DD HH:MM:SS` | arXiv submission header |
| External Public Announcement | arXiv | $T_{\text{ext\_post}}$ | `YYYY-MM-DD HH:MM:SS` | arXiv announcement date |
| External Formal Publication | Journal | $T_{\text{ext\_pub}}$ | `YYYY-MM-DD` | Journal DOI metadata |
