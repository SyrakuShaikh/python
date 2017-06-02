#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-06-02 Fri 14:34:07 Shaikh>
import numpy as np
import convolve_py

import pyximport
pyximport.install(setup_args={"include_dirs": np.get_include()},
                  reload_support=True,
                  inplace=True)
import convolve_c
import convolve_c2
import convolve_c3

import timeit

conpy = convolve_py.naive_convolve(np.array([[1, 1, 1]], dtype=np.int),
                                   np.array([[1], [2], [1]], dtype=np.int))
# print(conpy)

conc = convolve_c.naive_convolve(np.array([[1, 1, 1]], dtype=np.int),
                                 np.array([[1], [2], [1]], dtype=np.int))
# print(conc)

N = 100
f = np.arange(N*N, dtype=np.int).reshape((N, N))
g = np.arange(9*9, dtype=np.int).reshape((9, 9))

print("Original Python version: \n",
      timeit.timeit('convolve_py.naive_convolve(f, g)', number=5, globals=globals()),
      "\nSimple Cython version: \n",
      timeit.timeit('convolve_c.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (adding types): \n",
      timeit.timeit('convolve_c2.naive_convolve(f, g)', number=5, globals=globals()),
      "\nCython version (efficient indexing): \n",
      timeit.timeit('convolve_c3.naive_convolve(f, g)', number=5, globals=globals()))
