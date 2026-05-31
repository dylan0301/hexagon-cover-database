# Proof Tree for the Area Conjecture Route

Status: Reference / strategy

This file records the intended proof-tree structure for the area-conjecture
route.  The CE0 six-point case is the main goal.  The CE1/reduced-CE2
seven-point case is a separate extension.

## Main CE0 proof tree

```text
Main target:
  rule out a seven-open-unit-triangle cover in the CE0 case

Input assumptions:
  T_C is CE0

Six-point perimeter data:
  one ordinary cut point on each edge: x_0,...,x_5

Induced rows:
  (a_i,b_i) = (1-x_{i-1},x_i), i=0,...,5

Local area bounds:
  vertex rows bounded by f(a_i,b_i)

Monotonicity relaxation:
  identify rows with a_i+b_i>1
  require at least two such rows
  for rows with a_i+b_i>=1+epsilon, use
    f(a_i,b_i) <= f(a_i,1+epsilon-a_i)
  handle 1<a_i+b_i<1+epsilon as a boundary regime
  optionally investigate whether a global replacement map is valid

Area certificate target:
  prove sum_i f(a_i,b_i) < 5

Contradiction:
  the six vertex triangles contribute less than five unit-triangle areas
  the center triangle contributes at most one unit-triangle area
  the seven unit triangles then contribute less than area(H)
  so they cannot cover H
```

## CE1/reduced-CE2 extension tree

```text
Extension target:
  rule out a seven-open-unit-triangle cover in the CE1 or reduced-CE2 case

Input assumptions:
  T_C is CE1
    or
  T_C is CE2 and the CE2 one-interval lemma has reduced to one active interval

Normalize:
  active C-only interval T_C cap e_{0,1} = [s,t]

Seven-point perimeter data:
  C endpoints on e_{0,1}: s,t
  ordinary cut points on the other edges: x_1,...,x_5

Induced rows:
  (a_0,b_0) = (1-x_5,s)
  (a_1,b_1) = (1-t,x_1)
  (a_i,b_i) = (1-x_{i-1},x_i), i=2,3,4,5

Local area bounds:
  vertex rows bounded by f(a_i,b_i)

Monotonicity relaxation:
  identify rows with a_i+b_i>1
  require at least two such rows
  for rows with a_i+b_i>=1+epsilon, use
    f(a_i,b_i) <= f(a_i,1+epsilon-a_i)
  handle 1<a_i+b_i<1+epsilon as a boundary regime
  optionally investigate whether a global replacement map is valid

Area certificate target:
  prove sum_i f(a_i,b_i) < 5

Contradiction:
  the six vertex triangles contribute less than five unit-triangle areas
  the center triangle contributes at most one unit-triangle area
  the seven unit triangles then contribute less than area(H)
  so they cannot cover H
```

## Required sublemmas

The proof tree depends on the following unresolved pieces.

1. CE2 one-interval reduction.

   The CE2 use of this package assumes one CE2 interval can be removed as
   already covered by adjacent vertex triangles.  This is recorded elsewhere as
   a target lemma, not a proven theorem.

2. Local vertex area bound.

   For each row $(a,b)$, prove or certify the needed upper bound for $f(a,b)$.
   A structural proof may use the conjectured axis-aligned and Type 2
   realizers from `641_area_function_and_monotonicity.md`.

3. Pointwise threshold-bound reduction.

   For every row with $a_i+b_i\ge1+\varepsilon$, use monotonicity to justify

   $$
   f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
   $$

   The proof must also separate the boundary regime
   $1<a_i+b_i<1+\varepsilon$.

4. Global replacement formulation.

   Decide whether the older formulation, replacing supercritical rows by a
   valid cut-point configuration on $a_i+b_i=1+\varepsilon$, can be made
   correct.  This is optional for the pointwise strategy but should not be
   treated as established without a valid global map.

5. Final inequality.

   Prove

   $$
   \sum_{i=0}^5 f(a_i,b_i)<5
   $$

   after applying the pointwise threshold bounds, on every parameter regime
   with at least two supercritical rows.  Include boundary regimes.  For the
   CE1/reduced-CE2 extension, also separate degenerating regimes such as
   $t\to s$.

## Failure modes to separate

The proof should keep the following cases separate instead of hiding them in
the main inequality:

- no supercritical row after the relevant perimeter data is fixed;
- a row exactly tangent to the threshold $a_i+b_i=1$;
- degenerate active interval $t=s$;
- full CE2 before the one-interval reduction;
- any numerical search result without a certificate.
