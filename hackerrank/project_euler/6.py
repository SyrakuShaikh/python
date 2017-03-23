#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-03-23 Thu 17:41:12 Shaikh>
"""
Project Euler #6: Sum Square Difference

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... +
10^2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 +
... + 10)^2 = 55^2 = 3025. Hence the absolute difference between the sum of the
squares of the first ten natural numbers and the square of the sum is 3025 -
385 = 2640.

Find the absolute difference between the sum of the squares of the first N
natural numbers and the square of the sum.

clue:
1. difference: (a + b)^2 - (a^2 + b^2) = 2ab
               (a + b + c)^2 - (a^2 + b^2 + c^2) = 2(ab + bc + ac)
2. first N natural numbers.
   0
   1.2  * 2
   1.2  1.3 2.3  * 2
   1.2  1.3 2.3  1.4 2.4 3.4  * 2
   1.2  1.3 2.3  1.4 2.4 3.4  1.5 2.5 3.5 4.5  * 2
3. 1 + 2 + 3 + ... + n = n(n - 1)//2
"""
def addn(n: int) -> int:
    """
    1 + 2 + 3 + ... + n
    """
    return (n * (n + 1)) // 2

DICT = {1:0}

def difference(n: int) -> int:
    """
    Squares sum subtract sum squares.
    """
    global DICT
    if n in DICT:
        return DICT[n]
    else:
        rlt = 2 * n * addn(n - 1) + difference(n - 1)
        DICT[n] = rlt
        return rlt

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(difference(n))
