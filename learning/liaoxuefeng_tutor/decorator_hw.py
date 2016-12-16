# Time-stamp: <2016-12-17 Sat 00:50:10 Shaikh>
# -*- coding: utf-8 -*-
"""
Homework of the section 'decorator'.
"""
from functools import wraps


def log(str_or_func):
    """
    Define the decorator.

    Can accept a parameter or no parameter.
    """
    def decorator(func):
        """
        Outside decorator.
        """
        @wraps(func)
        def wrapper(*args, **kw):
            """
            Inner decorator.
            """
            fname = func.__name__
            print('%s call %s():' % (text, fname))
            func(*args, **kw)
            print('end call %s()' % fname)
        return wrapper
    if isinstance(str_or_func, str):
        text = str_or_func
        return decorator
    else:
        text = 'begin'
        return decorator(str_or_func)


@log
def f():
    """
    test function.
    """
    print('abc')

f()

@log('execute')
def g():
    """
    test function.
    """
    print('xyz')

g()
