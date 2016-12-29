#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-29 Thu 17:18:55 Shaikh>
"""
Debug codes with logging module.
"""
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = {}'.format(n))
print(10 / n)
