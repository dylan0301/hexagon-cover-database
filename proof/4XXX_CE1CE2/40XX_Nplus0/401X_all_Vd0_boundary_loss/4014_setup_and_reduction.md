# Setup and Boundary-Loss Reduction for CE1/CE2 Vd0

Status: Strategy

This file records the normalized boundary-loss reduction for the CE1/CE2, all-Vd0 case.  It is used by the later branch files in this folder.

## 1. Target and assumptions

Normalize the center triangle so that

$$
C=(0,0),\qquad M_0\in T_C.
$$

The intended case has:

- $T_C$ is CE1 or CE2.
- CE2 use of this reduction is conditional on the replacement theorem in
  `2104` and on routing every V-type or $N_+$ exit created by the replacement.
- All six $V_i$-triangles are Vd0.
- The contradiction assumption is

$$
a_i+b_i\le 1\qquad i=0,\dots,5.
$$

The boundary target is the hexagon perimeter contribution in the picture target.  The radial midpoint assumptions and the two half-diagonal segments are used only to force the local $c$-requirements recorded below.

If a $C$-boundary interval is already covered by the adjacent $V$-triangles, then that case is removable by the open-triangle perimeter argument.  Therefore the active cases considered here have a positive $C$-only interval.

## 2. Active interval notation

On the normalized edge

$$
e_{0,1}(x)=V_0+x(V_1-V_0),\qquad 0\le x\le1,
$$
write the active $C$-interval as

$$
T_C\cap e_{0,1}=[s,t],\qquad 0<s<t<1.
$$

Set

$$
u:=1-t,\qquad w:=t-s,\qquad s=1-u-w.
$$

The open-triangle, non-covered active interval condition is

$$
w>0.
$$

The same formulas apply to CE2 after using the `2104` two-gap replacement and
selecting the one remaining active $C$-interval, conditional on routing any
V-type or $N_+$ exit.

## 3. C-triangle slope parameterization

The formulas in this section are the historical $r>1$ specialization. The
exact CE1 center domain and radial exits are proved in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).
The coupled two-interval CE2 domain is different and is proved in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).
No proof reducing every exact CE1/CE2 configuration to the specialization
below is supplied in this package; this is one reason the file remains
Strategy.

Let the two side functions cutting $e_{0,1}$ at $s$ and $t$ have positive edge-slopes $p$ and $q$.  Put

$$
r=\frac qp.
$$

The recorded high-loss branch has $r>1$. Define

$$
D=\sqrt{r^2-r+1},\qquad R=\frac1r,\qquad S=\sqrt{1-R+R^2}=RD.
$$

The useful rationalized offset is

$$
\delta=\frac1{D+r}=\frac{R}{1+S}.
$$

On the main $r>1$ C-geometry branch, the radial exits toward $V_1$ and $V_5$ are

$$
\gamma_1=1-ru,
$$

and

$$
\gamma_5=u-\delta-\frac{w}{r-1} =u-\frac{R}{1+S}-\frac{R}{1-R}w.
$$

Equivalently, in $(R,u,s)$ variables,

$$
\gamma_5=u-\frac{R}{1+S}-\frac{R(1-u-s)}{1-R}.
$$

The values $1-\gamma_1$ and $1-\gamma_5$ are the radial requirements left for the adjacent $V_1$- and $V_5$-triangles.

## 4. The maximal adjacent V-values

Let the actual-coordinate nonsupercritical Vd0 map be

$$
\mathsf B_c^0(a)=
\sup\left\{
B(T):A(T)\ge a,
C(T)\ge c,
A(T)+B(T)\le1,
T\text{ Vd0}
\right\},
$$

when the set is nonempty.

The adjacent maximalized triangles satisfy

$$
B_1=\mathsf B_{1-\gamma_1}^0(u),
$$

and

$$
B_5=\mathsf B_{1-\gamma_5}^0(s).
$$

Define the boundary-loss objective

$$
F:=B_5+B_1.
$$

## 5. Reduction to $F<1$

Assume $F<1$.  Then the portion of the boundary left to $V_2,V_3,V_4$ has length at least

$$
(1-B_1)+1+1+(1-B_5)=4-F.
$$

If $F<1$, then

$$
4-F>3.
$$

But the contradiction assumption gives

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Each Vd0 triangle contributes at most $a_i+b_i$ units of boundary length on the perimeter.  Therefore $V_2,V_3,V_4$ cannot cover a boundary set of length greater than $3$.

Thus the branch analysis in this folder is reduced to the following inequality:

$$
\boxed{
\mathsf B_{1-\gamma_5}^0(s)
+\mathsf B_{1-\gamma_1}^0(u)<1.
}
$$

## 6. Covered-interval removal

If the active $C$-boundary interval is already covered by adjacent V-triangles,
then the $C$-triangle contributes no new boundary length on that interval. In
CE2, after the replacement normalization, if both $C$-intervals are covered by
V-triangles, then $T_C\cap\partial H$ contributes no new boundary length.

Under the open-triangle assumption and $a_i+b_i<1$, the six V-triangles alone have total boundary contribution strictly less than $6$, while $\partial H$ has length $6$.  Hence they cannot cover the perimeter.  Such covered-interval cases are removed before the branch analysis.

## 7. Degenerate limits

The exact point-contact case $w=0$ is removed because open triangles do not cover a boundary interval by a single point.  However, $w\to0^+$ remains a real limiting regime.  Several branch estimates in later files are therefore pointwise strict but not uniform in a full neighborhood of $w=0$.
