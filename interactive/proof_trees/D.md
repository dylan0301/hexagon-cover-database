# [D] Four-point ratio obstruction

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

A supported midpoint has an adjacent **supplier** whose open triangle contains that midpoint;
positive support alone does not imply supplying that midpoint.
For D, $Y(w)=V_0-wV_1$, $a\ge0$, $\varepsilon>0$, and $\beta\ge0$.
The original placement adapters force the four points and prove the ratio bound.

## Tree

- **Separate original placement from the geometric theorem.**
    - The T3-like or Vd1 chart forces $O,\varepsilon V_1,Y(a),Y(1-\beta)$ into $U_C$.
    - It proves $\beta\le\varepsilon/(a+\varepsilon)$.
    - Size bounds may still help force original gap endpoints; the geometric theorem does not require them.
- **Use diameter at the boundary.**
    - If $a=0$, the points contain $O,V_0$.
    - Put $s=a+\varepsilon$. If $s\ge1$, then $\|Y(a)-\varepsilon V_1\|^2=1-s+s^2\ge1$.
- **Otherwise reduce by convexity.**
    - Put $v=a/s$, so $0<s,v<1$ and $a=sv\le v\le1-\beta$.
    - Replace the far point by $Y(v)$ on the same boundary segment.
    - The smaller quadrilateral is $O,Y(v),Y(sv),s(1-v)V_1$.
- **Use four hull-edge calipers.**
    - Their side lengths are $1/\sqrt{1-v+v^2}$, $1+s(1-v)$, $1/\sqrt{1-s+s^2}$, and $1+v(1-s)$.
    - All exceed one for $0<s,v<1$ — [\[D-CALC\]](details/D-calculations.md).
- **Conclude $\Lambda(K_D)\ge1$.** Compact containment in an open unit triangle is impossible.

This proof neither forces a candidate midpoint nor introduces signed center parameters.

## Proof sources

The active terminal is [2616](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2616_bc_d_finite_calipers.md).
The D terminal does not depend on the BC capacity-envelope lemma. The original supplier adapters remain responsible for forcing its four points and establishing the ratio.
The entire page is explanatory; numbered sources supply proof authority.
