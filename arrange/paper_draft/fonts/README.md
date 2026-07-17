# Embedded Hangul font subsets

The manuscript uses two small static subsets of Noto Sans KR solely to render
the source term `걸거치는` required by the authoring guide.  The subsets were
derived from `@fontsource/noto-sans-kr` version 5.2.9:

- `noto_sans_kr_subset_115.ttf` contains U+AC78 (`걸`);
- `noto_sans_kr_subset_118.ttf` contains U+AC70, U+CE58, and U+B294
  (`거`, `치`, `는`).

The upstream WOFF files were converted losslessly to TrueType with
FontTools by loading each font, clearing its WOFF flavor, and saving it.  An
empty U+0020 glyph with the upstream font's standard space width was then
added to each subset so XeLaTeX can initialize it without a missing-space
warning.
The SIL Open Font License is reproduced in `OFL.txt`.

Compile the paper with XeLaTeX so `fontspec` can load these local fonts.
