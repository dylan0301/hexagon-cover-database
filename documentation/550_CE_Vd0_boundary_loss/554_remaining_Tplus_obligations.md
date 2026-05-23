# Remaining $T_+$ Obligations

Status: Lemma target with failed approaches recorded

This file records the remaining unsolved pieces after the branch lemmas in `553_proven_branch_lemmas.md`.

## 1. Solved $T_+$ branches

The following branches are proved or eliminated:

$$
(L,T_+),
$$

$$
(T_+,\mathrm{Full})\text{ is impossible},
$$

$$
(T_+^{hi},L),
$$

$$
(T_+^{lo},L),
$$

$$
(T_+^{hi},T_-),
$$

and

$$
(T_+^{hi},T_+^{hi})\text{ is impossible}.
$$

Therefore only lower-sheet left $T_+$ cases remain.

## 2. Remaining branches

The remaining branches are:

$$
(T_+^{lo},T_-),
$$

$$
(T_+^{lo},T_+^{hi}),
$$

and

$$
(T_+^{lo},T_+^{lo}).
$$

These are numerically non-tight, but no proof is recorded here.

## 3. Coupled-loss formulation for $T_+T_+$

For any $T_+T_+$ branch, write

$$
B_5=1-s-d_5,
\qquad
B_1=1-u-d_1.
$$

Then

$$
F=B_5+B_1=1+w-d_1-d_5.
$$

Thus the exact target is

$$
\boxed{d_1+d_5>w.}
$$

The two losses are not independent.  They are coupled by the common C-triangle equations

$$
\gamma_1=1-ru,
$$

and

$$
\gamma_5=u-\delta-{w\over r-1}.
$$

For a generic $T_+$ loss with input $a$, full endpoint $y=1-a$, and radial value $c=y+\tau$, write

$$
B=1-a-d.
$$

Then the loss $d$ is the unique positive root of

$$
E(d)=y\tau-Ad-(1-c^2)d^2=0,
$$

where

$$
A=2c^2-c+2\tau.
$$

This gives a monotone loss variable, but the lower bounds obtained by estimating each loss separately are currently too weak for the remaining lower-sheet cases.

## 4. Why separate loss bounds failed

For a $T_+$ loss equation

$$
E(d)=y\tau-Ad-(1-c^2)d^2=0,
$$

one has the crude lower bound

$$
d\ge {y\tau\over A+(1-c^2)y}.
$$

Applying this separately to $d_1$ and $d_5$ does not prove

$$
d_1+d_5>w
$$

globally.  The bound is too weak near branch-switching layers where one of the $\tau_i$ is small.

## 5. Lower-sheet information

On $T_+^{lo}$,

$$
B\le {c\over2}\le {1\over2}.
$$

This immediately proves $(T_+^{lo},L)$ because

$$
L\le {\sqrt3\over4}
$$

and

$$
{1\over2}+{\sqrt3\over4}<1.
$$

The same simple bound is not enough for $(T_+^{lo},T_-)$ or $T_+T_+$, because the other branch can in principle approach a full endpoint.  More correlation from the C-geometry is needed.

## 6. Numerical status

Strict maximal-branch sampling found realized lower-sheet cases.  Typical high values were around

$$
(T_+^{lo},T_+^{hi}):\qquad F\approx0.91965,
$$

and

$$
(T_+^{lo},T_+^{lo}):\qquad F\approx0.91093.
$$

Thus the empirical gap is approximately $0.08$ in the best focused samples, but this is not a proof and should not be cited as a proven bound.

## 7. Suggested next proof target

The most promising next target is an analytic uniform gap for the lower-sheet cases.  A plausible route is:

1. Parameterize the lower sheet by $\beta_-(\mu)$, where
   $$
   \beta_-(\mu)={1-\sqrt{4\mu^2-3}\over2}.
   $$
2. Use the equality $b=c\beta_-(\mu)$ to replace the crude $b\le c/2$ bound by a sharper branch-specific inequality.
3. Combine this with the C-geometry constraints for $\gamma_1$ and $\gamma_5$ to prove a uniform gap in the remaining lower-sheet cases.

This proof is not yet supplied.
