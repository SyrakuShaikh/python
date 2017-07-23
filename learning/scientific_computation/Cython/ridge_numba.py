#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# Time-stamp: <Sun, 23/07-2017 21:09:22 CST>
# Copyright (c) H.-K.Sun <spin.hk AT outlook DOT com>
"""A Sample From Vegas Tutorial."""

from numba import jit, float64
import numpy
import vegas


# Integrand: ridge of N Gaussian spread evenly along the diagonal
@jit(float64(float64), nopython=True, nogil=True)
def ridge(x):
    N = 2000
    x0 = numpy.arange(0.0, N) / (N - 1.)
    dx2 = 0.0
    for xd in x:
        dx2 += (xd - x0) ** 2
    return numpy.average(numpy.exp(-100. * dx2)) * (100. / numpy.pi) ** (len(x) / 2.)


def main():
    integ = vegas.Integrator(4 * [[0, 1]])
    # adapt
    integ(ridge, nitn=10, neval=1e4)
    # final result
    result = integ(ridge, nitn=10, neval=1e4)
    print('result = {0},  Q = {1:.2f}'.format(result, result.Q))


if __name__ == '__main__':
    main()
