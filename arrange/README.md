
# Manuscript and publication support

`paper_draft/main.tex` is the publication source; the exact electronic
certificate identified in Appendix F accompanies the manuscript. Its concise
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

`paper_draft/inline_proofs/main.tex` is an additional edition with no
appendices. The BC/D revision has 73 pages. Each of its 82 theorem, lemma, proposition, and corollary
statements is immediately followed by its proof. It integrates all the
canonical proof calculations, consolidates 14 repeated statement entries,
and places the main theorem and scaling corollary at the end. The certificate
explanation is part of the zero-gap argument; the authenticated data and
verifiers remain accompanying files. See
[`inline_proofs/README.md`](paper_draft/inline_proofs/README.md) for the source map
and preservation audit. Both editions now share the human-readable overview and witness explanations.

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
| Nonzero-gap finite enclosure | `2008b`, `2612`--`2616`, `4130_new`, `4143_new`, `4144_new`; `4102_new` retained only as a historical alternative |
| Zero-gap nine-point theorem | `31050`-`31059` and `3105X_computation` |
| Exhaustive completion | `0000` |

## Commands

```bash
python -m pip install -r arrange/_support/requirements.txt
python interactive/generate.py --trace-assets --check
python arrange/build.py --canonical
python arrange/build.py --inline-proofs
python arrange/build.py --all
python arrange/_support/verify_inline_proofs.py
python arrange/_support/verify_readability_preservation.py
arrange/_support/build_proof_free_paper.sh
```

The canonical build is written to `arrange/_build/canonical.pdf`. The
additional edition is written to `arrange/_build/inline_proofs.pdf`; `--all`
builds both. Its tracked publication artifact is
`arrange/paper_draft/inline_proofs/main.pdf`. The
proof-free command writes `arrange/paper_draft/proof_free.pdf`; it removes
formal proof environments while retaining prose and calculations outside
those environments.

The BC/D finite-caliper revision has 76 canonical pages and 73 inline-proof pages
(previously 69 and 64). The canonical CI guard is 73--78 pages. Page dimensions,
font family, and margins are unchanged; reader headings and proof-start page
break protection are improved. The older proof-free export is not the
reader-facing publication artifact for this revision.

The build commands use a temporary source copy, so LaTeX intermediates do not
pollute the source directory. Both tracked edition PDFs are publication
artifacts. CI compares clean rebuilds against them by stable PDF semantics and
rendered pixels. The additional edition has no page-count target.

## Active proof architecture

The body has six routing rows and three witness recipes BC/D/F.
Optional A and B, the own-endpoint seven-point specialization, the older
one-Vd radial-separation arguments, and the fifth-handoff corollary are not
compiled. Their numbered proof sources remain available in `proof/`.

The raw `(3,0)` exact-trace normalization is retained, including its complete
calculation. All actual reaches are defined after that normalization.
The self-midpoint obstruction is a corollary of the exact admissible set.
A shared corner chart supplies both incidence geometry and area loss.

BC now uses five fixed points, two nonuniform capacity pairs, and a rational
envelope followed by five finite calipers. Neighboring suppliers are controlled
before enclosure; the only clipped radial witness gives a diameter exit.
D uses four finite calipers under a ratio-only geometric hypothesis. The CE1
return is historical, not an active terminal dependency. Both replacement
charts and their strict margins remain intact. See
[the integration report](20260922_bc_d_finite_caliper_integration.md).

See `20260909_paper_shortening_implementation_report.md` for the removal
packages and preservation contracts. The subsequent reading-order repair
is documented in `20260910_self_containment_editorial_report.md`. Clean PDF comparison,
render audit, both exact zero-gap programs, and source checks remain mandatory.

## Human-readability revision

See [the reviewer report](20260913_readability_review_report.md). The canonical
introduction explains the boundary/interior tradeoff before the detailed
classifications, which now appear in common geometry. Shared passages in
`paper_draft/reading_guide/` explain coverage scope, fixed witnesses, candidate
enclosures, replacement, and the zero-gap comparison sets. The approved mathematical inventory is protected by the readability-preservation
audit; its prior baseline is archived for this explicit mathematical revision.
