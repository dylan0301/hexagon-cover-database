# Former Remaining $T_+$ Obligations

Status: Reference / superseded

This file records the lower-sheet $T_+$ obligations that were formerly open,
plus failed approaches that should not be repeated.

The obligations recorded here are now discharged by
`556_lower_sheet_completion_proofs.md`, which gives analytic proofs of all
three formerly open branches:

$$
(T_+^{lo},T_-),\qquad (T_+^{lo},T_+^{hi}),\qquad (T_+^{lo},T_+^{lo}).
$$

Thus this file is now historical.  It remains useful because it explains why
some plausible proof approaches are invalid or too weak.

## 1. Solved branches

The following branches were already proved or eliminated before the lower-sheet
completion:

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

The lower-sheet completion proves the remaining three branches:

$$
(T_+^{lo},T_-),\qquad (T_+^{lo},T_+^{hi}),\qquad (T_+^{lo},T_+^{lo}).
$$

Therefore no lower-sheet $T_+$ branch remains open for the boundary-loss
objective

$$
F=B(s,1-\gamma_5)+B(u,1-\gamma_1)<1.
$$

## 2. Historical coupled-loss formulation

For any $T_+T_+$ branch, one can write

$$
B_5=1-s-d_5, \qquad B_1=1-u-d_1.
$$

Then

$$
F=B_5+B_1=1+w-d_1-d_5.
$$

Thus the exact target is

$$
d_1+d_5>w.
$$

This formulation correctly identifies the coupling in the problem, but it is
not the proof route used in the final lower-sheet completion.  The final proof
for $(T_+^{lo},T_+^{hi})$ instead uses the left lower-sheet maximal branch to
bound the right high-sheet ratio.

## 3. Final lower-sheet proof route

Let

$$
R={1\over r},\qquad S=\sqrt{1-R+R^2},\qquad k={\sqrt{13}-1\over6}.
$$

For the final branch

$$
(T_+^{lo},T_+^{hi}),
$$

the decisive chain is:

1. Left lower sheet gives

   $$
   s\le k.
   $$

2. The $C$-geometry identity gives

   $$
   c_1:=1-\gamma_1\ge L(R):=1+{1-S\over R}-k.
   $$

3. Right high sheet gives

   $$
   c_1\le S.
   $$

4. Hence $L(R)\le S$, which forces

   $$
   R\ge k.
   $$

5. If $\beta=B_1/c_1$ is the right high-sheet ratio, then monotonicity of

   $$
   g_R(\beta)={\sqrt{\beta^2-\beta+1}\over R+\beta}
   $$

   and an exact one-variable factorization give

   $$
   \beta\le1-k.
   $$

6. Since the right branch is $T_+$, $\beta\ge R$.  Therefore

   $$
   k\le R\le1-k.
   $$

7. On this interval,

   $$
   S\le2k.
   $$

8. Hence

   $$
   B_1=\beta c_1\le(1-k)S\le2k(1-k)<{1\over2}.
   $$

The left lower-sheet bound gives

$$
B_5\le{1\over2},
$$

so

$$
F=B_5+B_1<1.
$$

The full proof is in `556_lower_sheet_completion_proofs.md`.

## 4. Failed approach: separate loss bounds

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

globally.  The bound is too weak near branch-switching layers where one of the
local surplus parameters is small.  The final proof avoids separate loss
estimates.

## 5. Failed approach: raw algebraic sheet parameterization

A tempting parameterization is to impose only the formal sheet equations

$$
b=c\beta_-(\mu)
$$

for the left lower sheet and

$$
b=c\beta_+(\mu)
$$

for the right high sheet.

This is insufficient.  It produces fake high-$F$ points because it does not
enforce the corrected maximal definition

$$
B(a,c)=\max\{b:(a,b,c)\in\mathcal A,\ a+b\le1\}.
$$

A formal algebraic root may be beaten by a Low or $T_-$ candidate and therefore
may fail to be the realized branch of $B(a,c)$.  This is precisely why
`552_B_map_branch_realization.md` treats branch labels as realized maxima, not
as formal roots.

## 6. Failed approach: infeasibility of $b=1/2$ alone

One intermediate route tried to prove that $b=1/2$ is infeasible on the right
side and then conclude $B_1<1/2$.

The infeasibility inequalities can be certified, but the conclusion has a
monotonicity gap: the exact admissible set for fixed $(a,c)$ is not simply
downward closed in $b$ across the full semialgebraic model.  Thus infeasibility
of the single value $b=1/2$ is not by itself enough to exclude a larger
realized branch value without an additional monotonicity argument.

The final proof avoids this gap by working directly with the realized right
high-sheet ratio

$$
\beta={B_1\over c_1}
$$

and proving

$$
\beta\le1-k,\qquad c_1\le S\le2k.
$$

## 7. Numerical status

Earlier strict sampling found the formerly remaining branches with visible
empirical gap.  These numerical observations were useful for finding the
analytic proof, but are no longer needed for the final status.

The important proof status is now analytic:

$$
(T_+^{lo},T_-),\quad (T_+^{lo},T_+^{hi}),\quad (T_+^{lo},T_+^{lo}) \quad\Longrightarrow\quad F<1.
$$
