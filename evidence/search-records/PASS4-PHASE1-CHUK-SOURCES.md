# Pass 4 Phase 1 Search Record: Primary Comparator Literature (`PASS4-SRCH-CHUK-SOURCES`)

> **Search Execution Metadata**  
> * **Search Record ID**: `PASS4-SRCH-CHUK-SOURCES`  
> * **Date Executed**: `2026-09-25T01:50:00Z` to `02:15:00Z`  
> * **Auditor / Scope**: Official Primary Literature Inspection for Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`), Masatoshi Suzuki (`arXiv:2606.09096`), Alain Groskin (`arXiv:2607.02828`), and Connes–Consani–Moscovici (`arXiv:2511.22755`).  
> * **Databases / Services Queried**: arXiv API / Web, DataCite DOI Resolver, Project Euclid.  
> * **Governing Standards**: [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) Section 4; [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 12 & 13.

---

## 1. Database-by-Database Query Logs

### Database: arXiv API & Web Interface

#### Query 1.1: Marcus Chuk / Xuefeng Zhu
* **Target URL**: `https://arxiv.org/abs/2608.24827` (v1 and v2 endpoints)
* **Execution Timestamp**: `2026-09-25T02:00:15Z`
* **Query / Identifier**: `arXiv:2608.24827`
* **HTTP Status**: `200 OK`
* **Raw Artifacts Retained**:
  - Abstract HTML: `evidence/phase1/chuk/arxiv-2608.24827-abs.html` (SHA-256: `955745f62df9a572a153406322ad1ebfa4d2be7338e5a7a72d7f8d6896253457`)
  - Full HTML: `.audit-cache/phase1/chuk/arxiv-2608.24827v2-full.html` (SHA-256: `a91fffc5a8731fe7b2bc212c4b7b2585f679fe266c1f07f59d57a4e69b0fa8ff`)
  - Source e-print tar: `.audit-cache/phase1/chuk/arxiv-2608.24827v2-source.tar.gz` (SHA-256: `1afc4e867bc69cabf5128db8b70187af61804e55bd773a16cdf16d17c4284c73`)
* **Items Shortlisted**:
  1. `arXiv:2608.24827v1` (Marcus Chuk, Aug 25, 2026, 9-page announcement)
  2. `arXiv:2608.24827v2` (Xuefeng Zhu, Sep 2, 2026, 34-page full article)
* **Disposition**: `STRONGER RESULT / DIFFERENT METHOD` (for $T \in [0.40, 0.54]$). Proves full-space positivity at $L=0.8$ ($Q(f) \ge 8.9\times 10^{-18} \|f\|_2^2$).

#### Query 1.2: Masatoshi Suzuki (Screw Function Form)
* **Target URL**: `https://arxiv.org/abs/2606.09096`
* **Execution Timestamp**: `2026-09-25T02:00:16Z`
* **Query / Identifier**: `arXiv:2606.09096`
* **HTTP Status**: `200 OK`
* **Raw Artifact Retained**: `evidence/phase1/chuk/arxiv-2606.09096-abs.html` (SHA-256: `6508931165be812bb0364d930263625fdfc5d27b9c614b62dbce25813e33f3eb`)
* **Disposition**: `KNOWN INGREDIENT / NOVEL SYNTHESIS SUPPORTED`. Provides screw function formulation and residual kernel properties; distinct from exact-prime Legendre-Schur reduction.

#### Query 1.3: Alain Groskin (Truncated Weil Form)
* **Target URL**: `https://arxiv.org/abs/2607.02828`
* **Execution Timestamp**: `2026-09-25T02:00:16Z`
* **Query / Identifier**: `arXiv:2607.02828`
* **HTTP Status**: `200 OK`
* **Raw Artifact Retained**: `evidence/phase1/chuk/arxiv-2607.02828-abs.html` (SHA-256: `813bbd8e03e2c39d893cf1166a9b40ca0c087cae12739eb395bb2d7ea278f244`)
* **Disposition**: `PARTIAL OVERLAP`. Quantifies archimedean tail orders and truncation artifacts for finite sections.

#### Query 1.4: Connes, Consani, Moscovici (Zeta Spectral Triples)
* **Target URL**: `https://arxiv.org/abs/2511.22755`
* **Execution Timestamp**: `2026-09-25T02:00:16Z`
* **Query / Identifier**: `arXiv:2511.22755`
* **HTTP Status**: `200 OK`
* **Raw Artifact Retained**: `evidence/phase1/chuk/arxiv-2511.22755-abs.html` (SHA-256: `a937a07be6160da2f099719eb793ef1ef974955b271d5300be58d415e61fb196`)
* **Disposition**: `DIFFERENT FUNCTION SPACE / OPERATOR FRAME`. Operator-theoretic framework constructing self-adjoint triples from finite-section Weil form restrictions.
