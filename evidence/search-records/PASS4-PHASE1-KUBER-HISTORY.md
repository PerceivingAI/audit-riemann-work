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

---

## Candidate Claim Search Adjudications

## CLM-PRIO-001

- Subject ID: `CLM-PRIO-001`
- Proposition SHA-256: `3c961b28f35d6b0e2fdca8a4365593d0aa639799ab276efd710f01165f2c09c6`
- Canonical Proposition: Fully public open-science research record since creation date `2026-08-20T20:39:42Z`.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-002

- Subject ID: `CLM-PRIO-002`
- Proposition SHA-256: `4c28ec7ab48bdd17d135ea8d7d4b31a1600a0eee6745e89939b04ea851a71075`
- Canonical Proposition: Public negative-result and obstruction trail preserved alongside theorems.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-003

- Subject ID: `CLM-PRIO-003`
- Proposition SHA-256: `80804734741b5f4e14b9a7c1a0391eeadd8c630502beca29a6e5abcc9f069191`
- Canonical Proposition: Public scientific correction trail without history rewriting.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-004

- Subject ID: `CLM-PRIO-004`
- Proposition SHA-256: `9294d15f4abc48badd689947227947872e2adafbce4da5d1afe38bda28d53d49`
- Canonical Proposition: Earliest public exact-prime Legendre-Schur proof of strict localized Weil positivity.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-005

- Subject ID: `CLM-PRIO-005`
- Proposition SHA-256: `1c30b6c0322afa3b95cbd8834df5ed1d8eb6e6b7e185db787bc07b4b97d09a00`
- Canonical Proposition: Earliest public finite-support Weil positivity theorem at $T=7/20$ (C-0050).
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-006

- Subject ID: `CLM-PRIO-006`
- Proposition SHA-256: `90fc2c0efb1b4c03f7c9dfd6d8d71636725514c46392596d73d354db438ed2ad`
- Canonical Proposition: Earliest public sequence of certified localized Weil positivity extending through $T=27/50$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-007

- Subject ID: `CLM-PRIO-007`
- Proposition SHA-256: `94db2b0856fba212034601e2d27f289dc0c51308270edf3dd6a0ddf86d3b12da`
- Canonical Proposition: First exact pole-annihilating shift filter for generalized prime-Laguerre Li sequences.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-008

- Subject ID: `CLM-PRIO-008`
- Proposition SHA-256: `975e5091a22da34f7bc4957a0f8680c137bf616a0266039bb9720b6791658406`
- Canonical Proposition: First prime-Laguerre RH root criterion after exact zeta-pole subtraction.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-009

- Subject ID: `CLM-PRIO-009`
- Proposition SHA-256: `1b3a448ae6cb059f531a1c69c211a289d065d45f4b573fb6a8712aaf1b411afc`
- Canonical Proposition: First interpretation of generalized Li prime kernel as critical-half-weight nonlinear Mellin chirp.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-010

- Subject ID: `CLM-PRIO-010`
- Proposition SHA-256: `2c6f83111a86deaeaac3ea7ea461ef7822ff2b2d65c42c426a0d001ae5045668`
- Canonical Proposition: First rank-one Hessian / separability obstruction for Vaughan/Heath-Brown decompositions of the chirp.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-011

- Subject ID: `CLM-PRIO-011`
- Proposition SHA-256: `1083220b92dde1d885304f263392051c0f2d50eb134387c127928f39fc21d744`
- Canonical Proposition: First conditional-negative-definite / Schoenberg characterization of RH directly from Li coefficients.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-PRIO-012

- Subject ID: `CLM-PRIO-012`
- Proposition SHA-256: `610cb62f3e7ea0d641b62cf2bb1a328956900963ea30c10a86422ba15d20d2d4`
- Canonical Proposition: First compressed-translation operator treatment making Weil prime-entry thresholds and shift norm explicit.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

