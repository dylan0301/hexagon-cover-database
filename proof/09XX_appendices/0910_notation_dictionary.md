# Glossary And Notation Dictionary

Status: Reference

## Global geometry

- $H$: side-$1$ regular hexagon.
- $H_L$: side-$L$ regular hexagon.
- $O$: center of the hexagon. Some older notes use $C$.
- $V_i$: hexagon vertices.
- $e_{i,i+1}$: boundary edge.
- $r_i$: radial segment $[O,V_i]$.
- $M_i$: midpoint $V_i/2$.
- $S$: full skeleton.
- $S_{1/2}$: half-skeleton.
- $T_C$: center triangle, not to be confused with the center point.
- $T_i$: vertex triangle at $V_i$.

## Role classes

- CE0/CE1/CE2: exhaustive preferred names for center-triangle
  perimeter-edge types.
- Ce0/Ce1/Ce2: historical aliases.
- Vd0/Vd1/Vd2/T3-like: exhaustive vertex-triangle types for original vertex
  roles.
- supercritical row: a row with $a_i+b_i>1$.
- $N_+$:
  $$
  \left\lvert\left\{i:a_i+b_i>1\right\}\right\rvert,
  $$
  the number of supercritical rows.
- short role: in `2530`, a vertex role that is supercritical or has
  positive-length support on an adjacent radial arm.
- $\mathrm{gr}$: active-gap rank, the number of positive center traces
  containing a V-gap.  One has $\mathrm{gr}\in\{0,1,2\}$ and
  $\mathrm{gr}\le1$ in CE1.  The symbol replaces the older use of $g$, which
  is now reserved for the raw transfer maps $g_c$.

## Universal enclosure and transfer calculus

- $R_{120}$: rotation through $2\pi/3$ when a distinction from the signed
  center parameter $R$ is needed.
- $h_K(n)=\max_{x\in K}\langle x,n\rangle$: support function.
- $\Lambda(K)$: least side length of a closed equilateral triangle containing
  $K$; equivalently
  $$
  \Lambda(K)=\frac{2}{\sqrt3}
  \min_{\lVert n\rVert=1}
  \sum_{j=0}^2h_K(R_{120}^jn).
  $$
- $\omega(x)=\sqrt{1-x+x^2}$ and
  $\sigma(x)=1-\omega(x)$: the universal equilateral radical and its concave
  deficit.
- $\mathcal R_J(p)$: far-side residual boundary demand after an initial trace
  $[0,p]$ and a center interval $J$.
- $g_c(a)=1-B_c(a)$: raw no-center transfer, valid for every row.
- $G_c(a)=1-F_c(a)=\max\{g_c(a),a\}$: capped transfer obtained by adjoining
  the identity lower bound.
- $\mathfrak g_{c,J}(a)=\mathcal R_J(B_c(a))$: raw center-assisted transfer.
- $\mathcal G_{c,J}(a)=\mathcal R_J(F_c(a))$: capped center-assisted transfer;
  $\mathfrak g_{c,\varnothing}=g_c$ and
  $\mathcal G_{c,\varnothing}=G_c$.
- $\mathsf T_{U,J}(a)=\mathcal R_J(U(a))$: transfer induced by any proved
  outgoing upper envelope $U$.
- $[\Phi_1\mid\cdots\mid\Phi_r](x)$:
  $(\Phi_r\circ\cdots\circ\Phi_1)(x)$, with the maps listed in row order.
- $\mathrm I(x)=x$: identity relaxation.
- $\Theta_d$: low-root threshold relaxation of $G_{1-d}$.
- $\mathsf L_{d,\lambda}(x)=x+\lambda(x-d)$: an affine selected-$T_+$ chord
  relaxation on a domain where the corresponding chord estimate is proved.
- $B_{\rm sc}(c)$ and $A_{\rm sc}(c)=1-B_{\rm sc}(c)$: free
  strict-supercritical outgoing and following-demand envelopes.  Equivalently,
  $A_{\rm sc}(c)$ is the infimum of $g_c$ over the region $g_c(a)<a$.

## Signed CE1/CE2 center normal form

The common signed variables are defined in `2109`.

- $R\in(0,1)$: normalized side-slope parameter; the historical CE1 variable
  is $\lambda=R$.
- $W=1-R$.
- $E=\sqrt{1-RW}=\sqrt{1-R+R^2}=\omega(R)$; historical CE1 notation is
  $\rho=E$.
- $\eta=1-E=\sigma(R)$.
- $P=E(1-E)$, with $RW=\eta+P$.
- $\alpha=F_0(O)$ and $\delta=F_2(O)$: the two nontrivial center slacks.
- $k=\eta+\alpha+\delta$.
- $\Delta_R=P-\alpha-W\delta$: normalized active-trace surplus; always
  positive in the signed normalization.
- $\Delta_L=P-R\alpha-\delta$: signed companion-trace surplus.
- CE1 sign: $\Delta_L\le0$.
- CE2 sign: $\Delta_L>0$.
- normalized right trace:
  $$
  \left[\frac{k}{R},W+\delta\right].
  $$
- possible companion trace:
  $$
  \left[\frac{k}{W},R+\alpha\right].
  $$
- common center exits:
  $$
  d_0^C=E-\alpha-\delta,
  \quad
  d_1^C=\frac{\delta}{R},
  \quad
  d_2^C=\delta,
  $$
  $$
  d_3^C=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
  \quad
  d_4^C=\alpha,
  \quad
  d_5^C=\frac{\alpha}{W}.
  $$
- complementary row demand: $c_i=1-d_i^C$.

Legacy CE1 variables are

$$
\lambda=R,
\qquad
s=\frac{k}{R},
\qquad
t=W+\delta,
\qquad
C_0=\alpha,
\qquad
C_2=\delta.
$$

Legacy CE2 variables are

$$
x=\frac{k}{W},
\qquad
u=R+\alpha,
\qquad
y=\frac{k}{R},
\qquad
v=W+\delta.
$$

The far endpoint historically denoted by $u$ is written $\nu$ in shared
high-sheet calculations when confusion with a local coordinate is possible.

## Vertex-role local coordinates

- $a,b,c$: local vertex-triangle coordinates; in envelope files these are
  lower-bound demands.
- $A(T),B(T),C(T)$: actual maximal local reaches of a realizing vertex
  triangle when they must be distinguished from demands.
- $(a_i,b_i)$: actual selected incoming and outgoing boundary row data for
  the vertex role $T_i$ in the proof corpus.
- $c_i$: prescribed or actual radial coordinate, as declared in the local
  file.
- admissible set $\mathcal A$: feasible local triples $(a,b,c)$; equivalently
  $\Lambda(K(a,b,c))\le1$.
- $B_c(a)$: maximal outgoing demand $b$ for fixed incoming and radial demands.
- $F_c(a)=\min\{B_c(a),1-a\}$: safe nonsupercritical outgoing cap.
- $g_c(a)=1-B_c(a)$ and $G_c(a)=1-F_c(a)$: raw and capped propagated
  next-row incoming lower bounds when no center interval intervenes.
- $e(d)=\ell(1-d)$: low selected root for a high radial demand $1-d$.
- $\sigma(x)=1-\sqrt{1-x+x^2}$: universal selected-$T_+$ increment; older
  files write this function as $\psi(x)$.
- $\beta(q)=(-q+\sqrt{4-3q^2})/2$: adjacent-edge diameter-transfer curve.
- $\lambda_\circ(q)=1-\beta(q)$: complementary diameter tail.

## Historical and auxiliary notation

- $d_0,d_{60},\dots,d_{300}$: historical degree-indexed center ray exits.
- $1-d_{60i}$: historical complementary radial distance after $T_C$.
- $K_5$: archived May 25 five-point set $\{P_3,P_5,D_0,D_1,D_2\}$.
- $f(a,b)$: local normalized maximum area inside $H$ for a vertex triangle
  forced to contain the corresponding row data.
- $\mathcal L_{\mathrm{area}}=1-f$: normalized local area loss.  Older files
  use $G=1-f$; that symbol is unrelated to the capped propagation map $G_c$.
- $F$: historical coverage-coordinate zero-diagonal map.
- $g_c$: historically used for the defect-coordinate admissible-set map and
  now retained as the canonical raw transfer $1-B_c$.
- algorithm 1: failed unimodality route using local diagonal max-$c$ points.
- algorithm 2: diagonal-relaxation route using equality patterns among the
  nonsupercritical rows in the CE0 all-Vd0 $N_+=1$ branch.
- 걸거치는: crossing or straddling adjacent structure in the problematic
  T3-like way.
