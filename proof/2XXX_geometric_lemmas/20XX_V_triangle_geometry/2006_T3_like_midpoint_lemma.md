# T3-like Midpoint Lemma

Status: Proven local lemma

This file uses the $V_i$-triangle type convention from
[`../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
and the half-skeleton midpoint inventory from
[`../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md).

## Statements

Let $H$ be the regular side-$1$ hexagon centered at $O$, with vertices
$V_0,\dots,V_5$, and let

$$
M_i=\frac12V_i
$$

be the midpoint of the radial segment $r_i=[O,V_i]$.

Let $T_i$ be a closed unit equilateral $V_i$-triangle. If $T_i$ is T3-like,
that is, if its local type is

$$
(o,n)=(2,1),
$$

then

$$
M_i\notin T_i.
$$

Consequently, after maximalizing a T3-like $V_i$-triangle over the
half-skeleton $S_{1/2}$, one may assume that it contains one of the adjacent
midpoints $M_{i-1}$ or $M_{i+1}$.

## Proof of the midpoint exclusion

By dihedral symmetry it is enough to prove the claim for $i=0$. Put the origin
at $V_0$ and use the cone basis

$$
E_-=V_5-V_0,\qquad E_+=V_1-V_0.
$$

Thus a point is written as

$$
X=V_0+uE_-+vE_+.
$$

In these coordinates,

$$
V_0=(0,0),\qquad O=(1,1),\qquad M_0=\left(\frac12,\frac12\right),
$$

and the metric is

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

The hexagon is

$$
H=\left\{(u,v):0\le u\le2,\ 0\le v\le2,\ -1\le v-u\le1\right\},
$$

and the two adjacent radial rays are

$$
r_5=\left\{(1,t):0\le t\le1\right\},\qquad r_1=\left\{(t,1):0\le t\le1\right\}.
$$

Let $T$ be a closed unit equilateral triangle containing $V_0=(0,0)$ and
$M_0=(1/2,1/2)$. Assume that exactly two vertices of $T$ lie outside $H$. We
will prove that $T$ has no positive-length intersection with either $r_5$ or
$r_1$. Hence $n=0$, so such a triangle cannot be T3-like.

Since $T$ has diameter $1$ and contains $(0,0)$, every vertex
$Z=(u,v)$ of $T$ satisfies

$$
u^2+v^2-uv\le1.
$$

If such a vertex lies outside $H$, then it must violate either $u\ge0$ or
$v\ge0$. Indeed, if $u>2$, then

$$
u^2+v^2-uv=\left(v-\frac u2\right)^2+\frac34u^2>1,
$$

and the case $v>2$ is symmetric. If $u,v\ge0$ and $v-u>1$, write
$v=u+d$ with $d>1$; then

$$
u^2+v^2-uv=u^2+ud+d^2>1.
$$

The case $u-v>1$ is identical. Therefore an outside vertex has either $u<0$
or $v<0$.

Also, every outside vertex has both coordinates strictly less than $1$. If
$u<0$ and $v\ge1$, then

$$
u^2+v^2-uv>v^2\ge1,
$$

contradicting the unit-distance bound. The case $v<0$ and $u\ge1$ is
symmetric.

Let the two outside vertices be $A$ and $B$, and let the third vertex be
$C$. After ordering $A$ and $B$, write

$$
B-A=(r,s),\qquad C-A=(s,s-r).
$$

This is one of the two possible orientations of the equilateral triangle over
the side $AB$; swapping $A$ and $B$ exchanges the two choices. The unit side
condition is

$$
r^2+s^2-rs=1.
$$

Since $(0,0)\in T$, there are $\lambda,\mu\ge0$ with
$\lambda+\mu\le1$ such that

$$
(0,0)=A+\lambda(B-A)+\mu(C-A).
$$

Thus

$$
A=-\lambda(r,s)-\mu(s,s-r).
$$

Consequently,

$$
A_u=-\lambda r-\mu s,\qquad A_v=-\lambda s-\mu(s-r),
$$

$$
B_u=(1-\lambda)r-\mu s,\qquad B_v=(1-\lambda)s-\mu(s-r),
$$

and

$$
C_u=-\lambda r+(1-\mu)s,\qquad C_v=-\lambda s+(1-\mu)(s-r).
$$

The midpoint vector has the decomposition

$$
\left(\frac12,\frac12\right)=\frac r2(r,s)+\frac{s-r}{2}(s,s-r),
$$

because $r^2+s^2-rs=1$. Hence $M_0\in T$ is equivalent to

$$
\lambda+\frac r2\ge0,\qquad \mu+\frac{s-r}{2}\ge0,\qquad \lambda+\mu+\frac s2\le1.
$$

Set

$$
t=s-r.
$$

Then

$$
r^2+rt+t^2=1,
$$

and

$$
C_u=A_u+s=B_u+t,\qquad C_v=A_v+t=B_v-r.
$$

Each outside vertex has at least one negative coordinate. We now check the
four possible choices of negative coordinates.

### Case 1: $A_u<0$ and $B_u<0$

First consider $C_u$. If $s\le1$, then $C_u=A_u+s<1$. Suppose instead that
$s>1$. Solving the unit equation as a quadratic in $r$ gives

$$
r=\frac{s\pm\sqrt{4-3s^2}}2.
$$

For $s>1$, both roots are positive and smaller than $s$, so

$$
r>0,\qquad t=s-r>0.
$$

Since $r^2+rt+t^2=1$, also $t<1$. From $B_u=A_u+r<0$ we get
$A_u<-r$, and therefore

$$
C_u=A_u+s=A_u+r+t<t<1.
$$

Thus $C_u\le1$.

Now consider $C_v$. If $r\ge0$, then

$$
C_v=B_v-r\le B_v<1,
$$

because $B$ is an outside vertex. Suppose instead that $r<0$. Since
$A_u=-\lambda r-\mu s<0$, one must have $s>0$. Put

$$
x=-r>0,\qquad y=s>0.
$$

Then

$$
x^2+y^2+xy=1.
$$

The midpoint containment inequality $\lambda+r/2\ge0$ gives
$\lambda\ge x/2$. Therefore

$$
C_v=-\lambda y+(1-\mu)(x+y)\le x+y-\frac{xy}{2}.
$$

Let $q=x+y$. From $x^2+y^2+xy=1$ we have $xy=q^2-1$, hence

$$
x+y-\frac{xy}{2}=q-\frac{q^2-1}{2}=1-\frac{(q-1)^2}{2}\le1.
$$

Thus $C_v\le1$.

### Case 2: $A_v<0$ and $B_v<0$

This is the reflection of Case 1 under $u\leftrightarrow v$. Hence again

$$
C_u\le1,\qquad C_v\le1.
$$

### Case 3: $A_u<0$ and $B_v<0$

First consider $C_u$. If $s>1$, the same quadratic calculation as in Case 1
gives $r>0$, $t>0$, and $t<s$. Since

$$
B_v=(1-\lambda)s-\mu t<0,
$$

we would have $\mu t>(1-\lambda)s$, hence $\mu>1-\lambda$. This contradicts
$\lambda+\mu\le1$. Therefore $s\le1$, and

$$
C_u=A_u+s<1.
$$

Now consider $C_v=B_v-r$. Since $B_v<0$, it is enough to prove $r\ge-1$.
Assume, for contradiction, that $r<-1$. Solving the unit equation as a
quadratic in $s$ gives

$$
s=\frac{r\pm\sqrt{4-3r^2}}2.
$$

For $r<-1$, both roots are negative, so $s<0$. But then

$$
A_u=-\lambda r-\mu s>0,
$$

unless $\lambda=\mu=0$, which would give $A=(0,0)$. In either case this
contradicts $A_u<0$. Hence $r\ge-1$, and

$$
C_v=B_v-r<-r\le1.
$$

Thus $C_u\le1$ and $C_v\le1$.

### Case 4: $A_v<0$ and $B_u<0$

This is the reflection of Case 3 under $u\leftrightarrow v$. Hence again

$$
C_u\le1,\qquad C_v\le1.
$$

The four cases cover all possibilities. Therefore all vertices of $T$ satisfy

$$
u\le1,\qquad v\le1.
$$

The outside vertices $A$ and $B$ in fact satisfy strict inequalities
$A_u,A_v,B_u,B_v<1$. Hence at most the single vertex $C$ can lie on the line
$u=1$. Since $T$ is convex, $T\cap\left\{u=1\right\}$ is the convex hull of
the vertices of $T$ lying on that line. Therefore

$$
T\cap r_5
$$

has zero length. The same argument with $v=1$ shows that

$$
T\cap r_1
$$

has zero length.

Thus any closed unit equilateral $V_0$-triangle that contains $M_0$ and has
two outside vertices has $n=0$. A T3-like triangle has $(o,n)=(2,1)$, so a
T3-like $V_0$-triangle cannot contain $M_0$. Rotating the argument proves the
claim for every $i$.

## Maximality consequence over $S_{1/2}$

For a normalized $V_i$-triangle over $S_{1/2}$, the local midpoint set is

$$
\left\{M_{i-1},M_i,M_{i+1}\right\}.
$$

A T3-like triangle has positive-length intersection with exactly one of the
two adjacent rays. By the midpoint exclusion above, it cannot contain $M_i$.
If, after maximalizing over $S_{1/2}$, it contained neither adjacent midpoint,
then its trace on the local half-skeleton would be dominated by the
corresponding axis-aligned representative on the same adjacent side. This
contradicts maximality. Hence a maximal T3-like representative over
$S_{1/2}$ contains one of

$$
M_{i-1},\qquad M_{i+1}.
$$
