# Boundary Length Bounds

Status: Lemma target

This file records the local boundary-length bounds needed by the proof-tree
branches that try to close by perimeter length.

Boundary contribution is measured in the open-triangle perimeter accounting:
only positive-length relatively open intervals of $\partial H$ count.
Point-only contacts, tangencies, and equality-only closed-triangle contacts are
degenerate boundary cases.

The relevant definitions are:

- CE edge type:
  [../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md](../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md).
- V-triangle type:
  [../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
- Local row coordinates:
  [../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md](../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).
- Boundary degeneracies:
  [../../1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md](../../1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md).

## Boundary cap targets

In the local boundary accounting, the intended caps are:

| Role or local type | Hypothesis | Boundary contribution cap |
|---|---|---:|
| CE0 center role | $T_C$ is CE0 | $0$ |
| CE1/CE2 center role | after reducing to the active $C$-only boundary interval | $\frac12$ |
| Vd0 vertex role | $a+b\le1$ | $1$ |
| Vd0 vertex role | $a+b>1$ | $\frac{2}{\sqrt3}$ |
| Vd1/Vd2 vertex role | intended reduced boundary-length branch | $\frac12$ |
| T3-like vertex role | intended reduced boundary-length branch | $1$ |

These caps alone do not prove any branch obstruction. A branch proof still has
to show that the relevant boundary intervals are assigned to these local roles
and has to remove equality-only open-cover endpoint cases.

## Immediate checks

### CE0

For CE0,

$$
N_E(T_C)=0.
$$

Therefore $T_C\cap\partial H$ contains no positive-length boundary interval.
Its open-boundary contribution is $0$.

### Vd0 with $a+b\le1$

For a Vd0 row, the local row coordinates record the incoming and outgoing
boundary lengths assigned to that vertex role. Thus the assigned boundary
contribution is $a+b$. If $a+b\le1$, the contribution is at most $1$.

### Vd0 with $a+b>1$

Normalize at $V_0$ and let $A$ and $B$ be the two assigned boundary endpoints
at local edge distances $a$ and $b$. The angle between the two adjacent
boundary edges is $120^\circ$, so

$$
\lvert A-B\rvert^2=a^2+ab+b^2.
$$

If a unit equilateral triangle contains both endpoints, then its diameter is
$1$, hence

$$
a^2+ab+b^2\le1.
$$

For fixed $s=a+b$, the expression $a^2+ab+b^2$ is minimized at
$a=b=s/2$, where it equals $3s^2/4$. Hence

$$
\frac34(a+b)^2\le1,
$$

and therefore

$$
a+b\le\frac{2}{\sqrt3}.
$$

## CE1/CE2 active interval check

In the CE1/CE2 boundary-loss reductions, the center role is used only through
the active $C$-only boundary interval left after covered intervals and
point-contact degeneracies are removed.

For the normalized CE1 interval $[s,t]$ recorded in
[../21XX_C_triangle_geometry/2102_CE1_M0_e01_maximal_intervals.md](../21XX_C_triangle_geometry/2102_CE1_M0_e01_maximal_intervals.md),
the maximal interval has

$$
t-s=\rho(1-\rho),\qquad \rho=\sqrt{s^2-s+1},\qquad 0<s<1.
$$

Since $\rho\ge\sqrt3/2$, this length is less than $\frac12$.

For the normalized reduced CE2 interval pair recorded in
[../21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md](../21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md),
write

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The total length of the two $C$-boundary intervals is

$$
(u-x)+(v-y)=\frac{D(1-D)}{S}.
$$

The $O$-containment start-domain condition gives $S>1/2$. Since
$D(1-D)\le1/4$, this total length is at most $\frac12$.

## Remaining reduced-branch type caps

The Vd1/Vd2 and T3-like entries above are the local type caps needed by the
perimeter-length branches:

$$
\mathrm{Vd1/Vd2}\quad\Longrightarrow\quad \text{boundary contribution}\le\frac12,
$$

and

$$
\mathrm{T3\text{-}like}\quad\Longrightarrow\quad \text{boundary contribution}\le1.
$$

These are not consequences of the raw outside-vertex and adjacent-ray counts
alone. A future proof must state the additional reduced-branch hypotheses under
which the relevant boundary contribution is being measured, and must then
exclude endpoint-only equality cases using the open-triangle convention.
