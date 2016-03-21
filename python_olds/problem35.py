#!/usr/bin/env python -tt

from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_p = int(sqrt(n))
    return all(n % p != 0 for p in xrange(3, max_p + 1, 2))

def get_circlars(n):
    s = str(n)
    ret = []
    for _ in xrange(len(s)):
        ret.append(int(s))
        s = s[1:] + s[0]
    return ret
    
def main(n):
    ret = 0
    for i in xrange(2, n+1):
        if all(is_prime(x) for x in get_circlars(i)):
            ret += 1
    print ret

if __name__ == '__main__':
    main(1000000)
