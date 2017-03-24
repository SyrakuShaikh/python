#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-23 Thu 19:14:51 Shaikh>
"""
Project Euler #7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that
the 6th prime is 13. What is the Nth prime number?
"""
from math import sqrt, ceil
WHEELS = [2, 3, 5, 7, 11, 13, 17, 19]

def sieve(total: int):
    global WHEELS
    current = WHEELS[-1] + 2
    while len(WHEELS) < total:
        test = ceil(sqrt(current))
        for w in WHEELS:
            if test < w:
                WHEELS.append(current)
                break
            elif current % w == 0:
                break
        current += 2
    return WHEELS[total-1]


T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    print(sieve(n))
