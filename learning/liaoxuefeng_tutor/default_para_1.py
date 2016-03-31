# Time-stamp: <2016-03-31 Thu 13:05:25 Shaikh>
# -*- coding: utf-8 -*-


def app_end(L=[]):
    L.append('END')
    return L


def app_end_re(M=None):
    if M is None:
        M = []
    M.append('END')
    return M

print(app_end())
print(app_end())
print(app_end())

print(app_end_re())
print(app_end_re())
print(app_end_re())
