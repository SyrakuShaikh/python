#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-29 Sun 16:15:17 Shaikh>
"""
Insertion Sort Advanced Analysis

Insertion Sort is a simple sorting technique which was covered in previous
challenges. Sometimes, arrays may be too large for us to wait around for
insertion sort to finish. Is there some other way we can calculate the number
of times Insertion Sort shifts each elements when sorting an array?

If k_i is the number of elements over which the i^th element of the array has
to shift, then the total number of shifts will be k_1 + k_2 + ... + k_N.
"""
def sorttest(l: list) -> bool:
    """
    Test whether a list is sorted.
    """
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def larger(l: list) -> int:
    """
    Calculate the number of elements in a list that larger than the tail
    element.
    """
    tail = l[-1]
    num = 0
    for i in l[:-1]:
        if i > tail:
            num += 1
    return num


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    sums = 0
    if n != 1 and not sorttest(arr):
        for j in range(1, n):
            sums += larger(arr[:j+1])
    print(sums)
