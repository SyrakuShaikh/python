#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-31 Sat 15:50:51 Shaikh>
"""
Project Euler #2:

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first terms will be:
   1 2 3 5 8 13 21 34 55 89 ...
By considering the terms in the Fibonacci sequence whose values do not exceed N,
find the sum of the even-valued terms.

e.g.
f(10) = 2 + 8 = 10
f(100) = 2 + 8 + 34 = 44

clue:
Odd(O), Even(E)
O + O = E
O + E = O
E + E = E
so, the second, 5th, 8th, 11th ... 2 + 3n number in the sequence is EVEN.

The following codes are accepted by Hackerrank. However, when dealing with
large t, use a dict to memorize all previous Fibonacci numbers can improve
performance.
1. save all the input N to a list.
2. find the max one using max(list).
3. generate all the even-valued Fibonacci numbers that not exceed max.
4. calculate the summations according to that list (in order.)
see 2v2.py
"""
def nexte(i: int, j: int) -> tuple:
    """
    The next even-valued Fibonacci number.
    """
    for k in range(3):
        i, j = j, i + j
    return i, j


t = int(input().strip())
for a0 in range(t):
    a, b = 1, 2
    total = 0
    n = int(input().strip())
    while True:
        if b <= n:
            total += b
        else:
            break
        a, b = nexte(a, b)
    print(total)
