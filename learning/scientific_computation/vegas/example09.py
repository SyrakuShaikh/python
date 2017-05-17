#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-17 Wed 15:55:42 Shaikh>
"""
Example of 'vegas'.
"""
import numpy as np
import vegas

class f_batch(vegas.BatchIntegrand):
    """
    Integrand function.

    batch decorator.
    evaluate integrand at multiple points simultaneously.
    """
    def __init__(self, dim):
        self.dim = dim
        self.norm = 1013.2118364296088 ** (dim / 4.)

    def __call__(self, x):
        dx2 = 0.0
        for d in range(self.dim):
            # not x[d] but [:, d] which I've never seen.
            dx2 += (x[:, d] - 0.5) ** 2
        return np.exp(-100. * dx2) * self.norm

f = f_batch(dim=4)
integ = vegas.Integrator(f.dim * [[0, 1]])

integ(f, nitn=10, neval=2e5)
result = integ(f, nitn=10, neval=2e5)
print('result = %s     Q = %.2f' % (result, result.Q))
