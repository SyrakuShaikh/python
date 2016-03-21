# Time-stamp: <2016-03-21 Mon 22:41:06 Shaikh>
# -*- coding: utf-8 -*-
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
