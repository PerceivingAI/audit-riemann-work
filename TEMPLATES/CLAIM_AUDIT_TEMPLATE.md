# Claim Audit: [CLAIM_ID] - [Short Title]

## 1. Claim Specification

* **Claim ID**: `[e.g., CLM-MATH-001]`
* **Category**: `[Mathematical | Methodology | Verification | Priority]`
* **Candidate Statement**:
  > *[Verbatim or formalized proposition as stated in the candidate record]*
* **Source Anchor Commits**:
  * First Introduction: `[Commit SHA / Date]`
  * Complete Implementation: `[Commit SHA / Date]`
  * Audited Snapshot: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Audited Files**: `[List paths within source/riemann-conjecture/]`

---

## 2. Mathematical Normalization

* **Target Notation**: `[Define conventions used in source repo]`
* **Standard Literature Notation**: `[Map to standardized literature variables]`
* **Equivalence Mapping**:
  * Variable / Operator 1: $X \iff Y$
  * Domain / Interval: $I_1 \iff I_2$
  * Normalization Constant: $C_1 \iff C_2$

---

## 3. Literature & Prior Art Search Summary

* **Search Records Referenced**:
  * `evidence/search-records/[SEARCH-LOG-ID].md`
* **Primary Literature Analyzed**:
  * `[LIT-ID]` - *Title*, Authors (Year) - [DOI/arXiv]
* **Key Findings from Literature**:
  * *[Summary of closest existing theorems, bounds, or methods]*

---

## 4. Comparative Analysis

### A. Result Analysis (Theorem / Bound / Constant)
* *[Comparison of quantitative bounds, generality, domain of validity]*

### B. Methodological Analysis (Proof Technique / Synthesis)
* *[Comparison of proof mechanisms: coercivity, spectral tools, Schur complements, etc.]*

### C. Ingredients vs. Synthesis Separation
* *Standard Ingredients Used*: `[e.g., Legendre polynomials, Gershgorin circles]`
* *Synthesis Novelty*: `[Assessment of the novel combination/application]`

---

## 5. Timeline & Priority Analysis (If Applicable)

| Anchor Event | Entity | Timestamp (UTC) | Reference / Hash |
| :--- | :--- | :--- | :--- |
| Project Public Push ($T_{\text{public\_push}}$) | `riemann-conjecture` | `YYYY-MM-DD` | Commit `[SHA]` |
| External Disclosure ($T_{\text{ext\_post}}$) | External Author | `YYYY-MM-DD` | `[arXiv:xxxx.xxxxx]` |

* **Chronological Precedence Assessment**: `[Earlier / Concurrent / Later / Not Applicable]`

---

## 6. Audit Verdict & Justification

* **Final Verdict**: `[PRIOR ART FOUND | INDEPENDENT REDISCOVERY | POSSIBLY NOVEL — NO PRIOR ART FOUND | NOVELTY SUPPORTED | PRIORITY PLAUSIBLE | PRIORITY SUPPORTED | INCONCLUSIVE | CLAIM REQUIRES NARROWER WORDING]`
* **Detailed Rationale**:
  * *[Definitive, evidence-grounded justification]*
* **Scope & Nuance Limitations**:
  * *[Any boundary conditions, restricted parameters, or caveats]*
