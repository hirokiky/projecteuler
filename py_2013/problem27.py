#!/usr/bin/env python -tt

from itertools import permutations

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def primeformula(a, b):
    n = 0
    while is_prime(n**2+a*n+b):
        n += 1
    return n-1

if __name__ == '__main__':
    p = [i for i in xrange(1, 1000) if is_prime(i)]
    p += map((lambda x: x*-1), p) + [1, -1]

    m = 0
    r = 0
    for a, b in permutations(p, 2):
        t = primeformula(a, b)
        if t > m:
            m = t
            r = a * b
    print r
        
