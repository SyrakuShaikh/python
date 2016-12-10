# Time-stamp: <2016-12-10 Sat 22:31:28 Shaikh>
# -*- coding: utf-8 -*-

"""
Pascal's Triangle.

Using generator.
"""

def triangle():
    """
    generator to generate Pascal's triangle, unlimited.
    """
    list1 = [1]
    while True:
        yield list1
        list1 = [0] + list1 + [0]
        list1 = [list1[i] + list1[i+1] for i in range(len(list1) - 1)]


CNT = 1
for t in triangle():
    print(t)
    CNT += 1
    if CNT == 10:
        break
