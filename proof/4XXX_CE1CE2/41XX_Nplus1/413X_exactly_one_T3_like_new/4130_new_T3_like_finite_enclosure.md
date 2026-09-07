# CE1/CE2, $N_+=1$, Exactly One T3-Like: Simplified Rescuer Proof

Status: Proven

This proof separates the only T3-specific calculation from the common
fixed four-point interface proved in
[`2612`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).
Both gap ranks use the same fixed four-point enclosure ending.

## Theorem

Assume the center is CE1 or CE2, exactly one actual V role is supercritical,
exactly one V role is T3-like, no V role is Vd1 or Vd2, the original open
roles cover the hexagon skeleton, and at least one boundary edge contains a
V-gap. Then no such configuration exists.

## 1. Midpoint reduction

Normalize the C midpoint to $M_0$. If the supercritical role is $T_0$,
apply the center-aligned theorem in
[`2612`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).
Otherwise the common midpoint-supplier lemma
[`2613`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md)
forces the T3-like role to be $T_0$ and, after reflection, the supercritical
role to be $T_1$, with $M_1\in U_0$. The remaining four roles are
nonsupercritical Vd0. This is the only placement-specific reduction.

Use the translated T3-like chart at $V_0$. Let

$$
T_0\cap e_{5,0}=[0,a]
$$

and write its supported interval on $r_1$, measured from $V_1$ toward $O$,
as

$$
[c,u],
\qquad
c\le\frac12\le u.
$$

By the radial-frontier corollary in `2612`, the supported O-side
endpoint is missed by all V roles: its own supercritical role stops before
$M_1$ and all other possible contributions are absent. Thus

$$\boxed{P_T=(1-u)V_1\in U_C.}\tag{1}$$

Put

$$
\varepsilon=1-u.
$$

## 2. The only T3-specific inequality

The translated normal form has parameters

$$
1\le D\le\frac2{\sqrt3},
\qquad
E_0=\sqrt{4-3D^2},
\qquad
R_0=\frac{D+E_0}{2},
$$

and

$$
c=\frac{D(1+a)-1}{R_0},
\qquad
u=1-\frac{R_0}{D}+a.
$$

Put

$$
x=\frac{aD}{R_0},
\qquad
\theta=\frac{D-1}{R_0}.
$$

Then

$$
c=x+\theta,
\qquad
0\le\theta\le2-\sqrt3,
$$

and the midpoint condition is equivalent to

$$
\frac{1-4\theta+\theta^2}{2(1-2\theta)}
\le x\le\frac12-\theta.
\tag{2}
$$

Let

$$
M=M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2.
$$

For $0\le z\le1/2$, put

$$
s(z)=\frac{z(2-z)}{1+z}.
$$

The defining relation for the strict-supercritical envelope is

$$
s(1-M)=c.
$$

Since $s$ is increasing, it is enough to prove $s(x)\le x+\theta$. After
multiplication by $1+x$, this becomes

$$
Q_\theta(x)=2x^2+(\theta-1)x+\theta\ge0.
$$

For $0\le\theta\le1/5$, the interval (2) lies to the right of the vertex of
$Q_\theta$, and substitution of its left endpoint gives

$$
Q_\theta(x)
\ge
\frac{\theta(1-5\theta+11\theta^2-\theta^3)}
{2(1-2\theta)^2}
\ge0.
$$

For $1/5\le\theta\le2-\sqrt3$, the vertex lies in the interval and

$$
Q_\theta(x)
\ge
\frac{10\theta-1-\theta^2}{8}>0.
$$

Thus $x\le1-M$. Since $D\ge R_0$,

$$
a\le x\le1-M.
$$

Moreover,

$$
a+\varepsilon=\frac{R_0}{D}\le1,
\qquad
\frac{a}{a+\varepsilon}
=
\frac{aD}{R_0}
=x\le1-M.
\tag{3}
$$

Equations (1) and (3) are exactly the hypotheses of the common four-point
interface in `2612`.

## 3. Apply the common fixed-witness interface

The local chart has verified $A_0+\varepsilon\le1$ and
$A_0/(A_0+\varepsilon)\le1-M$. The supported endpoint is the total radial
frontier from [2612](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md),
Corollary 2.2a. Skeleton coverage from $V_1$ to the start $c$ of the
rescuer's interval gives $C_1\ge c$: the center misses $M_1$ and the
other V roles have no positive trace on this ray. Corollary 6.2 of `2612`
therefore supplies the same four actual points and contradiction for either
gap rank. No repeated boundary-tail proof and no disk are needed. $\square$
