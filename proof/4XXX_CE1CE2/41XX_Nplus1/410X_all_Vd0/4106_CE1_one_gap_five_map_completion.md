# CE1 One-Gap Five-Map Completion

Status: Proven

This note proves that the CE1 exactly-one-gap state in `410X` is impossible.
The analytic inequality holds on the full strict CE1 center domain; no
auxiliary survivor restriction or classified map for the supercritical row
is needed.

Here a V-gap is the full nonempty set missed by the two adjacent open vertex
roles. It may be a positive-length interval or a singleton. The proof below
uses only weak endpoint bounds and therefore covers both cases.

For the geometric application, assume the `410X` hypotheses: all six vertex
roles are Vd0, $N_+=1$, and the unique center midpoint is $M_0$.  Section 1
of
[`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md)
then proves that $T_0$ is the unique supercritical row.

The selected capped-map formulas and equality conventions used below are
proved in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).

## 1. Exact normalized CE1 domain

Use the variables in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).
Put

$$
R=\lambda,
\qquad
w=1-R,
\qquad
E=\sqrt{1-R+R^2}=\sqrt{1-Rw},
$$

$$
\eta=1-E,
\qquad
P=\eta E,
\qquad
A=C_0,
\qquad
D=C_2.
$$

The elementary identities

$$
Rw=\eta(1+E),
\qquad
P=Rw-\eta=\frac{RwE}{1+E}
$$

will be used repeatedly.

Since $\sqrt3/2\le E<1$ and $E-E^2$ is decreasing on this interval,

$$
0<P\le\frac{2\sqrt3-3}{4}<\frac18.
$$

Direct substitution in `2105` gives

$$
s=\frac{\eta+A+D}{R},
\qquad
t=w+D,
\qquad
X:=1-t=R-D.
$$

The strict exact center domain implies

$$
A>0,
\qquad
D>0,
\qquad
A+wD<P,
\qquad
D+RA\ge P,
$$

and the midpoint conditions give

$$
A<\frac w2,
\qquad
D<\frac R2.
$$

Subtracting the two center inequalities yields

$$
RD-wA>0.
$$

Consequently, if

$$
m=\frac AR,
$$

then

$$
0<m<\frac w2<\frac12,
$$

because $A<P=RwE/(1+E)<Rw/2$. The six complementary radial demands from
`2105` are, in the present variables,

$$
\boxed{
\begin{aligned}
c_0&=Rs=\eta+A+D,\\
c_1&=1-\frac DR,\\
c_2&=1-D,\\
c_3&=1-\min\left\{\frac AR,\frac Dw\right\}=1-\frac AR=1-m,\\
c_4&=1-A,\\
c_5&=1-\frac Aw.
\end{aligned}
}
$$

Here the formula for $c_3$ uses $RD>wA$. The exact-one-midpoint
normalization gives $c_0\le1/2$. The bounds $D<R/2$, $A<w/2$, and
$m<1/2$ give

$$
\frac12<c_j<1,
\qquad j=1,2,3,4,5.
$$

Finally set

$$
H=\frac s2=\frac{\eta+A+D}{2R}.
$$

## 2. Capped-map duality and the three-row suffix

For $1/2<c<1$, write

$$
F_c(a)=\min\left\{B_c(a),1-a\right\},
\qquad
G_c(a)=1-F_c(a).
$$

Reflection of capped feasibility gives the exact duality

$$
\boxed{
G_c(a)\le z
\quad\Longleftrightarrow\quad
G_c(1-z)\le1-a.
}
$$

Every $G_c$ is nondecreasing and satisfies $G_c(a)\ge a$. It is therefore
enough to prove the stronger suffix inequality

$$
\boxed{
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)>1-H.
}
$$

Indeed, put $\Phi=G_{c_4}\circ G_{c_3}\circ G_{c_2}$. Since $G_{c_1}$ and
$G_{c_5}$ are extensive and $\Phi$ is nondecreasing,

$$
\begin{aligned}
(G_{c_5}\circ\Phi\circ G_{c_1})(X)
&\ge(\Phi\circ G_{c_1})(X)\\
&\ge\Phi(X).
\end{aligned}
$$

Repeated duality makes the reduction exact. Namely, failure of the suffix
inequality is equivalent successively to

$$
\begin{aligned}
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)\le1-H
&\quad\Longleftrightarrow\quad
G_{c_4}(H)
\le1-(G_{c_3}\circ G_{c_2})(X)\\
&\quad\Longleftrightarrow\quad
(G_{c_3}\circ G_{c_4})(H)
\le1-G_{c_2}(X)\\
&\quad\Longleftrightarrow\quad
(G_{c_2}\circ G_{c_3}\circ G_{c_4})(H)
\le1-X.
\end{aligned}
$$

We prove that the reverse composition is strictly greater than $1-X$.

## From the boundary gap to the analytic target

Use $a_i,b_i$ for the actual boundary reaches as in
[`1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md);
the symbols $c_i$ above are prescribed lower-bound radial demands.
Let $[s,t]\subset e_{0,1}$ be the maximal closed trace associated with the
open center role. Suppose it contains the vertex-uncovered set
$[b_0,1-a_1]$, possibly a singleton. Full boundary coverage puts this set in
the open center trace and in particular gives

$$
b_0\ge s,
\qquad
a_1\ge X=1-t.
$$

Let $\widehat c_j$ be the actual radial reach of $T_j$. Radial coverage and
the relaxation proved in `2105` give

$$
\widehat c_j\ge c_j,
\qquad j=0,1,\dots,5.
$$

Rows $T_1,\dots,T_5$ are nonsupercritical, so $a_j+b_j\le1$ for these
rows. Define the formal iterates

$$
z_0=X,
\qquad
z_j=G_{c_j}(z_{j-1}),
\qquad j=1,2,3,4,5.
$$

We claim that the actual incoming reaches dominate these iterates. The gap
bound gives $a_1\ge z_0$. If $a_j\ge z_{j-1}$, the capped-map theorem,
applied to the actual row $T_j$, and the fact that $F_{c_j}$ is nonincreasing
give

$$
b_j\le F_{c_j}(a_j)\le F_{c_j}(z_{j-1}).
$$

The CE1 center has no trace on the other five boundary edges. Full boundary
coverage therefore gives $a_{j+1}+b_j\ge1$ for $j=1,2,3,4$ and
$a_0+b_5\ge1$. Hence, for $j=1,2,3,4$,

$$
\begin{aligned}
a_{j+1}
&\ge1-b_j\\
&\ge1-F_{c_j}(z_{j-1})\\
&=G_{c_j}(z_{j-1})=z_j,
\end{aligned}
$$

and the same calculation in the fifth row gives

$$
a_0\ge1-b_5\ge G_{c_5}(z_4)=z_5.
$$

Thus the induction gives

$$
a_1\ge z_0,
\quad
a_2\ge z_1,
\quad
a_3\ge z_2,
\quad
a_4\ge z_3,
\quad
a_5\ge z_4,
\quad
a_0\ge z_5,
$$

and therefore

$$
a_0\ge
Z_{\mathrm{CE1}}
:=
(G_{c_5}\circ G_{c_4}\circ G_{c_3}\circ G_{c_2}\circ G_{c_1})(X).
$$

For the upper bound, the actual row $T_0$ realizes
$(a_0,b_0,\widehat c_0)$ in the exact admissible set $\mathcal A$ of
[`2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
Since
$b_0\ge s$ and $\widehat c_0\ge c_0$, coordinatewise down-closure gives

$$
(a_0,s,c_0)\in\mathcal A.
$$

Reflection of $\mathcal A$ exchanges the two boundary coordinates, so

$$
(s,a_0,c_0)\in\mathcal A.
$$

By the definition of the exact outgoing envelope in
[`2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),
this is precisely the bound

$$
a_0\le B_{c_0}(s).
$$

Consequently it is enough to prove

$$
Z_{\mathrm{CE1}}>B_{c_0}(s).
$$

## 3. Low-root estimates

For $0<d\le1-\sqrt3/2$, define the low Cell-$L$ root

$$
e(d)=\ell(1-d).
$$

The exact scalar lemma
[`2012_high_radial_low_root_bounds.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md)
proves

$$
\boxed{
e(d)<\frac{2d}{1-2d}
\qquad
\left(0<d\le\frac{2\sqrt3-3}{4}\right).
}
$$

It also proves

$$
\boxed{
e(d)\le2d+5d^2
\qquad
\left(0<d\le\frac18\right).
}
$$

and the sharper terminal estimate

$$
\boxed{
e(d)<2d+3d^2
\qquad
\left(0<d\le\frac1{10}\right).
}
$$

## 4. The first low root lies below the target

The inequality $A+wD<P$, with $D=R-X$, gives

$$
A<wX-\eta.
$$

Let

$$
f(X)=wX-\frac{X}{2(1+X)}.
$$

Because $D<R/2$, one has $R/2<X<R$. Moreover $f$ is convex. At the two
endpoints,

$$
f\left(\frac R2\right)<\frac{Rw}{2}<\eta,
$$

while $f(R)<\eta$ is equivalent to

$$
E(1-2R^2)<1,
$$

which is immediate from $E<1$. Hence $f(X)<\eta$, and therefore

$$
A<\frac{X}{2(1+X)}.
$$

Combining this with the first estimate of `2012` gives

$$
\boxed{e(A)<X.}
$$

We also have $H>A$. In fact,

$$
2R(H-A)=\eta+D+(1-2R)A.
$$

This is positive when $R\le1/2$. When $R>1/2$, use $A<P=\eta E$ to obtain

$$
2R(H-A)>
\eta\left(1-(2R-1)E\right)>0.
$$

## 5. The row-4 $T_+$ branch forces $X>1/2$

At row $4$, the Full branches are impossible because

$$
H>A,
\qquad
H<\frac12<1-A.
$$

If the selected branch is L or $T_-$, the catalog gives

$$
F_{1-A}(H)\le e(A),
$$

so

$$
G_{1-A}(H)\ge1-e(A)>1-X.
$$

Thus only the $T_+$ branch needs further work. Its selector gives

$$
H\le e(A)\le2A+5A^2.
$$

We now prove that this branch forces

$$
\boxed{X>\frac12.}
$$

Suppose instead that $X\le1/2$. The inequality $D+RA\ge P$ gives

$$
2RH=\eta+A+D\ge\eta+P+wA.
$$

Therefore

$$
Q(A):=\eta+P+wA-2R(2A+5A^2)\le0.
$$

The other center inequality and $X\le1/2$ give

$$
A<P-w\left(R-\frac12\right)=:A_0.
$$

The quadratic $Q$ is strictly concave and

$$
Q(0)=\eta+P=Rw>0.
$$

It remains to check its other endpoint. Rationalize by

$$
k=\frac{R}{1+E},
\qquad
0<k<\frac12.
$$

Then

$$
R=\frac{k(2-k)}{1-k^2},
\qquad
E=\frac{1-k+k^2}{1-k^2},
\qquad
\eta=\frac{k(1-2k)}{1-k^2}.
$$

If $R\le1/2$, then $k\le2-\sqrt3<27/100$, $A_0\ge P$, and direct
expansion gives

$$
Q(P)=
\frac{k(1-2k)(-f_8(k))}{(1-k^2)^5},
$$

where

$$
\begin{aligned}
f_8(k)={}&16k^8-77k^7+175k^6-244k^5+199k^4\\
&-101k^3+13k^2+12k-3.
\end{aligned}
$$

Put $p=-f_8$. Direct differentiation and regrouping give

$$
p'(k)=-12+g_1(k)+g_2(k)+g_3(k),
$$

where

$$
\begin{aligned}
g_1(k)&=-k(4k-1)(199k-26),\\
g_2(k)&=10k^4(122-105k),\\
g_3(k)&=k^6(539-128k).
\end{aligned}
$$

The first term is positive only for $26/199<k<1/4$. On that interval,

$$
g_1(k)
\le\frac14\max_k(1-4k)(199k-26)
=\frac{9025}{12736}<\frac34,
$$

and the same upper bound is automatic when $g_1(k)\le0$. The functions
$g_2$ and $g_3$ are increasing on $[0,27/100]$, and direct rational
evaluation gives

$$
g_2\left(\frac{27}{100}\right)<5,
\qquad
g_3\left(\frac{27}{100}\right)<\frac15.
$$

Consequently $p'(k)<-12+3/4+5+1/5<0$. Since

$$
p\left(\frac{27}{100}\right)
=\frac{81581849832351}{2500000000000000}>0,
$$

one has $-f_8(k)=p(k)>0$ throughout the required interval. Thus $Q(P)>0$.
Concavity now gives $Q(A)>0$ for $0<A<P$, a contradiction.

If $R>1/2$, then $0<A_0<P$ and direct expansion gives

$$
Q(A_0)=
\frac{(1-2k)(-g_5(k))}{2(1-k^2)^3},
$$

where

$$
g_5(k)=32k^5-118k^4+150k^3-86k^2+18k-1.
$$

At $k_0=2-\sqrt3$,

$$
g_5(k_0)=3471-2004\sqrt3<0,
$$

because

$$
3\mathbin{\cdot}2004^2-3471^2=207>0.
$$

For $u=4k-1\in[0,1]$, direct expansion gives

$$
-g_5'(k)
=\frac{29-5u^4+u\left(39(u-1)^2+12\right)}8>0.
$$

Thus $g_5$ is strictly decreasing on this interval. Since
$k>k_0>1/4$, one has $g_5(k)<0$, and hence $Q(A_0)>0$. Concavity gives
$Q(A)>0$ for $0<A<A_0$, again a contradiction. This proves $X>1/2$.

## 6. Routing at row 3

Assume from now on that row $4$ is $T_+$, and put

$$
p_1=G_{1-A}(H).
$$

By monotonicity and the catalog value at the end of the $T_+$ interval,

$$
p_1\le A+e(A)<3A+5A^2<\frac{29}{64}<\frac12.
$$

Also

$$
2R(H-m)=\eta+D-A>\eta-P>0,
$$

so $p_1\ge H>m$. Since $m<1/2$, both Full branches at row $3$ are
impossible.

If row $3$ is L, $T_-$, or the low-$c$ tie
$p_1=h(1-m)$, the catalog gives

$$
F_{1-m}(p_1)\le p_1.
$$

Therefore

$$
G_{1-m}(p_1)\ge1-p_1>\frac12>1-X.
$$

It remains only to analyze the branch in which rows $4$ and $3$ are both
$T_+$.

## 7. Concavity on the selected $T_+$ arcs

Consider a selected $T_+$ transition with deficit $0<d<1/2$, input $p$,
and output

$$
q=G_{1-d}(p).
$$

Put $c=1-d$ and $u=q-p$. The selected quadratic is

$$
f(q)=g(u),
\qquad
f(q)=(1-q)(q-d),
\qquad
g(u)=c^2u(2-u).
$$

On either selected $T_+$ arc, the exact catalog gives $f'(q)>0$ and
$g'(u)>0$. Write

$$
A_0=f'(q)=1+d-2q,
\qquad
B_0=g'(u)=2c^2(1-u).
$$

Implicit differentiation gives

$$
u'=\frac{A_0}{B_0},
\qquad
u''=\frac{2\left(c^2A_0^2-B_0^2\right)}{B_0^3}.
$$

Since $p>d$ and $u>0$,

$$
B_0-cA_0
=c(1-3d+2p+2du)>0
$$

and

$$
B_0-A_0
=1-5d+2d^2+2p+2d(2-d)u
>(1-d)(1-2d)>0.
$$

It follows that $u''<0$ and that $p=q-u$ is an increasing, strictly convex
function of $q$. Its inverse $q=G_{1-d}(p)$ is therefore increasing and
strictly concave on each selected $T_+$ arc. In particular, it lies above
the chord joining the endpoints of that arc.

### 7.1. Row 4

In the high-$c$ range the selected arc has endpoints

$$
(p,q)=(d,d)
\qquad\text{and}\qquad
(p,q)=(e(d),d+e(d)).
$$

Hence

$$
q\ge p+\frac{d}{e(d)-d}(p-d).
$$

For row $4$, $d=A<P\le(2\sqrt3-3)/4<1/8$, so the estimate in `2012`
gives

$$
\frac{d}{e(d)-d}
>\frac{1-2d}{1+2d}>1-4d.
$$

Applied with $d=A$ and $p=H$, this proves

$$
p_1>
(2-4A)H-(1-4A)A
=:L_1.
$$

### 7.2. Row 3

Since $X>1/2$, one has $R>1/2$, and therefore

$$
m<\frac w2<\frac14.
$$

We claim that every selected row-3 $T_+$ transition satisfies

$$
q>p+(1-5m)(p-m).
$$

This is immediate from $q>p$ when $m\ge1/5$. Suppose $m<1/5$. In the
high-$c$ range the catalog gives $e(m)>m$. If $m\le1/8$, the second
estimate in Section 3 gives

$$
\frac{m}{e(m)-m}
\ge\frac{1}{1+5m}>1-5m.
$$

This avoids applying the first estimate of Section 3 beyond its proved
range. If $1/8<m<1-\sqrt3/2$, the exact formula gives
$e(m)<(1-m)/2$, and hence

$$
\frac{m}{e(m)-m}
>\frac{2m}{1-3m}>1-5m.
$$

The last inequality is equivalent to

$$
15m^2-10m+1<0,
$$

which holds because this quadratic is decreasing below $1/3$ and has value
$-1/64$ at $m=1/8$.

It remains to consider the low-$c$ selected arc. Its endpoints are

$$
(p,q)=(m,m)
\qquad\text{and}\qquad
(p,q)=\left(h(1-m),1-h(1-m)\right),
$$

so its chord coefficient beyond extensivity is

$$
\frac{1-2h(1-m)}{h(1-m)-m}.
$$

On $3/4\le c\le\sqrt3/2$, direct differentiation of the formula in `2011`
shows that $h(c)$ is nonincreasing. Moreover

$$
h\left(\frac34\right)
=\frac{3}{2(\sqrt6+1)}<\frac7{16}.
$$

Here low $c$ gives $m\ge1-\sqrt3/2>2/15>1/16$, and hence

$$
h(1-m)<\frac7{16}<\frac{3+m}{7}.
$$

Thus the displayed chord coefficient is greater than $1/3$, while
$1-5m<1/3$. This proves the claim in every row-3 selected $T_+$ regime.

With

$$
p_2=G_{1-m}(p_1),
$$

the claim gives

$$
p_2>(2-5m)p_1-(1-5m)m.
$$

Because $2-5m>0$, the row-4 bound may be substituted to give

$$
p_2>L_2,
\qquad
L_2=(2-5m)L_1-(1-5m)m.
$$

## 8. Exact analytic terminal estimate

The row-4 $T_+$ selector and $e(A)<2A+5A^2$ give

$$
D\le D_h:=A(4R-1)+10RA^2-\eta.
$$

We first prove

$$
\boxed{D<\frac1{10}.}
$$

Suppose instead that $D\ge1/10$. Since $R>1/2$ and

$$
P=\frac{RwE}{1+E}<\frac{Rw}{2},
$$

the inequality $A+wD<P$ gives

$$
A<\frac{w(5R-1)}{10}=:\overline A.
$$

The function $D_h(A)$ is increasing. Also
$\eta=Rw/(1+E)>Rw/2$, so

$$
D<D_h(\overline A)
<U(R):=\overline A(4R-1)+10R\overline A^2-\frac{Rw}{2}.
$$

Direct expansion gives

$$
\frac1{10}-U(R)=-\frac{R}{10}P_4(R),
$$

where

$$
P_4(R)=25R^4-60R^3+26R^2+22R-14.
$$

For $y=2R-1\in(0,1)$,

$$
16P_4(R)=25y^4-20y^3-106y^2+124y-39
\le-101y^2+124y-39<0.
$$

The last quadratic has discriminant $-380$. Thus $U(R)<1/10$, a
contradiction.

Now define

$$
\Psi(D)=L_2-2D-3D^2,
\qquad
J(D)=L_2-\frac{23}{10}D.
$$

The bound just proved gives

$$
\Psi(D)-J(D)=3D\left(\frac1{10}-D\right)>0.
$$

For fixed $R,A$, exact differentiation yields

$$
J'(D)=\frac{S(R,A)}{10R^2},
$$

where

$$
S(R,A)=100A^2-(40R+50)A+R(20-23R).
$$

The nonempty interval $P-RA\le D\le D_h$ implies

$$
Rw\le A(5R-1+10RA).
$$

Since $A<P<Rw/2\le1/8$, it follows that

$$
A>\frac{4Rw}{25R-4}=:A_*.
$$

Moreover $\partial S/\partial A<-45$, and direct substitution gives

$$
S(R,A)<S(R,A_*)
=-\frac{R q_3(R)}{(25R-4)^2},
$$

where

$$
q_3(R)=8775R^3-14260R^2+7928R-1120.
$$

For $y=2R-1\in(0,1)$,

$$
8q_3(R)=8775y^3-2195y^2+997y+3007\ge812>0.
$$

Thus $J$ is strictly decreasing, and $J(D)\ge J(D_h)$.

At $D=D_h$, one has $H=2A+5A^2$. Write the corresponding value of $L_2$
as $L_{2,h}$. Exact expansion gives

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

On $0\le A\le Rw/2$,

$$
\frac{\partial^2Q}{\partial A^2}=20R(30A-4R-3)<0.
$$

It therefore suffices to check the endpoints. They are

$$
Q(R,0)=Rw(4R-1)>0
$$

and

$$
Q\left(R,\frac{Rw}{2}\right)=\frac{Rw}{2}p(R),
$$

where

$$
p(R)=25R^5-30R^4+20R^3-3R^2-7R+3.
$$

For $y=2R-1$,

$$
32p(R)=25y^5+65y^4+90y^3+106y^2-35y+5>0,
$$

because $106y^2-35y+5$ has discriminant $-895$. Hence

$$
L_{2,h}>A(1+4R).
$$

Finally, $A<P=\eta E$, $A<Rw/2$, and

$$
\frac1E>1+\frac{Rw}{2}
$$

give

$$
\frac{D_h}{A}
<C_0:=4R-2+5R^2w-\frac{Rw}{2}.
$$

Direct expansion gives

$$
1+4R-\frac{23}{10}C_0=\frac{h_3(R)}{20},
$$

where

$$
h_3(R)=230R^3-253R^2-81R+112.
$$

Here $h_3''(R)=46(30R-11)\ge184$. At $R_0=20/23$,

$$
h_3(R_0)=\frac{788}{529},
\qquad
h_3'(R_0)=\frac{17}{23}.
$$

Strong convexity therefore gives

$$
h_3(R)\ge
\frac{788}{529}-\frac{(17/23)^2}{368}
=\frac{289695}{194672}>0.
$$

Consequently

$$
J(D_h)>A\left(1+4R-\frac{23}{10}C_0\right)>0.
$$

Combining the estimates proves

$$
\boxed{\Psi(D)>J(D)\ge J(D_h)>0.}
$$

## 9. The final row-2 split

The terminal estimate and the sharper low-root bound from Section 3 yield

$$
\boxed{
p_2>L_2>2D+3D^2>e(D).
}
$$

Here $c_2=1-D>\sqrt3/2$. Put

$$
e_D=e(D)=\ell(1-D),
\qquad
r_D=(1-D)-e_D.
$$

The exact high-radial catalog partitions the row-2 input axis into

$$
\begin{array}{c|c|c}
\text{input range}&\text{label}&F_{1-D}(p)\\
\hline
0\le p\le D&\text{lower Full}&1-p\\
D<p\le e_D&T_+&T_+(p,1-D)\\
e_D<p<r_D&L&e_D\\
r_D\le p<1-D&T_-&T_-(p,1-D)\\
1-D\le p\le1&\text{upper Full}&1-p.
\end{array}
$$

Since $p_2>e_D$, the lower Full and $T_+$ ranges are impossible. On the
$L$ range, $F_{1-D}(p_2)=e_D$. On the $T_-$ range, monotonicity and the
transition value $F_{1-D}(r_D)=e_D$ give

$$
F_{1-D}(p_2)\le e_D.
$$

Thus in either of these middle ranges,

$$
G_{1-D}(p_2)
\ge1-e_D
>1-X,
$$

where the last strict inequality follows from

$$
e_D<2D+3D^2<\frac{23}{100}<\frac12<X.
$$

Finally, on upper Full one has

$$
G_{1-D}(p_2)=p_2\ge1-D>1-X,
$$

because $X>1/2>D$. Therefore every row-2 selector satisfies the required
strict inequality. Equivalently,

$$
(G_{c_2}\circ G_{c_3}\circ G_{c_4})(H)>1-X.
$$

By duality,

$$
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)>1-H.
$$

Restoring the extensive first and fifth maps proves

$$
Z_{\mathrm{CE1}}>1-H=1-\frac s2.
$$

## 10. Comparison with the supercritical target

The diameter constraint for a triangle meeting the two boundary rays at
parameters $s$ and $b$ is

$$
s^2+sb+b^2\le1.
$$

Consequently

$$
B_{c_0}(s)\le
\beta(s):=
\frac{-s+\sqrt{4-3s^2}}2.
$$

Because $s>0$,

$$
\beta(s)<1-\frac s2.
$$

Combining the last three inequalities gives

$$
\boxed{
Z_{\mathrm{CE1}}>B_{c_0}(s).
}
$$

This contradicts the necessary inequality from the boundary gap.  Hence the
CE1 exactly-one-gap state is impossible.
