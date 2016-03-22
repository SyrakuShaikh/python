# Time-stamp: <2016-03-22 Tue 13:48:36 Shaikh>
# -*- coding: utf-8 -*-
# a decorator receives a method it's wrapping as a variable 'f'


def increment(f):
    # we use arbitrary args and keywords to
    # ensure we grab all the input arguments
    def wraped_f(*args, **kw):
        # note we call f against the variables passed into the wrapper,
        # and cast the result to an int and increment.
        return int(f(*args, **kw)) + 1
    return wraped_f             # the wrapped function gets returned.


@increment
def plus(a, b):
    return a + b

result = plus(4, 6)
assert result == 11, "We wrote our decorator wrong!"
assert result == 10, "We wrote our decorator wrong!"
