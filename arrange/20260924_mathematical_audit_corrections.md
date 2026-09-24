# Corrections following the mathematical review of 24 September 2026

Base: `9dfeadea2ae47f184e650dd8966f191173043943`.
Delivery branch: `chatgpt/math-audit-fixes-20260924092000`.

## Mathematical changes

1. **Area-loss coordinates.** In Lemma C.1 and the inline local square-loss
   proof, the nested sets are the images of `T intersect W` in the common
   `(U,V)` reference simplex, not the physical intersections. The Jacobian
   magnitude `D=1-t+t^2` does not depend on the translation slacks. This gives
   monotonicity of retained Euclidean area and justifies minimizing outside
   area at `alpha=tb`, `beta=(1-t)a`. Numbered source 3205 already used the
   reference-simplex argument; it now states the area factor and distinguishes
   area comparison from physical inclusion explicitly. The square-loss bounds
   and cyclic accumulation are unchanged.

2. **Disk-caliper scope.** The concluding contact description now explicitly
   excludes the disk-only alternative, in numbered theorem 2609 and both
   manuscript editions. A disk with its center as the sole listed point
   illustrates why the exception is necessary. The candidate normals and the
   separate Case F four-contact theorem are unchanged.

3. **BC witness count.** Theorem 7.0 in 2612 now names the five-point set
   `K_BC` and says that all five points are center-contained. It cites the
   existing strict enclosure inequality `Lambda(K_BC)>1`. Historical six-point
   compatibility sets elsewhere are intentionally retained.

The main case split, fixed witness formulas, endpoint strictness, both
replacement charts, capacity selectors, and all active/historical Case F
certificate files are unchanged.

## Regression protection

`arrange/_support/verify_math_audit_fixes.py`, invoked by `proof/check.py`, checks
exact reference-coordinate identities, Jacobian and slack-coefficient signs,
the rational counterexample to physical nesting, a disk-only fixture, and the
corrected text in all seven affected mathematical source files.

`arrange/_support/math_audit_fixes.json` records their exact before/after
SHA-256 hashes and the two manuscript replacements. The existing readability
baseline is **not reset**. Its checker first authenticates the revised files,
then restores only the approved old text/hashes in memory before comparing
all other formal statements, complete proof environments, and proof sources
against that same baseline. Thus these repairs cannot silently authorize
unrelated mathematical changes.

The dependency viewer is regenerated from the corrected paper; its source
links point to the delivery branch. The theorem graph and witness geometry
are not redesigned.

## Validation and publication

Local source, inter-edition, regression, and PDF-render checks pass. Local
builds retain 69 canonical pages and 67 inline-proof pages. Corrected pages
were rendered and visually inspected.

The delivery workflow repeats the checks using the repository's pinned Python
dependencies and TeX Live 2025 image, replays all three exact certificate
programs, rebuilds both tracked PDFs, and validates the generated assets before
publication. A separate publication job accepts only the allowlisted files
whose bytes match the validation manifest. Temporary transport files and
workflows are removed before the final PR checks.

Principal reproduction commands:

```bash
python proof/check.py
python arrange/_support/verify_inline_proofs.py
python arrange/_support/verify_readability_preservation.py
python interactive/generate.py --dependency-graph --check
python interactive/generate.py --trace-assets --check
python interactive/check.py
python arrange/build.py --all
```

The three exact certificate replay commands are the unchanged ones in
`.github/workflows/ci.yml`. These are executable mathematical and source
regressions, not a proof-assistant formalization or a claim that every
geometric argument has been independently formalized.
