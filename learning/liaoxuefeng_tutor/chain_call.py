#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-22 Thu 16:30:01 Shaikh>
"""
Chained call.

链式调用。
"""
class Chain(object):
    """
    Chained call class for Github.

    GET /users/:user/repos
    """
    def __init__(self, path='GET /users'):
        self.__path = path

    def __getattr__(self, path):
        if path == 'users':
            # 'users' is a function that accepts an argument 'name'
            # Chained call requires that both functions and variables
            # return the instance of class 'Chain'.
            # therefore 'users' function should finally return an instance
            return lambda name: Chain('%s/%s' % (self.__path, ':' + name))
        elif path == 'repos':
            return Chain('%s/%s' % (self.__path, path))
        raise AttributeError('Wrong API arguments.')

    def __str__(self):
        return self.__path

    __repr__ = __str__


# test
results = Chain().users('Michael').repos
print(results)
