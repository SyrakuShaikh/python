#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-15 Mon 15:30:55 Shaikh>
"""
Example from 'vegas' Tutorial.
"""
import math
import vegas

def f(x):
    """
    Define the integrand function.

    x is a list.
    """
    dx2 = 0
    for d in range(4):
        dx2 += (x[d] - 0.5) ** 2
    return math.exp(-dx2 * 100.) * 1013.2118364296088

integ = vegas.Integrator([[-1, 1], [0, 1], [0, 1], [0, 1]])

result = integ(f, nitn=10, neval=1000)
print(result.summary())
print('result = %s     Q = %.2f' % (result, result.Q))
