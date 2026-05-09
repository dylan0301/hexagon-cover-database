# CE0 + Vd1/Vd2 Assembly

Status: Proven

We prove the expanded closed-triangle theorem, then obtain the original open-triangle corollary by the Lebesgue-number/scaling equivalence.

## Expanded theorem

For every $L>1$, no seven closed unit equilateral triangles cover $S_{1/2}(H_L)$ under the assumptions:

$$
T_C\text{ is CE0},
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

## Proof

Assume, for contradiction, that such a cover exists.

By symmetry, normalize the Vd1/Vd2 triangle to $T_0$. If $T_0$ is Vd2, choose one adjacent-ray intersection. This reduces to the Vd1 local geometry, since the second intersection only imposes an additional constraint.

Let $x$ be the largest distance from $O$ to the chosen adjacent-ray intersection. The local rhombus geometry with side length

$$
L=1+\epsilon
$$

extracts boundary data $(a,b)$ from $x$ and $\theta$.

There are two regimes.

### Regime 1: $x<1/2$

The remaining half-skeleton holes are handled by the midpoint-hole subcase split.

If two holes are covered by two different triangles, the ordinary zero-diagonal chain applies. The proven analytic inequality gives

$$
b+F^{\circ3}(a)<1.
$$

If one triangle covers two holes, apply the frontier perturbation lemma first. The perturbed point is stronger and feasible, so the same inequality applies.

In either subcase, the boundary/half-skeleton chain cannot close, contradicting coverage.

### Regime 2: $x\ge1/2$

On the natural domain where $a\in[0,1]$, the proven analytic inequality gives

$$
b+F^{\circ4}(a)<1.
$$

Again, if one triangle covers two holes, first apply the frontier perturbation lemma. If two triangles cover the holes separately, use the ordinary chain.

In either subcase, the chain cannot close, contradicting coverage.

Thus the expanded closed-triangle theorem holds.

## Original open-triangle corollary

If the original side-$1$ hexagon had a seven-open-unit-triangle cover in this case, the Lebesgue-number lemma would produce a shrunken closed cover, and scaling would produce a closed unit cover of some $H_L$, $L>1$. This contradicts the expanded theorem.

Therefore CE0 + Vd1/Vd2 cannot occur in a seven-open-unit-triangle cover of $S_{1/2}(H)$.
