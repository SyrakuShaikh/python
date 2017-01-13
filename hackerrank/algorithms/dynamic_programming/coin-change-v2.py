#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-13 Fri 21:47:21 Shaikh>
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
3. see coin-change-v2.py(this file) for details

another another clue:
http://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change

This is the best method and so-called 'dynamical programming'.
see coin-change-v3.py for details.
"""
def level(n: int, l) -> list:
    """
    pass
    """
    global PATTERN
    return ([sum(x), y] for x in l for y in PATTERN[x[1]])


N, M = input().strip().split(' ')
N, M = [int(N), int(M)]

# types of coin
C = sorted([int(i) for i in input().strip().split(' ')])

# pattern dictionary used to build the list level by level.
PATTERN = dict()
for c in C:
    PATTERN[c] = tuple([x for x in C[C.index(c):]])

# count the ways
NUM = 0

FINISH = False
NC = ([0, x] for x in C)
START = N // C[-1]
for i in range(START):
    NC = level(N, NC)
while not FINISH:
    temp = list()
    for i in NC:
        if sum(i) == N:
            NUM +=1
        elif sum(i) < N:
            temp += [i]
    if len(temp) == 0:
        FINISH = True
    else:
        NC = level(N, temp)
print(NUM)
