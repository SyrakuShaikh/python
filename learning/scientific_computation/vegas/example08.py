#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-17 Wed 15:17:47 Shaikh>
"""
Example of 'vegas'.
"""
import numpy as np
import vegas

@vegas.batchintegrand
def f_batch(x):
    """
    Integrand function.

    batch decorator.
    evaluate integrand at multiple points simultaneously.
    """
    # not len(x) but .shape[1]
    dim = x.shape[1]
    norm = 1013.2118364296088 ** (dim / 4.)
    dx2 = 0.0
    for d in range(dim):
        # not x[d] but [:, d] which I've never seen.
        dx2 += (x[:, d] - 0.5) ** 2
    return np.exp(-100. * dx2) * norm

integ = vegas.Integrator(4 * [[0, 1]])

integ(f_batch, nitn=10, neval=2e5)
result = integ(f_batch, nitn=10, neval=2e5)
print('result = %s     Q = %.2f' % (result, result.Q))
