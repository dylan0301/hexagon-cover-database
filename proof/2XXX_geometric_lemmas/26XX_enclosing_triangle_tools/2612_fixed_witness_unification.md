# Fixed finite witnesses and type-independent nonsupercritical paths

Status: Proven

This source owns the fixed-witness reformulation of the nonzero-gap enclosure
method. The finite sets are chosen from the original configuration before an
arbitrary candidate enclosing triangle is introduced. Nonsupercritical V roles
are not subdivided by V type in the path theorems. The local admissibility
formulas, connected-component selectors, and conditional CE1 return estimates
remain the inherited lemmas stated below; no numerical test replaces them.

The active witness families are BC (six points), D (four points), and
the unchanged zero-gap F (nine points). A (seven points) and B (four
points) are retained as independent alternatives, not dependencies of N0. The
counts are upper bounds, not assertions of minimality. A and F use disks
contained in the convex hull of six forced radial points. BC, optional B, and D use no
disk. Replacement and length/area exits are not enclosure theorems.

## 1. Conventions and inherited local interfaces

Put $O=0$, $V_i=(\cos(i\pi/3),\sin(i\pi/3))$,
$X_i(t)=(1-t)V_i+tV_{i+1}$, $r_i=[O,V_i]$, $M_i=V_i/2$, and
$h=\sqrt3/2$. Indices are modulo six. The original open unit equilateral
triangles satisfy $O\in U_C$ and $V_i\in U_i$; their closures are $T_C,T_i$.
Uppercase $A_i,B_i,C_i$ denotes the actual maximal preceding-edge,
following-edge, and own-radial reaches. Radial reaches are measured from
$V_i$ toward $O$. Nonsupercriticality means $A_i+B_i\le1$, not a condition
on a selected pair.

The exact capacities are those of
[`2004`](../20XX_V_triangle_geometry/2004_admissible_set.md) and
[`2008`](../20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).
Their common-pair comparison has the direct proof in
[`2008b`](../20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md),
independent of the full neighboring capacity formula:

$$
C_+(p,q),C_-(p,q)\le1-\min\{p,q\}\le c_{\max}(p,q),
\qquad p,q\ge0,\quad p+q\le1. \tag{1}
$$

Capacities are coordinatewise antitone. A nonsupercritical actual pair
therefore controls either permitted neighboring trace by
$1-\min\{A_i,B_i\}$. Absent traces need no bound. Including an additional
hypothetical neighboring contribution is safe as an upper bound; it is not
an assertion that the actual V triangle has that support.

For a compact nonempty set $K$, let $\Lambda(K)$ be its least closed
equilateral enclosure side. The compact-open lemma in `2608` gives

$$
K\subset U\text{ for an open unit equilateral }U
\quad\Longrightarrow\quad \Lambda(K)<1. \tag{2}
$$

Conversely, $\Lambda(K)<1$ produces such an open unit triangle by a slight
dilation of a smaller enclosing triangle. Thus excluding every open unit
candidate containing a fixed $K$ proves $\Lambda(K)\ge1$.

## 2. Fixed boundary and radial data

### Lemma 2.1. Actual gaps and boundary completion

The actual gap on $e_{i,i+1}$ is

$$
J_i=X_i([B_i,1-A_{i+1}]) \tag{3}
$$

when $B_i+A_{i+1}\le1$. Equality gives a singleton gap. Every point of $J_i$
is missed by the open V roles. If $\mathcal G$ is the set of endpoints of
all actual gaps, then every convex open set $U'$ satisfies

$$
\mathcal G\subset U'
\quad\Longrightarrow\quad
\partial H\subset U'\cup\bigcup_iU_i. \tag{4}
$$

**Proof.** The incident open traces have parameters $[0,B_i)$ and
$(1-A_{i+1},1]$. Nonincident V roles cannot meet an interior point of this
edge by diameter locality. Their complement is (3). Convexity fills each
closed gap segment from its two endpoints; a singleton is already an
endpoint. The other boundary points are covered by the incident V roles.
Under skeleton coverage the gap endpoints consequently belong to $U_C$.
$\square$

### Lemma 2.2. Total radial endpoints

Write $Z_i(c)=(1-c)V_i$. For each neighboring role let $u_{j\to i}$ be the
largest $c$ for which $Z_i(c)\in T_j$ when $T_j$ has a positive trace on
$r_i$, and put $u_{j\to i}=0$ if there is no positive trace. Define

$$
\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\},\qquad
 d_i=1-\gamma_i,\qquad \widehat P_i=d_iV_i. \tag{5}
$$

Then $0<d_i<1$ and $\widehat P_i\notin\bigcup_jU_j$. In particular,
skeleton coverage forces $\widehat P_i\in U_C$.

**Proof.** No $T_j$ contains $O$: its interior point $V_j$ is at distance
one from $O$, and moving $V_j$ a little away from $O$ within $U_j$ would
violate diameter one. Each $C_i>0$, so $0<\gamma_i<1$. If a local open role
contained $Z_i(\gamma_i)$, openness would extend its radial trace to some
$c>\gamma_i$. An absent neighboring positive trace would also become
positive. Both contradict (5). For a nonlocal index,

$$
\|d_iV_i-V_{i\pm2}\|^2=1+d_i+d_i^2>1,\qquad
\|d_iV_i-V_{i+3}\|=1+d_i>1.
$$

Hence no nonlocal role contains the point either. $\square$

### Corollary 2.2a. One actual-or-bounded radial frontier

For any $\gamma_i\le\Gamma_i\le1$, the point $(1-\Gamma_i)V_i$ is missed
by every open V role. Under skeleton coverage it belongs to $U_C$.

**Proof.** For $\Gamma_i<1$, repeat the local endpoint and nonlocal diameter
argument of Lemma 2.2 with $d=1-\Gamma_i>0$. For $\Gamma_i=1$ the point
is $O$, already excluded from every closed V role in that proof. $\square$

Thus actual total endpoints, uniform common-pair points, and supported
rescuer endpoints are instances of one forcing lemma. In a reduced rescuer
placement the supporting interval reaches the midpoint, the supercritical
own role stops before it, and every other contributor is absent; hence its
O-side endpoint is the actual total frontier. This does not assert that
arbitrary interior points of an inscribed disk are V-excluded.

### Lemma 2.3. Candidate containment recovers an own demand

Let $U'$ be an arbitrary open unit equilateral triangle containing $O$ and
$\widehat P_i$, and let $d_i'$ be the exit of $\overline{U'}$ on $r_i$,
measured from $O$. Then $\gamma_i>1-d_i'$. If both neighboring actual
endpoints are at most $1-d_i'$, then

$$
C_i>1-d_i'. \tag{6}
$$

A sufficient condition is that each neighboring role is nonsupercritical
and both of its actual boundary reaches exceed $d_i'$.

**Proof.** Open containment gives $d_i<d_i'$. Use (5) and exclude the two
neighboring terms from its maximum. The sufficient condition follows from
(1). This proof uses only candidate containment, not skeleton coverage by
$U'$ and the original V roles. $\square$

### Lemma 2.4. Origin already in the witness hull

For $G=X_0(t)$ with $0<t<1$ and positive $d_2,d_4$,

$$
G+\frac{1-t}{d_2}(d_2V_2)+\frac1{d_4}(d_4V_4)=0. \tag{7}
$$

Consequently $O\in\operatorname{conv}\{G,d_2V_2,d_4V_4\}$.

**Proof.** Expand $G=(1-t)V_0+tV_1$ and use
$V_2=V_1-V_0$ and $V_4=-V_1$. All three coefficients in (7) are positive;
dividing by their sum proves the convex-hull statement. $\square$

### Lemma 2.5. Nonsupercritical path monotonicity

Define actual boundary deficits $s_i=1-A_i-B_i$ and overlap surpluses
$\omega_i=B_i+A_{i+1}-1$. Identically,

$$A_{i+1}-A_i=s_i+\omega_i,\qquad
B_i-B_{i+1}=s_{i+1}+\omega_i.$$

On a gap-free nonsupercritical path, $s_i\ge0$ and $\omega_i>0$;
therefore $A$ increases and $B$ decreases. Weak handoffs give weak
monotonicity. On the full cycle $\sum_i\omega_i=-\sum_i s_i$.
A supercritical role has negative $s_i$ and must not be silently included
in an ordinary monotonicity chain.

## 3. Alternative family A: one gap and no supercritical role

### Theorem 3.1. Seven-point complementary-gap enclosure

Suppose $N_+=0$ and the only actual gap is $J_0$. Put

$$
p=A_1,\quad q=B_0,\quad c_A=c_{\max}(p,q),\quad d_A=1-c_A,
$$

$$
D_i^A=d_AV_i,\qquad
G_A=\begin{cases}X_0(q),&q\le p,\\X_0(1-p),&p<q,\end{cases}
$$

$$
K_A=\{D_i^A:0\le i\le5\}\cup\{G_A\},\qquad
\mathcal D_A=\{x:\|x\|\le h(1-c_{\max}(A_1,B_0))\}. \tag{8}
$$

Under skeleton coverage, $K_A\subset U_C$, while $\Lambda(K_A)\ge1$.
There is no restriction on the V types.

**Proof.** The five gap-free edges and nonsupercriticality give

$$
A_1<A_2<A_3<A_4<A_5<A_0,\qquad
B_0<B_5<B_4<B_3<B_2<B_1.
$$

Thus every actual pair dominates $(p,q)$, and $p+q\le1$ by (3).
Common-pair forcing in `2608` puts every $D_i^A$ in $U_C$. Their convex
hull contains exactly the displayed inscribed disk. The farther endpoint of
$J_0=X_0([q,1-p])$ is $G_A$; it is also center-forced. The proof of the
complementary-gap theorem in `2608` establishes
$\Lambda(\mathcal D_A\cup\{G_A\})\ge1$. Since this compact set lies in
$\operatorname{conv}(K_A)$, the finite-set inequality follows. $\square$

This includes singleton gaps as a statement; strict handoffs may already
exclude a particular equality configuration. No positive gap length is
assumed in the enclosure step.

## 4. Optional family B: two gaps and a five-role nonsupercritical path

### Theorem 4.1. Four-point two-gap enclosure

Suppose the actual gaps are precisely on $e_{5,0}$ and $e_{0,1}$, and
$A_i+B_i\le1$ for $1\le i\le5$. There is no assumption on the criticality
of $T_0$ or on the V types. Define from the original roles

$$
G_L=X_5(B_5),\quad G_R=X_0(1-A_1),\qquad
K_B=\{G_L,G_R,\widehat P_2,\widehat P_4\}. \tag{9}
$$

Then $\Lambda(K_B)\ge1$. Under skeleton coverage, $K_B\subset U_C$.
No disk is used.

**Proof.** Forcing follows from Lemmas 2.1 and 2.2. Suppose an arbitrary
open unit candidate $U'$ contains the same four points. Lemma 2.4 forces
$O\in U'$. Open containment of $G_L,G_R$ gives positive traces on both
adjacent boundary edges. The classification and exactly-one-midpoint result
in [`2100`](../21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
make the candidate CE2 with common midpoint $M_0$.

Use its own signed variables from
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,\quad W=1-R,\quad E=\sqrt{1-RW},\quad
\eta=1-E,\quad P=E\eta,\quad \alpha,\delta>0,
$$

$$
\alpha+W\delta<P,\qquad R\alpha+\delta<P,
\qquad k=\eta+\alpha+\delta.
$$

Set $p=W-\alpha$, $q=R-\delta$. The boundary witnesses lie strictly
inside the candidate traces, giving $B_5>p$ and $A_1>q$. The four middle
gap-free edges and Lemma 2.5 imply

$$
A_i>q,\qquad B_i>p\qquad(1\le i\le5). \tag{10}
$$

Every local contributor on $r_2$ or $r_4$ belongs to this path. By symmetry
of $c_{\max}$ and (1), with $c_*=c_{\max}(p,q)$,
$\gamma_2,\gamma_4\le c_*$. The exact short-ray theorem in
[`2609`](2609_simplified_finite_enclosure_lemmas.md) gives

$$
c_*<1-\min\{\alpha,\delta\}. \tag{11}
$$

If $\delta\le\alpha$, then $\|\widehat P_2\|=1-\gamma_2>\delta$,
although the candidate exit on $r_2$ is $\delta$. Otherwise
$\|\widehat P_4\|>\alpha$, contradicting its exit on $r_4$. The witnesses
have stayed fixed; only the comparison pair $(p,q)$ came from the candidate.
Thus every open unit candidate is excluded. $\square$

## 5. Family BC: one selected gap and a five-role nonsupercritical path

### Theorem 5.1. Unified six-point selected-gap enclosure

Assume $J_0$ is an actual gap, $A_i+B_i\le1$ for $1\le i\le5$, and

$$
B_i+A_{i+1}>1\quad(1\le i\le4),\qquad B_5\ge B_0/2.
$$

There is no assumption on the gap status of $e_{5,0}$. The scalar tail
inequality is an explicit hypothesis of this pure enclosure theorem.
Define

$$
K_{BC}=\{M_0,X_0(B_0),X_0(1-A_1),
             \widehat P_2,\widehat P_3,\widehat P_4\}. \tag{12}
$$

Then $\Lambda(K_{BC})\ge1$. Under skeleton coverage with the C triangle's
distinguished midpoint $M_0$, one has $K_{BC}\subset U_C$. The five path roles
may have arbitrary V types; $T_0$ need not be supercritical. No disk is used.
The former name $K_C$ denotes this same six-point set in compatibility
sources. For original perimeter covers the shared-anchor lemma
[`2018b`](../20XX_V_triangle_geometry/2018b_shared_gap_anchor_transfer.md)
supplies $B_5>B_0/2$, even with a second gap. For the old pure one-gap
hypothesis it follows from $B_5+A_0>1$ and $A_0\le M_0(B_0)$.

### 5.1 Candidate normalization and the scalar tail input

Forcing follows from Lemmas 2.1--2.2 and the structural C midpoint. Suppose
an arbitrary open unit triangle $U'$ contains (12). Lemma 2.4 implies
$O\in U'$. The midpoint anchor fixes $M_0$ as the unique midpoint. Use the
candidate's signed form as in Section 4, but now allow CE1 or CE2. Put

$$
X=R-\delta,\qquad Q=\frac{\eta+\alpha+\delta}{2R}. \tag{13}
$$

The gap endpoints give $B_0>2Q$ and $A_1>X$. The explicit scalar input
therefore gives

$$
B_5\ge B_0/2>Q. \tag{14}
$$

The four middle gap-free edges and nonsupercriticality imply

$$
A_1<A_2<A_3<A_4<A_5,\qquad B_1>B_2>B_3>B_4>B_5,
$$

$$
A_i>X,\qquad B_i>Q\qquad(1\le i\le5). \tag{15}
$$

Only these boundary inequalities are used below.

### 5.2 CE2 candidates

For $0<d<1-h$, write

$$
e(d)=\frac{1-d}{2}\left(1-\sqrt{4(1-d)^2-3}\right).
$$

The high-radial threshold of `2004` excludes an admissible nonsupercritical
pair with both coordinates above $e(d)$ at demand $1-d$. The CE2 center estimates are proved directly in Section 8 below:

$$
X>e(\alpha),\qquad \min\{e(\alpha),e(\delta)\}<Q. \tag{16}
$$

The pair $(X,Q)$ is positive with sum below one, by (15). If
$e(\alpha)<Q$, both coordinates exceed $e(\alpha)$, so
$c_{\max}(X,Q)<1-\alpha$. Otherwise
$e(\delta)<Q\le e(\alpha)<X$, so $c_{\max}(X,Q)<1-\delta$.
Using (1) and (15), the first case gives
$\gamma_4\le c_{\max}(X,Q)<1-\alpha$, and the second gives the analogous
bound for $\gamma_2$ and $\delta$. Each contradicts containment of the
corresponding fixed total endpoint in the candidate. CE2 is excluded.

### 5.3 CE1: recover the first two own-radial demands

Now $R\alpha+\delta\ge P$ and $\alpha+W\delta<P$. Put $m=\alpha/R$.
The inherited signed exits are

$$
d_4'=\alpha,\qquad d_3'=m,\qquad d_2'=\delta. \tag{17}
$$

Combining the two signed inequalities yields $E^2\alpha<RP$, hence
$m<\eta/E$. Moreover

$$
X>\frac{R}{1+E}>\frac{\eta}{E}>m.
$$

For the first inequality use $\delta<P/W=ER/(1+E)$; the second is
$E>W$ after using $\eta=RW/(1+E)$. Finally

$$
2R(Q-m)=\eta+\delta-\alpha>0,
$$

because $\alpha<P=E\eta<\eta$. Therefore

$$
\mu:=\min\{X,Q\}>m>\alpha. \tag{18}
$$

Both boundary reaches of every neighbor relevant to $r_4,r_3$ exceed
$\mu$. Equation (1) bounds their neighboring endpoints below the required
radial demands. Candidate containment and Lemma 2.3 now give

$$
C_4>1-\alpha,\qquad C_3>1-m. \tag{19}
$$

### 5.4 Recover the third demand before invoking the full return

Use only the first $T_4$ step of the local CE1 return in
[`4102`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md).
Use its tail-input first step with $B_4>Q$, the middle handoffs, and
the radial bound at $T_4$, but not the bounds at $T_3,T_2$.
A nonselected local branch immediately gives the boundary contradiction at
$T_1$. On the surviving selected branch it gives

$$
B_3>L_1,\qquad L_1=(2-4\alpha)Q-(1-4\alpha)\alpha. \tag{20}
$$

The additional identity needed for type independence is

$$
R(L_1-\delta)
=(1-2\alpha)\eta+(W-2\alpha)(\alpha+\delta)+4R\alpha^2>0. \tag{21}
$$

Every sign follows from $0<\alpha<P<\min\{1/2,W/2\}$. Thus $B_3>\delta$,
and (15) with backward monotonicity gives $B_1>B_3>\delta$ and
$A_1,A_3>X>\delta$. Both neighbors of $r_2$ therefore have neighboring
capacity strictly below $1-\delta$. Candidate containment of
$\widehat P_2$ and Lemma 2.3 give

$$
C_2>1-\delta. \tag{22}
$$

We have now proved all three own-radial hypotheses of the full tail-input
`4102` return. Its algebra uses the actual boundary pairs,
nonsupercriticality, $B_4\ge Q$, and these radial demands, not Vd0
locality or a fifth handoff. It gives $B_1>1-X$, contradicting
$A_1>X$ and $A_1+B_1\le1$. This excludes CE1 and proves Theorem 5.1. $\square$

The conditional selected-branch hypotheses in `4102` must be retained.
In particular, $\delta<1/10$ is used only after the surviving selected
conditions have been established; it is not a consequence of the bare CE1
signed domain. The first $T_4$ step above is invoked before the full return,
so no radial hypothesis is assumed in order to prove itself.

## 6. Family D: four-point supported-rescuer geometry

### Theorem 6.1. Four-point enclosure lemma

Let $Y(t)=(1-t)V_0+tV_5=X_5(1-t)$. Suppose

$$
a\ge0,\quad \varepsilon>0,\quad \beta\ge0,\quad
s=a+\varepsilon\le1,\quad a\le\varepsilon,\quad
\beta\le\frac{\varepsilon}{s}.
$$

Then the fixed geometric set

$$
K_D(a,\varepsilon,\beta)=
\{O,\varepsilon V_1,Y(a),Y(1-\beta)\} \tag{23}
$$

satisfies $\Lambda(K_D)\ge1$. No disk is used.

**Proof.** If $a=0$ or $\beta=0$, the set contains the origin and a hexagon
vertex at distance one and cannot lie in an open unit triangle. Otherwise
suppose an open unit candidate contains (23). The identity

$$
\frac{\varepsilon}{s}Y(a)+\frac a s(\varepsilon V_1)
=\frac{\varepsilon}{s}V_0 \tag{24}
$$

and $\varepsilon/s\ge1/2$ force $M_0$ into it. It also contains $O$ and
an interior point of a boundary edge openly. The exactly-one-midpoint
normal form applies. Use its left-active reflected form if necessary; no
positive right trace is assumed here. In the signed side-slack coordinates,
its left trace has candidate endpoints $k/W$ and $R+\alpha$, and its exit
on $r_1$ is $\delta/R$, with $\eta,\alpha,\delta>0$.
Containment of $Y(a)$ and $\varepsilon V_1$ gives

$$
Wa>k=\eta+\alpha+\delta,\qquad \delta>R\varepsilon.
$$

Therefore $\alpha<a-Rs$ and $R<a/s$. Since $s\le1$,

$$
R+\alpha<a+R(1-s)\le a/s.
$$

Containment of the other boundary point requires $1-\beta<R+\alpha$,
whereas the hypothesis gives $1-\beta\ge a/s$. Contradiction. $\square$

### Lemma 6.1a. Common scalar ratio test

For $0\le x,c\le1/2$ and $M=(c+\sqrt{c^2-8c+4})/2$,

$$x\le1-M\quad\Longleftrightarrow\quad x^2+(c-2)x+c\ge0.$$

**Proof.** The function $x(2-x)/(1+x)$ is increasing on $[0,1/2]$
and takes value $c$ at $x=1-M$. Multiplication by $1+x$ proves the claim.
In the T3-like chart $c=x+\theta$, the polynomial becomes
$2x^2+(\theta-1)x+\theta$. The Vd1 chart must verify its own parameter
inequalities; only the final ratio test is common. $\square$

### Corollary 6.2. Common rescuer adapter, both gap ranks

Suppose the reduced placement has distinguished C midpoint $M_0$, a
supported trace of $T_0$ on $r_1$ with actual endpoint coordinates
$0<c\le1/2\le u<1$, unique supercritical $T_1$, and nonsupercritical
$T_2,T_3,T_4,T_5$ on the center-free four-edge path. Put

$$
\varepsilon=1-u,\qquad
M=M_c^{\rm sup}=\frac{c+\sqrt{c^2-8c+4}}2.
$$

Assume the local adapter has established

$$
\varepsilon V_1\in U_C,\quad C_1\ge c,\quad
A_0+\varepsilon\le1,\quad
\frac{A_0}{A_0+\varepsilon}\le1-M. \tag{25}
$$

Then the actual four points

$$
K_D=\{O,\varepsilon V_1,Y(A_0),Y(1-B_5)\} \tag{26}
$$

lie in $U_C$ and have $\Lambda(K_D)\ge1$.

**Proof.** The strict-supercritical envelope gives $B_1<M$, and path
monotonicity gives $B_5\le B_1<M$. Since $M\ge1/2$, (25) gives
$A_0\le\varepsilon$ and
$B_5< M\le\varepsilon/(A_0+\varepsilon)$. Also
$A_0\le1-M$, by multiplying the ratio bound by
$A_0+\varepsilon\le1$. Hence $B_5<1-A_0$ and the two boundary points in
(26) are exactly the endpoints of the actual left-edge gap. Lemma 2.1
forces them into $U_C$; the other two points are already there. Apply
Theorem 6.1 with geometric parameters $a=A_0$, $\beta=B_5$.
The proof does not distinguish one from two gaps. $\square$

The T3-like and Vd1 chart calculations remain local adapters for (25).
A Vd2 rescuer is not assigned this theorem without those inequalities.
The old boundary-sum terminal is an alternative only, not the conclusion of
this finite-enclosure theorem.

## 7. The all-nonsupercritical assembly and replacement output

### Theorem 7.0. Center-aligned selected-gap path obstruction

Suppose the original roles cover the skeleton, there is at least one
actual gap, the C triangle's unique midpoint is $M_k$, and every V role
except possibly $T_k$ is nonsupercritical. Then the configuration is
impossible.

**Proof.** Normalize $k=0$. The signed center form confines all possible
gap edges to $e_{5,0},e_{0,1}$. Select either actual gap and reflect if
necessary so that it is $J_0$; the four middle edges are gap-free. Original
perimeter coverage and `2018b` give $B_5>B_0/2$. Theorem 5.1 therefore
applies with the same six-point set, whether or not the other incident
edge is also a gap. All six points belong to $U_C$, contradicting
$\Lambda(K_{BC})\ge1$ and compact-open containment. $\square$

### Theorem 7.1. N0

There is no cover of the full hexagon skeleton by the seven original open
roles with $N_+=0$.

**Proof.** With zero gaps the six positive $\omega_i$ contradict
$\sum_i\omega_i=-\sum_i s_i\le0$. With a nonzero gap, every role is
nonsupercritical, so Theorem 7.0 applies. $\square$

N0 uses BC, not optional A or B. This is acyclic: the BC proof uses the conditional CE1
local return and demand recovery, not N0, replacement, or a placement theorem.

A replacement that preserves the skeleton and produces six nonsupercritical
roles can therefore finish by N0. Its input gap count need not equal its
output gap count. The construction must still preserve both separate vertex
charts and all strict overlap margins. N0 uses actual output reaches, not
selected replacement lower bounds. The zero-gap nine-point theorem cannot
replace N0, because its asymmetric points require full-hexagon coverage.

## 8. Retained CE2 threshold calculation used in (16)

This calculation is included here so that the old all-Vd0 `4103` can become
a compatibility wrapper without creating a circular reference.
In the strict CE2 domain, $\alpha+W\delta<P$ and
$R\alpha+\delta<P$. Thus

$$
WX=RW-W\delta=\eta+P-W\delta>\eta+\alpha.
$$

Testing the selected low-root equation at this lower bound reduces
$e(\alpha)<X$ to positivity of

$$
\pi(t)=(\eta+t)(1-2t)-2Wt.
$$

This is concave on $[0,P]$, with
$\pi(0)=\eta>0$ and $\pi(P)=\eta(\eta+2ER^2)>0$. Hence the first
inequality in (16) holds. For the second put $T=\alpha+\delta$.
Multiply the two strict center inequalities by $W,R$ and add to obtain
$E^2T<P$, so $T<\eta/E$. For $d=\min\{\alpha,\delta\}$ the selected
low-root bound gives

$$
\min\{e(\alpha),e(\delta)\}<\frac{2d}{1-2d}
\le\frac{T}{1-T}.
$$

The last fraction is below $Q$ precisely when
$\chi(T)=(\eta+T)(1-T)-2RT>0$. This concave quadratic is positive at
$T=0$ and at $T=\eta/E$, where its value is
$\eta(E-R)^2/E^2>0$. Thus (16) follows.

## 9. Explicit disks and unchanged zero-gap ownership

For a positive common pair $p+q\le1$, set
$m=\min(p,q)$, $M=\max(p,q)$, $s=p+q$, and
$\chi=s^4-s^2+pq$. The existing exact formula is

$$
c_{\max}(p,q)=
\begin{cases}
C_L(m),&\chi\le0,\\
2M/(1+\sqrt{4s^2-3}),&\chi>0,
\end{cases}
$$

where $C_L(m)$ is the selected root in $[h,1]$ of
$z^4-z^2+mz-m^2=0$. Thus every common radial disk used here is explicitly
$\{x:\|x\|\le h(1-c_{\max}(p,q))\}$.

For zero gaps and one supercritical role, the unchanged
[`31058`](../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md)
constructs six radial points and $Q_-,Q_0,Q_+$. With supercritical index
four, one may choose strict handoffs
$x_i=(1-A_{i+1}+B_i)/2$, put $a=1-x_3<A_4$, $b=x_4<B_4$,
and use the disk
$\{x:\|x\|\le h(1-c_{\max}(1-b,1-a))\}$.
The asymmetric points, the four-contact theorem in `2611`, and the exact
certificate remain unchanged. A four-contact caliper reduction is not a
four-point witness theorem.
