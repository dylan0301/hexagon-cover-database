# Paper with proofs following statements

This 65-page additional edition has no appendices. Its 79 formal results each have
an immediate proof. The introduction announces the main result; the formal
main theorem and scaling corollary conclude the paper. Both editions share the new geometric overview and witness explanations.
The numbered sources include the approved five-point BC and four-point D replacement.
The exact zero-gap certificate data are unchanged.

From the repository root:

```bash
python arrange/build.py --inline-proofs
python arrange/_support/verify_inline_proofs.py
python arrange/_support/verify_readability_preservation.py
```

The clean build is `arrange/_build/inline_proofs.pdf`; the tracked publication
PDF is [main.pdf](main.pdf). The builder compiles [main.tex](main.tex) from
`arrange/paper_draft/` in a temporary source copy, reusing the existing figures.
`python arrange/build.py --all` builds both editions. CI compares both tracked
PDFs with pinned clean rebuilds and audits all rendered pages. Only the canonical
edition retains the existing page-count guard.

## Reading order and consolidation

The seven sections contain the introduction, common geometry, trace bounds,
area loss, nonzero-gap enclosure, zero-gap enclosure, and final assembly.
Common geometry includes the corner charts, exact-trace normalization,
strict handoffs, admissible cells, and signed-center normal form. Supporting
results precede their use; definitions precede the calculations using them.

The shortened canonical manuscript has 89 formal statements; this edition has
79, consolidating the ten remaining duplicate entries. The source map records
those merges and equation aliases. Four formerly separate body/appendix pairs
were already merged in the canonical edition during this shortening.

The correspondence audit checks 77 retained canonical proof bodies against
this edition, and checks that all 79 results have immediate proofs. Reviewed
changes to the common forcing argument, BC threshold criterion, and shared
BC/F bound are recorded in the shortening report; they are not described as
unchanged pre-refactor text. The D four-caliper proof remains byte-pinned to
its former appendix proof. Raw (3,0) normalization, both replacement charts,
and the unchanged local endpoint calculations retain their preservation checks.
The two supplier ratio arguments are intentionally replaced by factorizations;
their before/after hashes and actual-endpoint contracts are recorded separately.

The exact certificate's reduction, signs, checking rules, immutable source
link, transcript digest, and provenance are included in the zero-gap section.
Its existing machine data and both exact verifiers accompany the manuscript;
their contents are unchanged. No inactive alternative argument is introduced.

## Maintenance

The TeX files are directly editable sources. If a canonical result changes,
update the corresponding statement and proof here and rerun the preservation
audit. Update the map only for reviewed editorial consolidations; do not use
it to exempt a changed mathematical argument from proof review. Run both exact
certificate programs for changes to the certificate or its dependent theorem,
as required by the repository instructions.

The edition-specific layout keeps the end of each statement with the start
of its proof and places shared figures at their source positions. Run
`python arrange/_support/verify_inline_proofs.py --pdf arrange/_build/inline_proofs.pdf`
to check the rendered proof count, appendix referrals, and separated proof starts.

The quarter-envelope inventory contains 79 immediate proof environments. Its
pre-revision baseline is archived alongside the older readability baselines.
The current inventory is protected by the same source-regression audit; this
is a reviewed mathematical refactor, not merely proof relocation. Font sizes,
page dimensions, and margins are unchanged.

The [quarter-envelope report](../../20260923_quarter_envelope_revision_report.md)
records the polynomial BC comparison proof, factored T3-like/Vd1 ratios, and
strict own-ray lemma used by F. The exact BC/D/F witnesses, the capacity-free
five-point threshold, four-point calipers, and exact certificate are unchanged.
