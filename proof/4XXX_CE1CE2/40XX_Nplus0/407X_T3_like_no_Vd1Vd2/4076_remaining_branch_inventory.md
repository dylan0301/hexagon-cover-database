# Remaining Branch Inventory for $407X$

Status: Open inventory

This file records what remains after the progress files

- [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md),
- [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md),
- [`4074_L_Full_branch.md`](4074_L_Full_branch.md), and
- [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md).

The purpose of this file is to separate proved branch work from remaining obligations.  It does not claim that the remaining obligations are realizable; it records what still needs proof or exclusion.

## 1. Proved reductions and branch families

The following structural reductions are recorded in `4072`:

$$
T_2,T_4,T_5\text{ are Vd0},
$$

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

The boundary-loss framework is recorded in `4073`.  In that framework, the branch is closed once

$$
B(A_5,C_5)+B(A_1,C_1)<1
$$

is proved, with $B(A_1,C_1)$ replaced by the stricter neighboring-ray constrained map in the case where $T_1$ contributes to $r_0$.

The following boundary branch families are proved.

### Easy region

$$
A_1+A_5>1.
$$

### $(L,\mathrm{Full})$

Recorded in `4074`:

$$
(B_5,B_1)=(L,\mathrm{Full})\quad\Longrightarrow\quad B_5+B_1<1.
$$

### $\{L,T_-,T_+^{lo}\}^2$

Recorded in `4075`:

$$
(B_5,B_1)\in\{L,T_-,T_+^{lo}\}^2
\quad\Longrightarrow\quad
B_5+B_1<1.
$$

### Left-$T_-$ family

Recorded in `4075`, including non-overlap, middle-overlap, $S$-dominance, and the final right-high residual:

$$
B_5=T_-\quad\Longrightarrow\quad B_5+B_1<1
$$

for all right branches treated there.

## 2. Main remaining branch: $(L,T_+^{hi})$

The main open branch is

$$
(B_5,B_1)=(L,T_+^{hi}).
$$

Write

$$
z:=B_5=\ell(\gamma_5),\qquad A:=A_1,\qquad C_1=1-\eta.
$$

Write the right output as

$$
B_1=1-A-h.
$$

The target

$$
B_5+B_1<1
$$

is equivalent to

$$
h>z-A.
$$

The right $T_+$ equation is

$$
(1-A-h)(A+h-\eta)=h(2-h)(1-\eta)^2.
$$

Define

$$
G(x)=(1-A-x)(A+x-\eta)-x(2-x)(1-\eta)^2.
$$

Then $h$ is the positive root of $G$.  Therefore, in the nontrivial case $z>A$, the branch is closed if

$$
G(z-A)>0.
$$

Equivalently, the exact remaining semialgebraic target is

$$
\boxed{(1-z)(z-\eta)>(z-A)(2-z+A)(1-\eta)^2.}
$$

This inequality is false without the full $407X$ geometry.  For example,

$$
\eta={1\over4},\qquad z={2\over5},\qquad A={109-3\sqrt{241}\over200}
$$

violates it while satisfying the formal right high-sheet equation.  Therefore the remaining proof must use the direct $C$-triangle and T3-like $T_0$ geometry, not branch algebra alone.

A stronger statement suggested by numerical sampling is

$$
\boxed{(L,T_+^{hi})\quad\Longrightarrow\quad \ell(\gamma_5)<A_1.}
$$

This stronger statement would immediately close the branch.  It is not proved.

## 3. Direct semialgebraic system for $(L,T_+^{hi})$

A complete proof of the main remaining branch should use the following direct variables.

### $C$-triangle variables

$$
0<\lambda<1,\qquad \rho^2=1-\lambda+\lambda^2,\qquad \rho>0,
$$

$$
X\ge0,\qquad Y\ge0,\qquad X+(1-\lambda)Y<\rho(1-\rho).
$$

Set

$$
A_C=\lambda-Y,\qquad s={X+Y+1-\rho\over\lambda},\qquad t=1-\lambda+Y.
$$

The radial exits are

$$
\gamma_1=\min\left({Y\over\lambda},{\rho-X-Y\over1-\lambda}\right),
$$

$$
\gamma_5=\min\left({X\over1-\lambda},{\rho-X-Y\over\lambda}\right).
$$

For CE2,

$$
S={X+Y+1-\rho\over1-\lambda},\qquad T=X+\lambda.
$$

### T3-like $T_0$ variables

$$
R^2-DR+D^2=1,\qquad D>1,\qquad R>0,
$$

$$
\alpha+p_1={1\over D},\qquad q=1-p_1=\alpha+{D-1\over D}.
$$

The $r_1$ interval of $T_0$, measured from $V_1$ toward $O$, is

$$
c={Dq\over R},\qquad u=q+{1-R\over D}.
$$

Positive $r_1$ support is

$$
c<u,
$$

and no positive $r_5$ support is encoded by the corresponding strict non-overlap inequality from the side-through-$V_0$ model.

### Boundary input $A_1$

The $T_1$ boundary input is

$$
A_1=\begin{cases}
q,& p_1<s,\\
A_C,& s\le p_1<t,\\
q,& p_1\ge t.
\end{cases}
$$

### Radial input $C_1$

If $T_0$ misses the $T_C$ exit on $r_1$, then

$$
C_1=1-\gamma_1,\qquad \eta=\gamma_1.
$$

If $T_0$ hits the exit, then

$$
C_1=c,\qquad \eta=1-c,
$$

after clipping to the actual interval.

### Branch realization

The left Low branch requires

$$
z=\ell(\gamma_5)
$$

and realization of the Low candidate as the corrected maximum in $B(A_5,C_5)$.

The right $T_+^{hi}$ branch requires

$$
(1-A-h)(A+h-\eta)=h(2-h)(1-\eta)^2,
$$

$$
{1-A-h\over1-\eta}\ge{1\over2},
$$

and realization of this high-sheet candidate as the corrected maximum in $B(A_1,C_1)$.

The exact target is

$$
(1-z)(z-\eta)>(z-A)(2-z+A)(1-\eta)^2.
$$

## 4. Other possible branch-realization obligations

The following branch families have not been proved or excluded in this package:

$$
(\mathrm{Full},*),
$$

$$
(T_+^{hi},*),
$$

$$
(T_+^{lo},\mathrm{Full}),
$$

and

$$
(T_+^{lo},T_+^{hi}).
$$

Numerical searches have not consistently shown these as main obstructions in the current direct-geometry branch, but this file records them as unresolved unless a future branch-realization proof excludes them.

## 5. Recommended next proof target

The next proof file should target the main remaining branch:

$$
(L,T_+^{hi}).
$$

A strong target is

$$
\ell(\gamma_5)<A_1.
$$

A weaker exact target is

$$
(1-\ell(\gamma_5))(\ell(\gamma_5)-\eta)
>
(\ell(\gamma_5)-A_1)(2-\ell(\gamma_5)+A_1)(1-\eta)^2.
$$

Any proof must use the full semialgebraic system in Section 3; the inequality is false for formal branch variables alone.
