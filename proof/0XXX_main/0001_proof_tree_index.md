# Proof Tree Index

Status: Reference

This is navigation only.  A branch is proved only by a numbered source whose
recorded status supports the claimed conclusion.  The exhaustive assembly is
[`0000_main_theorem.md`](0000_main_theorem.md).

## Spine

Under a hypothetical seven-triangle cover, choose role triangles

$$
T_C,T_0,\ldots,T_5.
$$

The center role is exactly one of CE0, CE1, and CE2.  Every original vertex
role is exactly one of Vd0, Vd1, Vd2, and T3-like.  Let

$$
N_+
=
\left\lvert\left\{i:A_i+B_i>1\right\}\right\rvert
$$

be the number of actual supercritical vertex V triangles.  In CE1/CE2, let $m$ be the
number of non-Vd0 roles and $q$ the number of short roles.  The common budget
package `2530` proves

$$
q=N_++m
$$

and removes every $q\ge3$ state before the finer split.

For the all-Vd0 CE1/CE2 V triangles, let $\mathrm{gr}$ be the active-gap rank.  Bare
$g$ is reserved for transfer maps.  The two V-triangle counts use the kernel

| actual V-triangle count | $\mathrm{gr}=0$ | $\mathrm{gr}=1$ | $\mathrm{gr}=2$ |
|---|---|---|---|
| $N_+=0$ | strict identity cycle | one-side endpoint chain | paired CE2 endpoint chain |
| $N_+=1$ | nine-point obstruction | one five-V-triangle chain with CE1/CE2 relaxations | paired CE2 endpoint chain |

## Canonical transfer layer

The authoritative notation is
[`201d`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md):

$$
g_c(x)=\max\{y:(1-x,y,c)\in\mathcal A\},
\qquad
\widehat g_c(x)=\min\{g_c(x),x\},
$$

$$
f^\vee(a)=1-f(1-a).
$$

Thus $\widehat g_c^\vee$ is the ordinary nonsupercritical incoming-reach
transfer.  Center intervals use $\widehat g_{c,J}^\vee$, selected affine and
threshold relaxations use superscripts, and the single free strict-
supercritical envelope is $g_c^{\rm sc}$.

At zero radial demand,

$$
g_0(x)>x\quad(0<x<1),
\qquad
\widehat g_0(x)=x.
$$

The exact contact-cell aliases are

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a).
$$

## Setup and reusable lemmas

- `1XXX`: foundations
  - `1003`: open-unit and shrunken-closed equivalence.
  - `1101`: exhaustive CE0/CE1/CE2 classification.
  - `1201`: exhaustive Vd0/Vd1/Vd2/T3-like classification and T3-like
    translation normalization.
  - `1214`: strict handoff selection preserving the actual supercritical
    pattern.
- `2XXX`: geometric lemmas
  - `2004`: exact local admissible set.
  - `2007`: exact outgoing envelope and interval fibers.
  - `2010`: free strict-supercritical envelope, denoted $g_c^{\rm sc}$ in the
    canonical notation.
  - `2011`: exact hatted outgoing map, four labels, and complement duality;
    the file retains $F_c,G_c$ as technical aliases.
  - `2016`: universal selected-$T_+$ curve and affine chord bounds.
  - `2017`: one-hit and two-threshold routing.
  - `2018`: diameter transfer and common adjacent-rescuer obstruction in the
    $g_c^{\rm sc}$ notation.
  - `2019`: residual intervals, center-assisted $g$-transfers, and boundary
    path budget.
  - `201a`: enclosure gauge and universal radical calculus.
  - `201b`: global quarter radial envelope.
  - `201c`: Vd corner radial margins.
  - `201d`: canonical and relaxed $g$-composition calculus.
  - `2107`: one-side exact endpoint loss.
  - `2108`: paired CE2 endpoint loss.
  - `2109`: signed CE1/CE2 center normal form.
  - `2110`: common application of the paired endpoint theorem to both two-gap
    cells.
  - `2500`, `2510`, `2530`: boundary, skeleton, and common short-role budgets.

## CE0 branch

- `3010`: CE0, $N_+=0$, perimeter obstruction.
- CE0, $N_+=1$:
  - all Vd0: canonical direct nine-point package `3105X`, terminal `31059`;
  - some Vd1/Vd2: `3141` boundary-length obstruction;
  - no Vd1/Vd2 and some T3-like: `3171` direct area package.
- CE0, $N_+\ge2$: `3201` square-loss area package.

The older `3100X`--`3104X` routes and their failed or optional subroutes remain
in the corpus with their recorded statuses; they are not promoted by this
index.

## CE1/CE2 branch

- $N_+=0$:
  - all Vd0: `4013`, using the three active-gap-rank chains;
  - some Vd1/Vd2: `4040`, `4041`, unchanged Strategy 1 routes;
  - T3-like and no Vd1/Vd2: `407X`, exact hatted endpoint audit with
    identity-relaxed interior V triangles.
- $N_+=1$, all Vd0:
  - `4105` gives one exact five-V-triangle $\widehat g^\vee$ interface;
  - `4106` gives the CE1 affine/threshold relaxation;
  - `4107` gives the CE2 one-threshold-slot relaxation;
  - the zero-gap cell remains the Strategy 4 nine-point obstruction.
- $N_+=1$, special roles:
  - `4110`, `4111`, `4123`: unchanged Strategy 1 routes;
  - `413X`: exactly one T3-like, with the common
    $1-g_c^{\rm sc}$--identity--$g_c^{\rm sc}$ chain;
  - `414X`: exactly one Vd1/Vd2, with the same rescuer chain, the quarter
    terminal transfer, the Vd-specific terminal margin, and axis replacement;
    `4149` and `414a` remain Strategy 1.
- $N_+\ge2$: `4200`, unchanged Strategy 1 skeleton route.

## Failed-idea warnings

The following remain nondependencies:

- `908X`: counterexample to full-skeleton noncoverage;
- `962X`: failed four-point route;
- `963X`: failed five-point route;
- `964X`: failed CE1/CE2 area route;
- `3172`: false global T3-like coordinatewise tangent envelope.
