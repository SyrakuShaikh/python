#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-21 Wed 18:46:45 Shaikh>
"""
An exercise of @property decorator in class definition.

@property is used to decorate a variable's 'get' and 'set' method.
"""

class Screen(object):
    """
    Screen class. Three variables:

    height. writable
    width. writable
    resolution. read-only
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Must be a positive integer.')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Must be a positive integer.')
        self.__width = value

    @property
    def resolution(self):
        return self.__height * self.__width


# test
test = Screen()
test.width = 1024
test.height = 768
print(test.resolution)
assert test.resolution == 786432, '1024 * 768 = %d ?' % test.resolution
