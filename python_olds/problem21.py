#!/usr/env/python -tt

def get_sumofdivisors(n):
    return sum([x for x in xrange(1, n) if n % x == 0])

def get_amicablenum(a):
    b = get_sumofdivisors(a)
    if a == get_sumofdivisors(b) and a != b:
        return b
    else:
        return 0

if __name__ == '__main__':
    r = [t for t in [get_amicablenum(x) for x in xrange(1, 10001)] if t]
    print sum(r)
