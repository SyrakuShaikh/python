#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-13 Fri 14:21:11 Shaikh>
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
"""
def ts(l: list) -> tuple:
    """
    Sort the list first and then convert it to tuple type.
    """
    return tuple(sorted(l))


def ways(n: list, types: list) -> list:
    """
    Calculate the number of ways to make coin change.
    """
    if len(n) == 0:
        return n
    global SOLVED
    rlt = list()   # temp
    rltc = list()  # solved, count
    for nl in n:
        d = nl[-1]
        if d in SOLVED:
            # rltc += SOLVED[d]
            rltc += [nl[:-1] + list(so) for so in SOLVED[d]]
        else:
            c = types[:]
            for tp in c:
                if d == tp:
                    rltc += [nl]
                if d - tp in c and d - tp != tp:
                    rlt += [nl[:-1] + [tp, d - tp]]
                    c.remove(d - tp)
                elif d - tp >= c[0]:
                    rlt += [nl[:-1] + [tp, d - tp]]
    return rltc + ways(rlt, types)


# dict: key is an integer N, value is sorted tuples in list.
SOLVED = dict()

N, M = input().strip().split(' ')
N, M = [int(N), int(M)]

C = sorted([int(i) for i in input().strip().split(' ')])
for ty in C:
    temp = set()
    for r in ways([[ty]], C):
        temp.add(ts(r))
    SOLVED[ty] = temp

NL = list()
for ty in C:
    NL += list(range(N, C[-1], -ty))

for n in ts(NL):
    rlts = set()
    for l in ways([[n]], C):
        rlts.add(ts(l))
    SOLVED[n] = rlts

print(len(SOLVED[N]))
