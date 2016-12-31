#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-31 Sat 13:12:46 Shaikh>
"""
Project Euler #1:

If we list all the natural numbers below that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

clue:
arithmetic progression 3 6 9 12 ...
"""
def ap(n: int, base: int) -> int:
    """
    Sum the arithmetic progression starting with base and the max
    number is below n.
    """
    if base < 1:
        raise ValueError('wrong base {} in geometric progression.'.format(base))
    if n < base:
        return 0
    if base == 1:
        return n
    # find the max progression number below n
    n = n // base
    return base * ((1 + n) * n // 2)

t = int(input().strip())
for a0 in range(t):
    n_in = int(input().strip()) - 1 # below, not include.
    print(ap(n_in, 3) + ap(n_in, 5) - ap(n_in, 15))
