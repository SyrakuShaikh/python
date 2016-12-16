# Time-stamp: <2016-12-16 Fri 16:35:24 Shaikh>
# -*- coding: utf-8 -*-
"""
A Better Example of Closure.
"""

def count_o():
    """
    Original example from Liaoxuefeng.
    """
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


def count():
    """
    A better one without redefining the function 'f' in every loop.
    """
    fs = []
    def f():
        return i * i
    for i in range(1, 4):
        fs.append(f)
    return fs


f1, f2, f3 = count()
print('f1: ', f1())
print('f2: ', f2())
print('f3: ', f3())
