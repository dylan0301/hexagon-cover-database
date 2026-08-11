# Strategy 2 Implementation and Remaining-Work Audit

## 8. File-level revision

### `04_strategy2_summary.tex`

Replaced the formula catalogue by:

- a plain-language mechanism;
- one certified-chain definition;
- the exact center-free path condition;
- the four terminal endings;
- the active-gap kernel;
- concise endpoint, return, T3, rescuer, Vd, and replacement interfaces;
- a branch-to-optimization register;
- the unchanged branch-closure proposition.

Important external labels were retained so existing appendix and assembly
references continue to resolve.

### `04_strategy2_optimization_problems.tex`

Added a new appendix containing:

- the exact piecewise bivariate capped-output function;
- pure affine and threshold trial maps;
- the strict branch-certificate convention;
- the pure signed domains;
- four formalization-ready optimization problems;
- three explicitly identified partial interfaces;
- a formalization-readiness table.

### `main.tex`

The new optimization appendix is inserted before the consolidated Strategy 2
verification.  This makes the logical order:

$$
\text{body routing}
\to
\text{signed and local bridges}
\to
\text{optimization statements}
\to
\text{proofs}.
$$

### `appendix_roadmap.tex`

The roadmap is revised to distinguish geometry extraction from pure
optimization and verification.

## 9. Formalization order

The recommended order is:

1. define and verify the piecewise function $F$;
2. formalize S2-E1;
3. formalize S2-E2;
4. formalize S2-R2;
5. formalize S2-R1;
6. extract and formalize the rescuer domain;
7. extract and formalize the Vd domains;
8. extract and formalize the T3 four-label domain;
9. formalize the two-chart replacement directly as geometry.

S2-E1 and S2-E2 are the correct initial tests because they require only two
function evaluations and expose every issue with branch endpoints, radicals,
and strict equality exclusion.
