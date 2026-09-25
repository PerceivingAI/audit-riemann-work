# Pass 3 Literature & Repository Search Record: PASS3-SRCH-001-COMPARATORS

> **Search Record Metadata**  
> * **Search ID**: `PASS3-SRCH-001-COMPARATORS`  
> * **Standard**: Reproducible Search Record per [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) & [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md)  
> * **Target Scope**: Contemporary Comparators: `Kuberwastaken/riemann` (July 2026) and Marcus Chuk (`arXiv:2608.24827`, August 2026)  
> * **Access Date / Time**: `2026-09-24T22:25:00Z`  
> * **Auditor**: Independent Audit Pass 3 Team

---

## 1. Search Query Executions & Hit Counts

### Query 1.1: `Kuberwastaken/riemann` Repository Identification
* **Database / Engine**: GitHub API & Web Index
* **Exact Query String**: `"Kuberwastaken" riemann OR "kuberwastaken/riemann" OR "kuberwastaken" site:github.com`
* **Filters Applied**: `site:github.com`, `language:Any`, `type:Repository`
* **Total Results Returned**: **12 hits**
* **Shortlisted Items Inspected**:
  1. `https://github.com/Kuberwastaken/riemann` (Primary repository root)
  2. `README.md` (Project overview and scope)
  3. `CITATION.cff` (Release Date: `2026-07-23`, Author: Kuber Mehta)
  4. `FINDINGS.md` (Consolidated numerical & interval results)
  5. `experiments/README.md` & `experiments/weil_positivity/` (Arb ball arithmetic scripts)
  6. `logs/LOG.md` (Experiment logs, explicit-formula validation)
  7. `UPDATES.md` (Status of finite-dimensional vs. full-space continuation)
* **Relevance & Normalization Assessment**:
  - Confirmed repository release date of **July 23, 2026**.
  - Confirmed certified results are strictly **finite-dimensional** (e.g. 14D and 22D test function families at $L=0.45..0.62$).
  - Confirmed infinite-dimensional spectral/tail bounds were uncertified.

### Query 1.2: `Kuberwastaken/riemann` Method Keyword Scan
* **Database / Engine**: GitHub Repository Search within `Kuberwastaken/riemann`
* **Exact Query String**: `site:github.com/Kuberwastaken/riemann "Weil" OR "positivity" OR "Legendre" OR "Arb" OR "experiments"`
* **Filters Applied**: Repository-restricted code & markdown search
* **Total Results Returned**: **7 hits**
* **Shortlisted Items Inspected**:
  1. `experiments/weil_positivity/RESULTS.md`
  2. `experiments/weil_positivity/certify.py`
  3. `experiments/weil_positivity/PROOF-c0.md`
  4. `logs/LOG.md`
  5. `FINDINGS.md`
  6. `UPDATES.md`
  7. `CONTINUATION.md`
* **Logged Null Query**: `site:github.com/Kuberwastaken/riemann "harmonic coercivity" OR "Schur complement" OR "exact-prime"` $	o$ **0 hits (Null Search Logged)**.
* **Finding**: `Kuberwastaken/riemann` did not employ Legendre harmonic coercivity or component tail-Gram Schur reductions.

### Query 1.3: Marcus Chuk (`arXiv:2608.24827`)
* **Database / Engine**: arXiv (math.NT), Crossref, Google Scholar
* **Exact Query String**: `"2608.24827" OR "Marcus Chuk" "Weil positivity in compact windows"`
* **Filters Applied**: Date: `2026-08-01` to `2026-09-24`, Category: `math.NT`, `math.CA`
* **Total Results Returned**: **13 hits**
* **Shortlisted Items Inspected**:
  1. Marcus Chuk, *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*, arXiv:2608.24827v1 (Submitted `2026-08-25T11:42:00Z`).
  2. arXiv:2608.24827v2 (Revised `2026-09-04`).
* **Relevance & Normalization Assessment**:
  - Full-space unconditional certified positivity at $L=0.8$: $Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2$.
  - Discretization via Gauss-Legendre quadrature + spherical Bessel recurrences with interval arithmetic matrix enclosures.
  - Distinct certified proof architecture from `riemann-conjecture`'s exact rational Schur reduction.
