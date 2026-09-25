# Pass 4 Phase 1 Interim Report: Comparator Histories & Primary Source Reconstruction

> **Report Governance & Audit Metadata**  
> * **Audit Phase**: Pass 4 Phase 1 (Comparator Histories & Primary Sources)  
> * **Document Type**: Interim Milestone Audit Report  
> * **Date Compiled**: `2026-09-25`  
> * **Phase 1 Technical Exit Gate**: **`PASS`**  
> * **Audited Closed-State Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Execution Plan**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Phase 1; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md)

---

## 1. Executive Summary & Phase 1 Objectives

Pass 4 Phase 1 has completed an independent, primary-source and commit-level investigation of the two main contemporary comparators to `riemann-conjecture`:
1. **Kuber Mehta (`https://github.com/Kuberwastaken/riemann`)**: Full commit-by-commit reconstruction across all 419 reachable Git commits and 211 scoped commits touching tracked documentation, logs, experiments, and formal modules.
2. **Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`)**: Primary-source analysis of official arXiv records, version metadata (v1 vs. v2), the actual mathematical paper, and inspection of e-print source packages.
3. **Foundational Prior-Art Collision Leads**: Independent inspection of primary works cited in comparator collision analyses (Yoshida 1992, Bombieri 2000, Connes–Consani 2020/2021, Connes–Consani–Moscovici 2025, Suzuki 2026, Groskin 2026).

---

## 2. Key Investigation Findings

### 2.1 Kuber Mehta Git History Reconstruction
* **Dossier**: [`evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md`](../../evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md)
* **Evidence Manifest**: [`evidence/phase1/kuber/MANIFEST.json`](../../evidence/phase1/kuber/MANIFEST.json) (254 original-content text blobs retained with SHA-256 digests).
* **Findings**:
  1. *Subspace Boundary*: Kuber Mehta’s verified positivity curve ($W \ge 0.0726$ at $L=0.45$, $W \ge 0.0148$ at $L=0.50$, $W \ge 0.0013$ at $L=0.545$, $W \ge 7.6\times 10^{-5}$ at $L=0.60$, $W \ge 2.06\times 10^{-5}$ at $L=0.62$) applies strictly to **explicit finite-dimensional test function families** (14D and 22D subspaces).
  2. *Full-Space Non-Claim*: In `UPDATES.md` (commit `0e90b56a`, Aug 11) and `FINDINGS.md` (commit `e5ea3e87`, July 24), Kuber explicitly clarifies that turning these numerical results into full-space $L^2([-T, T])$ theorems requires certifying high-frequency spectral caps, which remained uncertified.
  3. *Uncertified Pilot Calculations*: On August 11, Kuber produced pilot $\sigma$-LP calculations crossing zero at $L=0.40$ (+0.0046, commit `27861654`) and $L=0.42$ (+0.0320, commit `9ab31fe3`). These were explicitly documented as uncertified preliminary experiments (`SHARP-FLOOR.md`).
  4. *Distinct Mechanism*: Kuber’s framework relies on Fourier-sine series and Dirichlet band-mass bounds (Lemma H in `T1-GRADED.md`), not on Legendre polynomials or Tuck's harmonic number identity ($J(P_n) = H_n \|P_n\|_2^2$).
  5. *Distinct Software/Formalization*: Kuber uses Python + Arb (`flint.arb`) interval ball arithmetic and formalizes the criterion bridge in Lean 4 (`RiemannFormal`), which is distinct from `riemann-conjecture`'s standalone zero-floating-point Rust verifier (`rh_cert`) and arithmetic verifier soundness lemmas (`Cert/*.lean`).

### 2.2 Marcus Chuk / Xuefeng Zhu Primary Source Audit
* **Dossier**: [`evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md`](../../evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md)
* **Evidence Manifest**: [`evidence/phase1/chuk/MANIFEST.json`](../../evidence/phase1/chuk/MANIFEST.json)
* **Findings**:
  1. *Author & Version History*:
     - **v1** (submitted `2026-08-25T17:07:51Z`, 9-page announcement): Author listed as Marcus Chuk.
     - **v2** (submitted `2026-09-02T17:32:21Z`, 34 pages): Author listed as Xuefeng Zhu (Dalian University of Technology), noting *"author name and affiliation updated"*.
  2. *Theorem Statement*: Unconditional certified full-space positivity on $L=0.8$ (autocorrelation support $[-1.6, 1.6]$):
     $$Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2 > 0 \qquad \forall f \in L^2[-0.8, 0.8]$$
  3. *Mathematical Subsumption of $T \in [0.40, 0.54]$*: Because $[-0.54, 0.54] \subset [-0.8, 0.8]$, any test function supported in $[-0.54, 0.54]$ is in the support domain of Chuk/Zhu's theorem. Pinned continuation records $T \in [0.40, 0.54]$ (`CLM-MATH-002..008`) registered between August 26 and September 24 are mathematically subsumed by Chuk/Zhu's earlier public theorem (`RESULT SUBSUMED BY PRIOR ART`).
  4. *Distinct Proof Strategy*: Chuk/Zhu uses a one-stroke pointwise symbol envelope on $[0, T^\sharp]$ ($T^\sharp=200$) with Legendre Galerkin matrix at $N=200$ and Python `mpmath` interval Cholesky factorization. `riemann-conjecture` uses an exact-prime operator decomposition + Tuck Legendre harmonic coercivity + 3-factor Schur complement. These represent two fundamentally distinct mathematical proof architectures.
  5. *Supplementary Availability*: The official arXiv source package (`arxiv-2608.24827v2-source.tar.gz`, SHA-256 `1afc4e867bc6...`) contains only TeX and figure files; the referenced independent script `verify_certificate.py` is not packaged in the arXiv tar and no external repository is linked.

---

## 3. Claim-by-Claim Adjudication Impact

| Candidate ID | Audited Proposition | Comparator Finding | Phase 1 Evidence Classification |
| :--- | :--- | :--- | :--- |
| `CLM-MATH-001` | Strict localized Weil positivity at $(T, N) = (0.35, 32)$ | Commit `6dd1d8f` (Aug 21) pre-dates Chuk (Aug 25); exceeds Yoshida prime-free bound ($0.35 > 0.34657$). | `POSSIBLY NOVEL` (Result) / `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-MATH-002..008` | Strict localized Weil positivity at $T \in [0.40, 0.54]$ | Commits post-date Chuk (Aug 25); support domain $[-0.54, 0.54] \subset [-0.8, 0.8]$ subsumed. | `RESULT SUBSUMED BY PRIOR ART` (Result) / `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-METH-001` | Exact-prime finite-support Weil decomposition | Physical-space compressed translation geometry is distinct from Kuber/Suzuki. | `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-METH-002` | Legendre harmonic coercivity $J(P_n) = H_n \|P_n\|_2^2$ | Tuck (1964) eigenvalue identity; high-mode Weil coercivity application is novel. | `KNOWN INGREDIENT / NOVEL APPL.` (Method) |
| `CLM-METH-003` | High-mode complement bound $\mu_N > 0$ | Not present in Kuber, Chuk, or prior literature. | `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-METH-004` | Component tail-Gram Schur criterion | 3-factor discrete matrix inequality is unique to `riemann-conjecture`. | `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-OPER-001` | Thresholded compressed translations | Physical-space thresholding $T > \frac{1}{2}\log m$ and compressed shift analysis. | `KNOWN INGREDIENT / NOVEL APPL.` (Method) |
| `CLM-OPER-002` | Shift norm $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$ | Chebyshev path graph spectrum applied to compressed shifts. | `KNOWN INGREDIENT / NOVEL APPL.` (Method) |
| `CLM-LAGU-001` | Euler-product prime-Laguerre expansion | Explicit in Lagarias (2007, Ann. Inst. Fourier). | `PRIOR ART FOUND` (Result & Method) |
| `CLM-VERF-001..007` | Standalone zero-float Rust verifier & Lean proof chain | Standalone exact rational verifier and interval/LDL/Gershgorin formal soundness lemmas are distinct from Kuber/Chuk. | `NOVEL VERIFICATION ARCHITECTURE` (Software) |

---

## 4. Deliverables Produced in Phase 1

1. [`evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md`](../../evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md): Full commit-by-commit chronological matrix and normalization analysis.
2. [`evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md`](../../evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md): Primary source analysis of `arXiv:2608.24827` (v1 and v2).
3. [`evidence/literature/PASS_4_PRIOR_ART.md`](../../evidence/literature/PASS_4_PRIOR_ART.md): Master prior-art synthesis across 10 primary comparator works.
4. [`evidence/search-records/PASS4-PHASE1-CHUK-SOURCES.md`](../../evidence/search-records/PASS4-PHASE1-CHUK-SOURCES.md): Per-database search log for official arXiv records.
5. [`evidence/search-records/PASS4-PHASE1-KUBER-HISTORY.md`](../../evidence/search-records/PASS4-PHASE1-KUBER-HISTORY.md): Search and query log for Kuber GitHub API and Git object history.
6. [`evidence/phase1/kuber/MANIFEST.json`](../../evidence/phase1/kuber/MANIFEST.json): Cryptographic manifest of 254 original-content comparator text blobs.
7. [`evidence/phase1/chuk/MANIFEST.json`](../../evidence/phase1/chuk/MANIFEST.json): Cryptographic manifest of primary paper records.
8. [`scripts/pass4_kuber.py`](../../scripts/pass4_kuber.py) and [`scripts/pass4_chuk.py`](../../scripts/pass4_chuk.py): Fully reproducible collection scripts.
9. [`evidence/computation-logs/PASS4-PHASE1-PUBLICATION.run.json`](../../evidence/computation-logs/PASS4-PHASE1-PUBLICATION.run.json): Closed Phase 1 publication validation record (exit code 0).
10. [`evidence/computation-logs/PASS4-PHASE1-FINAL-HASH-CHECK.json`](../../evidence/computation-logs/PASS4-PHASE1-FINAL-HASH-CHECK.json): Independent recomputation verifying 26 raw and normalized stream hashes across all 13 Phase 0 and Phase 1 runs.
11. Updated [`EVIDENCE_COVERAGE.md`](../../EVIDENCE_COVERAGE.md) and [`evidence/phase0/CANDIDATE_MAP.json`](../../evidence/phase0/CANDIDATE_MAP.json) reflecting Phase 1 comparator evidence.

---

## 5. Phase 1 Technical Exit Gate

| Phase 1 Exit Criterion | Evaluation / Evidence | Status |
| :--- | :--- | :--- |
| **Comparator History** | Every comparator conclusion references exact commit SHAs, author timestamps, and file paths. | **`PASS`** |
| **Primary Source Verification** | Official arXiv version records (v1 vs v2), author changes, and theorem locators verified from primary text. | **`PASS`** |
| **Normalization** | Test function spaces, support widths, operators, and tail bounds normalized before comparing. | **`PASS`** |
| **Reproducibility** | Per-database query logs, exit-code 0 execution records, and SHA-256 manifests preserved. | **`PASS`** |
| **Integrity & Immutability** | `scripts/pass4_validate.py` passes 0 errors; source snapshot `51feb3d` remains untouched. | **`PASS`** |

**Phase 1 is complete. Phase 2 (Claim-Specific Search Re-Execution) is ready to begin.**
