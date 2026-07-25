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

## Signed CE1/CE2 center normal form

The common signed variables are defined in `2109`.

- $R\in(0,1)$: normalized side-slope parameter; the historical CE1 variable
  is $\lambda=R$.
- $W=1-R$.
- $E=\sqrt{1-RW}=\sqrt{1-R+R^2}$; historical CE1 notation is $\rho=E$.
- $\eta=1-E$.
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

In the last display, the far endpoint is the ordinary variable $u$; the source
notation in mathematical prose is $u=R+\alpha$.

## Vertex-role local coordinates

- $a,b,c$: local vertex-triangle coordinates; in envelope files these are
  lower-bound demands.
- $A(T),B(T),C(T)$: actual maximal local reaches of a realizing vertex
  triangle when they must be distinguished from demands.
- $(a_i,b_i)$: actual selected incoming and outgoing boundary row data for
  the vertex role $T_i$ in the $N_+$ split.
- $c_i$: prescribed or actual radial coordinate, as declared in the local
  file.
- admissible set $\mathcal A$: feasible local triples $(a,b,c)$.
- $B_c(a)$: maximal outgoing demand $b$ for fixed incoming and radial demands.
- $F_c(a)=\min\{B_c(a),1-a\}$: safe capped outgoing map.
- $G_c(a)=1-F_c(a)$: propagated next-row incoming lower bound.
- $e(d)=\ell(1-d)$: low selected root for a high radial demand $1-d$.
- $\psi(x)=1-\sqrt{1-x+x^2}$: universal selected-$T_+$ increment.
- $\beta(q)=(-q+\sqrt{4-3q^2})/2$: adjacent-edge diameter-transfer curve.
- $\lambda_\circ(q)=1-\beta(q)$: complementary diameter tail.

## Historical and auxiliary notation

- $d_0,d_{60},\dots,d_{300}$: historical degree-indexed center ray exits.
- $1-d_{60i}$: historical complementary radial distance after $T_C$.
- $K_5$: archived May 25 five-point set $\{P_3,P_5,D_0,D_1,D_2\}$.
- $\Lambda(K)$: optimized side length of the smallest enclosing equilateral
  triangle for a finite set $K$.
- $f(a,b)$: local normalized maximum area inside $H$ for a vertex triangle
  forced to contain the corresponding row data.
- $G=1-f$: normalized local area loss in the area package; this is unrelated
  to the capped propagation map $G_c$ unless explicitly stated.
- $F$: historical coverage-coordinate zero-diagonal map.
- $g_c$: historical defect-coordinate admissible-set map.
- algorithm 1: failed unimodality route using local diagonal max-$c$ points.
- algorithm 2: diagonal-relaxation route using equality patterns among the
  nonsupercritical rows in the CE0 all-Vd0 $N_+=1$ branch.
- 걸거치는: crossing or straddling adjacent structure in the problematic
  T3-like way.
