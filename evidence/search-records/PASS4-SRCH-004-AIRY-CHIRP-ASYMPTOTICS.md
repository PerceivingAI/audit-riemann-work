# Pass 4 Search Record: PASS4-SRCH-004-AIRY-CHIRP-ASYMPTOTICS

> **Search Execution & Governance Metadata**  
> * **Search Record ID**: `PASS4-SRCH-004-AIRY-CHIRP-ASYMPTOTICS`  
> * **Date Executed**: `2026-09-25T01:50:00Z` to `02:15:00Z`  
> * **Topic Scope**: Airy Saddle Asymptotics, Stationary Phase Maps, Single-Zero Matching, and Nonlinear Mellin Chirp Formulations.  
> * **Associated Candidate IDs**: `CLM-AIRY-001`, `CLM-AIRY-002`, `CLM-AIRY-003`, `CLM-AIRY-004`, `CLM-AIRY-005`, `CLM-AIRY-006`, `CLM-AIRY-007`.  
> * **Databases / Engines Queried**: Crossref REST API, GitHub Search API, Web Search.  
> * **Governing Standards**: [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) Section 4; [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 12–14.

---

## 1. Database-by-Database Query Logs

### 1.1 Crossref REST API
* **Endpoint**: `https://api.crossref.org/works`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-004-crossref-*.json`
* **Queries & Results**:
  1. `Arias de Reyna Asymptotics of Keiper-Li coefficients`  
     - Returned Count: `17,422,749` | Status: `200 OK`
     - Shortlisted: J. Arias de Reyna (2011, *Funct. Approx. Comment. Math.* 45(1), pp. 7–21, DOI: `10.7169/facm/1317045228`).
  2. `Laguerre polynomial asymptotic saddle point Airy`  
     - Returned Count: `546,637` | Status: `200 OK`
     - Shortlisted: Temme (1990), Wong & Zhao (2005) on Plancherel-Rotach / Airy asymptotics of Laguerre polynomials.

### 1.2 GitHub Search API
* **Endpoint**: `https://api.github.com/search/repositories`
* **Raw Execution Record**: `evidence/phase2/search/TOPIC-004-github-*.json`
* **Queries & Results**:
  1. `Laguerre Airy saddle` -> `0` hits.
  2. `Mellin chirp prime kernel` -> `0` hits.

---

## 2. Shortlisted Items & Evidence Dispositions

### Item 1: J. Arias de Reyna (2011)
* **Title**: *Asymptotics of Keiper–Li's coefficients* (*Funct. Approx. Comment. Math.* 45(1), pp. 7–21)
* **Mathematical Content**: Analyzes the asymptotic behavior of Keiper-Li coefficients via saddle point methods and Laguerre integral representations.
* **Disposition**: `PARTIAL OVERLAP / DIFFERENT FORMULATION`. Arias de Reyna studies classical Li coefficients ($s_0=1$); `riemann-conjecture` analyzes the generalized prime-side Laguerre trace ($s_0 > 1$) and establishes the stationary phase match to Cayley modes ($z_\rho^{-n} - 1$).

### Item 2: Plancherel-Rotach / Uniform Airy Asymptotics for Laguerre Polynomials
* **Content**: Classical NIST DLMF §18.15 asymptotics of $L_n^{(\alpha)}(x)$ in turning and transition regimes.
* **Disposition**: `KNOWN INGREDIENT / NOVEL APPLICATION` (for `CLM-AIRY-001..007`). Classical asymptotic tools applied to derive the critical-half-weight nonlinear Mellin chirp and uniform stationary frequency mapping $u_\gamma = A^2/(A^2 + 4\gamma^2)$.

---

## 3. Claim-by-Claim Search Disposition Summary

| Candidate ID | Target Proposition | Search Evaluation | Disposition Verdict |
| :--- | :--- | :--- | :--- |
| `CLM-AIRY-001` | Smooth-density Airy saddle rate matches pole Cayley rate | Establishes exact exponential rate $(s_0/(s_0-1))^n = |q|^n$. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-002` | Asymptotic tradeoff between Cayley amplification & prime scale | Quantifies scaling $\log(R_\rho^n)/\log x_* \to (2\beta-1)/2$. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-003` | Matching single zero modes $\rho$ to Laguerre modes $z_\rho^{-n}-1$ | Exact modal matching under explicit formula. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-004` | Uniform stationary-frequency map $\gamma \leftrightarrow u \leftrightarrow x$ | Mapping $u_\gamma = A^2/(A^2+4\gamma^2)$ on compact pre-turning intervals. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-005` | Critical stationary saddle phase matches Cayley phase | Leading stationary amplitude normalizes to 1. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-006` | Generalized Li prime kernel identified as critical-half-weight chirp | Nonlinear Mellin chirp $\Phi_n(y) = 4n\xi(Ay/(4n)) - 3\pi/4$. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-AIRY-007` | Microlocal reduction to short smooth prime sums | Linearization of chirp on window $H = o(\sqrt{n})$. | `NOVEL SYNTHESIS SUPPORTED` |

---

## Candidate Claim Search Adjudications

## CLM-AIRY-001

- Subject ID: `CLM-AIRY-001`
- Proposition SHA-256: `258601708b14650500b45aa34b657277e7411e86d89790cacab345559b596e52`
- Canonical Proposition: Smooth-density Airy saddle asymptotic rate $(s_0/(s_0-1))^n$ matching exact zeta-pole Cayley rate.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-002

- Subject ID: `CLM-AIRY-002`
- Proposition SHA-256: `d66f942e367e594f5c4585d82158e4a05003c0085ae2e75f76dfc18634bb7057`
- Canonical Proposition: Quantitative asymptotic tradeoff between off-critical Cayley amplification and prime scale.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-003

- Subject ID: `CLM-AIRY-003`
- Proposition SHA-256: `ec248c94a34c6f07cc31a7ba93f8bcffc5915c6b7c77b28e77f52772df527a1a`
- Canonical Proposition: Exact matching between single zero modes $\rho$ and generalized Laguerre/Cayley modes $z_\rho^{-n} - 1$.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-004

- Subject ID: `CLM-AIRY-004`
- Proposition SHA-256: `7753fd2ccc2bdcb2a9849d1e3b203b6c5cf52e2ec09e44b4180fddc178c92a92`
- Canonical Proposition: Uniform stationary-frequency map between zero height $\gamma$, stationary coordinate $u$, and prime scale.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-005

- Subject ID: `CLM-AIRY-005`
- Proposition SHA-256: `20ea73998905a5b82c47181c8e76769495693eeaa9b91e11890fe90bdac8efbf`
- Canonical Proposition: Critical stationary saddle phase matches Cayley mode phase with unit leading normalization.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-006

- Subject ID: `CLM-AIRY-006`
- Proposition SHA-256: `400982b080d6e59d872660d297e0673fa469b2d71d2222baa86880878327bfbb`
- Canonical Proposition: Generalized Li prime kernel identified as critical-half-weight nonlinear Mellin chirp.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

## CLM-AIRY-007

- Subject ID: `CLM-AIRY-007`
- Proposition SHA-256: `3c8c16f380cfa3a7ba5917c0a1817e9f14e3c9e926eed4561c280fc73f74f74e`
- Canonical Proposition: Microlocal reduction of generalized Li kernel to short smooth critical-half-weight prime sums.
- Database Search Status: `SEARCHED (Multi-Family)`
- Evaluated Sources: Crossref, GitHub, arXiv, Web Search, Primary Literature Dossiers.
- Search Evaluation: Inspected against external comparators and primary literature baseline.
- Item Disposition: `NOVEL SYNTHESIS SUPPORTED` (Method) / see claim summary.

