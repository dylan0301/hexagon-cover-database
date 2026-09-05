# Zero-gap four-contact proof update

Base: `a1c9ccb569a5549044498984490b24d36417de8e`.
Branch: `chatgpt/zero-gap-four-contact-20260905120108`.

## Mathematical change

The zero-gap, `N_+=1` theorem retains its type-independent scope and all nine
forced points. The six radial points are compressed to their inscribed disk
by containment, not by an equality of enclosure problems. The easy region
`c_* <= 2/3` still closes by that disk alone.

For the hard region, the same Newton inner points form a convex three-point
chain outside the disk. Its only exposed straight contacts are the lines
through consecutive points and the two outer disk tangencies. The general
disk--finite-set caliper theorem therefore reduces the minimum enclosure to
four support sums. The two line bounds are the former analytic adjacent
estimates. The two tangent tests are the former mixed squared residuals.

The exact certificate is evaluated at a smaller rational radius. The new
simultaneous radius-transfer lemma transfers the two residuals together to
the actual radius. It uses the triangle inequality at the smaller radius,
the endpoint `e=1/3`, and convex interpolation. No separate monotonicity of
an individual residual is asserted.

The active terminal no longer constructs a Minkowski sum, the auxiliary
point `C+RA`, support caps, or a cyclic cap covering. The Newton construction,
rational radial envelopes, eight core polynomials, and twenty global
Bernstein identities remain in the proof.

## Determinant orientation

The geometric positive determinant is
`Delta = cross(C,RA) = cross(R^{-1}C,A) > 0`.
The previous paper incorrectly attached a positive sign to the reversed
determinant `cross(A,R^{-1}C)`. The wrapper now fixes the orientation and
explicitly records that the authenticated code uses the opposite sign.
Every occurrence in its residuals is squared, so no polynomial coefficient,
verifier byte, provenance manifest, or authenticated digest changes.

## Source ownership

- `2611_four_contact_disk_enclosure.md`: new proved common lemmas for the
  four-contact hull, tangent tests, and simultaneous radius transfer.
- `31054_four_cap_enclosure_reduction.md`: rewritten terminal geometry;
  retained Newton formulas and complete adjacent-line calculations.
- `31055_rational_radial_envelopes_and_mixed_reduction.md`: retained exact
  elimination, with the tangent interpretation and radius-transfer link.
- `31057_terminal_nine_point_enclosure.md`: new four-contact assembly.
- The `26XX` index, reusable-lemma catalog, `2610` terminal interface, and
  `31050` package index point to the new proved interface.

Historical filenames are retained for incoming links; their active titles
and proof contents describe the new route. Earlier alternative packages and
historical provenance are not deleted.

## Paper and navigation

The main finite-enclosure proof and abstract now identify four contacts and
two tangent bounds. Appendix E contains the convex-chain geometry,
four-contact minimization formula, tangent tests, radius-transfer lemma, and
terminal assembly. Appendix F retains the exact certificate and replaces
its cap implication by the actual-radius tangent implication.

The former support-cap figure is replaced by an exposed-hull/tangent figure
at the same registered path. The diagram is illustrative, not a proof object.
The dependency graph generator records the new proof dependencies, including
the separation of the line-geometry theorem from the exact certificate.
The generated graph and compiled canonical PDF are rebuilt.

## Validation

The local clean build has 92 pages, the same as the baseline, with no overfull
boxes or unresolved references. All 92 pages pass the repository render scan;
the new figure, contact lemma, transfer lemma, and certificate interface are
also visually inspected.

Both existing exact certificate programs return `PASS`. The unchanged core
transcript digest is

```
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```

The new `verify_four_contact_identities.py` verifies ten exact identities,
including the determinant crosswalk, two Gram factors, tangent projections,
and affine interpolation. `proof/check.py` invokes it and guards the new
paper labels and removal of the active cap terminal. These checks supplement,
not replace, the two authenticated certificate verifiers.

Local source checks and the interactive audit pass. The sandbox cannot fetch
network packages, so the complete pinned Python/Node/TeX environment and the
tracked-PDF comparison are checked again in Actions. The final pull request
and its exact-head check runs are the authoritative remote check record.

## Delivery safeguards

A temporary read-only Actions snapshot supplied the public baseline after
sandbox GitHub DNS/network access failed; that snapshot workflow was removed
immediately. Publication uses the feature branch only, audited manifests,
non-forced updates, and removal of all temporary files before the PR. The
persistent CI workflow and its page-count bounds are not weakened or changed.
