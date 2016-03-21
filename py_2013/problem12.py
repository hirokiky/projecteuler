#!/usr/env/python -tt

def triangle():
    x, r = 1, 2
    while True:
        yield x
        x, r = x + r, r + 1

from math import sqrt
def divisors(n):
    c = 2
    m = int(sqrt(n))
    if m*m == n:
        c += 1

    for i in xrange(2, m+1):
        if n%i == 0:
            c+=2
    return c

if __name__ == "__main__":
    t = triangle()
    x = t.next()
    while divisors(x) <= 500:
        x = t.next()
    print x
    
