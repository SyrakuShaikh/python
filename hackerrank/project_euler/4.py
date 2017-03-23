#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-23 Thu 17:40:29 Shaikh>
"""
Project Euler #4: Largest Palindrome Product

A palindromic number reads the same both ways. The smallest 6 digit palindrome
made from the product of two 3-digit numbers is 101101 = 143 x 707.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.

Analysis:
1. less than N
2. palindromic
3. largest
4. product of two numbers
5. both the two numbers are 3-digit.
===>
1. N: (min, max) (10e4, 10e6) and this problem in Hackerrank restrict N to be
   6-digit.
2. to string and s == s[::-1] <- usual way.
3. to not test but construct the palindromic numbers
4.
"""
from math import sqrt, ceil

def nlp(n: int) -> int:
    """
    The next largest palindromic number below N.
    """
    half = n // 1000
    while True:
        palin = int(str(half) + str(half)[::-1])
        half -= 1
        if palin >= n:
            continue
        else:
            yield palin


def divid(n: int) -> bool:
    """
    Test whether a number n is a product of two 3-digit numbers.
    """
    global mem
    if n in mem:
        return True
    for i in range(100, ceil(sqrt(n))):
        if n / i > 999.0:
            continue
        if n % i == 0:
            return True
    return False


mem = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for pa in nlp(n):
        if divid(pa):
            mem.append(pa)
            print(pa)
            break
