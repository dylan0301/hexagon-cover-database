#!/usr/bin/env python3
"""Standalone rational algebraic verification for Case F.

All polynomials are regenerated from the fixed-start point formulas.
No stored SOS witness, Bernstein conversion, optimizer, or numerical positivity
check is used. Five explicit-model Chebyshev remainders replace six SOS targets;
one earlier curvature remainder, two increment comparisons and boundary Taylor
checks remain. This is an exact computer-assisted proof, not a formal proof
assistant certification or a fresh audit of the upstream geometric lemmas.
Run: python verify_explicit_stage.py --output verification.json
Requires only SymPy and the Python standard library. Do not run with -O.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp

m, u, d, e = sp.symbols('m u d e')
G = (m, u, d, e)
a, b = 1-m, m+u
rho = sp.expand(a*a+a*b+b*b)
K = sp.expand(4*rho-3)
KP = sp.Poly(K, *G, domain=sp.QQ)


def reduce_d(expr):
    """Canonical polynomial remainder modulo d^2=K(m,u)."""
    p = sp.Poly(expr, *G, domain=sp.QQ)
    groups = {}
    for (i, j, k, l), c in p.terms():
        table = groups.setdefault(k//2, {})
        mon = (i, j, k % 2, l)
        table[mon] = table.get(mon, 0) + c
    out = sp.Poly(0, *G, domain=sp.QQ)
    for power, table in groups.items():
        out += sp.Poly.from_dict(table, G, domain=sp.QQ) * KP**power
    return out.as_expr()


records = []


analytic_records = []


def verify_norm_hand(Hdu):
    """Verify the displayed identities used by the hand inequality proof.

    No polynomial-positivity solver is used here. The inequalities
    follow from 0<=d<=1, 0<=u<=d^2/6 and the positive groupings in the report.
    """
    h0 = (d*d+3)*(27*d**5+9*d**4+36*d**3-2*d*d-40*d+48)
    hc = [h0,
          sp.Rational(3,2)*(27*d**6-306*d**5-189*d**4-788*d**3-660*d*d+240*d-480),
          -sp.Rational(3,2)*(54*d**6+198*d**5+459*d**4-1124*d**3-1731*d*d-1356*d-1896),
          54*(21*d**4+60*d**3+89*d*d-30*d-28),
          54*(15*d**4+16*d**3-84*d*d-120*d-231),
          -648*d*(13*d+6),-216*(12*d*d+2*d-83),12960,2592]
    assert sp.expand(Hdu-sum(c*u**i for i,c in enumerate(hc))) == 0
    low_before = (2*hc[2]-6*(1512+1620*d)*u
                  -12*(12474+6480*d+4536*d*d)*u*u
                  -20*(8424*d*d+3888*d)*u**3)
    positive_difference = (6*u*(1134*d**4+3240*d**3+4806*d*d)
                          +12*u*u*(810*d**4+864*d**3)
                          +30*u**4*(17928-2592*d*d-432*d)
                          +544320*u**5+145152*u**6)
    assert sp.expand(sp.diff(Hdu,u,2)-low_before-positive_difference) == 0
    low = (5688+4068*d+3681*d*d+1752*d**3-5535*d**4
           -2754*d**5-1674*d**6-360*d**7-780*d**8)
    assert sp.expand(low_before.subs(u,d*d/6)-low) == 0
    assert 5535+2754+1674+360+780 == 11103
    assert 5688+4068+3681+1752-11103 == 4086
    neg_slope = (720-360*d+42*d*d+504*d**3-456*d**4+32*d**5
                 +sp.Rational(39,2)*d**6-51*d**7+sp.Rational(33,2)*d**8
                 -d**9+sp.Rational(11,3)*d**10+d**11/3+d**12/18
                 -sp.Rational(2,27)*d**14)
    assert sp.expand(-sp.diff(Hdu,u).subs(u,d*d/6)-neg_slope) == 0
    x = sp.Symbol('norm_x')
    endpoint_coefficients = [5044,97166,-35625,40360,4565,-17736,-11711,
                             25172,-23022,11588,-2018,-1248,1148,-470,114,-16,1]
    endpoint = sum(sp.Integer(c)*x**i for i,c in enumerate(endpoint_coefficients))
    assert sp.expand(648*Hdu.subs(u,d*d/6).subs(d,1-x)-endpoint) == 0
    # The six negative groups are absorbed by the preceding lower powers.
    assert 97166-35625 == 61541
    assert 40360-17736-11711 == 10913
    assert 25172-23022 == 2150
    assert 11588-2018-1248 == 8322
    assert 1148-470 == 678
    assert 114-16 == 98
    analytic_records.append({'name':'endpoint_norm_hand_proof',
        'H_uu_lower_bound':'4086', 'minus_H_u_at_cap_lower_bound':'360',
        'H_lower_bound':'1261/162', 'method':'displayed identities and elementary power grouping'})
    print('PASS analytic endpoint norm order',flush=True)


def verify_weighted_curvature(P, numerator, Jb,Lb,Ja,La,Eb,Ea):
    """Concavity is a positive weighted sum of squared-norm identities."""
    assert reduce_d((1+d)**3*numerator+(1-d)**3*numerator.subs(d,-d)
                    -4*rho*rho*P) == 0
    vj = reduce_d(2*Jb*Ea+Ja*Eb)
    vl = reduce_d(2*Lb*Ea-La*Eb)
    vv = reduce_d(vj*vj+3*vl*vl)
    assert reduce_d((1+d)**3*vv+(1-d)**3*vv.subs(d,-d)
                    +2*rho*rho*sp.diff(P,e,2)) == 0
    c = sp.Symbol('capacity_c')
    fm = c**4-c*c+m*c-m*m
    assert sp.expand(K.subs(u,1-c)-(4*c**4-12*c+9)+4*fm) == 0
    assert sp.expand(c**4-3*c+2-(c-1)*(c**3+c*c+c-2)) == 0
    analytic_records.append({'name':'weighted_conjugate_curvature',
        'weights':['(1+D)^3','(1-D)^3'],
        'scope':'0<=D<=1; the full integration paths satisfy this condition',
        'method':'sum of squares; no coefficient positivity test'})
    print('PASS analytic weighted-conjugate curvature',flush=True)


def taylor_coeffs(poly, center, sign=1):
    x = sp.Symbol('taylor_x')
    p = sp.Poly(poly.as_expr().subs(m,center+sign*x),x,domain=sp.QQ)
    return list(reversed(p.all_coeffs()))


def verify_B_analytic(B):
    """Two explicit polynomial proofs; no SOS witness or remainder bound."""
    x,t=sp.symbols('radial_x radial_t')
    c=[
        10*(x*x+3)*(2*x*x+3)*(3*x*x+4),
        (81*x**7+189*x**6-369*x**5-21*x**4-2596*x**3-1644*x*x-2880*x-1440)/2,
        -sp.Rational(3,4)*(711*x**6+702*x**5+705*x**4-500*x**3-3242*x*x-3728*x-2664),
        2268*x**5+1161*x**4+2454*x**3+135*x*x-3332*x-120,
        -3861*x**4-1512*x**3-2628*x*x-3648*x-874,
        12*(144*x**3+45*x*x+123*x+385),
        24*(9*x-2)*(9*x+10),
        -1728*(x+1)]
    b2=sp.Poly(B,e).coeff_monomial(e*e)
    H=sp.expand(-b2.subs(m,(1-x)/2)/16)
    assert sp.expand(H-sum(v*u**j for j,v in enumerate(c)))==0
    assert 81+189<369
    assert 711+702+705<3242
    low=sp.expand(c[0]+c[1]/6-(3332*x+120)/216+c[4]/1296
                   -sp.Rational(480,6**6)-sp.Rational(1728,6**7)*(x+1))
    expected=(sp.Rational(27,4)*x**7+sp.Rational(303,4)*x**6-sp.Rational(123,4)*x**5
              +sp.Rational(16573,48)*x**4-sp.Rational(435,2)*x**3
              +sp.Rational(17675,36)*x*x-sp.Rational(20918,81)*x
              +sp.Rational(464137,1944))
    assert sp.expand(low-expected)==0
    # Replace x^5<=x^4 and x^3<=x^2 for their negative coefficients.
    assert sp.Rational(16573,48)-sp.Rational(123,4)==sp.Rational(15097,48)>0
    assert sp.Rational(17675,36)-sp.Rational(435,2)==sp.Rational(9845,36)>270
    assert sp.Rational(20918,81)<260 and sp.Rational(464137,1944)>238
    assert sp.expand(270*x*x-260*x+238-270*(x-sp.Rational(13,27))**2)==sp.Rational(4736,27)>175

    # For e=m set x=1-2m,t=6u. Write every higher t coefficient as P_j-N_j.
    positives={
        3:(2784*x**4+2768*x**3+2049*x*x)/54,
        4:(3807*x**6+108*x**5+279*x**4+1392*x**3+118*x*x)/324,
        5:(27*x**3+291*x+65)/162,
        6:(38*x*x+106*x+37)/486,
        7:(12*x**3+6*x*x+1)/486}
    negatives={
        3:(2430*x**7+351*x**6+1932*x**5+3320*x+136)/54,
        4:(4360*x+2362)/324,
        5:(117*x**5+18*x**4+470*x*x)/162,
        6:(90*x**4+27*x**3)/486,
        7:5*x/486}
    R0=(190+1342*x+526*x*x+3118*x**3-114*x**4+1630*x**5
        -198*x**6+138*x**7-27*x**8-27*x**9)
    R1=(198970-23352*x+80802*x*x+985572*x**3-262845*x**4+810405*x**5
        -12393*x**6+110079*x**7+34992*x**8-13122*x**9)
    f0=385+(1-x)*R0/2
    fend=sp.Rational(75368,243)+(1-x)*R1/972
    f2=(70713*x**8+94770*x**6-177066*x**5-121869*x**4-436590*x**3
        +87306*x*x+57614*x+220506)/972
    lower=(1-t)*f0+t*fend-f2*t*(1-t)
    remainder=sum(positives[j]*t**j+negatives[j]*t*t*(1-t**(j-2)) for j in range(3,8))
    target=sp.expand(B.subs(e,m).subs({m:(1-x)/2,u:t/6}))
    assert sp.expand(target-lower-remainder)==0
    # All P_j,N_j are polynomials with positive displayed coefficients.
    assert all(all(co>0 for co in sp.Poly(p,x).coeffs())
               for p in [*positives.values(),*negatives.values()])
    # Explicit elementary power groupings proving R0,R1>0 on [0,1].
    assert 3118-114>0 and 1630-198>0 and 138-27-27>0
    assert 198970-23352>0 and 985572-262845>0
    assert 810405-12393>0 and 34992-13122>0
    assert 70713+94770<177066
    assert sp.Rational(87306+57614+220506,972)<400
    assert sp.Rational(75368,243)>310 and 310-sp.Rational(400,4)==210
    analytic_records.append({'name':'radical_coefficient_concavity_and_endpoint',
        'bounds':{'minus_B_e2':'>2800','B_ee':'<-5600','B_at_m':'>210'},
        'domain':'0<=m<=1/2,0<=u<=1/6',
        'method':'explicit identities, power grouping, and t(1-t)<=1/4',
        'replaced_SOS_checks':['minus_B_e2','B_at_m']})
    print('PASS analytic B_ee<-5600 and B(m,u,m)>210',flush=True)


def verify_positive_radius_derivative(P):
    """Given retained Pue>0, two explicit one-variable factorizations suffice."""
    x=sp.Symbol('radius_x')
    Pe=sp.diff(P,e)
    endpoint=sp.Rational(8,3)*(x*x+3)*(21*x**8+130*x**6+289*x**4+712*x*x+144)
    curvature=-16*(x*x+3)*(309*x**8+1450*x**6+2293*x**4+1420*x*x+144)
    assert sp.expand(Pe.subs({u:0,e:sp.Rational(1,3)}).subs(m,(1-x)/2)-endpoint)==0
    assert sp.expand(sp.diff(P,e,2).subs(u,0).subs(m,(1-x)/2)-curvature)==0
    assert sp.Rational(8,3)*3*144==1152
    analytic_records.append({'name':'positive_radius_derivative',
        'bound':'Pi_e(m,u,e)>=1152',
        'domain':'0<=m<=1/2,0<=u<=1/6,0<=e<=1/3',
        'dependency':'retained Pue_at_third and minus_P_uee imply Pue>0',
        'removed_checks':['diagonal_second_derivative','diagonal_first_at_w2'],
        'reason':'Pi_e is minimized first at u=0 and then at e=1/3; explicit even-positive polynomial there. Together with Pu>0 on u,e>=b0, this gives coordinatewise monotonicity.'})
    print('PASS analytic Pi_e>=1152 and coordinatewise monotonicity',flush=True)


def verify_affine_endpoints_hand(P):
    """Explicit univariate identities and coefficient pairings replace two SOS cores."""
    x=sp.Symbol('endpoint_x')
    T0=[5950089,6245545,3511089,508925,-3979797,-2670105,-2294523,-675504,-279300,-6864,2864,4992,832]
    target=sp.Poly(P.subs({u:0,e:m}),m).exquo(sp.Poly((2*m-1)**2,m)).as_expr()
    assert sp.expand(target.subs(m,(1-x)/3)-sp.Rational(8,19683)*sum(c*x**i for i,c in enumerate(T0)))==0
    assert sum(T0[1:4])+sum(T0[4:10])==359466>0
    # Every negative term has degree >=4. Positives of degrees 1,2,3 absorb them.
    assert all(c<0 for c in T0[4:10]) and all(c>0 for c in T0[:4]+T0[10:])
    analytic_records.append({'name':'affine_zero_endpoint_power_grouping',
        'P_at_0_m_reduced_lower_bound':str(sp.Rational(8*T0[0],19683)),
        'first_coefficients':T0,
        'method':'explicit polynomial identity and power grouping'})
    verify_sharp_third_transfer(P)
    print('PASS affine endpoints: retained zero-endpoint grouping and sharp derivative transfer',flush=True)


def verify_shared_boundary(P, nr, dr):
    """Eliminate degree-105 substitution using a quadratic and Taylor bounds.

    Diagonal monotonicity now follows from the previously retained Pu and Pue signs and explicit Pe factorization.
    All Taylor and comparison checks below are exact rational inequalities.
    They are additional checks, not included in the core-square or remainder counts.
    """
    fifth, tenth = sp.Rational(1,5),sp.Rational(1,10)
    half = sp.Rational(1,2)
    w = m*(1-m)
    q = -sp.Rational(9,10)*m*m+sp.Rational(98,125)*m-sp.Rational(3711,100000)
    phi = sp.expand(P.subs(e,u))
    phit = sp.diff(phi,u)
    # No diagonal derivative certificates: retained Pu(m,u,b0)>0 and
    # analytic Pe>=1152 imply monotonicity for u,e>=b0.
    # q>=w/2 on [1/5,1/2], by concavity and the two endpoint values.
    assert sp.diff(q-w/2,m,2) == -sp.Rational(4,5)
    assert (q-w/2).subs(m,fifth) == sp.Rational(369,100000)
    assert (q-w/2).subs(m,half) == sp.Rational(489,100000)
    # r-q = p8/(100000*(dr/8)); dr>0 is a previous analytic fact.
    p8 = (52500*m**8-198400*m**7+623911*m**6-1136733*m**5
          +1605099*m**4-1322643*m**3+596576*m*m-143288*m+14844)
    assert sp.expand(100000*(nr-q*dr)-8*p8) == 0
    left = taylor_coeffs(sp.Poly(p8,m),sp.Rational(9,25),-1)
    expected = [sp.Rational(41724222906,244140625),sp.Rational(7752554236,1953125),
                sp.Rational(8237996528,390625),sp.Rational(18407109,15625),
                sp.Rational(63701151,125),sp.Rational(4797051,25),314455,47200,52500]
    assert left == expected
    # These explicitly displayed positive numbers prove p8>0 for m<=9/25.
    assert all(c>0 for c in expected)
    pc=taylor_coeffs(sp.Poly(p8,m),sp.Rational(43,100))
    assert pc[0]>7 and abs(pc[1])<355 and pc[2]>35000
    p8_bounds={3:135000,4:466000,5:64000,6:299000,7:18000,8:52501}
    assert all(abs(pc[k])<bound for k,bound in p8_bounds.items())
    rad=sp.Rational(7,100)
    p8_tail=sum(sp.Integer(bound)*rad**(k-2) for k,bound in p8_bounds.items())
    assert p8_tail<11800
    assert sp.Rational(7)-sp.Rational(355**2,4*23200)>5
    # Phi(m,q,q), degree 27, replaces the former degree-105 numerator.
    fq=sp.Poly(sp.expand(phi.subs(u,q)),m,domain=sp.QQ)
    fw=sp.Poly(sp.expand(phi.subs(u,w/2)),m,domain=sp.QQ)
    assert fq.degree()==27 and fw.degree()==27
    # m in [0,1/5]: x=1/5-m in [0,1/5].
    cw=taylor_coeffs(fw,fifth,-1)
    assert cw[0]>103 and cw[4]>61000
    assert all(cw[k]>=0 for k in [1,2,3,*range(8,19)])
    assert abs(cw[5])<46000 and abs(cw[6])<189000 and abs(cw[7])<5000
    assert all(abs(cw[k])<6000000 for k in range(19,28))
    fw_tail=46000*fifth+189000*fifth**2+5000*fifth**3+6000000*fifth**15/(1-fifth)
    assert fw_tail<17000
    # A single Taylor lower quadratic now covers m in [1/5,1/2].
    # x=m-41/100 belongs to [-21/100,9/100]; keep the cubic asymmetry.
    cc=taylor_coeffs(fq,sp.Rational(41,100))
    assert cc[0]>sp.Rational(16,25) and abs(cc[1])<10 and cc[2]>5500
    assert -17500<cc[3]<-17400 and cc[4]>-73000
    assert abs(cc[5])<32000 and abs(cc[6])<183000 and abs(cc[7])<655000
    assert all(abs(cc[k])<6000000 for k in range(8,13))
    assert all(abs(cc[k])<34000000 for k in range(13,28))
    rr=sp.Rational(21,100)
    global_tail=(32000*rr**3+183000*rr**4+655000*rr**5
                 +6000000*sum(rr**j for j in range(6,11))
                 +34000000*rr**11/(1-rr))
    assert global_tail<1600
    tx=sp.Symbol('boundary_x')
    parabola=5500-17500*tx-73000*tx*tx-21
    assert parabola.subs(tx,-sp.Rational(21,100))==sp.Rational(59347,10)
    assert parabola.subs(tx,sp.Rational(9,100))==sp.Rational(33127,10)
    assert sp.Rational(33127,10)-1600>1700
    global_lower=sp.Rational(16,25)-sp.Rational(100,4*1700)
    assert global_lower==sp.Rational(1063,1700)>sp.Rational(3,5)
    analytic_records.append({'name':'shared_boundary_one_global_quadratic_bound',
        'claim':'Pi(m,r,r)>1063/1700 for 0<=m<=1/2',
        'q':str(q),'comparison_degree':8,'boundary_degrees':[27,27],
        'p8_tail_bound':str(p8_tail),'p8_lower_bound':'5',
        'small_m_tail_bound':str(fw_tail),'small_m_lower_bound':'103',
        'whole_q_interval':['1/5','1/2'],
        'q_global_tail_bound':str(global_tail),
        'q_global_lower_bound':str(global_lower),
        'retained_derivative_SOS_certificates':0,
        'note':'Taylor coefficient comparisons remain exact computations. No partition at m=31/100 or separate diagonal derivative checks remain.'})
    print('PASS shared boundary >1063/1700; no diagonal certificates',flush=True)


def verify_increment_and_derivative_replacements(P):
    """Two quadratic coefficient-budget bounds replace the two largest SOS targets.

    The increment estimates are exact finite coefficient computations, NOT
    computer-free theorems. Their quadratic positivity arguments are elementary.
    No new SOS witness file, optimizer, or Bernstein conversion is used.
    """
    x,s,t=sp.symbols('increment_x increment_s increment_t')
    b0=m*(1-m)/2
    Pu=sp.diff(P,u)
    Q=sp.Poly(Pu.subs(e,b0),m,u,domain=sp.QQ)
    Q0=sp.Poly(Q.as_expr().subs(u,0),m,u,domain=sp.QQ)
    R=(Q-Q0).exquo(sp.Poly(u,m,u,domain=sp.QQ)).as_expr()
    assert sp.expand(Q.as_expr()-Q0.as_expr()-u*R)==0
    # A completely explicit nonnegative remainder on 0<=x<=1.
    A=-2985+503*x+sp.Rational(12515,2)*x*x
    nonnegative=(83782*x**4+64114*x**6+18944*x**8+2828*x**10
        +114234*x**2*(1-x)+189651*x**4*(1-x)
        +122145*x**6*(1-x)+45336*x**8*(1-x)
        +13312*x**10*(1-x)+732*x**10*(1-x*x)
        +3201*x**12*(1-x)+189*x**12*(1-x*x)
        +81*x**12*(1-x**3))
    assert sp.expand(8*(Q0.as_expr().subs(m,(1-x)/2)-A)-nonnegative)==0
    charts=[
        (sp.Rational(0),sp.Rational(1,4),
         4600*s*s+4700*s*t-5400*s-720*t*t-10700*t,sp.Integer(43400),
         sp.Rational(51047093775242087,1174136684544)),
        (sp.Rational(1,4),sp.Rational(1,2),
         11510*s*s+13385*s*t+19015*s+2171*t*t+5125*t,sp.Integer(40580),
         sp.Rational(95304134251780469,2348273369088))]
    local=[]
    for lo,hi,core,claimed_margin,expected_margin in charts:
        chart=sp.Poly(R.subs({m:(lo+hi)/2+(hi-lo)*s/2,u:(1+t)/12}),s,t,domain=sp.QQ)
        rem=sp.Poly(chart.as_expr()-core,s,t,domain=sp.QQ)
        constant=rem.coeff_monomial(1)
        signed_sum=sp.Rational(0); good=0; bad=0; positive_parts=0
        for (i,j),c in rem.terms():
            if i+j==0:continue
            if c>0 and i%2==0 and j%2==0:
                good+=1;positive_parts+=c*s**i*t**j
            else:
                bad+=1;signed_sum+=abs(c)
                sign=1 if c>0 else -1
                positive_parts+=abs(c)*(1+sign*s**i*t**j)
        epsilon=constant-signed_sum
        assert epsilon==expected_margin and epsilon>claimed_margin
        assert sp.expand(chart.as_expr()-core-epsilon-positive_parts)==0
        local.append({'m_interval':[str(lo),str(hi)],'quadratic':str(core),
            'coefficient_budget_constant':str(constant),'signed_coefficient_sum':str(signed_sum),
            'exact_margin':str(epsilon),'used_lower_constant':str(claimed_margin),
            'positive_even_monomials':good,'signed_monomials':bad,
            'target_degree':int(chart.total_degree()),
            'target_bidegree':[int(v) for v in chart.degree_list()],
            'target_terms':len(chart.terms()),
            'target_sha256':sha256(str(chart.terms()).encode()).hexdigest()})
    # Minimize in s by completing a square; the remaining t-quadratic is concave.
    floor1=43400-720*t*t-10700*t-(4700*t-5400)**2/sp.Integer(18400)
    floor2=40580+2171*t*t+5125*t-(19015+13385*t)**2/sp.Integer(46040)
    assert sp.diff(floor1,t,2)<0 and sp.diff(floor2,t,2)<0
    assert min(floor1.subs(t,-1),floor1.subs(t,1))==sp.Rational(1469855,46)>31900
    assert min(floor2.subs(t,-1),floor2.subs(t,1))==sp.Rational(28861276,1151)>25000
    # For U>=b0, Q >= A+25000 U >= this positive polynomial.
    restricted_lower=140+503*x+sp.Rational(6265,2)*x*x
    assert sp.expand(A+25000*(1-x*x)/8-restricted_lower)==0

    # The new quadratic Chebyshev model proves Pue>20000 at e=1/3;
    # H1=-PUee>0 transfers this to all 0<=e<=1/3.
    source=next(v for v in records if v['name']=='Pue')
    assert sp.Rational(source['target_lower_bound'])>=20000
    global_lower=A+20000*(sp.Rational(1,3)-(1-x*x)/8)
    displayed_lower=sp.Rational(3545,3)+503*x+sp.Rational(52545,6)*x*x
    assert sp.expand(global_lower-displayed_lower)==0
    assert sp.Rational(3545,3)>1180
    analytic_records.append({'name':'increment_and_derivative_replacements',
        'increment_quotient':'R=[Pi_U(m,U,b0)-Pi_U(m,0,b0)]/U, extended polynomially at U=0',
        'increment_lower_bound':'>25000','increment_charts':local,
        'Pu_at_b0_restricted_bound':'>=140+503*x+(6265/2)*x^2+25000*(U-b0), x=1-2m',
        'Pu_at_third_global_bound':'>3545/3+503*x+(52545/6)*x^2>1180',
        'global_third_dependencies':['Pue>20000','H1=-Pi_Uee>0'],
        'new_coefficient_checks':2,
        'note':'The two increment remainder bounds are retained exact coefficient computations.'})
    print('PASS increment R>25000; restricted Pu>=140; simplified global Pu at third>1180',flush=True)


def verify_sharp_third_transfer(P):
    """Independent direct coefficient-dominance proof on m>=1/3.

    This optional strengthening also replaces the old large-integer endpoint
    pairing. It uses explicit U coefficients and 0<=x<=1/3, not an SOS file.
    """
    x=sp.Symbol('sharp_x'); third=sp.Rational(1,3)
    Pu=sp.diff(P,u)
    poly=sp.Poly(sp.expand(Pu.subs({m:(1-x)/2,e:third})),u)
    assert poly.degree()==10
    # For every negative odd coefficient, x^(2j+1)<=x^(2j)/3.
    def group_odd(q, keep_linear=False):
        out=0
        for (i,),c in sp.Poly(q,x).terms():
            if c<0 and i%2 and not(keep_linear and i==1):
                out+=c*x**(i-1)/3
            else:out+=c*x**i
        return sp.Poly(sp.expand(out),x)
    low0=group_odd(poly.nth(0),True)
    expected0=(10880-sp.Rational(13376,3)*x+sp.Rational(1193024,27)*x*x
               +sp.Rational(563908,9)*x**4+sp.Rational(1294762,27)*x**6
               +sp.Rational(189044,9)*x**8+5838*x**10+828*x**12)
    assert sp.expand(low0.as_expr()-expected0)==0
    a=sp.Rational(1193024,27); b=sp.Rational(13376,3)
    min0=sp.Rational(10880)-b*b/(4*a)
    assert min0==sp.Rational(200717392,18641)>10700
    claims=[None,sp.Integer(34000),sp.Integer(0),sp.Integer(-500000),sp.Integer(0),
            sp.Integer(0),sp.Integer(-3000000),sp.Integer(-2000000),sp.Integer(0),
            sp.Integer(0),sp.Integer(0)]
    rows=[]
    for j in range(1,11):
        lj=group_odd(poly.nth(j))
        # Positive terms can be dropped; remaining negative powers are bounded at x=1/3.
        bound=lj.coeff_monomial(1)+sum(c*third**i for (i,),c in lj.terms() if i>0 and c<0)
        assert bound>=claims[j],(j,bound,claims[j])
        rows.append({'U_power':j,'grouped_polynomial':str(lj.as_expr()),
                     'exact_scalar_bound':str(bound),'used_bound':str(claims[j])})
    u_margin=sp.Rational(34000)-sp.Rational(500000,36)-sp.Rational(3000000,6**5)-sp.Rational(2000000,6**6)
    assert u_margin==sp.Rational(14348500,729)>0
    p0=(3159*x**14+26163*x**12+126501*x**10+376529*x**8
        +664736*x**6+603680*x**4+160512*x*x-6912)/72
    assert sp.expand(P.subs({m:(1-x)/2,u:0,e:third})-p0)==0
    par=-96+sp.Rational(6688,3)*x*x+sp.Rational(10700,18)*(1-3*x)
    assert sp.diff(par,x).subs(x,third)==-sp.Rational(2674,9)<0
    assert sp.diff(par,x,2)>0
    assert par.subs(x,third)==sp.Rational(4096,27)>151
    analytic_records.append({'name':'sharp_endpoint_derivative_and_transfer',
        'domain':'1/3<=m<=1/2,0<=U<=1/6','Pu_at_third_bound':'>10700',
        'stronger_constant_coefficient_bound':str(min0),'U_increment_margin':str(u_margin),
        'coefficient_rows':rows,
        'endpoint_domain':'U>=(m-1/3)/3','endpoint_value_bound':'>=4096/27>151',
        'removed_old_check':'degree-14 affine endpoint integer-pairing expansion',
        'note':'Direct exact coefficient dominance; additional to the two quadratic remainder comparisons.'})
    print('PASS direct Pu at third>10700 on m>=1/3; affine endpoint>=4096/27',flush=True)


def chebyshev_coefficients(poly):
    """Convert an exact bivariate polynomial to the tensor Chebyshev basis.

    For n>=1, z^n = 2^(1-n) sum_{j<n/2} binom(n,j) T_{n-2j}(z),
    plus 2^(-n) binom(n,n/2) if n is even. No numerical transform is used.
    """
    from math import comb
    cache = {0: {0: sp.Integer(1)}}
    def powers(n):
        if n not in cache:
            ans = {n-2*j: sp.Rational(comb(n,j), 2**(n-1))
                   for j in range((n-1)//2+1)}
            if n % 2 == 0:
                ans[0] = sp.Rational(comb(n,n//2), 2**n)
            cache[n] = ans
        return cache[n]
    result = {}
    for (i,j), c in poly.terms():
        for p, ap in powers(i).items():
            for q, bq in powers(j).items():
                result[p,q] = result.get((p,q), sp.Integer(0)) + c*ap*bq
    return {ij: c for ij,c in result.items() if c != 0}


def verify_cubic_curvature(P):
    """Prove -S_ell(1/3)>21500 on the whole rectangle by a cubic model.

    The proof has one exact, canonical Chebyshev-coefficient remainder check.
    The cubic's positivity uses a displayed completed-square/product identity.
    No stored SOS witness is consulted by this function.
    """
    s,t,X,Y = sp.symbols('cheb_s cheb_t corner_X corner_Y')
    third = sp.Rational(1,3)
    ell = (1+5*m)/2
    k0 = 1+m/2+2*m*m
    assert sp.expand(k0-ell-2*(m-sp.Rational(1,2))**2) == 0
    assert ell.subs(m,0) == sp.Rational(1,2)

    H = sp.expand(-sp.diff(P,u,2).subs(e,third)
                  +2*ell*sp.diff(P,u,e).subs(e,third)
                  -ell**2*sp.diff(P,e,2))
    F = sp.Poly((H/100).subs({m:(1+s)/4,u:(1+t)/12}),s,t,domain=sp.QQ)
    coefficients = chebyshev_coefficients(F)
    reconstructed = sum(c*sp.chebyshevt(i,s)*sp.chebyshevt(j,t)
                        for (i,j),c in coefficients.items())
    assert sp.Poly(reconstructed-F.as_expr(),s,t,domain=sp.QQ).is_zero
    assert F.total_degree() == 14
    assert len(coefficients) == 113

    # Exact interval norm proof: |T_n(z)|<=1 follows from this identity.
    for n in range(1, max(max(ij) for ij in coefficients)+1):
        assert sp.expand(sp.chebyshevt(n,s)**2
                         +(1-s*s)*sp.chebyshevu(n-1,s)**2-1) == 0

    cubic_coefficients = {
        (0,0):679, (1,0):-23, (0,1):197,
        (2,0):-92, (1,1):226, (0,2):-17,
        (3,0):19, (2,1):-80, (1,2):52, (0,3):-2,
    }
    g = sp.expand(sum(c*sp.chebyshevt(i,s)*sp.chebyshevt(j,t)
                      for (i,j),c in cubic_coefficients.items()))
    displayed = (76*s**3-160*s*s*t-184*s*s+104*s*t*t+226*s*t
                 -132*s-8*t**3-34*t*t+283*t+788)
    assert sp.expand(g-displayed) == 0

    low_error = sum(abs(coefficients.get(ij,0)-c)
                    for ij,c in cubic_coefficients.items())
    groups = {
        'degree_4':sum(abs(c) for ij,c in coefficients.items() if sum(ij)==4),
        'degree_5':sum(abs(c) for ij,c in coefficients.items() if sum(ij)==5),
        'degree_6':sum(abs(c) for ij,c in coefficients.items() if sum(ij)==6),
        'degree_7':sum(abs(c) for ij,c in coefficients.items() if sum(ij)==7),
        'degrees_8_to_14':sum(abs(c) for ij,c in coefficients.items() if sum(ij)>=8),
    }
    bounds = {'degree_4':sp.Integer(38),'degree_5':sp.Rational(17,2),
              'degree_6':sp.Rational(15,4),'degree_7':sp.Rational(1,2),
              'degrees_8_to_14':sp.Rational(17,100)}
    assert low_error < sp.Rational(31,10)
    for name,value in groups.items():
        assert value < bounds[name], (name,value,bounds[name])
    tail_bound = sp.Rational(31,10)+sum(bounds.values())
    exact_error = low_error+sum(groups.values())
    assert tail_bound == sp.Rational(2701,50) < 55
    assert exact_error < tail_bound

    # All displayed products are nonnegative on 0<=X,Y<=2.
    # Thus the identity proves g>=270+87/208, without coefficient estimates.
    corner = sp.expand(g.subs({s:1-X,t:Y-1}))
    positive = (52*(X-sp.Rational(37,104))**2+sp.Rational(87,208)
                +76*X*X*(2-X)+sp.Rational(111,4)*X*(4-Y*Y)
                +Y*(sp.Rational(185,4)*(2-X)*(2-Y)
                    +sp.Rational(149,4)*X*(2-Y)
                    +sp.Rational(341,4)*(2-X)*Y
                    +160*X*(2-X)+8*Y*(2-Y)))
    assert sp.expand(corner-270-positive) == 0
    # Cruder round bound used by the report: F>270-55=215, H>21500.
    assert 100*(270-sp.Integer(55)) == 21500

    analytic_records.append({
        'name':'affine_curvature_cubic_Chebyshev_replacement',
        'target':'-Pi_UU(m,u,1/3)+2*ell*Pi_Ue(m,u,1/3)-ell^2*Pi_ee(m,u)',
        'ell':str(ell),'slope_identity':'kappa0-ell=2*(m-1/2)^2',
        'domain':'0<=m<=1/2; 0<=u<=1/6',
        'target_degree':14,'normalization':'F=target/100',
        'chart':{'m':'(1+s)/4','u':'(1+t)/12'},
        'cubic_model':str(g),'model_lower_bound':'270+87/208',
        'low_degree_coefficient_error':str(low_error),
        'tail_group_sums':{k:str(v) for k,v in groups.items()},
        'tail_group_bounds':{k:str(v) for k,v in bounds.items()},
        'exact_total_coefficient_error':str(exact_error),
        'total_error_bound':str(tail_bound),
        'strict_target_lower_bound':'21500',
        'coefficient_count':len(coefficients),'model_coefficient_count':10,
        'higher_degree_coefficient_count':len(coefficients)-10,
        'canonical_coefficients':[[i,j,str(c)] for (i,j),c in sorted(coefficients.items())],
        'coefficient_sha256':sha256(str(sorted(coefficients.items())).encode()).hexdigest(),
        'note':'This exact coefficient-remainder calculation replaces, not conceals, the removed SOS check. Prior increment and boundary Taylor computations remain.',
    })
    print('PASS analytic affine curvature >21500: simpler slope; cubic product identity; exact Chebyshev remainder',flush=True)


# New proof routines. These are inserted into the standalone verifier.

def check_uniform_model(name, target, model, s, t, scale, error_bound):
    """Exact tensor-Chebyshev l1 remainder; no witness file or optimizer.

    The input target is defined from the geometric polynomials, not coefficient
    data. All coefficients output below are regenerated using rational arithmetic.
    """
    F = sp.Poly((target/scale).subs({m:(1+s)/4,u:(1+t)/12}),s,t,domain=sp.QQ)
    coefficients = chebyshev_coefficients(F)
    model_poly = sp.Poly(model,s,t,domain=sp.QQ)
    model_coefficients = chebyshev_coefficients(model_poly)
    keys = set(coefficients) | set(model_coefficients)
    error = sum(abs(coefficients.get(ij,0)-model_coefficients.get(ij,0)) for ij in keys)
    assert error < error_bound, (name,error,error_bound)
    reconstructed = sum(c*sp.chebyshevt(i,s)*sp.chebyshevt(j,t)
                        for (i,j),c in coefficients.items())
    assert sp.Poly(reconstructed-F.as_expr(),s,t,domain=sp.QQ).is_zero
    for n in range(1,max(max(ij) for ij in keys)+1):
        assert sp.expand(sp.chebyshevt(n,s)**2+(1-s*s)*sp.chebyshevu(n-1,s)**2-1)==0
    record = {
        'name':name, 'method':'explicit_model_plus_exact_Chebyshev_error',
        'domain':'0<=m<=1/2, 0<=u<=1/6',
        'scale':str(scale), 'model':str(model),
        'target_degree':int(F.total_degree()),
        'model_degree':int(model_poly.total_degree()),
        'target_bidegree':list(map(int,F.degree_list())),
        'canonical_coefficient_count':len(coefficients),
        'coefficient_error_terms':len(keys),
        'exact_uniform_error':str(error),'used_error_bound':str(error_bound),
        'canonical_coefficients':[[i,j,str(c)] for (i,j),c in sorted(coefficients.items())],
        'coefficient_sha256':sha256(str(sorted(coefficients.items())).encode()).hexdigest(),
    }
    records.append(record)
    return record


def verify_uniform_B_endpoint(B):
    """B(m,u,b0)>4 on the whole rectangle: one cubic, no q split."""
    s,t=sp.symbols('B_s B_t')
    b0=m*(1-m)/2
    g=(-292*s**3+556*s*s*t+1504*s*s+364*s*t*t-317*s*t
       -1795*s-28*t**3+272*t*t-389*t+804)/10
    record=check_uniform_model('B_at_b0_uniform',B.subs(e,b0),g,s,t,
                               sp.Integer(1),sp.Rational(17,2))
    assert sp.Rational(record['exact_uniform_error'])==sp.Rational(1351198806043,163074539520)
    # On s<=0, g_ss>0 and g_s(0,t)<0 imply g(s,t)>=g(0,t).
    assert sp.expand(sp.diff(g,s,2)-(1504-876*s+556*t)/5)==0
    assert (sp.Integer(1504)-876-556)/5==sp.Rational(72,5)>0
    assert sp.expand(sp.diff(g,s).subs(s,0)-(364*t*t-317*t-1795)/10)==0
    assert (sp.Integer(364)+317-1795)/10==sp.Rational(-557,5)<0
    assert sp.expand(g.subs(s,0)-(804-389*t+272*t*t-28*t**3)/10)==0
    assert (sp.Integer(804)-389-28)/10==sp.Rational(387,10)>sp.Rational(25,2)

    # On 0<=s<=1, the Hessian minus 8 I is affine in (s,t).
    # Its four vertex values are positive definite; their convex combination is
    # the matrix everywhere on this rectangle.
    matrix=sp.expand(10*(sp.hessian(g,(s,t))-8*sp.eye(2)))
    vertices={
        (0,-1):sp.Matrix([[1816,-1045],[-1045,632]]),
        (0,1):sp.Matrix([[4040,411],[411,296]]),
        (1,-1):sp.Matrix([[64,67],[67,1360]]),
        (1,1):sp.Matrix([[2288,1523],[1523,1024]])}
    weights={(0,-1):(1-s)*(1-t)/2,(0,1):(1-s)*(1+t)/2,
             (1,-1):s*(1-t)/2,(1,1):s*(1+t)/2}
    interpolation=sp.zeros(2)
    matrices=[]
    for vertex,expected in vertices.items():
        actual=matrix.subs({s:vertex[0],t:vertex[1]})
        assert actual==expected and actual[0,0]>0 and actual.det()>0
        interpolation+=weights[vertex]*actual
        matrices.append({'vertex':list(vertex),'matrix':[[str(z) for z in row] for row in actual.tolist()],
                         'determinant':str(actual.det())})
    assert (matrix-interpolation).applyfunc(sp.expand)==sp.zeros(2)
    # Strong convexity about z0=(2/3,1/3):
    # g(z)>=g(z0)+grad g(z0).(z-z0)+4||z-z0||^2.
    z0={s:sp.Rational(2,3),t:sp.Rational(1,3)}
    g0=g.subs(z0)
    grad=sp.Matrix([sp.diff(g,s).subs(z0),sp.diff(g,t).subs(z0)])
    assert g0==sp.Rational(383,30)
    assert grad==sp.Matrix([sp.Rational(13,45),sp.Rational(-35,18)])
    floor=sp.factor(g0-(grad.dot(grad))/16)
    assert floor==sp.Rational(1623259,129600)>sp.Rational(25,2)
    assert sp.Rational(25,2)-sp.Rational(17,2)==4
    record.update({'model_lower_bound':'25/2','target_lower_bound':'4',
                   'Hessian_vertex_matrices':matrices,
                   'right_half_strong_convexity_lower_bound':str(floor),
                   'consequence':'B(m,u,e)>4 for b0<=e<=m, by the retained B_ee<0 and B(m,u,m)>210.'})
    print('PASS uniform B endpoint >4: one cubic, four 2x2 matrices, exact Chebyshev error',flush=True)


def verify_four_mixed_models(P):
    """Four related signs via explicit quadratic identities and exact errors."""
    s,t=sp.symbols('mixed_s mixed_t')
    third=sp.Rational(1,3)
    Uee=sp.diff(P,u,e,2)
    UUe=sp.diff(P,u,2,e)
    definitions=[
        ('H1',-Uee,(130,80,-124,52,100,454),70,250000),
        ('H2',UUe.subs(e,0)-2*Uee,(466,414,124,238,771,1379),300,500000),
        ('H3',UUe.subs(e,third)-2*Uee,(286,228,-202,154,348,1090),176,550000),
        ('Pue',sp.diff(P,u,e).subs(e,third),(18,4,-14,6,17,44),8,20000),
    ]
    for name,target,parameters,error_bound,claimed_lower in definitions:
        aa,bb,cc,dd,ee,ff=map(sp.Integer,parameters)
        model=aa*s*s+bb*s*t+cc*s+dd*t*t+ee*t+ff
        record=check_uniform_model(name,target,model,s,t,sp.Integer(1000),sp.Integer(error_bound))
        gamma=sp.factor(dd-bb*bb/(4*aa))
        delta=sp.factor(ee-bb*cc/(2*aa)-2*gamma)
        floor=sp.factor(ff-ee+dd-(cc-bb)**2/(4*aa))
        rhs=aa*(s+(bb*t+cc)/(2*aa))**2+gamma*(t+1)**2+delta*(t+1)+floor
        assert sp.expand(model-rhs)==0
        assert aa>0 and gamma>0 and delta>0
        assert 1000*(floor-error_bound)>=claimed_lower
        record.update({'model_lower_bound':str(floor),'target_lower_bound':str(claimed_lower),
                       'quadratic_parameters':list(map(str,parameters)),
                       'completed_square_gamma':str(gamma),'linear_generator_weight':str(delta)})
        print(f'PASS {name}: quadratic model; exact Chebyshev error; target>{claimed_lower}',flush=True)
    analytic_records.append({'name':'mixed_derivative_transfer',
        'identity':'S_kappa,e=(1-3e)H2+3e H3+2(kappa-1)H1',
        'domain':'0<=e<=1/3, kappa>=1',
        'Pue_transfer':'H1=-Pi_Uee>0 implies Pi_Ue(m,u,e)>=Pi_Ue(m,u,1/3)>20000'})


def verify():
    records.clear()
    analytic_records.clear()
    # A1/rho, B1/rho, G1/rho, D1/rho are the normalized line coefficients.
    A1 = (b+2*a-b*d)/2
    B1 = (b-a+(a+b)*d)/2
    G1 = (-b+a+(a+b)*d)/2
    D1 = (2*b+a-a*d)/2
    assert reduce_d(A1*A1+A1*B1+B1*B1-rho*rho) == 0
    assert reduce_d(D1*D1+D1*G1+G1*G1-rho*rho) == 0
    assert sp.expand((a+b)*A1+b*B1-rho) == 0
    assert sp.expand((a+b)*D1+a*G1-rho) == 0

    nb, na = 12*b*b-12*b+7, 12*a*a-12*a+7
    Eb, Ea = sp.expand(8*rho-12*u*A1), sp.expand(8*rho-12*u*D1)
    Jb = sp.expand((1-2*b)*Eb+(A1+2*B1)*nb)
    Lb = sp.expand(Eb-A1*nb)
    Ja = sp.expand((1-2*a)*Ea+(D1+2*G1)*na)
    La = sp.expand(Ea-D1*na)

    # Independent consistency checks with the original Cartesian point map.
    AX = sp.expand((b-2)*Eb+(A1-B1)*nb)  # 2 Eb times x_A
    AY = sp.expand(-b*Eb+(A1+B1)*nb)    # Eb times y_A/h
    CX = sp.expand((a-2)*Ea+(D1-G1)*na)
    CY = sp.expand(a*Ea-(D1+G1)*na)
    assert sp.expand(2*AX+Jb+3*Lb) == 0
    assert sp.expand(2*AY-Jb+Lb) == 0
    assert sp.expand(2*CX+Ja+3*La) == 0
    assert sp.expand(2*CY+Ja-La) == 0

    bilinear = reduce_d(Jb*La+Ja*Lb)
    numerator = reduce_d(
        bilinear**2-((1-2*e)*Jb*Ea-e*Ja*Eb)**2
        -3*((1-2*e)*Lb*Ea+e*La*Eb)**2)
    core = sp.Poly(numerator, *G, domain=sp.QQ).exquo(
        sp.Poly(2*rho*rho, *G, domain=sp.QQ)).as_expr()
    pd = sp.Poly(core, d)
    assert pd.degree() == 1
    A, B = pd.coeff_monomial(1), pd.coeff_monomial(d)
    P = sp.expand((1+3*K)*A+K*(3+K)*B)
    assert sp.expand(d*(1+3*d*d)-d*d*(3+d*d)-d*(1-d)**3) == 0

    # Exact endpoint-norm ordering: N_A-N_C = 8 u z rho^2 H/(Eb^2 Ea^2).
    norm_num = reduce_d((Jb*Jb+3*Lb*Lb)*Ea**2
                        -(Ja*Ja+3*La*La)*Eb**2)
    H = sp.Poly(norm_num, *G, domain=sp.QQ).exquo(
        sp.Poly(-32*u*(u+2*m-1)*rho*rho, *G, domain=sp.QQ)).as_expr()
    z, t = sp.symbols('z t')
    Hz = sp.Poly(sp.expand(H.subs(m, (1-u-z)/2)), z,
                 domain=sp.QQ[u, d]).rem(
        sp.Poly(z*z-(d*d-6*u-3*u*u), z, domain=sp.QQ[u, d]))
    assert Hz.degree() == 0
    Hdu = Hz.as_expr()
    norm_chart = sp.Poly(Hdu.subs(u, d*d*t/6), d, t, domain=sp.QQ)
    verify_norm_hand(Hdu)

    # The rational radial lower bound established in the preceding report.
    w = m*(1-m)
    nr = sp.expand(w*(4-w)*(3*w*w-4*w+4))
    dr = sp.expand(8*(4+2*m-10*w+6*w*w-w**3))
    N, L = sp.Poly(nr, m, u), sp.Poly(dr, m, u)
    k0 = 1+m/2+2*m*m
    H7 = 12*m**7-45*m**6+136*m**5-238*m**4+312*m**3-249*m**2+164*m+4
    assert sp.expand((m*dr-nr)-k0*nr-m**3*H7/2) == 0

    # One uniform polynomial lower endpoint replaces both former B endpoints.
    # The q comparison is retained only in the shared-boundary proof below.
    verify_B_analytic(B)
    verify_uniform_B_endpoint(B)

    Pu = sp.diff(P, u)
    Puu = sp.diff(P, u, 2)
    Pue = sp.diff(P, u, e)
    Pee = sp.diff(P, e, 2)
    PUee = sp.diff(P, u, e, e)
    PUUe = sp.diff(P, u, u, e)
    third = sp.Rational(1, 3)

    # Concavity along e=m-kappa u when 0<=e<=1/3, kappa>=k0>=1.
    verify_weighted_curvature(P,numerator,Jb,Lb,Ja,La,Eb,Ea)
    verify_four_mixed_models(P)
    verify_positive_radius_derivative(P)
    # Since Pee<0 on physical integration paths, S_kappa<0 for kappa>=0.
    # The new slope is the endpoint tangent to kappa0, with a one-square gap.
    # The curvature bound is proved by a cubic and one canonical coefficient check.
    verify_cubic_curvature(P)

    # Constant-radius region: certify Pu directly on u>=b0, not Puu at r.
    # The extra generator is nonnegative on this exact application domain.
    verify_increment_and_derivative_replacements(P)
    analytic_records.append({'name':'direct_constant_radius_monotonicity',
        'lower_radius':'b0=m*(1-m)/2',
        'extra_constraint':'u>=b0',
        'implication':'u>=r>=b0 and Pue>0 imply Pu(m,u,r)>=Pu(m,u,b0)>0',
        'deleted_checks':['P_uu_at_r','P_u_at_w_over_2']})

    # Shared boundary: no high-degree rational substitution.
    verify_shared_boundary(P,nr,dr)

    # Left endpoint of the affine interval, when m<=1/3.
    start = sp.Poly(sp.expand(P.subs({u: 0, e: m})), m)
    start = start.exquo(sp.Poly((2*m-1)**2, m))
    verify_affine_endpoints_hand(P)

    # Left endpoint when m>=1/3: u_3=(m-1/3)/kappa >= (m-1/3)/3.
    # No P_u_at_third SOS check: both global and sharp local bounds were proved above.

    assert len(records) == 5
    assert all(r['method']=='explicit_model_plus_exact_Chebyshev_error' for r in records)
    assert sum(r['canonical_coefficient_count'] for r in records)==383
    return {
        'claim':'Both fixed-start tangent residuals are positive at e0 when e0<=1/3, on the strict reflected F domain, conditional on the preserved geometric lemmas.',
        'scope':'Complete modified algebraic verifier; not a fresh independent audit of all upstream geometric arguments.',
        'arithmetic':'Exact rational polynomial identities, five new model Chebyshev errors, one retained curvature Chebyshev error, two retained increment coefficient bounds, retained Taylor comparisons.',
        'base_report_repository_revision':'e255ed51d54c3f005dc9c5764e8ee3736cd06946',
        'sympy_version':sp.__version__,
        'stored_SOS_witness_count':0,
        'bernstein_sign_check_count':0,
        'new_model_checks':len(records),
        'new_model_coefficient_count':sum(r['canonical_coefficient_count'] for r in records),
        'retained_curvature_Chebyshev_coefficient_count':113,
        'retained_increment_nonconstant_remainder_count':208,
        'models':records,
        'analytic_reductions':analytic_records,
    }


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: this exact verifier uses assertions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('verification.json'))
    args = parser.parse_args()
    answer = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(answer, indent=2)+'\n', encoding='utf-8')
    print("ALL PASSED: no stored SOS witness; 5 explicit-model Chebyshev checks; "
          "uniform B>4; four quadratic mixed-derivative bounds; "
          "prior curvature, increment and Taylor checks retained.")



if __name__ == '__main__':
    main()
