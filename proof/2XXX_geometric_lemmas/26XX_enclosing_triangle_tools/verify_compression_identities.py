"""Exact symbolic checks for the new proof-compression lemmas.

Run with Python 3 and SymPy installed. These checks do NOT run the repository's
proof/check.py or its exact zero-gap certificate, and do not replace the sign
and hypothesis arguments in 2008b and 2614.
"""
import sympy as s

m, c, q = s.symbols('m c q', real=True)
h = s.sqrt(3) / 2
rot = s.Matrix([[-s.Rational(1, 2), -h], [h, -s.Rational(1, 2)]])
points = {
    'P': s.Matrix([0, 0]),
    'A': s.Matrix([m, 0]),
    'B': s.Matrix([-m/2, h*m]),
    'Z': s.Matrix([c-s.Rational(1, 2), h]),
}
passed = []

def equal(name, left, right):
    residual = s.simplify(s.expand(left-right))
    if residual != 0:
        raise AssertionError(f'{name}: nonzero residual {residual}')
    passed.append(name)

DA = (c-m)**2 - (c-m) + 1
DB = c*c + c*m - c + m*m - 2*m + 1
NA = m + c*c - c*m - c + 1
NB = c*m + c*c - c - m + 1
nA = s.Matrix([h, s.Rational(1, 2)-(c-m)])
nB = s.Matrix([h*(m-1), m/2+c-s.Rational(1, 2)])
equal('AZ edge-normal squared length', nA.dot(nA), DA)
equal('ZB edge-normal squared length', nB.dot(nB), DB)
equal('AZ support-sum lower bound', sum(points[p].dot(rot**j*nA) for j,p in enumerate(['A','Z','P']))/h, NA)
equal('ZB support-sum lower bound', sum(points[p].dot(rot**j*nB) for j,p in enumerate(['B','P','Z']))/h, NB)

posA = (q*q*((q+1-3*m)**2 + 4*m*m-2*m+1)
        + q*(1-2*m)*(6*m*m-2*m+1) + m*m*(1-2*m)**2)
posB = (q**4 + (2-2*m)*q**3 + (m*m-4*m+2)*q*q
        + (1-m)*(1-2*m)*q)
equal('AZ exact positive decomposition', (NA*NA-DA).subs(c,1-m+q), posA)
equal('ZB exact positive decomposition', (NB*NB-DB).subs(c,1-m+q), posB)
equal('AZ auxiliary quadratic positivity', 4*m*m-2*m+1, 4*(m-s.Rational(1,4))**2+s.Rational(3,4))
equal('AZ second auxiliary quadratic positivity', 6*m*m-2*m+1, 6*(m-s.Rational(1,6))**2+s.Rational(5,6))
equal('ZB numerator positivity form', NB.subs(c,1-m+q), 1-m+(1-m)*q+q*q)

# Both chart templates are unit equilateral in the oblique metric.
p, eps = s.symbols('p eps', real=True)
minus = [s.Matrix([0,1-p]), s.Matrix([1,1-p]), s.Matrix([0,-p])]
plus = [s.Matrix([p,0]), s.Matrix([p,1]), s.Matrix([p-1,0])]
def metric(v):
    return v[0]**2+v[1]**2-v[0]*v[1]
for name, vertices in [('minus',minus),('plus',plus)]:
    for i in range(3):
        equal(f'{name} template side {i+1}', metric(vertices[i]-vertices[(i+1)%3]),1)
equal('minus actual boundary sum', (p-eps)+(1-p), 1-eps)
equal('plus actual boundary sum', p+(1-p-eps), 1-eps)

Ai, Bi, Aj, Bj = s.symbols('Ai Bi Aj Bj')
ni, nj, oi = 1-Ai-Bi, 1-Aj-Bj, Aj+Bi-1
equal('forward handoff identity', Aj-Ai, ni+oi)
equal('backward handoff identity', Bi-Bj, nj+oi)
equal('multiple-ascent square completion', (1-m)**2+s.Rational(1,4)+4*m*m, 5*(m-s.Rational(1,5))**2+s.Rational(21,20))

print(f'PASS: {len(passed)} exact symbolic identities.')
for name in passed:
    print('  '+name)
