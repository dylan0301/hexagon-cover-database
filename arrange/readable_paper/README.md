# Reader-oriented paper tree

This directory is a new publication tree.  It does not modify or replace
`arrange/paper_draft/`; unchanged sections are resolved from that directory
through TeX's input path, while the reorganized introduction, Method 3
chapters, appendices, and completion live here.

## Build

```bash
cd arrange/readable_paper
./build.sh
```

The public architecture is:

1. introduction and stable routing IDs;
2. common geometry;
3. Method 1: trace/skeleton length;
4. Method 2: area loss;
5. Method 3 toolkit and nonzero-gap obstructions;
6. separate zero-gap nine-point obstruction;
7. exhaustive completion;
8. finite-enclosure calculation appendix;
9. nonzero-gap trace-exact atlas;
10. exact mixed-overlap certificate.

The original historical nine-point TikZ figure is restored in
`figures/strategy4_nine_point_witness.tex`.  Its asymmetric positions are
explicitly marked as schematic; all proofs use the parameter-dependent exact
formulas.
