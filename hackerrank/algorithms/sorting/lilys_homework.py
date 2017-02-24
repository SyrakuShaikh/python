#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-02-24 Fri 21:20:27 Shaikh>
"""
Lily's Homework

Whenever George asks Lily to hang out, she's busy doing homework. George wants
to help her finish it faster, but he's in over his head! Can you help George
understand Lily's homework so she can hang out with him?

Consider an array of n distinct integers, A = [a_0, a_1, ..., a_n-1]. George
can swap any two elements of the array any number of times. An array is
beautiful if the sum of |a_i - a_i-1| among 0 < i < n is minimal possible
(after, possibly, performing some swaps).

Given the array A, find and print the minimum number of swaps that should be
performed in order to make the array beautiful.
"""
def insertion_sort(ar: list):
    """
    Insertion Sort Function.
    """
    for i in range(1, len(ar)):
        pivot = ar[i]
        for j in range(i-1, -1, -1):
            if ar[j] > pivot:
                ar[j+1] = ar[j]
            else:
                ar[j+1] = pivot
                break
        else:
            ar[j] = pivot


def cqc(ar: list, st: int, ed: int):
    """
    Quick Sort Function.

    Single pivot version.
    So-called classic quick sort.
    Fixed position pivot.
    """
    if ed - st < 2:
        return
    pivot = ar[ed-1]
    index = st
    for i, a in enumerate(ar[st:ed-1]):
        ind = i+st
        if a <= pivot:
            if ind != index:
                ar[ind], ar[index] = ar[index], ar[ind]
            index += 1
    if index != ed-1:
        ar[ed-1], ar[index] = ar[index], ar[ed-1]
    cqc(ar, st, index)
    cqc(ar, index+1, ed)


def dpqc(ar: list, left: int, right: int):
    """
    Dual-Pivot Quick Sort.
    """
    if right - left < 10:
        print(*ar[left:right+1])
        cqc(ar, left, right+1)
        print(*ar[left:right+1])
        return
    # record the initial left index which may be used
    # later when the partition completes.
    oldleft = left
    # locate the two pivots' index
    while ar[left] >= ar[right] and left < right:
        if ar[left] > ar[right]:
            ar[left], ar[right] = ar[right], ar[left]
            break
        else:
            left += 1

    pivot1 = ar[left]
    pivot2 = ar[right]

    less = left + 1
    while less < right and ar[less] < pivot1:
        less += 1
    # when loop ends, ar[less] >= pivot1

    king = less + 1
    while king < right and pivot1 <= ar[king] <= pivot2:
        king += 1
    # when loop ends, ar[king] is < pivot1 or > pivot2.

    great = right - 1
    while great >= king and ar[great] > pivot2:
        great -= 1
    # when loop ends, ar[great] <= pivot2.

    while king <= great:
        temp = ar[king]
        if temp <= pivot2:
            ar[king], ar[less] = ar[less], ar[king]
            if temp < pivot1:
                less += 1
            king += 1
        else:
            ar[king], ar[great] = ar[great], ar[king]
            great -= 1
    # partition completes!
    ar[right], ar[great] = ar[great], ar[right]
    ar = ar[0:oldleft] + ar[left+1:less] + ar[oldleft:left+1] + ar[less:]
    # recursion
    print(*ar)
    dpqc(ar, oldleft, oldleft+less-left-2)
    dpqc(ar, less, great-1)
    dpqc(ar, king+1, right)



def swaps(ar: list, ars: list) -> int:
    """
    Counting the number of swaps.

    This function CHANGES the list 'ars'!
    """
    ard = dict()
    for i, a in enumerate(ars):
        ard[a] = i
    n = 0
    for i, a in enumerate(ar):
        if i != ard[a]:
            # increase the count
            n += 1
            # swap both the dict and the list
            ard[ars[i]] = ard[a]
            ars[i], ars[ard[a]] = ars[ard[a]], ars[i]
            # remove the unused dict item.
            ard.pop(a)
    return n

# t = int(input().strip())
# array = [int(x) for x in input().strip().split(' ')]
# arrays = array[:]

# here used the built-in 'sort' function can pass all the test_cases
# therefore I need to find a better sort algorithm.
# (my cqc is not good enough)
# cqc(arrays, 0, len(arrays))
# if t < 47:
#     insertion_sort(arrays)
# else:
#     dpqc(arrays, 0, len(arrays)-1)

# arrayss = arrays[:]
# arrayss.reverse()
# c1 = swaps(array, arrays)
# c2 = swaps(array, arrayss)
# print(min(c1, c2))

from random import sample
arr = sample(list(range(1, 200)), k=30)
print(*arr)
dpqc(arr, 0, len(arr)-1)
print(*arr)
