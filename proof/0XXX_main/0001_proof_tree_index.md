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

For the detailed tables, write

$$
d=
\left\lvert
\left\lbrace i:T_i\text{ is Vd1 or Vd2}\right\rbrace
\right\rvert,
\qquad
t=
\left\lvert
\left\lbrace i:T_i\text{ is T3-like}\right\rbrace
\right\rvert,
$$

so $N_{\rm sp}=d+t$. Let $N_{\rm gap}\in\{0,1,2\}$ be the number of
positive C-triangle boundary traces containing a boundary gap. Singleton
missed sets count as gaps because the covering roles are open. Boundary
locality gives the fundamental outer split

$$
N_{\rm gap}=0
\quad\Longleftrightarrow\quad
U_0,\ldots,U_5\text{ cover }\partial H.
$$

The zero-gap tree is therefore center-independent:

| $N_+$ | $(d,t)$ | Terminal route | Method | Recorded status |
|---:|---|---|---:|---|
| $0$ | any | V-only strict boundary overlap `2500` | 1 | Proven |
| $1$ | $d\ge1$ | V-only boundary-length deficit `2500` | 1 | Proven |
| $1$ | $d=0$, $t\ge1$ | strict handoffs and T3 cyclic area loss `3174` | 2 | Proven |
| $1$ | $(0,0)$ | center-independent nine-point obstruction `31058` | 3 | Proven |
| at least $2$ | any | at-least-two-ascent cyclic area loss `3208` | 2 | Proven |

No row of this table uses the local reach certificates as a separate strategy. For nonzero gap count, the common
budget package `2530` directly closes every state with
$N_++N_{\rm sp}\ge3$. The detailed tree below nevertheless retains the
numbered branch wrappers that apply this budget, so that the Vd1/Vd2 and
T3-like combinatorial cases remain visible.

## Local reach-certificate layer

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

Every CE0 cover has $N_{\rm gap}=0$ and is therefore an instance of the
center-independent zero-gap matrix above. The historical CE0 package names
record the same specializations:

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

Only $N_{\rm gap}\ge1$ remains here; zero gap was dispatched before the
center split.  The rows retain the detailed special-type counts underlying the
shorter condition $N_++N_{\rm sp}\ge3$.  Strategy 1 is trace length,
Strategy 2 is area loss, and Strategy 3 is finite enclosure.  The exact local
reach maps below are subordinate certificates for Strategy 3.

| $N_{\rm gap}$ | $N_+$ | $(d,t)$ | Center class | Terminal route | Strategy | Recorded status |
|---:|---:|---|---|---|---|---|
| at least $1$ | $0$ | $(0,0)$ | CE1/CE2 | finite-enclosure package `4013_new` | 3 | Proven |
| at least $1$ | $0$ | $(0,1)$ or $(0,2)$ | CE1/CE2 | finite-enclosure package `4070_new` | 3 | Proven |
| at least $1$ | $0$ | $(0,t)$, $t\ge3$ | CE1/CE2 | direct skeleton budget `2530`, used in `4072` | 1 | Proven |
| at least $1$ | $0$ | $d\ge1$, any $t$ | CE1/CE2 | CE1 `4040`; CE2 `4041` | 1 | Proven |
| at least $1$ | $1$ | $(0,0)$ | CE1/CE2 | finite-enclosure package `4101_new` | 3 | Proven |
| at least $1$ | $1$ | $(0,1)$ | CE1/CE2 | finite-enclosure package `4130_new` | 3 | Proven |
| at least $1$ | $1$ | $(0,t)$, $t\ge2$ | CE1/CE2 | skeleton obstruction `4123` | 1 | Proven |
| at least $1$ | $1$ | $d\ge1$, any $t$ | CE1 | boundary-length obstruction `4110` | 1 | Proven |
| at least $1$ | $1$ | $d\ge2$, any $t$ | CE2 | boundary-length obstruction `4111` | 1 | Proven |
| at least $1$ | $1$ | $d=1$, $t\ge1$ | CE2 | mixed positive-support obstruction `414a` | 1 | Proven |
| at least $1$ | $1$ | $(1,0)$ | CE2 | finite-enclosure package `4140_new` below | 1 and 3 | Proven |
| at least $1$ | at least $2$ | any | CE1/CE2 | skeleton-length route `4200` | 1 | Proven |

### Finite-enclosure reach certificates

The nonzero-gap Strategy 3 rows use the following exact reach calculations to certify that the finite residual hull cannot fit in a unit C triangle. Here $N_{\rm gap}\ge1$ means one gap in CE1 and one or two in CE2.

| $N_{\rm gap}$ | $N_+$ | $(d,t)$ | Center | Chain or terminal inequality | Source | Recorded status |
|---:|---:|---|---|---|---|---|
| $1$ | $0$ | $(0,0)$ | CE1/CE2 | two exact endpoint outputs with three identity-relaxed interior roles | `4013`, `2107` | Proven |
| $1$ | $1$ | $(0,0)$ | CE1 | exact five-role $\Phi_c$ chain with affine and threshold relaxations | `4105`, `4106` | Proven |
| $1$ | $1$ | $(0,0)$ | CE2 | the same five-role chain with the CE2 threshold alternative | `4105`, `4107` | Proven |
| $2$ | $0$ or $1$ | $(0,0)$ | CE2 | paired exact endpoints with three identity-relaxed interior roles | `2110`, `2108` | Proven |
| at least $1$ | $0$ | $(0,1)$ or $(0,2)$ | CE1/CE2 | two exact T3-like endpoint outputs and the middle $\mathrm I^3$ chain | `407X` | Proven |
| at least $1$ | $1$ | $(0,1)$ | CE1/CE2 | $1-M_c^{\rm sup}$--$\mathrm I^3$--$M_c^{\rm sup}$ adjacent-rescuer chain | `4131`, `4132`, `2018` | Proven |
| at least $1$ | $1$ | $(1,0)$ | CE2 | detailed placement audit, including Method 1 complements and the replacement gap-rank router | `4148`, `414b` | Proven |

### Detailed `414X` placement audit

The standing branch has $N_{\rm gap}\in\{1,2\}$; its zero-gap counterpart is
already Method 1. First, `414a` closes the entry branch having an additional
positive-support V role. This includes every mixed
exactly-one-Vd1/Vd2--T3-like state. On the complement, normalize the unique
C-triangle midpoint to $M_0$, let $T_\sigma$ be the unique supercritical role,
and let $T_\tau$ be the unique Vd1/Vd2 role. They are distinct, and every
other V role is nonsupercritical Vd0.

| Entry reduction | Terminal route | Method | Recorded status |
|---|---|---|---|
| an additional positive-support V role | direct $N_++N_{\rm sp}$ skeleton budget `414a` | 1 | Proven |

The no-additional-support complement has exactly the following six placement
rows.  Reflections of the displayed index sets are included.

| Placement | Forced refinement | Terminal route | Strategy | Recorded status |
|---|---|---|---|---|
| $\sigma=0$, $\tau\in\{1,5\}$ | the Vd1/Vd2 role is adjacent to the supercritical role | exact residual and radial obstruction `4144` | 3 | Proven |
| $\sigma=0$, $\tau\in\{2,3,4\}$ | the Vd1/Vd2 role is nonadjacent to the supercritical role | Vd-specific radial separation `4146` | 3 | Proven |
| $\tau=0$, $T_\tau$ Vd1 | midpoint forcing gives $\sigma\in\{1,5\}$ and $T_\tau$ rescues $M_\sigma$ | adjacent-rescuer finite-enclosure certificate `4143`, `2018` | 3 | Proven |
| $\tau=0$, $T_\tau$ Vd2 | midpoint forcing gives $\sigma\in\{1,5\}$ and $T_\tau$ rescues $M_\sigma$ | neighboring-midpoint perimeter obstruction `4149` | 1 | Proven |
| $\sigma\ne0$, $\tau\ne0$, $T_\tau$ Vd1 | midpoint forcing makes $\sigma$ and $\tau$ adjacent | two-chart replacement `4147`; recompute $N'_{\rm gap}$, then Method 1 if zero and nonzero-gap `4013` otherwise | 1 or 2 | Proven |
| $\sigma\ne0$, $\tau\ne0$, $T_\tau$ Vd2 | midpoint forcing makes $\sigma$ and $\tau$ adjacent | neighboring-midpoint perimeter obstruction `4149` | 1 | Proven |

The proved assembly is `4148`; the independent exhaustive post-repair audit
is `414b`.

## Active finite-enclosure package pointers

- `2608`: common residual-hull finite-enclosure principle.
- `4013_new`: nonzero-gap, $N_+=0$, all-Vd0 wrapper.
- `4070_new`: nonzero-gap, $N_+=0$, T3-like wrapper.
- `4101_new`: nonzero-gap, $N_+=1$, all-Vd0 wrapper.
- `4130_new`: nonzero-gap, $N_+=1$, exactly-one-T3-like wrapper.
- `4140_new`: nonzero-gap, $N_+=1$, exactly-one-Vd1/Vd2 wrapper.

The original numbered packages remain exact local certificates and provenance
sources.  They no longer own a fourth strategy.

## Failed-idea warnings

The following remain nondependencies:

- `908X`: counterexample to full-skeleton noncoverage;
- `962X`: failed four-point route;
- `963X`: failed five-point route;
- `964X`: failed CE1/CE2 area route;
- `3172`: false global T3-like coordinatewise tangent envelope.
