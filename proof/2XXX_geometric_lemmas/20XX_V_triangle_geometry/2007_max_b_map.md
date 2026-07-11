# Exact Piecewise Maximal $B_c(a)$ Map

Status: Proven

This note evaluates the outgoing-demand map from
[`2004_admissible_set.md`](2004_admissible_set.md) by explicit support-contact
pieces. Every quadratic and quartic root is restricted to its geometric
contact interval before it can contribute. This is the component selection
missing from the former candidate-root maximum.

## 1. Definition and boundary values

For $a,c\in[0,1]$, define

$$
B_c(a)=
\max_{\substack{0\le b\le1\\ {}(a,b,c)\in\mathcal A}}b.
$$

The feasible set is nonempty because the unit triangle

$$
\mathrm{conv}\left\{O,u,u+v\right\}
$$

contains $O$, $au$, and $c(u+v)$. If $b$ is feasible, every $b'$ with
$0\le b'\le b$ is feasible by convexity. Hence

$$
\left\{
b\in[0,1]:(a,b,c)\in\mathcal A
\right\}
=
[0,B_c(a)].
$$

Define the diameter cap

$$
\beta(a)=
\frac{-a+\sqrt{4-3a^2}}2.
$$

It is the nonnegative solution of

$$
a^2+a\beta+\beta^2=1.
$$

The degenerate boundary values are

$$
\boxed{
B_0(a)=\beta(a)
\qquad
(0\le a\le1),
}
$$

$$
\boxed{
B_c(0)=1
\qquad
(0\le c\le1),
}
$$

$$
\boxed{
B_c(1)=0
\qquad
(0\le c\le1),
}
$$

and

$$
\boxed{
B_1(a)=0
\qquad
(0<a\le1).
}
$$

The rest of the piecewise formula assumes

$$
0<a<1,
\qquad
0<c<1,
$$

and abbreviates $\beta=\beta(a)$. A branch value is declared empty by
assigning it $-\infty$.

## 2. Inner-triangle and axial-support pieces

The inner-triangle piece is

$$
\beta_{\mathrm{in}}=
\begin{cases}
\beta,
& c(a+\beta)\le a\beta,\\
-\infty,
& c(a+\beta)>a\beta.
\end{cases}
$$

Indeed, the first condition places the radial point in
$\mathrm{conv}\left\{O,A,B\right\}$ at the diameter endpoint $b=\beta$.

The support-on-$OA$ piece is

$$
\beta_{OA}=
\min\left\{
\beta,
1-\max\left\{a,c\right\}
\right\}.
$$

The support-on-$BO$ piece is

$$
\beta_{BO}=
\begin{cases}
\min\left\{\beta,1-a\right\},
& a+c\le1,\\
-\infty,
& a+c>1.
\end{cases}
$$

These follow from the exact side lengths

$$
L_{OA}=b+\max\left\{a,c\right\},
\qquad
L_{BO}=a+\max\left\{b,c\right\}.
$$

In particular, they include the genuine boundary plateau $b=1-a$.

## 3. The two $AC$ pieces

Set

$$
R_a=\sqrt{a^2-ac+c^2}.
$$

For $a\ge c$, define

$$
U_A=
\begin{cases}
+\infty,
& a=c,\\
\dfrac{ac}{a-c},
& a>c.
\end{cases}
$$

Then

$$
\beta_{AC}^{(1)}=
\begin{cases}
\min\left\{
\beta,
U_A,
\dfrac{R_a-a^2}{c}
\right\},
& a\ge c\text{ and the displayed minimum is nonnegative},\\
-\infty,
& \text{otherwise}.
\end{cases}
$$

The bound $b\le U_A$ is exactly the outer-hull condition
$c(a+b)\ge ab$. The final bound is equivalent to

$$
L_{AC}=
\frac{a^2+bc}{R_a}
\le1.
$$

For $a<c$, define

$$
\beta_{AC}^{(2)}=
\begin{cases}
\min\left\{
\beta,
\dfrac{R_a}{c}-a
\right\},
& a<c\text{ and }R_a\ge c^2,\\
-\infty,
& \text{otherwise}.
\end{cases}
$$

Here the contact interval begins at $b=c-a$, and the displayed condition says
that the proposed cap reaches that interval. On the interval,

$$
L_{AC}=
\frac{c(a+b)}{R_a}
\le1.
$$

The remaining subcase $c>a+b$ creates no larger cap. If $c^2\le R_a$, it
reaches $b=c-a$ and continues into $\beta_{AC}^{(2)}$; if $c^2>R_a$, it is
infeasible.

## 4. The three $CB$ pieces

Set

$$
R_b=\sqrt{b^2-bc+c^2}.
$$

### 4.1. Contact range $b\ge c$

Define

$$
P_{a,c}(b)=
b^4+(2ac-1)b^2+cb+(a^2-1)c^2.
$$

On this contact range,

$$
L_{CB}=\frac{b^2+ac}{R_b}\le1
\quad\Longleftrightarrow\quad
P_{a,c}(b)\le0.
$$

The exact upper endpoint of the geometric contact interval is

$$
U_H=
\begin{cases}
\beta,
& a\le c,\\
\min\left\{\beta,\dfrac{ac}{a-c}\right\},
& a>c.
\end{cases}
$$

When $c\le U_H$, let $\rho_H$ be the largest root in the geometric contact
interval:

$$
c\le\rho_H\le U_H,
\qquad
P_{a,c}(\rho_H)=0.
$$

If no such root exists, $\rho_H$ is undefined. The exact piece is

$$
\beta_{CB}^{(1)}=
\begin{cases}
U_H,
& c\le U_H\text{ and }P_{a,c}(U_H)\le0,\\
\rho_H,
& c\le U_H,\ P_{a,c}(U_H)>0,\text{ and }\rho_H\text{ exists},\\
-\infty,
& \text{otherwise}.
\end{cases}
$$

Thus the quartic equation is explicit, but its root is selected inside the
proved contact interval. An unrestricted largest quartic root is not a
geometric formula.

### 4.2. Contact range $b<c\le a+b$

Define

$$
L_M=\max\left\{0,c-a\right\},
\qquad
U_M=\min\left\{c,\beta\right\},
$$

and

$$
Q_{a,c}(b)=
(c^2-1)b^2+(2ac^2+c)b+(a^2-1)c^2.
$$

On $[L_M,U_M]$,

$$
L_{CB}=\frac{c(a+b)}{R_b}\le1
\quad\Longleftrightarrow\quad
Q_{a,c}(b)\le0.
$$

Put

$$
\Delta_M=
(2ac^2+c)^2-4(1-c^2)(1-a^2)c^2.
$$

When $\Delta_M\ge0$, define

$$
r_\pm=
\frac{
2ac^2+c\pm\sqrt{\Delta_M}
}{
2(1-c^2)
},
\qquad
r_-\le r_+.
$$

Then

$$
\beta_{CB}^{(2)}=
\begin{cases}
-\infty,
& L_M>U_M,\\
U_M,
& L_M\le U_M\text{ and }Q_{a,c}(U_M)\le0,\\
r_-,
& \Delta_M\ge0\text{ and }L_M\le r_-<U_M<r_+,\\
-\infty,
& \text{otherwise}.
\end{cases}
$$

If $\Delta_M<0$, the concave quadratic $Q_{a,c}$ is negative everywhere,
so the second line applies whenever the contact interval is nonempty. The
third line explicitly selects the lower component when the upper endpoint
lies between the two roots.

### 4.3. Contact range $c>a+b$

Define

$$
U_L=\min\left\{\beta,c-a\right\}
$$

and

$$
H_c(b)=b^2-bc+c^2-c^4.
$$

On $0\le b\le U_L$,

$$
L_{CB}=\frac{c^2}{R_b}\le1
\quad\Longleftrightarrow\quad
H_c(b)\ge0.
$$

For $c\ge\sqrt3/2$, put

$$
\ell(c)=
\frac c2
\left(
1-\sqrt{4c^2-3}
\right),
$$

$$
r(c)=
\frac c2
\left(
1+\sqrt{4c^2-3}
\right).
$$

The exact low piece is

$$
\beta_{CB}^{(3)}=
\begin{cases}
-\infty,
& U_L<0,\\
U_L,
& U_L\ge0\text{ and }c<\sqrt3/2,\\
U_L,
& c\ge\sqrt3/2\text{ and }
\left(U_L\le\ell(c)\text{ or }U_L\ge r(c)\right),\\
\ell(c),
& c\ge\sqrt3/2\text{ and }\ell(c)<U_L<r(c).
\end{cases}
$$

Indeed, $H_c$ has negative discriminant for $c<\sqrt3/2$. For
$c\ge\sqrt3/2$,

$$
H_c(b)\ge0
\quad\Longleftrightarrow\quad
b\le\ell(c)\text{ or }b\ge r(c).
$$

This is the exact source of the familiar low expression $\ell(c)$.

## 5. Final piecewise formula

Let

$$
\mathscr B(a,c)=
\left\{
\beta_{\mathrm{in}},
\beta_{OA},
\beta_{BO},
\beta_{AC}^{(1)},
\beta_{AC}^{(2)},
\beta_{CB}^{(1)},
\beta_{CB}^{(2)},
\beta_{CB}^{(3)}
\right\}
\setminus
\left\{-\infty\right\}.
$$

The exact maximal map is

$$
\boxed{
B_c(a)=
\begin{cases}
\beta(a),
& c=0,\\
1,
& a=0\text{ and }0<c\le1,\\
0,
& a=1\text{ and }0<c\le1,\\
0,
& 0<a<1\text{ and }c=1,\\
\max_{x\in\mathscr B(a,c)}x,
& 0<a<1\text{ and }0<c<1.
\end{cases}
}
$$

This is a finite piecewise-algebraic formula. If disjoint domains are desired,
assign each tie to a fixed branch order and define the domain of a branch by
requiring its cap to be at least every later cap and strictly greater than
every earlier cap. No floating-point comparison is part of the definition.

## 6. Proof that the pieces are exhaustive

Every admissible $b$ satisfies $b\le\beta$ because $AB$ has length
$\sqrt{a^2+ab+b^2}$. If the radial point lies in $OAB$, the endpoint of that
regime gives $\beta_{\mathrm{in}}$.

Otherwise the support proof in `2004` shows that a minimum enclosing
equilateral triangle has a normal supporting one of

$$
OA,
\qquad
AC,
\qquad
CB,
\qquad
BO.
$$

The $OA$ and $BO$ inequalities give the two axial caps. The three cases of
$L_{AC}$ give $\beta_{AC}^{(1)}$, $\beta_{AC}^{(2)}$, and no additional
cap. The three cases of $L_{CB}$ give respectively the quartic $P_{a,c}$,
the quadratic $Q_{a,c}$, and the quadratic $H_c$. Their contact intervals
are exactly the intervals imposed above. Squaring is reversible there because
all displayed side lengths and denominators are nonnegative.

Thus every cap is feasible, and every maximizing support orientation appears
in the list. Taking the greatest nonempty cap proves the formula.

## 7. Monotonicity, reflection, and classified maps

If

$$
a_1\le a_2,
\qquad
c_1\le c_2,
$$

then inclusion of demand fibers gives

$$
B_{c_1}(a_1)\ge B_{c_2}(a_2).
$$

Reflection in the radial line gives

$$
b\le B_c(a)
\quad\Longleftrightarrow\quad
a\le B_c(b).
$$

For a unit vertex triangle $T$, let $A(T),B(T),C(T)$ be its actual maximal
reaches. For a row class $\mathcal R$, the proof-safe classified envelope is

$$
B_c^{\mathcal R}(a)=
\sup_{\substack{T\in\mathcal R\\A(T)\ge a\\C(T)\ge c}}B(T),
$$

when the indexing set is nonempty. The relevant Vd0 classes are

$$
\mathcal R_0=
\left\{
T:T\text{ is Vd0 and }A(T)+B(T)\le1
\right\},
$$

and

$$
\mathcal R_+=
\left\{
T:T\text{ is Vd0 and }A(T)+B(T)>1
\right\}.
$$

The explicit formula above is the unclassified demand map. It does not by
itself prove that a maximizing realization is Vd0 or belongs to either actual
row class. In particular,

$$
\max_{\substack{0\le b\le1\\ {}(a,b,c)\in\mathcal A\\a+b\le1}}b
$$

is only a demand-coordinate relaxation of the nonsupercritical classified
map.

## 8. Exact rejection of the former high sheet

Take

$$
a=\frac5{12},
\qquad
b=\frac9{20},
\qquad
c=\frac{27}{28}.
$$

Here

$$
s=a+b=\frac{13}{15},
\qquad
M=b=\frac9{20},
\qquad
\sqrt{4s^2-3}=\frac1{15}.
$$

The raw Cell-$T$ quadratic has the two roots

$$
c_-=
\frac{27}{32},
\qquad
c_+=
\frac{27}{28}.
$$

Thus the old rule accepted $b=9/20$ at the fake upper root. The correct
component selector rejects it because

$$
c>2M.
$$

The direct support formula also gives

$$
L_{OA}=\frac{99}{70}>1,
\qquad
L_{BO}=\frac{29}{21}>1.
$$

Moreover,

$$
a^2-ac+c^2-c^4
=
-\frac{901385}{5531904}<0,
$$

and

$$
b^2-bc+c^2-c^4
=
-\frac{2553849}{15366400}<0.
$$

Hence $L_{AC}>1$ and $L_{CB}>1$ as well. The exact piecewise formula instead
gives

$$
\boxed{
B_{27/28}\left(\frac5{12}\right)
=
\ell\left(\frac{27}{28}\right)
=
\frac{27(14-\sqrt{141})}{784}.
}
$$

This is the selected low component, not a formal maximum over unrelated
algebraic roots.
