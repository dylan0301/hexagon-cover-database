# CE1 One-Gap Five-Map Completion

Status: Proven

This note proves that the CE1 exactly-one-gap state in `410X` is impossible.
The analytic inequality holds on the full strict CE1 center domain; no
auxiliary survivor restriction or classified map for the supercritical V triangle
is needed.

Here a V-gap is the full nonempty set missed by the two adjacent open vertex
roles. It may be a positive-length interval or a singleton. The proof below
uses only weak endpoint bounds and therefore covers both cases.

For the geometric application, assume the `410X` hypotheses: all six vertex
roles are Vd0, $N_+=1$, and the unique center midpoint is $M_0$. Section 1 of
[`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md)
then proves that $T_0$ is the unique supercritical V triangle.

The exact capped maps are proved in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).
The selected-$T_+$ concavity and both chord forms are isolated in
[`2016_universal_Tplus_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md),
and the final one-hit threshold step is isolated in
[`2017_threshold_routing.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md).

## 1. Exact normalized CE1 domain

Use the variables in
[`2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).
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

will be used repeatedly. Since $\sqrt3/2\le E<1$ and $E-E^2$ is decreasing
on this interval,

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
m_3=\frac AR,
$$

then

$$
0<m_3<\frac w2<\frac12,
$$

because $A<P=RwE/(1+E)<Rw/2$. The six complementary radial demands from
`2105` are

$$
\boxed{
\begin{aligned}
c_0&=Rs=\eta+A+D,\\
c_1&=1-\frac DR,\\
c_2&=1-D,\\
c_3&=1-\min\left\{\frac AR,\frac Dw\right\}=1-\frac AR=1-m_3,\\
c_4&=1-A,\\
c_5&=1-\frac Aw.
\end{aligned}
}
$$

Here the formula for $c_3$ uses $RD>wA$. The exact-one-midpoint
normalization gives $c_0\le1/2$. The bounds $D<R/2$, $A<w/2$, and $m_3<1/2$
give

$$
\frac12<c_j<1,
\qquad j=1,2,3,4,5.
$$

Finally set

$$
H=\frac s2=\frac{\eta+A+D}{2R}.
$$

## 2. Capped-map duality and the three-V triangle suffix

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

Every $G_c$ is nondecreasing and extensive. It is therefore enough to prove

$$
\boxed{
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)>1-H.
}
$$

Indeed, put $\Phi=G_{c_4}\circ G_{c_3}\circ G_{c_2}$. Then

$$
(G_{c_5}\circ\Phi\circ G_{c_1})(X)
\ge(\Phi\circ G_{c_1})(X)
\ge\Phi(X).
$$

Repeated duality gives

$$
\begin{aligned}
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)\le1-H
&\Longleftrightarrow
G_{c_4}(H)\le1-(G_{c_3}\circ G_{c_2})(X)\\
&\Longleftrightarrow
(G_{c_3}\circ G_{c_4})(H)\le1-G_{c_2}(X)\\
&\Longleftrightarrow
(G_{c_2}\circ G_{c_3}\circ G_{c_4})(H)\le1-X.
\end{aligned}
$$

We prove that the reverse composition is strictly greater than $1-X$.

## 3. Actual-V triangle induction from the boundary gap

Use $a_i,b_i$ for the actual boundary reaches as in
[`1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md);
the symbols $c_i$ above are prescribed lower-bound radial demands.
Let $[s,t]\subset e_{0,1}$ be the maximal closed trace associated with the
open center role. Suppose it contains the vertex-uncovered set
$[b_0,1-a_1]$, possibly a singleton. Full boundary coverage gives

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

V triangles $T_1,\dots,T_5$ are nonsupercritical. Define

$$
z_0=X,
\qquad
z_j=G_{c_j}(z_{j-1}),
\qquad j=1,2,3,4,5.
$$

The actual incoming reaches dominate these iterates. The gap gives
$a_1\ge z_0$. If $a_j\ge z_{j-1}$, the capped-map theorem and monotonicity of
$F_{c_j}$ give

$$
b_j\le F_{c_j}(a_j)\le F_{c_j}(z_{j-1}).
$$

The center has no trace on the other five boundary edges, so
$a_{j+1}+b_j\ge1$ for $j=1,2,3,4$ and $a_0+b_5\ge1$. Hence

$$
a_{j+1}\ge1-b_j\ge G_{c_j}(z_{j-1})=z_j
\qquad(1\le j\le4),
$$

and

$$
a_0\ge1-b_5\ge G_{c_5}(z_4)=z_5.
$$

Thus

$$
a_0\ge
Z_{\mathrm{CE1}}
:=
(G_{c_5}\circ G_{c_4}\circ G_{c_3}\circ G_{c_2}\circ G_{c_1})(X).
$$

For the upper bound, $T_0$ realizes
$(a_0,b_0,\widehat c_0)$ in the exact admissible set. Since $b_0\ge s$ and
$\widehat c_0\ge c_0$, down-closedness and reflection give

$$
(s,a_0,c_0)\in\mathcal A.
$$

By the exact outgoing envelope in
[`2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),

$$
a_0\le B_{c_0}(s).
$$

It remains to prove

$$
Z_{\mathrm{CE1}}>B_{c_0}(s).
$$

## 4. Low-root estimates and the first threshold

For $0<d\le1-\sqrt3/2$, put

$$
e(d)=\ell(1-d).
$$

The scalar bounds in
[`2012_high_radial_low_root_bounds.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md)
are

$$
\boxed{
e(d)<\frac{2d}{1-2d}
\qquad
\left(0<d\le\frac{2\sqrt3-3}{4}\right),
}
$$

$$
\boxed{
e(d)\le2d+5d^2
\qquad
\left(0<d\le\frac18\right),
}
$$

and

$$
\boxed{
e(d)<2d+3d^2
\qquad
\left(0<d\le\frac1{10}\right).
}
$$

The inequality $A+wD<P$, with $D=R-X$, gives

$$
A<wX-\eta.
$$

Let

$$
f(X)=wX-\frac{X}{2(1+X)}.
$$

Because $D<R/2$, one has $R/2<X<R$, and $f$ is convex. At the endpoints,

$$
f\left(\frac R2\right)<\frac{Rw}{2}<\eta,
$$

while $f(R)<\eta$ is equivalent to

$$
E(1-2R^2)<1,
$$

which follows from $E<1$. Hence

$$
A<\frac{X}{2(1+X)}.
$$

The first low-root estimate now gives

$$
\boxed{e(A)<X.}
$$

We also have $H>A$. Indeed,

$$
2R(H-A)=\eta+D+(1-2R)A.
$$

This is positive when $R\le1/2$. When $R>1/2$, use $A<P=\eta E$ to obtain

$$
2R(H-A)>
\eta\left(1-(2R-1)E\right)>0.
$$

## 5. The V triangle-4 $T_+$ branch forces $X>1/2$

At V triangle $4$, the Full branches are impossible because

$$
H>A,
\qquad
H<\frac12<1-A.
$$

If the selected branch is L or $T_-$, then

$$
F_{1-A}(H)\le e(A),
$$

and therefore

$$
G_{1-A}(H)\ge1-e(A)>1-X.
$$

Only the selected $T_+$ branch remains. Its selector gives

$$
H\le e(A)<\frac{2A}{1-2A}.
$$

We prove

$$
\boxed{X>\frac12.}
$$

Suppose instead that $X\le1/2$. The lower center inequality gives

$$
\begin{aligned}
2RH
&=\eta+A+D\\
&\ge\eta+A+P-RA\\
&=\eta+P+wA\\
&=w(R+A).
\end{aligned}
$$

Combining this with the selected-$T_+$ bound yields

$$
\frac{w(R+A)}{2R}
\le H
<\frac{2A}{1-2A}.
$$

Thus

$$
f_R(A)<0,
$$

where

$$
f_R(z)=w(R+z)(1-2z)-4Rz.
$$

This quadratic is strictly concave:

$$
f_R''(z)=-4w<0,
$$

and

$$
f_R(0)=Rw>0.
$$

We now check the other endpoint of the possible interval for $A$.

### 5.1. The range $R\le1/2$

Since $D>0$ and $A+wD<P$,

$$
0<A<P.
$$

Using $P=(1-E)E$ and $E^2=1-R+R^2$, direct simplification gives

$$
f_R(P)
=(1-E)
\left(
4E^3-2E^2+1-R(2E^3-2E^2+5E)
\right).
$$

The coefficient $2E^3-2E^2+5E$ is positive. Hence $R\le1/2$ gives

$$
f_R(P)
\ge
\frac{1-E}{2}
\left(6E^3-2E^2-5E+2\right).
$$

Put

$$
\phi(E)=6E^3-2E^2-5E+2.
$$

On $\sqrt3/2\le E<1$,

$$
\phi'(E)=18E^2-4E-5>0,
$$

because its value at $E=\sqrt3/2$ is

$$
\frac{17}{2}-2\sqrt3>0.
$$

Also

$$
\phi\left(\frac{\sqrt3}{2}\right)
=\frac{2-\sqrt3}{4}>0.
$$

Therefore $f_R(P)>0$. Strict concavity puts $f_R$ above its endpoint chord,
so

$$
f_R(A)>0
\qquad(0<A<P),
$$

contrary to $f_R(A)<0$.

### 5.2. The range $R>1/2$

The assumption $X\le1/2$ gives

$$
D=R-X\ge R-\frac12.
$$

Hence

$$
0<A<A_0,
\qquad
A_0:=P-w\left(R-\frac12\right)=\frac w2-\eta.
$$

Using again $E^2=1-R+R^2$, direct simplification gives

$$
f_R(A_0)
=
\frac{1-E}{2}
\left(E+11R-3ER-5\right).
$$

Since $11-3E>0$ and $R>1/2$,

$$
\begin{aligned}
E+11R-3ER-5
&=R(11-3E)+E-5\\
&>\frac{11-3E}{2}+E-5\\
&=\frac{1-E}{2}>0.
\end{aligned}
$$

Thus $f_R(A_0)>0$. Concavity again gives

$$
f_R(A)>0
\qquad(0<A<A_0),
$$

contrary to $f_R(A)<0$. Both ranges are impossible, proving
$X>1/2$.

## 6. Routing at V triangle 3

Assume from now on that V triangle $4$ is selected $T_+$, and put

$$
p_1=G_{1-A}(H).
$$

By monotonicity and the catalog value at the end of the selected interval,

$$
p_1\le A+e(A)<3A+5A^2<\frac{29}{64}<\frac12.
$$

Also

$$
2R(H-m_3)=\eta+D-A>\eta-P>0,
$$

so $p_1\ge H>m_3$. Since $m_3<1/2$, both Full branches at V triangle $3$ are
impossible.

If V triangle $3$ is L, $T_-$, or the low-radial tie, the exact catalog gives

$$
F_{1-m_3}(p_1)\le p_1.
$$

Therefore

$$
G_{1-m_3}(p_1)\ge1-p_1>\frac12>1-X.
$$

It remains only to analyze the branch in which V triangles $4$ and $3$ are both
selected $T_+$.

## 7. Universal selected-$T_+$ chord bounds

The universal normal form in `2016` proves that every selected $T_+$ map is
increasing and strictly concave. It also gives the two exact chord forms used
below, so no branch-specific implicit differentiation is required.

### 7.1. V triangle 4

On the high-radial selected arc the endpoints are

$$
(p,q)=(d,d)
\qquad\text{and}\qquad
(p,q)=(e(d),d+e(d)).
$$

Hence

$$
q\ge p+\frac{d}{e(d)-d}(p-d).
$$

For V triangle $4$, $d=A<P<(1/8)$, and the first low-root bound gives

$$
\frac{d}{e(d)-d}
>
\frac{1-2d}{1+2d}
>
1-4d.
$$

Applied with $d=A$ and $p=H$, this proves

$$
p_1>
(2-4A)H-(1-4A)A
=:L_1.
$$

### 7.2. V triangle 3

Since $X>1/2$, one has $R>1/2$, and therefore

$$
m_3<\frac w2<\frac14.
$$

We claim that every selected V triangle-$3$ $T_+$ transition satisfies

$$
q>p+(1-5m_3)(p-m_3).
$$

This is immediate from $q>p$ when $m_3\ge1/5$. Suppose $m_3<1/5$.

On the high-radial selected arc, the universal chord coefficient is

$$
\frac{m_3}{e(m_3)-m_3}.
$$

If $m_3\le1/8$, then

$$
\frac{m_3}{e(m_3)-m_3}
\ge\frac{1}{1+5m_3}>1-5m_3.
$$

If $1/8<m_3<1-\sqrt3/2$, then $e(m_3)<(1-m_3)/2$, and hence

$$
\frac{m_3}{e(m_3)-m_3}
>
\frac{2m_3}{1-3m_3}
>
1-5m_3.
$$

The last inequality is equivalent to

$$
15m_3^2-10m_3+1<0,
$$

which holds because this quadratic is decreasing below $1/3$ and has value
$-1/64$ at $m_3=1/8$.

On the low-radial selected arc, put $t=h(1-m_3)$. The universal chord
coefficient is

$$
\frac{1-2t}{t-m_3}.
$$

On $3/4\le c\le\sqrt3/2$, the exact formula in `2011` shows that $h(c)$ is
nonincreasing, and

$$
h\left(\frac34\right)
=\frac{3}{2(\sqrt6+1)}<\frac7{16}.
$$

Here the low-radial range gives

$$
m_3\ge1-\frac{\sqrt3}{2}>\frac2{15}>\frac1{16},
$$

so

$$
t=h(1-m_3)<\frac7{16}<\frac{3+m_3}{7}.
$$

Thus

$$
\frac{1-2t}{t-m_3}>\frac13>1-5m_3.
$$

This proves the V triangle-$3$ claim in every selected $T_+$ regime.

With

$$
p_2=G_{1-m_3}(p_1),
$$

the claim gives

$$
p_2>(2-5m_3)p_1-(1-5m_3)m_3.
$$

Because $2-5m_3>0$, the V triangle-$4$ bound gives

$$
p_2>L_2,
\qquad
L_2=(2-5m_3)L_1-(1-5m_3)m_3.
$$

## 8. Exact analytic terminal estimate

The V triangle-$4$ selector and $e(A)\le2A+5A^2$ give

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
A<\frac{w(5R-1)}{10}=: \overline A.
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

The last quadratic has negative discriminant. Thus $U(R)<1/10$, a
contradiction.

Now define

$$
\Psi(D)=L_2-2D-3D^2,
\qquad
J(D)=L_2-\frac{23}{10}D.
$$

Since $D<1/10$,

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

Since $A<P<Rw/2\le1/8$,

$$
A>\frac{4Rw}{25R-4}=:A_*.
$$

Moreover $\partial S/\partial A<-45$, and

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

At $D=D_h$, one has $H=2A+5A^2$. Write the corresponding value of $L_2$ as
$L_{2,h}$. Exact expansion gives

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

It therefore suffices to check the endpoints:

$$
Q(R,0)=Rw(4R-1)>0,
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

because $106y^2-35y+5$ has negative discriminant. Hence

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

Strong convexity gives

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
\boxed{
\Psi(D)>J(D)\ge J(D_h)>0.
}
$$

Therefore

$$
\boxed{
p_2>L_2>2D+3D^2>e(D).
}
$$

## 9. The V triangle-2 threshold trigger

The preceding section gives $D<1/10$ and

$$
p_2>e(D).
$$

The one-hit threshold-routing lemma `2017`, applied to the V triangle-$2$ map
$G_{1-D}$, gives directly

$$
G_{1-D}(p_2)\ge1-e(D).
$$

Moreover

$$
e(D)<2D+3D^2<\frac{23}{100}<\frac12<X.
$$

Hence

$$
\boxed{
G_{1-D}(p_2)>1-X.
}
$$

Equivalently,

$$
(G_{c_2}\circ G_{c_3}\circ G_{c_4})(H)>1-X.
$$

By duality,

$$
(G_{c_4}\circ G_{c_3}\circ G_{c_2})(X)>1-H.
$$

Restoring the extensive first and fifth maps gives

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

Combining the inequalities gives

$$
\boxed{
Z_{\mathrm{CE1}}>B_{c_0}(s).
}
$$

This contradicts the necessary inequality from the boundary gap. Hence the
CE1 exactly-one-gap state is impossible.
