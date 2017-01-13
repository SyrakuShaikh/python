#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-13 Fri 22:38:19 Shaikh>
"""
The Coin Change Problem
https://www.hackerrank.com/challenges/coin-change

Given a value N, if we want to make change for N cents, and we have infinite
supply of each of C = {C1, C2, ..., CM} valued coins, how many ways can we make
the change? The order of coins doesn’t matter.

clue:

1. sorted tuples in set. {(,), (,),...} can eliminate overlappings.
2. save results in dict can improve performance.
3. only require the number of ways but not showing all the ways.
4. since clue-3, clue-1 is changed, only save the length of that set.

another clue:

1. there is a way to build a list level by level that no overlappings will exist.
2. example for coin types [1, 2, 3]
   1                                2            3
   1              2        3        2       3    3
   1      2    3  2    3   3        2    3  3    3
   1 2 3  2 3  3  2 3  3   3        2 3  3  3    3
3. see coin-change-v2.py for details

another another clue:
http://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change

This is the best method and so-called 'dynamical programming'.
see coin-change-v3.py (this file) for details.
"""
def ways(n: int, l: list):
    """
    pass
    """
    if len(l) == 1:
        return 1 if n % l[0] == 0 else 0
    global SOLVED
    t = n // l[-1]
    if t == 0:
        if (n, l[:-1]) not in SOLVED:
            SOLVED[(n, l[:-1])] = ways(n, l[:-1])
        return SOLVED[(n, l[:-1])]
    else:
        temp = 0
        for i in range(t + 1):
            tup = (n - i * l[-1], l[:-1])
            if tup not in SOLVED:
                SOLVED[tup] = ways(tup[0], tup[1])
            temp += SOLVED[tup]
        return temp


N, M = input().strip().split(' ')
N, M = [int(N), int(M)]

# types of coin
C = tuple(sorted([int(i) for i in input().strip().split(' ')]))

# SOLVED
SOLVED = dict()

NUM = 0
print(ways(N, C))
