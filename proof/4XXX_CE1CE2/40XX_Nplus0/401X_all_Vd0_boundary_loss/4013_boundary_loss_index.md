# CE1/CE2 All-Vd0 Boundary-Loss Obstruction

Status: Proven

## Theorem

Assume that the center role is CE1 or CE2, all six vertex roles are Vd0,
and

$$
a_i+b_i\le1
\qquad (i=0,\ldots,5).
$$

Then the seven roles cannot cover the hexagon. Equivalently, every such
cover has at least one supercritical vertex row $a_i+b_i>1$.

The proof uses the exact center formulas
[`2105`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md)
and
[`2106`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md),
the capped demand map
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md),
and the two loss theorems
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md)
and
[`2108`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md).

## 1. Boundary bookkeeping

Write $a_i,b_i$ for the two incident boundary reaches of the Vd0 role at
$V_i$. Vd0 boundary locality says that this role has no other positive-length
boundary trace. If its incident input reach is at least $a$ and its radial
demand is at least $c$, `2011` bounds its other incident reach by
$\widehat B_c(a)$. The theorem in `2011` is an upper relaxation, so it applies
to the actual row even when either requirement is exceeded.

On the radial arm $r_i$, Vd0 locality leaves $T_i$ as the only vertex role
with positive-length support.  Therefore, if the center role exits that arm
at distance $d_i$ from $O$, coverage forces the actual radial reach of $T_i$
from $V_i$ to be at least $1-d_i$.  This explicitly assigns every
complementary demand $c_i=1-d_i$ used below to the corresponding endpoint
role.

Suppose the roles adjacent to the center trace leave outgoing reaches at
most $B_1$ on $e_{1,2}$ and $B_5$ on $e_{4,5}$. The roles at
$V_2,V_3,V_4$ must then cover boundary length at least

$$
(1-B_1)+1+1+(1-B_5)=4-(B_1+B_5).
$$

If $B_1+B_5<1$, this length is greater than $3$, whereas their row caps give

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Thus every case below is finished once the two adjacent capped outputs have
sum less than one.

## 2. The no-gap case

First suppose every center-boundary interval is already covered by the six
vertex roles. Then the vertex roles alone cover all of $\partial H$. Put

$$
U_i=T_i\cap\partial H.
$$

Each $U_i$ is relatively open in the connected polygonal circle
$\partial H$, and

$$
\mathcal H^1(U_i)\le a_i+b_i\le1.
$$

There are at least two nonempty $U_i$, since one set of length at most one
cannot cover a perimeter of length six. The nonempty members of a finite
relatively open cover of a connected space cannot be pairwise disjoint.
Hence some $U_i\cap U_j$ is a nonempty relatively open subset of
$\partial H$ and has positive length. Therefore

$$
\sum_{i=0}^5\mathcal H^1(U_i)
>
\mathcal H^1\left(\bigcup_{i=0}^5U_i\right)
=6,
$$

contrary to

$$
\sum_{i=0}^5\mathcal H^1(U_i)
\le
\sum_{i=0}^5(a_i+b_i)
\le6.
$$

This proves the no-gap case, including every equality case in the row caps.

## 3. CE1

Normalize the unique CE1 boundary interval as

$$
T_C\cap e_{0,1}=[s,t],
\qquad
u=1-t,
\qquad
w=t-s.
$$

The no-gap case being excluded, this interval contains an active V-gap; in
particular $s,u,w>0$. Let $b_0$ be the reach of the $V_0$ role on
$e_{0,1}$, let $a_0$ be its reach on $e_{5,0}$, and let $a_1,b_5$ be the
reaches from $V_1,V_5$ toward the center interval. Coverage outside the
center trace gives

$$
b_0\ge s,
\qquad
a_1\ge u.
$$

The CE1 center has no trace on $e_{5,0}$, so boundary coverage there gives
$a_0+b_5\ge1$. Since $a_0+b_0\le1$,

$$
b_5\ge1-a_0\ge b_0\ge s.
$$

This is the endpoint propagation needed for the two adjacent capped maps.

Put

$$
0<R<1,
\qquad
S=\sqrt{1-R+R^2},
\qquad
\delta=\frac{R}{1+S}.
$$

The exact CE1 formulas in `2105` give the complementary radial demands

$$
c_1=\frac uR,
\qquad
c_5=1-\gamma_5,
\qquad
\gamma_5=u-\delta-\frac{R}{1-R}w,
$$

with

$$
0<u<R,
\qquad
\gamma_5>0.
$$

Since $s+u+w=1$, all hypotheses of `2107` hold. Consequently

$$
\widehat B_{c_5}(s)+\widehat B_{c_1}(u)<1.
$$

The propagated actual inputs are at least $s$ and $u$, so `2011` makes these
valid upper bounds for the outgoing reaches. Section 1 now gives the
contradiction.

## 4. CE2 with exactly one active interval

Use the exact CE2 notation

$$
T_C\cap e_{5,0}=[x,U],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

with both edges parameterized from $V_0$. Suppose first that the interval on
$e_{0,1}$ contains an active V-gap and the interval on $e_{5,0}$ does not.
As in Section 3, coverage gives

$$
b_0\ge y,
\qquad
a_1\ge1-v.
$$

The absence of a gap on $e_{5,0}$ means that its center trace is already
covered by the endpoint roles; together with coverage outside that trace,
this gives $a_0+b_5\ge1$. Hence

$$
b_5\ge1-a_0\ge b_0\ge y.
$$

Set

$$
S_0=x+y,
\qquad
R=\frac{x}{S_0},
\qquad
S=\sqrt{1-R+R^2},
$$

and

$$
s=y,
\qquad
u=1-v,
\qquad
w=v-y.
$$

The formulas and coupling equation in `2106` give

$$
c_1=\frac uR,
\qquad
c_5=1-\gamma_5,
\qquad
\gamma_5=u-\frac{R}{1+S}-\frac{R}{1-R}w.
$$

Moreover,

$$
s,u,w>0,
\qquad
s+u+w=1,
\qquad
0<u<R,
\qquad
\gamma_5>0.
$$

Thus `2107` again yields

$$
\widehat B_{c_5}(y)+\widehat B_{c_1}(1-v)<1.
$$

Endpoint propagation and Section 1 finish this orientation. Reflection
interchanges the two CE2 intervals and proves the other orientation.

## 5. CE2 with two active intervals

Keep the notation of Section 4 and put

$$
p=1-U,
\qquad
q=1-v.
$$

If both center intervals contain active V-gaps, coverage outside the far
endpoints gives

$$
b_5\ge p,
\qquad
a_1\ge q.
$$

Set

$$
r=\frac{x}{x+y},
\qquad
w=\frac{y}{x+y}.
$$

After reflection if necessary, $0<w\le1/2$ and $r=1-w$. The exact radial
formulas give

$$
c_5=\frac pw,
\qquad
c_1=\frac qr.
$$

The complete two-endpoint theorem `2108`, including the strict inequalities
forced by the CE2 coupling equation, gives

$$
\widehat B_{p/w}(p)+\widehat B_{q/r}(q)<1.
$$

These are valid upper bounds for the adjacent outgoing reaches, so Section 1
again gives the contradiction.

Sections 2--5 exhaust CE1 and the zero-, one-, and two-active-interval CE2
states. This proves the theorem.

$$
\Box
$$
