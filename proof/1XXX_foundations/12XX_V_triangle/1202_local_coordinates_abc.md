# Local Coordinates $(a,b,c)$

Status: Definition

For a normalized $V_i$-triangle:

$$
a_i=\text{coverage length on }e_{i-1,i}\text{ from }V_i,
$$

$$
b_i=\text{coverage length on }e_{i,i+1}\text{ from }V_i,
$$

$$
c_i=\text{coverage length on }[V_i,O]\text{ from }V_i.
$$

These indexed coordinates are the actual maximal reaches of the chosen
triangle on the three local unit segments. In admissible-set and propagation
files, unindexed lowercase $(a,b,c)$ may instead denote prescribed lower-bound
demands. In that use, a realizing triangle has actual reaches

$$
A\ge a,
\qquad
B\ge b,
\qquad
C\ge c.
$$

Row-type conditions such as $A+B\le1$ or $A+B>1$ concern the actual reaches,
not arbitrary smaller demands. A file using demand coordinates must state
that convention explicitly.

Boundary coverage requires

$$
b_i+a_{i+1}\ge1.
$$

The tight chain is

$$
b_i+a_{i+1}=1.
$$
