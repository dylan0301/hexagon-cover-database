# Six-Step Composition

Status: Definition

Let $x_i$ be the defect handed to the edge after $V_i$. Then

$$
x_{i+1}=g_{c_i}(x_i),
$$

and after one full cycle,

$$
x_6=(g_{c_5}\circ g_{c_4}\circ\cdots\circ g_{c_0})(x_0).
$$

A cover requires

$$
x_0\ge x_6.
$$

A contradiction strategy proves

$$
x<(g_{c_5}\circ\cdots\circ g_{c_0})(x)
$$

for every allowed $x$.
