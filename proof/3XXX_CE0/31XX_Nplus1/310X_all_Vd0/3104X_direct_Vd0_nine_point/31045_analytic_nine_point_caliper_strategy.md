# Analytic Nine-Point Caliper Replacement Strategy

Status: Strategy

## 1. Scope And Status

This note proposes an interval-free alternative for the terminal enclosure step
used by the direct all-Vd0 nine-point route.  It does not replace the proved
terminal theorem in
[`31034_witness_enclosure_inequality.md`](../3103X_residual_core/31034_witness_enclosure_inequality.md),
and it does not change any proof status.

The present proof first forces six radial points and three asymmetric points
into the open center role.  It then replaces the radial hexagon by its incircle
and proves the final enclosure inequality by a Minkowski cap argument.  The
only interval-arithmetic dependency is the pair of mixed cap overlaps in
Section 7 of `31034`.

The proposed alternative is to retain the finite radial hexagon and apply the
exact finite caliper theorem from
[`20095_exact_caliper_certificate.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md)
directly.  This may turn the mixed disk--point inequalities into finitely many
ordinary algebraic edge inequalities.

## 2. Forced Finite Witness Set

Use the strict parameter domain

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
\rho=a^2+ab+b^2<1.
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
\qquad
r=1-c_*.
$$

The direct radial-forcing theorem
[`31041_direct_radial_forcing.md`](31041_direct_radial_forcing.md) gives

$$
D_i=rV_i\in T_C
\qquad(i=0,\ldots,5).
$$

The direct asymmetric-forcing theorem
[`31042_direct_asymmetric_witness_forcing.md`](31042_direct_asymmetric_witness_forcing.md) gives

$$
Q_-,Q_0,Q_+\in T_C.
$$

Retain the junction-tangent points from Section 3 of `31034`.  Thus

$$
A\in(Q_0,Q_-),
\qquad
B=Q_0,
\qquad
C\in(Q_0,Q_+),
$$

where the two open intervals are line segments.  Since the center role is
convex,

$$
A,B,C\in T_C.
$$

Define the finite set

$$
\widehat K_9(a,b)
=
\left\{D_0,\ldots,D_5,A,B,C\right\}.
$$

An analytic proof of

$$
\boxed{
\Lambda\left(\widehat K_9(a,b)\right)\ge1
}
\tag{1}
$$

on the full strict domain would replace the terminal use of the
outward-rounded mixed-overlap certificate in the direct nine-point route.
Indeed, `31043` already supplies the compact containment in the open center
role, while compactness inside an open unit equilateral triangle would imply a
closed enclosing triangle of side strictly less than one.

## 3. Why Retaining The Hexagon May Help

Let

$$
h=\frac{\sqrt3}{2},
\qquad
\mathcal H_r=\mathrm{conv}\left\{D_0,\ldots,D_5\right\}.
$$

The current proof uses only the incircle

$$
\mathbb D(0,hr)\subseteq\mathcal H_r.
$$

This replacement is safe but discards directional support.  For every unit
normal $n$,

$$
h_{\mathcal H_r}(n)
=
r\max_{0\le i<6}\langle V_i,n\rangle
\ge hr.
$$

The lower bound is the incircle support, but the exact hexagon support is
strictly larger away from the six side normals.  Those extra directional
margins are precisely what the disk-based mixed overlaps cannot use.

The finite caliper theorem says that a finite set is contained in a closed
unit equilateral triangle if and only if one of the finitely many pair-normal
calipers has support sum at most $h$ after normalization.  Therefore (1) can
be attacked without an orientation variable and without interval subdivision.
A convex-hull order proof would reduce the candidate normals further to hull
edges; otherwise all point-pair normals remain a finite exact list.

## 4. Two Line-Edge Calipers Already Have Analytic Input

The analytic adjacent-overlap proof in Section 6 of `31034` gives

$$
\frac{\mathrm{cross}(A,B)}{\lVert B-A\rVert}
\ge h(2c_*-1)
$$

and

$$
\frac{\mathrm{cross}(B,C)}{\lVert C-B\rVert}
\ge h(2c_*-1).
$$

At either corresponding line-edge caliper, the other two rotated support
directions receive at least $hr$ each from the retained radial hexagon.
Consequently the prospective support lower bound is

$$
2hr+h(2c_*-1)
=
h,
$$

because $r=1-c_*$.  Thus the two asymmetric line edges should require only an
exact support-label audit, not a new global inequality.

This is the main structural advantage over the disk proof: the analytic
adjacent estimate already reaches the exact amount needed once the two radial
supports are kept instead of encoded as mixed cap overlaps.

## 5. Candidate Connector-Edge Inequality

Use the centered basis

$$
E_0=V_5-V_4,
\qquad
E_1=V_3-V_4.
$$

In this basis,

$$
D_0=(r,0),
\qquad
D_1=(r,r),
\qquad
D_2=(0,r).
$$

Use the coordinates already established in `31034`:

$$
A=(-X,-Y),
\qquad
C=(-P,-Q),
$$

with

$$
0<X,Y,P,Q<1,
\qquad
X>\frac12,
\qquad
Q>\frac12.
$$

For the candidate hull edge $D_2A$, suppose the three rotated support labels
are respectively the edge tie $D_2/A$, the point $C$, and the radial point
$D_1$.  Direct determinant expansion gives the normalized caliper support

$$
\mathcal L_{2A}
=
X(r+P)+(r+Y)(r+Q-P).
\tag{2}
$$

The edge length is

$$
\lVert A-D_2\rVert
=
\sqrt{X^2+(r+Y)^2-X(r+Y)}.
\tag{3}
$$

Thus this connector caliper reduces to the explicit inequality

$$
\boxed{
X(r+P)+(r+Y)(r+Q-P)
\ge
\sqrt{X^2+(r+Y)^2-X(r+Y)}
}.
\tag{4}
$$

Reflection gives the corresponding $CD_0$ target.  Before squaring (4), the
left side must be proved nonnegative.  The squared difference is then an
ordinary algebraic expression in $a,b,c_*$ and

$$
D=\sqrt{4\rho-3}.
$$

The tangent construction makes $X,Y,P,Q$ rational functions of $a,b,D$.
Hence the remaining radical and radial-envelope structure is explicit rather
than hidden in an interval support calculation.

Equation (4) is a strategy target, not a proved inequality in this note.  Its
support labels and its validity on the full parameter domain both require an
exact proof.

## 6. Analytic Program

A proof attempt should use the same exact two radial-envelope cells as `31034`.

1. On the explicit radial cell, substitute the closed formula for $c_*$.
2. On the quartic cell, retain

   $$
   c_*^4-c_*^2+mc_*-m^2=0
   $$

   together with the selected-root and selector inequalities.
3. Use

   $$
   U=a+b-1,
   \qquad
   z=a-b,
   \qquad
   D^2=z^2+6U+3U^2,
   $$

   so that

   $$
   0<U<\frac16,
   \qquad
   0<D<1.
   $$
4. Clear only denominators whose positivity has been proved.
5. Reduce powers of $D$ with its quadratic relation and powers of $c_*$ with
   the selected radial equation.
6. Prove the resulting signs by factorization, monotonicity, convexity, or
   endpoint comparison.  No interval boxes are intended in this route.

The six radial witnesses also allow some flexibility.  Since $O,D_i\in T_C$
and $T_C$ is convex, every point

$$
\widetilde D_i=\widetilde r V_i,
\qquad
0\le\widetilde r\le r,
$$

is forced into the center role.  A simpler parameter-dependent
$\widetilde r(a,b)$ may therefore be used if it improves factorization.
However, the asymmetric limits are sharp, so a uniform loss from $r$ is
unlikely to close the full domain.

## 7. Required Audit Before Any Status Change

The following obligations remain.

1. Prove the exact coordinate identification of the tangent points used here
   with the forced asymmetric segments from `31042` and `31034`.
2. Determine the convex-hull order of
   $D_0,\ldots,D_5,A,B,C$, or retain and prune the complete finite pair list.
3. Prove every support label used in the line-edge and connector-edge
   reductions.
4. Prove (4), its reflection, and the remaining radial-edge calipers on both
   radial-envelope cells.
5. Handle the selector face, reflection face, and the sharp limits
   $(a,b)\to(0,1)$ and $(1,0)$ analytically.
6. Only after these steps are complete, rewrite `31034`, the manuscript, and
   the source ledger to remove the interval certificate.

Until those obligations are discharged, the existing outward-rounded
certificate remains the valid proof dependency and this note remains
`Status: Strategy`.
