#!/usr/env/python -tt

import sys

def collatz(n, c):
    if n == 1:
        return c
    elif n % 2:
        return collatz(n*3+1, c+1)
    else:
        return collatz(n/2, c+1)

def collatz_iter(n):
    return collatz(n, 1)

if __name__ == '__main__':
    m = 0
    for x in xrange(1, 1000000):
        r = collatz_iter(x)
        if r > m:
            m = r
        print x, r, m
