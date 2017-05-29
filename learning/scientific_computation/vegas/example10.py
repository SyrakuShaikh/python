#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-29 Mon 16:24:07 Shaikh>
"""
ridge.py

test MPI support for vegas.
"""
import numpy as np
import vegas

# Integrand: ridge of  N Gaussians spread evenly along the diagonal
def ridge(x):
    N = 1000
    x0 = np.arange(0.0, N) / (N - 1.)
    dx2 = 0.0
    for xd in x:
        dx2 += (xd - x0) ** 2
    return np.average(np.exp(-100. * dx2)) * (100. / np.pi) ** (len(x) / 2.)

def main():
    integ = vegas.Integrator(4 *[[0, 1]])
    # adapt
    integ(ridge, nitn=10, neval=1e4)
    # final result
    result = integ(ridge, nitn=10, neval=1e4)
    # if integ.mpi_rank == 0:
    #     print('result = %s   Q = %.2f' % (result, result.Q))
    print('result = %s   Q = %.2f' % (result, result.Q))

if __name__ == '__main__':
    main()
