# Active Length-Budget Corollaries

Status: Proven

This source owns every active Strategy 1 substitution. The geometric caps are
proved in [`2500`](2500_boundary_length_bounds.md) and
[`2510`](2510_skeleton_length_bounds.md); the generic perimeter and skeleton
budgets are proved in
[`2530`](2530_common_CE1_CE2_budget_lemmas.md). Historical case files remain as
compatibility wrappers around the named rows below.

## 1. Cap ledger

For the closures of the original open roles:

$$
L_C=0\quad\text{in CE0},
$$

$$
L_C\le\frac{\sqrt3}{2}-\frac34\quad\text{in CE1},
\qquad
L_C<\frac12\quad\text{in CE2}.
\tag{1}
$$

A nonsupercritical V role contributes at most $1$ to $\partial H$; a
supercritical role is Vd0 and contributes at most $2/\sqrt3$; a Vd1/Vd2 role
contributes strictly less than $1/2$. A Vd2 role containing a neighboring
midpoint contributes strictly less than $1/3$.

Put

$$
\theta=\frac2{\sqrt3}-1.
$$

The master perimeter-deficit theorem in `2530` says that a state with $n$
supercritical Vd0 roles and strict exceptional caps $q_j<1$ is impossible if

$$
L_C+n\theta\le\sum_j(1-q_j).
\tag{2}
$$

## 2. Boundary-complete rows

### Row Z0

If the six open V roles cover $\partial H$ and $N_+=0$, the state is
impossible.

Indeed, on every edge the two incident relatively open traces overlap, so
$B_i+A_{i+1}>1$. Summing gives

$$
6<\sum_i(A_i+B_i)\le6,
$$

a contradiction.

### Row Z1

If the six open V roles cover $\partial H$, $N_+=1$, and at least one role is
Vd1 or Vd2, the state is impossible.

The exceptional role is nonsupercritical, the unique supercritical role is
Vd0, and the other four roles contribute at most one. Hence the V-only total
is strictly below

$$
\frac12+\frac2{\sqrt3}+4<6.
$$

## 3. Perimeter substitutions with a C trace

### Row P0

CE1 or CE2, $N_+=0$, and at least one Vd1/Vd2 role is impossible. Use (2)
with $n=0$, $q_1=1/2$, and $L_C<1/2$.

### Row P1

CE1, $N_+=1$, and at least one Vd1/Vd2 role is impossible. Use (2) with
$n=1$, $q_1=1/2$, and the CE1 cap in (1); equivalently,

$$
\left(\frac{\sqrt3}{2}-\frac34\right)+\theta<\frac12.
$$

### Row P2

CE2, $N_+=1$, and at least two Vd1/Vd2 roles is impossible. Use (2) with
$n=1$, $q_1=q_2=1/2$; indeed $L_C+\theta<1$.

### Row P3

CE2, $N_+=1$, with a Vd2 role containing $M_{i-1}$ or $M_{i+1}$ is
impossible. Use (2) with $n=1$, $q_1=1/3$; the required inequality is

$$
\frac12+\theta<\frac23,
$$

which is equivalent to $12<7\sqrt3$.

## 4. Skeleton count substitutions

Every supercritical V role and every positive-support V role contributes
strictly less than $3/2$ to the full skeleton. The two classes are disjoint.
The C role contributes strictly less than $3/2$, while every remaining
nonsupercritical Vd0 role contributes at most $2$. Thus, with

$$
N_{\rm sp}=|\{i:T_i\text{ is Vd1, Vd2, or T3-like}\}|,
$$

`2530` proves

$$
N_++N_{\rm sp}\ge3
\quad\Longrightarrow\quad
L_S(T_C)+\sum_iL_S(T_i)<12.
\tag{3}
$$

### Row S0

Every CE1/CE2 state with $N_++N_{\rm sp}\ge3$ is impossible by (3). This
single row includes:

- $N_+=1$ with at least two T3-like roles;
- $N_+=1$ with one Vd1/Vd2 role and a further positive-support role;
- every other mixed state reaching the same count.

### Row S1

Every CE1/CE2 state with $N_+\ge2$ is impossible. Normalize the unique C-role
midpoint to $M_0$ and choose a supercritical index $s\ne0$. The self-midpoint
obstruction excludes $M_s$ from $T_s$, and the C role also misses it.
Diameter locality forces $M_s$ into an adjacent open V role, which then has
positive support on $r_s$. This rescuer is distinct from the supercritical
roles, so $N_{\rm sp}\ge1$ and (3) applies.

## 5. Dispatch theorem

### Theorem 5.1

Rows Z0, Z1, P0--P3, S0, and S1 close every routing entry assigned wholly to
Strategy 1.

### Proof

The structural routing distinguishes zero gaps from nonzero gaps, then uses
$N_+$ and the V-type counts. Z0 and Z1 are the two zero-gap length rows. P0
closes the $N_+=0$ Vd branch; P1 closes the CE1 one-Vd branch; P2 removes the
CE2 branch with at least two Vd roles; P3 is the Vd2 neighboring-midpoint
hybrid. S0 performs the common high-count pruning, and S1 removes all
$N_+\ge2$ nonzero-gap states. These are exactly the Strategy 1 entries.
$\square$
