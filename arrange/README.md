
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
appendices. The quarter-envelope revision has 65 pages. Each of its 79 theorem, lemma, proposition, and corollary
statements is immediately followed by its proof. It integrates all the
canonical proof calculations, consolidates ten remaining repeated statement entries,
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

The quarter-envelope revision has 67 canonical pages and 65 inline-proof pages,
compared with 70 and 68 after reusable-lemma shortening (76 and 73 before it).
The canonical CI guard is 65--69 pages. Page dimensions, fonts, and margins are unchanged. The reduction comes
from reusable forcing and threshold lemmas, deleted duplicate calculations
and wrappers, a single final assembly, and removal of example galleries.
The gallery image files remain available to interactive companions.

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
envelope followed by a capacity-free threshold criterion: four calipers are
automatically above one, and only one requires the capacity inequality. Neighboring suppliers are controlled
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

## Reusable-lemma shortening

See [the exact change report](20260923_reusable_lemmas_shortening_report.md).
BC and F now share the radial-deficit estimate; clipped BC radii and uniform
F radii use one total-endpoint forcing lemma. The canonical paper no longer
prints the old six-point witness table, generic unused M_c(a), candidate-demand
recovery, the unused CE2 total-slack lemma, or duplicate baseline proofs.
The dependency graph follows the surviving primary results and distinguishes
capacity-free geometry from its capacity-dependent covering application.

## Quarter-range envelope and ratio revision

See [the implementation report](20260923_quarter_envelope_revision_report.md).
Source 2615 proves the unchanged coupled BC theorem through the explicit
quarter-range envelope, retaining the exact witness radii. The prior wider
3/8-range envelope is retained separately in source 2615a, not silently
restated on a smaller domain. Both local D adapters keep their original
endpoint and size conditions but use shorter factored ratio estimates.
The new strict own-ray lemma feeds the preliminary F radial bound, not the
terminal exact certificate. The approved inventory now has 89 canonical and
79 inline formal statements; 77 complete proof bodies are matched between
editions. The previous inventory and the two intentionally replaced supplier
hashes are archived; all other preservation contracts remain enabled.

## Case F explicit-comparison revision

The active fixed-start Case F calculation is [3105b_explicit_comparison_enclosure.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105b_explicit_comparison_enclosure.md).
The original nine witnesses and actual disk are unchanged. The tangent proof
uses explicit cubic/quadratic comparisons and exact coefficient budgets, with
remaining degree-27 boundary Taylor work. It no longer reads an SOS witness file
or a Bernstein transcript. The old exact programs remain historical CI checks.

Run the active calculation from the repository root:

```bash
python proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_explicit_stage.py --output /tmp/F-explicit.json
```

The new [fixed-start viewer](../interactive/f_explicit_comparison.html)
is a numerical illustration, not a proof. Older F Newton/cap-chain captures
are labeled historical. See `arrange/20260924_f_explicit_comparison_integration.md`
for the integration and validation record.
