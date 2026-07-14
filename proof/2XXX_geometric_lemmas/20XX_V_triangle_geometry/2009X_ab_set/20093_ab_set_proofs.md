# The AB-Set: Partial Derivations And Proof Obligations

Status: Empirical

This file records exact preliminary lemmas and the intended proof of the
description of $K(a,b)$ stated in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md).  It is not a
complete proof of that general catalog. Notation is as there:
$O=(0,0)$, $B=(b,0)$, $A=a u(120^\circ)$, $u(\theta)=(\cos\theta,\sin\theta)$,
$u^\perp(\theta)=u(\theta+90^\circ)$, $h=\frac{\sqrt3}2$, $\sigma=a+b$, $R^2=a^2+ab+b^2$,
$C=\{ru(\theta):r\ge0,\ \theta\in[0^\circ,120^\circ]\}$,
$$U=\bigcup\{T:\ T\ \text{unit equilateral},\ \{A,O,B\}\subset T\},\qquad K=U\cap C .$$
For a compact $S\subset\mathbb R^2$ write $g_S(\theta)=\max_{p\in S}\langle p,u(\theta)\rangle$
(support function), and for the three-point configuration
$g(\theta):=g_{\{A,O,B\}}(\theta)=\max\{0,\ a\cos(\theta-120^\circ),\ b\cos\theta\}$.

## Proof ledger

The fitting criterion, the formula for the three-point orientation function,
the band endpoints, star-shapedness, and the displayed parametric/implicit
curve identities are exact.  The strict Band IV formula is separated as a
lemma target in
[`20091_ab_union_curve_a_plus_b_gt_1.md`](20091_ab_union_curve_a_plus_b_gt_1.md);
that file records an exact counterexample to its former support-sector
exhaustion, although not to the final formula.

The proposed general Bands I--III catalog still has the following precise
obligations.

1. The claimed arc order and the assertion that every listed pivot triangle
   contains the fourth marked point are checked only at finitely many sampled
   parameters and directions; the scalar inequalities are not written down
   and proved uniformly on each case region.
2. Lemma 9.1 is only a certification template.  The file does not eliminate
   every pair of catalog curves over every parameter region, prove that every
   possible interior intersection is among the listed corners, or prove that
   each sign-defined case region is connected.  A single floating-point
   evaluation therefore cannot supply the missing global comparisons.
3. The domination or non-realizability of the seven $h$-circles, the unused
   flush lines, and the remaining support configurations is asserted rather
   than certified by exact inequalities.
4. The single-signed derivative used for endpoint capping in the gap sectors
   is asserted without its derivative formula and sign proof.
5. Several predicate-pruning implications in §10, including mutual exclusion
   of the two $\mathcal G$ predicates and the implication from the mid-dip
   predicate to $\mathcal G$, are supported only by rectangular grids.

Exact resultant and tangency identities locate possible transitions, but do
not by themselves prove which branch is exposed on either side or exclude
other transitions.  Accordingly this file and the general catalog remain
`Empirical` until the five obligations above receive exact inequalities,
interval certificates, or another independently checkable global
certificate.

---

## 1. The fitting criterion

Every unit equilateral triangle with outer unit normals
$n_k=u(\varphi+120^\circ k)$, $k=0,1,2$, has the form
$$T(\varphi;c_0,c_1,c_2)=\{x:\ \langle x,n_k\rangle\le c_k,\ k=0,1,2\},\qquad c_0+c_1+c_2=h. \tag{1.1}$$

**Lemma 1.1.** *(i) For $c_0+c_1+c_2\ge 0$ the set (1.1) is an equilateral triangle of side
$\frac{2}{\sqrt3}(c_0+c_1+c_2)$; in particular it is a unit triangle iff $c_0+c_1+c_2=h$, and every
unit triangle with these normals arises this way. (ii) A compact $S$ is contained in some unit
triangle with normals $n_k(\varphi)$ iff*
$$F_S(\varphi):=\sum_{k=0}^{2}g_S(\varphi+120^\circ k)\ \le\ h. \tag{1.2}$$

*Proof.* (i) Since $n_0+n_1+n_2=0$, the intersection of the three half-planes is invariant in shape:
translating so that the incenter (the point $x^*$ with $\langle x^*,n_k\rangle = c_k-\rho$ for all
$k$, i.e. equidistant $\rho$ from the three lines) sits at the origin, we get the equilateral
triangle with inradius $\rho=\frac{c_0+c_1+c_2}{3}$; a unit equilateral triangle has inradius
$\frac{1}{2\sqrt3}=\frac h3$. Equivalently this is Viviani's theorem: for any point $x$ in a unit
equilateral triangle, the distances to the three sides sum to the height $h$; and
$\sum_k\langle x,n_k\rangle=0$.
(ii) $S\subset T(\varphi;c)$ iff $c_k\ge g_S(\varphi+120^\circ k)$ for each $k$; such $c$ with
$\sum c_k=h$ exists iff (1.2). $\square$

**Corollary 1.2.** $x\in U$ iff $\min_{\varphi}F_{\{A,O,B,x\}}(\varphi)\le h$. Moreover, writing
$F(\varphi):=F_{\{A,O,B\}}(\varphi)$ and $\Phi=\{\varphi:F(\varphi)\le h\}$ (period $120^\circ$),
$$U=\bigcup_{\varphi\in\Phi}U_\varphi,\qquad
U_\varphi:=\{x:\ F_{\{A,O,B,x\}}(\varphi)\le h\}. \tag{1.3}$$

**Lemma 1.3 (the hexagon $U_\varphi$).** Let $m_k=g(\varphi+120^\circ k)$ and
$s=h-F(\varphi)\ (\ge0$ for $\varphi\in\Phi)$. Then
$$U_\varphi=\Bigl\{x:\ \langle x,n_k\rangle\le m_k+s\ \ (k=0,1,2),\quad
\langle x,-n_k\rangle\le h-m_k\ \ (k=0,1,2)\Bigr\}. \tag{1.4}$$

*Proof.* $F_{\{A,O,B,x\}}(\varphi)=\sum_k\max(m_k,\langle x,n_k\rangle)\le h=\sum_k m_k+s$.
Expanding the sum of maxima by which terms exceed $m_k$, and using $\sum_k\langle x,n_k\rangle=0$
for the triple term, this is equivalent to: for every $k$, $\langle x,n_k\rangle-m_k\le s$; and for
every pair $i\ne j$, $(\langle x,n_i\rangle-m_i)+(\langle x,n_j\rangle-m_j)\le s$, i.e.
$\langle x,-n_k\rangle\le m_i+m_j+s=h-m_k$ for $\{i,j,k\}=\{0,1,2\}$. $\square$

Geometrically $U_\varphi$ is the union of all unit triangles of orientation $\varphi$ containing
$\{A,O,B\}$: a hexagon with alternating outer sides (normals $n_k$) and inner sides (normals
$-n_k$); its outer/inner corner in direction "between $n_i$ and $n_j$" is the free vertex of the
triangle whose other two sides touch the supports.

## 2. The three-point data

**Lemma 2.1 (supports).** Let $\theta_{AB}\in[30^\circ,90^\circ]$ be defined by
$\cos\theta_{AB}=\frac{\sqrt3 a}{2R}$, $\sin\theta_{AB}=\frac{a+2b}{2R}$ (any value for $R=0$);
$u(\theta_{AB})$ is the outer normal of the segment $AB$, and the distance from $O$ to the line
$AB$ is $d_{AB}=\frac{\sqrt3 ab}{2R}$. Then the maximizer in
$g(\theta)$ is $B$ for $\theta\in(-90^\circ,\theta_{AB})$, $A$ for
$\theta\in(\theta_{AB},210^\circ)$, and $O$ for $\theta\in(210^\circ,270^\circ)$, with ties at the
three transition angles. *(Direct verification from $g=\max(0,a\cos(\theta-120^\circ),b\cos\theta)$.)*

**Lemma 2.2 (the function $F$).** On a period, with all angles mod $120^\circ$:
$$F(\varphi)=\begin{cases}
\sigma\cos\varphi, & \varphi\in[-30^\circ,30^\circ],\\[2pt]
R \cos(\varphi-\theta_{AB}+30^\circ), & \varphi\in[30^\circ,\theta_{AB}],\\[2pt]
R \cos(\varphi-\theta_{AB}-30^\circ), & \varphi\in[\theta_{AB},90^\circ].
\end{cases} \tag{2.1}$$
Hence $\min F=\frac{\sqrt3}2R$ (at $\varphi=\theta_{AB}$), the two local maxima are
$F(0^\circ)=\sigma$ and $F(\theta_{AB}\pm30^\circ)=R$ ($+$ if $a>b$, $-$ if $b>a$; for $a=b$ they
merge), and the secondary local minimum is $F(30^\circ)=F(90^\circ)=\frac{\sqrt3}2\sigma$
(attained at $90^\circ$ if $a>b$, at $30^\circ$ if $b>a$).

*Proof.* For $\varphi\in(0^\circ,30^\circ)$ the three normals $\varphi,\varphi+120^\circ,
\varphi+240^\circ$ have supports $B,A,O$ (Lemma 2.1), so
$F=b\cos\varphi+a\cos\varphi+0=\sigma\cos\varphi$; the case $\varphi\in(90^\circ,120^\circ)$ is the
mirror image. For $\varphi\in(30^\circ,90^\circ)$ the supports are
$\bigl(\max(A,B),A,B\bigr)$ giving
$F=\max\bigl(a\cos(\varphi-120^\circ),b\cos\varphi\bigr)+a\cos\varphi+b\cos(\varphi-120^\circ)$;
using $\cos\varphi+\cos(\varphi-120^\circ)=\cos(\varphi-60^\circ)$ and writing
$a\cos\varphi+b\cos(\varphi-60^\circ)=R\cos(\varphi-\delta)$ with $\delta=\theta_{AB}-30^\circ$
(a direct check of $R\cos\delta=a+\frac b2$, $R\sin\delta=\frac{\sqrt3}2b$), one gets
$F=\max\bigl(R\cos(\varphi-\delta), R\cos(\varphi-\delta-60^\circ)\bigr)$, whose two branches swap
exactly at $\varphi=\delta+30^\circ=\theta_{AB}$. Values and monotonicity follow, using
$\frac{\sqrt3}2\sigma\le R\le\sigma$ (the first is $(a-b)^2\ge0$, the second is $ab\ge0$). $\square$

**Corollary 2.3 (existence; bands).** $U\ne\varnothing$ iff $R\le1$; at $R=1$, $U$ is the single
unit triangle with base $[A,B]$ and third vertex on the $O$-side of the line $AB$
(the minimal enclosing triangle at orientation $\theta_{AB}$).
For $R<1$, comparing $h$ with the critical values
$\tfrac{\sqrt3}2R\le\tfrac{\sqrt3}2\sigma\le R\le\sigma$ yields exactly the four band structures of
$\Phi$ stated in the bands table of `20092_ab_set_case_catalog.md`, with endpoints:

* outer gap ($\sigma>\frac{\sqrt3}2$): $\Phi$ misses the interval $(-\psi_1,\psi_1)$ around
  $\varphi\equiv0$, where $\cos\psi_1=\frac{\sqrt3}{2\sigma}$; this uses the first branch of (2.1),
  which requires $\psi_1\le30^\circ$, i.e. $\sigma\le1$ (for $\sigma>1$ see the merged case below);
* mid gap ($R>\frac{\sqrt3}2$): the gap around $\varphi=\theta_{AB}\pm30^\circ$ is
  $(\theta_{AB}\pm30^\circ-\kappa,\ \theta_{AB}\pm30^\circ+\kappa)$ with
  $\cos\kappa=\frac{\sqrt3}{2R}$ ($+$ for $a>b$);
* for $\sigma>1$ the two gaps merge and $\Phi=[\theta_{AB}-30^\circ+\kappa,\ \theta_{AB}+30^\circ-\kappa]$.

## 3. Global structure of $U$ and the radial function

**Lemma 3.1.** $U$ is compact, $U\subseteq \bar B(P,1)$ for each $P\in\{A,O,B\}$, and $U$ is
star-shaped with respect to every point of $\mathrm{conv}\{A,O,B\}$. Consequently $K=U\cap C$ is
compact and star-shaped w.r.t. $O$, and for $\theta\in(0^\circ,120^\circ)$
$$K\cap\{ru(\theta):r\ge0\}=\{ru(\theta):0\le r\le r^*(\theta)\},\qquad
r^*(\theta)=\max\{r:\ ru(\theta)\in U\}.$$

*Proof.* Boundedness and the ball containments: any two points of a unit equilateral triangle are
at distance $\le1$ (its diameter). Compactness: the family of admissible triangles is compact
(orientations in the compact set $\Phi$, translations bounded), so the union is closed.
Star-shape: if $x\in T\supseteq\{A,O,B\}$ then $T\supseteq[y,x]$ for every
$y\in\mathrm{conv}\{A,O,B\}\subseteq T$ by convexity. $\square$

For fixed $\theta$ and $\varphi\in\Phi$ let
$$\rho_\varphi(\theta)=\max\{r\ge0:\ ru(\theta)\in U_\varphi\}$$
(well-defined: $O\in U_\varphi$, $U_\varphi$ compact convex). By (1.3),
$$r^*(\theta)=\max_{\varphi\in\Phi}\rho_\varphi(\theta). \tag{3.1}$$
By Lemma 1.3, $\rho_\varphi(\theta)$ is computed from the six linear constraints; equivalently, with
$c_k(\varphi)=\cos(\theta-\varphi-120^\circ k)$,
$$\rho_\varphi(\theta)=\max\Bigl\{r:\ \sum_k\max\bigl(m_k(\varphi), r c_k(\varphi)\bigr)\le h\Bigr\},$$
a strictly increasing piecewise-linear equation in $r$ (its exact solution formula is what
`rho_of` in `2009X_computation/verify_ab_set.py` implements).

## 4. Classification of boundary configurations

Fix $\theta\in(0^\circ,120^\circ)$ and let $r=r^*(\theta)$, $x=ru(\theta)\in\partial U$, and let
$\varphi^*\in\Phi$ attain the max in (3.1). Write $T^*$ for the *minimal* triangle at orientation
$\varphi^*$ containing $\{A,O,B,x\}$ (sides at the support values); by maximality
$F_{\{A,O,B,x\}}(\varphi^*)=h$, so $T^*$ is a unit triangle, $x\in\partial T^*$, and each side of
$T^*$ touches at least one of $A,O,B,x$.

**Lemma 4.1 (first-order conditions).** One of the following holds at $\varphi^*$:

**(E)** $\varphi^*\in\partial\Phi$ (i.e. $F(\varphi^*)=h$): then $x$ lies on a side of the extreme
triangle $T_{\varphi^*}$, on the side line through the 3-point support of that side.

**(S)** $\varphi^*\in\mathrm{int} \Phi$ and near $\varphi^*$ the support points of all three sides
are locally unique and constant. Then $\frac{d}{d\varphi}F_{\{A,O,B,x\}}(\varphi^*)=0$, i.e.
$\sum_k\langle P_k,u^\perp(\varphi^*+120^\circ k)\rangle=0$ where $P_k$ is the support point of
side $k$. This forces (writing $R_{\pm120}$ for rotations):

* (S1) $x$ on one side, say side $0$, other supports $Q_1,Q_2\in\{A,O,B\}$: then
  $x=-R_{-120^\circ}Q_1-R_{120^\circ}Q_2+h u(\varphi^*)$: $x$ lies on the circle of radius $h$
  about one of the seven centers
  $$O,\ A,\ B,\ -a u(0^\circ),\ -b u(120^\circ),\ -(a u(0^\circ)+b u(120^\circ)),\ \sigma u(60^\circ).$$
* (S2) $x$ at a vertex (on two sides), the third side supported by $Q\in\{A,O,B\}$: then
  $x-Q\ \|\ $ the third normal and $\langle Q-x,n\rangle=h$, i.e. $|x-Q|=h$: circle of radius $h$
  about $Q$.

**(T)** $\varphi^*\in\mathrm{int} \Phi$ and $\varphi^*$ is a kink of
$F_{\{A,O,B,x\}}$: two points tie as support of some side at $\varphi^*$, and the one-sided
derivatives straddle $0$. The possible ties:

* (T1) $x$ ties with $Q\in\{A,O,B\}$ on a side, and $x$ supports only that side. Then
  $F_{\{A,O,B,x\}}(\varphi^*)=F(\varphi^*)=h$, so in fact $\varphi^*\in\partial\Phi$ — this is (E)
  again, with $x$ on the extreme-triangle side through $Q$.
* (T2) $x$ ties with $Q$ on one side and $x$ also supports a second side ($x$ at a vertex $v$ of
  $T^*$, $Q$ on a side through $v$), third side supported by $Q_2\in\{A,O,B\}$: a one-parameter
  family; eliminating the triangle parameters gives the quartic $E_{QQ_2}$ (computed in §6). For
  $Q_2=Q$ it degenerates to the circle $|x-Q|=1$.
* (T3) two of $\{A,O,B\}$ tie on a side **not** containing $x$. The tie pins that side's normal:
  $u(210^\circ)$ for $\{O,A\}$ (side flush on the line $OA$), $u(270^\circ)$ for $\{O,B\}$ (flush
  on line $OB$), $u(\theta_{AB})$ for $\{A,B\}$. With the flush side fixed, either
  (a) $x$ is at the opposite vertex: lines $L_A$ ($\langle x,u(30^\circ)\rangle=h$),
  $L_B$ ($\langle x,u(90^\circ)\rangle=h$), or the $AB$-analogue
  $\langle x,u(\theta_{AB})\rangle=d_{AB}-h$ (never in $C$, cf. §9); or
  (b) $x$ is on one of the two remaining sides and the last side is supported by a point or vertex:
  the flush-slide lines $M_A$, $M_B$, $\lambda_B$, $\lambda_A$ and the horizontal/slant variants
  through $A$ or $B$ (all derived in §6; only the four named ones are ever exposed, see §9).

*Proof.* $F_{\{A,O,B,x\}}$ is a sum of maxima of finitely many smooth sinusoids in $\varphi$, hence
piecewise-smooth with kinks exactly where a support changes; at an interior minimum either the
derivative vanishes (S) or the subdifferential interval $[\partial^-,\partial^+]$ contains $0$ at a
kink (T). The derivative of a support term with unique support point $P$ is
$\langle P,u^\perp\rangle$. In case (S1) the two displayed equations ($F=h$ and $F'=0$) determine
$x$'s components along $u(\varphi^*)$ and $u^\perp(\varphi^*)$; assembling them gives
$x=h u(\varphi^*)-R_{-120^\circ}Q_1-R_{120^\circ}Q_2$, and letting $\varphi^*$ vary traces the
stated circle; the seven centers are the values of $-R_{-120^\circ}Q_1-R_{120^\circ}Q_2$ over the
support assignments that are realizable for some direction (Lemma 2.1 excludes
$(Q_1,Q_2)\in\{(O,A),(B,O)\}$). (S2), (T1)–(T3) are the analogous eliminations; (T2) is carried out
in §6. Note every case lands in the **catalog**: extreme-triangle side lines (E/T1), seven
$h$-circles (S1, S2), quartics $E_{QQ_2}$ and circles $c_A,c_B$ plus $|x-O|=1$ (T2), and flush
lines (T3). $\square$

**Proposition 4.2 (master formula).** For each $\theta$, $r^*(\theta)$ equals the maximum of the
radial coordinates (in direction $\theta$) over the finite catalog of Lemma 4.1 restricted to the
configurations realizable at that direction. In particular $\partial K$ minus the two cone edges is
covered by finitely many explicit algebraic curves, namely the catalog of `20092_ab_set_case_catalog.md` §1 (the
$h$-circles and the extra flush lines are in the catalog but turn out never to be exposed inside
$C$; §9).

*Proof.* Combine (3.1) with Lemma 4.1: the maximizing $\varphi^*$ exists by compactness of $\Phi$
and continuity, and each alternative places $x$ on a catalog curve. $\square$

**Lemma 4.3 (the circle $|x-O|=1$ never appears).** For $a,b>0$ the circle $|x-O|=1$ contains no
boundary point of $U$: a configuration (T2) with $Q=Q_2=O$ places $O$ at a vertex of $T^*$, and
$A,B\in T^*$ would lie in the $60^\circ$ wedge of $T^*$ at $O$ — impossible since
$\angle AOB=120^\circ$. (For $a=0$, when $A=O$, the circle does appear; it is then the common
degeneration of $c_A$ and $E_{AO}$, consistently with the case tables.) By contrast $c_A$ and
$c_B$ are realizable: the wedge at the vertex $A$ must contain $O$ and $B$, which subtend an angle
$\le60^\circ$ at $A$ whenever $|AO|,|AB|\ge$ the relevant chords — quantitatively this is the
containment computation of §5 and pins the exposed arcs exactly between the corners listed in the
case tables. $\square$

## 5. Lower bounds = realizability

**Lemma 5.1.** Let $\Gamma\subset C$ be the closed chain claimed for a case in `20092_ab_set_case_catalog.md` §4
(including the two cone-edge segments), and suppose every point of the chain lies in $U$. Then the
compact region $S$ enclosed by $\Gamma$ satisfies $S\subseteq K$.

*Proof.* Each claimed chain is by construction the graph of a positive continuous function
$\theta\mapsto r_\Gamma(\theta)$ over $[0^\circ,120^\circ]$ (checked case by case: consecutive arcs
meet at the listed corners with increasing $\theta$), so $S=\{ru(\theta):0\le r\le
r_\Gamma(\theta)\}$. For $x=ru(\theta)\in S$ take the chain point $x_0=r_\Gamma(\theta)u(\theta)\in
U$; a triangle $T\ni x_0$ containing $\{A,O,B\}$ contains $O$, hence the segment $[O,x_0]\ni x$.
Also $x\in C$. $\square$

So the lower bound reduces to: **every chain point is covered by an explicit triangle.** For each
arc type we exhibit the triangle and the containment inequalities:

* **Ray segments.** For $x=(t,0)$, $0\le t\le t_{B^*}=\frac{\sqrt{4-3a^2}-a}{2}$: the four points
  $O,A,B,x$ lie in a unit triangle iff the three-point set $\{O,A,(\max(t,b),0)\}$ does (the
  fourth point lies in the convex hull); by Corollary 2.3 applied to parameters $(a,\max(t,b))$
  this holds iff $a^2+a t+t^2\le1$, i.e. $t\le t_{B^*}$, which also shows $B^*\in c_A$. Mirror for
  the other ray.
* **$c_A$-arcs** ($x$ with $|x-A|=1$): take $T$ with vertices $x$, $A$, and
  $v=A+R_{-60^\circ}(x-A)$ (the choice on the clockwise side). Containment of $O$ and $B$ amounts
  to four scalar inequalities, e.g. $\langle O-A, n\rangle\le0$ etc., which hold exactly for the
  $\theta$-range between the listed corners (endpoints of the range are exactly where $O$ or $B$
  reaches a side, which is where the adjacent arc of the chain takes over; this containment is
  re-verified pointwise along every claimed arc in `2009X_computation/verify_ab_set.py`).
* **$L_A$-segments**: $T$ = the flush triangle with base
  $[x-h u(30^\circ)-\tfrac12u(120^\circ),\ x-h u(30^\circ)+\tfrac12u(120^\circ)]$ on the line
  $OA$ and apex $x$; containment of $O,A$ = both in the base segment; containment of $B$:
  $\langle B,u(30^\circ)\rangle=\frac{\sqrt3}2b\le h$ automatic, and the two lateral constraints
  hold exactly between the corners listed ($P_1,G_1,P_2$-range). Similarly $L_B$, and $M_A,M_B$
  (the rigid triangles $T_A^*,T_B^*$; e.g. $B\in T_A^*$ iff
  $\langle B,u(-30^\circ)\rangle\le\frac{\sqrt3}{2}(1-a)$ iff $\sigma\le1$),
  and $\lambda_B,\lambda_A$ (sliding flush triangles; the slide interval is nonempty exactly on the
  exposed sub-segment).
* **Extreme segments** $s^{\bullet}_{\bullet}$: $T=T_{\varphi_e}$ itself.
* **Quartic arcs** $E_{QQ_2}$: $T$ = the defining pivot triangle of the configuration (T2), which
  by construction contains $Q,Q_2,x$; the containment of the remaining point is a single scalar
  inequality along the arc, which holds precisely between the listed corners. (Equality at a corner
  is exactly the corner condition — e.g. the $E_{BO}$-arc pivots keep $A$ inside until
  $\varphi$ reaches the value at which $A$ touches a side, which is the handover corner $W_\mp$ or
  $G_1'$ or $P_2$… as listed.)

All these scalar inequalities are polynomial in $(a,b)$ and the arc parameter; they are verified
symbolically/numerically in `2009X_computation/verify_ab_set.py` over each case region (see
`20094_ab_set_verification.md`).

## 6. Derivation of the catalog curves

Below $\varphi$ is the orientation, $n_k=u(\varphi+120^\circ k)$; complex notation
$z\simeq(X,Y)$.

**6.1 Circles of radius $h$ (S1/S2).** Immediate from Lemma 4.1: e.g. for (S1) with
$(Q_1,Q_2)=(A,B)$, the side line through $x$ is
$\langle y,u(\varphi)\rangle=h-\langle A,n_1\rangle-\langle B,n_2\rangle
= h-\langle a u(0^\circ)+b u(120^\circ),u(\varphi)\rangle$, whose envelope over $\varphi$ is the
circle of radius $h$ centered $-(a u(0^\circ)+b u(120^\circ))$. These circles never win the
maximum (3.1) inside $C$ (they are dominated by the (T2)/(T3)/(E) families; part of the §9
comparisons), so they do not appear in the case tables.

**6.2 The quartics (T2).** Configuration: $x$ at the vertex $n_0\wedge n_1$, companion $Q$ on the
side with normal $n_1$ (chirality; the other chirality exchanges the roles of $n_0,n_1$), $Q_2$ on
the side with normal $n_2$. Solving
$\langle x,n_0\rangle=h-\langle Q,n_1\rangle-\langle Q_2,n_2\rangle$,
$\langle x,n_1\rangle=\langle Q,n_1\rangle$ for $x$ gives (with $w=e^{i\varphi}$)
$$z(\varphi)=e^{i(\varphi+30^\circ)}+\frac{Q e^{i30^\circ}-Q_2 e^{i150^\circ}}{\sqrt3}
-\frac{i(\bar Q-\bar Q_2)}{\sqrt3} e^{2i\varphi} \tag{6.1}$$
(and the mirror-chirality formula with $e^{i(\varphi+90^\circ)}$, $e^{-i30^\circ}$,
$+e^{-i30^\circ}(\bar Q-\bar Q_2)$). These are limaçons: a fixed circle of radius 1 plus a second
harmonic of amplitude $\frac{|Q-Q_2|}{\sqrt3}$. Eliminating $\varphi$
(resultants; done in `2009X_computation/derive_quartics.py`) yields the implicit quartics $E_{AO},E_{BO},E_{BA},E_{AB}$ printed
in `20092_ab_set_case_catalog.md` §1. For $Q=Q_2$, (6.1) is the circle $|z-Q|=1$; this is how $c_A$ ($Q=A$) and $c_B$
($Q=B$) arise, while $Q=O$ is excluded by Lemma 4.3. Smoothness on the exposed ranges: a limaçon
$e^{it}+\gamma e^{2it}$ is regular iff $|\gamma|\ne\frac12$; here $|\gamma|\in\{\frac a{\sqrt3},
\frac b{\sqrt3},\frac R{\sqrt3}\}$ and on the exposed ranges $a<\frac12$ (resp. $b<\frac12$,
$R<\frac12$… in fact $\sigma<\frac12$) holds, so $|\gamma|<\frac1{2}$—no cusps or loops on exposed
arcs.

**6.3 Flush lines (T3).** Side flush on line $OA$ means normal $n_1=u(210^\circ)$, support value
$0$; then $c_0+c_2=h$. If $x$ is the opposite vertex, $\langle x,n_0\rangle+\langle x,n_2\rangle
=\langle x,-n_1\rangle=\langle x,u(30^\circ)\rangle=h$: the line $L_A$. If $x$ is on the side with
normal $u(330^\circ)$ (the "right" side) and the third side touches $A$ at its end
(vertex at $A$), the triangle is the rigid $T_A^*$ and $x$ moves on
$\langle x,u(330^\circ)\rangle=h-\langle A,u(90^\circ)\rangle=\frac{\sqrt3}{2}(1-a)$: the line
$M_A$. If instead the third side touches $B$, the triangle slides and
$\langle x,u(90^\circ)\rangle=h-\langle B,u(330^\circ)\rangle=\frac{\sqrt3}{2}(1-b)$: the line
$\lambda_B$. The $OB$-flush family gives $L_B$, $M_B$, $\lambda_A$ mirror-wise. (The remaining
combinatorial options — third side touching $O$, or the $AB$-flush family — produce lines that are
never exposed inside $C$; §9.)

**6.4 Extreme segments (E).** At $\varphi_e\in\partial\Phi$, $U_{\varphi_e}$ is the single triangle
$T_{\varphi_e}$; its side lines are $\langle x,n_k\rangle=m_k(\varphi_e)$ with the supports of
Lemma 2.1. The values of $\varphi_e$ per band (Corollary 2.3) give exactly the line formulas
$s_A^{\mathrm{out}},s_B^{\mathrm{out}},s_A^{\mathrm{mid}},s_B^{\mathrm{mid}},
s_A^{\mathrm{IV}},s_B^{\mathrm{IV}}$ of `20092_ab_set_case_catalog.md` §1 after substituting
$\cos\psi_1=\frac{\sqrt3}{2\sigma}$, $\sin\psi_1=\frac{q}{2\sigma}$,
$\cos\kappa=\frac{\sqrt3}{2R}$, $\sin\kappa=\frac p{2R}$ and the $\theta_{AB}$ data of Lemma 2.1
(routine trigonometry; verified in sympy).

## 7. Corner identities and thresholds

All statements below are polynomial identities in $(a,b)$, verified exactly in sympy
(`2009X_computation/derive_thresholds.py`; also re-checked numerically). Redundant spurious factors like $(\sigma\pm1)$
powers are discarded against the band inequalities.

1. $P_1=A+(1,0)$ lies on $c_A$, $L_A$ and $E_{AO}$ for all $a,b$; $E_{AO}$ is tangent to $L_A$ at
   $P_1$ iff $a=\frac12$. For $a<\frac12$ the arc of $E_{AO}$ emanating from $P_1$ lies strictly
   above $L_A$ (outside the half-plane $\langle x,u(30^\circ)\rangle\le h$), for $a>\frac12$
   strictly below — whence the predicate $\alpha$.
2. $P_3=B+u(120^\circ)$ lies on $c_B\cap L_B\cap E_{BO}$; tangency of $E_{BO},L_B$ at $P_3$ iff
   $b=\frac12$ — predicate $\beta$. (Mirror of 1.)
3. $P_2=B+(1-b)u(60^\circ)\in L_A\cap E_{BA}\cap E_{BO}$, and $E_{BA}$ is tangent to $L_A$ at $P_2$
   iff $\sigma=\frac12$; $P_2'=A+(1-a)u(60^\circ)\in L_B\cap E_{AB}\cap E_{AO}$, tangency of
   $E_{AB},L_B$ at $P_2'$ iff $\sigma=\frac12$ — predicate $\varepsilon$. ($E_{BO}$ is transversal
   to $L_A$ at $P_2$ unless $b=\frac12$; $E_{AO}$ transversal to $L_B$ at $P_2'$ unless
   $a=\frac12$.)
4. Restrictions to the flush lines factor as
   $$E_{AO}\big|_{L_A}\propto\bigl(t-(a-\tfrac12)\bigr) \mathcal C_A(t),\qquad
   E_{BO}\big|_{L_B}\propto\bigl(t-(b-\tfrac12)\bigr) \mathcal C_B(t),$$
   $$E_{BA}\big|_{L_A}\propto\bigl(t-(\tfrac12-b)\bigr) \mathcal D_A(t),\qquad
   E_{AB}\big|_{L_B}\propto\bigl(t-(\tfrac12-a)\bigr) \mathcal D_B(t),$$
   with the cubics of `20092_ab_set_case_catalog.md` §2 (parametrizations: on $L_A$,
   $x=(\tfrac34-\tfrac t2,\ \tfrac{\sqrt3}4(1+2t))$, so $t=a-\frac12\leftrightarrow P_1$ and
   $t=\frac12-b\leftrightarrow P_2$; on $L_B$, $x=(t,\tfrac{\sqrt3}2)$, so
   $t=b-\frac12\leftrightarrow P_3$, $t=\frac12-a\leftrightarrow P_2'$). This identifies
   $G_1,G_1',G_2,G_2'$ and shows they are the *unique* extra crossings in the relevant ranges.
5. $E_{BO}$ passes through $P_2'$ iff $(\sigma-1) \mathcal W=0$ where
   $\mathcal W=a^3+a^2b-a^2+a-b$; equivalently $\mathcal C_B\bigl(\tfrac12-a\bigr)=-8 \mathcal W$.
   Note the exact identity $w_-=-\mathcal W$ (expand: $-\mathcal W=b(1-a^2)-a(a^2-a+1)$).
   Since the $E_{BO}$-arc through $P_2$ and $P_3$ is the outermost long arc on its side, the
   $B$-side flank (the $E_{AB}$/$L_B$ pieces around $P_2'$) is exposed iff $E_{BO}$ passes
   radially *inside* $P_2'$, i.e. iff $w_->0$; the threshold is exactly $P_2'\in E_{BO}$, i.e.
   $\mathcal W=0$. Mirror: the $A$-side flank is exposed iff $w_+>0$, threshold $P_2\in E_{AO}$,
   via $P_2\in E_{AO}\iff(\sigma-1)(ab^2-a+b^3-b^2+b)=0$ and
   $w_+=-(ab^2-a+b^3-b^2+b)$.
6. $\eta_\pm$ (band I, $\varepsilon$-regime): the segment of $L_B$ between $E_{AB}$ and $E_{BO}$
   appears exactly when their crossing $Q_2'$ passes below $L_B$; at the threshold
   $E_{AB},E_{BO},L_B$ are concurrent, i.e. the cubics $\mathcal D_B,\mathcal C_B$ have a common
   root: $\mathrm{Res}_t(\mathcal D_B,\mathcal C_B)=0$, the polynomial $\mathcal E(a,b)$
   (sign convention checked on the region: exposure $\iff\mathcal E>0$; numerically the transition
   was located independently by bisection at $(a,b)=(0.135, b)$, giving $b=0.27225\ldots$, at
   which the two real roots coincide to $2\cdot10^{-16}$ and $\mathcal E$ vanishes to
   $6\cdot10^{-17}$). The event is independent of the state of the other side, so it also splits
   the both-flanks region into I.1/I.1a/I.1b/I.1c; e.g. at $(0.24,0.255)$ both $\eta_\pm$ hold and
   the verified chain is the ten-arc I.1c chain. Mirror on $L_A$: $\mathcal E(b,a)$.
7. Outer-dip flush ($\lambda_B$): exposed iff the level $\frac{\sqrt3}2(1-b)$ exceeds the height of
   the crossing $s_A^{\mathrm{out}}\cap s_B^{\mathrm{out}}$; eliminating radicals gives the
   polynomial threshold $\mathcal G(a,b)$ of `20092_ab_set_case_catalog.md` §3 (factor of degree 5; the discarded
   factors $(\sigma-1)^2(\sigma+1)$ do not vanish in bands II–III interior). Mirror $\lambda_A$:
   $\mathcal G(b,a)$. At most one of $\mathcal G(a,b),\mathcal G(b,a)$ is positive
   (their sum is negative on $\sigma\le1$… verified numerically on the region — see verification).
8. Mid-dip flush ($M_A$; band III, $a>b$): exposed iff the $M_A$-line lies radially beyond
   $s_A^{\mathrm{mid}}\cap s_B^{\mathrm{mid}}$; eliminating radicals, the essential factor is
   $$(3+a) R^2-3,$$
   giving the predicate $\mu$. Mirror: $(3+b)R^2-3$.
9. Corner–vertex identities: the corner between $c_A$ and $s_A^{\mathrm{mid}}$ is
   $V_A^{\mathrm{mid}}=A+u(r_2-90^\circ)$, the far endpoint of the side of $T_{r_2}$ through its
   vertex $A$ (both on $c_A$, distance $1$ from $A$, and on the side line); similarly
   $\widetilde V_A^{\mathrm{mid}}=A+u(r_3-90^\circ)$, $V_A^{\mathrm{IV}}=A+u(\varphi_+-90^\circ)$,
   $V_B^{\mathrm{IV}}=B+u(\varphi_-+90^\circ)$; and the corners between the long arcs and the outer
   segments are the $AB$-vertices $W_\mp$ of $T_{\mp\psi_1}$ (the unique vertex on both the side
   through $A$ and the side through $B$). These are direct consequences of the configuration
   degenerations: e.g. approaching the end of the admissible interval, the (T2) pivot triangle of
   $E_{BO}$ converges to $T_{\varphi_e}$ with $x$ converging to its $AB$-vertex.

## 8. Proposed case-by-case inclusion of the chains in $U$

For each sampled case of `20092_ab_set_case_catalog.md` §4, the constructions
of §5 numerically realize the listed arcs and the endpoint corners are where
the sampled containment inequality becomes active.  The script also observes
the claimed increasing-$\theta$ order.  A proof of the uniform containment
inequalities and of the corner order over each whole case region is still
required before Lemma 5.1 can be used to conclude $S\subseteq K$ globally.

## 9. Unresolved case-by-case maximality ($K\subseteq S$)

Fix a case region and $\theta\in(0^\circ,120^\circ)$. By Proposition 4.2, $r^*(\theta)$ is the
largest radial value among the realizable catalog configurations at direction $\theta$. The claimed
chain radius $r_\Gamma(\theta)$ belongs to the catalog, so $r^*\ge r_\Gamma$ is automatic (§8), and
it remains to show no other catalog configuration exceeds $r_\Gamma(\theta)$. The finitely many
comparisons are of three kinds:

1. **Curve-vs-curve on a sector.** E.g. in case I.6, for $\theta$ between $\theta(P_1)$ and
   $\theta(P_2)$ one checks that $L_A$ dominates $c_A$, $c_B$, $E_{AO}$, $E_{BO}$, $E_{BA}$,
   $E_{AB}$, the seven $h$-circles and the other flush lines. Such a comparison
   would be certified by the following standard semialgebraic scheme once its
   hypotheses are proved for every listed pair.

   **Lemma 9.1 (sector-certification template).** Let $f,g:(\theta;a,b)\mapsto\mathbb R$ be the radial
   functions of two catalog curves, continuous on a sector bundle
   $\Sigma=\{(\theta,a,b):\ (a,b)\in\Omega,\ \theta\in[\theta_0(a,b),\theta_1(a,b)]\}$ over a
   connected case region $\Omega$, with algebraic graphs. If $f=g$ has no solution in the interior
   of $\Sigma$, then $\mathrm{sign}(f-g)$ is constant on the interior of $\Sigma$, so a
   single interior evaluation decides the comparison on all of $\Sigma$. The no-solution
   hypothesis in turn is equivalent to the intersection locus of the two
   curves missing the open sector for every $(a,b)\in\Omega$. $\square$

   The catalog has not yet proved that no unlisted intersection locus meets
   the open sector, nor that every $\Omega$ used here is connected.  Those are
   hypotheses of the template, not consequences of the threshold list.

   Each comparison is thus reduced to the corner identities (§7), the constant signs of the
   threshold polynomials on the case region (definitional), and one interior evaluation per
   comparison per case region; the interior evaluations are performed at high precision (residual
   margins $\gg10^{-6}$, far above the $10^{-10}$ computational accuracy) in `2009X_computation/verify_ab_set.py`.
2. **Non-realizability.** Configurations that are realizable as critical data but whose defining
   triangle fails to contain all of $\{A,O,B\}$ at direction $\theta$ do not enter the max. This
   prunes: the $h$-circles inside $C$ (their (S1)/(S2) triangles always lose a containment against
   the competing (T2)/(T3) configuration that dominates them — e.g. the $|x-O|=h$ circle is
   dominated by $L_A/L_B$ wherever its configuration is feasible); the $AB$-flush lines
   ($\langle x,u(\theta_{AB})\rangle=d_{AB}-h$ has negative right side, so the line misses
   $C$ entirely); the variants of (T3b) with third-side support $O$ (their lines pass through
   regions already dominated by $L_A$ or $L_B$); and, by Lemma 4.3, the circle $|x-O|=1$ for
   $a,b>0$.
3. **$\Phi$-endpoint capping.** For $\theta$ in a dip sector, all interior-critical configurations
   have already been pruned or dominated, and $\rho_\varphi(\theta)$ is maximized at
   $\varphi\in\partial\Phi$ (the function $\varphi\mapsto\rho_\varphi(\theta)$ is monotone toward
   the endpoint on each side of the gap — its derivative is single-signed there because the
   binding hexagon constraint's envelope point lies outside the sector); hence
   $r^*(\theta)=\max(\rho_{\varphi_e^-},\rho_{\varphi_e^+},\text{flush lines})$, which is exactly
   the dip description (segments of $T_{\varphi_e}$ sides and the exposed flush lines, resolved by
   $\mathcal G$, $\mu$).

The numerical outcomes are tabulated by
`2009X_computation/verify_ab_set.py`. Dense grids and exact checks of the
quoted identities support the proposed comparisons, but do not verify their
universal quantifiers.  Thus §§8--9 do not yet prove $S=K$ on the general case
regions.

## 10. Unresolved comprehensiveness

The case regions are defined by sign conditions on the finite polynomial family
$$\Bigl\{R^2-1,\ 4\sigma^2-3,\ 4R^2-3,\ \sigma-1,\ a-\tfrac12,\ b-\tfrac12,\ \sigma-\tfrac12,\
w_+,\ w_-,\ \mathcal E(a,b),\ \mathcal E(b,a),\ \mathcal G(a,b),\ \mathcal G(b,a),\
(3+a)R^2-3,\ (3+b)R^2-3,\ a-b\Bigr\}.$$
Every point of $\{a,b\ge0\}$ satisfies one of $R^2>1$ (Case 0) or the band
inequalities I--IV.  Within a band, however, completeness of the shorter
subcase tables requires the following pruning implications.  The script found
no violations on its finite grid; exact proofs are still required where none
is supplied below:

* $\varepsilon\Rightarrow\alpha\wedge\beta$ (trivially);
* in bands I–III at least one of $w_\pm>0$ ($w_+\le0\wedge w_-\le0$ forces $\sigma\ge1$);
* band I $\wedge\ a\ge\tfrac12\Rightarrow w_+>0\wedge w_-\le0$ (so I.6 needs no further split);
* band II excludes $\varepsilon$ ($\sigma>\tfrac{\sqrt3}2>\tfrac12$);
* within bands II–III never $\mathcal G(a,b)>0\wedge\mathcal G(b,a)>0$; in band II the flush lines
  occur only in the rows II.1/II.1′;
* band III $\wedge a>b\Rightarrow a>\tfrac12>b$ (proved in §2-style estimates: $\max(a,b)\le\tfrac12$
  would give $R^2\le\tfrac34$, and $a,b>\tfrac12$ would give $\sigma>1$);
* band III $\wedge a>b$: $(3+a)R^2>3\Rightarrow\mathcal G(a,b)>0$ (so case "$M_A$ without
  $\lambda_B$" is empty);
* band IV admits no side predicates (the corner configurations at $P_1,P_2,P_2',P_3$ need
  $\varphi=90^\circ$ or $30^\circ$ admissible, i.e. $F(90^\circ)=\tfrac{\sqrt3}2\sigma\le h$, i.e.
  $\sigma\le1$).

The claimed agreement of every adjacent chain on every threshold boundary is
likewise part of the remaining global certification problem.  The exact Band
IV candidate chain is recorded separately in `20091`; its global support
partition remains open.

---

### Appendix: verified identity list

(All checked exactly in sympy; script `2009X_computation/derive_thresholds.py`, `2009X_computation/derive_quartics.py`.)

* $F$-formulas (2.1); $\min F=\frac{\sqrt3}{2}R$; band endpoints.
* Implicit quartics of $E_{AO},E_{BO},E_{BA},E_{AB}$ from the parametrizations (6.1).
* $P_1\in c_A\cap L_A\cap E_{AO}$; $P_2\in L_A\cap E_{BA}\cap E_{BO}$;
  $P_2'\in L_B\cap E_{AB}\cap E_{AO}$; $P_3\in L_B\cap c_B\cap E_{BO}$.
* Tangency thresholds: $E_{AO}$–$L_A$ at $P_1$: $2a-1$; $E_{BO}$–$L_B$ at $P_3$: $2b-1$;
  $E_{BA}$–$L_A$ at $P_2$: $(b-1)(2\sigma-1)$; $E_{AB}$–$L_B$ at $P_2'$: $(a-1)(2\sigma-1)$;
  $E_{BO}$–$L_A$ at $P_2$: $(b-1)(2b-1)$; $E_{AO}$–$L_B$ at $P_2'$: $(a-1)(2a-1)$.
* Factorizations of the restrictions to $L_A,L_B$ (§7.4) and
  $\mathcal C_B(\tfrac12-a)=-8 \mathcal W$.
* $P_2'\in E_{BO}\iff(\sigma-1)\mathcal W=0$; $P_2\in E_{AO}\iff(\sigma-1)(ab^2-a+b^3-b^2+b)=0$.
* $\mathcal G$ (outer flush) and $(3+a)R^2-3$ (mid flush) thresholds by radical elimination.
* Vertex identities of §7.9.
