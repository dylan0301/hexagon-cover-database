# Skeleton-Length Obstruction for CE1/CE2 with at Least Two Supercritical $V$-Triangles

Status: Practically proven

## Statement

Let $H$ be the regular hexagon of side length $1$, centered at $O$, with vertices
$$
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),
\qquad i\in\mathbb Z/6\mathbb Z.
$$
Let
$$
M_i=\frac12V_i.
$$
Let the full hexagon skeleton be
$$
S=\partial H\cup\bigcup_{i=0}^5[O,V_i].
$$
Then
$$
\mathcal H^1(S)=6+6=12.
$$

Suppose a hypothetical cover of $S$ is organized as
$$
T_C,T_0,T_1,\dots,T_5,
$$
where $T_C$ is a center triangle containing $O$, and $T_i$ is a $V_i$-triangle containing $V_i$.

Assume:

1. $T_C$ is CE1 or CE2.
2. By the normalized CE1/CE2 midpoint lemma,
   $$
   T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
   $$
3. At least two $V_i$-triangles are supercritical:
   $$
   a_i+b_i>1.
   $$

Assume the following center-triangle skeleton cap:

**Center cap.** Every exact-$M_0$ CE1/CE2 center triangle satisfies
$$
L_S(T_C):=\mathcal H^1(T_C\cap S)<\frac32.
$$

Then the seven triangles cannot cover $S$.

---

## Lemma 1: A supercritical $V_i$-triangle covers no local midpoint

Let $T_i$ be a $V_i$-triangle with
$$
a_i+b_i>1.
$$
Then $T_i$ covers none of the three local radial midpoints
$$
M_{i-1},\quad M_i,\quad M_{i+1}.
$$

### Proof

First, $T_i$ cannot contain its own midpoint $M_i$, because the midpoint self-cover lemma gives
$$
M_i\in T_i\implies a_i+b_i\le1.
$$
Thus
$$
M_i\notin T_i.
$$

Second, $T_i$ cannot contain an adjacent radial midpoint. In normalized $V_0$-coordinates, the adjacent-ray maximum $C_+(a,b)$ is undefined when
$$
a+b>1.
$$
Equivalently, no point of the adjacent ray can be contained together with the two prescribed boundary edge intervals when $a+b>1$. By reflection, the same holds for both adjacent rays.

Therefore
$$
M_{i-1},M_i,M_{i+1}\notin T_i.
$$
$$
\Box
$$

---

## Lemma 2: At least one non-Vd0 rescuer is forced

Assume $T_C$ is CE1 or CE2 and covers exactly $M_0$. If at least two $V_i$-triangles satisfy
$$
a_i+b_i>1,
$$
then at least one $V_i$-triangle is Vd1, Vd2, or T3-like.

### Proof

Let
$$
A=\{i:a_i+b_i>1\}.
$$
By assumption,
$$
|A|\ge2.
$$
Since $A\subset\mathbb Z/6\mathbb Z$, at least one element of $A$ is not $0$. Choose
$$
s\in A,\qquad s\ne0.
$$

By Lemma 1, $T_s$ does not contain $M_s$. Also, $T_C$ does not contain $M_s$, because $T_C$ contains exactly $M_0$ and $s\ne0$.

Since $S$ contains the midpoint $M_s$, the midpoint $M_s$ must be covered by some other triangle.

A unit equilateral triangle has diameter $1$. If a $V_j$-triangle contains $M_s$, then
$$
|V_j-M_s|\le1.
$$
For the regular hexagon geometry, this is possible only for
$$
j\in\{s-1,s,s+1\}.
$$
The case $j=s$ is excluded because $T_s$ does not contain $M_s$. Hence $M_s$ must be covered by
$$
T_{s-1}\quad\text{or}\quad T_{s+1}.
$$

A Vd0 triangle has no positive-length adjacent-ray intersection and cannot cover an adjacent midpoint. Therefore the triangle rescuing $M_s$ must be one of
$$
\text{Vd1},\quad \text{Vd2},\quad \text{T3-like}.
$$
Thus at least one $V_i$-triangle is Vd1, Vd2, or T3-like.
$$
\Box
$$

---

## Lemma 3: Vd1, Vd2, and T3-like skeleton caps follow from the CE1/CE2 center cap

Assume the following unrestricted translated-center cap:

For any regular side-$1$ hexagon $K$, every CE1/CE2 center triangle $T$ satisfies
$$
L_{S(K)}(T)<\frac32,
$$
where $S(K)$ is the skeleton of $K$.

Then every $V_i$-triangle of type Vd1, Vd2, or T3-like satisfies
$$
L_S(T_i)<\frac32.
$$

### Proof

By hexagon symmetry it is enough to prove the claim for a $V_0$-triangle $T_0$.

Define the translated hexagon
$$
\widetilde H:=V_0+H.
$$
Its center is
$$
\widetilde O=V_0,
$$
and its vertices are
$$
W_j=V_0+V_j.
$$
In particular,
$$
W_3=V_0+V_3=O,
$$
$$
W_2=V_0+V_2=V_1,
$$
$$
W_4=V_0+V_4=V_5.
$$

Therefore the original local skeleton components around $V_0$ are components of the translated skeleton
$$
\widetilde S:=\partial\widetilde H\cup\bigcup_{j=0}^5[\widetilde O,W_j].
$$
Indeed,
$$
[V_0,V_1]=[\widetilde O,W_2],
$$
$$
[V_0,V_5]=[\widetilde O,W_4],
$$
$$
[O,V_1]=[W_3,W_2],
$$
$$
[O,V_5]=[W_3,W_4],
$$
and
$$
[O,V_0]=[\widetilde O,W_3].
$$

Now let $T_0$ be a $V_0$-triangle. Since $T_0$ contains $V_0=\widetilde O$, it is a center triangle for $\widetilde H$.

If $T_0$ is Vd1, Vd2, or T3-like, then $T_0$ has positive-length intersection with at least one of the adjacent rays
$$
[O,V_1]\quad\text{or}\quad[O,V_5].
$$
But these are boundary edges of $\widetilde H$:
$$
[O,V_1]=[W_3,W_2],
$$
$$
[O,V_5]=[W_3,W_4].
$$
Hence, viewed as a center triangle for $\widetilde H$, the triangle $T_0$ has positive-length overlap with at least one boundary edge of $\widetilde H$.

A unit equilateral triangle cannot have positive-length overlap with three boundary edges of a regular side-$1$ hexagon. Indeed, among any three boundary edges of a regular hexagon, two contain positive-length subsegments whose mutual distance is strictly greater than $1$, while a unit equilateral triangle has diameter $1$. Therefore $T_0$, viewed in $\widetilde H$, is CE1 or CE2.

By the translated CE1/CE2 center cap,
$$
L_{\widetilde S}(T_0)<\frac32.
$$

Finally, a unit triangle containing $V_0$ can meet the original skeleton $S$ in positive length only on the five local components
$$
[V_0,V_1],\quad [V_0,V_5],\quad [O,V_1],\quad [O,V_0],\quad [O,V_5].
$$
All five are contained in $\widetilde S$. Therefore
$$
L_S(T_0)\le L_{\widetilde S}(T_0)<\frac32.
$$
Thus
$$
L_S(T_0)<\frac32.
$$
By rotation symmetry, the same holds for every $V_i$-triangle of type Vd1, Vd2, or T3-like.
$$
\Box
$$

---

## Lemma 4: Vd0 with $a_i+b_i\le1$ has skeleton length at most $2$

Let $T_i$ be Vd0 and suppose
$$
a_i+b_i\le1.
$$
Then
$$
L_S(T_i)\le2.
$$

### Proof

By rotational symmetry, normalize to $i=0$.

Since $T_0$ is Vd0, it has no positive-length intersection with the adjacent rays
$$
[O,V_1]\quad\text{and}\quad[O,V_5].
$$
Thus among the six radial arms, it can have positive-length intersection only with its own radial arm
$$
[O,V_0],
$$
whose length is $1$. Hence the radial contribution is at most $1$.

The boundary contribution of $T_0$ is the sum of its adjacent boundary coverages:
$$
a_0+b_0\le1.
$$
A unit triangle containing $V_0$ cannot have positive-length intersection with non-adjacent boundary edges, because every non-adjacent boundary point, except isolated vertices, lies at distance $>1$ from $V_0$, while a unit equilateral triangle has diameter $1$.

Therefore
$$
L_S(T_0)\le (a_0+b_0)+1\le2.
$$
$$
\Box
$$

---

## Lemma 5: Vd0 with $a_i+b_i>1$ has skeleton length less than $3/2$

Let $T_i$ be Vd0 and suppose
$$
a_i+b_i>1.
$$
Then
$$
L_S(T_i)<\frac32.
$$

### Proof

By rotational symmetry, normalize to $i=0$. Write
$$
a=a_0,\qquad b=b_0.
$$
Since $T_0$ is Vd0 and $a+b>1$, it has no adjacent-ray contribution. Thus its skeleton contribution is
$$
L_S(T_0)=a+b+c,
$$
where $c$ is the length of its intersection with its own radial arm $[O,V_0]$.

We prove
$$
a+b+c<\frac32.
$$

By symmetry, assume
$$
0\le a\le b.
$$
The $a+b\ge1$ admissible cell gives the inequality
$$
(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0,
$$
with
$$
c\le\frac12.
$$

Set
$$
s=a+b,\qquad d=b-a.
$$
Then
$$
a=\frac{s-d}{2},\qquad b=\frac{s+d}{2}.
$$
The feasible range is
$$
1<s\le\frac2{\sqrt3},
$$
and
$$
0\le d\le\sqrt{4-3s^2}.
$$

Let
$$
c_0=\frac32-s.
$$
It is enough to prove that the quadratic expression
$$
P(c)=(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)
$$
is nonnegative at $c=c_0$. Since
$$
P(0)=b^4-b^2<0,
$$
the first positive root of $P$ is then at most $c_0$, so
$$
c\le c_0.
$$

Substituting $c_0=\frac32-s$ and multiplying by $16$, one obtains
$$
\begin{aligned}
Q(s,d)=
&d^4+8d^3s-6d^3+14d^2s^2-18d^2s+5d^2\\
&-8ds^3+30ds^2-34ds+12d\\
&+s^4-6s^3-19s^2+60s-36.
\end{aligned}
$$

We show
$$
Q(s,d)\ge0.
$$
Differentiate with respect to $d$:
$$
\frac{\partial Q}{\partial d}
=
2(2d+4s-3)\left(d^2+4ds-3d-s^2+3s-2\right).
$$
Since $s\ge1$ and $d\ge0$,
$$
2d+4s-3>0.
$$
For the second factor,
$$
d^2+4ds-3d-s^2+3s-2
=
d^2+d(4s-3)+(s-1)(2-s).
$$
On
$$
1<s\le\frac2{\sqrt3}<2,
$$
all three terms are nonnegative:
$$
d^2\ge0,
$$
$$
d(4s-3)\ge0,
$$
$$
(s-1)(2-s)>0.
$$
Therefore
$$
\frac{\partial Q}{\partial d}\ge0.
$$
So $Q(s,d)$ is increasing in $d$, and hence
$$
Q(s,d)\ge Q(s,0).
$$

Now
$$
Q(s,0)=(s-1)(s^3-5s^2-24s+36).
$$
The factor $s-1$ is positive. Let
$$
g(s)=s^3-5s^2-24s+36.
$$
Then
$$
g'(s)=3s^2-10s-24<0
$$
on
$$
1\le s\le\frac2{\sqrt3}.
$$
Thus $g$ is decreasing on this interval, and its minimum occurs at $s=2/\sqrt3$. We have
$$
g\left(\frac2{\sqrt3}\right)
=
\frac{88}{3}-\frac{136\sqrt3}{9}>0.
$$
Therefore
$$
g(s)>0
$$
throughout the feasible interval, and hence
$$
Q(s,d)>0.
$$

Thus
$$
P(c_0)\ge0,
$$
so
$$
c\le c_0=\frac32-a-b.
$$
Therefore
$$
a+b+c\le\frac32.
$$

Equality can occur only in the limiting degenerate case $a+b\to1^+$. Since the branch assumes $a+b>1$, we have strict inequality:
$$
a+b+c<\frac32.
$$
Thus
$$
L_S(T_0)<\frac32.
$$
$$
\Box
$$

---

## Theorem: Skeleton noncoverage under CE1/CE2 and at least two supercritical $V$-triangles

Assume:

1. $T_C$ is CE1 or CE2 and covers exactly one midpoint, normalized as $M_0$.
2. At least two $V_i$-triangles satisfy
   $$
   a_i+b_i>1.
   $$
3. The exact-$M_0$ CE1/CE2 center cap holds:
   $$
   L_S(T_C)<\frac32.
   $$

Then
$$
T_C,T_0,\dots,T_5
$$
cannot cover the skeleton $S$.

### Proof

By Lemma 2, since at least two $V_i$-triangles are supercritical, at least one $V_i$-triangle is Vd1, Vd2, or T3-like.

By Lemma 3, every Vd1, Vd2, or T3-like triangle satisfies
$$
L_S(T_i)<\frac32.
$$

The supercritical triangles are Vd0 with empty local midpoint subset, and by Lemma 5 each satisfies
$$
L_S(T_i)<\frac32.
$$

The remaining ordinary Vd0 triangles with $a_i+b_i\le1$ satisfy, by Lemma 4,
$$
L_S(T_i)\le2.
$$

The worst possible skeleton-length upper bound occurs when there are exactly:

- two supercritical Vd0 triangles;
- one Vd1/Vd2/T3-like rescuer;
- three ordinary Vd0 non-supercritical triangles.

Therefore
$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)
<
\frac32
+
2\cdot\frac32
+
\frac32
+
3\cdot2.
$$
The right-hand side is
$$
\frac32+3+\frac32+6=12.
$$
Thus
$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<12.
$$

But if the seven triangles covered $S$, then by subadditivity of length,
$$
12=\mathcal H^1(S)
\le
L_S(T_C)+\sum_{i=0}^5L_S(T_i).
$$
This is a contradiction.

Hence the skeleton $S$ is not covered.
$$
\Box
$$
