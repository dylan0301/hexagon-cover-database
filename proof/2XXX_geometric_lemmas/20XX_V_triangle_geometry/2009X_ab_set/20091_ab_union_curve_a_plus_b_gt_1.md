# Strict Supercritical $AB$-Union Target

Status: Lemma target

Let $A,O,B$ be three points with angle $120^\circ$ at $O$. Put

$$
A=ae_A,\qquad B=be_B,
$$

where $e_A$ and $e_B$ are unit directions with angle $120^\circ$, and let

$$
C=\{ue_A+ve_B:u\ge0,\ v\ge0\}.
$$

The local $AB$-union set is

$$
\mathcal U_{AB}(a,b)=C\cap\bigcup\{T:T\text{ is a closed unit equilateral triangle and }O,A,B\in T\}.
$$

If no such triangle exists, this union is empty.

This note records the candidate exact non-axis frontier of
$\mathcal U_{AB}(a,b)$ in cone coordinates.  It is the strict
$\sigma=a+b>1$, $R^2<1$ specialization of Band IV in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md), but the proof
attempt below is independent of the unresolved general case catalog.  In the
notation below, $\rho=R^2$.  Numerical tests strongly support the formula, but
the support-pattern exhaustion described after equation (5) is not yet proved;
one formerly asserted intermediate equivalence is false.  The formula must
therefore not be used as a proved theorem.

## Target statement

Assume the strict branch

$$
a+b>1, \qquad \rho=a^2+ab+b^2<1.
$$

Work in cone coordinates

$$
x=ue_A+ve_B, \qquad u\ge0, \qquad v\ge0,
$$

where $e_A$ and $e_B$ are unit directions with angle $120^\circ$.  The metric is

$$
\lVert ue_A+ve_B\rVert^2=u^2+v^2-uv.
$$

Let

$$
A=(a,0), \qquad B=(0,b), \qquad h=\frac{\sqrt3}{2}, \qquad D=\sqrt{4\rho-3}.
$$

Define

$$
\alpha=\frac{h(a+2b-aD)}{2\rho}, \qquad \beta=\frac{h(a-b+(a+b)D)}{2\rho},
$$

$$
\gamma=\frac{h(-a+b+(a+b)D)}{2\rho}, \qquad \delta=\frac{h(2a+b-bD)}{2\rho},
$$

and

$$
\Omega=\alpha\delta-\gamma\beta= \frac{3(1-D)(D+3)}{16\rho}>0.
$$

Define the two closed unit disks

$$
\mathcal D_A=\left\{(u,v):(u-a)^2+v^2-(u-a)v\le1\right\},
$$

$$
\mathcal D_B=\left\{(u,v):u^2+(v-b)^2-u(v-b)\le1\right\},
$$

and the two half-planes

$$
\mathcal H_A=\left\{(u,v):\alpha(u-a)+\beta v\le0\right\},
\qquad
\mathcal H_B=\left\{(u,v):\gamma u+\delta(v-b)\le0\right\}.
$$

Then the whole union set, not only its frontier, has the exact description

$$
\boxed{
\mathcal U_{AB}(a,b)
=
\left(C\cap\mathcal D_A\cap\mathcal H_A\right)
\mathbin\cup
\left(C\cap\mathcal D_B\cap\mathcal H_B\right).
}
\tag{1}
$$

The five junction points are

$$
P_0=\left(0,\frac{-a+\sqrt{4-3a^2}}{2}\right),
$$

$$
P_1=\left(a-\frac{\beta}{h},\frac{\alpha}{h}\right),
$$

$$
P_2=\left( \frac{\delta(a\alpha-b\beta)}{\Omega}, \frac{\alpha(b\delta-a\gamma)}{\Omega} \right),
$$

$$
P_3=\left(\frac{\delta}{h},b-\frac{\gamma}{h}\right),
$$

$$
P_4=\left(\frac{-b+\sqrt{4-3b^2}}{2},0\right).
$$

The curve is ordered as

$$
P_0\to P_1\to P_2\to P_3\to P_4.
$$

It is the union of four pieces:

$$
\Gamma_{AB}=\Gamma_A^{\mathrm{circ}}\cup\Gamma_A^{\mathrm{lin}} \cup\Gamma_B^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{circ}}.
$$

The first piece is the circle arc centered at $A$:

$$
\Gamma_A^{\mathrm{circ}}: \quad (u-a)^2+v^2-(u-a)v=1,
$$

with branch

$$
v=\frac{u-a+\sqrt{4-3(u-a)^2}}{2}, \qquad 0\le u\le a-\frac{\beta}{h}.
$$

The second piece is the line segment from $P_1$ to $P_2$:

$$
\Gamma_A^{\mathrm{lin}}: \quad \alpha(u-a)+\beta v=0.
$$

Equivalently,

$$
v=\frac{\alpha}{\beta}(a-u).
$$

The third piece is the line segment from $P_2$ to $P_3$:

$$
\Gamma_B^{\mathrm{lin}}: \quad \gamma u+\delta(v-b)=0.
$$

Equivalently,

$$
v=b-\frac{\gamma}{\delta}u.
$$

The fourth piece is the circle arc centered at $B$:

$$
\Gamma_B^{\mathrm{circ}}: \quad u^2+(v-b)^2-u(v-b)=1,
$$

with branch

$$
v=b+\frac{u-\sqrt{4-3u^2}}{2}, \qquad \frac{-b+\sqrt{4-3b^2}}{2}\le u\le\frac{\delta}{h}.
$$

This last arc is traversed from $P_3$ to $P_4$, so $u$ decreases along the boundary orientation.

Thus the target asserts that the strict $a+b>1$ $AB$-union curve consists of
exactly two unit-circle arcs and two line segments.

The endpoint chord of each line piece coincides with the line piece itself.  It is neither above nor below the corresponding boundary piece.

## Partial derivation and open proof obligation

The fitting criterion and rotating-calipers reduction below are exact.  In the
four-vertex hull case they reduce the target to the two non-axis hull edges.
The subsequent calculation correctly handles one support sector, but that
sector is not exhaustive.  A concrete omitted support pattern is recorded
below, so the derivation stops short of proving (1).

### 1. Fitting function and an edge-normal minimum

For a compact set $S$ and a unit vector $n$, write

$$
h_S(n)=\max_{p\in S}\langle p,n\rangle.
$$

If $n_k(\varphi)=u(\varphi+120^\circ k)$, put

$$
G_S(\varphi)=\sum_{k=0}^2 h_S\left(n_k(\varphi)\right).
$$

The intersection of the three supporting half-planes

$$
\left\{y:\langle y,n_k(\varphi)\rangle
\le h_S\left(n_k(\varphi)\right),\ k=0,1,2\right\}
$$

is an equilateral triangle of side
$2G_S(\varphi)/\sqrt3$.  Indeed, the sum of the three support
numbers is translation-invariant because $n_0+n_1+n_2=0$, and three lines
with these normals enclose an equilateral triangle whose inradius is one
third of that sum.  Consequently

$$
S\text{ fits in a closed unit equilateral triangle}
\quad\Longleftrightarrow\quad
\min_\varphi G_S(\varphi)\le h.
\tag{2}
$$

We also need the following rotating-calipers observation.  If $Q$ is a convex
polygon, a minimum of $G_Q$ occurs at an orientation at which one of the three
support lines contains an edge of $Q$.  Between consecutive edge-normal
directions the three support vertices are fixed, so on such an interval

$$
G_Q(\varphi)=c\cos\varphi+d\sin\varphi,
\qquad
G_Q''(\varphi)=-G_Q(\varphi)<0.
$$

Thus an open support cell contains no local minimum.  Continuity supplies a
minimum at one of its endpoints, where a support face contains an edge.

### 2. The four possible hull edges

Let $x=ue_A+ve_B\in C$.  The triangle
$\triangle OAB$ is already contained in an equilateral triangle of side
$R=|AB|$: direct substitution at the normal of $AB$ gives
$G_{\{O,A,B\}}=hR$, while the diameter bound shows that no smaller side is
possible.  Since $R<1$, it is also contained in a unit equilateral triangle.
If $x\in\triangle OAB$, it is therefore in
$\mathcal U_{AB}(a,b)$; it also satisfies the right-hand side of (1), since
that right-hand side is convex on each displayed component and contains
$O,A,B$.  For the first component these containments follow from
$a<1$, $\rho<1$, and the exact line evaluations

$$
\alpha(0-a)+\beta 0=-\alpha a<0,
\qquad
\alpha(0-a)+\beta b
=\frac{h}{2}(D-1)<0;
$$

$A$ lies on the line.  Thus
$\triangle OAB\subset C\cap\mathcal D_A\cap\mathcal H_A$.

Suppose now that $x\notin\triangle OAB$, with $u,v>0$, no three of the four
points collinear, and all four points extreme in their convex hull.  The cyclic
order is

$$
O, B, x, A.
$$

The cases in which $A$ or $B$ is not a hull vertex require a separate
three-vertex support check and are included in the open partition obligation
below.

By the edge-normal observation, only the four hull edges $OB$, $Bx$, $xA$,
and $AO$ need be tested in (2).  The two axis edges cannot give a unit
triangle.  At the outward normal of $AO$, direct substitution of
$A=(a,0)$, $B=(0,b)$, and $x=(u,v)$ in cone coordinates gives

$$
\frac{G_Q}{h}
=
\max\{a,u\}+\max\{b,v-u\}
\ge a+b>1.
\tag{3}
$$

At the outward normal of $OB$ the mirror calculation gives

$$
\frac{G_Q}{h}
=
\max\{b,v\}+\max\{a,u-v\}
\ge a+b>1.
\tag{4}
$$

It remains to test $xA$ and $Bx$.  The following exact calculation covers one
support sector for $xA$; the reflected calculation covers the corresponding
sector for $Bx$.  Let $t=(x-A)/|x-A|$, let $n_0$ be the outward normal to
$xA$, and label the other normals counterclockwise as $n_1,n_2$.  In the
sector under consideration the supports are

$$
h_Q(n_0)=\langle A,n_0\rangle=\langle x,n_0\rangle,
\qquad
h_Q(n_1)=\langle A,n_1\rangle,
$$

$$
h_Q(n_2)=
\max\left\{\langle B,n_2\rangle,\langle x,n_2\rangle\right\}.
\tag{5}
$$

After the tie $A=x$ on $n_0$, the two support triples in this sector are

| support on $n_0$ | support on $n_1$ | support on $n_2$ |
|---|---|---|
| $A,x$ | $A$ | $x$ |
| $A,x$ | $A$ | $B$ |

and they are exactly (5).  They do **not** exhaust every $xA$ support pattern
that can meet the unit bound.  The following exact example disproves the
former two-row exhaustion.  Take

$$
a=\frac25,\qquad b=\frac{13}{20},\qquad
(u,v)=\left(\frac12,\frac1{20}\right).
$$

Then

$$
a+b=\frac{21}{20}>1,
\qquad
\rho=\frac{337}{400}<1.
$$

Also

$$
\frac{u}{a}+\frac{v}{b}=\frac{69}{52}>1,
$$

so $x\notin\triangle OAB$ as required in this part of the reduction.

In Cartesian coordinates with

$$
e_A=(1,0),\qquad e_B=\left(-\frac12,\frac{\sqrt3}{2}\right),
$$

the outward normal to $A\to x$ and its two $120^\circ$ rotations are

$$
n_0=\left(\frac12,-\frac{\sqrt3}{2}\right),\quad
n_1=\left(\frac12,\frac{\sqrt3}{2}\right),\quad
n_2=(-1,0).
$$

The support values on the ordered point list $O,A,B,x$ are

$$
\begin{array}{c|cccc}
&O&A&B&x\\
\hline
n_0&0&\frac15&-\frac{13}{20}&\frac15\\
n_1&0&\frac15&\frac{13}{40}&\frac{11}{40}\\
n_2&0&-\frac25&\frac{13}{40}&-\frac{19}{40}.
\end{array}
$$

Thus the support faces are $[A,x],B,B$, and

$$
G_Q=\frac15+\frac{13}{40}+\frac{13}{40}
=\frac{17}{20}<\frac{\sqrt3}{2}.
$$

This admissible $xA$ candidate is absent from the table.  It lies in
$\mathcal D_A$, because the defining quadratic equals $3/400$, but it lies
outside $\mathcal H_A$.  Indeed, after removing the positive common factor
$h/(2\rho)$, its half-plane expression is

$$
\frac{63}{400}+\frac{\sqrt{37}}{800}>0.
$$

On the other hand, its $\mathcal D_B$ quadratic is $91/100<1$, and the
corresponding unscaled $\mathcal H_B$ expression is

$$
-\frac{149}{200}+\frac{183\sqrt{37}}{2000}<0.
$$

The last sign is exact because

$$
183^2\cdot37=1239093<2220100=1490^2.
$$

Thus the point is captured by the reflected component in (1).  The example
invalidates the attempted proof without refuting the final union formula.

If $x$ supplies the last maximum in (5), then, using
$n_0+n_1+n_2=0$ and the tie on $n_0$,

$$
G_Q=\langle x-A,n_2\rangle=h|x-A|.
\tag{6}
$$

If $B$ supplies it, then

$$
G_Q=\langle B-A,n_2\rangle.
\tag{7}
$$

The right side of (7) is exactly the three-point fitting function for
$\{O,A,B\}$ on the branch where $A$ supports two consecutive sides.  On one
$120^\circ$ period that branch is

$$
R\cos\left(\varphi-\theta_{AB}-30^\circ\right),
$$

where

$$
\cos\theta_{AB}=\frac{\sqrt3a}{2R},
\qquad
\sin\theta_{AB}=\frac{a+2b}{2R}.
$$

Its unit-level endpoint is

$$
\varphi_+=\theta_{AB}+30^\circ-\kappa,
\qquad
\cos\kappa=\frac{h}{R},
\qquad
\sin\kappa=\frac{D}{2R}.
$$

Within the two support rows in (5), the $xA$ edge gives $G_Q\le h$ exactly
when

$$
|x-A|\le1
\quad\text{and}\quad
(a+2b-aD)(u-a)+(a-b+(a+b)D)v\le0.
\tag{8}
$$

For completeness, let $n_+=u(\varphi_+)$. Substitution of the displayed sine
and cosine values for $\theta_{AB}$ and $\kappa$ gives the exact identities

$$
\langle n_+,e_A\rangle=\alpha,
\qquad
\langle n_+,e_B\rangle=\beta.
$$

Consequently

$$
\langle n_+,x-A\rangle=\alpha(u-a)+\beta v.
$$

Within the normal-fan sector isolated in (5), the normal $n_+$ is the last
admissible outward normal for a side through $A$.  The edge normal has not passed
$n_+$ exactly when the last scalar product is nonpositive.  This proves the
second condition in (8) within that sector, without a numerical orientation comparison. In the
branch (7), the inequality $|x-A|\le1$ is
automatic from

$$
h|x-A|=\langle x-A,n_2\rangle
\le\langle B-A,n_2\rangle=G_Q\le h;
$$

in the branch (6), it is precisely the fitting inequality.  Hence the two
support rows in (5) give the condition
$x\in\mathcal D_A\cap\mathcal H_A$.

Reflecting $a\leftrightarrow b$ gives, for the corresponding two $Bx$ support
rows,

$$
|x-B|\le1
\quad\text{and}\quad
(-a+b+(a+b)D)u+(2a+b-bD)(v-b)\le0,
\tag{9}
$$

which is $x\in\mathcal D_B\cap\mathcal H_B$ in those rows.  Equations
(2)--(9) therefore prove the candidate formula only for the displayed support
sectors.  To prove (1), every omitted $xA$ and $Bx$ support regime must be
partitioned exactly and shown either impossible at the unit bound or already
contained in the opposite disk--half-plane component.  The exact example
above shows that the first alternative alone cannot work.  Continuity at
cone-axis and collinear degeneracies does not supply this missing global
partition.

### 3. Conditional frontier extraction

Assume the unproved set identity (1).  The following calculations then give
its advertised four-piece boundary, subject also to the explicitly noted
ordering calculation.

The strict assumptions imply

$$
0<D<1,
$$

and all four coefficients are positive.  For the only non-obvious two, use

$$
(a+b)^2D^2-(a-b)^2
=4\rho\left((a+b)^2-1\right)>0.
$$

Also

$$
\Omega=\frac{3(1-D)(D+3)}{16\rho}>0.
$$

Hence both sets on the right side of (1) are compact, convex, contain $O$,
and meet each cone ray in an initial interval.  Their outer radial boundaries
are obtained by taking, respectively, the nearer of a disk and its associated
line; the boundary of their union takes the farther of those two radial
values.

Solving the resulting three pairs of equations gives, in order,

$$
\mathcal D_A\cap\{u=0\}:P_0,
\quad
\partial\mathcal D_A\cap\partial\mathcal H_A:P_1,
\quad
\partial\mathcal H_A\cap\partial\mathcal H_B:P_2,
$$

$$
\partial\mathcal H_B\cap\partial\mathcal D_B:P_3,
\quad
\mathcal D_B\cap\{v=0\}:P_4.
$$

The quadratic formula gives $P_0,P_1,P_3,P_4$, and Cramer's rule gives
$P_2$; these are the five displayed formulas above.  To complete the
extraction, one must substitute them to prove that all five lie in $C$ and
that their cone-ray slopes occur strictly in the displayed order.  The
intended calculation reduces the successive $2\times2$ determinants to
positive factors among $1-D$, $1-\rho$, and $(a+b)^2-1$, but those reductions
are not recorded here.  They are still required to rule out an additional
switch of the four radial constraints.

It follows from (1) that the non-axis outer boundary is, successively,

$$
\partial\mathcal D_A,\quad
\partial\mathcal H_A,\quad
\partial\mathcal H_B,\quad
\partial\mathcal D_B,
$$

from $P_0$ to $P_4$.  Conditional on the omitted ordering calculation,
expanding these four equations gives the two circle arcs and two line segments
stated in the target.

At $\rho=1$, one has $D=1$ and $\Omega=0$; the nondegenerate four-piece
formula is therefore correctly excluded and must be replaced by its limiting
degeneration.  This completes the conditional extraction, not the target
proof.
