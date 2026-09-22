# [BC] Five-point selected-gap obstruction

[\[MAIN\]](README.md) · [\[BC\]](BC.md) · [\[D\]](D.md) · [\[CALIPERS\]](CALIPERS.md)

## Terms used here

$H$ is the closed regular hexagon of side one, $O=0$ its center, and
$V_i=(\cos(i\pi/3),\sin(i\pi/3))$ its vertices (indices modulo six).
The spoke is $r_i=[O,V_i]$ and its midpoint is $M_i=V_i/2$.
$U_C$ is the open unit equilateral triangle containing $O$; $U_i$ contains $V_i$.
Their closures are $T_C,T_i$. Coverage uses the open triangles.
$A_i,B_i$ are the actual boundary reaches toward $V_{i-1},V_{i+1}$.
Nonsupercritical means $A_i+B_i\le1$, not a condition on arbitrary lower demands.
A gap $X_i([B_i,1-A_{i+1}])$, where $X_i(w)=(1-w)V_i+wV_{i+1}$,
includes a singleton when its endpoints coincide.
A witness is forced into $U_C$ if the original covering hypotheses imply that membership.
$\Lambda(F)$ is the minimum closed equilateral enclosure side of the compact set $F$;
$F\subset U_C$ implies $\Lambda(F)<1$.
$C_0(a,b)=c_{\max}(a,b)$ is the own-ray capacity function, not the actual scalar $C_i$.
$C_+$ and $C_-$ are neighboring-ray capacities for that same prescribed pair.

## Tree

- **Use the original boundary path.**
    - Normalize the structural midpoint to $M_0$ and select gap $J_0$.
    - The five roles $T_1,\ldots,T_5$ are nonsupercritical; four middle edges have $B_i+A_{i+1}>1$.
    - Thus $A$ increases and $B$ decreases. Original perimeter coverage supplies $B_5>B_0/2$.
- **Keep two different comparison pairs.**
    - Put $x=B_0$, $y=1-A_1$, $z=B_3$, so $0<x\le y<1$ and $x/2\le z\le y$.
    - Set $r=1-C_0(1-y,z)$ and $t=1-C_0(1-z,x/2)$.
    - No uniform minimum pair is used. There is no point on $r_3$, but $B_3$ remains essential.
- **Force at most five points.**
    - The midpoint and both selected-gap endpoints are in $U_C$.
    - Apply $C_\pm(a,b)\le1-\min(a,b)\le C_0(a,b)$ separately at each triangle's own pair.
    - Safe radii are $\min\{1-C_0(A_i,B_i),A_{i-1},B_{i+1}\}$.
    - Therefore the fixed witnesses are $M_0,G_x,G_y,rV_2,\min(t,A_3)V_4$, where $G_w=X_0(w)$.
- **Deal with the one clipping explicitly.**
    - If $A_3<t$, then $A_3\ge1-y$ and $\|G_y-A_3V_4\|^2\ge1+(1-y)(2-y)>1$: diameter ends the proof.
    - Otherwise the fixed set is $M_0,G_x,G_y,rV_2,tV_4$.
- **Apply finite calipers.**
    - The hull order is $M_0,G_x,G_y,rV_2,tV_4$; discard a zero gap edge if $x=y$.
    - Four calipers exceed one by elementary squared identities.
    - The fifth follows from $2(r+t)>(1-y+r)(2x-y+r)$.
    - **CALCULATION LEAF:** reusable envelope, coupled inequality, and five support formulas — [\[BC-CALC\]](details/BC-calculations.md).
- **Conclude.** Every branch has $\Lambda(K_{BC})>1$, contrary to compact containment in $U_C$.

There is no candidate CE1/CE2 split, no CE1 return, no disk, and no sixth radial witness.
Structural midpoint and supplier classifications elsewhere remain part of the full proof.

## Proof sources

The active terminal is [2616](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2616_bc_d_finite_calipers.md).
Its capacity input is [2615](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2615_slack_sensitive_radial_envelope.md).
The entire page is explanatory; numbered sources supply proof authority.
