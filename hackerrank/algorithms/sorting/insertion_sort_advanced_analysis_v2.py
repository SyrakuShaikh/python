#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-23 Thu 17:17:02 Shaikh>
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


def binary(i: int, ar: list) -> int:
    """
    for large list
    """
    length = len(ar[:i])
    tail = ar[i]
    index = length // 2
    prev = length
    while not ar[index] <= tail < ar[index+1]:
        if tail < ar[index]:
            if index == 0:
                index = -1
                break
            else:
                prev = index
                index = index // 2
        elif index == prev - 1:
            break
        else: # tail > ar[index+1]
            index = index + (prev - index) // 2
    # sort
    ar.pop(i)
    ar.insert(index+1, tail)
    # return insertion swaps
    return length - index - 1


def insertion(num: int, ar: list) -> int:
    sums = 0
    for i in range(1, len(ar)):
        sums += binary(i, ar)
    return sums


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    total = 0
    if n != 1 and not sorttest(arr):
        total = insertion(n, arr)
    print(total)

# from random import sample
# arr = sample(list(range(0, 20)), k=20)
# print(*arr, ':: B')
# print('='*50)
# for i in range(1, len(arr)):
#     binary(i, arr)
# print('='*50)
# print(*arr, ':: E')
