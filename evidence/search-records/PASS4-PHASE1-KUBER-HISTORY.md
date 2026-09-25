# Pass 4 Phase 1 Search Record: Kuber Mehta Git History (`PASS4-SRCH-KUBER-HISTORY`)

> **Search Execution Metadata**  
> * **Search Record ID**: `PASS4-SRCH-KUBER-HISTORY`  
> * **Date Executed**: `2026-09-25T01:45:00Z` to `02:10:00Z`  
> * **Auditor / Scope**: Commit-level historical reconstruction of `https://github.com/Kuberwastaken/riemann`.  
> * **Databases / Services Queried**: GitHub REST API v3, Git Object Store (bare mirror & full tree clone).  
> * **Governing Standards**: [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) Section 4; [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 9 & 10.

---

## 1. Query Formulations & API Response Records

### Service: GitHub REST API (Repo Metadata)
* **Endpoint**: `https://api.github.com/repos/Kuberwastaken/riemann`
* **Query Timestamp**: `2026-09-25T01:46:00Z`
* **HTTP Status**: `200 OK`
* **Raw Artifact Retained**: `evidence/phase1/kuber/github-repository.json` (SHA-256: `7d00f53eb3c4f74d47eb38b97c45831ea236a287fa837bfdb3c7e750e065aa87`)
* **Key Fields Verified**:
  - `created_at`: `2026-07-23T10:22:27Z`
  - `pushed_at`: `2026-08-11T20:32:37Z`
  - `default_branch`: `main`

### Service: GitHub REST API (Branches & Tags)
* **Endpoints**: `.../branches?per_page=100`, `.../tags?per_page=100`
* **Query Timestamp**: `2026-09-25T01:46:01Z`
* **HTTP Status**: `200 OK`
* **Raw Artifacts Retained**:
  - `evidence/phase1/kuber/github-branches.json` (SHA-256: `a937a07be6160da2f099719eb793ef1ef974955b271d5300be58d415e61fb196`)
  - `evidence/phase1/kuber/github-tags.json` (SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`)
* **Key Fields Verified**: 1 branch (`main`), 0 tags.

### Service: Local Git Object Engine (`git log` & `git cat-file`)
* **Commands Executed**:
  1. `git log --all --reverse --topo-order --format="%H\t%P\t%aI\t%cI\t%s"` (Output: `evidence/phase1/kuber/all-commits.tsv`, SHA-256: `fefd7790b83e60333246ebbb569f52f36f98108cbb947a1ecce3c41ef585b4fc`)
  2. `git diff-tree --root --no-commit-id --raw --no-abbrev -r -M -z <oid>` across all 419 commits.
  3. Extraction of 254 unique original-content text blobs into `evidence/phase1/kuber/objects/`.
* **Execution Timestamp**: `2026-09-25T01:46:05Z` to `01:46:44Z`
* **Run Record**: `evidence/computation-logs/PASS4-PHASE1-KUBER-COLLECTED.run.json` (Exit code: `0`)
* **Items Shortlisted for Detailed Review**:
  1. `UPDATES.md` (commit `0e90b56a`, Aug 11): Adjudication layer, finite vs full-space boundary.
  2. `FINDINGS.md` (commit `e5ea3e87`, July 24): Tiered ledger of results.
  3. `CONTINUATION.md` (commit `50557c08`, Aug 11): Analytical Schur continuation theorem.
  4. `COLLISION.md` (commit `0d18760c`, Aug 11): Prior art collision audit.
  5. `experiments/weil_positivity/EPSILON-N.md` (commit `35b28a8a`, Aug 11): CCM hypothesis verification on finite sections.
  6. `experiments/weil_positivity/SHARP-FLOOR.md` (commit `27861654`, Aug 11): Uncertified pilot $\sigma$-LP crossing.
  7. `formal/RiemannFormal/*.lean` (commits `401e98e1` to `5415f4a4`, Aug 11): Lean 4 proofs of Lemma 1, $\sigma$-LP assembly, conditional $T_1$, and `weil_positivity_of_RH`.
* **Disposition**: `PARTIAL OVERLAP / DIFFERENT REGIME & SCOPE`.
  - Finite-dimensional positive definiteness verified in Arb on explicit subspaces.
  - Infinite-dimensional full-space theorems left uncertified.
  - Distinct mathematical mechanism (Fourier-sine series vs. Legendre harmonic coercivity).
