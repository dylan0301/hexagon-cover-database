# CE2 One-Gap Five-Map Completion

Status: Proven

This note proves that both orientations of the CE2 exactly-one-gap state in
`410X` are impossible.  The analytic inequalities hold on the full strict
CE2 center domain; no auxiliary survivor restriction or classified map for
the supercritical row is needed.

Here a V-gap is the full nonempty set missed by the two adjacent open vertex
roles. It may be a positive-length interval or a singleton. The proof uses
only weak endpoint bounds and therefore includes both cases.

For the geometric application, assume the `410X` hypotheses: all six vertex
roles are Vd0, $N_+=1$, and the unique center midpoint is $M_0$.  Section 1
of
[`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md)
then proves that $T_0$ is the unique supercritical row.

## 1. Exact normalized CE2 domain

Use the exact CE2 variables for the maximal closed traces associated with the
open center role from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md):

$$
\overline{T_C}\cap e_{5,0}=[x,u],
\qquad
\overline{T_C}\cap e_{0,1}=[y,v].
$$

Set

$$
S=x+y,
\qquad
R=\frac{x}{S},
\qquad
w=1-R=\frac{y}{S},
$$

$$
E=\sqrt{1-R+R^2}=\sqrt{1-Rw},
\qquad
\eta=1-E,
\qquad
P=\eta E,
$$

and

$$
\alpha=u-R,
\qquad
\delta=v-w.
$$

Because $0<R<1$, one has

$$
\frac{\sqrt3}{2}\le E<1,
\qquad
\eta>0,
\qquad
Rw=1-E^2=\eta(1+E).
$$

The CE2 coupling equation becomes

$$
RwS=\eta+\alpha+\delta.
$$

Write

$$
k=\eta+\alpha+\delta.
$$

Then

$$
x=\frac{k}{w},
\qquad
y=\frac{k}{R},
\qquad
u=R+\alpha,
\qquad
v=w+\delta.
$$

The strict interval conditions $x<u$ and $y<v$ are respectively equivalent
to

$$
\delta+R\alpha<P,
\qquad
\alpha+w\delta<P.
$$

Indeed, for example,

$$
x<u
\quad\Longleftrightarrow\quad
k<w(R+\alpha)
\quad\Longleftrightarrow\quad
\delta+R\alpha<P,
$$

where $Rw=\eta+P$ was used.  The other equivalence follows by reflection.
Thus the exact normalized strict CE2 domain is

$$
\boxed{
\alpha>0,
\qquad
\delta>0,
\qquad
\delta+R\alpha<P,
\qquad
\alpha+w\delta<P.
}
$$

These inequalities also imply the midpoint bounds

$$
\alpha<\frac w2,
\qquad
\delta<\frac R2.
$$

For example,

$$
\alpha<\frac PR
=\frac{wE}{1+E}
<\frac w2,
$$

and the second inequality is symmetric.

The exact complementary radial demands from `2106` are

$$
\begin{aligned}
c_0&=k,\\
c_1&=1-\frac{\delta}{R},\\
c_2&=1-\delta,\\
c_3&=1-\min\left\{\frac{\delta}{w},\frac{\alpha}{R}\right\},\\
c_4&=1-\alpha,\\
c_5&=1-\frac{\alpha}{w}.
\end{aligned}
$$

For each nonsupercritical row put

$$
F_i(a)=F_{c_i}(a),
\qquad
G_i(a)=G_{c_i}(a)=1-F_{c_i}(a),
$$

where the exact capped maps $F_c$ and $G_c$ are proved in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).
In particular, every $G_i$ is nondecreasing and extensive:

$$
G_i(a)\ge a.
$$

## From a boundary gap to the analytic targets

Use the actual boundary reaches $a_i,b_i$ from
[`1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md),
and write $\widehat c_i$ for the actual radial reach of $T_i$.  Thus the
symbols $c_i$ above remain lower-bound demands.  The radial-exit theorem
`2106` gives

$$
\widehat c_i\ge c_i
\qquad (i=0,\dots,5).
$$

Suppose first that the unique active vertex-uncovered set
$[b_0,1-a_1]$, possibly a singleton, lies in the open center trace associated
with $[y,v]\subset e_{0,1}$, while the trace associated with $[x,u]$ contains
no V-gap.  The weak endpoint bounds proved in Section 2 of
[`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md)
give

$$
b_0\ge y,
\qquad
a_1\ge1-v.
$$

The same section of `4101` shows that absence of a V-gap is equivalent to a
strict handoff.  Since the displayed gap is the unique gap, the other five
edges therefore satisfy

$$
a_{i+1}>1-b_i
\qquad (i=1,\dots,4),
$$

and the fifth-row return satisfies

$$
a_0>1-b_5.
$$

Define, once for this orientation,

$$
z_0=1-v=R-\delta,
\qquad
z_i=G_i(z_{i-1})
\quad (i=1,\dots,5),
$$

and hence

$$
Z_{\mathrm{CE2}}^R
:=
z_5=
(G_5\circ G_4\circ G_3\circ G_2\circ G_1)(1-v).
$$

Here is the full passage from the actual rows to this formal composition.
The initial endpoint bound is $a_1\ge z_0$.  For $1\le i\le4$, suppose
inductively that $a_i\ge z_{i-1}$.  The row $T_i$ is nonsupercritical by
Section 1 of `4101`, and its actual reaches satisfy

$$
a_i\ge z_{i-1},
\qquad
\widehat c_i\ge c_i.
$$

The proof-safe capped-map bound in `2011` therefore gives

$$
b_i\le F_{c_i}(z_{i-1})=F_i(z_{i-1}).
$$

Combining this with the strict handoff on the next edge yields

$$
\begin{aligned}
a_{i+1}
&>1-b_i\\
&\ge1-F_i(z_{i-1})\\
&=G_i(z_{i-1})\\
&=z_i.
\end{aligned}
$$

This proves successively $a_2\ge z_1,\dots,a_5\ge z_4$.  Applying the same
capped-map bound to the nonsupercritical fifth row and then using the final
return handoff gives

$$
\begin{aligned}
a_0
&>1-b_5\\
&\ge1-F_5(z_4)\\
&=G_5(z_4)\\
&=z_5
=Z_{\mathrm{CE2}}^R.
\end{aligned}
$$

Thus, in particular,

$$
a_0\ge Z_{\mathrm{CE2}}^R.
$$

The same triangle $T_0$ has outgoing reach $b_0\ge y$ and actual radial reach
$\widehat c_0\ge c_0$.  Reflection of the local admissible set proved in
[`2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md)
interchanges the two boundary demands and preserves the radial demand.  The
same result proves coordinatewise down-closure, so
$(y,a_0,c_0)$ is admissible.  The definition of the exact unclassified map in
[`2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md)
therefore gives

$$
a_0\le B_{c_0}(y).
$$

Thus the right-gap orientation is impossible once

$$
Z_{\mathrm{CE2}}^R>B_{c_0}(y)
$$

is proved.  For the left-gap orientation, put

$$
Z_{\mathrm{CE2}}^L
:=
(G_1\circ G_2\circ G_3\circ G_4\circ G_5)(1-u).
$$

The reflected row-by-row argument in Section 7 will give
$b_0\ge Z_{\mathrm{CE2}}^L$ and $b_0\le B_{c_0}(x)$.  Thus the remaining
analytic targets proved in Sections 5--7 are precisely

$$
Z_{\mathrm{CE2}}^R>B_{c_0}(y),
\qquad
Z_{\mathrm{CE2}}^L>B_{c_0}(x).
$$

## 2. The scalar low-root bounds

For

$$
0<X<1-\frac{\sqrt3}{2},
$$

put

$$
e(X)=\ell(1-X)
=\frac{1-X}{2}
\left(1-\sqrt{4(1-X)^2-3}\right).
$$

Also put

$$
\mu=\frac{2\sqrt3-3}{4}.
$$

The scalar-root lemma in
[`2012`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md)
gives, on the smaller range $0<X\le\mu$,

$$
\boxed{
X<e(X)<\frac{2X}{1-2X}.
}
$$

The high-demand threshold lemma in the same file holds on the full range
$0<X<1-\sqrt3/2$ and gives

$$
\boxed{
a>e(X)
\quad\Longrightarrow\quad
G_{1-X}(a)\ge1-e(X).
}
$$

Both lemmas apply to $X=\alpha$ and $X=\delta$.  Indeed, $E(1-E)$ is
decreasing for $E\ge\sqrt3/2$, so

$$
P\le
\frac{\sqrt3}{2}
\left(1-\frac{\sqrt3}{2}\right)
=\mu
=\frac{2\sqrt3-3}{4}.
$$

The exact-domain inequalities imply

$$
0<\alpha,\delta<P\le\mu,
$$

and

$$
\mu<1-\frac{\sqrt3}{2}
$$

because $7>4\sqrt3$.

## 3. A universal lower bound for the initial input

For the right-gap input $z_0$ defined above, the second strict domain
inequality gives

$$
wz_0
=Rw-w\delta
=\eta+P-w\delta
>\eta+\alpha.
$$

We next prove

$$
\frac{\eta+\alpha}{w}
>\frac{2\alpha}{1-2\alpha}.
$$

Define

$$
\pi(q)=(\eta+q)(1-2q)-2qw.
$$

This is concave in $q$, and

$$
\pi(0)=\eta>0,
$$

while direct simplification using $P=\eta E$ and $E^2=1-Rw$ gives

$$
\pi(P)=\eta\left(\eta+2ER^2\right)>0.
$$

Therefore $\pi(q)>0$ for $0<q<P$.  Since $1-2\alpha>0$, this proves the
displayed inequality.  The scalar-root upper bound now gives the strict chain

$$
\boxed{
z_0
>\frac{\eta+\alpha}{w}
>\frac{2\alpha}{1-2\alpha}
>e(\alpha).
}
$$

Only the displayed comparison with $e(\alpha)$ is used below.  The
two-threshold lemma supplies the needed conditional comparison with
$e(\delta)$; no symmetric strengthening is assumed.

## 4. The two-threshold lemma

Put

$$
Q=\frac y2=\frac{k}{2R}.
$$

We claim

$$
\boxed{
\min\left\{e(\alpha),e(\delta)\right\}<Q.
}
$$

Suppose instead that both low roots are at least $Q$.  By the strict scalar
upper bound,

$$
Q<\frac{2\alpha}{1-2\alpha},
\qquad
Q<\frac{2\delta}{1-2\delta}.
$$

Solving these inequalities gives

$$
\alpha>L,
\qquad
\delta>L,
\qquad
L=\frac{Q}{2(1+Q)}.
$$

Since $k=2RQ=\eta+\alpha+\delta$, it follows that

$$
\eta
<Q\left(2R-\frac1{1+Q}\right).
$$

On the other hand, the first strict CE2 domain inequality gives

$$
\begin{aligned}
\eta E
&>\delta+R\alpha\\
&=R(\alpha+\delta)+w\delta\\
&>R(2RQ-\eta)+wL.
\end{aligned}
$$

Consequently

$$
\eta(E+R)
>Q\left(2R^2+\frac{w}{2(1+Q)}\right).
$$

Combining the strict upper and lower bounds for $\eta$ yields

$$
H(Q)>0,
$$

where

$$
H(q)=
\left(2R-\frac1{1+q}\right)(E+R)
-2R^2-\frac{w}{2(1+q)}.
$$

But

$$
H'(q)=
\frac{E+R+w/2}{(1+q)^2}>0.
$$

Moreover $x=k/w<1$ gives

$$
Q<\frac{w}{2R}.
$$

At the latter endpoint,

$$
H\left(\frac{w}{2R}\right)
=\frac{R(2RE-R-1)}{R+1}<0.
$$

For the final strict sign, both $2RE$ and $R+1$ are positive and

$$
(R+1)^2-4R^2E^2
=(1-R)(4R^3+3R+1)>0.
$$

Thus

$$
H(Q)
<H\left(\frac{w}{2R}\right)
<0,
$$

contradicting $H(Q)>0$.  The two-threshold lemma follows.

## 5. Completion of the right-gap five-map inequality

For the successive inputs $z_1,\dots,z_5$ defined in the geometric induction
above, every map is extensive.  Thus every later input is at least $z_0$, and
any strict lower bound, once obtained, persists through the rest of the chain.

If $e(\alpha)<Q$, then $z_3\ge z_0>e(\alpha)$.  Since $c_4=1-\alpha$, the
threshold lemma at row $4$ gives

$$
z_4\ge1-e(\alpha)>1-Q.
$$

Therefore $z_5>1-Q$.

If $e(\alpha)\ge Q$, the two-threshold lemma gives $e(\delta)<Q$.  The
universal input estimate then supplies the essential conditional chain

$$
z_1\ge z_0>e(\alpha)\ge Q>e(\delta).
$$

Since $c_2=1-\delta$, the threshold lemma at row $2$ gives

$$
z_2\ge1-e(\delta)>1-Q.
$$

Rows $3$, $4$, and $5$ preserve this strict inequality.  Hence in both cases

$$
\boxed{
Z_{\mathrm{CE2}}^R>1-\frac y2.
}
$$

## 6. Diameter bound for the supercritical target

Define the diameter endpoint

$$
\beta(q)=\frac{-q+\sqrt{4-3q^2}}2,
$$

so that

$$
q^2+q\beta(q)+\beta(q)^2=1.
$$

The diameter bound in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md)
holds for every radial demand and gives

$$
B_{c_0}(y)\le\beta(y).
$$

Because $y>0$,

$$
\beta(y)<1-\frac y2.
$$

Combining these two inequalities with Section 5 proves

$$
\boxed{
Z_{\mathrm{CE2}}^R
>1-\frac y2
>B_{c_0}(y).
}
$$

This proves the required right-gap inequality.

Together with the actual-row bounds from the geometric induction,

$$
a_0\ge Z_{\mathrm{CE2}}^R
>B_{c_0}(y)
\ge a_0,
$$

which is the required contradiction in the right-gap orientation.

## 7. Exact reflection and the left-gap target

Suppose now that the unique gap lies in the trace $[x,u]\subset e_{5,0}$.
In the coordinate on this edge measured from $V_0$, the vertex-uncovered set
is $[a_0,1-b_5]$.  Its containment in the open center trace $(x,u)$ gives

$$
a_0\ge x,
\qquad
b_5\ge1-u.
$$

Reflect the configuration across the symmetry axis through $V_0$, and use
primes for the reflected data.  On the normalized variables this exchanges

$$
x\longleftrightarrow y,
\qquad
u\longleftrightarrow v,
\qquad
R\longleftrightarrow w,
\qquad
\alpha\longleftrightarrow\delta.
$$

The strict normalized CE2 domain is invariant.  Reflection fixes row $0$ and
reverses rows $1,\dots,5$.  It interchanges incoming and outgoing actual
boundary reaches, so

$$
a'_0=b_0,
\qquad
b'_0=a_0,
$$

and

$$
a'_i=b_{6-i},
\qquad
b'_i=a_{6-i}
\qquad (i=1,\dots,5).
$$

The radial demands transform in the exact order

$$
(c_1,c_2,c_3,c_4,c_5)
\longleftrightarrow
(c_5,c_4,c_3,c_2,c_1).
$$

In particular, $c'_0=c_0$ and $c'_i=c_{6-i}$ for $1\le i\le5$.  The
reflected maps consequently satisfy

$$
G'_1=G_5,
\qquad
G'_2=G_4,
\qquad
G'_3=G_3,
\qquad
G'_4=G_2,
\qquad
G'_5=G_1.
$$

The right-gap composition in the reflected configuration is therefore

$$
G'_5\circ G'_4\circ G'_3\circ G'_2\circ G'_1
=G_1\circ G_2\circ G_3\circ G_4\circ G_5.
$$

Its initial actual reach is

$$
a'_1=b_5\ge1-u=1-v',
$$

and its right-gap endpoint demand is

$$
b'_0=a_0\ge x=y'.
$$

The five-row geometric induction already proved above, now applied in the
reflected order $T_5,T_4,T_3,T_2,T_1$, gives

$$
\begin{aligned}
b_0=a'_0
&\ge
(G'_5\circ G'_4\circ G'_3\circ G'_2\circ G'_1)(1-v')\\
&=(G_1\circ G_2\circ G_3\circ G_4\circ G_5)(1-u)\\
&=Z_{\mathrm{CE2}}^L.
\end{aligned}
$$

Meanwhile $a_0\ge x$ and $\widehat c_0\ge c_0$.  Coordinatewise
down-closure gives the admissible triple $(x,b_0,c_0)$, so the
defining upper bound for the exact map $B_{c_0}$ gives

$$
b_0\le B_{c_0}(x).
$$

It remains to compare the two bounds.  Applying the already proved analytic
right-gap inequality to the reflected parameters gives

$$
\boxed{
Z_{\mathrm{CE2}}^L
=(G_1\circ G_2\circ G_3\circ G_4\circ G_5)(1-u)
>1-\frac x2.
}
$$

The reflected diameter bound gives

$$
B_{c_0}(x)\le\beta(x)<1-\frac x2.
$$

Consequently

$$
\boxed{
Z_{\mathrm{CE2}}^L>B_{c_0}(x).
}
$$

Combining this with the two actual-row bounds gives

$$
b_0\ge Z_{\mathrm{CE2}}^L
>B_{c_0}(x)
\ge b_0,
$$

a contradiction.  This proves the required left-gap inequality and eliminates
the reflected orientation.

## 8. Conclusion

Both exactly-one-gap CE2 orientations are therefore eliminated on the full
strict CE2 center domain.
