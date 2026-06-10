# Full T3-like Tangent-Envelope Conjecture

Status: Lemma target

This file states the local no-midpoint T3-like area envelope used by the CE0
one-supercritical certificate in this folder.

No midpoint condition is imposed.  A local triangle may contain none, one, two,
or three of the local midpoints.  The only local type condition is

$$
(o,n)=(2,1).
$$

This file does not prove the envelope.  It gives the exact tangent branch that
experiments identify as the local supremal envelope, derives its formulas, and
states the conjecture in the form needed by the global proof.

## Local coordinates

Normalize to $V_0$.  Use the triangular basis $V_0,V_1$, where

$$
V_5=V_0-V_1.
$$

The two boundary points adjacent to $V_0$ are

$$
P_A=e_{5,0}(A)=V_0+A(V_5-V_0)=V_0-AV_1,
$$

and

$$
P_B=e_{0,1}(B)=V_0+B(V_1-V_0)=(1-B)V_0+BV_1.
$$

The upper tangent branch has a limiting vertex on the adjacent ray $r_1$:

$$
S=sV_1,
\qquad 0\le s\le\frac12.
$$

The branch is the limiting configuration in which:

1. the two sides through $S$ pass through $P_A$ and $P_B$;
2. the opposite side of the unit equilateral triangle passes through $V_0$;
3. the triangle is tangent to the adjacent ray $r_1$.

The reflected lower branch is obtained by swapping $A$ and $B$.

## Branch equations

Let

$$
u=P_A-S=V_0-(A+s)V_1,
$$

and

$$
v=P_B-S=(1-B)V_0+(B-s)V_1.
$$

In the triangular basis, the Euclidean inner product is determined by

$$
V_0\cdot V_0=1,
\qquad
V_1\cdot V_1=1,
\qquad
V_0\cdot V_1=\frac12.
$$

The condition that the two side rays from $S$ meet at angle $60^\circ$ gives

$$
4(u\cdot v)^2=|u|^2|v|^2,
\qquad
u\cdot v>0.
$$

Expanding and taking the observed T3-like tangent branch gives

$$
As-A-B+s^2-s+1=0.
$$

Equivalently,

$$
B=(1-A)(1-s)+s^2.
$$

The condition that the opposite side of the unit equilateral triangle passes
through $V_0$ gives

$$
A(1-s^2)=s(s^2-s+1).
$$

Therefore

$$
\boxed{
A(s)=\frac{s(s^2-s+1)}{1-s^2}
}
$$

and

$$
\boxed{
B(s)=\frac{s^2-s+1}{1+s}.
}
$$

The parameter range $0\le s\le1/2$ is exactly the range in which the upper
branch runs from the axis endpoint $(A,B)=(0,1)$ to the symmetric endpoint
$(A,B)=(1/2,1/2)$.

## Area of the tangent branch

The part of the tangent limiting triangle inside $H$ is the quadrilateral

$$
V_0P_BSP_A.
$$

Using the coordinates above, its Euclidean area is

$$
\frac{\sqrt3}{4}\bigl(A+B-Bs\bigr).
$$

Since a unit equilateral triangle has area $\sqrt3/4$, the normalized inside
area of the branch is

$$
F(s)=A(s)+B(s)-B(s)s.
$$

Substituting the formulas for $A(s)$ and $B(s)$ gives

$$
\boxed{
F(s)=\frac{(s^2-s+1)^2}{1-s^2}.
}
$$

The reflected branch is

$$
(B(s),A(s),F(s)).
$$

## Tangent-envelope conjecture

Define the full no-midpoint T3-like local inside-area function by

$$
f_{\mathrm{T3}}(a,b)=
\sup_T \frac{\operatorname{area}(T\cap H)}{\sqrt3/4},
$$

where the supremum is over closed unit equilateral $V_0$-triangles satisfying

$$
(o,n)=(2,1),
$$

and containing the required local boundary points

$$
V_0,
\qquad
 e_{5,0}(a),
\qquad
 e_{0,1}(b).
$$

No midpoint condition is imposed in this definition.

The conjectural envelope is:

$$
\boxed{
\begin{aligned}
f_{\mathrm{T3}}(a,b)
\le
\sup\{F(s):&\ 0\le s\le1/2,\\
& A(s)\ge a,\ B(s)\ge b\}
\\
{}\vee{}
\sup\{F(s):&\ 0\le s\le1/2,\\
& B(s)\ge a,\ A(s)\ge b\}.
\end{aligned}
}
$$

Here $\vee$ means the maximum of the two reflected quantities.  Empty suprema
are ignored.

Equivalently, every T3-like local triangle with required lower-bound data
$(a,b)$ and normalized inside area $F_T$ is conjectured to be dominated by one
of the two tangent branches: there exists $s\in[0,1/2]$ such that either

$$
A(s)\ge a,
\qquad
B(s)\ge b,
\qquad
F_T\le F(s),
$$

or

$$
B(s)\ge a,
\qquad
A(s)\ge b,
\qquad
F_T\le F(s).
$$

## Non-claim

This file does not prove that the tangent branch is the full T3-like envelope.
The conjecture is the remaining local proof obligation for the T3-like area
package.  The subsequent files prove rigorous consequences assuming this local
input.