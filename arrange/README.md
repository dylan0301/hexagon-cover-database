
# Manuscript and publication support

`paper_draft/main.tex` is the self-contained publication source. Its concise
body gives the geometric definitions and three proof methods:

1. trace length;
2. area loss;
3. direct finite enclosure.

Appendices A--E contain the solved structural, trace, area, nonzero-gap, and
zero-gap optimizations.  The existing
`A_zero_gap_exact_certificate.tex` is input last and therefore renders as
Appendix F; it records the exact mixed-overlap certificate required by the
zero-gap nine-point theorem. The numbered files under `proof/` remain the
authority for theorem status and hypotheses; the manuscript is the
publication layer.

The trace-exact panels remain available under
`paper_draft/figures/trace_exact_ab/` and in the standalone explorer.
The canonical paper includes only the illustrations needed for its active
arguments. These assets explain the geometry; they are not proof authorities.

## Section-to-proof map

| Manuscript component | Principal proof material |
|---|---|
| Introduction and routing | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| Common geometry | `1001`-`1214`, `2004`, `2008b`, `2100`, `2109` |
| Trace-length method | `2500`, `2510`, `2530`--`2532` and routed terminals |
| Area-loss method | `3205`, `2400` (T3-like alternative retained outside the paper) |
| Nonzero-gap finite enclosure | `2008b`, `2612`--`2614`, `2609`, `4102_new`, `4130_new`, `4143_new`, `4144_new` |
| Zero-gap nine-point theorem | `31050`-`31059` and `3105X_computation` |
| Exhaustive completion | `0000` |

## Commands

```bash
python -m pip install -r arrange/_support/requirements.txt
python interactive/generate.py --trace-assets --check
python arrange/build.py --canonical
python arrange/build.py --all
arrange/_support/build_proof_free_paper.sh
```

The canonical build is written to `arrange/_build/canonical.pdf`. The
proof-free command writes `arrange/paper_draft/proof_free.pdf`; it removes
formal proof environments while retaining prose and calculations outside
those environments.

The shortened canonical paper has 66 pages, compared with 89 in the audited
base revision; its proof-free version has 36 pages, compared with 50.
The CI page-count guard is 64--68. No font-size or margin reduction is used.

Both commands use a temporary source copy, so LaTeX intermediates do not
pollute the source directory. The tracked canonical PDF is a publication
artifact. CI compares clean rebuilds against it by stable PDF semantics and
rendered pixels.

## Active proof architecture

The body has six routing rows and three witness recipes BC/D/F.
Optional A and B, the own-endpoint seven-point specialization, the older
one-Vd radial-separation arguments, and the fifth-handoff corollary are not
compiled. Their numbered proof sources remain available in `proof/`.

The raw `(3,0)` exact-trace normalization is retained, including its complete
calculation. All actual reaches are defined after that normalization.
The self-midpoint obstruction is a corollary of the exact admissible set.
A shared corner chart supplies both incidence geometry and area loss.

The first CE1 return step is stated independently of the T2/T3 own-radial
demands. BC uses it to recover the final demand before invoking the full
return. The supported-rescuer calculation has one common four-point ending,
and both replacement charts and their strict margins remain intact.

See `20260909_paper_shortening_implementation_report.md` for the removal
packages, preservation contracts, and validation record. Clean PDF comparison,
render audit, both exact zero-gap programs, and source checks remain mandatory.
