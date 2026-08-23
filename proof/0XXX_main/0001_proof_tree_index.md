# Proof Tree Index

Status: Reference

This is navigation only.  A branch is proved only by a numbered source whose
recorded status supports the claimed conclusion.  The exhaustive assembly is
[`0000_main_theorem.md`](0000_main_theorem.md).

## Spine

Under a hypothetical seven-open-triangle cover, write the original roles as

$$
U_C,U_0,\ldots,U_5,
$$

and put $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. The closed C triangle
$T_C$ is exactly one of CE0, CE1, and CE2. Raw $(o,n)=(3,0)$ vertex roles are
first replaced by the exact-trace translates in `1201`, which leave all actual
reaches unchanged. Every resulting closed V triangle $T_i$ is exactly one of
Vd0, Vd1, Vd2, and T3-like. Let

$$
N_+
=
\left\lvert\left\{i:A_i+B_i>1\right\}\right\rvert
$$

be the number of actual supercritical V triangles, and let

$$
N_{\rm sp}
=
\left\lvert\left\{i:T_i\text{ is Vd1, Vd2, or T3-like}\right\}\right\rvert.
$$

The common budget package `2530` removes every state with
$N_++N_{\rm sp}\ge3$ before the finer split.

For the all-Vd0 CE1/CE2 branches, let $N_{\rm gap}\in\{0,1,2\}$ be the
number of positive C-triangle boundary traces containing a boundary gap.
Singleton missed sets count as boundary gaps because the covering roles are
open. The two V-triangle counts use the kernel

| actual V-triangle count | $N_{\rm gap}=0$ | $N_{\rm gap}=1$ | $N_{\rm gap}=2$ |
|---|---|---|---|
| $N_+=0$ | strict identity cycle | one-side endpoint chain | paired CE2 endpoint chain |
| $N_+=1$ | nine-point obstruction | one five-V-triangle chain with CE1/CE2 relaxations | paired CE2 endpoint chain |

## Canonical transfer layer

The authoritative notation is
[`201d`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md):

$$
M_c(a)=\max\{b:(a,b,c)\in\mathcal A\}.
$$

For a nonsupercritical actual V triangle with incoming lower bound $a$ and
radial lower bound $c$, the outgoing estimate is used branchwise:

$$
B\le
\begin{cases}
1-a,&c\le1/2,\\
M_c(a),&c>1/2.
\end{cases}
$$

The high-radial branch is automatically nonsupercritical because the demanded
radial segment contains the midpoint.  Hence $M_c(1-x)\le x$ for $c\ge1/2$,
and the map $x\mapsto M_{1/2}(1-x)$ is $\mathrm I$.  On a center-free edge the corresponding incoming
transfer is the identity in the low-radial branch and $\Phi_c$ in the
high-radial branch. Center intervals use the same two cases after applying the
residual operator. Selected affine and threshold relaxations are decorated
versions of the high-radial raw map. The single free strict-supercritical
envelope is $M_c^{\rm sup}$.

At zero radial demand the raw map satisfies

$$
M_0(1-x)>x\qquad(0<x<1),
$$

so it is not used for a nonsupercritical low-radial handoff; that branch uses
the direct inequality $B\le1-A$.

The exact nonsupercritical cap and propagation map are

$$
\overline M_c(a)=
\begin{cases}
1-a,&c\le1/2,\\
M_c(a),&c>1/2,
\end{cases}
\qquad
\Phi_c(a)=1-\overline M_c(a).
$$

## Setup and reusable lemmas

- `1XXX`: foundations
  - `1003`: open-unit and shrunken-closed equivalence.
  - `1101`: exhaustive CE0/CE1/CE2 classification.
  - `1201`: exhaustive normalized Vd0/Vd1/Vd2/T3-like classification,
    exact-trace normalization of raw $(3,0)$ Vd0 roles, and T3-like
    closed-trace normalization.
  - `1214`: strict handoff selection preserving the actual supercritical
    pattern.
- `2XXX`: geometric lemmas
  - `2004`: exact local admissible set.
  - `2007`: exact outgoing envelope and interval fibers.
  - `2010`: free strict-supercritical envelope, denoted $M_c^{\rm sup}$ in the
    canonical notation.
  - `2011`: exact branchwise nonsupercritical output, the high-radial four
    labels, and complement duality; $\overline M_c,\Phi_c$ are the canonical
    cap and propagation maps.
  - `2016`: universal selected-$Q_+$ curve and affine chord bounds.
  - `2017`: one-hit and two-threshold routing.
  - `2018`: diameter transfer and common adjacent-rescuer obstruction in the
    $M_c^{\rm sup}$ notation.
  - `2019`: residual intervals, center-assisted transfers, and boundary
    path budget.
  - `201a`: enclosure gauge and universal radical calculus.
  - `201b`: global quarter radial envelope.
  - `201c`: Vd corner radial margins.
  - `201d`: canonical raw, capped, propagation, and relaxed-map calculus.
  - `2100`: CE1/CE2 exactly-one-midpoint theorem, with $O$ in the interior.
  - `2107`: one-side exact endpoint loss.
  - `2108`: paired CE2 endpoint loss.
  - `2109`: signed CE1/CE2 center normal form.
  - `2110`: common application of the paired endpoint theorem to both two-gap
    cells.
  - `2500`, `2510`, `2530`: boundary, skeleton, and direct
    $N_++N_{\rm sp}$ budgets.

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
  - all Vd0: `4013`, using the three boundary-gap-count chains;
  - some Vd1/Vd2: `4040`, `4041`, unchanged Strategy 1 routes;
  - T3-like and no Vd1/Vd2: `407X`, exact branchwise endpoint audit with
    identity-relaxed interior V triangles; a low-radial endpoint is the direct
    $\mathrm{Lin}$ case.
- $N_+=1$, all Vd0:
  - `4105` gives one exact five-V-triangle high-radial $\Phi_c$ interface;
  - `4106` gives the CE1 affine/threshold relaxation;
  - `4107` gives the CE2 one-threshold-slot relaxation;
  - the zero-gap cell remains the Strategy 4 nine-point obstruction.
- $N_+=1$, special roles:
  - `4110`, `4111`, `4123`: unchanged Strategy 1 routes;
  - `413X`: exactly one T3-like, with the common
    $1-M_c^{\rm sup}$--identity--$M_c^{\rm sup}$ chain;
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
