#!/usr/bin/env python -tt

def is_abundantnum(n):
    r = 0
    for i in xrange(n-1, 0, -1):
        if n % i == 0:
            r += i
            if r > n:
                return 1
    return 0

def get_abundantnums():
    r = [False] * (28123 - 12 + 1)
    for i in xrange(1, 28123-12+1):
        if not r[i] and is_abundantnum(i):
            r[i] = True
            if i < (28123-12) / 2:
                for j in xrange(2, (28123-12+1)/i):
                    k = i * j
                    if not r[k]:
                        r[k] = True
    return r

def is_sumoftwonums(n, l):
    for i in xrange(12, n):
        if l[i] and l[n-i]:
            return 1
    return 0

def main():
    l = get_abundantnums()
    r = 0
    for i in xrange(1, 28123+1):
        if not is_sumoftwonums(i, l):
            r += i
    print r

if __name__ == '__main__':
    main()
