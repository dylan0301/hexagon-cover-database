# CE1/CE2, $N_+=1$, Exactly One T3-Like: Simplified Rescuer Proof

Status: Proven

This proof separates the only T3-specific calculation from the common
rescuer-tail budget proved in
[`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md).
The two-gap branch uses the same short CE2 theorem as the all-Vd0 case.

## Theorem

Assume the center is CE1 or CE2, exactly one actual V role is supercritical,
exactly one V role is T3-like, no V role is Vd1 or Vd2, the original open
roles cover the hexagon skeleton, and at least one boundary edge contains a
V-gap. Then no such configuration exists.

## 1. Midpoint reduction

Normalize the unique center midpoint to $M_0$. A T3-like role cannot cover
its own midpoint, a supercritical role covers none of its three local
midpoints, and a Vd0 role cannot rescue an adjacent midpoint. After reflection,

$$
T_0\text{ is T3-like},
\qquad
M_1\in T_0,
$$

$$
T_1\text{ is uniquely supercritical},
$$

and $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 roles.

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

The O-side endpoint

$$
P_T=(1-u)V_1
$$

does not belong to the open T3-like role. The adjacent supercritical role
contains $V_1$ but misses $M_1$, so convexity excludes the O-side of $M_1$.
All remaining roles are Vd0 or nonlocal. Thus

$$
\boxed{P_T\in U_C.}
\tag{1}
$$

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

Equations (1) and (3) are exactly the hypotheses of the common rescuer-tail
theorem in `2609`.

## 3. One gap

In the one-gap branch, Theorem 4.1 of `2609` shows that the far boundary
demand on $T_5$ is at least $M$, while the adjacent supercritical role has

$$
B_1<M.
$$

The four ordinary roles then satisfy

$$
\sum_{i=2}^5(A_i+B_i)>4,
$$

contrary to nonsupercriticality. This closes both CE1 and CE2 one-gap
placements without repeating the center-hiding calculation.

## 4. Two gaps

In the two-gap branch the center is CE2. The four intervening center-free
handoffs give the common pair

$$
p=W-\alpha,
\qquad
q=R-\delta
$$

on $T_1,\ldots,T_5$. The neighboring-ray formula and common-pair domination
in
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
show that the permitted T3-like support does not exceed
$c_{\max}(p,q)$. Hence the type-aware points

$$
D_2=(1-c_{\max}(p,q))V_2,
\qquad
D_4=(1-c_{\max}(p,q))V_4
$$

belong to $U_C$. Theorem 2.1 of `2609` places one of them beyond its C exit.

The one- and two-gap cases are exhaustive. $\square$
