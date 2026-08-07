> **Superseded on 2026-08-07.**  The T3, rescuer, and Vd domain extractions and the verification split described below as remaining work are completed by `20260807_strategy2_optimization_extraction_audit.md`.

# Strategy 2 Implementation Audit: Remaining Work and Conclusion

## 11. What remains incomplete and why

### T3-like endpoint domain

The objective is pure, but the full feasible set is distributed across the
`407X` label files.  Consolidating it requires copying every selector,
radical sign condition, and equality assignment into one finite domain
registry.  Omitting any selector could admit a spurious algebraic root.

### Adjacent-rescuer domain

The current proof starts from a translated geometric normal form.  Its
rational parameters and sign conditions must be isolated before the problem
is formalization-ready.

### Vd terminal domains

The adjacent and nonadjacent objectives are already scalar, but some inputs
are defined by placement suprema.  Those suprema must be eliminated or
introduced as variables with exact graph constraints.

### Consolidated verification file

`04_strategy2_verification.tex` still contains historical reader summaries
and alternates between bridge arguments and optimization proofs.  Removing
that duplication should be the next editorial pass, after the new
optimization registry is stable.  Deleting it immediately would risk losing
proof details or changing a dependency, so this revision leaves it intact.

## 12. Reviewer conclusion

The proof should not be presented as a long catalogue of local formulas.
Its conceptual Strategy 2 content is a monotone propagation argument with
four terminal shapes.  The calculations are legitimate, but they belong in
named optimization problems with explicit domains and objective functions.

The current revision establishes that architecture and makes the four central
all-Vd0 calculations ready for formalization.  A second revision should
complete the real-domain extraction for the T3, rescuer, and Vd terminals and
then split the consolidated verification appendix into geometry-bridge and
optimization-proof files.
