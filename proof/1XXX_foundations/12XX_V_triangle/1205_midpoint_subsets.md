# Local Midpoint Subsets Over $S_{1/2}$

Status: Reference

This inventory concerns maximal normalized $V_0$-triangles over the
half-skeleton target $S_{1/2}$. It records which subsets of the local midpoint
set can occur after maximalizing for $S_{1/2}$.

Warning. This inventory is not a statement about arbitrary $V_0$-triangles, and
it is not a statement about maximal triangles over the full skeleton $S$. For
example, a maximal T3-like triangle over $S$ may contain no midpoints. In
full-skeleton arguments, midpoint containment must come from the cover
hypotheses, midpoint-counting, type definitions, or a separate lemma; do not
infer it from this $S_{1/2}$ inventory alone.

For a normalized $V_0$-triangle over $S_{1/2}$, the local midpoint set is

$$
\{M_5,M_0,M_1\}.
$$

Midpoint subsets for maximal normalized $V_0$-triangles over $S_{1/2}$:

- Vd0 $n=0$: $\varnothing$ or $\{M_0\}$. The older split assigned these
  possibilities to $(o,n)=(1,0)$ and $(2,0)$ respectively. The corrected
  Vd0 definition also includes $(3,0)$; it adds no adjacent-midpoint coverage
  for an original open role because such coverage would give positive
  adjacent-ray support.
- Vd1 $(o,n)=(1,1)$:
  $$
  \varnothing,\ \{M_0\},\ \{M_1\},\ \{M_5\},\ \{M_0,M_1\},\ \{M_0,M_5\}.
  $$
- Vd2 $(o,n)=(1,2)$:
  $$
  \{M_0\},\ \{M_0,M_1\},\ \{M_0,M_5\},\ \{M_0,M_1,M_5\}.
  $$
- T3-like $(o,n)=(2,1)$:
  $$
  \{M_1\},\ \{M_5\}.
  $$

Symmetry note. This inventory lists midpoint subsets before quotienting
by the reflection symmetry fixing $V_0$ and $M_0$ and swapping $M_1$ with
$M_5$. In case analysis, reflected copies need not be considered separately
when the surrounding hypotheses are reflected with the local data. For
example, the Vd1 cases $\{M_1\}$ and $\{M_5\}$ are equivalent, as are
$\{M_0,M_1\}$ and $\{M_0,M_5\}$.
