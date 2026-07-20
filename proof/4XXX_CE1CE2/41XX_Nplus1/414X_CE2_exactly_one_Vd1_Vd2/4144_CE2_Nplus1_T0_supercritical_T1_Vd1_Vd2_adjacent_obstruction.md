# CE2, $N_+=1$, $T_0$ Supercritical And Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent remaining placement in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) branch:

$$
T_C\text{ is CE2},\qquad T_0\text{ is the unique supercritical row},
\qquad T_1\text{ is the unique Vd1/Vd2 row}.
$$

The reflected placement with $T_5$ Vd1/Vd2 is identical.

The proof uses the Vd1/Vd2 normal form from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md),
the boundary caps from
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md),
the exact admissible-set radial envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md),
the reusable half-edge rational envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md),
and the CE2 interval-pair model from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md).

The radial-envelope step below is an application of the proved theorem in
`2012`; the branch-local calculation is retained to display the exact
Cell-$T$ selector and strictness used in this placement.

## Statement

Assume a reduced 414X cover candidate satisfies

$$
T_C\text{ is CE2},\qquad T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique supercritical row},\qquad T_1\text{ is the unique Vd1/Vd2 row},
$$

and

$$
T_2,T_3,T_4,T_5
$$

are Vd0 rows satisfying

$$
a_i+b_i\le1,\qquad i=2,3,4,5.
$$

Then the seven role triangles cannot cover the hexagon perimeter together with
the two diagonal targets $r_1$ and $r_2$.  In particular, the adjacent
$T_0$-supercritical, $T_1$-Vd1/Vd2 placement is impossible in the 414X branch.

## CE2 variables and diagonal lengths

Write the normalized CE2 boundary intervals as

$$
T_C\cap e_{5,0}=[x,u],\qquad T_C\cap e_{0,1}=[y,v].
$$

Set

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The CE2 parameterization gives

$$
0<x<u<1,\qquad 0<y<v<1,
$$

$$
(u+v)S-xy=D,
$$

$$
uS\ge x,\qquad vS\ge y,
$$

and

$$
uS<x+\frac y2,\qquad vS<y+\frac x2.
$$

Set

$$
E:=vS-y.
$$

Substitution into the CE2 half-plane model gives the center-triangle lengths on
$r_1$ and $r_2$, measured from $O$ toward the corresponding vertex:

$$
d_1^C=\frac{E}{x},\qquad d_2^C=\frac{E}{S}.
$$

Thus the uncovered vertex-side demands are

$$
q_1=1-d_1^C,\qquad q_2=1-d_2^C.
$$

## Boundary demands

Let $(a_0,b_0)$ be the boundary coordinates of $T_0$.  Since $T_0$ is
supercritical,

$$
a_0+b_0>1.
$$

The adjacent endpoint distance condition gives

$$
a_0^2+a_0b_0+b_0^2\le1.
$$

On $e_{0,1}$, coverage by $T_0$, $T_C$, and $T_1$ forces

$$
a_1\ge A,
$$

where

$$
A=
\begin{cases}
1-b_0,& b_0<y,\\
\max(0,1-\max(b_0,v)),& b_0\ge y.
\end{cases}
$$

On $e_{5,0}$, coverage by $T_0$, $T_C$, and $T_5$ forces

$$
b_5\ge H,
$$

where

$$
H=
\begin{cases}
1-a_0,& a_0<x,\\
\max(0,1-\max(a_0,u)),& a_0\ge x.
\end{cases}
$$

Because $u<1$ and $T_0$ is strictly supercritical, $H>0$ in a genuine
candidate.

For ordinary nonsupercritical Vd0 rows, $a_i+b_i\le1$.  Together with
$b_i+a_{i+1}\ge1$, this propagates the $b_5$ lower bound backward:

$$
b_5\ge H\Longrightarrow b_4\ge H\Longrightarrow b_3\ge H
\Longrightarrow b_2\ge H\Longrightarrow b_1\ge H.
$$

Thus

$$
\boxed{a_1\ge A,\qquad b_1\ge H.}
$$

## Vd1/Vd2 boundary cap

The boundary-length theorem, equivalently the last conclusion of the normal
form in `2014`, gives directly

$$
\boxed{a_1+b_1<\frac12.}
$$

Combining with $a_1\ge A$ and $b_1\ge H$ gives

$$
\boxed{A+H<\frac12.}
$$

## Local radial-envelope bound for $T_2$

Let

$$
p=\frac12+A,\qquad h=H.
$$

Then $p\ge1/2$, $h\ge0$, $p+h<1$, and $p\ge h$.  The half-edge rational
envelope theorem in `2012` therefore gives directly

$$
\boxed{c_{\max}(p,h)\le1-\frac h3.}
$$

For completeness, the following branch-local verification records the selected
component.  Set $c_0=1-h/3$ and work in the ordered half $h\le p$ of the
admissible-set formulas.

In the $q<0$ branch, the boundary value is the first positive root of

$$
P(c)=c^4-c^2+hc-h^2.
$$

If $q<0$, then $h<3/8$; otherwise $p\ge1/2$ gives

$$
q=s^4-s^2+ph\ge\left(h+\frac12\right)^4-\left(h+\frac12\right)^2+\frac h2\ge0.
$$

For $h\ge3/8$ and $p\ge1/2$, the derivative
$4s^3-2s+h$ is positive, so the first inequality follows by monotonicity in
$p$. The last expression is increasing in $h>0$ and equals $33/4096$ at
$h=3/8$.

At $c_0$,

$$
P(c_0)=\frac{h}{81}\left(h^3-12h^2-63h+27\right)>0
$$

for $0<h\le3/8$, since the cubic is decreasing there and equals $891/512$ at
$3/8$.  Hence the first positive root is $<c_0$, so $c_{\max}<c_0$.  The case
$h=0$ is trivial.

In the $q\ge0$ branch, the boundary inequality is

$$
(s^2-1)c^2+pc-p^2\le0,\qquad s=p+h.
$$

At $c_0=1-h/3$, the exact expansion is

$$
\begin{aligned}
9F_T(p,h,c_0)={}&h(h-6)p^2
+\left(2h^3-12h^2+15h+9\right)p\\
&+h^4-6h^3+8h^2+6h-9.
\end{aligned}
$$

For $0<h\le1/2$, this expression is strictly increasing in $p$ on
$[1/2,1-h]$. Its derivative is minimized at $p=1-h$, where it equals

$$
2h^2+3h+9>0.
$$

Also $q(p)=s^4-s^2+ph$ is strictly increasing wherever $q\ge0$. Indeed,
$ph\le s^2/4$ gives

$$
q\le s^2\left(s^2-\frac34\right),
$$

so $q\ge0$ implies $s\ge\sqrt3/2$, and then

$$
q'(p)=4s^3-2s+h>0.
$$

Suppose first that $q(1/2)<0$. Then $h<3/8$, and there is a unique
$p_0\in(1/2,1-h)$ with $q(p_0)=0$. At

$$
p_*=1-\frac{4h}{3},
$$

direct substitution gives

$$
q(p_*)=
\frac{h}{81}\left(h^3-12h^2-63h+27\right)>0.
$$

Hence $p_0<p_*$ and

$$
s_0=p_0+h<c_0.
$$

At $q=0$, the exact Cells $L$ and $T$ agree and their selected radial root is
$s_0$. Therefore $F_T(p_0,h,c_0)\ge0$, and monotonicity in $p$ gives the same
inequality for every $p\ge p_0$.

Now suppose $q(1/2)\ge0$. Put

$$
q_{1/2}(h)=h^4+2h^3+\frac{h^2}{2}-\frac3{16},
$$

and

$$
R(h)=9F_T\left(\frac12,h,c_0\right)
=h^4-5h^3+\frac94h^2+12h-\frac92.
$$

Both functions are strictly increasing on $[0,1/2]$. Indeed,

$$
q_{1/2}'(h)=h\left(4h^2+6h+1\right)>0,
$$

and

$$
R'(h)=4h^3-15h^2+\frac92h+12.
$$

The latter derivative is concave on this interval and has endpoint values
$12$ and $11$, so it is positive. For

$$
h_* = \frac{24}{65},
$$

one has

$$
q_{1/2}(h_*)=-\frac{20739}{285610000}<0,
$$

while

$$
R(h_*)=\frac{157527}{35701250}>0.
$$

Thus $q(1/2)\ge0$ implies $h>h_*$ and hence $R(h)>0$. Monotonicity in $p$
again yields $F_T(p,h,c_0)\ge0$.

Finally,

$$
c_0\le1\le2p.
$$

This is the exact Cell-$T$ selector check. It places $c_0$ on the selected
lower component, not on the discarded high component. Since
$F_T(p,h,c_0)\ge0$, $c_0$ lies at or beyond the selected first boundary root.
Thus

$$
\boxed{c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.}
$$

## Outer ratio target

We prove

$$
\boxed{d_2^C<\frac H3.}
$$

### Branch I: $H=1-u$

In this branch $a_0\ge x$ and $a_0\le u$.  Define

$$
K:=x+2y-xy-D.
$$

Since

$$
d_2^C=\frac{D+xy-uS-y}{S}
$$

and $D+xy-y=S-K$,

$$
d_2^C=1-u-\frac KS=H-\frac KS.
$$

Thus

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}.
$$

Let

$$
b_\circ(x)=\frac{-x+\sqrt{4-3x^2}}2,\qquad h(x)=b_\circ(x)-\frac12.
$$

We claim

$$
H\