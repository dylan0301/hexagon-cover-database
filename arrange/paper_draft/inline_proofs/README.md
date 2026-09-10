# Paper with proofs following statements

This 64-page additional edition has no appendices. Its 83 formal results each have
an immediate proof. The introduction announces the main result; the formal
main theorem and scaling corollary conclude the paper. The canonical edition
and all numbered mathematical sources are unchanged.

From the repository root:

```bash
python arrange/build.py --inline-proofs
python arrange/_support/verify_inline_proofs.py
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

The 97 canonical statement entries become 83 statements by consolidating
14 repeated entries. [source_map.json](source_map.json) records the merges
against canonical revision `9447b27ae5b5feefefb2209fd45cd7c1a4de4292`.
Each merged statement retains both original statement labels. The two repeated
zero-gap equation targets are redirected to the single retained equations;
the map records these reference aliases explicitly.

All 81 retained canonical proof bodies are checked against the new edition.
Type-aware references and whitespace may change. Three documented prose edits
remove a forward consequence referral, defer reach notation until after
normalization, and include the four-point convex combination in its full proof.
The BC proof also includes the original covering-forcing conclusion. The
detached main proof is preserved, and its scaling deduction becomes the
corollary's separate immediate proof. These are editorial regression checks,
not a proof-assistant verification of the mathematics.

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
