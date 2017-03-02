#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-02 Thu 17:53:29 Shaikh>
"""
Fraudulent Activity Notifications.

HackerLand National Bank has a simple policy for warning clients about possible
fraudulent account activity. If the amount spent by a client on a particular
day is greater than or equal to 2x the client's median spending for the last d
days, they send the client a notification about potential fraud. The bank
doesn't send the client any notifications until they have at least d prior days
of transaction data.

Given the value of d and a client's total daily expenditures for a period of n
days, find and print the number of times the client will receive a notification
over all n days.

Hint: The expenditures in this problem is limited as: 0 <= expenditure <= 200.
Therefore, counting sort may be a good choice.
"""
def counting_sort(ar: list) -> list:
    """
    Counting Sort Function.
    """
    # from 0 to 200
    LIST = [0]*201
    for a in ar:
        LIST[a] += 1
    return LIST


def median(l: list, ds: int) -> int:
    """
    Find the median in a list.
    """
    m = (ds // 2) + 1
    temp = 0
    last = 0
    while l[last] == 0:
        last += 1
    if m == 1: # ds == 1
        return last
    for i, a in enumerate(l):
        temp += a
        if temp == m:
            if a > 1:
                return i
            elif a == 1:
                if ds % 2 == 1:
                    return i
                else:
                    return (last + i) / 2
            else: # m == 0 => ds == 1
                return last
        elif temp > m:
            if ds % 2 == 1:
                return i
            else:
                if a == temp - m + 1:
                    return (last + i) / 2
                else: # a > temp - m + 1
                    return i
        if a != 0:
            last = i


def notifications(total: int, days: int, ex: list) -> int:
    """
    Count the number of fraudulent activity notifications.
    """
    if days == total:
        return 0
    counts = 0
    current = counting_sort(ex[:days])
    med = median(current, days)
    index = days
    while index < len(ex):
        if index > days:
            current[ex[index-days-1]] -= 1
            current[ex[index-1]] += 1
            med = median(current, days)
        if ex[index] >= 2 * med:
            counts += 1
        index += 1
    return counts


n, d = (int(x) for x in input().strip().split(' '))
exps = [int(x) for x in input().strip().split(' ')]

print(notifications(n, d, exps))
