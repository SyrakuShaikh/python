#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-31 Wed 16:46:12 Shaikh>
def primes(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0  # the (k+1)_th prime
    n = 2  # the first prime
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result
