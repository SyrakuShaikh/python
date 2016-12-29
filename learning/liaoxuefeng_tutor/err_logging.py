#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-29 Thu 16:45:05 Shaikh>
"""
Using logging module to log the error messages.
"""
import logging

def foo(s:int):
    """
    test function 1.
    """
    return 10 / int(s)

def bar(s:int):
    """
    test function 2.
    """
    return foo(s) * 2

def main():
    """
    main test function.
    """
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
