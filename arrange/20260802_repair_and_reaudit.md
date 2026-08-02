# 2026-08-02 Repair, Consolidation, and Full Re-Audit

## Commit scope

This audit covers the active proof package, the compiled manuscript, the exact
Strategy 4 supplement, and the new CI checks.

## Repairs that passed

1. **`4147` two-chart replacement.** The Vd1 replacement is constructed in a
   chart based at its distinguished vertex, and the adjacent supercritical
   replacement is constructed in a second chart based at the adjacent
   distinguished vertex. Both open origins, all three reach coordinates,
   boundary sums, and adjacent-arm exclusions are proved directly.
2. **Full skeleton preservation.** The replacement proof checks
   $e_{5,0},e_{0,1},e_{1,2},r_0,r_1$ separately; every other skeleton
   component is unchanged.
3. **`4013` skeleton strengthening.** Its theorem now assumes exactly the
   boundary and radial data used in its proof. The radial demands are derived
   from Vd0 locality and skeleton coverage before the gap-rank split.
4. **Rank-two interface.** `2110` is stated and proved at skeleton-data level.
5. **`414X` placement audit.** `414b` verifies the positive-support
   complement and all three relative-position cases.
6. **Notation.** Actual $N_+$ uses uppercase reaches. Local ray endpoints use
   Latin $u$; the signed CE2 far boundary endpoint uses Greek $\nu$.
7. **Terminology.** Singleton-inclusive branches say “nonempty gap.” Geometric
   objects are called V triangles or transfer slots, not rows.
8. **Strategy 4 source.** The duplicate mixed-overlap certificate was removed;
   `06a_strategy4_exact_certificate.tex` is the sole certificate source.
9. **Strategy 2 source.** The appendix sources were consolidated into
   `04_strategy2_verification.tex`; the late correction layer was removed.
10. **Automation.** CI checks active dependency statuses, notation,
    cross-references, exact certificate replay, LaTeX compilation, PDF
    rendering, and artifact upload.

## Mathematical conclusion

The chart defect and theorem-interface defect identified in the preceding
audit are repaired. The repaired `4147` hypotheses imply the strengthened
`4013` hypotheses exactly. The `414X` case split remains exhaustive, and no
terminal is invoked outside its proved domain. The main theorem status remains
**Proven**.

## Machine verification

- `python tools/proof_lint.py`: passed.
- `verify_mixed_overlap_core_derivation.py`: passed.
- `verify_global_core_positivity.py`: passed.
- `latexmk -xelatex -halt-on-error main.tex`: passed.
- PDF page count: 136.

## Independent post-commit source audit

A second read of the committed tree found and repaired three nonmathematical
defects: the remaining `\nu_{\rm adj}` transcription in the Markdown source,
two unexpanded TeX spacing placeholders, and stale duplicated architecture
documentation. The review also removed accidentally committed LaTeX
intermediates and strengthened the linter to reject recurrence. No new defect
was found in the two-chart reach calculation, skeleton preservation, the
strengthened `4013` rank split, `2110`, or the exhaustive `414b` placement
audit.

Final rebuilt PDF page count: 129.
