#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2017-01-05 Thu 15:09:47 Shaikh>
"""
Journey to the Moon.
https://www.hackerrank.com/challenges/journey-to-the-moon

The member states of the UN are planning to send 2 people to the Moon. But there
is a problem. In line with their principles of global unity, they want to pair
astronauts of different 2 countries.

There are N trained astronauts numbered from 0 to N-1. But those in charge of
the mission did not receive information about the citizenship of each
astronaut. The only information they have is that some particular pairs of
astronauts belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts
belonging to different countries. Assume that you are provided enough pairs to
let you identify the groups of astronauts even though you might not know their
country directly. For instance, if 1, 2, 3 are astronauts from the same
country; it is sufficient to mention that (1, 2) and (2, 3) are pairs of
astronauts from the same country without providing information about a third
pair (1, 3).

Additional explanation:

There will be singleton group which means if there is one astronaut who belongs
to a country by him/herself, this group (should like (7)) will not be shown.
"""
def nC2(n: int) -> int:
    """
    Pick two elements from n elements, un-ordered.
    """
    return (n * (n - 1)) // 2


N, I = input().strip().split(' ')
N, I = [int(N), int(I)]

country = []
for g in range(I):
    g1, g2 = input().strip().split(' ')
    country.append({g1, g2})

if I == 1:
    print(nC2(N) - 1)
else:
    i = 0
    while len(country) > 1 and i < len(country) - 1:
        union = False
        li = len(country[i])
        for j in range(i + 1, len(country)):
            lj = len(country[j])
            iju = set.union(country[i], country[j])
            lij = len(iju)
            if lij < li + lj:
                country[j] = iju
                country.remove(country[i])
                union = True
                break

        if not union:
            i += 1

    rlt = nC2(N)
    for l in country:
        rlt -= nC2(len(l))

print(rlt)
