#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-07 Sat 17:15:52 Shaikh>
"""
Sherlock and pairs.
https://www.hackerrank.com/challenges/sherlock-and-pairs

Sherlock is given an array of N integers (A_0, A_1, A_2, ..., A_N-1) by Watson.
Now Watson asks Sherlock how many different pairs of indices i and j exist such
that i is not equal j to but A_i is equal to A_j.

That is, Sherlock has to count the total number of pairs of indices (i, j)
where A_i = A_j AND i != j.

additional explanation:

The indices (i, j)'s order matters i.e. (1, 0) and (0, 1) are different and
should both be counted.
"""
from collections import defaultdict

t = int(input().strip())

for i in range(t):
    N = int(input().strip())
    array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    counts = defaultdict(int)
    for i in array:
        counts[i] += 1
    pairs = 0
    for tup in counts.items():
        num = tup[1]
        if num > 1:
            pairs += (num * (num - 1))
    print(pairs)
