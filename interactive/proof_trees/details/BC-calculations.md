# [BC-CALC] Finite calipers and the rational envelope

[\[MAIN\]](../README.md) · [\[BC\]](../BC.md) · [\[D\]](../D.md) · [\[CALIPERS\]](../CALIPERS.md)

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

- **Five calipers, one capacity-dependent orientation.**
    - With $P=rV_2$, $Q=tV_4$, and $k=y-r$, the hull edges are $MG_x,G_xG_y,G_yP,PQ,QM$.
    - The difficult side is $[r+t+\max\{1/2,1-x(1-k)\}]/\sqrt{1-k+k^2}$.
- **Use the coupled inequality.**
    - The two radii satisfy $2(r+t)>(1-y+r)(2x-y+r)$.
    - Thus its numerator exceeds $1-k/2+k^2/2\ge\sqrt{1-k+k^2}$.
- **Use a reusable local envelope, not a new center normal form.**
    - For $m=\min(a,b)\le3/8$ and $\delta=1-a-b\ge0$, put $b(m)=m/2-2m^2/5$ and $K(m)=(5+4m)/(5-4m)$.
    - Then $1-C_0(a,b)\ge\max\{b(m),m-K(m)\delta\}$.
    - Outside this coefficient range use $m(1-m)/2$; do not extend the rational envelope without proof.
- **Retain the complete analytic reduction.**
    - Branchwise concavity reduces the coupled inequality to three transition configurations.
    - Their residuals have explicitly positive cubic, quartic, and quadratic bounds in 2615.
    - Exact symbolic checkers audit identities, not the completeness of the geometric proof.

The other four calipers are evaluated explicitly in 2616; finite calipers are exhaustive, not an angular scan.

## Proof sources

The active terminal is [2616](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2616_bc_d_finite_calipers.md).
Its capacity input is [2615](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2615_slack_sensitive_radial_envelope.md).
The entire page is explanatory; numbered sources supply proof authority.
