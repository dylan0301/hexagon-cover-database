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
- $T_C$: center triangle.
- $T_i$: vertex triangle at $V_i$.

## Role classes

- CE0/CE1/CE2: exhaustive preferred center-triangle perimeter-edge types.
- Ce0/Ce1/Ce2: historical aliases.
- Vd0/Vd1/Vd2/T3-like: exhaustive original vertex-role types.
- supercritical V triangle: a V triangle whose actual reaches satisfy $A_i+B_i>1$.
- $N_+$:
  $$
  \left\lvert\left\{i:A_i+B_i>1\right\}\right\rvert,
  $$
  the number of actual supercritical V triangles.
- short role: in `2530`, a vertex role that is supercritical or has
  positive-length support on an adjacent radial arm.
- $\mathrm{gr}$: active-gap rank, the number of positive center traces
  containing a V-gap. One has $\mathrm{gr}\in\{0,1,2\}$ and
  $\mathrm{gr}\le1$ in CE1. Bare $g$ is reserved for transfer maps.

## Universal enclosure calculus

- $R_{120}$: rotation through $2\pi/3$ when a distinction from the signed
  center parameter $R$ is needed.
- $h_K(n)=\max_{x\in K}\langle x,n\rangle$: support function.
- $\Lambda(K)$: least side length of a closed equilateral triangle containing
  $K$:
  $$
  \Lambda(K)=\frac{2}{\sqrt3}
  \min_{\lVert n\rVert=1}
  \sum_{j=0}^2h_K(R_{120}^jn).
  $$
- $\omega(x)=\sqrt{1-x+x^2}$ and
  $\sigma(x)=1-\omega(x)$: the universal equilateral radical and its concave
  deficit.

## The canonical $g$-family

The paper uses one transfer alphabet. Hats impose the nonsupercritical cap,
and $\vee$ changes from boundary-defect coordinates to complementary
incoming-reach coordinates.

- $\mathcal A$: the exact local admissible set of demand triples $(a,b,c)$.
- $x=1-a$: incoming boundary defect corresponding to incoming reach $a$.
- $g_c(x)$:
  $$
  g_c(x)
  =
  \max\left\{
  y:(1-x,y,c)\in\mathcal A
  \right\}.
  $$
  This is the historical raw defect-coordinate map. Equivalently,
  $g_c(x)=B_c(1-x)$.
- $\widehat g_c(x)=\min\{g_c(x),x\}$: nonsupercritical capped defect map.
- $f^\vee(a)=1-f(1-a)$: complement dual of any map $f$.
- $g_c^\vee$: raw next-incoming reach lower transfer, valid for every V triangle.
- $\widehat g_c^\vee$: capped next-incoming reach lower transfer for a
  nonsupercritical V triangle. It is extensive:
  $$
  \widehat g_c^\vee(a)\ge a.
  $$
- $\mathcal R_J(p)$: far-side residual demand after an initial trace $[0,p]$
  and a center interval $J$.
- $g_{c,J}^\vee(a)=\mathcal R_J(g_c(1-a))$: raw center-assisted reach transfer.
- $\widehat g_{c,J}^\vee(a)=\mathcal R_J(\widehat g_c(1-a))$: capped
  center-assisted reach transfer.
- $g_c^{\rm sc}$:
  $$
  g_c^{\rm sc}
  =
  \sup_{\{x:g_c(x)>x\}}g_c(x)
  =
  \frac{c+\sqrt{c^2-8c+4}}2
  \quad(0\le c<1/2).
  $$
  This single scalar is the free strict-supercritical outgoing envelope.
  Every such V triangle has outgoing reach $<g_c^{\rm sc}$.  If the outgoing edge is
  center-free, the following incoming reach is $>1-g_c^{\rm sc}$.
- $[\Phi_1\mid\cdots\mid\Phi_r](x)$:
  $(\Phi_r\circ\cdots\circ\Phi_1)(x)$, with maps listed in geometric V-triangle order.
- $\mathrm I(x)=x$: identity lower relaxation.
- $\widehat g_{1-d}^{\vee,\lambda}(x)=x+\lambda(x-d)$: certified affine
  selected-$T_+$ lower relaxation on its stated arc.
- $\widehat g_{1-d}^{\vee,\rm th}$: low-root threshold lower relaxation of
  $\widehat g_{1-d}^\vee$.

At zero radial demand,

$$
g_0(x)>x\quad(0<x<1),
\qquad
\widehat g_0(x)=x,
$$

and hence

$$
g_0^\vee(a)<a,
\qquad
\widehat g_0^\vee(a)=a.
$$

This distinguishes the historical raw $g_0$ from its hatted
nonsupercritical cap.

### Technical aliases

The exact contact-cell files retain three incoming-reach aliases when they
shorten formulas:

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a).
$$

The older free-envelope aliases are

$$
B_{\rm sc}(c)=g_c^{\rm sc},
\qquad
A_{\rm sc}(c)=1-g_c^{\rm sc}.
$$

Reader-facing files should prefer the canonical $g$-family.

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
  positive.
- $\Delta_L=P-R\alpha-\delta$: companion-trace surplus.
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
  d_0^C=E-\alpha-\delta,\quad
  d_1^C=\frac{\delta}{R},\quad
  d_2^C=\delta,
  $$
  $$
  d_3^C=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},\quad
  d_4^C=\alpha,\quad
  d_5^C=\frac{\alpha}{W}.
  $$
- center-complement radial demand: $c_i^C=1-d_i^C$.
- local CE1 affine-slot scalar:
  $$
  m_3=d_3^C,
  $$
  distinct from the global non-Vd0 role count $m$.

Legacy CE1 variables are

$$
\lambda=R,\qquad
s=\frac{k}{R},\qquad
t=W+\delta,\qquad
C_0=\alpha,\qquad
C_2=\delta.
$$

Legacy CE2 variables are

$$
x=\frac{k}{W},\qquad
u=R+\alpha,\qquad
y=\frac{k}{R},\qquad
v=W+\delta.
$$

The far endpoint historically denoted by $u$ is written $\nu$ in shared
high-sheet calculations when confusion with a local coordinate is possible.

## Vertex-role local coordinates

- $a,b,c$: local lower-bound demands; a closed $V_i$-triangle $T$ realizes
  them when $(a,b,c)\le(A(T),B(T),C(T))$ coordinatewise. For an open role,
  the same weak statement applies to its closure.
- $A(T),B(T),C(T)$: actual maximal reaches of a $V_i$-triangle $T$ toward
  $V_{i-1}$, $V_{i+1}$, and $O$, respectively. Equivalently, these are the
  incoming, outgoing, and own-radial reaches. They are unchanged when an
  original open role is replaced by its closure.
- $(A_i,B_i,C_i)=(A(T_i),B(T_i),C(T_i))$: compact indexed aliases for the
  actual maximal V triangle reaches.
- $(a_i,b_i,c_i)$: selected lower-bound demands in the manuscript.
- $e(d)=\ell(1-d)$: low selected root for radial demand $1-d$.
- $\sigma(x)=1-\sqrt{1-x+x^2}$: universal selected-$T_+$ increment; older
  files write $\psi(x)$.
- $\beta(q)=(-q+\sqrt{4-3q^2})/2$: adjacent-edge diameter-transfer curve.

## Historical and auxiliary notation

- $d_0,d_{60},\dots,d_{300}$: historical degree-indexed center exits.
- $1-d_{60i}$: historical complementary radial distance after $T_C$.
- $K_5$: archived May 25 five-point set.
- $f(a,b)$: normalized maximal retained area for a forced vertex triangle.
- $\mathcal L_{\rm area}=1-f$: normalized local area loss.
- $F$: historical coverage-coordinate zero-diagonal map, unrelated to the
  technical alias $F_c$ above.
- algorithm 1: failed unimodality route.
- algorithm 2: diagonal-relaxation route in the CE0 all-Vd0 branch.
- 걸거치는: crossing or straddling adjacent structure in the problematic
  T3-like way.
