#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-01 Wed 20:47:57 Shaikh>
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


def cqs(ar: list, st: int, ed: int):
    """
    Quick Sort Function.

    Single pivot version.
    So-called classic quick sort.
    Fixed position pivot.
    """
    if ed - st < 2:
        return ar
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
    ar = cqs(ar, st, index)
    ar = cqs(ar, index+1, ed)
    return ar


def dpqs(ar: list, left: int, right: int):
    """
    Dual-Pivot Quick Sort.
    """
    length = right - left
    if length < 1:
        return ar
    elif length < 300:
        ar = cqs(ar, left, right+1)
        return ar

    # # record the initial left index which may be used
    # # later when the partition completes.
    # oldleft = left

    # # locate the two pivots' index
    # while ar[left] >= ar[right] and left < right:
    #     if ar[left] > ar[right]:
    #         ar[left], ar[right] = ar[right], ar[left]
    #         break
    #     else:
    #         left += 1

    pivots = {}
    i = 5
    while len(pivots) < 5:
        div = (length - 2) // i
        pivots = {ar[left + x * div]:left + x * div for x in range(1, i+1)}
        i += 1

    pivotsK = list(pivots.keys())
    insertion_sort(pivotsK)

    newdiv = len(pivots) // 3
    newleft = pivots[pivotsK[1*newdiv]]
    newright = pivots[pivotsK[2*newdiv+1]]

    ar[left], ar[newleft] = ar[newleft], ar[left]
    ar[right], ar[newright] = ar[newright], ar[right]

    pivot1 = ar[left]
    pivot2 = ar[right]

    less = left + 1
    while less < right and ar[less] < pivot1:
        less += 1
    # when loop ends, ar[less] >= pivot1

    king = less
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

    # arrange two pivots
    ar[right], ar[king] = ar[king], ar[right]
    ar[left], ar[less-1] = ar[less-1], ar[left]
    # ar = ar[0:oldleft] + ar[left:king] + ar[oldleft:left] + ar[king:]

    # recursion
    # dif = left - oldleft
    ar = dpqs(ar, left, less-2)
    ar = dpqs(ar, less, great)
    ar = dpqs(ar, king+1, right)
    return ar


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

t = int(input().strip())
array = [int(x) for x in input().strip().split(' ')]
arrays = array[:]

# here used the built-in 'sort' function can pass all the test_cases
# therefore I need to find a better sort algorithm.
# (my cqs is not good enough)
# cqs(arrays, 0, len(arrays))
if t < 47:
    insertion_sort(arrays)
else:
    arrays = dpqs(arrays, 0, len(arrays)-1)

arrayss = arrays[:]
arrayss.reverse()
c1 = swaps(array, arrays)
c2 = swaps(array, arrayss)
print(min(c1, c2))
