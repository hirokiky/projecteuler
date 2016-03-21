#! /usr/bin/env python -tt

from itertools import combinations
from math import fabs

UPPER_LIMIT = 1000

def is_right_triangle(a, b, c):
    return c ** 2 == a ** 2 + b ** 2

def figure_generator(a, b, c):
    i = 1
    while a * i + b * i + c * i <= UPPER_LIMIT:
        yield a * i, b * i, c * i
        i += 1

if __name__ == "__main__":
    right_triangles = set()
    for a, b, c in combinations(xrange(1, UPPER_LIMIT+1), 3):
        if a + b + c > UPPER_LIMIT or (a, b, c) in right_triangles:
            continue
        elif is_right_triangle(a, b, c):
            right_triangles.update(figure_generator(a, b, c))
        print a, b, c

    ans = {}
    for t in right_triangles:
        try:
            ans[sum(t)] += 1
        except KeyError:
            ans[sum(t)] = 1
    print max(ans.items(), key=lambda x: x[1])
