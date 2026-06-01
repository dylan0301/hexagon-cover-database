# Threshold Relaxation

Status: Strategy

This file records the monotonicity relaxation intended for the CE0 six-point
area route and the CE1/reduced-CE2 seven-point extension.

## Supercritical rows

A vertex row is called supercritical here when

$$
a_i+b_i>1.
$$

The area strategy focuses on configurations where one or more rows are
supercritical after the relevant perimeter cut data has been fixed.

By monotonicity of $f(a,b)$, increasing either coordinate can only decrease the
local maximum inside area.  Therefore the worst area case for a supercritical
row should occur near the threshold

$$
a_i+b_i=1.
$$

## Pointwise threshold bound

Fix a small number

$$
\varepsilon>0.
$$

For a supercritical row with

$$
a_i+b_i\ge1+\varepsilon,
$$

monotonicity gives the pointwise bound

$$
f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
$$

Indeed,

$$
1+\varepsilon-a_i\le b_i,
$$

so the second boundary coordinate has been decreased while the first coordinate
is kept fixed.  Since decreasing a coordinate enlarges the feasible triangle
search space, the value of $f$ can only increase.  Therefore the
near-threshold row gives an upper bound for the original row's inside-area
contribution.

This is the primary threshold relaxation in this package.  It is termwise and
does not require constructing a new global perimeter configuration.

Rows with

$$
1<a_i+b_i<1+\varepsilon
$$

are not covered by this fixed-$\varepsilon$ inequality.  They should be treated
as a boundary or limiting regime.

## Application to CE0

In the CE0 six-point model,

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Thus the pointwise threshold bound applies to row $i$ whenever

$$
1-x_{i-1}+x_i\ge1+\varepsilon.
$$

In that case,

$$
f(1-x_{i-1},x_i) \le f(1-x_{i-1},x_{i-1}+\varepsilon).
$$

## Application to CE1/reduced-CE2

In the CE1 and reduced-CE2 seven-point model, the rows are

$$
(a_0,b_0)=(1-x_5,s),
$$

$$
(a_1,b_1)=(1-t,x_1),
$$

and, for $i=2,3,4,5$,

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

The same pointwise threshold bound applies to any row satisfying
$a_i+b_i\ge1+\varepsilon$:

$$
f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
$$

Only the formulas for the inputs $(a_i,b_i)$ differ from the CE0 case.

## Global replacement formulation

An older formulation of the relaxation was to replace every supercritical row
by a row on the near-threshold line

$$
a_i+b_i=1+\varepsilon.
$$

This should now be treated as a global replacement formulation, not as the
primary relaxation.  It may be useful, but one should check whether it is
actually correct: changing one perimeter cut point affects adjacent rows, so a
simultaneous replacement of all supercritical rows may fail to define a valid
global cut-point configuration or may change neighboring rows in an
uncontrolled way.

## Maximizing neighboring subcritical rows

The perimeter cut points are shared by adjacent rows.  Changing one cut point
can decrease a supercritical row while increasing a neighboring subcritical
row.
The global replacement formulation would need to prove:

1. keep each designated supercritical row supercritical;
2. push each such row down to $a_i+b_i=1+\varepsilon$;
3. within those constraints, maximize the neighboring subcritical $b$- or
   $a$-coordinates that increase the possible inside-area contribution.

If this can be done, the result would be a cleaner finite-dimensional target in
which the hardest rows are placed near threshold, while the adjacent
subcritical rows have been made as favorable as the supercritical constraints
allow.  This package does not yet claim that the global replacement
formulation is valid.

## Proof obligation

The pointwise relaxation is not complete until the proof specifies which rows
are bounded by

$$
f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i)
$$

and separates the boundary regime $1<a_i+b_i<1+\varepsilon$.

The global replacement formulation has an additional obligation: it must be
written as an explicit map from the original cut points to relaxed cut points
and checked to preserve the relevant parameter domain.

For a global CE0 replacement, this means preserving

$$
0\le x_i\le1,\qquad i=0,\dots,5.
$$

For a global CE1/reduced-CE2 replacement, this additionally means preserving

$$
0\le x_i\le1,\qquad 0<s<t<1,
$$

the active $C$-interval assumptions, and the chosen set of supercritical rows.

The final proof must show that the pointwise threshold bounds give an upper
bound for the shared vertex inside-area sum

$$
\sum_{i=0}^5 f(a_i,b_i)
$$

over the original configurations in the relevant domain.  The target after
relaxation is

$$
\sum_{i=0}^5 f(a_i,b_i)<5
$$

whenever at least two rows are supercritical.
