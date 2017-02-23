#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-02-23 Thu 21:44:33 Shaikh>
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
def quick_sort(ar: list, st: int, ed: int):
    """
    Quick Sort Function.
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
    quick_sort(ar, st, index)
    quick_sort(ar, index+1, ed)


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
# (my quick_sort is not good enough)
quick_sort(arrays, 0, len(arrays))
arrayss = arrays[:]
arrayss.reverse()
c1 = swaps(array, arrays)
c2 = swaps(array, arrayss)
print(min(c1, c2))
