#!/usr/bin/env python -tt

from itertools import permutations

if __name__ == '__main__':
    for i, c in enumerate(permutations(range(10), 10)):
        if i+1 == 1000000:
            print c
            break
