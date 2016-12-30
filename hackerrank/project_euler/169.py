#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-30 Fri 20:19:18 Shaikh>
"""
Project Euler #169:

Exploring the number of different ways a number can be expressed as a sum of
powers of 2 using each power no more than twice.

example:
0: 1 # definition f(0) = 1
10: 5  f(10) = 5

clue:
f(2k+1) = f(k)
f(2k) = f(k) + f(k-1), for k >= 1

and more:
f((2k+1)*2^m) = f(2k+1) + m*f(2k)
               = (m+1)*f(k) + m*f(k-1)
for m, k>0
"""
def ways(n: int) -> int:
    """
    Recursion and binary form.
    """
    if n == 0:
        return 1
    elif n == -1:
        return 0
    else:
        BN = bin(n)[2:]
        diff = len(BN) - len(BN.rstrip('0'))
        if diff == 0:
            return ways(n >> 1)
        else:
            new = n >> (diff + 1)
            return (diff + 1) * ways(new) + diff * ways(new - 1)


N = int(input())
print(ways(N))

# def maxtwo(n: int) -> int:
#     """
#     Find the max number of 2 in a number n.

#     n = (2k+1)*2^m for m, k >= 0
#     return m

#     Trick:
#     binary form. all the zeroes in the tail.
#     """
#     BN = bin(n)[2:]
#     return len(BN) - len(BN.strip('0'))


# def ways(n: int) -> int:
#     """
#     Recursion function.
#     """
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         # use maxtwo function and the reduced formula
#         # can achieve much better performance.
#         i = maxtwo(n)
#         j = n >> i
#         return ways(j) + i * ways(j - 1)
#     else:
#         return ways((n - 1) >> 1)


# from itertools import groupby

# def count(t: iter, x = '1', y = '0') -> list:
#     """
#     Count the number of continuous elements of an iterable.

#     This is the simple version which only considers two different elements.
#     e.g. \"11000101011000\" -> [(2, 3), (1, 1), (1, 1), (2, 3)]. The first
#     number in the tuple is the number of \"1\" and the second is for \"0\".
#     """
#     if len(t) == 0:
#         return [(0, 0)]
#     rlt = []
#     if t[0] == x:
#         a, b = 1, 0
#         is_x = True
#     else:
#         a, b = 0, 1
#         is_x = False
#     i = 1
#     while i < len(t):
#         if is_x and t[i] == x:
#             a += 1
#         elif is_x:
#             b += 1
#             is_x = False
#         elif t[i] == x:
#             rlt.append((a, b))
#             a, b = 1, 0
#             is_x = True
#         else:
#             b += 1
#         i +=1
#     rlt.append((a, b))

#     # or use a included battery
#     # here for a double check.
#     ## commented in upload to Hackerrank.
#     # rlt2 = []
#     # grouped = [(k, sum(1 for i in g)) for k, g in groupby(t)]
#     # lg = len(grouped)

#     # init = grouped[0]
#     # if init[0] == x and lg > 1:
#     #     rlt2.append((init[1], grouped[1][1]))
#     #     i = 2
#     # elif init[0] == x:
#     #     rlt2 = [(init[1], 0)]
#     # elif lg > 1:
#     #     rlt2.append((0, init[1]))
#     #     i = 1
#     # else:
#     #     rlt2 = [(0, init[1])]

#     # while i < lg:
#     #     if lg - i >= 2:
#     #         rlt2.append((grouped[i][1], grouped[i + 1][1]))
#     #         i += 2
#     #     else:
#     #         rlt2.append((grouped[i][1], 0))
#     #         i += 1

#     # if rlt2 == rlt:
#     #     return rlt2
#     # else:
#     #     raise ValueError('Mine: {} v.s. Groupby {}'.format(rlt, rlt2))
#     return rlt


# def ext(arr, a, b):
#     """
#     Misc function.

#     return the element of a 2-dim array easily
#     """
#     return arr[a][b]


# def ways(grp: list) -> int:
#     """
#     Base a formula reduced by myself to get the ways required by
#     Project Euler #169.

#     Details: 12 -> binary: 1100 -> [(2, 2)], only one group, 2 '1' and 2 '0'.
#     1100 -> 1 100 : 12 = 8 + 4
#          -> 1 010 : 12 = 8 + 2 + 2
#          -> 1 011 : 12 = 8 + 2 + 1 + 1
#          ## '100' has 3 ways and 2 of them 'push' one '0' to left which allow
#             the '1' representing 8 to split into 4 + 4.
#          -> 0 110 : 12 = 4 + 4 + 2 + 2
#          -> 0 111 : 12 = 4 + 4 + 2 + 1 + 1

#     Since the rules restrict that each powers of 2 is no more than twice, only
#     can push ONE zero.

#     for multi-groups situations:
#     One need to extract the push-zero terms clearly and it's a pseudo-product
#     not a summation i.e. roughly, group-1 3 ways, group-2 4 ways,
#     group-3 2 ways, then total is 3 + 3 * 4 + 3 * 4 * 2.
#     """
#     lg = len(grp)
#     if lg == 1 and grp[0][1] == 0:
#         # for number whose binary form are all '1'.
#         return 1
#     elif lg == 1:
#         # for number like 1..10...0
#         ## rules confuse me, should '8 = 2^3' be counted?
#         return ext(grp, 0, 0) * ext(grp, 0, 1) + min(1, grp[0][0] - 1)
#     else:
#         rlt1 = (ext(grp, 0, 0) - 1) * ext(grp, 0, 1) + 1
#         rlt2 = ext(grp, 0, 1) # push-zero terms
#         rlt = rlt1 + rlt2
#         i = 1
#         while i < lg:
#             rlt11 = rlt1 * (ext(grp, i, 0) - 1) * ext(grp, i, 1)
#             rlt12 = rlt2 * ((ext(grp, i, 0) - 1) * (ext(grp, i, 1) + 1))
#             rlt21 = rlt1 * ext(grp, i, 1) # push-zero terms part1
#             rlt22 = rlt2 * (ext(grp, i, 1) +1) # push-zero terms part2
#             rlt1, rlt2 = rlt11 + rlt12, rlt21 + rlt22
#             rlt += rlt1 + rlt2
#             i += 1
#     return rlt

# N = int(input())
# if N in (1, 0):
#     print(1)
# else:
#     BN = bin(N)[2:]
#     groups = count(BN)[::-1]
#     print(ways(groups))
