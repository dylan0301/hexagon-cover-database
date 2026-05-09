# Cyclic Contradiction Template

Status: Proof template

1. Assume seven triangles cover the chosen target.
2. Select $T_C,T_0,\dots,T_5$.
3. Extract $\gamma_i$ from $T_C$.
4. Extract $(a_i,b_i,c_i)$ from each $T_i$.
5. Enforce boundary coverage:
   $$
   b_i+a_{i+1}\ge1.
   $$
6. Use the admissible set $\mathcal A$.
7. Convert to a composition of one-variable maps.
8. Prove the cycle cannot close.
