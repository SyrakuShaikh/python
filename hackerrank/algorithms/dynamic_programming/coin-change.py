#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-06 Fri 21:33:13 Shaikh>
"""
The Coin Change Problem
https://www.hackerrank.com/challenges/coin-change

Given a value N, if we want to make change for N cents, and we have infinite
supply of each of C = {C1, C2, ..., CM} valued coins, how many ways can we make
the change? The order of coins doesn’t matter.

clue:

1. sorted tuples in set. {(,), (,),...} can eliminate overlappings.
2. save results in dict can improve performance.
"""
def ts(l: list) -> tuple:
    """
    Tuple of sorted list.
    """
    return tuple(sorted(l))


def ways(n: list, types: list) -> tuple:
    """
    a
    """
    global SOLVED
    c = types
    solve = True
    rlt = list()
    for nl in n:
        d = nl[-1]
        if d in SOLVED:
            for s in SOLVED[d]:
                rlt += [nl[:-1] + list(s)]
        else:
            for tp in c:
                if d - tp in c:
                    c.remove(d - tp)
                    rlt += [nl[:-1] + [tp, d - tp]]
                elif d - tp >= c[0]:
                    rlt += [nl[:-1] + [tp, d - tp]]
                elif d == c:
                    rlt += [nl]
        if solve:
            s_temp = set()
            for r in n:
                s_temp.add(ts(r))
            SOLVED[sum(n[0])] = s_temp
    return rlt, solve


# dict: key is an integer N, value is sorted tuples in list.
SOLVED = dict()

N, M = input().strip().split(' ')
N, M = [int(N), int(M)]

C = input().strip().split(' ')
C = sorted([int(i) for i in C])

NC = [[i] for i in C]
while not ways(NC, C)[1]:
    NC = ways(NC, C)[0]
    print(NC)

print(SOLVED)
SN = ways([[N]], C)[0]
while not ways(SN, C)[1]:
    SN = ways(SN, C)[0]
    print(SN)
