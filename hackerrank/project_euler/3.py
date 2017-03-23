#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-23 Thu 17:38:29 Shaikh>
"""
Project Euler #3: Largest Prime Factor

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
"""
def primes(n: int) -> list:
    """
    Generate all the primes not greater than n.

    Using method: sieve of Eratosthenes.
    """
    if n < 2:
        raise ValueError('Do you know what is prime?')
    l = list(range(2, n + 1))
    i = 0
    while i < len(l) - 1:
        base = l[i]
        j = i + 1
        while j < len(l):
            c = l[j]
            if c % base == 0:
                l.remove(c)
            j += 1
        i += 1
    return l


t = int(input().strip())
LIST = []
# for a0 in range(t):
#     n = int(input().strip())
#     LIST = primes(n) if len(primes(n)) > len(LIST) else LIST
#     for i in LIST[::-1]:
#         if i == n or (i < n and n % i == 0):
#             print(i)
#             break

for a0 in range(t):
    LIST.append(int(input().strip()))
MAX = max(LIST)
# generate all the primes not exceed MAX.
pLIST = primes(MAX)[::-1] # largest prime factor

for k in LIST:
    for n in pLIST:
        if n == k or (n < k and k % n == 0):
            print(n)
            break
