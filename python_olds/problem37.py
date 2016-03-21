#!/usr/bin/env python -tt

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_p = int(sqrt(n))
    return all(n % p != 0 for p in xrange(3, max_p + 1, 2))

def _is_trunc(s, f):
    if len(s) == 0:
        return 1
    if is_prime(int(s)):
        if f == 'r':
            return _is_trunc(s[:-1], f)
        elif f == 'l':
            return _is_trunc(s[1:], f)
    else:
        return 0
    
def is_truncatableprime(n):
    return _is_trunc(str(n), 'r') and _is_trunc(str(n), 'l')

def main():
    i = 8
    r = []
    while len(r) < 11:
        if is_truncatableprime(i):
            r.append(i)
        i += 1
    print sum(r)

if __name__ == '__main__':
    main()
