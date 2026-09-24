# Source Provenance & Target Definition

This document establishes the exact identity, commit pins, provenance records, and historical anchors for the target repository under audit.

---

## 1. Audited Target Repository

* **Repository URL**: `https://github.com/PerceivingAI/riemann-conjecture`
* **Repository Visibility**: `PUBLIC`
* **Public Creation Timestamp**: `2026-08-20T20:39:42Z`
* **Audit Boundary**: Strictly Read-Only snapshot

---

## 2. Frozen Snapshot Anchor

The closed-state commit representing the primary target of this audit is:

```text
Commit Hash: 51feb3d176e4a53773c22dc157567cc0486f4c71
Timestamp  : 2026-09-24
Tree Location: source/riemann-conjecture (Git submodule / pinned checkout)
```

---

## 3. Historical Commit Anchors & Provenance Map

Priority and provenance audits must evaluate the exact point of origin for each specific result within the Git history, rather than evaluating solely the terminal commit `51feb3d`.

| Anchor Commit SHA | Commit Timestamp (UTC) | Milestone / Proposition Introduced | Associated Claims |
| :--- | :--- | :--- | :--- |
| `[Repo Creation]` | `2026-08-20T20:39:42Z` | Initial public repository creation on GitHub | `CLM-PRIO-001` |
| `cc57e7037a40...` | `2026-08-20` | Pole-subtracted Li/Laguerre criterion, Euler product decomposition, shift-filter work | `CLM-LAGU-001` to `005`, `CLM-OBST-004`, `CLM-PRIO-007`, `008` |
| `64e884b89c11...` | `2026-08-20` | Stationary-map, single-zero matching, nonlinear chirp, block-$L^2$ formulation | `CLM-AIRY-001` to `007`, `CLM-OBST-006` to `010`, `CLM-PRIO-009` |
| `1752f19dec98...` | `2026-08-20/21` | Bilinear / Vaughan / Heath-Brown rank-one Hessian and phase obstructions | `CLM-OBST-011` to `015`, `CLM-PRIO-010` |
| `fab5933fdcbd...` | `2026-08-21` | Li Gram kernel hierarchy, Schoenberg CND formulation, compressed-translation operator | `CLM-OPER-001`, `002`, `CLM-GRAM-001` to `003`, `CLM-PRIO-011`, `012` |
| `3111accb59df...` | `2026-08-21` | Legendre coercivity, exact-prime decomposition, high-mode complement bound, tail-Gram Schur | `CLM-METH-001` to `004`, `CLM-OBST-001` to `003`, `CLM-PRIO-004` |
| `6dd1d8f07e23...` | `2026-08-21T14:05:13Z` | First completed exact-prime theorem C-0050 ($T=0.35, N=32$), exact rational certificate & verifier | `CLM-MATH-001`, `CLM-METH-005`, `CLM-VERF-001`, `002`, `CLM-PRIO-005` |
| `b5405a9347a8...` | `2026-08-26` | Moving-dimension continuation sequence start (C-0051 through C-0056) | `CLM-MATH-002` to `007`, `CLM-CONT-001`, `CLM-VERF-004` |
| `51feb3d176e4...` | `2026-09-24` | Final closed state: C-0057 ($T=0.54, N=104$), 8/8 retained proof chain replay, Lean soundness | `CLM-MATH-008`, `CLM-CONT-002`, `CLM-VERF-003`, `005` to `007`, `CLM-PRIO-006` |

---

## 4. Source Inspection Rules

1. **Local Access**: Files from the source repository must be accessed strictly via `source/riemann-conjecture/`.
2. **Provenance Verification**: For every audited claim, the auditor must cross-check:
   * The earliest commit where the mathematical statement appears.
   * The earliest commit where the complete proof / code artifact was committed.
   * Author and committer timestamps for those commits.
3. **No Direct Mutation**: The `source/riemann-conjecture/` directory must remain untouched by any audit tooling or edits.
