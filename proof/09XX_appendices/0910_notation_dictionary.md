# Glossary And Notation Dictionary

Status: Reference

- $H$: side-$1$ regular hexagon.
- $H_L$: side-$L$ regular hexagon.
- $O$: center of the hexagon. Some older notes use $C$.
- $V_i$: hexagon vertices.
- $e_{i,i+1}$: boundary edge.
- $r_i$: radial segment $[O,V_i]$.
- $M_i$: midpoint $V_i/2$.
- $S$: skeleton.
- $S_{1/2}$: half-skeleton.
- $T_C$: center triangle, not to be confused with the center point.
- $T_i$: vertex triangle at $V_i$.
- CE0/CE1/CE2: exhaustive preferred names for C-triangle perimeter-edge types.
- Ce0/Ce1/Ce2: historical aliases.
- Vd0/Vd1/Vd2/T3-like: exhaustive V-triangle types for original vertex roles.
- $d_0,d_{60},\dots,d_{300}$: degree-indexed ray-intersection distances from $O$ to $\partial T_C$.
- $1-d_{60i}$: available complementary radial distance on $[O,V_i]$ after $T_C$.
- $a,b,c$: local V-triangle coordinates; in envelope files these are stated
  lower-bound demands.
- $A(T),B(T),C(T)$: actual maximal local reaches of a realizing vertex
  triangle when they must be distinguished from demands.
- $(a_i,b_i)$: actual selected incoming and outgoing boundary row data for the
  vertex role $T_i$ in the $N_+$ split.
- $c_i$: radial coordinate of $T_i$.
- supercritical row: a row with $a_i+b_i>1$.
- $N_+$: $\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert$, the number of supercritical rows.
- $K_5$: archived May 25 five-point obstruction set $\{P_3,P_5,D_0,D_1,D_2\}$.
- $\Lambda(K)$: optimized side length of the smallest enclosing equilateral
  triangle for the finite set $K$.
- admissible set: feasible local triples $(a,b,c)$.
- $f(a,b)$: local normalized maximum area inside $H$ for a vertex triangle
  forced to contain the corresponding row data.
- $G=1-f$: normalized local area loss.
- $F$: coverage-coordinate zero-diagonal map.
- $g_c$: defect-coordinate admissible-set map.
- algorithm 1: the failed unimodality route using local diagonal max-$c$ points.
- algorithm 2: the diagonal-relaxation route using equality patterns among the
  nonsupercritical rows in the CE0 all-Vd0 $N_+=1$ branch.
- 걸거치는: crossing or straddling adjacent structure in the problematic T3-like way.
