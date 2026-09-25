# Source provenance and frozen target

## Audited target

- Repository: `https://github.com/PerceivingAI/riemann-conjecture`.
- Frozen commit: `51feb3d176e4a53773c22dc157567cc0486f4c71`.
- Frozen tree: `8a1dd144a90a4121601ea839d048860bd724b413`.
- Checkout: `source/riemann-conjecture/`, read-only.

Phase 0 captured the source commit, tree, refs, Git status, and a raw-byte inventory before historical restoration. The initial Git status is clean. Existing ignored build outputs and caches are present; clean Git status does not imply their absence. They are included in the byte inventory and must not be removed or modified.

[Source baseline](evidence/phase0/SOURCE_BEFORE.json) contains all 3,948 file/directory entries captured, including 3,444 files. Each file's `sha256` hashes exact raw bytes; directory entries record existence, and symlink entries record the target. The comparison does not claim to preserve access timestamps. Source identity checks use Git with optional index locks disabled. No source build, test, theorem replay, or dependency installation is needed for Phase 0.

## Candidate locations and historical leads

[CANDIDATE_MAP.json](evidence/phase0/CANDIDATE_MAP.json) records pinned source locations, exact inventory proposition digests, original reference labels, and resolved historical commit IDs for all 66 candidates. A resolved Git object proves identity, not that it contains the first complete proof or was public at that time.

The prior provenance table and its creation-time assertions remain preserved in [Pass 3 SOURCE.md](archive/baselines/pass-3/SOURCE.md). They are leads for later chronology, not newly verified event evidence. Phase 0 does not assert the source repository's creation time or earliest public push.

Source excerpt digests use UTF-8 text formed by joining the selected decoded lines with LF and no added final newline. They detect changes in the inspected excerpt; raw file identities are independently retained in the source baseline.

## Execution boundary

Do not edit source code, findings, derivations, certificates, retained calculations, documentation, or Git history. Do not place outputs or caches there. Later execution must redirect all writes into audit-owned paths or use a documented hash-verified execution copy. Any source defect is an audit finding with commit, path, line/section, candidate ID, and evidence.

The validator compares the current checkout's files/directories, raw hashes, refs, commit, tree, and Git status with the captured baseline. This is a local preservation check, not proof of historical public availability. [TIMELINE_RULES.md](TIMELINE_RULES.md) governs that separate question.
