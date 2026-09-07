
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

The two former trace-exact atlas wrapper sources were removed.  Their fifteen
generated PNG panels are instead colocated under
[`paper_draft/figures/trace_exact_ab/`](paper_draft/figures/trace_exact_ab/)
and placed directly where the corresponding finite-enclosure cases are read.
The same preset registry drives the standalone
[`trace_exact_ab_envelope_explorer.html`](../interactive/trace_exact_ab_envelope_explorer.html).
One additional static illustration, `strategy4_core_case_example.png`, is
protected by an exact SHA-256 check.  All sixteen images are explanatory
publication assets, not proof authorities.

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

The compressed canonical paper is 88 pages (formerly 91). The proof-free rendering
is generated on demand; its former page count is not a fixed contract.  The tight expected CI page-count interval is 86--90;
the paper is not padded to meet that interval.

Both commands use a temporary source copy, so LaTeX intermediates do not
pollute the source directory. The tracked canonical PDF is a publication
artifact. CI compares clean rebuilds against it by stable PDF semantics and
rendered pixels.

## Compressed proof architecture

The body has six disjoint routing rows and four finite-witness recipes
B/C/D/F. The seven-point complementary-gap proof A remains an optional
appendix alternative, not a dependency of N0. The direct neighboring
bound replaces the full cubic-capacity evaluation in the paper. The
midpoint supplier and the two-vertex scalar replacement work in both CE1
and CE2, while their genuinely different local calculations remain explicit.
The three-page reduction removes repeated derivations rather than prose
explaining why a witness is fixed or why a strict endpoint is required.

The CI page-count contract is translated from 91 +/- 2 to 88 +/- 2 pages;
its width is unchanged. Clean PDF comparison, render audit, both exact
zero-gap programs, and all source checks remain mandatory.
