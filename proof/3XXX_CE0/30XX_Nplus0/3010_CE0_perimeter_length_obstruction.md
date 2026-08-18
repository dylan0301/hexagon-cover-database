# CE0 Perimeter-Length Obstruction

Status: Proven

Assume a hypothetical open-triangle cover has original roles

$$
U_C,U_0,\dots,U_5,
$$

with indices taken modulo $6$, and put $T_C=\overline{U_C}$ and
$T_i=\overline{U_i}$. Suppose

$$
T_C\text{ is CE0}
$$

and

$$
N_+=\left\lvert \left\lbrace i : A_i+B_i>1 \right\rbrace \right\rvert=0.
$$

Then the cover cannot exist.

## Proof

Write $e_{i,i+1}$ for the side of $H$ from $V_i$ to $V_{i+1}$, and write
$e_{i,i+1}^{\circ}$ for its relative interior.

Since $T_C$ is CE0, it has no positive-length overlap with any boundary edge of
$H$. If $U_C$ contained any point of
$e_{i,i+1}^{\circ}$, then openness would give a positive-length interval of
$e_{i,i+1}$ contained in $T_C$. Hence

$$
U_C\cap e_{i,i+1}^{\circ}=\varnothing.
$$

If $j\notin\{i,i+1\}$, then a $V_j$-triangle cannot contain any point of
$e_{i,i+1}^{\circ}$: every point of $e_{i,i+1}^{\circ}$ has distance greater
than $1$ from $V_j$, while a unit open equilateral triangle containing $V_j$
contains only points at distance less than $1$ from $V_j$.

Therefore the open interval $e_{i,i+1}^{\circ}$ must be covered by the two
relatively open sets

$$
U_i\cap e_{i,i+1}^{\circ}
$$

and

$$
U_{i+1}\cap e_{i,i+1}^{\circ}.
$$

Both are nonempty, because $U_i$ contains $V_i$ and $U_{i+1}$ contains
$V_{i+1}$ as open-cover vertex roles. Since $e_{i,i+1}^{\circ}$ is connected,
these two nonempty relatively open covering sets cannot be disjoint. Their
intersection contains a nonempty relatively open subinterval, and hence has
positive length. Thus

$$
1=\mathcal H^1(e_{i,i+1}^{\circ})<B_i+A_{i+1}.
$$

Summing over all six sides gives

$$
6<\sum_{i=0}^5(B_i+A_{i+1})=\sum_{i=0}^5(A_i+B_i).
$$

But $N_+=0$ means that every V triangle satisfies

$$
A_i+B_i\le1.
$$

Therefore

$$
\sum_{i=0}^5(A_i+B_i)\le6,
$$

contradicting the strict perimeter inequality above. Hence the CE0,
$N_+=0$ branch is impossible.
$$
\Box
$$
