#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-17 Fri 15:57:25 Shaikh>
"""
Insertion Sort Advanced Analysis

Insertion Sort is a simple sorting technique which was covered in previous
challenges. Sometimes, arrays may be too large for us to wait around for
insertion sort to finish. Is there some other way we can calculate the number
of times Insertion Sort shifts each elements when sorting an array?

If k_i is the number of elements over which the i^th element of the array has
to shift, then the total number of shifts will be k_1 + k_2 + ... + k_N.
"""
from random import randint


def sorttest(l: list) -> bool:
    """
    Test whether a list is sorted.
    """
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


def larger(element: int, LIST: list) -> int:
    """
    Count the larger elements than the given one.
    """
    temp = 0
    for i in LIST:
        if i > element:
            temp += 1
    return temp


def counting(length: int, LIST: list) -> int:
    """
    Calculate the number of elements in a list that larger than the tail
    element.
    """
    sums = 0
    for i in range(1, length):
        sums += larger(LIST[i], LIST[:i])
    return sums


def divide(element: int, LIST: list) -> list:
    """
    Divide one list to two lists.

    This function divides one list to two lists based on whether the elements
    in it is larger than the given element.
    """
    partitions = [[], []]
    MAX = None # the largest one less than the given element.
    if len(LIST) == 0:
        return [[], [element], MAX]
    for i in LIST:
        if i > element:
            partitions[0].append(i)
        else:
            if i < element:
                MAX = i if MAX is None else max(MAX, i)
            partitions[1].append(i)
    return partitions + [MAX]


def check():
    """
    Check function.

    Check whether every 'value' of the dictionary PARTS is shorter than NUMS.
    """
    global PARTS, NUMS
    new_parts = dict()
    for k, v in PARTS.items():
        if len(v) > NUMS and k != 'R':
            trys = 1
            temp = [v, [], None]
            while len(temp[0]) > NUMS or len(temp[1]) > NUMS:
                pivot_index = randint(0, len(v))
                pivot = v[pivot_index]
                temp = divide(pivot, v)
                new_parts[k] = temp[1]
                new_parts[pivot] = temp[0]
                if trys > 30:
                    break
                else:
                    trys += 1
        else:
            new_parts[k] = v
    PARTS = new_parts


def insertion(length: int, LIST: list) -> int:
    global PARTS, NUMS
    sums = 0
    if length < 5000:
        return counting(length, LIST)
    else:
        sums = counting(4999, LIST[:4999])

        i = 4999
        temp = divide(LIST[i], LIST[:i])
        PARTS[LIST[i]] = temp[0]
        PARTS['R'] = temp[1] + [LIST[i]]

        while i < length-1:
            i += 1

            COMP = list(PARTS.keys())
            COMP.remove('R')
            tempa = divide(LIST[i], COMP)

            for j in tempa[0]:
                sums += len(PARTS[j])

            if LIST[i] in COMP:
                sums += len(PARTS[LIST[i]])
                if tempa[2] is None:
                    PARTS['R'] += [LIST[i]]
                else:
                    PARTS[tempa[2]] += [LIST[i]]
            elif tempa[2] is None:
                tempb = divide(LIST[i], PARTS['R'])
                sums += len(tempb[0])
                PARTS[LIST[i]] = tempb[0]
                PARTS['R'] = tempb[1] + [LIST[i]]
            else:
                tempc = divide(LIST[i], PARTS[tempa[2]])
                sums += len(tempc[0])
                if len(PARTS[tempa[2]]) > NUMS:
                    PARTS[LIST[i]] = tempc[0]
                    PARTS[tempa[2]] = tempc[1] + [LIST[i]]
            check()

        return sums


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    PARTS = dict()
    NUMS = 2000
    total = 0
    if n != 1 and not sorttest(arr):
        total = insertion(n, arr)
    print(total)

# from random import sample
# PARTS = dict()
# arr = sample(list(range(1, 200)), k=100)
# total = 0
# if len(arr) != 1 and not sorttest(arr):
#     total = insertion(len(arr), arr)
# print(total)
