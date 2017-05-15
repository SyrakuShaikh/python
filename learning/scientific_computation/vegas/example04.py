#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-15 Mon 20:39:12 Shaikh>
"""
Example from 'vegas' Tutorial.
"""
import math
import vegas

def f_sph(x):
    """
    Define the integrand function.

    x is a list.
    """
    dx2 = 0
    for d in range(4):
        dx2 += (x[d] - 0.5) ** 2
    # restricted to a 4-D sphere of radius 0.2
    if dx2 < 0.2 ** 2:
        return math.exp(-dx2 * 100.) * 1115.3539360527281318
    else:
        return 0.0

integ = vegas.Integrator([[-1, 1], [0, 1], [0, 1], [0, 1]])

# 'alpha' controls the speed with which 'vegas' adapts.
# default value is 0.5. smaller, slower.
# Step 1 -- adapt to f; discard results
integ(f_sph, nitn=10, neval=1000, alpha=0.1)

# Step 2 -- 'integ' has adapted to f; keep results
# also, one can turn off adaption at all, using 'alpha=False'.
result = integ(f_sph, nitn=10, neval=1000, alpha=0.1)

print(result.summary())
print('result = %s     Q = %.2f' % (result, result.Q))
