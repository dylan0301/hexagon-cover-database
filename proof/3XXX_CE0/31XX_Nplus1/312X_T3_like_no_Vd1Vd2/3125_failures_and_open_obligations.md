# Failures and Open Obligations for the T3-like Area Package

Status: Reference

This file records what the `312X_T3_like_no_Vd1Vd2` package does not prove,
and where naive area strategies fail.

## Completed conditional part

The global inequality in `653_CE0_one_supercritical_T3_certificate.md` is a
complete analytic proof from the stated local inputs:

1. the Vd0 square-loss bounds;
2. the full T3-like tangent-envelope conjecture.

Under those inputs, the proof shows

$$
\sum_{i=0}^5G_i>1
$$

for the CE0 case with exactly one supercritical row, one T3-like row, and all
other rows Vd0.

The proof is independent of the position of the unique supercritical row and
independent of the position of the T3-like row.  After cyclic rotation, the
supercritical row is row $0$; the T3-like row can be any of rows
$1,\dots,5$.

## Open local obligation 1: Vd0 square-loss bounds

The package uses the Vd0 square-loss bounds

$$
a+b\le1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge\max(a,b)^2.
$$

These are the same local square-loss inputs used by the conditional CE0 area
certificate in `../../32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`.
They are not proved in this folder.

## Open local obligation 2: full T3-like tangent envelope

The package assumes the local tangent-envelope conjecture from
`651_full_T3_like_tangent_envelope_conjecture.md`.

The conjecture says that every no-midpoint-restricted T3-like local triangle is
area-dominated by one of the two tangent branches

$$
(A(s),B(s),F(s)),
\qquad
(B(s),A(s),F(s)),
\qquad
0\le s\le\frac12,
$$

where

$$
A(s)=\frac{s(s^2-s+1)}{1-s^2},
\qquad
B(s)=\frac{s^2-s+1}{1+s},
\qquad
F(s)=\frac{(s^2-s+1)^2}{1-s^2}.
$$

This is not proved in this folder.  The derivation of the candidate branch is
included, but the exclusion of all other T3-like geometries remains open.

## Failure 1: no uniform local T3 loss

No proof can use a uniform positive lower bound

$$
G_{\mathrm{T3}}(a,b)\ge c>0
$$

for all T3-like rows.

Indeed, the tangent branch has

$$
A(0)=0,
\qquad
B(0)=1,
\qquad
F(0)=1.
$$

Hence the normalized outside loss

$$
G(0)=1-F(0)
$$

is zero in the limiting tangent envelope.  Genuine T3-like triangles can
approach this tangent boundary by perturbation, so the local T3-like loss has no
positive uniform lower bound.

The reflected endpoint gives the same failure near $(a,b)=(1,0)$.

## Failure 2: the strict global inequality needs admissibility

The global proof in `653_CE0_one_supercritical_T3_certificate.md` obtains

$$
\sum_iG_i\ge1+m^2,
$$

where $m$ is the minimum of the normalized cut sequence after reflection
normalization.  The strict inequality follows from $m>0$.

The proof of $m>0$ uses the necessary local admissibility inequality

$$
a^2+ab+b^2\le1.
$$

Without this admissibility input, one can form degenerate formal cut sequences
for which $m=0$ and the lower bound gives only

$$
\sum_iG_i\ge1.
$$

That is not enough for an area contradiction.

Thus any complete proof must keep the local existence/admissibility constraints
for the vertex rows.

## Failure 3: T3-like cannot be treated as a second supercritical row

The two-supercritical CE0 certificate in `../../32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`
uses two rows with $a+b>1$.  In the present package, the T3-like row is not a
replacement supercritical row.  Under the tangent-envelope conjecture, every
T3-like row is nonsupercritical:

$$
a+b\le1.
$$

The replacement for the second supercritical loss is instead the local T3-like
loss estimate

$$
G_{\mathrm{T3}}(a,b)\ge2m-4m^2
$$

when both row coordinates are at least $m$.

## Failure 4: midpoint subsets are not used here

The half-skeleton midpoint inventory expects T3-like rows to have exact local
midpoint subset $\{M_1\}$ or $\{M_5\}$.  This package deliberately does not use
that condition, because the intended area route is for T3-like triangles with no
midpoint restriction.

Consequently, this package should not be cited as a proof of any maximal
half-skeleton exact-midpoint frontier.  It is an area package for the broader
T3-like type condition $(o,n)=(2,1)$.

## Required future certificates

To turn this package into an unconditional CE0 proof component, it remains to
supply:

1. a proof or certificate of the Vd0 square-loss bounds;
2. a proof or certificate of the full T3-like tangent-envelope conjecture;
3. a check that the global case assumptions really reduce all non-T3 rows to
   Vd0 under the surrounding case strategy.

Until these are supplied, the package status remains conditional.