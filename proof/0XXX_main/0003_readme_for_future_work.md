# README For Future Work

Status: Research hygiene

These files are concise research notes, not a single finished proof of the main theorem.

The final theorem is about seven **open** unit equilateral triangles covering the side-$1$ hexagon. Closed triangles and expanded hexagons occur through the Lebesgue-number/scaling equivalence.

Rules:

- Do not cite a result as proven unless its file says `Status: Proven`, `Status: Proven local lemma`, or `Status: Proven analytic inequality`.
- Numerical optimization remains `Empirical` unless a certificate is supplied.
- Failed ideas are kept in detail to avoid repeating dead ends.
- The Korean term **걸거치는** is preserved where it names the recurring geometric phenomenon of a triangle crossing or straddling adjacent structure in a non-axis-aligned way.
- No images are included in this folder.
- All files are markdown-only.
- In math, write cardinalities as
  `\left\lvert \left\lbrace\, ... \,\right\rbrace \right\rvert`;
  do not use hash-based notation for cardinality.
- In math, use `\mathrm{...}` for named operators; do not use the operatorname
  macro.
- For `\sup`, `\inf`, `\min`, and `\max`, put conditions in subscripts, using
  `\substack{...}` when multiple lines are needed. Do not put alignment
  markers inside operator arguments.
