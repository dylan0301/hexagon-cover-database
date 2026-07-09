# CE2, $N_+=1$, Vd2 Neighbor-Midpoint Rescue Obstruction

Status: Proven

This file records the global use of the Vd2 local caps from
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md).

## Statement

In the CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch, suppose the unique Vd1/Vd2
row is Vd2 and covers a neighboring midpoint.  Then the branch is impossible by
boundary length.

Equivalently, a Vd2 row cannot be the unique rescuer of the midpoint of the
unique supercritical row.

## Local midpoint reduction

Normalize the Vd2 row at $V_0$.  It is enough by reflection to treat the case
where it covers the outgoing neighboring midpoint

$$
M_1=\left(\frac12,1\right)
$$

in local coordinates.  By the corner-side normal form from
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md),
there are $t>0$, $a\ge0$, $b\ge0$, and

$$
d=\sqrt{t^2+t+1}
$$

such that the row is given by

$$
x-(t+1)y\le a,
$$

$$
ty-(t+1)x\le tb,
$$

and

$$
tx+y\le d-a-tb.
$$

The point

$$
M_0=\left(\frac12,\frac12\right)
$$

satisfies the first two inequalities automatically whenever $a,b\ge0$:

$$
\frac12-(t+1)\frac12=-\frac t2\le a,
$$

and

$$
t\frac12-(t+1)\frac12=-\frac12\le tb.
$$

For the third inequality, containment of $M_1$ gives

$$
\frac t2+1\le d-a-tb.
$$

But

$$
\frac{t+1}{2}\le \frac t2+1.
$$

Therefore

$$
\frac{t+1}{2}\le d-a-tb,
$$

which is exactly the third inequality for $M_0$.  Hence

$$
M_1\in T_0\quad\Longrightarrow\quad M_0\in T_0.
$$

By reflection,

$$
M_5\in T_0\quad\Longrightarrow\quad M_0\in T_0.
$$

Thus any Vd2 row covering a neighboring midpoint has exact local midpoint
subset among

$$
\{M_0,M_1\},\qquad \{M_0,M_5\},\qquad \{M_5,M_0,M_1\},
$$

possibly with one or both adjacent midpoints included.

## Boundary cap consequence

The Vd2 local caps in `4142` give

$$
\{M_0,M_1\}\text{ or }\{M_0,M_5\}
\quad\Longrightarrow\quad
 a+b<\frac{29-7\sqrt{13}}{12},
$$

and

$$
\{M_5,M_0,M_1\}
\quad\Longrightarrow\quad
 a+b\le \sqrt3-\frac32.
$$

Both constants are strictly below

$$
K_*:=\frac32-\frac2{\sqrt3}.
$$

Therefore every Vd2 row that covers a neighboring midpoint has boundary
contribution strictly less than $K_*$.

## Global boundary contradiction

In the 414X branch there is one CE2 center row, one unique supercritical Vd0
row, one unique Vd2 row, and four ordinary nonsupercritical Vd0 rows.

The boundary caps recorded in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
are:

$$
T_C\text{ CE1/CE2 active center contribution}\le\frac12,
$$

$$
\text{supercritical Vd0 contribution}\le\frac2{\sqrt3},
$$

and

$$
\text{ordinary nonsupercritical Vd0 contribution}\le1.
$$

Thus, if the Vd2 row contributes less than $K_*$, the total boundary length
available is strictly less than

$$
\frac12+K_*+\frac2{\sqrt3}+4
=\frac12+\left(\frac32-\frac2{\sqrt3}\right)+\frac2{\sqrt3}+4
=6.
$$

But the boundary of the side-one regular hexagon has length $6$.  Hence the
boundary cannot be covered.

This proves the Vd2 neighbor-midpoint rescue obstruction.
