# AB-Set Case Catalog

Status: Empirical

**Setup.** Let $O=(0,0)$, let $B=(b,0)$ with $b\ge0$ on the positive $x$-axis, and let
$A=a (\cos120^\circ,\sin120^\circ)=\bigl(-\tfrac a2,\tfrac{\sqrt3}2a\bigr)$ with $a\ge0$, so that
$\angle AOB=120^\circ$ counterclockwise. Let
$C=\{r(\cos\theta,\sin\theta):r\ge0,\ 0^\circ\le\theta\le120^\circ\}$ be the closed convex cone
spanned by the directions of $OB$ and $OA$ (for $a=0$ or $b=0$ we keep this same cone).

> **Definition.** The **ab-set** is
> $$K(a,b)\;=\;\Bigl( \bigcup\{T:\ T\ \text{closed equilateral triangle of side }1,\ \{A,O,B\}\subset T\}\Bigr)\ \cap\ C .$$

This file records a proposed complete answer: a partition of
$\{(a,b):a,b\ge0\}$ into cases described by polynomial inequalities, and for
each case a proposed boundary $\partial K(a,b)$ as a list of explicit
algebraic curves in counterclockwise order.  The general catalog remains
empirical because the global curve comparisons and predicate-region pruning
have not been certified.  The exact proof ledger is in
[`20093_ab_set_proofs.md`](20093_ab_set_proofs.md). Numerical checks of every sampled case are in
[`2009X_computation/verify_ab_set.py`](2009X_computation/verify_ab_set.py), summarized in
[`20094_ab_set_verification.md`](20094_ab_set_verification.md).

The strict Band IV subcase $a+b>1$, $R^2<1$ is isolated as a numerically
supported lemma target in
[`20091_ab_union_curve_a_plus_b_gt_1.md`](20091_ab_union_curve_a_plus_b_gt_1.md).
Its candidate formula survives extensive tests, but the written
support-pattern exhaustion is incomplete.

**Notation.**
$$h=\tfrac{\sqrt3}2,\qquad \sigma=a+b,\qquad R=\sqrt{a^2+ab+b^2}\;(=|AB|),\qquad
u(\theta)=(\cos\theta,\sin\theta),$$
$$q=\sqrt{4\sigma^2-3}\ \ (\sigma\ge h),\qquad p=\sqrt{4R^2-3}\ \ (R\ge h).$$

Basic facts (proved in the companion file):

* **Fitting criterion (Viviani).** A finite set $S$ fits in a unit equilateral triangle with outer
  normals $u(\varphi+120^\circ k)$, $k=0,1,2$, iff
  $F_S(\varphi)=\sum_k\max_{p\in S}\langle p,u(\varphi+120^\circ k)\rangle\le h$.
* **Existence.** With $F=F_{\{A,O,B\}}$: $\min_\varphi F=\tfrac{\sqrt3}2R$. Hence:

> **Case 0.** If $a^2+ab+b^2>1$, then $K(a,b)=\varnothing$.
> If $a^2+ab+b^2=1$, then $K$ is the intersection of $C$ with the single unit triangle having base
> $[A,B]$ and third vertex on the $O$-side of line $AB$ — a convex polygon (its boundary: the two
> cone-edge segments and parts of the triangle's sides).

* **Symmetry.** Reflection across the ray $\theta=60^\circ$,
  $(X,Y)\mapsto\bigl(-\tfrac X2+\tfrac{\sqrt3}2Y,\ \tfrac{\sqrt3}2X+\tfrac Y2\bigr)$, maps
  $K(a,b)$ to $K(b,a)$. "Mirror case" below always means: swap $a\leftrightarrow b$, reflect all
  curves, reverse the counterclockwise order.

**Bands.** For $R<1$ let $\Phi=\{\varphi:F(\varphi)\le h\}$ (period $120^\circ$) be the set of
admissible triangle orientations. Its topology yields the primary cases:

| band | polynomial inequalities | $\Phi$ |
|---|---|---|
| I   | $4\sigma^2\le3$ | everything |
| II  | $4\sigma^2>3$ and $4R^2\le3$ | one gap: the **outer gap** $(-\psi_1,\psi_1)$, $\cos\psi_1=\frac{\sqrt3}{2\sigma}$ |
| III | $4R^2>3$ and $\sigma\le1$ | outer gap **and** **mid gap** $(\theta_{AB}\!\pm\!30^\circ\!-\kappa,\ \theta_{AB}\!\pm\!30^\circ\!+\kappa)$, $\cos\kappa=\frac{\sqrt3}{2R}$ ($+$ if $a>b$, $-$ if $b>a$) |
| IV  | $\sigma>1$ and $R^2\le1$ | single arc $[\theta_{AB}-30^\circ+\kappa,\ \theta_{AB}+30^\circ-\kappa]$ |

Here $\theta_{AB}$ is the outer normal direction of segment $AB$:
$\cos\theta_{AB}=\frac{\sqrt3a}{2R},\ \sin\theta_{AB}=\frac{a+2b}{2R}$.
Bands I–IV and Case 0 cover the quadrant; on shared band boundaries the adjacent descriptions
coincide (degenerating arcs have zero length), so closed inequalities may be used everywhere.

---

## 1. Catalog of boundary curves

Every boundary arc of every ab-set is an arc of one of the following curves.

**Cone edges.**
$$\ell_{OB}:\ Y=0\ \ \text{(exposed part: } [O,B^*]\text{)},\qquad
\ell_{OA}:\ \sqrt3X+Y=0\ \ \text{(exposed part: }[A^*,O]\text{)},$$
$$B^*=\Bigl(\tfrac{\sqrt{4-3a^2}-a}{2},0\Bigr),\qquad
A^*=\tfrac{\sqrt{4-3b^2}-b}{2} u(120^\circ)$$
($B^*$ = the point of the ray at distance $1$ from $A$; $A^*$ at distance $1$ from $B$).

**Circles** ($x$ and a fixed vertex at two vertices of the triangle — a diameter pair):
$$c_A:\ \bigl(X+\tfrac a2\bigr)^2+\bigl(Y-\tfrac{\sqrt3}2a\bigr)^2=1,\qquad
c_B:\ (X-b)^2+Y^2=1 .$$

**Lines** (one triangle side flush along line $OA$ or line $OB$):
$$\begin{aligned}
&L_A:\ \sqrt3X+Y=\sqrt3 \quad(\text{flush on }OA,\ x\ \text{at the opposite vertex}),\\
&L_B:\ 2Y=\sqrt3 \quad(\text{flush on }OB,\ x\ \text{opposite}),\\
&M_A:\ \sqrt3X-Y=\sqrt3(1-a) \quad(\text{flush on }OA\ \text{with a vertex pinned at }A:\ \text{the rigid triangle}\ T_A^*=\{A, A+u(-60^\circ), A+(1,0)\};\ x\ \text{on its third side}),\\
&M_B:\ Y-\sqrt3X=\sqrt3(1-b) \quad(\text{mirror: }T_B^*=\{B, B-(1,0), B+u(120^\circ)\}),\\
&\lambda_B:\ 2Y=\sqrt3(1-b) \quad(\text{flush on }OA,\ \text{sliding, with }B\ \text{on the right side};\ x\ \text{on the top side}),\\
&\lambda_A:\ \sqrt3X+Y=\sqrt3(1-a) \quad(\text{flush on }OB,\ \text{sliding, with }A\ \text{on the left side}).
\end{aligned}$$

**Extreme-orientation segments** (sides of the unique triangle at an endpoint of $\Phi$):

* outer gap (bands II–III):
  $$s_A^{\mathrm{out}}:\ \sqrt3(q-1)X+(3+q)Y=2\sqrt3 a
  \qquad\text{(side through }A\text{ of }T_{-\psi_1},\ \text{normal }u(120^\circ-\psi_1)),$$
  $$s_B^{\mathrm{out}}:\ \sqrt3X+qY=\sqrt3 b
  \qquad\text{(side through }B\text{ of }T_{+\psi_1},\ \text{normal }u(\psi_1)).$$
* mid gap (band III; formulas for $a>b$, mirror them for $b>a$):
  $$s_A^{\mathrm{mid}}:\ \sqrt3\bigl[(a-b)+\sigma p\bigr]X+\bigl[3\sigma-(a-b)p\bigr]Y
  =\sqrt3 a (a+2b-ap)$$
  (side through $A$ of $T_{r_2}$, $r_2=\theta_{AB}+30^\circ-\kappa$; this triangle has a **vertex at $A$**),
  $$s_B^{\mathrm{mid}}:\ \sqrt3\bigl[(a+2b)+ap\bigr]X+\bigl[(a+2b)p-3a\bigr]Y
  =\sqrt3 b (a+2b+ap)$$
  (side through $B$ of $T_{r_3}$, $r_3=\theta_{AB}+30^\circ+\kappa$; vertex at $A$).
* band IV: $s_A^{\mathrm{IV}}$ = the same line as $s_A^{\mathrm{mid}}$ (side through $A$ of
  $T_{\varphi_+}$, $\varphi_+=\theta_{AB}+30^\circ-\kappa$, vertex at $A$), and
  $$s_B^{\mathrm{IV}}:\ \sqrt3\bigl[(2a+b)-bp\bigr]X+\bigl[3b+(2a+b)p\bigr]Y
  =\sqrt3 b \bigl[(2a+b)-bp\bigr]$$
  (side through $B$ of $T_{\varphi_-}$, $\varphi_-=\theta_{AB}-30^\circ+\kappa$, vertex at $B$).

**Quartics** ($x$ at a vertex; one of $A,O,B$ on a side through $x$; another on the opposite side).
With $w=X^2+Y^2$:

$$E_{AO}:\ 3w^2+6aXw-2\sqrt3 aYw-3w+3a^2X^2+a^2Y^2-2\sqrt3 a^2XY-3aX+3\sqrt3 aY-3a^2=0,$$
$$E_{BO}:\ 3w^2-6bXw+2\sqrt3 bYw-3w+3b^2X^2+b^2Y^2-2\sqrt3 b^2XY+6bX-3b^2=0,$$
$$\begin{aligned}
E_{BA}:\ &3w^2+6(a-b)Xw-2\sqrt3(a-b)Yw-3w\\
&+3(a-b)^2X^2-6abX^2+(a-b)^2Y^2-6abY^2-2\sqrt3(a-b)^2XY\\
&-6ab(a-b)X+2\sqrt3 ab(a-b)Y+6bX+3a^2b^2-3b^2=0,
\end{aligned}$$
$$E_{AB}:\ \text{same as }E_{BA}\ \text{with the last line replaced by}\ \
-6ab(a-b)X+2\sqrt3 ab(a-b)Y-3aX+3\sqrt3 aY+3a^2b^2-3a^2=0 .$$

Parametrically ($\mathbb R^2\simeq\mathbb C$; $\varphi$ = triangle orientation): these are
limaçons, e.g.
$$E_{BO}:\ z(\varphi)=e^{i(\varphi+90^\circ)}+\tfrac b{\sqrt3}e^{-i30^\circ}\bigl(1+e^{2i\varphi}\bigr),
\qquad
E_{AO}:\ z(\varphi)=e^{i(\varphi+30^\circ)}+\tfrac a{\sqrt3}e^{i150^\circ}+\tfrac a{\sqrt3}e^{i(2\varphi+150^\circ)} .$$
The subscript convention: $E_{QQ'}$ has companion $Q$ on the side through $x$ and $Q'$ on the
opposite side. As $a\to0$, $c_A$ and $E_{AO}$ degenerate to the circle $X^2+Y^2=1$; as $b\to0$,
$c_B$ and $E_{BO}$ do — this makes the axes $a=0$, $b=0$ continuous limits of every case below.

---

## 2. Distinguished points (corners)

* $P_1=A+(1,0)=\bigl(1-\tfrac a2,\ \tfrac{\sqrt3}2a\bigr)\ \in\ c_A\cap L_A\cap E_{AO}$ (always).
* $P_2=B+(1-b)u(60^\circ)=\bigl(\tfrac{1+b}2,\ \tfrac{\sqrt3}2(1-b)\bigr)\ \in\ L_A\cap E_{BA}\cap E_{BO}$.
* $P_2'=A+(1-a)u(60^\circ)=\bigl(\tfrac{1-2a}2,\ \tfrac{\sqrt3}2\bigr)\ \in\ L_B\cap E_{AB}\cap E_{AO}$.
* $P_3=B+u(120^\circ)=\bigl(b-\tfrac12,\ \tfrac{\sqrt3}2\bigr)\ \in\ L_B\cap c_B\cap E_{BO}$.
* $G_1\in L_A\cap E_{AO}$: with the parametrization $x(t)=\bigl(\tfrac34-\tfrac t2,\
  \tfrac{\sqrt3}4(1+2t)\bigr)$ of $L_A$, $G_1=x(t)$ at the unique root
  $t\in\bigl(a-\tfrac12,\ \tfrac12-b\bigr)$ of
  $$\mathcal C_A(t)=8t^3-(4+8a)t^2+(6+8a)t+(6a-3).$$
* $G_1'\in L_B\cap E_{BO}$: $x=(t,\tfrac{\sqrt3}2)$ at the unique root
  $t\in\bigl(b-\tfrac12,\ \tfrac12-a\bigr)$ of
  $$\mathcal C_B(t)=8t^3-(4+8b)t^2+(6+8b)t+(6b-3).$$
* $G_2\in L_A\cap E_{BA}$ and $G_2'\in L_B\cap E_{AB}$: the analogous relevant roots of
  $$\mathcal D_A(t)=8t^3+(4-16a+8b)t^2+(6+8a^2-16ab-8b)t+(3-12a-4a^2+8ab+8a^2b-6b),$$
  $$\mathcal D_B(t)=8t^3+(4+8a-16b)t^2+(6-8a-16ab+8b^2)t+(3-6a+8ab+8ab^2-4b^2-12b).$$
  (Identities: $E_{AO}\cap L_A=\{P_1\}\cup\{\mathcal C_A\text{-roots}\}$,
  $E_{BA}\cap L_A=\{P_2\}\cup\{\mathcal D_A\text{-roots}\}$,
  $E_{BO}\cap L_B=\{P_3\}\cup\{\mathcal C_B\text{-roots}\}$,
  $E_{AB}\cap L_B=\{P_2'\}\cup\{\mathcal D_B\text{-roots}\}$; and
  $\mathcal C_B\bigl(\tfrac12-a\bigr)=-8(a^3+a^2b-a^2+a-b)$.)
* $Q$-corners (transversal quartic–quartic crossings): $Q_1=E_{AO}\cap E_{BA}$,
  $Q_2=E_{BA}\cap E_{BO}$, $Q_1'=E_{AO}\cap E_{AB}$, $Q_2'=E_{AB}\cap E_{BO}$,
  $Q_M=E_{BO}\cap E_{AO}$ — each the unique intersection in the arc range where it is listed
  (algebraically: the appropriate real root of the resultant of the two quartics).
* Extreme-triangle vertices:
  * mid gap (band III, $a>b$): $V=A+u(r_2-90^\circ)$ and $\widetilde V=A+u(r_3-90^\circ)$ — both on
    $c_A$ (they are at distance 1 from the vertex $A$);
  * band IV: $V=A+u(\varphi_+-90^\circ)\in c_A$ and $V'=B+u(\varphi_-+90^\circ)\in c_B$;
  * outer gap: $W_-$ = the vertex of $T_{-\psi_1}$ on both its side through $A$ and its side
    through $B$, i.e. the solution of
    $\langle x,u(120^\circ-\psi_1)\rangle=a\cos\psi_1,\ \langle x,u(-\psi_1)\rangle=b\cos\psi_1$;
    $W_+$ = the vertex of $T_{+\psi_1}$ on its sides through $B$ and through $A$:
    $\langle x,u(\psi_1)\rangle=b\cos\psi_1,\ \langle x,u(\psi_1+120^\circ)\rangle=a\cos\psi_1$.
* Line–line dip corners: intersections of
  $s_A^{\mathrm{out}},\lambda_B\ (\text{or }\lambda_A),s_B^{\mathrm{out}}$, of
  $s_A^{\mathrm{mid}},M_A\ (\text{or }M_B),s_B^{\mathrm{mid}}$, and of
  $s_A^{\mathrm{IV}},s_B^{\mathrm{IV}}$ — explicit $2\times2$ linear systems.

---

## 3. Sub-case predicates

All fine structure is decided by the signs of the following polynomials (geometric meaning and the
proof that each is the exact threshold: proofs §7).

* $\alpha:\ a<\tfrac12$ — the arc of $E_{AO}$ at $P_1$ is exposed
  (at $a=\tfrac12$: $E_{AO}$ tangent to $L_A$ at $P_1$).
* $\beta:\ b<\tfrac12$ — the arc of $E_{BO}$ at $P_3$ is exposed.
* $\varepsilon:\ \sigma<\tfrac12$ — the arcs $E_{BA}$, $E_{AB}$ exist
  (at $\sigma=\tfrac12$: tangency to $L_A$ at $P_2$, resp. $L_B$ at $P_2'$).
* $w_+:=a(1-b^2)-b(b^2-b+1)>0$ — the **$A$-side flank** (pieces around $P_2$) is exposed
  (threshold: $P_2\in E_{AO}$).
* $w_-:=b(1-a^2)-a(a^2-a+1)>0$ — the **$B$-side flank** (around $P_2'$) is exposed
  (threshold: $P_2'\in E_{BO}$). In bands I–III at least one of $w_\pm>0$.
* $\Lambda_B:\ \mathcal G(a,b)>0$ — the flush line $\lambda_B$ appears in the outer dip, where
  $$\mathcal G(a,b)=(1-b)^2\sigma^3+(b-1)(b-3)\sigma^2-b(b-1)\sigma-(b^2-3b+3).$$
  Mirror $\Lambda_A:\ \mathcal G(b,a)>0$ ($\lambda_A$ appears). Never both.
* $\mu:\ (3+a)R^2>3$ — the line $M_A$ appears in the mid dip (band III, $a>b$).
  Mirror: $(3+b)R^2>3$ for $M_B$ (band III, $b>a$).
* $\eta_-:\ \mathcal E(a,b)>0$ — in the regime $\varepsilon\wedge(w_->0)$, a segment of $L_B$ is
  exposed between $E_{AB}$ and $E_{BO}$; here
  $$\mathcal E(a,b)=-\bigl(4a^3b^3+10a^3b^2-3a^3-a^2b^5+10a^2b^3+5a^2b^2-15a^2b+3a^2
  +2ab^4-ab^3-12ab^2+3ab+b^5-3b^4-9b^3+3b^2\bigr),$$
  which is $-2^{-18}\mathrm{Res}_t\!\bigl(\mathcal D_B(t),\mathcal C_B(t)\bigr)$
  (three-curve concurrency $E_{AB}\cap E_{BO}\cap L_B$).
  Mirror $\eta_+:\ \mathcal E(b,a)>0$ ($L_A$ exposed between $E_{AO}$ and $E_{BA}$).

---

## 4. The cases

In every non-empty case the boundary is, counterclockwise,
$$\partial K=\bigl[ O\to B^*\ \text{on}\ Y=0 \bigr]\ \cup\ \Gamma\ \cup\
\bigl[ A^*\to O\ \text{on}\ \sqrt3X+Y=0 \bigr],$$
where the chain $\Gamma$ runs counterclockwise from $B^*$ to $A^*$ and is listed below with its
corners. Arcs of positive but possibly very small length are still listed; on the boundary between
two cases the disappearing arc has length zero and the two chains agree.

### Band I: $4\sigma^2\le3$

Below, "$A$-side block" means: $E_{BA}$ alone (entered at the corner $Q_1=E_{AO}\cap E_{BA}$,
left at $P_2$) if $\eta_+^c$, and $L_A$ **then** $E_{BA}$ (corners $G_1$, $P_2$, $Q_2=E_{BA}\cap
E_{BO}$) if $\eta_+$; likewise the "$B$-side block": $E_{AB}$ alone ($P_2'$, $Q_2'$) if
$\eta_-^c$, and $E_{AB}$ **then** $L_B$ (corners $Q_1'$, $P_2'$, $G_1'$) if $\eta_-$.

| case | region (within band I) | chain $\Gamma$ (from $B^*$ to $A^*$) |
|---|---|---|
| I.1 | $\varepsilon$, $w_+>0$, $w_->0$, $\eta_+^c$, $\eta_-^c$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{Q_1}E_{BA}\xrightarrow{P_2}E_{BO}\xrightarrow{Q_M}E_{AO}\xrightarrow{P_2'}E_{AB}\xrightarrow{Q_2'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.1a | $\varepsilon$, $w_+>0$, $w_->0$, $\eta_+$, $\eta_-^c$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BA}\xrightarrow{Q_2}E_{BO}\xrightarrow{Q_M}E_{AO}\xrightarrow{P_2'}E_{AB}\xrightarrow{Q_2'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.1b | $\varepsilon$, $w_+>0$, $w_->0$, $\eta_+^c$, $\eta_-$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{Q_1}E_{BA}\xrightarrow{P_2}E_{BO}\xrightarrow{Q_M}E_{AO}\xrightarrow{Q_1'}E_{AB}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.1c | $\varepsilon$, $w_+>0$, $w_->0$, $\eta_+$, $\eta_-$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BA}\xrightarrow{Q_2}E_{BO}\xrightarrow{Q_M}E_{AO}\xrightarrow{Q_1'}E_{AB}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.2 | $\varepsilon$, $w_+>0$, $w_-\le0$, $\eta_+^c$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{Q_1}E_{BA}\xrightarrow{P_2}E_{BO}\xrightarrow{P_3}c_B$ |
| I.2′ | mirror: $\varepsilon$, $w_+\le0$, $\eta_-^c$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{Q_1'}E_{AB}\xrightarrow{P_2'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.3 | $\varepsilon$, $w_+>0$, $w_-\le0$, $\eta_+$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BA}\xrightarrow{Q_2}E_{BO}\xrightarrow{P_3}c_B$ |
| I.3′ | mirror: $\varepsilon$, $w_+\le0$, $\eta_-$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{Q_1'}E_{AB}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.4 | $\varepsilon^c$, $\alpha$, $\beta$, $w_+>0$, $w_->0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{Q_M}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.5 | $\varepsilon^c$, $\alpha$, $\beta$, $w_+>0$, $w_-\le0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{P_3}c_B$ |
| I.5′ | mirror: $\varepsilon^c$, $\alpha$, $\beta$, $w_+\le0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| I.6 | $a\ge\tfrac12$ (forces $b<\tfrac12$, $w_+>0$, $w_-<0$ in band I) | $c_A\xrightarrow{P_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{P_3}c_B$ |
| I.6′ | mirror: $b\ge\tfrac12$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{P_3}c_B$ |

(The regions I.1a/I.1b/I.1c are thin slivers along the $\mathcal E=0$ curves near the tip
$\sigma=\tfrac12$ of the $\varepsilon$-region — e.g. $(0.24,0.255)\in$ I.1c — and make the
transition I.1 $\to$ I.4 across $\sigma=\tfrac12$ continuous: the arcs $E_{BA},E_{AB}$ shrink to
the tangency points $P_2,P_2'$ while the $L_A,L_B$ slivers are already present.)

### Band II: $4\sigma^2>3\ \ge\ 4R^2$

Take the band-I chain of the same side-predicates ($\varepsilon$ is impossible here since
$\sigma>\tfrac{\sqrt3}2>\tfrac12$) and splice the **outer dip** into the arc crossing the top: the
long arc is interrupted between the vertices $W_-$ and $W_+$ by
$$\text{dip}=\ s_A^{\mathrm{out}}\ \to\ \bigl[\lambda_B\ \text{if}\ \mathcal G(a,b)>0;\quad
\lambda_A\ \text{if}\ \mathcal G(b,a)>0;\quad\text{else nothing}\bigr]\ \to\ s_B^{\mathrm{out}},$$
with corners $W_-$ (onto $s_A^{\mathrm{out}}$), then either
$s_A^{\mathrm{out}}\cap s_B^{\mathrm{out}}$ or the two crossings with the flush line, then $W_+$.
Explicitly:

| case | region (within band II) | chain $\Gamma$ |
|---|---|---|
| II.1 | $a\ge\tfrac12$ (then $b<\tfrac12$, $w_-<0$) | $c_A\xrightarrow{P_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda]\to s_B^{\mathrm{out}}\xrightarrow{W_+}E_{BO}\xrightarrow{P_3}c_B$ |
| II.1′ | mirror: $b\ge\tfrac12$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda]\to s_B^{\mathrm{out}}\xrightarrow{W_+}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{P_3}c_B$ |
| II.2 | $\alpha$, $\beta$, $w_+>0$, $w_->0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda]\to s_B^{\mathrm{out}}\xrightarrow{W_+}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |
| II.3 | $\alpha$, $\beta$, $w_+>0$, $w_-\le0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{G_1}L_A\xrightarrow{P_2}E_{BO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda]\to s_B^{\mathrm{out}}\xrightarrow{W_+}E_{BO}\xrightarrow{P_3}c_B$ |
| II.3′ | mirror: $\alpha$, $\beta$, $w_+\le0$ | $c_A\xrightarrow{P_1}E_{AO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda]\to s_B^{\mathrm{out}}\xrightarrow{W_+}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{G_1'}E_{BO}\xrightarrow{P_3}c_B$ |

Each row has in principle three sub-cases by the bracket $[\lambda]$ ($\lambda_B$ / $\lambda_A$ /
absent), decided by the signs of $\mathcal G(a,b)$, $\mathcal G(b,a)$; in fact within band II the
flush line occurs only in the rows II.1 (then $\lambda_B$) and II.1′ (then $\lambda_A$): on the
regions of rows II.2, II.3, II.3′ both $\mathcal G$-signs are negative (region audit in the
verification). Never are both $\mathcal G$-signs positive.

### Band III: $4R^2>3$, $\sigma\le1$ — stated for $a>b$ (mirror for $b>a$)

Necessarily $a>\tfrac12>b$ here, so the band-II chain is that of II.1; additionally the **mid-gap
dip** is spliced into the initial arc of $c_A$ between $V=A+u(r_2-90^\circ)$ and
$\widetilde V=A+u(r_3-90^\circ)$:

$$\Gamma:\quad
c_A\bigl[B^*\!\to\!V\bigr]\to s_A^{\mathrm{mid}}\to\bigl[M_A\ \text{iff}\ (3+a)R^2>3\bigr]\to
s_B^{\mathrm{mid}}\to c_A\bigl[\widetilde V\!\to\!P_1\bigr]\xrightarrow{P_1}L_A\xrightarrow{P_2}
E_{BO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to\bigl[\lambda_B\ \text{iff}\ \mathcal G(a,b)>0\bigr]\to
s_B^{\mathrm{out}}\xrightarrow{W_+}E_{BO}\xrightarrow{P_3}c_B .$$

Sub-cases by the two brackets (the combination $\mu\wedge\mathcal G\le0$ is infeasible in band
III — region audit — so three sub-cases occur):

| case | $(3+a)R^2-3$ | $\mathcal G(a,b)$ | mid dip | outer dip |
|---|---|---|---|---|
| III.1 | $\le0$ | $\le0$ | $s_A^{\mathrm{mid}}\!\to\!s_B^{\mathrm{mid}}$ | $s_A^{\mathrm{out}}\!\to\!s_B^{\mathrm{out}}$ |
| III.2 | $\le0$ | $>0$ | $s_A^{\mathrm{mid}}\!\to\!s_B^{\mathrm{mid}}$ | $s_A^{\mathrm{out}}\!\to\!\lambda_B\!\to\!s_B^{\mathrm{out}}$ |
| III.4 | $>0$ | $>0$ | $s_A^{\mathrm{mid}}\!\to\!M_A\!\to\!s_B^{\mathrm{mid}}$ | $s_A^{\mathrm{out}}\!\to\!\lambda_B\!\to\!s_B^{\mathrm{out}}$ |

(III.1 — neither $M_A$ nor $\lambda_B$ — occupies only a thin sliver adjacent to the band II/III
interface $4R^2=3$, i.e. $b$ near $0$ with $a$ near $\tfrac{\sqrt3}2$; there both $s_B$ pieces are
present but short, shrinking to $0$ as $b\to0$. Sample: $(0.86,0.02)$. As $b\to0$ the whole mid dip
and the $s_B$ pieces vanish into the $a=0$-type degeneration.)

For $b>a$ the mirror places the mid dip inside the **final** $c_B$-arc (between
$\widetilde V'=B+u(\text{mirror of }r_3\ \text{data})$ and $V'$), with $M_B$ iff $(3+b)R^2>3$ and
$\lambda_A$ iff $\mathcal G(b,a)>0$; explicitly the mirror chain is
$$c_A\xrightarrow{P_1}E_{AO}\xrightarrow{W_-}s_A^{\mathrm{out}}\to[\lambda_A?]\to
s_B^{\mathrm{out}}\xrightarrow{W_+}E_{AO}\xrightarrow{P_2'}L_B\xrightarrow{P_3}
c_B\bigl[P_3\!\to\!\widetilde V'\bigr]\to s_A^{\mathrm{mid'}}\to[M_B?]\to s_B^{\mathrm{mid'}}\to
c_B\bigl[V'\!\to\!A^*\bigr],$$
where $s^{\mathrm{mid'}}_\bullet$ are the mirrored mid-gap side lines (through $A$, resp. through
$B$, of the triangles with vertex at $B$).

### Band IV: $\sigma>1$, $R^2\le1$ — one case

$$\Gamma:\quad c_A\bigl[B^*\to V\bigr]\ \to\ s_A^{\mathrm{IV}}\ \to\ s_B^{\mathrm{IV}}\ \to\
c_B\bigl[V'\to A^*\bigr],$$
with $V=A+u(\varphi_+-90^\circ)$, $V'=B+u(\varphi_-+90^\circ)$, and the middle corner
$s_A^{\mathrm{IV}}\cap s_B^{\mathrm{IV}}$. No other arcs occur. As $R\to1$: $B^*,V\to B$ and
$A^*,V'\to A$; the two segments converge to the base $[A,B]$, recovering the degenerate Case 0
boundary ($R=1$).

---

## 5. Degenerate parameters

* $a=b=0$: $K=\{X^2+Y^2\le1\}\cap C$; boundary: segment $[0,1]$ on $Y=0$, arc of $X^2+Y^2=1$ from
  $(1,0)$ to $u(120^\circ)$, segment back to $O$. (Limit of I.1: all quartics and circles collapse
  onto $X^2+Y^2=1$.)
* $a=0<b$ (mirror for $b=0$): all case formulas apply verbatim with $A=O$. Then $B^*=(1,0)=P_1$,
  the $c_A$-arc degenerates to a point, and $c_A,E_{AO}$ both become the circle $X^2+Y^2=1$;
  $E_{BA}\to E_{BO}$; $L_A,\lambda_A,M_A$ keep their equations with $a=0$.
* Case boundaries ($a=\tfrac12$, $b=\tfrac12$, $\sigma=\tfrac12$, $w_\pm=0$, $\mathcal E=0$,
  $\mathcal G=0$, $(3+\max)R^2=3$, and the band interfaces $4\sigma^2=3$, $4R^2=3$, $\sigma=1$,
  $R=1$): the adjacent chains coincide (the arc being created/destroyed has zero length), so the
  closed cases cover all of $\{a,b\ge0\}$ consistently.

---

## 6. Example instantiations (numerically verified)

| $(a,b)$ | case | chain |
|---|---|---|
| $(0.05,0.05)$ | I.1 | $c_A,E_{AO},E_{BA},E_{BO},E_{AO},E_{AB},E_{BO},c_B$ |
| $(0.25,0.15)$ | I.2 | $c_A,E_{AO},E_{BA},E_{BO},c_B$ |
| $(0.372,0.087)$ | I.3 | $c_A,E_{AO},L_A,E_{BA},E_{BO},c_B$ |
| $(0.135,0.277)$ | I.3′ | $c_A,E_{AO},E_{AB},L_B,E_{BO},c_B$ |
| $(0.35,0.35)$ | I.4 | $c_A,E_{AO},L_A,E_{BO},E_{AO},L_B,E_{BO},c_B$ |
| $(0.42,0.35)$ | I.5 | $c_A,E_{AO},L_A,E_{BO},c_B$ |
| $(0.6,0.2)$ | I.6 | $c_A,L_A,E_{BO},c_B$ |
| $(0.3,0.5)$ | I.6′ | $c_A,E_{AO},L_B,c_B$ |
| $(0.55,0.40)$ | II.1 (no $\lambda$) | $c_A,L_A,E_{BO},s_A^{\mathrm{out}},s_B^{\mathrm{out}},E_{BO},c_B$ |
| $(0.753,0.183)$ | II.1+$\lambda_B$ | $c_A,L_A,E_{BO},s_A^{\mathrm{out}},\lambda_B,s_B^{\mathrm{out}},E_{BO},c_B$ |
| $(0.45,0.45)$ | II.2 | $c_A,E_{AO},L_A,E_{BO},s_A^{\mathrm{out}},s_B^{\mathrm{out}},E_{AO},L_B,E_{BO},c_B$ |
| $(0.467,0.42)$ | II.3 | $c_A,E_{AO},L_A,E_{BO},s_A^{\mathrm{out}},s_B^{\mathrm{out}},E_{BO},c_B$ |
| $(0.24,0.255)$ | I.1c | $c_A,E_{AO},L_A,E_{BA},E_{BO},E_{AO},E_{AB},L_B,E_{BO},c_B$ |
| $(0.7,0.28)$ | III.2 | $c_A,s_A^{\mathrm{mid}},s_B^{\mathrm{mid}},c_A,L_A,E_{BO},s_A^{\mathrm{out}},\lambda_B,s_B^{\mathrm{out}},E_{BO},c_B$ |
| $(0.85,0.10)$ | III.4 | $c_A,s_A^{\mathrm{mid}},M_A,s_B^{\mathrm{mid}},c_A,L_A,E_{BO},s_A^{\mathrm{out}},\lambda_B,s_B^{\mathrm{out}},E_{BO},c_B$ |
| $(0.70,0.40)$ | IV | $c_A,s_A^{\mathrm{IV}},s_B^{\mathrm{IV}},c_B$ |

---

## 7. Verification

[`2009X_computation/verify_ab_set.py`](2009X_computation/verify_ab_set.py) checks for
representative samples inside every case region (and near every
threshold): (i) the boundary computed from first principles (the support-function criterion, at
machine precision) consists exactly of the claimed arcs in the claimed counterclockwise order;
(ii) at many directions $\theta$ the boundary point lies on the claimed curve to $\le10^{-8}$;
(iii) the programmed corner/tangency identities of §2--§3 hold (exactly, via
`sympy`).  These finite samples are evidence, not a global certificate. Results:
[`20094_ab_set_verification.md`](20094_ab_set_verification.md).
