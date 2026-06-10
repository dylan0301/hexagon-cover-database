# Algorithm-2 Diagonal Relaxation

Status: Empirical strategy

Algorithm 2 chooses three diagonal points by forcing two of the three
nonsupercritical rows among $V_0,V_1,V_2$ to lie on equality lines.

The three equality patterns are:

$$
a_1+b_1=1,\qquad a_2+b_2=1,
$$

$$
a_0+b_0=1,\qquad a_2+b_2=1,
$$

and

$$
a_0+b_0=1,\qquad a_1+b_1=1.
$$

The intended property is that, regardless of how the free boundary points move,
the corresponding diagonal points remain inside the relaxed obstruction region
used for the finite five-point test.

The current status is empirical/strategy. A proof must define the relaxed
region exactly and prove the containment for all allowed parameters.
