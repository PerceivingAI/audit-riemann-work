# Pass 4 Search Record: PASS4-SRCH-001-WEIL-THEOREMS-AND-CONTINUATION

> **Search Execution & Governance Metadata**  
> * **Search Record ID**: `PASS4-SRCH-001-WEIL-THEOREMS-AND-CONTINUATION`  
> * **Date Executed**: `2026-09-25T01:50:00Z` to `02:15:00Z`  
> * **Topic Scope**: Localized Weil Positivity Theorems, Support Continuation, and Moving-Dimension Strategy.  
> * **Associated Candidate IDs**: `CLM-MATH-001`, `CLM-MATH-002`, `CLM-MATH-003`, `CLM-MATH-004`, `CLM-MATH-005`, `CLM-MATH-006`, `CLM-MATH-007`, `CLM-MATH-008`, `CLM-CONT-001`, `CLM-CONT-002`.  
> * **Databases / Engines Queried**: Crossref REST API, GitHub Search API, arXiv Web/API, Project Euclid.  
> * **Governing Standards**: [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) Section 4; [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 12–14.

---

## 1. Database-by-Database Query Logs

### 1.1 Crossref REST API
* **Endpoint**: `https://api.crossref.org/works`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-001-crossref-*.json`
* **Queries & Results**:
  1. `Weil positivity compact support`  
     - Filter: `rows=5` | Returned Count: `989,568` (approximate total) | Status: `200 OK`
     - Shortlisted: Connes & Consani (2021, *Selecta Math.*, DOI: `10.1007/s00029-021-00680-3`).
  2. `explicit formula positive definite compact support`  
     - Filter: `rows=5` | Returned Count: `1,477,945` | Status: `200 OK`
     - Shortlisted: Bombieri (2000, *Rend. Mat. Acc. Lincei*, `RLIN_2000_9_11_3_183_0`).
  3. `Yoshida Hermitian forms attached to zeta functions`  
     - Filter: `rows=5` | Returned Count: `831,583` | Status: `200 OK`
     - Shortlisted: Yoshida (1992, *Adv. Stud. Pure Math.*, DOI: `10.2969/aspm/02110281`).

### 1.2 GitHub Search API
* **Endpoint**: `https://api.github.com/search/repositories`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-001-github-*.json`
* **Queries & Results**:
  1. `Weil positivity Riemann`  
     - Total Results: `7` | Status: `200 OK`
     - Shortlisted: `Kuberwastaken/riemann` (Kuber Mehta), `PerceivingAI/riemann-conjecture`.
  2. `Weil quadratic form support continuation`  
     - Total Results: `0` (Zero-hit novelty boundary).

### 1.3 arXiv & Direct Repository Verification
* **Targets**: `arXiv:2608.24827` (Marcus Chuk / Xuefeng Zhu), `arXiv:2006.13771` (Connes–Consani).
* **Raw Execution Record**: `evidence/phase1/chuk/`
* **Shortlisted**:
  - Marcus Chuk / Xuefeng Zhu (2026, `arXiv:2608.24827v2`): Unconditional certified positivity on $L=0.8$ ($Q(f) \ge 8.9\times 10^{-18} \|f\|_2^2$).

---

## 2. Shortlisted Items & Evidence Dispositions

### Item 1: Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`)
* **Title**: *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*
* **Submission Date**: v1: `2026-08-25T17:07:51Z`, v2: `2026-09-02T17:32:21Z`
* **Disposition**:
  - `POSSIBLY NOVEL` (for `CLM-MATH-001` at $T=0.35$): Local commit `6dd1d8f` (Aug 21) pre-dates Chuk v1 by 4.1 days; public push unverified.
  - `STRONGER RESULT / SAME PHENOMENON` (for `CLM-MATH-002..008` at $T=0.40..0.54$): Pinned commits post-date Chuk v1 (Aug 25); support domain $[-0.54, 0.54]$ is mathematically subsumed by Chuk's $L=0.8$ window.

### Item 2: Hiroyuki Yoshida (1992)
* **Title**: *On Hermitian forms attached to zeta functions* (Adv. Stud. Pure Math. 21, pp. 281–325)
* **Disposition**: `WEAKER RESULT / SAME PHENOMENON`. Proves positivity on prime-free window $T \le \frac{1}{2}\log 2 \approx 0.34657$. `CLM-MATH-001` at $T=0.35$ extends past this boundary.

### Item 3: Kuber Mehta (`Kuberwastaken/riemann`)
* **Title**: *Riemann research archive and laboratory* (GitHub repo, 2026-07-23 to 2026-08-11)
* **Disposition**: `PARTIAL OVERLAP / DIFFERENT REGIME`. Certified positive definiteness on 14D and 22D subspaces at $L=0.45..0.62$; full-space infinite-dimensional theorems explicitly uncertified in `UPDATES.md`.

---

## 3. Claim-by-Claim Search Disposition Summary

| Candidate ID | Target Proposition | Search Evaluation | Disposition Verdict |
| :--- | :--- | :--- | :--- |
| `CLM-MATH-001` | Localized Weil positivity at $T=0.35$ | Commit `6dd1d8f` pre-dates Chuk; exceeds Yoshida prime-free bound ($0.35 > 0.34657$). | `POSSIBLY NOVEL` / `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-MATH-002..008` | Localized Weil positivity at $T \in [0.40, 0.54]$ | Commits post-date Chuk (Aug 25); $[-0.54, 0.54] \subset [-0.8, 0.8]$ subsumed. | `RESULT SUBSUMED BY PRIOR ART` / `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-CONT-001` | Moving-dimension strategy restoring positivity | No prior work implements dimension-scaling on Legendre Schur matrices. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-CONT-002` | Rejection of deceptive floating finite sections | Groskin (2026) analyzes inconclusive band; algorithmic rejection is unique. | `PARTIAL OVERLAP / NOVEL SYNTHESIS SUPPORTED` |

---

## Candidate Claim Search Adjudications

## CLM-MATH-001

- Subject ID: `CLM-MATH-001`
- Proposition SHA-256: `51ab3da81e91a08cc8a318bac80dd83d3b96dcf1c114cd9b60e12f7248f29768`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (7/20, 32) = (0.35, 32)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-002

- Subject ID: `CLM-MATH-002`
- Proposition SHA-256: `7664866123828f4301922bca5be9f091cc83b2cb90fbf32209a9323dbec2c852`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (2/5, 40) = (0.40, 40)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-003

- Subject ID: `CLM-MATH-003`
- Proposition SHA-256: `d0c2c03bb4db5a5fcd3ed885584f145347c10b223d8cc91fd84183e7c0371a0f`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (17/40, 48) = (0.425, 48)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-004

- Subject ID: `CLM-MATH-004`
- Proposition SHA-256: `8f8744c9e3d341fd84a95570d3abd9be2ebbb33e8a29fde74d580cdfb2890179`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (9/20, 56) = (0.45, 56)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-005

- Subject ID: `CLM-MATH-005`
- Proposition SHA-256: `566b682940d905d18975f003ff056ad9ea151638c819ecced15a0d171103de17`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (19/40, 68) = (0.475, 68)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-006

- Subject ID: `CLM-MATH-006`
- Proposition SHA-256: `f23c311fc7f3074319c5bb165cfc7e4056a7f7ffe7f173ce8914323d3702cb2d`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (1/2, 80) = (0.50, 80)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-007

- Subject ID: `CLM-MATH-007`
- Proposition SHA-256: `a430730d11dc2dc140e4cbba46d3d6c9b57f6a7611cca135706ee90807105d3e`
- Canonical Proposition: Strict localized Weil positivity at $(T, N) = (21/40, 96) = (0.525, 96)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-MATH-008

- Subject ID: `CLM-MATH-008`
- Proposition SHA-256: `0f43fd298c2229d016d3f0b9edfc78676030a8e6660958e96adf7d081c57d1fa`
- Canonical Proposition: Strict localized Weil positivity at frontier $(T, N) = (27/50, 104) = (0.54, 104)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-CONT-001

- Subject ID: `CLM-CONT-001`
- Proposition SHA-256: `2b9000afb7d355d54177b3be6e4d3152383567baa56609aca1fbdf6614fc6bea`
- Canonical Proposition: Moving-dimension strategy: increasing $N$ restores rigorous positivity as $T$ grows.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-CONT-002

- Subject ID: `CLM-CONT-002`
- Proposition SHA-256: `cc220e6fc67683051ac80a4f20e181210be642aff0528e2dca29b280cf39ebb9`
- Canonical Proposition: Rigorous rejection of deceptive floating/truncated finite sections.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

