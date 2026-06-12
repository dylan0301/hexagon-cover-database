# Neighbor-Ray Maximum $c$ Formula

Status: Proven local lemma

This file records the adjacent-ray maximum for a normalized $V_0$-triangle. It is separate from [`2004_admissible_set.md`](2004_admissible_set.md): that file concerns the local radial coordinate on $[V_0,O]$, while this file concerns the neighboring radial point $(1-c)V_1$ on $r_1$.

## 1. Target

Work in the normalized $V_0$ picture. Let

$$
A_a=e_{5,0}(a),\qquad B_b=e_{0,1}(b),\qquad X_c=(1-c)V_1,
$$

where $0\le a,b,c\le 1$. Define

$$
C_+(a,b)=\max\{c\in[0,1]:\text{there is a closed unit equilateral }V_0\text{-triangle }T_0\text{ with }V_0,A_a,B_b,X_c\in T_0\}.
$$

If the set is empty, $C_+(a,b)$ is called undefined. The lower-neighbor function is

$$
C_-(a,b)=C_+(b,a).
$$

Thus the two adjacent-ray capacities are

$$
(c_{i\to i-1}(a,b),c_{i\to i+1}(a,b))=(C_+(b,a),C_+(a,b)).
$$

Containment of $A_a$ and $B_b$ is equivalent, by convexity and the fixed containment of $V_0$, to containing the adjacent edge intervals $e_{5,0}([0,a])$ and $e_{0,1}([0,b])$.

## 2. Formula

Let

$$
f_a(x)=x^3-(a+2)x^2+2(a+1)x-1.
$$

For $0\le a\le 1/2$, let $p(a)$ be the unique root of $f_a(x)=0$ in $[a,1]$. Define

$$
\sigma(a)=1-p(a),\qquad \tau(a)=1-a-(p(a)-a)(1-p(a)).
$$

Then

$$
C_+(a,b)=\begin{cases}\text{undefined},&a+b>1,\\1-b,&a+b\le1\text{ and }a>1/2,\\1-b,&0\le a\le1/2\text{ and }0\le b\le\sigma(a),\\p(a),&0\le a\le1/2\text{ and }\sigma(a)\le b\le\tau(a),\\a+1/2-\sqrt{(a+b)^2-3/4},&0\le a\le1/2\text{ and }\tau(a)<b\le1-a.\end{cases}
$$

At $b=\tau(a)$, the value is the plateau value $p(a)$, even though the last displayed expression may also define a feasible but dominated triangle.

## 3. Cone coordinates and exact semialgebraic constraints

Put the origin at $V_0$ and use the cone basis

$$
E_-=V_5-V_0,\qquad E_+=V_1-V_0.
$$

Thus a point is written as $uE_-+vE_+$. The metric is

$$
\|uE_-+vE_+\|^2=u^2+v^2-uv.
$$

In these coordinates,

$$
V_0=(0,0),\qquad A_a=(a,0),\qquad B_b=(0,b),\qquad X_c=(c,1).
$$

Let $R,S\in\mathbb R$ satisfy

$$
R^2+S^2-RS=1.
$$

Set

$$
P=RE_-+SE_+,\qquad Q=SE_-+(S-R)E_+.
$$

Then $P$ and $Q$ are unit vectors with angle $60^\circ$. Write each point $Y=(u,v)$ uniquely as $Y=U(Y)P+V(Y)Q$, and set $W(Y)=U(Y)+V(Y)$. Direct inversion gives

$$
U(u,v)=(R-S)u+Sv,\qquad V(u,v)=Su-Rv,\qquad W(u,v)=Ru+(S-R)v.
$$

For the four points $O=(0,0)$, $A=(a,0)$, $B=(0,b)$, and $X=(c,1)$, the support coordinates are:

| point | $U$ | $V$ | $W$ |
|---|---:|---:|---:|
| $O$ | $0$ | $0$ | $0$ |
| $A$ | $(R-S)a$ | $Sa$ | $Ra$ |
| $B$ | $Sb$ | $-Rb$ | $(S-R)b$ |
| $X$ | $(R-S)c+S$ | $Sc-R$ | $Rc+S-R$ |

For a fixed orientation $(R,S)$, a translate of the unit equilateral triangle with side directions $P,Q$ is described by

$$
U\ge u_0,\qquad V\ge v_0,\qquad W\le w_0,\qquad w_0-u_0-v_0=1.
$$

Therefore the four points fit in such a triangle if and only if

$$
\max_Y W(Y)-\min_Y U(Y)-\min_Y V(Y)\le1.
$$

Equivalently, the exact semialgebraic feasibility condition is the existence of $R,S$ with $R^2+S^2-RS=1$ such that

$$
W(Y_k)-U(Y_i)-V(Y_j)\le1\qquad\text{for all }Y_i,Y_j,Y_k\in\{O,A,B,X\}.
$$

This is the finite system used below.

## 4. Active-support reduction

Let $Q(a,b,c)=\mathrm{conv}\{O,A,X,B\}$. For $a,b,c$ away from the obvious zero-length degeneracies, this is the convex quadrilateral with cyclic vertices $O,A,X,B$.

A boundary value of $C_+(a,b)$ is attained by a unit equilateral triangle whose support lines have one of the following non-dominated active patterns:

| pattern | active support equations | candidate value |
|---|---|---:|
| $OA$ and $BX$ supported | $R=S=1$ and $V(B)=V(X)$ | $c=1-b$ |
| $AX$ supported, $B$ inactive | $V(A)=V(X)$ and $W(X)=-1$ | $c=p(a)$ |
| $AX$ supported, $B$ active | $V(A)=V(X)$ and $-U(B)-V(A)=1$ | $c=a+1/2-\sqrt{(a+b)^2-3/4}$ |

Proof of reduction. For a fixed orientation, the minimal side length enclosing the four points is

$$
L_{R,S}(a,b,c)=\max_Y W(Y)-\min_Y U(Y)-\min_Y V(Y).
$$

At a maximal feasible $c$, one has $\min_{R,S}L_{R,S}(a,b,c)=1$. If a minimizing support triangle had no side containing an edge of $Q(a,b,c)$, then all active contacts would be isolated vertices. A sufficiently small rotation of the three support directions about the active contacts preserves containment of the fixed points $O,A,B$ to first order and moves the side through $X$ in the positive $c$ direction, unless two adjacent vertices of $Q(a,b,c)$ already lie on a common support side. Hence a non-dominated boundary triangle has a support side containing one of the hull edges $OA$, $AX$, $XB$, or $BO$.

Substitution of the four edge-contact possibilities into the finite system in Section 3 gives the displayed table. The edge $OA$ gives $R=S=\pm1$; only $R=S=1$ can contain $X_c$ with $c\ge0$ without increasing the side length above $1$, and the additional contact $V(B)=V(X)$ gives $c=1-b$. The edge $XB$ gives the same non-dominated solution after relabeling the two lower support sides. The edge $AX$ gives $V(A)=V(X)$, hence $R=S(c-a)$, and splits according as the third lower support side is attained at $X$ or at $B$. The edge $BO$ gives only the reflected lower-neighbor cells or cells satisfying $c\le1-b$, so it is dominated for $C_+$. These substitutions exhaust the finite inequalities because each support side is one of $U=\text{constant}$, $V=\text{constant}$, or $W=\text{constant}$, and each hull edge has been assigned to each possible support side.

It remains to evaluate the three active patterns.

## 5. Pattern $OA/BX$

Take $R=S=1$. Then

$$
U(O)=U(A)=0,\qquad V(B)=-b,\qquad W(X)=c.
$$

The triangle

$$
U\ge0,\qquad V\ge-b,\qquad W\le c
$$

has side length $c+b$. It is a unit triangle exactly when $c+b=1$. Therefore the boundary value is

$$
c=1-b.
$$

The point $A$ is contained exactly when

$$
W(A)=a\le c=1-b.
$$

Thus this pattern is feasible exactly when $a+b\le1$, and it gives the candidate $1-b$.

## 6. Pattern $AX$ with $B$ inactive

Let

$$
d=c-a.
$$

The side through $A$ and $X$ is $V(A)=V(X)$, so

$$
Sa=Sc-R,\qquad\text{hence}\qquad R=Sd.
$$

The unit condition becomes

$$
S^2(d^2-d+1)=1.
$$

For the $B$-inactive pattern, the opposite support side is $W(O)=0$, and the lower vertex is $X$. Thus

$$
W(X)=-1.
$$

Since $W(X)=S(d(c-1)+1)$, elimination of $S$ gives

$$
(d(c-1)+1)^2=d^2-d+1.
$$

Using $d=c-a$, this factors as

$$
(c-a)(c^3-(a+2)c^2+2(a+1)c-1)=0.
$$

The factor $c=a$ is the degenerate endpoint already covered by the branch $c=1-b$ at $a+b=1$. The nondegenerate value is the root $c=p(a)$ of

$$
p^3-(a+2)p^2+2(a+1)p-1=0.
$$

For $0\le a\le1/2$, this root exists and is unique in $[a,1]$. Indeed,

$$
f_a(a)=2a-1\le0,\qquad f_a(1)=a\ge0,
$$

and

$$
f_a'(x)=3x^2-2(a+2)x+2(a+1)
$$

has discriminant

$$
4(a+2)^2-24(a+1)=4(a^2-2a-2)<0
$$

on $0\le a\le1/2$, so $f_a$ is strictly increasing.

It remains to impose the $B$-containment inequalities. With $c=p(a)$ and $d=p(a)-a$, the only nonautomatic one is

$$
U(B)\ge U(X).
$$

Since $S<0$, this is equivalent to

$$
b\le1-p(a)(1+a-p(a)).
$$

The right-hand side is

$$
1-p(a)(1+a-p(a))=1-a-(p(a)-a)(1-p(a))=\tau(a).
$$

Therefore this pattern is feasible exactly for $b\le\tau(a)$, and it gives the candidate $p(a)$.

The branch $p(a)$ dominates $1-b$ exactly when

$$
b\ge1-p(a)=\sigma(a).
$$

Thus the plateau branch is maximal on $\sigma(a)\le b\le\tau(a)$.

## 7. Pattern $AX$ with $B$ active

Again write $d=c-a$, so $R=Sd$. In this pattern the active support sides are

$$
W(O)=0,\qquad V(A)=V(X),\qquad U(B)\text{ active}.
$$

The side-length equation is

$$
0-U(B)-V(A)=1.
$$

Since $U(B)=Sb$ and $V(A)=Sa$, this gives

$$
-S(a+b)=1,\qquad\text{so}\qquad S=-\frac1{a+b}.
$$

The unit condition now gives

$$
d^2-d+1=(a+b)^2.
$$

The valid upper-neighbor branch has $0\le d\le1/2$, hence

$$
d=\frac{1-\sqrt{4(a+b)^2-3}}2.
$$

Therefore

$$
c=a+d=a+\frac12-\sqrt{(a+b)^2-\frac34}.
$$

This candidate is real exactly when

$$
a+b\ge\frac{\sqrt3}{2}.
$$

On the final branch below, this condition is automatic. To see this, solve the cubic relation for $a$ in terms of $p=p(a)$:

$$
a=\frac{(1-p)(p^2-p+1)}{p(2-p)}.
$$

Then

$$
a+\tau(a)=\frac{p^2-p+1}{p(2-p)}.
$$

The function $(p^2-p+1)/(p(2-p))$ on $1/2\le p\le1$ has derivative $(p^2+2p-2)/(p^2(p-2)^2)$ and minimum $\sqrt3/2$ at $p=\sqrt3-1$. Hence $b>\tau(a)$ implies $a+b>\sqrt3/2$.

The nonactive containment inequalities reduce to

$$
0\le a\le\frac12,\qquad b\le1-a,\qquad b\ge\tau(a).
$$

Indeed, after substituting $S=-1/(a+b)$ and $d=(1-\sqrt{4(a+b)^2-3})/2$, the only nonautomatic inequality is $U(X)\ge U(B)$, which is equivalent to $b\ge1-c(1+a-c)$. On the interval $b\ge\tau(a)$ this follows by the preceding $p$-parameterization, and equality occurs at $b=1-a$ and, when $a\ge\sqrt3-3/2$, also at $b=\tau(a)$.

Thus this pattern gives the candidate

$$
a+\frac12-\sqrt{(a+b)^2-\frac34}
$$

for $0\le a\le1/2$ and $\tau(a)<b\le1-a$.

It dominates the $OA/BX$ candidate on this interval. Let $s=a+b$. Since $\sqrt3/2\le s\le1$,

$$
\left(a+\frac12-\sqrt{s^2-\frac34}\right)-(1-b)=s-\frac12-\sqrt{s^2-\frac34}\ge0,
$$

because both sides are nonnegative and

$$
\left(s-\frac12\right)^2-\left(s^2-\frac34\right)=1-s\ge0.
$$

## 8. Completion of the proof

First suppose $a+b>1$. Every non-dominated active pattern listed in Section 4 requires $a+b\le1$. Hence no point $X_c$ with $0\le c\le1$ can be contained together with $V_0,A_a,B_b$ in a unit equilateral $V_0$-triangle, and $C_+(a,b)$ is undefined.

Now suppose $a+b\le1$.

If $a>1/2$, then the $AX$ branches are not valid: the cubic branch has no root in $[a,1]$, and the active-$B$ branch fails the inequality $U(X)\ge U(B)$. The only non-dominated candidate is therefore $1-b$.

If $0\le a\le1/2$, then the three candidates are ordered as follows. Since

$$
\tau(a)-\sigma(a)=(p(a)-a)p(a)\ge0,
$$

and

$$
\tau(a)\le1-a,
$$

all three intervals in the formula are ordered correctly. For $b\le\sigma(a)$, one has $1-b\ge p(a)$, so the $OA/BX$ value is maximal. For $\sigma(a)\le b\le\tau(a)$, the plateau value $p(a)$ is feasible and dominates $1-b$. For $b>\tau(a)$, the plateau pattern is infeasible and the active-$B$ branch is feasible; by Section 7 it dominates $1-b$. This proves the displayed formula for $C_+(a,b)$.

Finally, reflection across the line $OV_0$ swaps $e_{5,0}$ with $e_{0,1}$ and swaps $r_5$ with $r_1$. Therefore

$$
C_-(a,b)=C_+(b,a).
$$

## 9. Boundary cases and degeneracies

If $a=0$, then $p(0)=1$, $\sigma(0)=0$, and $\tau(0)=1$. Hence

$$
C_+(0,b)=1\qquad(0\le b\le1).
$$

If $a=1/2$, then $p(1/2)=1/2$ and $\sigma(1/2)=\tau(1/2)=1/2$. The formula collapses to

$$
C_+(1/2,b)=1-b\qquad(0\le b\le1/2).
$$

At $b=\tau(a)$, the plateau value $p(a)$ is feasible and is the maximal value. The right-hand branch may have a smaller one-sided limit. The jump occurs exactly for

$$
0\le a<\sqrt3-\frac32.
$$

For $a\ge\sqrt3-3/2$, the right-hand branch is continuous at $b=\tau(a)$.

At $b=1-a$, the upper-neighbor value is

$$
C_+(a,1-a)=a.
$$

When $a+b>1$, the function is undefined rather than zero: $c=0$ would mean the endpoint $V_1$, and even that point is not feasible together with the prescribed $A_a$ and $B_b$.

## 10. Independent numerical verification

The symbolic proof above does not depend on numerical optimization. The following independent check samples orientations and compares the numerical frontier against the closed formula.

```python
import math
import numpy as np


def support_length(a, b, c, theta):
    R = -math.cos(theta) - math.sin(theta) / math.sqrt(3)
    S = -math.cos(theta) + math.sin(theta) / math.sqrt(3)
    U = [0.0, (R - S) * a, S * b, (R - S) * c + S]
    V = [0.0, S * a, -R * b, S * c - R]
    W = [0.0, R * a, (S - R) * b, R * c + S - R]
    return max(W) - min(U) - min(V)


def feasible(a, b, c, n=20000):
    vals = [support_length(a, b, c, 2 * math.pi * k / n) for k in range(n)]
    return min(vals) <= 1.0 + 1e-8
```

A verification run should test a grid in $0\le a,b\le1$ and, for each formula value $C_+(a,b)$, check:

- if $C_+(a,b)$ is defined, then `feasible(a,b,C_+(a,b))` is true;
- if $C_+(a,b)+\varepsilon\le1$, then `feasible(a,b,C_+(a,b)+\varepsilon)` is false for small positive $\varepsilon$;
- if $a+b>1$, then no sampled $c\in[0,1]$ is feasible;
- the active contacts match the three support patterns in Sections 5, 6, and 7.

Evidence of an error would be any sampled feasible point with $c>C_+(a,b)+10^{-6}$, any sampled infeasibility at the displayed formula value, or any new non-dominated active support pattern not represented in the table in Section 4.
