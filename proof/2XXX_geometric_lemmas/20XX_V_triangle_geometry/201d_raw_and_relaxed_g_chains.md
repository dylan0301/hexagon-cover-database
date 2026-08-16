# Canonical Forward-Cap and Propagation Chains

Status: Proven

This note fixes the public Strategy 2 notation.  It uses selected reach lower
bounds and retains the established terms V triangle and C triangle.

## 1. Raw envelope and nonsupercritical cap

Let $\mathcal A\subseteq[0,1]^3$ be the exact local admissible set from
[`2004`](2004_admissible_set.md).  Define

$$
M_c(a)=\max\{b:(a,b,c)\in\mathcal A\}.
$$

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

The midpoint theorem gives

$$
c\ge\frac12\Longrightarrow M_c(a)\le1-a,
\qquad
M_{1/2}(a)=1-a.
$$

Hence $\overline M_c(a)=\min\{M_c(a),1-a\}$ and every $\Phi_c$ is
nondecreasing and extensive.

## 2. Actual V-triangle propagation

Let an actual V triangle have maximal reaches $(A,B,C)$ and suppose

$$
A\ge a,
\qquad
C\ge c.
$$

Then

$$
B\le M_c(a).
$$

If it is nonsupercritical, then

$$
B\le\overline M_c(a).
$$

On a center-free next edge, coverage gives

$$
A_{\rm next}\ge\Phi_c(a)\ge a.
$$

At $c=0$ the raw envelope satisfies $M_0(a)>1-a$ for $0<a<1$; the
nonsupercritical handoff therefore uses the cap, not the raw envelope.

## 3. C-triangle intervals

Let $\mathcal R_J$ be the residual operator of
[`2019`](2019_interval_component_and_path_budget.md), where $J$ is empty or a
closed C-triangle interval.  The raw and nonsupercritical handoffs are

$$
A_{\rm next}\ge\mathcal R_J(M_c(a))
$$

and

$$
A_{\rm next}\ge\mathcal R_J(\overline M_c(a)),
$$

respectively.  No additional center-assisted map symbol is needed.

## 4. Strict-supercritical source

For $0\le c<1/2$, define

$$
M_c^{\rm sup}
=\sup\{M_c(a):M_c(a)>1-a\}
=\frac{c+\sqrt{c^2-8c+4}}2.
$$

The supremum is not attained.  Every actual strict-supercritical V triangle
with radial reach at least $c$ satisfies

$$
B<M_c^{\rm sup},
$$

and a center-free following edge satisfies

$$
A_{\rm next}>1-M_c^{\rm sup}.
$$

## 5. Composition and relaxations

For maps listed in geometric V-triangle order, write

$$
[\Psi_1\mid\cdots\mid\Psi_r](x)
=(\Psi_r\circ\cdots\circ\Psi_1)(x).
$$

The leftmost slot acts first.  If actual lower bounds satisfy

$$
x_j\ge\Psi_j(x_{j-1})
$$

and nondecreasing relaxations satisfy $\underline\Psi_j\le\Psi_j$, then

$$
x_r\ge
[\underline\Psi_1\mid\cdots\mid\underline\Psi_r](x_0).
$$

This is the usual induction using monotonicity.

On a selected $Q_+$ arc with $c=1-d>1/2$, any proved affine chord is written

$$
\Phi_{1-d}^{\lambda}(x)=x+\lambda(x-d)
\le\Phi_{1-d}(x).
$$

For $0<d<1-\sqrt3/2$, let $e(d)$ be the low-root threshold from
[`2012`](2012_high_radial_low_root_bounds.md).  The threshold relaxation is

$$
\Phi_{1-d}^{\rm th}(x)=
\begin{cases}
x,&x\le e(d),\\
1-e(d),&x>e(d),
\end{cases}
\qquad
\Phi_{1-d}^{\rm th}\le\Phi_{1-d}.
$$

## 6. Six-position register

For each boundary edge, let $J_i^C$ be its empty or closed C-triangle trace.
The $i$th V-triangle position uses

$$
a\longmapsto\mathcal R_{J_i^C}(M_{c_i}(a))
$$

in the raw case, and

$$
a\longmapsto\mathcal R_{J_i^C}(\overline M_{c_i}(a))
$$

in the nonsupercritical case.  Identity relaxation is licensed only after the
edge is proved C-triangle-free and the current V triangle is proved
nonsupercritical.

For the $N_+=1$ all-Vd0 one-gap branch, the exact five-V-triangle subchain is

$$
[\Phi_{c_1}\mid\Phi_{c_2}\mid\Phi_{c_3}\mid\Phi_{c_4}\mid\Phi_{c_5}],
$$

followed by the independent terminal cap for the unique supercritical V
triangle.

## 7. Provenance-preserving aliases

The authenticated 407X files retain the older symbols recorded in
[`0910_notation_dictionary.md`](../../09XX_appendices/0910_notation_dictionary.md).
Those aliases are confined to the provenance-bound exact-cell layer and do not
create a second public transfer family.
