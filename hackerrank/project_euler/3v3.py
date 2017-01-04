#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-04 Wed 14:30:24 Shaikh>
"""
Project Euler #3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N?

The following code (3.py) costs very much time when the given number N is large
since it generates ALL the primes. However, this problem #3 has 3 keywords:
largest, prime, factor which means it's a more specific one and thus needs a
more specific method.

clue:
1. a better implementation of sieve of Eratosthenes with the help of wheels.
2. Use a relatively small list of primes to check the number N fist
3. if failed, extend the list of primes by one prime and retest N
4. repeat 3 until find the largest prime factor
see 3v2.py for details.

clue 2:
1. The main keyword is factor not prime.
2. The computation complexity of finding all the primes not greater than N and
   testing N's factors from 1 to N differs a lot.
3. Considering a 11-digit prime P, using 3v2.py, one need to find all the primes
   that not exceed P and that is a huge mount of work compared with dividing P
   by numbers from 1 to P or sqrt(P).
see 3v3.py (this file) for details.
"""
from math import sqrt, floor

def lpf(n: int) -> int:
    """
    The largest prime factor of n.
    """
    if n < 2:
        raise ValueError('Do you know what is the Prime?')
    if n == 2:
        return 2
    while n % 2 == 0:
        n = n // 2
    i = 3
    while i <= floor(sqrt(n)):
        if n == i:
            return n
        elif n % i == 0:
            n = n // i
            continue
        else:
            i += 2
    # no return from the while loop
    # which indicate that n is a prime itself.
    return n


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lpf(n))
