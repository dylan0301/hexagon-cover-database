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

because $A<P=RwE/(1+E)<Rw/2$. In particular, all three demands below lie
strictly between $1/2$ and $1$:

$$
c_2=1-D,
\qquad
c_3=1-m,
\qquad
c_4=1-A.
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

Indeed, $G_{c_1}(X)\ge X$, the three displayed maps are nondecreasing, and
$G_{c_5}$ is extensive.

Repeated duality shows that failure of this suffix inequality is equivalent
to

$$
(G_{c_2}\circ G_{c_3}\circ G_{c_4})(H)\le1-X.
$$

We prove that the reverse composition is strictly greater than $1-X$.

## From the boundary gap to the analytic target

Let $[s,t]\subset e_{0,1}$ be the maximal closed trace associated with the
open center role. Suppose it contains the vertex-uncovered set
$[b_0,1-a_1]$, possibly a singleton. Full boundary coverage puts this set in
the open center trace and in particular gives

$$
b_0\ge s,
\qquad
a_1\ge X=1-t.
$$

Rows $T_1,\dots,T_5$ are nonsupercritical.  Starting with the actual incoming
reach $a_1$, the capped-map theorem and boundary coverage give successively

$$
a_{j+1}\ge G_{c_j}(a_j),
\qquad j=1,2,3,4,
$$

and

$$
a_0\ge G_{c_5}(a_5).
$$

Monotonicity therefore implies

$$
a_0\ge
Z_{\mathrm{CE1}}
:=
(G_{c_5}\circ G_{c_4}\circ G_{c_3}\circ G_{c_2}\circ G_{c_1})(X).
$$

The same triangle $T_0$ has radial reach at least $c_0$ and outgoing reach
$b_0\ge s$.  Reflection of the exact admissible set, followed by monotonicity
in both demands, gives

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
proves, on the ranges used below,

$$
\boxed{
e(d)<\frac{2d}{1-2d}.
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

The degree-eight Bernstein coefficients of $-f_8$ on $[0,27/100]$ are

$$
\begin{aligned}
&3,
\frac{519}{200},
\frac{603723}{280000},
\frac{96261783}{56000000},
\frac{9126684741}{7000000000},\\
&\frac{129114182427}{140000000000},
\frac{650458634673}{1120000000000},
\frac{226624193321631}{800000000000000},
\frac{81581849832351}{2500000000000000}.
\end{aligned}
$$

They are all positive, so $Q(P)>0$. Concavity now gives $Q(A)>0$ for
$0<A<P$, a contradiction.

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

The Bernstein coefficients of $-g_5'$ on $[1/4,1/2]$ are

$$
\frac{29}{8},
\qquad
\frac{167}{32},
\qquad
\frac{83}{16},
\qquad
\frac{19}{4},
\qquad
\frac92.
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

## 7. Two exact $T_+$ growth estimates

Consider a selected $T_+$ transition with deficit $d$, input $p$, and
output

$$
q=G_{1-d}(p).
$$

The selected quadratic is equivalently

$$
(1-q)(q-d)=(q-p)(2-q+p)(1-d)^2.
$$

The selected $q$ is the larger root, and $q>p>d$. The residual is a concave
quadratic in $q$, and at the trial point $q=p$ it equals

$$
(1-p)(p-d)>0.
$$

Thus $p$ lies strictly between the two roots. For a trial value $L$ with
$p<L<1$, positivity of the residual at $L$ implies $q>L$. When a trial
value is at most $p$, the same conclusion follows immediately from $q>p$.

### 7.1. Row 4

For $0<d<1/8$ and $p\le e(d)$, set

$$
L=p+(1-4d)(p-d).
$$

Here $p<L<1$: the lower inequality uses $p>d$, while
$L<2p<4d/(1-2d)<1$.

Substitution in the quadratic gives

$$
(p-d)S_4(d,p),
$$

where

$$
\begin{aligned}
S_4(d,p)={}&-16d^5+40d^4-9d^3-20d^2+9d\\
&+p(16d^4-40d^3+17d^2+6d-3).
\end{aligned}
$$

The coefficient of $p$ is negative on $[0,1/8]$. Using
$p\le e(d)<2d+5d^2$ therefore gives

$$
S_4(d,p)>S_4(d,2d+5d^2),
$$

and the latter is

$$
d\left(80d^5-184d^4+45d^3+55d^2-23d+3\right)>0.
$$

For the last sign, discard the positive terms and use

$$
3-23d-184d^4\ge\frac{41}{512}>0.
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

Every selected row-3 $T_+$ input satisfies

$$
p_1\le\frac{13m}{4}.
$$

In the high-$c$ range this follows from
$p_1\le e(m)<2m/(1-2m)<13m/4$. In the low-$c$ range the endpoint is the
fixed point $h(1-m)$. The desired comparison
$h(1-m)\le13m/4$ reduces, after squaring two positive sides, to positivity
of

$$
676m^4-1352m^3+439m^2+84m-16.
$$

Its Bernstein coefficients on $[2/15,1/2]$ are

$$
\frac{676}{50625},
\qquad
\frac{559}{45},
\qquad
\frac{26099}{1080},
\qquad
\frac{921}{40},
\qquad
9.
$$

This interval contains the entire low-$c$ range needed here.

Set

$$
L=p+(1-5d)(p-d).
$$

If $d\ge1/5$, then $L\le p<q$, so the desired lower bound is immediate.
Suppose $d<1/5$. Then $p<L<1$ on the selected range, and the quadratic
residual argument applies. Explicitly,

$$
L\le\frac{d(22-45d)}4<1.
$$

The quadratic residual at $L$ is $(p-d)S_5(d,p)$, where

$$
\begin{aligned}
S_5(d,p)={}&-25d^5+60d^4-11d^3-25d^2+10d\\
&+p(25d^4-60d^3+21d^2+8d-3).
\end{aligned}
$$

The Bernstein coefficients of the negative of the coefficient of $p$ on
$[0,1/4]$ are

$$
3,
\qquad
\frac52,
\qquad
\frac{57}{32},
\qquad
\frac{69}{64},
\qquad
\frac{135}{256}.
$$

Thus this coefficient is negative. At the upper bound $p=13d/4$,

$$
S_5\left(d,\frac{13d}{4}\right)
=
\frac d4
\left(225d^4-540d^3+229d^2+4d+1\right)>0.
$$

The Bernstein coefficients of the last polynomial on $[0,1/4]$ are

$$
1,
\qquad
\frac54,
\qquad
\frac{373}{96},
\qquad
\frac{435}{64},
\qquad
\frac{2241}{256}.
$$

Therefore, if

$$
p_2=G_{1-m}(p_1),
$$

then

$$
p_2>
(2-5m)p_1-(1-5m)m.
$$

Because $2-5m>0$, the row-4 bound may be substituted to give

$$
p_2>L_2,
\qquad
L_2=(2-5m)L_1-(1-5m)m.
$$

## 8. Exact terminal certificate

Define

$$
\Psi(R,A,D)=L_2-2D-3D^2.
$$

For fixed $R,A$,

$$
\frac{\partial^2\Psi}{\partial D^2}=-6.
$$

The center inequality supplies the lower endpoint

$$
D\ge D_0:=P-RA.
$$

The row-4 $T_+$ selector and $e(A)<2A+5A^2$ supply the upper endpoint

$$
D\le D_h:=A(4R-1)+10RA^2-\eta.
$$

Write

$$
A=\alpha P,
\qquad
0<\alpha<1,
$$

and use the rational parameter $k$ from Section 5. The exact verifier
[`4108_ce1_terminal_verifier.py`](4108_ce1_terminal_verifier.py) expands
$\Psi(D_0)$ and $\Psi(D_h)$ over the rational rectangles and proves the
following facts using rational arithmetic only.

- After removal of positive denominators, the numerator for $\Psi(D_0)$
  has bidegree $(13,3)$ on $[0,1/2]\mathbin{\times}[0,1]$. Its 56
  Bernstein coefficients consist of 55 positive coefficients and the single
  boundary zero at index $(0,3)$. The least positive coefficient is
  $2187/8192$. The canonical tensor digest is
  `831285d98a37fcf362f31a1d8d6859e91a38ec418b5b2df19494c1c05da4d21e`.
- Actual feasibility has $D_h>0$. The verifier proves that this forces
  $k>1/5$. On $[1/5,1/2]\mathbin{\times}[0,1]$, the numerator for
  $\Psi(D_h)$ has bidegree $(21,4)$ and all 110 Bernstein coefficients are
  positive. The least is $818360091/28940800000$, and the canonical tensor
  digest is
  `242eb4af2b3163854095ff91b8c72dd650a5110951771f1a2e9022cae9da9e2e`.

Because actual $k$ and $\alpha$ are interior, the boundary zero in the first
tensor causes no equality. Hence

$$
\Psi(D_0)>0,
\qquad
\Psi(D_h)>0.
$$

The function $\Psi$ is concave in $D$, so it lies above the chord joining
its endpoint values. Therefore

$$
\boxed{\Psi(R,A,D)>0.}
$$

For reproducibility, from the repository root run

```text
python3 proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4108_ce1_terminal_verifier.py
```

The script requires SymPy and uses no floating-point comparisons.

## 9. The final row-2 split

We first prove

$$
\boxed{D<\frac1{10}.}
$$

From $A+wD<P$,

$$
D<\frac{P-A}{w}.
$$

If $D\ge1/10$, then

$$
A<P-\frac w{10}=:A_*.
$$

Because $R>1/2$, the function $D_h(A)$ is strictly increasing. The exact
verifier proves

$$
\frac1{10}-D_h(A_*)
=
-\frac{k(k-2)g_8(k)}{10(k-1)^5(k+1)^5}>0
$$

for $0<k<1/2$, where

$$
\begin{aligned}
g_8(k)={}&319k^8-1028k^7+2002k^6-2220k^5+1665k^4\\
&-796k^3+128k^2+44k-14.
\end{aligned}
$$

The last sign is certified by the positive Bernstein coefficients of
$-g_8$ on $[0,3/8]$ and $[3/8,1/2]$, all printed by `4108`. It follows that

$$
D\le D_h(A)<D_h(A_*)<\frac1{10},
$$

a contradiction.

For $0<D<1/10$, direct substitution gives

$$
h_D(2D+3D^2)=D^2(8D^2+19D-2)<0.
$$

Thus

$$
e(D)<2D+3D^2.
$$

The terminal certificate now yields

$$
\boxed{
p_2>L_2>2D+3D^2>e(D).
}
$$

This strict inequality handles every row-2 selector:

- lower Full and $T_+$ are impossible because $p_2>e(D)$;
- on L or $T_-$, the catalog gives
  $F_{1-D}(p_2)\le e(D)$, and hence
  $G_{1-D}(p_2)\ge1-e(D)>1-X$, where the last strict inequality follows
  from

  $$
  e(D)<2D+3D^2<\frac{23}{100}<\frac12<X;
  $$

- on upper Full, $G_{1-D}(p_2)=p_2\ge1-D>1-X$, because
  $X>1/2>D$.

Therefore every reverse branch satisfies

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
