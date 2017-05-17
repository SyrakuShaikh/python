#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-05-17 Wed 21:09:04 Shaikh>
import numpy as np
import pyximport
pyximport.install(inplace=True)

import vegas
from cython_integrand import f_batch
f = vegas.batchintegrand(f_batch)

integ = vegas.Integrator(4 * [[0, 1]])

integ(f, nitn=10, neval=2e5)
result = integ(f, nitn=10, neval=2e5)
print('result = %s     Q = %.2f' % (result, result.Q))
