# One strict budget principle for perimeter, skeleton, and area

Status: Proven

Let $X$ be a connected compact space with a finite Borel measure $\mu$ such
that every nonempty relatively open subset has positive measure. If finitely
many open sets $U_j$ cover $X$, and at least two have nonempty intersections
with $X$, then

$$\sum_j\mu(U_j\cap X)>\mu(X).$$

**Proof.** The nonempty relative pieces cannot all be pairwise disjoint,
otherwise they separate $X$. Some two overlap in a nonempty relatively open
set, of positive measure. Coverage gives multiplicity at least one everywhere
and at least two on that overlap. Integrating proves the strict inequality.
$\square$

Apply this to $\partial H$ and the full skeleton with $\mathcal H^1$, or to
$H$ with planar area. Each has the stated full-support property. Since the
original roles are open and their closures are $T_j$, any upper bounds whose
sum satisfies

$$\sum_j\mu(T_j\cap X)\le\mu(X)$$

already exclude coverage. Thus target budgets are $6$, $12$, and normalized
area $6$. This unifies only the final contradiction, not the local geometric
caps. Endpoint ownership still matters in every forcing and handoff argument.
