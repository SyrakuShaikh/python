#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-04 Wed 16:48:46 Shaikh>
"""
Project Euler #5:

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible(divisible with no
remainder) by all of the numbers from 1 to N?
"""
def smallest(n: int) -> list:
    """
    Construct the list used to calculate the smallest multiple.
    """
    global LIST
    if n in LIST:
        return
    i = len(LIST) + 1
    while i <= n:
        lt = i
        for j in LIST:
            if j == 1:
                continue
            if lt == 1:
                break
            if lt % j == 0:
                lt = lt // j
        LIST.append(lt)
        i += 1


def multiple(l: list) -> int:
    """
    Calculate the product of a list.
    """
    rlt = 1
    for i in l:
        rlt *= i
    return rlt


LIST = [1, 2, 3]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n <= len(LIST):
        print(multiple(LIST[:n]))
    else:
        smallest(n)
        print(multiple(LIST))
