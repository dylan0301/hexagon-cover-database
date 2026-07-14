# Exact Finite Caliper Certificate For The AB-Set

Status: Proven

Write $u(\theta)=(\cos\theta,\sin\theta)$.  Let

$$
O=(0,0),\qquad B=(b,0),\qquad A=a u(120^\circ),
$$

where $a,b\ge0$, and retain the fixed closed cone

$$
C=\left\{r u(\theta):r\ge0,\ 0^\circ\le\theta\le120^\circ\right\}
$$

even when $A=O$ or $B=O$.  Put

$$
S_x=\left\{O,A,B,x\right\}.
$$

This note gives an exact finite certificate for

$$
K(a,b)=C\cap\bigcup\left\{T:T\text{ is a closed unit equilateral
triangle and }\left\{O,A,B\right\}\subseteq T\right\}.
$$

Unlike the simplified named-curve tables in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md), the
certificate below has no sampled comparison, generic-position assumption, or
unresolved case pruning.  It is an exhaustive description for every
$a,b\ge0$, including repeated points and collinear degeneracies.

## 1. Support sums

Let $R$ denote counterclockwise rotation through $120^\circ$, and let $J$
denote counterclockwise rotation through $90^\circ$.  For a nonempty finite
set $S$ and a vector $N$, define

$$
W_S(N)=\sum_{k=0}^2\max_{z\in S}\left\langle z,R^kN\right\rangle.
\tag{1}
$$

Because $N+RN+R^2N=0$, this quantity is translation-invariant.  It is also
nonnegative: for any fixed $z_0\in S$, the three maxima in (1) are at least
the three scalar products with $z_0$, whose sum is zero.

For two distinct points $p,q\in S$, put

$$
N_{pq}^{\varepsilon}=\varepsilon J(q-p),\qquad
\varepsilon\in\left\{-1,1\right\}.
\tag{2}
$$

Thus $N_{pq}^{\varepsilon}$ is an unnormalized normal to the line $pq$.

## 2. Finite caliper theorem

**Theorem 2.1.** Let $S$ be a nonempty finite subset of the plane.

- If $S$ has only one distinct point, it is contained in equilateral
  triangles of arbitrarily small positive side length.
- If $S$ has at least two distinct points, then $S$ is contained in a closed
  unit equilateral triangle if and only if there are distinct $p,q\in S$ and
  $\varepsilon\in\left\{-1,1\right\}$ such that

$$
W_S\left(N_{pq}^{\varepsilon}\right)
\le \frac{\sqrt3}{2}\lVert p-q\rVert.
\tag{3}
$$

*Proof.*  For a unit vector $n$, let

$$
G_S(n)=\sum_{k=0}^2h_S(R^kn),\qquad
h_S(n)=\max_{z\in S}\langle z,n\rangle.
$$

The three supporting half-planes with outward normals $n,Rn,R^2n$ and
support numbers $h_S(n),h_S(Rn),h_S(R^2n)$ enclose an equilateral triangle
of side $2G_S(n)/\sqrt3$.  Indeed, the sum of the support numbers is
translation-invariant and equals three times the inradius.  Consequently
a supporting triangle of side at most $1$ may be enlarged concentrically to
a unit one, and

$$
S\text{ fits in a closed unit equilateral triangle}
\quad\Longleftrightarrow\quad
\min_{\lVert n\rVert=1}G_S(n)\le\frac{\sqrt3}{2}.
\tag{4}
$$

It remains to make the minimum finite.  Replace $S$ by its convex hull.  On
an open interval of normal directions on which the three support vertices
are fixed, rotation by an angle $\varphi$ gives

$$
G_S(\varphi)=c\cos\varphi+d\sin\varphi,
\qquad G_S''(\varphi)=-G_S(\varphi)<0.
$$

The strict sign holds for every non-singleton $S$: if $G_S(n)=0$, then the
three support inequalities, applied relative to any one point of $S$, force
every difference of two points to have zero scalar product with the three
spanning normal directions, so all points coincide.  Hence an open support
cell contains no local minimum.  A global minimum is
attained at a cell endpoint, where at least one of the three support faces
contains two distinct points $p,q\in S$.  One of its three normals is
therefore $N_{pq}^{\varepsilon}/\lVert p-q\rVert$ for a sign
$\varepsilon$.  If that normal is $R^kn$ rather than $n$, replace $n$ by
$R^kn$; cyclic invariance gives $G_S(Rn)=G_S(n)$.  Conversely every normal
in (2) is a legitimate orientation to test.  Since $W_S$ is homogeneous of
degree one in its normal, (4) is exactly (3).

If the convex hull is a nondegenerate segment, the same conclusion follows
directly by using either normal to that segment.  This also proves the only
lower-dimensional case not covered by the open-cell argument. $\square$

## 3. Exact AB-set formula

**Corollary 3.1.** If $S_x$ has at least two distinct points, then

$$
\boxed{
x\in K(a,b)
\quad\Longleftrightarrow\quad
x\in C\ \text{ and }\
\min_{\substack{\left\{p,q\right\}\subseteq S_x,\ p\ne q\\
\varepsilon\in\left\{-1,1\right\}}}
\frac{W_{S_x}\left(N_{pq}^{\varepsilon}\right)}{\lVert p-q\rVert}
\le\frac{\sqrt3}{2}.
}
\tag{5}
$$

When all four labels coincide, (5) is replaced by the first clause of
Theorem 2.1, and $x=O=A=B$ belongs to $K(a,b)$.

There are at most six unordered pairs in $S_x$ and two signs for each pair,
so (5) has at most twelve caliper candidates.  Repeated labels simply remove
zero-length pairs; no limiting convention is required.

*Proof.* Apply Theorem 2.1 to $S_x$.  A unit triangle contains $x$ together
with $O,A,B$ exactly when $x$ belongs to the defining union for $K(a,b)$.
The additional condition $x\in C$ is the final intersection in the
definition of $K(a,b)$. $\square$

## 4. Finite polynomial cells

Formula (5) is also a finite semialgebraic certificate.  Fix a candidate
$(p,q,\varepsilon)$, write $N=N_{pq}^{\varepsilon}$ and $N_k=R^kN$, and
choose labels $z_0,z_1,z_2\in S_x$.  The corresponding support cell is
defined by the finite linear or quadratic inequalities

$$
\langle z_k,N_k\rangle\ge\langle z,N_k\rangle
\qquad (z\in S_x,\ k=0,1,2).
\tag{6}
$$

On that cell,

$$
W_{S_x}(N)=\sum_{k=0}^2\langle z_k,N_k\rangle.
\tag{7}
$$

The clause also includes the strict polynomial condition
$\lVert p-q\rVert^2>0$.  Without it, a repeated pair would create the
spurious squared inequality $0\le0$.

Since $W_{S_x}(N)\ge0$, condition (3) is equivalent on the cell to

$$
4\left(\sum_{k=0}^2\langle z_k,N_k\rangle\right)^2
\le3\lVert p-q\rVert^2.
\tag{8}
$$

There are only $4^3$ choices of $(z_0,z_1,z_2)$ for each of the at most
twelve pair-normal candidates.  All four labeled points are affine-linear in
the joint variables $(a,b,x)$, so the scalar products in (6)--(8) have degree
at most two and (8) has degree at most four in those variables.  Taking the
union of these finitely many support cells is exactly (5).  Thus (6)--(8),
with no omitted sign pattern, are an exhaustive polynomial case catalog for
the ab-set.

This expansion also proves that every non-axis algebraic boundary piece has
degree at most four.  Lines, unit circles, and the limaçon quartics of the
empirical named-curve catalog arise by resolving particular choices in
(6)--(8); they are not additional geometric assumptions.

## 5. Existence and exact counterclockwise tracing

Put

$$
\rho=a^2+ab+b^2=\lVert A-B\rVert^2.
$$

If $\rho>0$, the three-point set $\left\{O,A,B\right\}$ has minimum enclosing
equilateral-triangle side length $\sqrt\rho$.  Indeed, the distance
$\lVert A-B\rVert$ gives the lower bound, and testing the normal to $AB$
whose supporting triangle lies on the $O$-side gives the matching upper
bound in (4).  If $\rho=0$, all three labels
coincide and triangles of arbitrarily small positive side contain them.
Therefore

$$
K(a,b)=\varnothing\quad\Longleftrightarrow\quad\rho>1.
\tag{9}
$$

For $\rho\le1$, the set $K(a,b)$ is compact and star-shaped with respect to
$O$.  Indeed, the fitting functional in (4) is continuous in $x$, while the
diameter bound gives $\lVert x-O\rVert\le1$; and if a triangle contains $O$
and $x$, it contains the segment $[O,x]$.
Consequently its non-axis boundary is traced counterclockwise by increasing
$\theta\in[0^\circ,120^\circ]$ and taking

$$
r_*(\theta)=\max\left\{r\ge0:r u(\theta)\text{ satisfies one of the finite
cells }(6)\text{--}(8)\right\}.
\tag{10}
$$

After substituting $x=r u(\theta)$, every candidate in (10) is given by
explicit polynomial equalities and inequalities of degree at most four.
The largest admissible endpoint is therefore an exact, finite algebraic
boundary rule in counterclockwise order.  Ties cover tangencies, zero-length
arcs, and transitions automatically.  In particular, no connectivity claim
about a separately proposed parameter region and no floating-point sample is
needed for exhaustiveness.

The especially useful strict branch $a+b>1$, $\rho<1$ simplifies much
further to two disks cut by two half-planes.  That closed form and its
four-piece frontier are proved in
[`20091_ab_union_curve_a_plus_b_gt_1.md`](20091_ab_union_curve_a_plus_b_gt_1.md).
