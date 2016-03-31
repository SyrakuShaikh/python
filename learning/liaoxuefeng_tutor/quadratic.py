# Time-stamp: <2016-03-31 Thu 12:42:31 Shaikh>
# -*- coding: utf-8 -*-
import math


def quadratic(a, b, c):
    test = b**2 - 4*a*c
    if test > 0:
        stest = math.sqrt(test)
        return ((-b + stest)/(2*a),
                (-b - stest)/(2*a))
    elif test == 0:
        return (-b)/(2*a)
    else:
        raise ValueError('No Real roots!')

a = float(
    input("To solve the equation 'ax^2 + bx + c = 0',\n\
please input a = "))
if a == 0:
    raise ValueError("Not a quadratic equation.")
b = float(input("and input b = "))
c = float(input("finally, c = "))
# a, b, c = input("Please input 'a, b, c' to complete\
# the equation 'ax^2+bx+c = 0'")
sol = quadratic(a, b, c)
if type(sol) is float:
    print("Solution: only one root {0:.3f}.".format(quadratic(a, b, c)))
else:
    print("Solution: 1st root is {0:.3f} and 2nd root is {1:.3f}"
          .format(sol[0], sol[1]))
