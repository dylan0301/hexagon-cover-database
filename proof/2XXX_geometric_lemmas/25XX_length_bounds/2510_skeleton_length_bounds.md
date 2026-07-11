# Skeleton-Length Obstruction for CE1/CE2 with At Least Two Supercritical $V$-Triangles

Status: Proven

## Statement

Let $H$ be the regular hexagon of side length $1$, centered at $O$, with vertices

$$
V_i=(\cos(i\pi/3),\sin(i\pi/3)),\qquad i\in\mathbb Z/6\mathbb Z.
$$

Let

$$
M_i=(1/2)V_i.
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

where $T_C$ is a center triangle containing $O$ in its interior, and $T_i$ is
a $V_i$-triangle containing $V_i$.

Assume:

1. $T_C$ is CE1 or CE2.
2. By the normalized CE1/CE2 midpoint lemma, whose interior hypothesis is
   supplied above,

   $$
   T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
   $$

3. At least two $V_i$-triangles are supercritical:

   $$
   a_i+b_i>1.
   $$

Then the seven triangles cannot cover $S$.

---

## Lemma 1: A supercritical $V_i$-triangle covers no local midpoint

Let $T_i$ be a $V_i$-triangle with

$$
a_i+b_i>1.
$$

Then $T_i$ covers none of

$$
M_{i-1},\quad M_i,\quad M_{i+1}.
$$

### Proof

The self-midpoint lemma gives

$$
M_i\in T_i\implies a_i+b_i\le1.
$$

Thus $M_i\notin T_i$.

Also, in normalized $V_0$-coordinates, the adjacent-ray maximum $C_+(a,b)$ is undefined when $a+b>1$. Hence no adjacent-ray point can be contained together with the two prescribed boundary edge intervals when $a+b>1$. By reflection, the same holds for both adjacent rays.

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

Since $|A|\ge2$, choose $s\in A$ with $s\ne0$.

By Lemma 1, $T_s$ does not contain $M_s$. Also, $T_C$ does not contain $M_s$, because $T_C$ contains exactly $M_0$ and $s\ne0$.

Since $S$ contains $M_s$, some other triangle must contain $M_s$. A unit equilateral triangle has diameter $1$. Therefore a $V_j$-triangle can contain $M_s$ only when

$$
j\in\{s-1,s,s+1\}.
$$

The case $j=s$ is excluded because $T_s$ does not contain $M_s$. Hence $M_s$ must be covered by $T_{s-1}$ or $T_{s+1}$.

A Vd0 triangle has no positive-length adjacent-ray intersection and cannot cover an adjacent midpoint. Therefore the rescuer is Vd1, Vd2, or T3-like.

$$
\Box
$$

---

## Lemma 3: Exact-$M_0$ CE1/CE2 center triangles have skeleton length $<3/2$

Let $T_C$ be an exact-$M_0$ CE1 or CE2 center triangle. Then

$$
L_S(T_C):=\mathcal H^1(T_C\cap S)<3/2.
$$

### Proof

Use the local affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Thus

$$
V_0=(0,0),\qquad V_1=(1,0),\qquad V_5=(0,1),\qquad O=(1,1).
$$

By reflection if necessary, assume that $T_C$ has positive boundary overlap with $e_{0,1}$. Write

$$
T_C\cap e_{0,1}=[s,t],\qquad 0<s<t<1.
$$

Label the two sides cutting $e_{0,1}$ so that

$$
T_C=\{F_0\ge0,\ F_1\ge0,\ F_2\ge0\},
$$

where

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t,
$$

and

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

The side functions satisfy

$$
F_0+F_1+F_2=\rho.
$$

They define a unit equilateral triangle because their gradients have the three side-normal directions of a unit equilateral triangle.

The exact-$M_0$ CE geometry forces

$$
0<\lambda<1.
$$

Indeed, if $\lambda=1$, then $F_0(O)=s-t<0$, contradicting $O\in T_C$. If $\lambda>1$, the conditions $O\in T_C$ and $s<t$ imply

$$
s>(\lambda-\rho)/(\lambda-1),
$$

whereas $M_1\notin T_C$ forces

$$
s<t<1-\lambda/2.
$$

But

$$
(\lambda-\rho)/(\lambda-1)\ge1-\lambda/2,
$$

because this is equivalent to

$$
(\lambda^2-\lambda+2)/2\ge\rho,
$$

and after squaring the difference is

$$
((\lambda^2-\lambda+2)/2)^2-\rho^2=(\lambda^2-\lambda)^2/4\ge0.
$$

Thus $\lambda\ge1$ is impossible. After possibly relabeling the two cutting sides, $0<\lambda<1$.

Define the center slacks

$$
C_0:=F_0(O),\qquad C_2:=F_2(O).
$$

Since $O\in T_C$,

$$
C_0\ge0,\qquad C_2\ge0.
$$

Direct calculation gives

$$
C_0=\rho-\lambda(1-s)-t,
$$

$$
C_2=\lambda+t-1.
$$

Hence

$$
t=1-\lambda+C_2,
$$

and

$$
\lambda s=C_0+C_2+1-\rho.
$$

Set

$$
P:=\rho(1-\rho).
$$

The condition $s<t$ becomes

$$
(C_0+C_2+1-\rho)/\lambda<1-\lambda+C_2.
$$

Multiplying by $\lambda$ and using $\rho^2=1-\lambda+\lambda^2$, this is

$$
C_0+(1-\lambda)C_2<P.
$$

So

$$
\boxed{C_0+(1-\lambda)C_2<P.}
$$

The $e_{0,1}$ boundary contribution is

$$
\ell_{01}=t-s=1-\lambda+C_2-(C_0+C_2+1-\rho)/\lambda.
$$

Now compute the possible $e_{5,0}$ overlap. On $e_{5,0}$, $b=0$, so

$$
F_1=(1-\lambda)a-\lambda s,
$$

$$
F_2=t+\lambda a>0,
$$

$$
F_0=\rho+\lambda s-t-a.
$$

Thus the $e_{5,0}$ interval length is

$$
\ell_{50}=[a_U-a_L]_+,
$$

where

$$
a_L=\lambda s/(1-\lambda)=(C_0+C_2+1-\rho)/(1-\lambda)
$$

and

$$
a_U=\rho+\lambda s-t=C_0+\lambda.
$$

Therefore

$$
(1-\lambda)(a_U-a_L)=P-(\lambda C_0+C_2),
$$

so

$$
\boxed{\ell_{50}=\left[(P-(\lambda C_0+C_2))/(1-\lambda)\right]_+.}
$$

This term is zero in the CE1 case and positive in the CE2 case.

Let $d_i$ be the length of $T_C\cap[O,V_i]$. Parameterize each radial arm by distance $q$ from $O$ toward the corresponding vertex. Direct substitution into $F_0,F_1,F_2$ gives

$$
d_0=1-\lambda s=\rho-C_0-C_2,
$$

$$
d_1\le C_2/\lambda,
$$

$$
d_2\le C_2,
$$

$$
d_3\le\min(C_0/\lambda,C_2/(1-\lambda)),
$$

$$
d_4\le C_0,
$$

$$
d_5\le C_0/(1-\lambda).
$$

For instance, on $[O,V_1]$ the side $F_2=0$ is reached after distance $C_2/\lambda$, and on $[O,V_3]$ the first exit is bounded by the smaller of the $F_0$ and $F_2$ exits.

Therefore

$$
L_S(T_C)\le \ell_{01}+\ell_{50}+d_0+d_1+d_2+d_3+d_4+d_5.
$$

Substitution and cancellation give

$$
L_S(T_C)\le K_\lambda-C_0/\lambda+C_0/(1-\lambda)+C_2+\min(C_0/\lambda,C_2/(1-\lambda))+\left[(P-(\lambda C_0+C_2))/(1-\lambda)\right]_+,
$$

where

$$
K_\lambda:=1-\lambda+\rho-(1-\rho)/\lambda.
$$

Set

$$
X=C_0,\qquad Y=C_2.
$$

Then

$$
X\ge0,\qquad Y\ge0,\qquad X+(1-\lambda)Y<P.
$$

Define

$$
\mathcal E(X,Y)=-X/\lambda+X/(1-\lambda)+Y+\min(X/\lambda,Y/(1-\lambda))+\left[(P-(\lambda X+Y))/(1-\lambda)\right]_+.
$$

We prove

$$
\mathcal E(X,Y)\le P/(1-\lambda).
$$

First suppose

$$
X/\lambda\le Y/(1-\lambda).
$$

Then

$$
(1-\lambda)X\le\lambda Y.
$$

The minimum is $X/\lambda$, so

$$
\mathcal E=X/(1-\lambda)+Y+[(P-(\lambda X+Y))/(1-\lambda)]_+.
$$

If the positive part is zero, then

$$
\mathcal E=(X+(1-\lambda)Y)/(1-\lambda)<P/(1-\lambda).
$$

If the positive part is positive, then

$$
\mathcal E=(P+(1-\lambda)X-\lambda Y)/(1-\lambda)\le P/(1-\lambda).
$$

Now suppose

$$
X/\lambda\ge Y/(1-\lambda).
$$

Then

$$
Y\le(1-\lambda)X/\lambda.
$$

The minimum is $Y/(1-\lambda)$. If the positive part is zero, then

$$
\mathcal E=-X/\lambda+X/(1-\lambda)+Y+Y/(1-\lambda).
$$

Since

$$
-X/\lambda+Y/(1-\lambda)\le0,
$$

we get

$$
\mathcal E\le X/(1-\lambda)+Y=(X+(1-\lambda)Y)/(1-\lambda)<P/(1-\lambda).
$$

If the positive part is positive, then

$$
\mathcal E=P/(1-\lambda)+Y-(1-\lambda)X/\lambda\le P/(1-\lambda).
$$

Thus in all cases

$$
\mathcal E(X,Y)\le P/(1-\lambda).
$$

Therefore

$$
L_S(T_C)\le K_\lambda+P/(1-\lambda).
$$

The inequality is strict in the nondegenerate CE1/CE2 branch because $s<t$ gives $X+(1-\lambda)Y<P$.

It remains to prove

$$
K_\lambda+P/(1-\lambda)<3/2.
$$

Using $P=\rho(1-\rho)$,

$$
K_\lambda+P/(1-\lambda)=1-\lambda+\rho-(1-\rho)/\lambda+\rho(1-\rho)/(1-\lambda).
$$

A direct simplification gives

$$
3/2-(K_\lambda+P/(1-\lambda))=\frac{2+\lambda-\lambda^2-2\rho(1+\lambda-\lambda^2)}{2\lambda(1-\lambda)}.
$$

Let

$$
A=1+\lambda-\lambda^2.
$$

The numerator is

$$
1+A-2\rho A.
$$

Both sides in the comparison $1+A>2\rho A$ are positive, so it is enough to square. We compute

$$
(1+A)^2-4A^2\rho^2=\lambda^2(1-\lambda)^2(5+4\lambda-4\lambda^2).
$$

For $0<\lambda<1$, this is positive. Hence

$$
1+A>2\rho A.
$$

Therefore

$$
K_\lambda+P/(1-\lambda)<3/2.
$$

Consequently

$$
L_S(T_C)<3/2.
$$

$$
\Box
$$

---

## Lemma 4: Vd1, Vd2, and T3-like skeleton caps follow from Lemma 3

Every $V_i$-triangle of type Vd1, Vd2, or T3-like satisfies

$$
L_S(T_i)<3/2.
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

Since $T_0$ contains $V_0=\widetilde O$, it is a center triangle for $\widetilde H$.

If $T_0$ is Vd1, Vd2, or T3-like, then $T_0$ has positive-length intersection with at least one of the adjacent rays

$$
[O,V_1]\quad\text{or}\quad[O,V_5].
$$

These are boundary edges of $\widetilde H$. Hence, viewed as a center triangle for $\widetilde H$, $T_0$ has positive-length overlap with at least one boundary edge of $\widetilde H$.

A unit equilateral triangle cannot have positive-length overlap with three boundary edges of a regular side-$1$ hexagon. Among any three boundary edges, two contain positive-length subsegments whose mutual distance is strictly greater than $1$, while a unit equilateral triangle has diameter $1$. Therefore $T_0$, viewed in $\widetilde H$, is CE1 or CE2.

By the CE1/CE2 exact-one-midpoint lemma applied to $\widetilde H$, the triangle $T_0$ covers exactly one radial midpoint of $\widetilde H$. By dihedral symmetry of $\widetilde H$, Lemma 3 applies to this translated CE1/CE2 configuration. Hence

$$
L_{\widetilde S}(T_0)<3/2.
$$

Finally, a unit triangle containing $V_0$ can meet the original skeleton $S$ in positive length only on the five local components

$$
[V_0,V_1],\quad [V_0,V_5],\quad [O,V_1],\quad [O,V_0],\quad [O,V_5].
$$

All five are contained in $\widetilde S$. Therefore

$$
L_S(T_0)\le L_{\widetilde S}(T_0)<3/2.
$$

By rotation symmetry, the same holds for every $V_i$-triangle of type Vd1, Vd2, or T3-like.

$$
\Box
$$

---

## Lemma 5: Vd0 with $a_i+b_i\le1$ has skeleton length at most $2$

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

## Lemma 6: Supercritical $V_i$-triangles have skeleton length less than $3/2$

Let $T_i$ be a $V_i$-triangle and suppose

$$
a_i+b_i>1.
$$

Then

$$
L_S(T_i)<3/2.
$$

### Proof

By rotational symmetry, normalize to $i=0$. Write

$$
a=a_0,\qquad b=b_0.
$$

Since $a+b>1$, $T_0$ has no adjacent-ray contribution. Thus its skeleton contribution is

$$
L_S(T_0)=a+b+c,
$$

where $c$ is the length of its intersection with its own radial arm $[O,V_0]$.

We prove

$$
a+b+c<3/2.
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
c\le1/2.
$$

Set

$$
s=a+b,\qquad d=b-a.
$$

Then

$$
a=(s-d)/2,\qquad b=(s+d)/2.
$$

The feasible range is

$$
1<s\le2/\sqrt3,
$$

and

$$
0\le d\le\sqrt{4-3s^2}.
$$

Let

$$
c_0=3/2-s.
$$

It is enough to prove that

$$
P(c)=(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)
$$

is nonnegative at $c=c_0$. Since

$$
P(0)=b^4-b^2<0,
$$

the first positive root of $P$ is then at most $c_0$, so $c\le c_0$.

Substituting $c_0=3/2-s$ and multiplying by $16$ gives

$$
Q(s,d)=d^4+8d^3s-6d^3+14d^2s^2-18d^2s+5d^2-8ds^3+30ds^2-34ds+12d+s^4-6s^3-19s^2+60s-36.
$$

Differentiate with respect to $d$:

$$
\partial Q/\partial d=2(2d+4s-3)(d^2+4ds-3d-s^2+3s-2).
$$

Since $s\ge1$ and $d\ge0$, the first factor is positive. For the second factor,

$$
d^2+4ds-3d-s^2+3s-2=d^2+d(4s-3)+(s-1)(2-s).
$$

On $1<s\le2/\sqrt3<2$, every term is nonnegative. Hence

$$
\partial Q/\partial d\ge0.
$$

So $Q(s,d)$ is increasing in $d$, and

$$
Q(s,d)\ge Q(s,0).
$$

Now

$$
Q(s,0)=(s-1)(s^3-5s^2-24s+36).
$$

The first factor is positive. Let

$$
g(s)=s^3-5s^2-24s+36.
$$

Then

$$
g'(s)=3s^2-10s-24<0
$$

on $1\le s\le2/\sqrt3$. Therefore $g$ is decreasing, and its minimum is at $s=2/\sqrt3$. There,

$$
g(2/\sqrt3)=88/3-(136\sqrt3)/9>0.
$$

Thus $Q(s,d)>0$ throughout the feasible region. Hence

$$
P(c_0)\ge0,
$$

so

$$
c\le c_0=3/2-a-b.
$$

Therefore

$$
a+b+c\le3/2.
$$

Equality can occur only in the limiting degenerate case $a+b\to1^+$. Since $a+b>1$, the inequality is strict:

$$
a+b+c<3/2.
$$

Thus

$$
L_S(T_0)<3/2.
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

Then

$$
T_C,T_0,\dots,T_5
$$

cannot cover the skeleton $S$.

### Proof

By Lemma 2, since at least two $V_i$-triangles are supercritical, at least one $V_i$-triangle is Vd1, Vd2, or T3-like.

By Lemma 4, every Vd1, Vd2, or T3-like triangle satisfies

$$
L_S(T_i)<3/2.
$$

By Lemma 6, every supercritical $V_i$-triangle satisfies

$$
L_S(T_i)<3/2.
$$

The remaining ordinary Vd0 triangles with $a_i+b_i\le1$ satisfy, by Lemma 5,

$$
L_S(T_i)\le2.
$$

The center triangle satisfies, by Lemma 3,

$$
L_S(T_C)<3/2.
$$

The worst possible skeleton-length upper bound occurs when there are exactly:

- two supercritical $V$-triangles;
- one Vd1/Vd2/T3-like rescuer;
- three ordinary Vd0 non-supercritical triangles.

Therefore

$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<3/2+2\cdot(3/2)+3/2+3\cdot2.
$$

The right-hand side is

$$
3/2+3+3/2+6=12.
$$

Thus

$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<12.
$$

But if the seven triangles covered $S$, then by subadditivity of length,

$$
12=\mathcal H^1(S)\le L_S(T_C)+\sum_{i=0}^5L_S(T_i).
$$

This is a contradiction. Hence the skeleton $S$ is not covered.

$$
\Box
$$
