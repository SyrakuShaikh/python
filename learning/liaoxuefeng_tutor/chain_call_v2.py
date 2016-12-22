#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-22 Thu 16:40:30 Shaikh>
"""
Chained call using __call__.

链式调用。
"""
class Chain(object):
    """
    Chained call class for Github.

    GET /users/:user/repos
    """
    def __init__(self, path='GET /users'):
        self.__path = path

    def __call__(self, name):
        return Chain('%s%s' % (self.__path, name))

    def __getattr__(self, path):
        if path == 'users':
            # using __call__. Class Chain is callable, i.e. can accept arguments.
            return Chain('%s/%s' % (self.__path, ':'))
        elif path == 'repos':
            return Chain('%s/%s' % (self.__path, path))
        raise AttributeError('Wrong API arguments.')

    def __str__(self):
        return self.__path

    __repr__ = __str__


# test
results = Chain().users('Michael').repos
print(results)
