# Canonical Notation Dictionary

Status: Reference

This file is the public notation contract for the active proof package.  The
paper and the numbered proof sources use the same symbols.  The established
geometric terms are **C triangle** and **V triangle**; those terms are not
expanded to “center triangle” or “vertex triangle” in the proof package.

## 1. Distinguished triangles

- $T_C$ is the closed C triangle containing the center $O$.
- $T_i$ is the closed $V_i$ triangle containing the hexagon vertex $V_i$.
- CE0, CE1, and CE2 are the C-triangle boundary-trace types.
- Vd0, Vd1, Vd2, and T3-like are the V-triangle types.

## 2. Actual reaches and selected lower bounds

For an actual $V_i$ triangle $T_i$,

$$
(A_i,B_i,C_i)
$$

denote its maximal backward-boundary, forward-boundary, and own-radial
reaches.  Supercriticality and exact trace length always concern these actual
reaches:

$$
T_i\text{ is supercritical}
\quad\Longleftrightarrow\quad
A_i+B_i>1,
$$

$$
L_{\partial H}(T_i)=A_i+B_i.
$$

Lowercase indexed symbols are selected lower bounds only:

$$
0\le a_i\le A_i,
\qquad
0\le b_i\le B_i,
\qquad
0\le c_i\le C_i.
$$

Unindexed letters such as $a,b,c$ may be used as bound variables inside a
local theorem when that theorem explicitly declares their meaning.  Indexed
lowercase reaches are never used for actual maxima.

## 3. Counts

$$
N_+=\#\{i:A_i+B_i>1\},
$$

$$
N_{\rm sp}
=\#\{i:T_i\text{ is Vd1, Vd2, or T3-like}\},
$$

and

$$
N_{\rm gap}
=\#\{\text{positive C-triangle boundary traces containing a V-uncovered set}\}.
$$

The skeleton-length route is stated directly as

$$
N_++N_{\rm sp}\ge3
\quad\Longrightarrow\quad
\text{skeleton noncoverage}.
$$

No additional “short-role” count is part of the canonical interface.

## 4. Local admissible set and propagation

For selected lower bounds $(a,b,c)$,

$$
\mathcal A
=\{(a,b,c)\in[0,1]^3:K(a,b,c)\text{ fits in a closed unit equilateral triangle}\}.
$$

The raw forward envelope is

$$
M_c(a)=\max\{b:(a,b,c)\in\mathcal A\}.
$$

Its zero-radial specialization is

$$
M_0(a)=\frac{-a+\sqrt{4-3a^2}}2.
$$

The argument-free symbol $M_0$ denotes the radial midpoint.  The function
notation $M_0(a)$ denotes this zero-radial envelope.

The exact nonsupercritical cap and center-free propagation map are

$$
\overline M_c(a)=
\begin{cases}
1-a,&0\le c\le1/2,\\
M_c(a),&1/2<c\le1,
\end{cases}
\qquad
\Phi_c(a)=1-\overline M_c(a).
$$

Thus an actual nonsupercritical V triangle with $A\ge a$ and $C\ge c$
satisfies

$$
B\le\overline M_c(a),
$$

and a center-free following edge gives

$$
A_{\rm next}\ge\Phi_c(a).
$$

For a C-triangle trace interval $J$, the generalized handoff is written
without a second map family:

$$
A_{\rm next}\ge\mathcal R_J(M_c(a))
$$

in the raw case and

$$
A_{\rm next}\ge\mathcal R_J(\overline M_c(a))
$$

in the nonsupercritical case.

For $0\le c<1/2$, the strict-supercritical forward supremum is

$$
M_c^{\rm sup}
=\sup\{M_c(a):M_c(a)>1-a\}
=\frac{c+\sqrt{c^2-8c+4}}2.
$$

## 5. High-radial branches

The exact branch labels are

$$
\mathrm{Lin},\qquad
\mathrm{Const},\qquad
Q_-,\qquad
Q_+.
$$

The admissible-set cell names $\mathcal A_L$, $\mathcal A_T$, and
$\mathcal A_S$ are different objects and are retained.

## 6. Signed C-triangle variables

The signed normal form uses

$$
0<R<1,
\qquad W=1-R,
\qquad E=\sqrt{1-RW},
\qquad \eta=1-E,
$$

$$
P=E(1-E),
\qquad
\Delta_R=P-\alpha-W\delta,
\qquad
\Delta_L=P-R\alpha-\delta.
$$

These symbols are reserved for the C-triangle normal form.  A V-triangle
radial lower bound is written $c_i$, not $\delta$.

## 7. Legacy crosswalk

The authenticated 407X exact-cell package and historical files retain some
older symbols because changing them would invalidate recorded Git-blob
provenance.  In those files only,

$$
g_c(x)=M_c(1-x),
\qquad
B_c=M_c,
\qquad
F_c=\overline M_c,
\qquad
G_c=\Phi_c,
$$

and

$$
\mathrm{Full}=\mathrm{Lin},
\qquad
L=\mathrm{Const},
\qquad
T_-=Q_-,
\qquad
T_+=Q_+.
$$

These are compatibility aliases, not a second public notation layer.
