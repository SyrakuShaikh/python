#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-04 Wed 14:22:06 Shaikh>
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
see 3v2.py (this file) for details.

clue 2:
1. The main keyword is factor not prime.
2. The computation complexity of finding all the primes not greater than N and
   testing N's factors from 1 to N differs a lot.
3. Considering a 11-digit prime P, using 3v2.py, one need to find all the primes
   that not exceed P and that is a huge mount of work compared with dividing P
   by numbers from 1 to P or sqrt(P).
see 3v3.py for details.
"""
from math import sqrt, floor

def sieveE(w: list) -> list:
    """
    Using Sieve of Eratosthenes to generate list of wheels by one prime.
    """
    # a prime must be odd.
    nextp = w[-1] + 2
    while True:
        found = True
        for p in w:
            if nextp % p == 0:
                nextp += 2
                found = False
                break
        if found:
            break
    return w + [nextp]


def sieveEra(w: list, n: int) -> list:
    """
    Sieve of Eratosthenes with wheels.
    """
    if n <= w[-1] + 1:
        return w
    while n > w[-1]:
        w = sieveE(w)
    return w


def lpf(n: int, inx: int = 0) -> int:
    """
    Largest Prime Factor of n.
    """
    global wheels
    while inx < len(wheels):
        base = wheels[inx]
        if n <= base:
            return base, inx
        elif n % base == 0:
            n = n // base
        else:
            inx += 1
    return n, inx


wheels = [2, 3, 5, 7, 11, 13, 17, 19, 23]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest, pos = lpf(n)

    # the largest is greater than wheels[-1]
    while pos == len(wheels):
        fs = floor(sqrt(largest))
        # the reduced n, i.e. largest is the product of
        # +larger primes than wheels[-1]
        # or it is a very large prime
        if fs > wheels[-1]:
            wheels = sieveEra(wheels, fs)
        else: # the reduced n, i.e. largest is a little larger prime.
            wheels = sieveEra(wheels, largest)
        largest, pos = lpf(largest, pos)

    print(largest)
