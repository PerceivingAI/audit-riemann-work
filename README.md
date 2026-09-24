# Riemann Conjecture Research Audit

A public, independent, and evidentiary audit of the mathematical, methodological, and priority claims originating from [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

## 1. Objective & Scope

This repository provides an evidentiary record investigating the novelty, rigor, reproducibility, and priority of results produced by the `riemann-conjecture` project.

The audit evaluates candidate hypotheses against established mathematical literature, historical records, and contemporary preprints under an adversarial, skeptical standard.

### Core Audit Principles

1. **Strict Read-Only Stance**: The source repository `PerceivingAI/riemann-conjecture` is strictly read-only. No changes, pull requests, or issue updates are made upstream. All findings, logs, and artifacts reside entirely within this audit repository.
2. **Skeptical Default**: Claims are treated as unverified hypotheses until exhaustive literature searches and mathematical normalization demonstrate otherwise.
3. **Public Evidentiary Record**: Adverse findings, prior art discoveries, search logs, and inconclusive results are recorded with equal rigor to supported claims.
4. **Primary Source Verification**: Claims and counter-claims must be backed by primary mathematical literature, official timestamps, or reproducible code artifacts.
5. **Separation of Concerns**: Result novelty, method novelty, and foundational mathematical ingredients are assessed independently.

---

## 2. Directory Structure

```text
riemann-conjecture-audit/
├── README.md                  # Public overview, scope, and governance
├── AUDIT_PLAN.md              # Master phased execution strategy, tiering, and gates
├── AUDIT_PROTOCOL.md          # Methodological rules, taxonomy, and standards
├── SOURCE.md                  # Source repo provenance, commit pinning, commit map
├── CLAIMS_TO_AUDIT.md         # Queue of candidate hypotheses under audit
├── EVIDENCE_STANDARDS.md      # Citation rules, source hierarchy, copyright/PDF policy
├── TIMELINE_RULES.md          # Multi-anchor priority & timestamp evaluation framework
├── TEMPLATES/
│   ├── CLAIM_AUDIT_TEMPLATE.md    # Template for individual claim audits
│   └── SEARCH_RECORD_TEMPLATE.md  # Template for literature search logs
├── source/
│   └── riemann-conjecture/   # Pinned snapshot / submodule at commit 51feb3d
├── claims/
│   ├── mathematical/          # Analytical theorems, parameter bounds, lemmas
│   ├── methodology/           # Structural proofs, coercivity methods, Schur complements
│   ├── verification/          # Rigorous interval arithmetic, exact certificates
│   └── priority/              # Public disclosure chronology vs external preprints
├── evidence/
│   ├── literature/            # BibTeX, DOIs, formal excerpts, comparison notes
│   ├── public-timeline/       # Git commit proofs, archive timestamps, preprint logs
│   └── search-records/        # Raw query logs across databases and catalogs
└── reports/
    ├── interim/               # Periodic progress dossiers
    └── FINAL_AUDIT.md         # Comprehensive synthesized audit report
```

---

## 3. Workflow for Auditors

1. **Intake**: A proposition from `CLAIMS_TO_AUDIT.md` is selected.
2. **Normalization**: Standardize mathematical definitions and notation per `AUDIT_PROTOCOL.md`.
3. **Literature Search**: Execute queries across mathematical databases and record queries in `evidence/search-records/` per `EVIDENCE_STANDARDS.md`.
4. **Provenance & Chronology**: Trace earliest commit introduction in `source/riemann-conjecture` and compare with external timelines per `TIMELINE_RULES.md`.
5. **Verdict Assignment**: Issue a formal evaluation dossier in `claims/{category}/` adhering to `TEMPLATES/CLAIM_AUDIT_TEMPLATE.md` using the standard outcome taxonomy.

---

## 4. Audited Target Reference

* **Repository**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Closed State Target Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`
* **Provenance Details**: See [`SOURCE.md`](SOURCE.md) for detailed commit anchors.
