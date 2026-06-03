# One-Critical Neighbor-Envelope Strategy

Status: Strategy

This file records the June 3 one-critical strategy for realizing the diagonal
endpoints $D_0,D_1,D_2$ in the May 25 five-point package.

Here one-critical means the May 25 reduced slice with unique strict local
$AB$-union vertex $V_4$, as specified in
[`631_reduction_prompt_spec.md`](631_reduction_prompt_spec.md).

The point is to use the local radial maximum for the row $V_j$ together with
the proven neighboring-ray maximums for $V_{j-1}$ and $V_{j+1}$, then replace
the resulting maximum by a simpler max-free envelope.  This is a proof target,
not a completed endpoint-realization proof.

## Local reach comparison

For $j=0,1,2$, write

$$
D_j=\rho_jV_j.
$$

The endpoint parameter satisfies

$$
\rho_j=1-E_j
$$

if $E_j$ is the largest inward reach from $V_j$ along $[V_j,O]$ attained by the
union of the relevant local regions.

The intended local comparison is

$$
E_j=\max\{C_{\mathrm{rad}}(a_j,b_j), C_+(a_{j-1},b_{j-1}), C_+(b_{j+1},a_{j+1})\}.
$$

Here:

- $C_{\mathrm{rad}}(a,b)$ denotes the local same-ray radial candidate from
  [`../300_vertex_triangle/304_piecewise_c_formula.md`](../300_vertex_triangle/304_piecewise_c_formula.md).
- $C_+(a,b)$ denotes the proven upper-neighbor capacity from
  [`../300_vertex_triangle/310_neighbor_ray_max_c_formula.md`](../300_vertex_triangle/310_neighbor_ray_max_c_formula.md).
- The lower-neighbor capacity is $C_-(a,b)=C_+(b,a)$.

Undefined capacities should be treated as absent candidate cuts, not as
numerical zeroes.  A finished proof must still show that no non-adjacent region
$R_i$ cuts $[O,V_j]$ earlier than the three listed sources.

## Four-variable local form

The three rows $j-1,j,j+1$ have six local coordinates, but two adjacent pairs
share boundary points:

$$
b_{j-1}+a_j=1,\qquad b_j+a_{j+1}=1.
$$

Use the four variables

$$
x=a_{j-1},\qquad y=b_{j-1},\qquad z=b_j,\qquad w=b_{j+1}.
$$

Then

$$
a_j=1-y,\qquad a_{j+1}=1-z,
$$

and the local comparison becomes

$$
E_j=\max\{C_{\mathrm{rad}}(1-y,z), C_+(x,y), C_+(w,1-z)\}.
$$

The one-critical envelope target is to find a simple max-free function

$$
\mathcal E(x,y,z,w)
$$

such that, on the relevant May 25 one-critical domain,

$$
\mathcal E(x,y,z,w)=\max\{C_{\mathrm{rad}}(1-y,z), C_+(x,y), C_+(w,1-z)\}.
$$

If this identity is proved with the required branch conditions, then the
diagonal point can be plotted and used with

$$
\mathcal E_j=\mathcal E(x,y,z,w)
$$

as

$$
D_j=(1-\mathcal E_j)V_j.
$$

## Required proof checks

To turn this strategy into a diagonal endpoint realization, one must prove:

1. the radial candidate $C_{\mathrm{rad}}(1-y,z)$ is valid on the intended
   local branch, using the exact predicate from
   [`631_reduction_prompt_spec.md`](631_reduction_prompt_spec.md);
2. the two neighboring candidates are valid applications of the proven
   neighbor-ray formula, including all undefined and boundary cases;
3. every non-adjacent $R_i$ either misses $[O,V_j]$ before the candidate
   endpoint or gives only a later cut;
4. the max-free envelope $\mathcal E$ agrees with the displayed maximum on the
   full reduced domain needed for $D_0,D_1,D_2$;
5. tangent, endpoint, $O\notin U$, and no-cut cases are separated before the
   five-point inequality $\Lambda(K_5)>1$ is applied.

Until these checks are supplied, this file should be cited only as a strategy
for simplifying the diagonal endpoint computation.
