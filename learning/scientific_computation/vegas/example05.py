#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-16 Tue 16:20:56 Shaikh>
"""
Example of 'vegas'.
"""
import math
import vegas
import gvar as gv

def integrand(x):
    """
    Integrand function.
    """
    dx2 = 0.0
    for d in range(4):
        dx2 += (x[d] - 0.5) ** 2
    f = math.exp(-200 * dx2)
    # multi integral simultaneously, return a list.
    return [f, f * x[0], f * x[0] ** 2]

integ = vegas.Integrator(4 * [[0, 1]])

# adapt grid
training = integ(integrand, nitn=10, neval=2000)

# final analysis
result = integ(integrand, nitn=10, neval=1e4)
print('I[0] = {}   I[1] = {}   I[2] = {}'.format(*result))
print('Q = %.2f\n' % result.Q)

print('<x> = ', result[1] / result[0])
print('sigma_x^2 = <x^2> - <x>^2 = ',
      result[2] / result[0] - (result[1] / result[0]) ** 2)
print('\ncorrelation matrix:\n', gv.evalcorr(result))
