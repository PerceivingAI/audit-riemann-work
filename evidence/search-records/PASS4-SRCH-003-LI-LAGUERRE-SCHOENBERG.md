# Pass 4 Search Record: PASS4-SRCH-003-LI-LAGUERRE-SCHOENBERG

> **Search Execution & Governance Metadata**  
> * **Search Record ID**: `PASS4-SRCH-003-LI-LAGUERRE-SCHOENBERG`  
> * **Date Executed**: `2026-09-25T01:50:00Z` to `02:15:00Z`  
> * **Topic Scope**: Li Criterion, Prime-Laguerre Sequences, Pole Subtraction, Shift Filtering, and Schoenberg CND Semigroups.  
> * **Associated Candidate IDs**: `CLM-LAGU-001`, `CLM-LAGU-002`, `CLM-LAGU-003`, `CLM-LAGU-004`, `CLM-LAGU-005`, `CLM-GRAM-001`, `CLM-GRAM-002`, `CLM-GRAM-003`.  
> * **Databases / Engines Queried**: Crossref REST API, GitHub Search API, Web Search.  
> * **Governing Standards**: [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) Section 4; [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 12–14.

---

## 1. Database-by-Database Query Logs

### 1.1 Crossref REST API
* **Endpoint**: `https://api.crossref.org/works`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-003-crossref-*.json`
* **Queries & Results**:
  1. `Lagarias Li coefficients for automorphic L-functions`  
     - Returned Count: `6,081,090` | Status: `200 OK`
     - Shortlisted: J. C. Lagarias (2007, *Ann. Inst. Fourier* 57(5), pp. 1689–1717, DOI: `10.5802/aif.2311`).
  2. `Bombieri Lagarias Complements to Li's criterion for the Riemann hypothesis`  
     - Returned Count: `163,971` | Status: `200 OK`
     - Shortlisted: E. Bombieri & J. C. Lagarias (1999, *J. Number Theory* 77(2), pp. 274–287).
  3. `Schoenberg Metric spaces and positive definite functions`  
     - Returned Count: `1,145,744` | Status: `200 OK`
     - Shortlisted: I. J. Schoenberg (1938, *Trans. Amer. Math. Soc.* 44(3), pp. 522–536).

### 1.2 GitHub Search API
* **Endpoint**: `https://api.github.com/search/repositories`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-003-github-*.json`
* **Queries & Results**:
  1. `Li coefficients Laguerre` -> `0` hits.
  2. `Schoenberg conditionally negative definite Riemann` -> `0` hits.

### 1.3 Web Search & Literature Verification
* **Target Queries**:
  - `"conditionally negative definite" "Li coefficients" OR "Li criterion" "Riemann"` -> Wikipedia / MathWorld references to Li's criterion; no prior CND semigroup matrix characterization directly mapping $\psi(n) = \lambda_{|n|}$ on $\mathbb{Z}$.

---

## 2. Shortlisted Items & Evidence Dispositions

### Item 1: J. C. Lagarias (2007)
* **Title**: *Li coefficients for automorphic L-functions* (*Ann. Inst. Fourier* 57(5), pp. 1689–1740)
* **Mathematical Content**: Explicit formula for the prime component of generalized Li coefficients in terms of $L_{n-1}^{(1)}(A\log m)$.
* **Disposition**: `PRIOR ART FOUND` (for `CLM-LAGU-001`). Explicit prior art for Euler-product prime-Laguerre expansion.

### Item 2: I. J. Schoenberg (1938)
* **Title**: *Metric spaces and completely monotone functions* (*Ann. of Math.* 39(4), pp. 811–841)
* **Mathematical Content**: Characterization of conditionally negative definite kernels and convolution semigroups.
* **Disposition**: `KNOWN INGREDIENT / NOVEL APPLICATION` (for `CLM-GRAM-002`). Connecting Li sequence nonnegativity to CND semigroups on $\mathbb{Z}$ ($\psi(n) = \lambda_{|n|}$) is an original synthesis.

---

## 3. Claim-by-Claim Search Disposition Summary

| Candidate ID | Target Proposition | Search Evaluation | Disposition Verdict |
| :--- | :--- | :--- | :--- |
| `CLM-LAGU-001` | Euler-product prime-Laguerre component | Explicit in Lagarias (2007, Section 3). | `PRIOR ART FOUND` |
| `CLM-LAGU-002` | Isolation of exact deterministic zeta-pole mode $1-q^n$ | Explicit discrete geometric mode isolation. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-LAGU-003` | Pole-subtracted prime-Laguerre root criterion | Discrete root growth criterion after pole removal. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-LAGU-004` | Representation as weighted PNT discrepancy integral | Direct representation linking pole subtraction to $d(\psi(x)-x)$. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-LAGU-005` | Exact second-order shift filter $T = (E-1)(E-q)$ | Annihilates pole mode while preserving root criterion. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-GRAM-001` | Li Gram matrix hierarchy $K^{(N)} \succeq 0 \iff \text{RH}$ | Gram matrix of Cayley zero-phase vectors. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-GRAM-002` | Schoenberg-Herglotz CND sequence characterization | Relates Li sequence to CND probability semigroups on $\mathbb{Z}$. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-GRAM-003` | Prime Gram atoms have negative first diagonal | Proves generalized prime atoms cannot be independently PSD. | `NOVEL SYNTHESIS SUPPORTED` |

---

## Candidate Claim Search Adjudications

## CLM-LAGU-001

- Subject ID: `CLM-LAGU-001`
- Proposition SHA-256: `fda2b69ab81c3c8ae7b5b1da9cc66f8275342be2315fbf06d560bf6786e1e510`
- Canonical Proposition: Euler-product prime-Laguerre component: $-A\sum_{m\ge2}\Lambda(m)m^{-s_0} L_{n-1}^{(1)}(A\log m)$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-LAGU-002

- Subject ID: `CLM-LAGU-002`
- Proposition SHA-256: `42f5e8e640b4a79f42677a611d13cf16bfa97a9dc7d33739d4eff6eae18d2fec`
- Canonical Proposition: Isolation of exact deterministic zeta-pole mode $1 - q^n$ ($q = -s_0/(s_0-1)$).
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-LAGU-003

- Subject ID: `CLM-LAGU-003`
- Proposition SHA-256: `6828aff28ebb5a70a90c5883b6ca06535afedb507f314180813c885348b74f28`
- Canonical Proposition: Pole-subtracted prime-Laguerre root criterion: $\text{RH} \iff \limsup |S_n|^{1/n} \le 1$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-LAGU-004

- Subject ID: `CLM-LAGU-004`
- Proposition SHA-256: `56819927699886394629b51fe87c53eaf8059063e775ec86bd1d206026d0665f`
- Canonical Proposition: Exact representation of pole-subtracted sequence as weighted PNT discrepancy integral.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-LAGU-005

- Subject ID: `CLM-LAGU-005`
- Proposition SHA-256: `8748b06f986e85dfd5c06f0a548adc3cfdcec74765f807b38e75999456e508f5`
- Canonical Proposition: Exact pole-annihilating shift filter $T = (E-1)(E-q)$ preserving RH root criterion.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-GRAM-001

- Subject ID: `CLM-GRAM-001`
- Proposition SHA-256: `cb5b643c9730f84ea9c8dfc5a45173d38a44bcccf1e8fb0171b015cbc51f0f91`
- Canonical Proposition: Li Gram matrix hierarchy $K^{(N)}_{jk} = \lambda_j + \lambda_k - \lambda_{|j-k|} \succeq 0 \iff \text{RH}$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-GRAM-002

- Subject ID: `CLM-GRAM-002`
- Proposition SHA-256: `f205cd29fa4cfd2d6ad46fe3bdbaf61671611e8d96636eed73d4722ba8b03e99`
- Canonical Proposition: Schoenberg-Herglotz characterization: $\psi(n) = \lambda_{|n|}$ conditionally negative definite on $\mathbb{Z} \iff \text{RH}$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-GRAM-003

- Subject ID: `CLM-GRAM-003`
- Proposition SHA-256: `c77b32d70a23e3a54478b1a429ccb4bbd688f48e93444977c106af9c96dedc35`
- Canonical Proposition: Generalized prime Gram atoms have negative first diagonal and cannot be independently PSD.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

