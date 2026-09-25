# Mathematical Validity Dossier: Certified Localized Weil Positivity Theorems (`CLM-MATH-001..008`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-MATH-001-008-THEOREMS`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group A — Certified Theorem Candidates (`CLM-MATH-001` through `CLM-MATH-008`)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 7 (Group A) & 20; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Mathematical Statement & Reduction Framework

The audited project establishes localized strict Weil positivity theorems for Suzuki's scaled finite-support quadratic form $Q_T(w)$ on compact support intervals $[-T, T]$ ($T \in [0.35, 0.54]$) on the admissible subspace of $L^2[-T, T]$ (under standard pole orthogonality conditions).

### 1.1 Analytical Reduction Architecture
The theorem reduction proceeds in four exact steps:
1. **Exact-Prime Operator Decomposition**:
   $$Q_T(w) = J(w) + V(w) + P_2(w) + R_T(w) - c_T \|w\|_2^2$$
   where $J(w) = \frac{1}{4}\iint \frac{|w(x)-w(y)|^2}{|x-y|} dx dy$, $V(x) = -\frac{1}{2}\log(1-x^2)$, $P_2$ is the $p=2$ compressed translation operator, and $R_T$ is Suzuki's finite-support residual kernel.
2. **Legendre Harmonic Complement Coercivity**:
   On the orthogonal complement subspace $\mathcal{Q}_N = \operatorname{span}\{P_0, \dots, P_{N-1}\}^\perp$, Tuck's identity yields:
   $$J(q) \ge H_N \|q\|_2^2 \implies Q_T(q) \ge \mu_N \|q\|_2^2, \qquad \mu_N = H_N - c_T - c_2 - \rho_R > 0$$
3. **Component Tail-Gram Schur Reduction**:
   Decomposing the low-to-tail coupling block as $B_N = B_V + B_2 + B_R$, Cauchy-Schwarz yields full-space positivity if the finite $N \times N$ matrix satisfies:
   $$A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) \succ 0$$
4. **Exact Rational Witness Verification**:
   The finite matrix inequality is verified in exact rational arithmetic via certified LDL decomposition and Gershgorin disc isolation in `rh_cert`.

---

## 2. Claim-by-Claim Validity Review

### CLM-MATH-001
* **Proposition**: Strict localized Weil positivity at $(T, N) = (7/20, 32) = (0.35, 32)$ (Source: `C-0050`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L558-L563`
* **Independent Verification**:
  - Replayed certificate `computations/2026-08-21T135237Z-exact-prime-schur-certificate/data/t035-n32-certificate.json` through `rh_cert` (exit 0).
  - Verified complement bound $\mu_{32} = H_{32} - c_{0.35} - c_2 - \rho_R > 0.65 > 0$.
  - Exact rational witness confirms $\lambda_{\min} > 0$ with positive Gershgorin margins.
* **Hypotheses & Limitations**: Applies strictly to compact support $T = 0.35$; does not prove arbitrary-support positivity or RH.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW, CODE_INSPECTION]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-002
* **Proposition**: Strict localized Weil positivity at $(T, N) = (2/5, 40) = (0.40, 40)$ (Source: `C-0051`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L570-L574`
* **Independent Verification**: Replayed retained certificate `C-0051` via `rh_cert`; verified $\mu_{40} > 0.73 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-003
* **Proposition**: Strict localized Weil positivity at $(T, N) = (17/40, 48) = (0.425, 48)$ (Source: `C-0052`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L581-L585`
* **Independent Verification**: Replayed retained certificate `C-0052` via `rh_cert`; verified $\mu_{48} > 0.81 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-004
* **Proposition**: Strict localized Weil positivity at $(T, N) = (9/20, 56) = (0.45, 56)$ (Source: `C-0053`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L592-L596`
* **Independent Verification**: Replayed retained certificate `C-0053` via `rh_cert`; verified $\mu_{56} > 0.88 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-005
* **Proposition**: Strict localized Weil positivity at $(T, N) = (19/40, 68) = (0.475, 68)$ (Source: `C-0054`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L603-L607`
* **Independent Verification**: Replayed retained certificate `C-0054` via `rh_cert`; verified $\mu_{68} > 0.96 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-006
* **Proposition**: Strict localized Weil positivity at $(T, N) = (1/2, 80) = (0.50, 80)$ (Source: `C-0055`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L614-L618`
* **Independent Verification**: Replayed retained certificate `C-0055` via `rh_cert`; verified $\mu_{80} > 1.02 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-007
* **Proposition**: Strict localized Weil positivity at $(T, N) = (21/40, 96) = (0.525, 96)$ (Source: `C-0056`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L625-L629`
* **Independent Verification**: Replayed retained certificate `C-0056` via `rh_cert`; verified $\mu_{96} > 1.09 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

### CLM-MATH-008
* **Proposition**: Strict localized Weil positivity at frontier $(T, N) = (27/50, 104) = (0.54, 104)$ (Source: `C-0057`).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L636-L640`
* **Independent Verification**: Replayed retained certificate `C-0057` via `rh_cert`; verified $\mu_{104} > 1.12 > 0$; exact rational LDL witness positive. Subsumed by Chuk/Zhu $L=0.8$.
* **Verification Basis**: `[MACHINE_REPLAY, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`
