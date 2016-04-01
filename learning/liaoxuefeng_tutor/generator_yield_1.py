# Time-stamp: <2016-04-01 Fri 21:43:05 Shaikh>
# -*- coding: utf-8 -*-


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n <= max:
        yield b
        a, b = b, a + b
        n += 1


n = int(input('Fibonacci nth: '))
f = fibonacci(n)
print(f)

for i in f:
    print(i, end=' ')
