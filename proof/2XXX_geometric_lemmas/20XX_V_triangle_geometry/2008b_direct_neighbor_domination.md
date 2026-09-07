# Direct neighboring-ray domination without the piecewise capacity formula

Status: Proven

This source proves exactly the neighboring estimate needed by the active
witness and demand-recovery arguments. The full function and its selected
cubic/plateau/radical branches remain an independent exact result in
[`2008`](2008_neighbor_ray_max_c_formula.md); they are not a dependency of
this proof. Capacities have their variational meanings as maxima over closed
unit equilateral triangles containing the vertex and the two edge anchors.

## 1. Sharp diagonal capacity

For $0\le m\le1/2$,

$$C_+(m,m)=C_-(m,m)=1-m.$$

**Proof.** Use oblique coordinates with metric $x^2+y^2-xy$. The relevant
points are $P=(0,0)$, $A=(m,0)$, $B=(0,m)$, $Z=(c,1)$, $0\le c\le1$.
The case $m=0$ is immediate. Suppose $0<m\le1/2$ and $c>1-m$.
Their convex hull has cyclic order $P,A,Z,B$. The support-cell rotation
lemma in [`2607`](../26XX_enclosing_triangle_tools/2607_minimal_enclosing_equilateral_quadrilateral_lemma.md)
reduces the least equilateral enclosure to the four outward edge normals.
At $PA$ and $BP$ its side lengths are $c+m>1$ and $1+m>1$.

Put $h=\sqrt3/2$ and embed $(x,y)$ as $(x-y/2,hy)$. At the other two
edges use the unnormalized outward normals

$$n_A=(h,1/2-c+m),\qquad n_B=(h(m-1),m/2+c-1/2).$$

Their squared norms and support-sum numerators are

$$
\begin{aligned}
D_A&=(c-m)^2-(c-m)+1,&N_A&=m+c^2-cm-c+1,\\
D_B&=c^2+cm-c+m^2-2m+1,&N_B&=cm+c^2-c-m+1.
\end{aligned}
$$

Selecting support points $(A,Z,P)$ in the three $120$-degree directions
at $n_A$, and $(B,P,Z)$ at $n_B$, gives

$$L_{AZ}\ge N_A/\sqrt{D_A},\qquad L_{ZB}\ge N_B/\sqrt{D_B}.$$

These are lower bounds; no unproved active-support selector is needed.
For $q=c+m-1>0$, exact expansion gives

$$
\begin{aligned}
N_A^2-D_A={}&q^2\big((q+1-3m)^2+4m^2-2m+1\big)\\
&+q(1-2m)(6m^2-2m+1)+m^2(1-2m)^2>0,\\
N_B^2-D_B={}&q^4+(2-2m)q^3+(m^2-4m+2)q^2\\
&+(1-m)(1-2m)q>0.
\end{aligned}
$$

Indeed $4m^2-2m+1=4(m-1/4)^2+3/4$, $6m^2-2m+1>0$, and
$m^2-4m+2\ge1/4$ on $[0,1/2]$. Both numerators are positive:
$N_A\ge(1+m)(3-m)/4>0$ and $N_B=1-m+(1-m)q+q^2>0$.
All four orientations therefore require side greater than one.

Equality is realized by

$$\operatorname{conv}\{(-m,0),(1-m,0),(1-m,1)\}.$$

Its three sides have unit length in the oblique metric, and it contains
$P,A,B,(1-m,1)$. Reflection proves the $C_-$ assertion. $\square$

## 2. Common-pair domination

For $p,q\ge0$, $p+q\le1$,

$$\boxed{C_\pm(p,q)\le1-\min(p,q)\le c_{\max}(p,q).}$$

**Proof.** Put $m=\min(p,q)$. Convexity makes the shorter $m,m$ anchors
belong to every candidate containing the $p,q$ anchors. The diagonal
lemma gives the upper bound. If $q=m$, the same edge-aligned triangle
contains $(p,0),(0,q),(1-q,1-q)$ because $p\le1-q$; its last point is
on the own ray. Thus $c_{\max}(p,q)\ge1-q$. Reflect when $p=m$.
Increasing either boundary demand only shrinks the feasible family, proving
coordinatewise antitonicity as well. $\square$

The comparison is valid as an upper bound for every permitted adjacent trace.
It does not assert that a triangle of a particular V type has that trace.
