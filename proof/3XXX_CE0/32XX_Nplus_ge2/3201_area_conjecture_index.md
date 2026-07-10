# CE0, $N_+\ge2$, Area Package

Status: Proven

This folder proves the CE0 branch with at least two supercritical vertex rows.

The branch assumptions are

$$
T_C\text{ is CE0},
$$

and

$$
N_+
=
\left\lvert
\left\lbrace
i:a_i+b_i>1
\right\rbrace
\right\rvert
\ge2.
$$

## Proof route

The local area function is defined in
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md):

$$
f(a,b)
=
\max_T
\frac{\mathrm{area}(T\cap H)}{\sqrt3/4},
$$

where $T$ ranges over closed unit equilateral vertex triangles containing the
two required adjacent boundary points.

The unconditional local theorem in
[`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md)
proves

$$
f(a,b)\le1-\min(a,b)^2
$$

for every feasible row, and

$$
a+b>1
\quad\Longrightarrow\quad
f(a,b)\le1-\max(a,b)^2.
$$

The six-row analytic certificate in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
proves from exactly these two inequalities that

$$
N_+\ge2
\quad\Longrightarrow\quad
\sum_{i=0}^5f(a_i,b_i)<\frac{99}{20}<5.
$$

Because the local hypotheses of `3208` are now proved in `3205`, the
certificate is unconditional.

The CE0 center triangle contributes at most one normalized unit-triangle area.
Hence the seven triangles contribute less than

$$
\frac{99}{20}+1
=
\frac{119}{20}
<6,
$$

where $6$ is the normalized area of the side-$1$ regular hexagon.  Therefore
the branch cannot cover $H$.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md) | Reference | Defines $f(a,b)$, symmetry, monotonicity, and records the now-unneeded structural-maximizer conjecture as historical context. |
| [`3204_supercritical_vertex_loss_lemma.md`](3204_supercritical_vertex_loss_lemma.md) | Proven | Earlier supercritical proof under a structural hypothesis; superseded by the unconditional theorem in `3205`. |
| [`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md) | Proven | Proves both local square-loss inequalities for every admissible unit triangle without a structural hypothesis. |
| [`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md) | Proven | Proves the six-row strict area inequality from the square-loss inequalities; `3205` discharges those hypotheses. |

## Conclusion

The CE0, $N_+\ge2$ branch is closed unconditionally.
