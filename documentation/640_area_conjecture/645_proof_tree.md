# Proof Tree for the Area Conjecture Route

Status: Reference / strategy

This file records the proof-tree structure for the area-conjecture route.  The
CE0 six-point case is the main goal.  The CE1/reduced-CE2 seven-point case is a
separate extension.

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

Conditional CE0 certificate route:
  prove or certify the local square-loss bounds
    a+b <= 1  =>  f(a,b) <= 1 - min(a,b)^2
    a+b >  1  =>  f(a,b) <= 1 - max(a,b)^2
  then apply 647_CE0_conditional_area_certificate.md
  conclusion under these local bounds:
    if at least two rows satisfy a_i+b_i>1, then
      sum_i f(a_i,b_i) < 99/20 < 5

Older monotonicity threshold route:
  identify rows with a_i+b_i>1
  require at least two such rows
  for rows with a_i+b_i>=1+epsilon, use
    f(a_i,b_i) <= f(a_i,1+epsilon-a_i)
  handle 1<a_i+b_i<1+epsilon as a boundary regime
  optionally investigate whether a global replacement map is valid

Contradiction after either valid certificate:
  the six vertex triangles contribute less than five unit-triangle areas
  the center triangle contributes at most one unit-triangle area
  the seven unit triangles then contribute less than area(H)
  so they cannot cover H
```

The conditional CE0 certificate route is now the shortest recorded path for the
CE0 six-point area target.  It still depends on local square-loss upper bounds
for $f(a,b)$.

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

2. Local vertex area bounds.

   For each row $(a,b)$, prove or certify the needed upper bound for $f(a,b)$.
   For the conditional CE0 certificate, it is enough to prove the square-loss
   bounds

   $$
   a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
   $$

   and

   $$
   a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
   $$

   A structural proof may use the conjectured axis-aligned and Type 2 realizers
   from `641_area_function_and_monotonicity.md`, but a structural proof is not
   required if the displayed upper bounds are independently certified.

3. Pointwise threshold-bound reduction.

   This remains relevant to the older threshold route and to possible CE1 or
   reduced-CE2 extensions.  For every row with
   $a_i+b_i\ge1+\varepsilon$, monotonicity should justify

   $$
   f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
   $$

   The proof must also separate the boundary regime
   $1<a_i+b_i<1+\varepsilon$.

4. Global replacement formulation.

   Decide whether the older formulation, replacing supercritical rows by a
   valid cut-point configuration on $a_i+b_i=1+\varepsilon$, can be made
   correct.  This is optional for the pointwise strategy and is not used in
   `647_CE0_conditional_area_certificate.md`.

5. Final inequality.

   In the CE0 six-point model, the final inequality is now proved in
   `647_CE0_conditional_area_certificate.md` conditional on the local
   square-loss bounds.

   For the CE1/reduced-CE2 extension, the final inequality remains open in this
   package:

   $$
   \sum_{i=0}^5 f(a_i,b_i)<5.
   $$

   A proof must include boundary regimes and degenerating regimes such as
   $t\to s$.

## Failure modes to separate

The proof should keep the following cases separate instead of hiding them in
the main inequality:

- no supercritical row after the relevant perimeter data is fixed;
- a row exactly tangent to the threshold $a_i+b_i=1$;
- degenerate active interval $t=s$;
- full CE2 before the one-interval reduction;
- any numerical search result without a certificate.
