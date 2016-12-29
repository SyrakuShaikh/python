#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-29 Thu 16:53:17 Shaikh>
"""
Catch an error using try...except and re-raise it.
"""
def errfunc(s:int):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: {}'.format(s))
    return 10 / n

def main():
    try:
        errfunc('0')
    except ValueError as e:
        print('ValueError!')
        raise

main()
