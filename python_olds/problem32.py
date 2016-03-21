#!/usr/bin/env python -tt

from itertools import permutations

def is_pandigital(n):
    s = str(n)
    for i in xrange(1, len(s)-2):
        for j in xrange(i+1, len(s)):
            if int(s[:i]) * int(s[i:j]) == int(s[j:]):
                return int(s[j:])
    return 0

def main():
    ret = []
    for t in permutations(range(1, 10), 9):
        n = reduce(lambda x,y:x*10+y, t)
        a = is_pandigital(n)
        if a:
            if not a in ret:
                print a
                ret.append(a)
    print sum(ret)

if __name__ == '__main__':
    main()
