# CE2 One-Interval Lemma

Status: Lemma target

Normalize a CE2 center triangle so that

$$
M_4\in T_C.
$$

Let $T_4$ be the vertex role at $V_4$, and let $(a_4,b_4)$ be its incoming and
outgoing perimeter row. Assume the skeleton covering has been maximalized and
that $T_4$ is supercritical:

$$
a_4+b_4>1.
$$

Then

$$
T_C\cap\partial H=I_L\sqcup I_R,
$$

with

$$
I_L\subset e_{3,4}, \qquad I_R\subset e_{4,5}.
$$

The nearby vertex triangles are

$$
T_3,T_4,T_5.
$$

## Target conclusion

At least one of the following holds:

$$
I_L\subset T_3,
$$

$$
I_L\subset T_4,
$$

$$
I_R\subset T_4,
$$

$$
I_R\subset T_5.
$$

Equivalently, in the maximalized skeleton covering, one interval of
$T_C\cap\partial H$ is covered by adjacent $V$-triangles.

## Interaction types

For interval $I$ and $K_i=T_i\cap\partial H$:

- include: $I\subset K_i$;
- intersect: $I\cap K_i\ne\varnothing$ but $I\not\subset K_i$;
- attach: $I\cap K_i=\varnothing$ and closures touch;
- far: closures are disjoint.

After maximality, intersect cases should be eliminated. The remaining cases are

$$
(\mathrm{attach},\mathrm{attach}), (\mathrm{attach},\mathrm{far}), (\mathrm{far},\mathrm{attach}), (\mathrm{far},\mathrm{far}).
$$

Coordinate form:

$$
x_3<\beta_L, \qquad x_5<\beta_R \implies b_4\ge\beta_L\quad\text{or}\quad a_4\ge\beta_R.
$$

After eliminating intersect cases:

$$
x_3\le\alpha_L, \qquad x_5\le\alpha_R \implies b_4\ge\beta_L\quad\text{or}\quad a_4\ge\beta_R.
$$
