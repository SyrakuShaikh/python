#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-17 Sat 19:33:12 Shaikh>
"""
Test 'sys' module's 'argv' method.

Is there any difference between ~python3 hello.py~ and ~./hello.py~.
"""

__author__ = 'Shaikh'

import sys

def test():
    """
    test function, main function.
    """
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments.')


if __name__ == '__main__':
    test()
