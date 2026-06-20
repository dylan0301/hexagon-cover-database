# CE1, $N_+=0$, T3-Like/No Vd1-Vd2: $T_0$ Forcing

Status: Proven

This file proves only the following reduction. It does not close the whole
CE1, $N_+=0$, T3-like/no-Vd1-Vd2 branch.

## 1. Statement

Work in the CE1 branch. Normalize by the CE1/CE2 exactly-one-midpoint lemma and
by dihedral symmetry so that

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
$$

Assume also that

$$
N_+=0,
$$

no vertex role is Vd1 or Vd2, and at least one vertex role is T3-like. Then

$$
\boxed{T_0\text{ is T3-like}.}
$$

Equivalently, under these hypotheses the alternative in which all T3-like roles
lie among $T_1,\dots,T_5$ is impossible.

The proof uses the local midpoint inventory over $S_{1/2}$ from
[`../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md),
the T3-like midpoint exclusion from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md),
and the T3-like half-diagonal support convention from
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
Point-only contacts are treated as degeneracies in the sense of
[`../../../1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md`](../../../1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md).

## 2. A one-sided T3-like tradeoff

### Lemma 2.1

Let $T$ be a normalized T3-like $V_0$-triangle. Assume that $T$ contains
$M_1$, does not contain $M_0$, and has positive-length intersection with the
adjacent ray $r_1$.

Let

$$
b=\sup\{x\in[0,1]: e_{0,1}([0,x])\subset T\}
$$

be the boundary coordinate on $e_{0,1}$ from $V_0$ toward $V_1$.
Let

$$
c=\sup\{x\in[0,1]: [V_0,(1-x)V_0]\subset T\}
$$

be the own-radial exit coordinate on $r_0=[V_0,O]$, measured from $V_0$ toward
$O$. Finally, let $\ell$ be the first parameter on $r_1=[V_1,O]`, measured from
$V_1$ toward $O$, at which $T$ enters $r_1$. Thus $T\cap r_1$ contains
$M_1$ and begins at parameter $\ell\le 1/2$.

Then

$$
\boxed{b+c<1}
$$

and

$$
\boxed{b+\ell>1}.
$$

The reflected statement holds for a normalized T3-like $V_0$-triangle containing
$M_5$.

### Proof

Use Euclidean coordinates with

$$
V_0=(0,0),\qquad V_1=(1,0),\qquad O=\left({1\over2},-{\sqrt3\over2}\right).
$$

Put

$$
h={\sqrt3\over2}.
$$

By the T3-like normalization convention, translate the triangle, preserving its
side length and orientation, so that $V_0$ lies on a side of $T$. Write that
side in the unit direction

$$
d=(\cos\theta,\sin\theta),
$$

and put

$$
e=R_{-\pi/3}d.
$$

For some $0\le\lambda\le1$, the triangle has vertices

$$
-\lambda d,\qquad (1-\lambda)d,\qquad -\lambda d+e.
$$

In the oblique coordinates $X=xd+ye$, this is exactly

$$
x\ge -\lambda,\qquad y\ge0,\qquad x+y\le1-\lambda.
$$

Set

$$
K=\cos\left(\theta-{\pi\over6}\right).
$$

A direct solution of the two-by-two linear system for the three relevant lines
$e_{0,1}$, $r_0$, and $r_1$ gives

$$
b={h(1-\lambda)\over K},
$$

$$
c={h\lambda\over\sin\theta},
$$

and

$$
\ell={K-h(1-\lambda)\over\sin\theta}.
$$

Here the formula for $b$ comes from the side $x+y=1-\lambda$ on the boundary
edge $e_{0,1}$; the formula for $c$ comes from the side $x=-\lambda$ on the
own ray $r_0$; and the formula for $\ell$ comes from the side $x+y=1-\lambda$
on the adjacent ray $r_1$.

The condition $M_1\in T$ gives two active inequalities. First, the entry point
on $r_1$ lies no farther than $M_1$, so

$$
\ell\le {1\over2}.
$$

Using the formula for $\ell$, this is equivalent to

$$
\lambda\le1-\cos\theta.
$$

Second, the inequality $x(M_1)\ge-\lambda$ gives

$$
\lambda\ge {\sqrt3\over2}\sin\theta-{1\over2}\cos\theta.
$$

The exclusion $M_0\notin T$ is the strict inequality that the midpoint of $r_0$
lies beyond the side $x=-\lambda$, namely

$$
\lambda<{\sin\theta\over\sqrt3}.
$$

Since $\lambda\ge0$, this forces $\sin\theta>0$. If $\theta\ge\pi/3$, then

$$
{\sqrt3\over2}\sin\theta-{1\over2}\cos\theta
\ge {\sin\theta\over\sqrt3},
$$

contradicting the two preceding inequalities. Hence

$$
0<\theta<{\pi\over3}.
$$

On this interval,

$$
K>\sin\theta.
$$

Therefore $b+c$ is increasing as a function of $\lambda$, since

$$
{\partial\over\partial\lambda}(b+c)
=h\left(-{1\over K}+{1\over\sin\theta}\right)>0.
$$

Using $\lambda\le1-\cos\theta`, we get

$$
b+c
\le {h\cos\theta\over K}+{h(1-\cos\theta)\over\sin\theta}.
$$

Let

$$
y=\tan{\theta\over2}.
$$

Then $0<y<1/\sqrt3$, and direct simplification gives

$$
1-\left({h\cos\theta\over K}+{h(1-\cos\theta)\over\sin\theta}\right)
=
{y(1-\sqrt3 y)^2\over 2(\sqrt3+2y-\sqrt3 y^2)}.
$$

The right-hand side is strictly positive for $0<y<1/\sqrt3$. Hence

$$
b+c<1.
$$

For the second inequality, $b+\ell$ is also increasing in $\lambda$, because

$$
{\partial\over\partial\lambda}(b+\ell)
=h\left(-{1\over K}+{1\over\sin\theta}\right)>0.
$$

Thus its minimum occurs at $\lambda=0$. Therefore

$$
b+\ell-1
\ge {h\over K}+{K-h\over\sin\theta}-1
={ (K-h)(K-\sin\theta)\over K\sin\theta}.
$$

For $0<\theta<\pi/3$, both $K-h$ and $K-\sin\theta$ are strictly positive.
Hence

$$
b+\ell>1.
$$

This proves the lemma. The reflected case is obtained by swapping the two
adjacent sides at $V_0$.

## 3. Crossed adjacent T3-like pairs are impossible

### Lemma 3.1

Let $T_i$ and $T_{i+1}$ be adjacent T3-like vertex roles. Suppose

$$
M_{i+1}\in T_i,\qquad M_i\in T_{i+1}.
$$

Assume that, on the outer half-radial segments

$$
R_i=[V_i,M_i],\qquad R_{i+1}=[V_{i+1},M_{i+1}],
$$

no role other than $T_i$ and $T_{i+1}$ has positive-length support. Then this
configuration is impossible.

### Proof

Let $b_i$ be the boundary coordinate of $T_i$ on $e_{i,i+1}$ from $V_i$ toward
$V_{i+1}$. Let $c_i$ be the own-radial exit coordinate of $T_i$ on $r_i$, and
let $\ell_i$ be the entry coordinate of $T_i$ on $r_{i+1}$, measured from
$V_{i+1}$ toward $O$.

Apply Lemma 2.1 after rotating indices from $0$ to $i$. Since $M_{i+1}\in T_i$,
we have

$$
b_i+c_i<1,
$$

and

$$
b_i+\ell_i>1.
$$

Now let $a_{i+1}$ be the boundary coordinate of $T_{i+1}$ on the same boundary
edge $e_{i,i+1}$, measured from $V_{i+1}$ toward $V_i$. Let $c_{i+1}$ be its
own-radial exit coordinate on $r_{i+1}$, and let $\ell_{i+1}$ be its entry
coordinate on $r_i$, measured from $V_i$ toward $O$.

The reflected form of Lemma 2.1 gives

$$
a_{i+1}+c_{i+1}<1,
$$

and

$$
a_{i+1}+\ell_{i+1}>1.
$$

Because the outer half $R_i$ is covered and only $T_i$ and $T_{i+1}$ have
positive-length support on it, the own interval of $T_i$ and the adjacent-ray
interval of $T_{i+1}$ cannot leave an open gap. Therefore

$$
c_i\ge\ell_{i+1}.
$$

Similarly, covering $R_{i+1}$ gives

$$
c_{i+1}\ge\ell_i.
$$

Using $c_i\ge\ell_{i+1}$ and $a_{i+1}+\ell_{i+1}>1$, we get

$$
a_{i+1}+c_i>1.
$$

Together with $b_i+c_i<1$, this implies

$$
a_{i+1}>b_i.
$$

Using $c_{i+1}\ge\ell_i$ and $b_i+\ell_i>1`, we get

$$
b_i+c_{i+1}>1.
$$

Together with $a_{i+1}+c_{i+1}<1$, this implies

$$
b_i>a_{i+1}.
$$

The two strict inequalities $a_{i+1}>b_i$ and $b_i>a_{i+1}$ are incompatible.
Thus the crossed adjacent T3-like pair is impossible.

## 4. Midpoint matching among T3-like roles

Assume for contradiction that $T_0$ is not T3-like.

Since no vertex role is Vd1 or Vd2, every vertex role is either Vd0 or T3-like.
By the CE1/CE2 exactly-one-midpoint normalization, $T_C$ covers $M_0$ and no
other midpoint. Therefore every midpoint

$$
M_1,\dots,M_5
$$

must be covered by vertex roles.

Let $I$ be a maximal consecutive block of T3-like indices inside

$$
\{1,2,3,4,5\}.
$$

Such a block exists by the hypothesis that at least one vertex role is T3-like
and by the contradiction assumption that $T_0$ is not T3-like.

For any $j\in I$, the T3-like midpoint exclusion gives

$$
M_j\notin T_j.
$$

A Vd0 role covers no adjacent midpoint in the half-skeleton midpoint inventory,
and a T3-like role covers exactly one adjacent midpoint in that inventory. Hence
$M_j$ must be covered by one of the T3-like roles adjacent to it. Since $I$ is a
maximal consecutive T3-like block, the covering role also has index in $I$.

The number of T3-like triangles in $I$ is the same as the number of midpoint
requirements indexed by $I$, and each T3-like triangle in $I$ covers exactly one
adjacent midpoint. Therefore these incidences form a bijective matching between
the midpoint labels in $I$ and the T3-like triangle labels in $I$, with edges
only between adjacent indices.

Let $m$ be the left endpoint of $I$. If $m=5$, then $M_5$ has no adjacent
T3-like source, because $T_4$ is outside $I$ and $T_0$ is not T3-like. This is
impossible. Hence $m<5$.

The midpoint $M_m$ cannot be matched to $T_{m-1}$, since $T_{m-1}$ is not
T3-like or does not exist inside $\{1,\dots,5\}$. Hence

$$
M_m\in T_{m+1}.
$$

By bijectivity of the matching, the triangle $T_m$ must then be matched to its
only possible remaining adjacent midpoint, namely $M_{m+1}$. Thus the first two
indices of the block form a crossed adjacent pair:

$$
M_{m+1}\in T_m,\qquad M_m\in T_{m+1}.
$$

In particular, $|I|\ge2$.

It remains to justify the support hypothesis of Lemma 3.1 for this endpoint
pair. The center triangle $T_C$ contains $O$ but does not contain either
$M_m$ or $M_{m+1}$. By convexity, $T_C$ has no point on the outer halves
$[V_m,M_m]$ and $[V_{m+1},M_{m+1}]$; otherwise the segment from that point to
$O$ would contain the corresponding midpoint.

A nonadjacent vertex role cannot meet either outer half in positive length,
because it contains a hexagon vertex at distance greater than $1$ from that
outer half, while every unit equilateral triangle has diameter $1$. The only
possible adjacent helpers would be $T_{m-1}$ on $R_m$ and $T_{m+2}$ on
$R_{m+1}$. The role $T_{m-1}$ is outside the maximal T3-like block, hence it is
Vd0 or absent, and therefore has no positive-length support on the adjacent ray
$r_m$. If $T_{m+2}$ exists and is T3-like, then the endpoint matching above
forces it to cover the midpoint on its other side, not $M_{m+1}$; by the
T3-like support convention it therefore has no positive-length support on
$r_{m+1}$. If $T_{m+2}$ is absent or Vd0, the same conclusion is immediate.

Consequently the outer halves $R_m$ and $R_{m+1}$ have positive-length support
only from $T_m$ and $T_{m+1}$. Lemma 3.1 applies and gives a contradiction.

Therefore the assumption that $T_0$ is not T3-like is impossible. Hence

$$
T_0\text{ is T3-like}.
$$

This proves the stated reduction.
