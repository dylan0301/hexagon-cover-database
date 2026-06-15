# Threshold Relaxation Failure

Status: Failed

This file archives the threshold-relaxation and global-replacement route that
was formerly attached to the CE0 area-conjecture package and the
CE1/reduced-CE2 seven-point extension.

The successful CE0 conditional certificate does not use this route.  See
[`../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`](../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md).

## Supercritical rows

A vertex row is called supercritical here when

$$
a_i+b_i>1.
$$

The failed route focused on configurations where one or more rows are
supercritical after the relevant perimeter cut data has been fixed.

By monotonicity of $f(a,b)$, increasing either coordinate can only decrease the
local maximum inside area.  Therefore the worst area case for a supercritical
row was expected to occur near the threshold

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

Rows with

$$
1<a_i+b_i<1+\varepsilon
$$

are not covered by this fixed-$\varepsilon$ inequality.  They require a boundary
or limiting regime that is not supplied here.

## CE0 formula

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

This route is not needed for the CE0 conditional certificate once the local
square-loss bounds are supplied.

## CE1/reduced-CE2 formula

In the failed CE1/reduced-CE2 seven-point area route, the rows were

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

The same pointwise threshold bound was intended for any row satisfying
$a_i+b_i\ge1+\varepsilon$:

$$
f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
$$

This application should not be used without a new certified argument.

## Global replacement formulation

An older formulation of the relaxation was to replace every supercritical row
by a row on the near-threshold line

$$
a_i+b_i=1+\varepsilon.
$$

This is not a certified replacement.  Changing one perimeter cut point affects
adjacent rows, so a simultaneous replacement of all supercritical rows may fail
to define a valid global cut-point configuration or may change neighboring rows
in an uncontrolled way.

The global replacement formulation would need to prove:

1. keep each designated supercritical row supercritical;
2. push each such row down to $a_i+b_i=1+\varepsilon$;
3. within those constraints, maximize the neighboring subcritical $b$- or
   $a$-coordinates that increase the possible inside-area contribution.

This file does not claim that the global replacement formulation is valid.

## Failure reason

This route is archived because it does not provide a complete proof of the area
target.  The missing pieces include the boundary regime
$1<a_i+b_i<1+\varepsilon$, the global replacement map, and the CE1/reduced-CE2
validity checks.
