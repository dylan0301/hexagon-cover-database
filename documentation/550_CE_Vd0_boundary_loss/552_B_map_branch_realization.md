# Corrected $B(a,c)$ Map and Branch Realization

Status: Definition with proven local branch-realization lemmas

This file records the corrected interpretation of the Vd0 admissible map $B(a,c)$ and the branch-pair notation used throughout `550_CE_Vd0_boundary_loss/`.  The main rule is that algebraic roots are only candidates.  The value $B(a,c)$ is the largest actually admissible $b$.

## 1. Correct definition

For fixed input boundary coordinate $a$ and radial requirement $c$, define

$$
B(a,c)=\max\{b\in[0,1-a]:(a,b,c)\in\mathcal A\}.
$$

Here $\mathcal A$ is the Vd0 admissible set on the $a+b\le1$ side.

Let

$$
\sigma=a+b,
$$

$$
m=\min(a,b),\qquad M=\max(a,b),
$$

and

$$
\Delta=\sigma^4-\sigma^2+ab.
$$

The relevant admissible alternatives are:

$$
\Delta\le0,\qquad c^4-c^2+mc-m^2\le0,
$$

or

$$
\Delta\ge0,\qquad (\sigma^2-1)c^2+Mc-M^2\le0.
$$

Therefore a branch formula for $b$ is valid only if the candidate $b$ satisfies all cell inequalities and is maximal among all admissible candidates.

## 2. The $c(a,b)$ warning

For $\sigma<1$ and $\Delta\ge0$, the radial condition is

$$
(\sigma^2-1)c^2+Mc-M^2\le0.
$$

This is a concave quadratic in $c$.  If

$$
d=\sqrt{4\sigma^2-3},
$$

then the two roots are

$$
c_-={2M\over 1+d},
\qquad
c_+={2M\over 1-d}
$$

when the second expression is finite.  Thus the feasible radial set can be

$$
[0,c_-]\cup[c_+,1]
$$

rather than a single interval $[0,c_-]$.

Consequently, $c(a,b)$ should not be treated as a single-valued smaller-root function.  The safe object is the feasible set

$$
C(a,b)=\{c:(a,b,c)\in\mathcal A\},
$$

and $B(a,c)$ is the maximum $b$ such that $c\in C(a,b)$.

## 3. Single-side branch labels

The branch names in this folder mean that the maximizing value $b=B(a,c)$ is realized on the specified frontier.  A label is not assigned merely because an algebraic equation has a root.

The branch label set used here is

$$
\mathfrak B=\{L,\mathrm{Full},T_-,T_+^{hi},T_+^{lo}\}.
$$

When the sheet of $T_+$ is irrelevant or not yet split, the shorthand $T_+$ means

$$
T_+=T_+^{hi}\cup T_+^{lo}.
$$

### Full

The Full branch is

$$
B(a,c)=1-a.
$$

It is valid only if

$$
c\le\max(a,1-a).
$$

This condition is essential.  Without it, fake Full branches appear.

### Low branch $L$

Set $c=1-\eta$.  The low radial branch is

$$
B(a,1-\eta)=\ell(\eta),
$$

where

$$
\ell(\eta)=\frac{(1-\eta)(1-\sqrt{4(1-\eta)^2-3})}{2}.
$$

It is the smaller positive root of

$$
b^2-(1-\eta)b-(1-\eta)^4+(1-\eta)^2=0.
$$

The low-branch candidate must also satisfy the cell condition

$$
(a+\ell)^4-(a+\ell)^2+a\ell\le0,
$$

and the order condition appropriate to the branch.

### $T_-$

The $T_-$ branch is the Cell $2$ branch with $b\le a$.  It is determined by

$$
((a+b)^2-1)c^2+ac-a^2=0.
$$

For a threshold $x$, define

$$
\Psi^-_{a,c}(x)=((a+x)^2-1)c^2+ac-a^2.
$$

Since

$$
{d\over dx}\Psi^-_{a,c}(x)=2(a+x)c^2>0,
$$

we have the exact root-order test

$$
B_{T_-}(a,c)<x\quad\Longleftrightarrow\quad \Psi^-_{a,c}(x)>0.
$$

### $T_+$

The $T_+$ branch is the Cell $2$ branch with $b\ge a$.  It is determined by

$$
((a+b)^2-1)c^2+bc-b^2=0.
$$

Let

$$
\mu=a+b,\qquad \beta={b\over c}.
$$

Then

$$
\beta^2-\beta+1-\mu^2=0.
$$

Thus

$$
\beta_\pm(\mu)=\frac{1\pm\sqrt{4\mu^2-3}}2.
$$

This splits $T_+$ into two sheets:

$$
T_+^{hi}:\quad b=c\beta_+(\mu),
$$

and

$$
T_+^{lo}:\quad b=c\beta_-(\mu).
$$

The lower sheet satisfies

$$
B_{T_+^{lo}}(a,c)\le {c\over2}.
$$

## 4. Branch-pair notation

For the active $C$-interval $[s,t]\subset e_{0,1}$, set

$$
u=1-t.
$$

The two adjacent maximal V-values are

$$
B_5:=B(s,1-\gamma_5),
$$

and

$$
B_1:=B(u,1-\gamma_1).
$$

Here $B_5$ is the $V_5$-side, or first, contribution.  It uses input boundary length $s$ and radial requirement $1-\gamma_5$.  The term $B_1$ is the $V_1$-side, or second, contribution.  It uses input boundary length $u=1-t$ and radial requirement $1-\gamma_1$.

A branch pair

$$
(X,Y),\qquad X,Y\in\mathfrak B,
$$

means the following precise statement:

$$
B_5=B(s,1-\gamma_5)\text{ is realized on branch }X,
$$

and

$$
B_1=B(u,1-\gamma_1)\text{ is realized on branch }Y.
$$

The first coordinate is always the $B_5$ branch.  The second coordinate is always the $B_1$ branch.

For example,

$$
(L,\mathrm{Full})
$$

means

$$
B_5=\ell(\gamma_5)
$$

with the Low branch realization conditions for input $s$, and

$$
B_1=1-u
$$

with the Full branch condition for input $u$.  Therefore, on this branch pair,

$$
F=B_5+B_1=\ell(\gamma_5)+1-u.
$$

Similarly,

$$
(T_+^{hi},T_-)
$$

means

$$
B_5=B_{T_+^{hi}}(s,1-\gamma_5),
$$

and

$$
B_1=B_{T_-}(u,1-\gamma_1).
$$

Branch-pair notation is therefore notation for a pair of realized maxima.  It is not notation for a pair of formal algebraic roots.

## 5. $D_1$ is not an independent branch

The separator

$$
D_1:\quad \Delta=(a+b)^4-(a+b)^2+ab=0
$$

is not an independent maximal branch.  Let $v=a+b$.  On $D_1$,

$$
ab=v^2-v^4,
$$

so $v\ge\sqrt3/2$.

If a point on $D_1$ is feasible in Cell $1$, then it is also feasible in Cell $2$ at the same point.  Moreover,

$$
{\partial\Delta\over\partial b}=4(a+b)^3-2(a+b)+a.
$$

At $v=a+b\ge\sqrt3/2$,

$$
4v^3-2v+a>0.
$$

Thus increasing $b$ moves into $\Delta>0$.  If the Cell $2$ radial inequality is strict, maximality fails.  If it is tight, the point belongs to a genuine $T_-$ or $T_+$ transition branch.

Therefore $D_1$ is only a switching interface, not a separate maximal $B$-branch.

## 6. Full-Full impossibility

On the main $r>1$ C-branch, $(\mathrm{Full},\mathrm{Full})$ is impossible.

If $B_1=\mathrm{Full}$, then

$$
u\le{1\over r+1}.
$$

If $B_5=\mathrm{Full}$, then $s\le1/2$ and

$$
\gamma_5\ge s.
$$

Using

$$
\gamma_5=u-\delta-{w\over r-1},
\qquad s=1-u-w,
$$

these conditions imply

$$
2u+w\left(1-{1\over r-1}\right)\ge1+\delta.
$$

For $0<r-1<1$, the left side is at most $2u\le2/(r+1)<1$, contradiction.  For $r-1\ge1$, using $\gamma_5\ge0$ gives $w\le(r-1)(u-\delta)$, hence the left side is less than $1$, again a contradiction.

Thus the branch $(\mathrm{Full},\mathrm{Full})$ is fake and does not occur after exact Full conditions are enforced.
