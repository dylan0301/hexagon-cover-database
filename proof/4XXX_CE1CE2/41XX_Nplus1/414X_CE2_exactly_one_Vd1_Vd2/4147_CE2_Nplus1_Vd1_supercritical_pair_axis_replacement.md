# CE2 Vd1--Supercritical Adjacent-Pair Axis Replacement

Status: Proven

This note proves the Vd1 replacement used in the Case-3 branch of
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).
The Vd2 alternative is eliminated by
[`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md).

## Statement

Assume the original open roles cover the perimeter and radial skeleton in the
complementary 414X branch. Let $T_i$, $i\ne0$, be the unique supercritical
row, and let the unique Vd1 row, distinct from $T_0$ and adjacent to $T_i$,
contain $M_i$. Assume every other vertex row is nonsupercritical Vd0 and the
center has no boundary trace on the shared edge of this pair.

Then the Vd1--supercritical pair can be replaced by two open
nonsupercritical Vd0 roles while preserving every boundary and radial demand
used by the proved `4013` all-Vd0 boundary-loss package. The reflected
placement is identical.

## 1. Normalization and Vd1 margins

Normalize the Vd1 row at $V_0$, the supercritical row at $V_1$, and the
rescued midpoint as $M_1$. Let $a,b$ be the Vd1 row's exact incident-edge
reaches. By the Vd corner normal form, there are $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that the row is

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

Its own-radial reach and its neighboring-arm endpoints are

$$
c=\frac{d-a-tb}{t+1},
\qquad
\lambda=\frac{t(1-b)}{t+1},
\qquad
\mu=\frac{d-a-tb-1}{t},
$$

where the neighboring-arm coordinate runs from $V_1$ toward $O$.

Because the original open Vd1 role contains $M_1$, its closure satisfies,
with strict margin,

$$
b>\frac{t-1}{2t},
\qquad
a+tb<d-1-\frac t2.
$$

The row has no positive-length trace on the other adjacent arm. If $t<1$,
then

$$
d-a-tb-t>1-\frac t2>\frac1{t+1}>\frac{1-a}{t+1},
$$

which would create such a trace. Hence

$$
\boxed{t\ge1.}
$$

We need the four strict margins

$$
\boxed{
a+c<1,
\qquad
a<\lambda\le\frac12,
\qquad
b<\frac12,
\qquad
\mu<1-a.}
\tag{1}
$$

For $a+c<1$, maximize $a+c$ on the closed midpoint face
$a=d-1-t/2-tb$. There

$$
a+c-1
=-\frac{2bt^2+2bt-2dt-2d+t^2+4t+2}{2(t+1)}.
$$

Using $b\ge(t-1)/(2t)$, the numerator is at least

$$
2t^2+4t+1-2(t+1)d.
$$

This is positive for $t\ge1$, because

$$
(2t^2+4t+1)^2-4(t+1)^2d^2
=4t^3+4t^2-4t-3>0.
$$

The original midpoint inequalities are strict, so $a+c<1$.

The bound $\lambda\le1/2$ follows from the lower bound for $b$. The closed
upper bound for $a$, subtracted from $\lambda$, is minimized at
$b=(t-1)/(2t)$ and equals $(t+1)-d>0$, so $a<\lambda$. Also

$$
b<\frac{d-1-t/2}{t}<\frac12
$$

because $d<t+1$. Finally,

$$
t(\mu+a-1)=d-(t+1)-tb+(t-1)a
\le t(d-t-1)<0.
$$

This proves (1).

## 2. The supercritical row and the half-square lemma

Let $A_i,B_i,C_i$ be the actual incoming, outgoing, and own-radial reaches of
the supercritical row. The center-free shared edge forces

$$
A_i\ge1-b>\frac12,
$$

and radial coverage up to the Vd1 interval forces

$$
C_i\ge\lambda.
$$

We use the following consequence of the exact admissible set.

### Half-square admissibility lemma

If $(x,y,z)$ is admissible and

$$
x\ge\frac12,
\qquad
0\le z\le\frac12,
$$

then

$$
\boxed{y\le1-z.}
$$

Suppose instead that $y>1-z$. Then $x+y>1$, so the selected supercritical
cell applies. In the ordered half $x\le y$, its necessary inequality is

$$
F(x,y,z):=(x^2-1)z^2+(2xy^2+y)z+y^4-y^2\le0.
$$

The function is nondecreasing in $x$. At $x=1/2$, its derivative in $y$ is

$$
4y^3-2y+2yz+z.
$$

This is increasing for $y\ge1-z$ and is positive at $y=1-z$. Hence

$$
F(x,y,z)>F\left(\frac12,1-z,z\right)
=\frac{z^2(2z-5)(2z-1)}4\ge0,
$$

a contradiction.

In the reflected half $y<x$, the necessary inequality is $F(y,x,z)\le0$.
Both arguments exceed $r=1-z$. On this quadrant $F$ is nondecreasing in both
arguments; the second partial derivative is bounded below by

$$
4r^2z+z+4r^3-2r=2-5z+4z^2>0.
$$

Therefore

$$
F(y,x,z)>F(r,r,z)=z(1-2z)\ge0,
$$

again a contradiction. This proves the lemma.

For a supercritical admissible row, the actual own-radial reach has
$C_i\le1/2$.
Applying the lemma gives

$$
B_i\le1-C_i\le1-\lambda.
$$

Since $a<\lambda$,

$$
\boxed{a+B_i<1.}
\tag{2}
$$

## 3. Center handoff

Let $d_i^C$ be the center reach on the rescued arm, measured from $O$ toward
$V_i$, and put

$$
c_i^{\rm req}=1-d_i^C.
$$

Only the center, the supercritical row, and the Vd1 row have positive
intervals on this arm. Open coverage at the center handoff forces

$$
c_i^{\rm req}<\max\{C_i,\mu\}.
$$

By the half-square lemma and (1),

$$
\max\{C_i,\mu\}
\le
\max\{1-B_i,1-a\}.
$$

The first comparison is strict, so together they give the strict bridge
margin

$$
\boxed{
c_i^{\rm req}<\max\{1-B_i,1-a\}.}
\tag{3}
$$

No unjustified strictness is needed in the second comparison.

## 4. Explicit open Vd0 replacements

For $0\le p\le1$, define

$$
\Delta_p^-=\operatorname{conv}\{(0,1-p),(1,1-p),(0,-p)\}
\qquad(0\le p\le1/2),
$$

and

$$
\Delta_p^+=\operatorname{conv}\{(p,0),(p,1),(p-1,0)\}
\qquad(1/2<p\le1).
$$

In the local metric these are unit equilateral triangles. Their two incident
reaches are $p,1-p$, their own-radial reach is respectively $1-p$ or $p$, and
they have no positive adjacent-arm support.

The strict inequalities (1)--(3) allow parameters

$$
a<p_1<p_2<1-B_i
$$

such that

$$
p_1<\frac12,
\qquad
1-p_1>c,
\qquad
\max\{p_2,1-p_2\}>c_i^{\rm req}.
$$

Choose $p_1$ close to $a$. For $p_2$, choose a point close to $a$ when the
right side of (3) is supplied by $1-a$, and close to $1-B_i$ when it is
supplied by $1-B_i$.

Define the physical-coordinate map

$$
X_{\mathrm{loc}}:\mathbb R^2\to\mathbb R^2,
\qquad
X_{\mathrm{loc}}(x,y)
:=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Choose

$$
0<\varepsilon<
\min\left\{
p_1-a, p_2-p_1, 1-B_i-p_2,
1-p_1-c, \max\{p_2,1-p_2\}-c_i^{\rm req}
\right\},
$$

and define

$$
T_0'
:=
X_{\mathrm{loc}}\left(
\mathrm{int}(\Delta_{p_1}^-)+(-\varepsilon,0)
\right),
$$

$$
T_1'
:=
\begin{cases}
X_{\mathrm{loc}}\left(
\mathrm{int}(\Delta_{p_2}^-)+(-\varepsilon,0)
\right),&p_2\le1/2,\\
X_{\mathrm{loc}}\left(
\mathrm{int}(\Delta_{p_2}^+)+(0,-\varepsilon)
\right),&p_2>1/2.
\end{cases}
$$

The closure of $T_0'$ has relevant reaches

$$
(p_1-\varepsilon,1-p_1,1-p_1).
$$

The closure of $T_1'$ has relevant reaches

$$
(p_2-\varepsilon,1-p_2,1-p_2)
$$

when $p_2\le1/2$, and

$$
(p_2,1-p_2-\varepsilon,p_2)
$$

when $p_2>1/2$. The first replacement still supplies at least $a$ and $c$;
the second supplies at least $B_i$ and $c_i^{\rm req}$. The shared open edge
is covered because

$$
(1-p_1)+(p_2-\varepsilon)>1.
$$

Both replacements contain their distinguished vertices in their interiors,
have zero adjacent support, and have boundary sum below one. Thus they are
open nonsupercritical Vd0 roles preserving all boundary and radial demands
used by `4013`. The resulting all-Vd0 datum is impossible.

$$
\Box
$$
