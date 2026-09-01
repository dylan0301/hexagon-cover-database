# Transverse Seven-Point Enclosure for the One-Gap All-Vd0 Case

Status: Proven

This note strengthens the one-gap part of
[`4101`](4101_new_all_Vd0_finite_enclosure.md).  The former witness retained
all six actual own-radial endpoints.  The proof below needs only the three
transverse endpoints on $r_2,r_3,r_4$.

The local threshold and selected-chord facts come from
[`2004`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
The signed C-triangle coordinates come from
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
The scalar CE1 estimates are those proved in
[`4102`](4102_new_CE1_direct_radial_certificate.md).

## 1. Setup and forced points

Let

$$
U_C,U_0,\ldots,U_5
$$

be the original open unit equilateral roles, and put
$T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. Assume:

- all six V roles are Vd0;
- $T_0$ is the unique supercritical V role;
- $T_1,\ldots,T_5$ are nonsupercritical;
- there is exactly one actual V-gap, normalized to

  $$
  J=[X(\ell),X(r)]\subset e_{0,1};
  $$

- the seven roles cover the hexagon skeleton.

Let $C_i$ be the actual maximal own-radial reach of $T_i$ and define

$$
P_i=(1-C_i)V_i.
$$

Because $P_i$ is the closed own-trace endpoint, $P_i\notin U_i$. Adjacent
roles are Vd0, and the three nonlocal roles are excluded by diameter one.
Thus

$$
P_i\in U_C
\qquad(0\le i\le5).
\tag{1}
$$

Since $J$ is the actual gap,

$$
\boxed{\ell=B_0,\qquad r=1-A_1.}
\tag{2}
$$

Define the transverse seven-point set

$$
\boxed{
K_{\rm tr}
=
\{O,M_0,X(\ell),X(r),P_2,P_3,P_4\}.
}
\tag{3}
$$

Equation (1), the center ownership of the gap, and convexity give

$$
K_{\rm tr}\subset U_C.
$$

## 2. Statement

### Theorem 2.1

No open unit equilateral triangle contains $K_{\rm tr}$. Consequently,

$$
\boxed{\Lambda(K_{\rm tr})\ge1.}
\tag{4}
$$

In particular, for the former ten-point set

$$
K_{410}
=
\{O,M_0,X(\ell),X(r),P_0,\ldots,P_5\},
$$

one has

$$
\Lambda(K_{410})\ge\Lambda(K_{\rm tr})\ge1.
$$

## 3. A candidate C triangle and the upper squeeze

Suppose that an open unit equilateral triangle $U'$ contains $K_{\rm tr}$,
and put $T'=\overline{U'}$. Since $O,M_0\in U'$ and $U'$ has a
positive-length trace on $e_{0,1}$, the exactly-one-midpoint theorem
[`2100`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
makes $M_0$ its unique radial midpoint after the present normalization.
Therefore $T'$ is CE1 or CE2 and has signed variables

$$
0<R<1,\qquad W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
P=E\eta,
$$

$$
\alpha>0,\qquad\delta>0,
\qquad
k=\eta+\alpha+\delta.
$$

Its trace on $e_{0,1}$ is

$$
\left[\frac{k}{R},W+\delta\right].
$$

Put

$$
X=R-\delta,
\qquad
Q=\frac{k}{2R}.
\tag{5}
$$

Both actual gap endpoints belong to the open triangle $U'$, so they lie
strictly inside this closed trace. Using (2),

$$
\boxed{
B_0=\ell>\frac{k}{R}=2Q,
\qquad
A_1=1-r>X.
}
\tag{6}
$$

The two actual boundary endpoints of $T_0$ are at distance at most one.
Hence

$$
A_0^2+A_0B_0+B_0^2\le1,
$$

and therefore

$$
A_0
\le
M_0(B_0)
:=
\frac{-B_0+\sqrt{4-3B_0^2}}2.
$$

The function $M_0$ is strictly decreasing. Since $0<2Q<B_0\le1$,

$$
A_0
<
M_0(2Q)
=
-Q+\sqrt{1-3Q^2}
<
1-Q.
$$

Thus

$$
\boxed{A_0<1-Q.}
\tag{7}
$$

This estimate uses the actual gap endpoint only; the old point $P_0$ is not
needed.

## 4. Boundary monotonicity and the transverse radial data

Every boundary edge other than $e_{0,1}$ is V-gap-free. Since the incident
open V traces must overlap,

$$
B_i+A_{i+1}>1
\qquad(1\le i\le4),
$$

and

$$
B_5+A_0>1.
$$

Together with $A_i+B_i\le1$ for $1\le i\le5$, this gives

$$
\boxed{
A_1<A_2<A_3<A_4<A_5<A_0.
}
\tag{8}
$$

Equations (6)--(8) imply

$$
X<A_i<1-Q
\qquad(1\le i\le5).
\tag{9}
$$

In particular,

$$
\boxed{B_2>Q,\qquad B_4>Q.}
\tag{10}
$$

The radial exits of $T'$ on $r_2,r_3,r_4$ are

$$
d_2'=\delta,
\qquad
d_3'=
\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
\qquad
d_4'=\alpha.
$$

Since $P_i=(1-C_i)V_i$ belongs to the open triangle $U'$ for
$i=2,3,4$,

$$
\boxed{
C_2>1-\delta,
\qquad
C_3>
1-\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
\qquad
C_4>1-\alpha.
}
\tag{11}
$$

These are the only radial data used below.

## 5. CE2: two direct thresholds

For $0<d<1-\sqrt3/2$, put

$$
\epsilon(d)
=
\frac{1-d}{2}
\left(1-\sqrt{4(1-d)^2-3}\right).
$$

The exact local admissible set gives the direct threshold:

> If a nonsupercritical V triangle has
> $A>\epsilon(d)$ and $C\ge1-d$, then
> $B\le\epsilon(d)$.

Assume first that $T'$ is CE2. Its strict signed inequalities are

$$
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
\tag{12}
$$

We record the two elementary center estimates used by the threshold
dichotomy.

### Lemma 5.1

In the strict CE2 domain,

$$
\boxed{
X>\epsilon(\alpha),
\qquad
\min\{\epsilon(\alpha),\epsilon(\delta)\}<Q.
}
\tag{13}
$$

### Proof

The first inequality in (12) gives

$$
WX=RW-W\delta=\eta+P-W\delta>\eta+\alpha.
$$

Testing the selected low-root quadratic at this lower bound is equivalent to
the positivity of

$$
\pi(t)=(\eta+t)(1-2t)-2Wt.
$$

The function $\pi$ is concave on $[0,P]$, while

$$
\pi(0)=\eta>0,
\qquad
\pi(P)=\eta(\eta+2ER^2)>0.
$$

Since $0<\alpha<P$, one gets $\pi(\alpha)>0$, which is precisely
$\epsilon(\alpha)<X$.

For the second estimate put $T=\alpha+\delta$. Multiplying the two
inequalities in (12) by $W$ and $R$ and adding gives

$$
E^2T<P=E\eta,
\qquad
T<\frac{\eta}{E}.
$$

If $d=\min\{\alpha,\delta\}$, then the elementary low-root bound gives

$$
\min\{\epsilon(\alpha),\epsilon(\delta)\}
<
\frac{2d}{1-2d}
\le
\frac{T}{1-T}.
$$

It remains to compare $T/(1-T)$ with $Q$. This is equivalent to the
positivity of

$$
\chi(T)=(\eta+T)(1-T)-2RT.
$$

The function $\chi$ is concave,

$$
\chi(0)=\eta>0,
$$

and

$$
\chi\left(\frac{\eta}{E}\right)
=
\frac{\eta}{E^2}(E-R)^2>0.
$$

Thus $\chi(T)>0$, proving (13). $\square$

If $\epsilon(\alpha)<Q$, then (9), (11), and (13) give

$$
A_4>\epsilon(\alpha),
\qquad
C_4>1-\alpha.
$$

The threshold at $T_4$ yields

$$
B_4\le\epsilon(\alpha)<Q,
$$

contradicting (10).

Otherwise $\epsilon(\alpha)\ge Q$, and (13) gives
$\epsilon(\delta)<Q$. Then

$$
A_2>X>\epsilon(\alpha)\ge Q>\epsilon(\delta),
\qquad
C_2>1-\delta.
$$

The threshold at $T_2$ yields

$$
B_2\le\epsilon(\delta)<Q,
$$

again contradicting (10). Hence $T'$ cannot be CE2.

## 6. CE1: the three-transverse return

Assume that $T'$ is CE1. Then

$$
P-R\alpha-\delta\le0,
$$

and the signed normal form gives

$$
d_3'=\frac{\alpha}{R}.
$$

Thus (11) becomes

$$
C_4>1-\alpha,
\qquad
C_3>1-\frac{\alpha}{R},
\qquad
C_2>1-\delta.
\tag{14}
$$

We now apply the direct argument of `4102`, but only with the hypotheses
actually used there. Suppose for contradiction that $A_0\le1-Q$. The
V-gap-free edges and nonsupercriticality first give

$$
B_5\ge Q,
\qquad
B_4\ge B_5\ge Q.
$$

At $T_4$, use the radial demand $1-\alpha$ from (14). Every local branch
other than the selected $Q_+$ branch forces the preceding boundary reach
beyond $1-X$ and immediately contradicts
$A_1>X$, $A_1+B_1\le1$. On the selected branch, the first chord estimate of
`4102` gives

$$
B_3>L_1,
\qquad
L_1=(2-4\alpha)Q-(1-4\alpha)\alpha.
\tag{15}
$$

At $T_3$, use the radial demand $1-\alpha/R$. Again every nonselected branch
gives the immediate contradiction. On the selected branch the second chord
estimate gives

$$
B_2>L_2,
$$

$$
L_2=
\left(2-\frac{5\alpha}{R}\right)L_1
-
\left(1-\frac{5\alpha}{R}\right)\frac{\alpha}{R}.
\tag{16}
$$

Sections 3--6 of `4102` prove, solely from the strict CE1 signed domain,

$$
\delta<\frac1{10},
\qquad
L_2>2\delta+3\delta^2>\epsilon(\delta),
\qquad
\epsilon(\delta)<X.
\tag{17}
$$

Using the radial demand $1-\delta$ at $T_2$ from (14), the reflected direct
threshold gives

$$
A_2\le\epsilon(\delta).
$$

Coverage of $e_{1,2}$ then gives

$$
B_1\ge1-A_2>1-X.
$$

Together with $A_1>X$, this contradicts nonsupercriticality of $T_1$.
Therefore

$$
\boxed{A_0>1-Q}
\tag{18}
$$

in CE1. Equations (7) and (18) are incompatible.

The proof has used only $P_4,P_3,P_2$ in that order. The points
$P_0,P_1,P_5$ play no role.

## 7. Completion

Both CE1 and CE2 candidates have been excluded. Hence no open unit
equilateral triangle contains $K_{\rm tr}$.

If $\Lambda(K_{\rm tr})<1$, a closed equilateral triangle of side less than
one contains $K_{\rm tr}$; a slight dilation about its incenter produces an
open unit equilateral triangle containing the same compact set. This is
impossible. Therefore (4) holds. $\square$
