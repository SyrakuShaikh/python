#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-17 Wed 15:01:21 Shaikh>
"""
Example of 'vegas'.
"""
import math
import vegas

def f(x):
    """
    Integrand function.
    """
    dim = len(x)
    norm = 1013.2118364296088 ** (dim / 4.)
    dx2 = 0.0
    for d in range(dim):
        dx2 += (x[d] - 0.5) ** 2
    return math.exp(-100. * dx2) * norm

integ = vegas.Integrator(4 * [[0, 1]])

integ(f, nitn=10, neval=2e5)
result = integ(f, nitn=10, neval=2e5)
print('result = %s     Q = %.2f' % (result, result.Q))
