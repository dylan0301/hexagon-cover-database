# CE1 Three-Transverse Return Certificate

Status: Proven

This note isolates the CE1 return used by the simplified seven-point
enclosure theorem.  It works directly with the actual boundary reaches on the
backward path

$$
T_5,T_4,T_3,T_2,T_1
$$

and uses radial information only at $T_4,T_3,T_2$.  No radial hypothesis at
$T_0,T_1,T_5$, formal iterate, or composed propagation map is used.

All local facts used below are derived from the exact finite-caliper
admissible set [`2004`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
In particular, Sections 3--4 derive the selected low root, the direct threshold,
and the two chord inequalities needed by the reverse path.

## 1. Center domain

Use the signed CE1 variables

$$
0<R<1,
\qquad
w=1-R,
$$

$$
E=\sqrt{1-Rw},
\qquad
\eta=1-E,
\qquad
P=E(1-E),
$$

and write

$$
A=\alpha,
\qquad
D=\delta.
$$

The strict CE1 domain is

$$
A>0,
\qquad
D>0,
$$

$$
A+wD<P,
\qquad
D+RA\ge P.
\tag{1}
$$

Put

$$
X=R-D,
\qquad
m=\frac AR,
\qquad
h_0=\frac{\eta+A+D}{2R}.
\tag{2}
$$

The sign difference in (1) gives

$$
RD>wA,
$$

so the center exit on $r_3$ is $A/R=m$.  Moreover

$$
0<A<P<\frac18,
\qquad
0<D<\frac R2,
\qquad
0<m<\frac w2<\frac12.
\tag{3}
$$

For

$$
0<d<1-\frac{\sqrt3}{2},
$$

put

$$
e(d)=\frac{1-d}{2}
\left(1-\sqrt{4(1-d)^2-3}\right).
$$

This is the selected smaller root of the exact $L$-cell frontier at radial
demand $1-d$.  The following estimates are
proved below and used by the direct reach argument:

$$
\boxed{e(A)<X,\qquad h_0>A.}
\tag{4}
$$

If the $T_4$ local state is selected $Q_+$, then in fact

$$
\boxed{X>\frac12.}
\tag{5}
$$

## 2. Three-transverse return statement

Let $T_0$ be the unique supercritical role and let
$T_1,\ldots,T_5$ be nonsupercritical Vd0 roles.  Assume that their actual
reaches satisfy

$$
A_1\ge X,
$$

$$
B_i+A_{i+1}\ge1\quad(1\le i\le4),
\qquad
B_5+A_0\ge1,
$$

and only the three transverse radial lower bounds

$$
C_4\ge1-A,
\qquad
C_3\ge1-m,
\qquad
C_2\ge1-D.
\tag{6}
$$

Then

$$
\boxed{A_0>1-h_0}.
$$

Suppose, to the contrary, that

$$
A_0\le1-h_0.
\tag{6a}
$$

The assumed final handoff gives $A_0+B_5\ge1$, so (6a) gives
$B_5\ge h_0$.  Since $T_5$ is nonsupercritical and
$B_4+A_5\ge1$,

$$
A_5+B_5\le1,
\qquad
B_4+A_5\ge1,
$$

so

$$
\boxed{B_4\ge B_5\ge h_0.}
\tag{7}
$$

The assumed transverse radial demand at $T_4$ is at least $1-A$.  Apply the exact local finite-caliper catalogue of `2004` to the reflected boundary pair $(B_4,A_4)$.

If the state is not on the selected $Q_+$ branch, then (4) and the constant,
$Q_-$, and linear catalogue values give

$$
1-A_4\ge1-e(A)>1-X.
$$

The edge $e_{3,4}$ then gives $B_3>1-X$.  Nonsupercriticality and the next two
center-free edges carry this strict lower bound backward to $B_1>1-X$, which
contradicts $A_1\ge X$ and $A_1+B_1\le1$.

It remains to assume that the $T_4$ state is selected $Q_+$.  The selected-arc chord calculation in Section 4 gives

$$
B_3> L_1,
$$

where

$$
\boxed{
L_1=(2-4A)h_0-(1-4A)A.
}
\tag{8}
$$

The selected-state hypothesis also implies (5).  Hence

$$
m<\frac w2<\frac14.
\tag{9}
$$

If $B_3\ge1/2$, then $B_3>1-X$ and the preceding immediate contradiction
applies.  Assume $B_3<1/2$.  At $T_3$ the incoming reflected coordinate is
$B_3>h_0>m$, and the radial demand is $1-m$.  If this local state is not
selected $Q_+$, the exact catalogue gives

$$
B_2\ge1-B_3>\frac12>1-X.
$$

Again the remaining center-free edge gives the contradiction at $T_1$.

Thus both $T_4$ and $T_3$ are selected $Q_+$.  The same direct selected-arc calculation for $T_3$ gives

$$
B_2>(2-5m)B_3-(1-5m)m.
$$

Since $2-5m>0$, (8) yields

$$
\boxed{
B_2>L_2,
\qquad
L_2=(2-5m)L_1-(1-5m)m.
}
\tag{10}
$$

The scalar estimate in Sections 4--6 proves

$$
\boxed{
D<\frac1{10},
\qquad
L_2>2D+3D^2>e(D),
\qquad
e(D)<X.
}
\tag{11}
$$

The assumed transverse radial demand at $T_2$ is at least $1-D$.  Since $B_2>e(D)$, the
high-radial threshold theorem, applied after reflection, gives

$$
A_2\le e(D).
$$

Coverage of $e_{1,2}$ therefore forces

$$
B_1\ge1-A_2\ge1-e(D)>1-X,
$$

contradicting $A_1\ge X$ and nonsupercriticality of $T_1$.

Thus (6) is impossible.  Every configuration satisfying the displayed boundary and transverse radial hypotheses satisfies

$$
\boxed{A_0>1-h_0.}
\tag{12}
$$

## 3. Preliminary estimates

The inequality $A+wD<P$, with $D=R-X$, gives

$$
A<wX-\eta.
$$

Convexity of

$$
f(X)=wX-\frac{X}{2(1+X)}
$$

on $R/2<X<R$, together with the endpoint checks, gives

$$
A<\frac{X}{2(1+X)}.
$$

The selected quadratic evaluated at $2A/(1-2A)$ gives

$$
e(A)<\frac{2A}{1-2A}<X.
$$

Also

$$
2R(h_0-A)=\eta+D+(1-2R)A>0.
$$

For $R>1/2$, use $A<P=\eta E$ to obtain the last sign.  This proves (4).

Assume the $T_4$ state is selected $Q_+$.  Its selector gives

$$
h_0\le e(A)<\frac{2A}{1-2A}.
\tag{13}
$$

Suppose $X\le1/2$.  The lower center inequality in (1) gives

$$
2Rh_0=\eta+A+D\ge\eta+A+P-RA=w(R+A).
$$

Combining with (13) yields

$$
f_R(A)<0,
$$

where

$$
f_R(z)=w(R+z)(1-2z)-4Rz.
$$

This quadratic is strictly concave and $f_R(0)=Rw>0$.  If $R\le1/2$, then
$0<A<P$ and

$$
f_R(P)
\ge
\frac{1-E}{2}(6E^3-2E^2-5E+2)>0.
$$

The final cubic is increasing on $E\in[\sqrt3/2,1)$ and is positive at
$E=\sqrt3/2$.  Concavity gives $f_R(A)>0$, a contradiction.

If $R>1/2$, the assumption $X\le1/2$ gives

$$
0<A<A_*:=P-w\left(R-\frac12\right)=\frac w2-\eta.
$$

Direct simplification gives

$$
f_R(A_*)=
\frac{1-E}{2}(E+11R-3ER-5)>0.
$$

Concavity again contradicts $f_R(A)<0$.  Thus (5) holds.

## 4. The two selected chord bounds

For a selected $Q_+$ state with deficit $d$, the exact selected $T$-cell equation gives the high-radial chord coefficient

$$
\frac{d}{e(d)-d}.
$$

For $d=A<1/8$, the low-root bound gives

$$
\frac{A}{e(A)-A}>1-4A,
$$

which proves (8).

For the $T_3$ state, the selected coefficient is greater than $1-5m$.  If
$m\le1/8$, this follows from

$$
e(m)\le2m+5m^2.
$$

If $1/8<m<1-\sqrt3/2$, use $e(m)<(1-m)/2$ to obtain

$$
\frac{m}{e(m)-m}>\frac{2m}{1-3m}>1-5m.
$$

On the low-radial selected arc, direct differentiation of the selected quadratic gives a chord coefficient greater than $1/3>1-5m$.  This proves (10) in every selected component.

## 5. The bound $D<1/10$

The $T_4$ selected-state inequality and $e(A)\le2A+5A^2$ give

$$
D\le D_h:=A(4R-1)+10RA^2-\eta.
\tag{14}
$$

Suppose $D\ge1/10$.  Since $R>1/2$ and
$P<Rw/2$, the inequality $A+wD<P$ gives

$$
A<\overline A:=\frac{w(5R-1)}{10}.
$$

The right side of (14) is increasing in $A$, and $\eta>Rw/2$, so

$$
D<U(R):=\overline A(4R-1)+10R\overline A^2-\frac{Rw}{2}.
$$

Direct expansion gives

$$
\frac1{10}-U(R)=-\frac R{10}P_4(R),
$$

where

$$
P_4(R)=25R^4-60R^3+26R^2+22R-14.
$$

For $y=2R-1\in(0,1)$,

$$
16P_4(R)
=25y^4-20y^3-106y^2+124y-39
\le-101y^2+124y-39<0.
$$

The last quadratic has negative discriminant.  Hence $U(R)<1/10$, contrary
to $D\ge1/10$.

## 6. The terminal lower bound for $L_2$

Define

$$
\Psi(D)=L_2-2D-3D^2,
\qquad
J(D)=L_2-\frac{23}{10}D.
$$

Since $D<1/10$,

$$
\Psi(D)-J(D)=3D\left(\frac1{10}-D\right)>0.
$$

For fixed $R,A$, exact differentiation of the expression in (10) gives

$$
J'(D)=\frac{S(R,A)}{10R^2},
$$

where

$$
S(R,A)=100A^2-(40R+50)A+R(20-23R).
$$

The nonempty interval $P-RA\le D\le D_h$ implies

$$
A>\frac{4Rw}{25R-4}=:A_*.
$$

On the relevant range, $\partial S/\partial A<-45$, and

$$
S(R,A)<S(R,A_*)
=-\frac{Rq_3(R)}{(25R-4)^2},
$$

where

$$
q_3(R)=8775R^3-14260R^2+7928R-1120.
$$

For $y=2R-1\in(0,1)$,

$$
8q_3(R)=8775y^3-2195y^2+997y+3007>0.
$$

Thus $J$ decreases with $D$, and $J(D)\ge J(D_h)$.

At $D=D_h$, one has $h_0=2A+5A^2$.  Let the corresponding value of $L_2$ be
$L_{2,h}$.  Exact expansion gives

$$
L_{2,h}-A(1+4R)=\frac{A}{R^2}Q(R,A),
$$

where

$$
\begin{aligned}
Q(R,A)={}&100A^3R-40A^2R^2-30A^2R+12AR^2-15AR+5A\\
&-4R^3+5R^2-R.
\end{aligned}
$$

The polynomial is concave in $A$ on $0\le A\le Rw/2$.  At the endpoints,

$$
Q(R,0)=Rw(4R-1)>0,
$$

and

$$
Q\left(R,\frac{Rw}{2}\right)
=\frac{Rw}{2}p(R),
$$

where

$$
p(R)=25R^5-30R^4+20R^3-3R^2-7R+3>0.
$$

For $y=2R-1$, positivity follows from

$$
32p(R)=25y^5+65y^4+90y^3+106y^2-35y+5>0.
$$

Hence

$$
L_{2,h}>A(1+4R).
$$

Finally $A<P=\eta E$, $A<Rw/2$, and $1/E>1+Rw/2$ give

$$
\frac{D_h}{A}
<C_*:=4R-2+5R^2w-\frac{Rw}{2}.
$$

Moreover

$$
1+4R-\frac{23}{10}C_*=\frac{h_3(R)}{20},
$$

where

$$
h_3(R)=230R^3-253R^2-81R+112>0.
$$

For example, strong convexity about $R_0=20/23$ gives the exact positive lower
bound

$$
h_3(R)\ge\frac{289695}{194672}.
$$

Therefore $J(D_h)>0$, so

$$
L_2>2D+3D^2.
$$

Substitution in the selected low-root quadratic gives

$$
e(D)<2D+3D^2
$$

for $D<1/10$.  Also $e(D)<X$ follows from the same preliminary estimate as in
Section 3.  This proves (11).

## 7. Conclusion

The contradiction above proves

$$
\boxed{A_0>1-h_0}
$$

from the five boundary handoffs and the three radial lower bounds at
$T_4,T_3,T_2$.  These are exactly the data supplied by the transverse
seven-point witness.  No reach on $r_0,r_1,r_5$ enters the proof.

$$
\Box
$$
