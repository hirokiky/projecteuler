#!/usr/bin/env python -tt

def get_cycle(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    i = 1
    while 10**i % n != 1:
        i += 1
    return i

if __name__ == '__main__':
    mr = 0
    mi = 0
    for i in xrange(2, 1001):
        r = get_cycle(i)
        if r > mr:
            mr = r
            mi = i
    print mi
