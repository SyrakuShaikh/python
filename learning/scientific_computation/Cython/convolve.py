#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-06-16 Fri 18:57:39 Shaikh>
import numpy as np
import convolve_py

import pyximport
pyximport.install(setup_args={"include_dirs": np.get_include()},
                  reload_support=False, inplace=False)
import convolve_c
import convolve_c2
import convolve_c3
import convolve_c4
import convolve_c5

import timeit

conpy = convolve_py.naive_convolve(np.array([[1, 1, 1]], dtype=np.int),
                                   np.array([[1], [2], [1]], dtype=np.int))
# print(conpy)

conc = convolve_c.naive_convolve(np.array([[1, 1, 1]], dtype=np.int),
                                 np.array([[1], [2], [1]], dtype=np.int))
# print(conc)

N = 300
f = np.arange(N*N, dtype=np.int).reshape((N, N))
g = np.arange(9*9, dtype=np.int).reshape((9, 9))

print("Original Python version: \n",
      timeit.timeit('convolve_py.naive_convolve(f, g)', number=5, globals=globals()),
      "\nSimple Cython version: \n",
      timeit.timeit('convolve_c.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (adding types): \n",
      timeit.timeit('convolve_c2.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (efficient indexing): \n",
      timeit.timeit('convolve_c3.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (more efficient indexing): \n",
      timeit.timeit('convolve_c4.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (use typed memoryview, a simpler syntax.): \n",
      timeit.timeit('convolve_c5.naive_convolve(f, g)', number=5, globals=globals()))
