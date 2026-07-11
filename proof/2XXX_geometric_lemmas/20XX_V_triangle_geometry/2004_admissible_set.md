# Exact Piecewise Local Admissible Set

Status: Proven

This note gives two equivalent explicit descriptions of the local admissible
set: a geometry-first minimum-side formula and a three-cell algebraic formula.
The second description restores the useful polynomial cells while adding the
component selector that the former Cell-2 sheet omitted.

## 1. Local demand coordinates

After a rigid motion, take unit vectors

$$
u=
\left(
\frac12,
\frac{\sqrt3}{2}
\right),
\qquad
v=
\left(
\frac12,
-\frac{\sqrt3}{2}
\right).
$$

They meet at $120$ degrees, and $u+v=(1,0)$ is the inward radial direction.
For $0\le a,b,c\le1$, put

$$
O=0,
\qquad
A=au,
\qquad
B=bv,
\qquad
C=c(u+v),
$$

and

$$
K(a,b,c)=\mathrm{conv}\left\{O,A,B,C\right\}.
$$

The coordinates $(a,b,c)$ are lower-bound demands. Define

$$
\mathcal A=
\left\{
(a,b,c)\in[0,1]^3:
K(a,b,c)\text{ lies in a closed unit equilateral triangle}
\right\}.
$$

If a particular triangle has actual reaches $(A_0,B_0,C_0)$, it realizes
every demand triple with

$$
0\le a\le A_0,
\qquad
0\le b\le B_0,
\qquad
0\le c\le C_0.
$$

Thus demand coordinates must not be substituted for actual reaches when a row
is classified by $A_0+B_0\le1$ or $A_0+B_0>1$.

## 2. Exact piecewise minimum-side formula

Let $L_{\min}(a,b,c)$ be the least side length of a closed equilateral
triangle containing $K(a,b,c)$. Set

$$
s=a+b,
\qquad
D=\sqrt{a^2+ab+b^2}.
$$

If $s>0$ and

$$
cs\le ab,
$$

then $C\in\mathrm{conv}\left\{O,A,B\right\}$. In this case

$$
L_{\min}(a,b,c)=D.
$$

For the remaining case $s>0$ and $cs>ab$, define

$$
R_a=\sqrt{a^2-ac+c^2},
\qquad
R_b=\sqrt{b^2-bc+c^2}.
$$

The four support-contact side lengths are

$$
L_{OA}=b+\max\left\{a,c\right\},
$$

$$
L_{BO}=a+\max\left\{b,c\right\},
$$

$$
L_{AC}=
\begin{cases}
\dfrac{a^2+bc}{R_a},
& a\ge c,\\
\dfrac{c(a+b)}{R_a},
& a<c\le a+b,\\
\dfrac{c^2}{R_a},
& c>a+b,
\end{cases}
$$

and

$$
L_{CB}=
\begin{cases}
\dfrac{b^2+ac}{R_b},
& b\ge c,\\
\dfrac{c(a+b)}{R_b},
& b<c\le a+b,\\
\dfrac{c^2}{R_b},
& c>a+b.
\end{cases}
$$

The exact formula is

$$
\boxed{
L_{\min}(a,b,c)=
\begin{cases}
c,
& a=b=0,\\
\sqrt{a^2+ab+b^2},
& a+b>0\text{ and }c(a+b)\le ab,\\
\min\left\{L_{OA},L_{BO},L_{AC},L_{CB}\right\},
& a+b>0\text{ and }c(a+b)>ab.
\end{cases}
}
$$

Consequently the requested admissible set is the explicit piecewise set

$$
\boxed{
\mathcal A=
\left\{
(a,b,c)\in[0,1]^3:
L_{\min}(a,b,c)\le1
\right\}.
}
$$

There is no angular minimization or numerical root choice left in this
formula.

## 3. Proof of the minimum-side formula

If $c(a+b)\le ab$ and $a+b>0$, then the barycentric inequality

$$
\frac{c}{a}+\frac{c}{b}\le1
$$

holds whenever $a,b>0$, with the zero-coordinate cases obtained by a limit.
Hence $C$ lies in the triangle $OAB$. The distance $AB$ is $D$ and is the
diameter of that triangle. The equilateral triangle with vertices

$$
A,
\qquad
B,
\qquad
-bu-av
$$

has side $D$ and contains $O$. It therefore contains $C$, proving
$L_{\min}=D$.

Now suppose $c(a+b)>ab$. The convex hull has cyclic order

$$
O,
\quad
B,
\quad
C,
\quad
A.
$$

For a compact set $K$, write

$$
h_K(n)=\max_{p\in K}n\mathbin{\cdot}p.
$$

For three outward unit normals $n_0,n_1,n_2$ separated by $120$ degrees, the
least equilateral triangle with those normals and containing $K$ has side

$$
\frac2{\sqrt3}
\sum_{j=0}^2h_K(n_j).
$$

On an open angular cell on which the three support points are fixed, the
support sum has the form

$$
X\cos\phi+Y\sin\phi
$$

and its second derivative is the negative of the sum. The sum is positive in
the nondegenerate case, so an interior critical point is a maximum. Therefore
a minimizing orientation has one normal perpendicular to a hull edge. The
four possibilities are $OA$, $AC$, $CB$, and $BO$.

The $OA$ and $BO$ projections give $L_{OA}$ and $L_{BO}$ directly. For the
$AC$ edge, an outward unit normal is

$$
n_0=
\frac1{2R_a}
\left(
\sqrt3a,
2c-a
\right).
$$

Put $x_+=\max\left\{x,0\right\}$. After rotating $n_0$ twice by $120$
degrees, the three support values are

$$
\frac{\sqrt3ac}{2R_a},
\qquad
\frac{\sqrt3a(a-c)_+}{2R_a},
\qquad
\frac{\sqrt3c\max\left\{b,(c-a)_+\right\}}{2R_a}.
$$

Their sum gives the three displayed cases for $L_{AC}$. Reflection exchanges
$a$ and $b$ and gives $L_{CB}$. Taking the least of the four exhaustive
support contacts proves the formula. Zero-length hull edges and equality
cases follow by continuity; the displayed expressions remain valid on their
stated closed boundaries.

## 4. Equivalent algebraic cells

For calculations that prefer polynomial inequalities, set

$$
m=\min\left\{a,b\right\},
\qquad
M=\max\left\{a,b\right\},
\qquad
s=a+b,
$$

$$
d=a^2+ab+b^2,
\qquad
q=s^4-s^2+ab,
$$

and

$$
F_L(a,b,c)=c^4-c^2+mc-m^2,
$$

$$
F_T(a,b,c)=(s^2-1)c^2+Mc-M^2,
$$

$$
F_S(a,b,c)=
(m^2-1)c^2+(2mM^2+M)c+(M^4-M^2).
$$

Define

$$
\mathcal A_L=
\left\{
(a,b,c)\in[0,1]^3:
d\le1,
s\le1,
q\le0,
F_L(a,b,c)\le0
\right\},
$$

$$
\mathcal A_T=
\left\{
(a,b,c)\in[0,1]^3:
d\le1,
s\le1,
q\ge0,
F_T(a,b,c)\le0,
c\le2M
\right\},
$$

and

$$
\mathcal A_S=
\left\{
(a,b,c)\in[0,1]^3:
d\le1,
s>1,
F_S(a,b,c)\le0,
c\le\frac12
\right\}.
$$

Then the exact algebraic form is

$$
\boxed{
\mathcal A=\mathcal A_L\cup\mathcal A_T\cup\mathcal A_S.
}
$$

The cells overlap only on genuine transition boundaries. In particular, when
$q=0$ and $s>0$, the point may be assigned to either subcritical cell. At the
origin, $\mathcal A_L$ supplies the full radial segment while the degenerate
$\mathcal A_T$ condition supplies only $c=0$.

To verify this algebraic form, assume by symmetry that $a=m\le b=M$ and
substitute the four support formulas from Section 2. The possible active
support triples and their unit-frontier equations are

| Range | Active support points | Unit-frontier equation |
|---|---|---|
| $s<1$, $q<0$ | $\left\{O\right\}$, $\left\{C\right\}$, $\left\{A,C\right\}$ | $F_L=0$ |
| $s<1$, $q>0$ | $\left\{O\right\}$, $\left\{B,C\right\}$, $\left\{A\right\}$ | $F_T=0$ |
| $s=1$ | the preceding pattern with an additional $O,B$ tie | $c=M$ |
| $s>1$ | $\left\{B\right\}$, $\left\{B,C\right\}$, $\left\{A\right\}$ | $F_S=0$ |

The inactive-point inequalities reduce respectively to $q\le0$, $q\ge0$,
and $s>1$. Squaring the positive side-length equations gives the displayed
polynomials. The only nonautomatic issue is selecting the correct connected
component after squaring.

For Cell $T$ with $0<s<1$, the roots of $F_T=0$ are

$$
c_-=
\frac{2M}{1+\sqrt{4s^2-3}},
\qquad
c_+=
\frac{2M}{1-\sqrt{4s^2-3}}.
$$

The raw inequality $F_T\le0$ holds both for $0\le c\le c_-$ and for
$c\ge c_+$. Only the first interval is geometric. The condition

$$
c\le2M
$$

lies between the two roots and selects that interval. Equivalently, under the
other Cell-$T$ conditions one may use

$$
M+2(s^2-1)c\ge0.
$$

For Cell $S$,

$$
F_S(a,b,0)=M^2(M^2-1)<0
$$

and

$$
F_S(a,b,M)=M^2(s^2-1)>0.
$$

Also $4F_S(a,b,1/2)$ is increasing in $m$, and at $m=1-M$ it equals

$$
M^2(2M-1)^2.
$$

Because $s>1$ gives $m>1-M$, one has $F_S(a,b,1/2)>0$. Since the quadratic
opens downward, $1/2$ lies strictly between its two roots. Thus $c\le1/2$
selects the smaller-root component. Cell $L$ has one selected root in
$(0,1]$. This proves the algebraic union and explains precisely why the
former unselected Cell-2 inequality admitted a fake high-$c$ sheet.

## 5. Explicit radial envelope

Define

$$
c_{\max}(a,b)=
\max_{\substack{0\le c\le1\\ {}(a,b,c)\in\mathcal A}}c.
$$

If $d>1$, this quantity is undefined. If $d\le1$, let $C_L(m)$ denote the
unique root in $[\sqrt3/2,1]$ of

$$
z^4-z^2+mz-m^2=0.
$$

The convention $C_L(0)=1$ includes the degenerate endpoints. On the domain
$d\le1$, $s\le1$, and $q>0$, define

$$
C_T(m,M)=
\frac{2M}{1+\sqrt{4s^2-3}},
$$

On the domain $d\le1$ and $s>1$, define

$$
C_S(m,M)=
\frac{
M(2mM+1)
-
M\sqrt{4d-3}
}{
2(1-m^2)
}.
$$

Then

$$
\boxed{
c_{\max}(a,b)=
\begin{cases}
1,
& a=b=0,\\
C_L(m),
& d\le1,\ s\le1,\ q\le0,\ (a,b)\ne(0,0),\\
C_T(m,M),
& d\le1,\ s\le1,\ q>0,\\
C_S(m,M),
& d\le1,\ s>1,\\
\text{undefined},
& d>1.
\end{cases}
}
$$

When $q=0$ and $s>0$, the two subcritical formulas agree and equal $s$. At
$s=1$, the selected subcritical value is $M$. The origin is displayed
separately because the square root in $C_T$ is not real-defined there; the
convention $C_L(0)=1$ gives the same radial value.

## 6. Structural consequences

The formula is symmetric:

$$
(a,b,c)\in\mathcal A
\quad\Longleftrightarrow\quad
(b,a,c)\in\mathcal A.
$$

The set is coordinatewise down-closed. If $(a,b,c)\in\mathcal A$ and

$$
0\le a'\le a,
\qquad
0\le b'\le b,
\qquad
0\le c'\le c,
$$

then convexity of the containing triangle and its containment of $O$ give

$$
(a',b',c')\in\mathcal A.
$$

Every fixed-coordinate fiber is therefore an interval beginning at zero.
The discarded high-$c$ quadratic component cannot be a second geometric
fiber.
