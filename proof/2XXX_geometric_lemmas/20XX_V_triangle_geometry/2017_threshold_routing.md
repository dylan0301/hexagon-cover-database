# Exact Threshold Routing for Capped Demand Chains

Status: Proven

This note isolates the branch-independent routing principle used by the CE1,
CE2, and T3-like Strategy 2 arguments.  Once an actual-V triangle demand crosses one
low-root threshold, the corresponding capped map produces a high output and
all later extensive maps preserve it.  The statement prevents unnecessary
expansion of a full five-map composition after the decisive threshold has
already been crossed.

## 1. One-hit threshold routing

For

$$
0<d<1-\frac{\sqrt3}{2},
$$

put

$$
e(d)=\ell(1-d).
$$

The high-demand threshold theorem in
[`2012_high_radial_low_root_bounds.md`](2012_high_radial_low_root_bounds.md)
proves

$$
z>e(d)
\quad\Longrightarrow\quad
G_{1-d}(z)\ge1-e(d).
$$

Let

$$
z_j=G_j(z_{j-1})
\qquad(1\le j\le m),
$$

where every $G_j:[0,1]\to[0,1]$ is nondecreasing and extensive:

$$
G_j(t)\ge t.
$$

Suppose that, for some index $k$,

$$
G_k=G_{1-d}
$$

and

$$
z_{k-1}>e(d).
$$

Then

$$
z_k\ge1-e(d).
$$

Extensivity gives successively

$$
z_j\ge z_k\ge1-e(d)
\qquad(k\le j\le m).
$$

Therefore:

$$
\boxed{
\text{once a chain input crosses }e(d),
\text{ every later output is at least }1-e(d).
}
$$

In particular, if $e(d)<Q$, then

$$
\boxed{
z_m>1-Q.}
$$

The final inequality is strict because $1-e(d)>1-Q$.

## 2. Persistence before the trigger

If all maps before position $k$ are extensive, then

$$
z_{k-1}\ge z_0.
$$

Thus an initial estimate

$$
z_0>e(d)
$$

may be routed to any later occurrence of the map $G_{1-d}$ without estimating
the intervening maps separately.

More generally, any strict lower bound obtained at one stage persists through
every subsequent extensive map until the desired threshold map is reached.

## 3. Two-threshold routing

The CE2 one-gap proof uses the following exact dichotomy.

Let $d_1,d_2$ satisfy

$$
0<d_1,d_2<1-\frac{\sqrt3}{2},
$$

and suppose a chain contains later occurrences of both maps

$$
G_{1-d_1},
\qquad
G_{1-d_2}.
$$

Assume

$$
z_0>e(d_1)
$$

and, for some target $Q$,

$$
\min\left\{e(d_1),e(d_2)\right\}<Q.
$$

Then one of the following alternatives holds.

1. If $e(d_1)<Q$, extensivity preserves $z>e(d_1)$ until the
   $G_{1-d_1}$ V triangle, and that V triangle forces every later output above $1-Q$.
2. If $e(d_1)\ge Q$, then

   $$
   z_0>e(d_1)\ge Q>e(d_2),
   $$

   so extensivity preserves an input above $e(d_2)$ until the
   $G_{1-d_2}$ V triangle, and that V triangle forces every later output above $1-Q$.

Hence

$$
\boxed{
z_m>1-Q.}
$$

This is a logical routing lemma: it does not require evaluation of the maps
that precede or follow the first triggered threshold.

## 4. Passage from formal iterates to actual V triangles

The routing lemma applies only after the usual actual-V triangle induction has been
established.  Suppose an actual nonsupercritical V triangle has incoming reach
$A_i\ge z$, actual radial reach $C_i\ge c_i$, and outgoing reach $B_i$ with

$$
A_i+B_i\le1.
$$

The proof-safe capped-map theorem in
[`2011_capped_demand_map.md`](2011_capped_demand_map.md) gives

$$
B_i\le F_{c_i}(z).
$$

If the next boundary handoff gives $A_{i+1}\ge1-B_i$, then

$$
A_{i+1}\ge1-F_{c_i}(z)=G_{c_i}(z).
$$

Thus the formal iterates are lower bounds for actual incoming reaches.  Once
this induction has been written for the required V triangles, Sections 1--3 may be
used to discard all maps that are irrelevant after the decisive threshold
crossing.

The distinction is essential: threshold routing shortens the scalar part of
the proof, but it does not replace the V triangle-by-V triangle verification that each
formal iterate is realized as a lower bound for the corresponding actual
role.
