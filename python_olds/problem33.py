#!/usr/bin/env python -tt

from fractions import Fraction

def cur(si, sj):
    for s in si:
        if s in sj:
            li = si.strip(s)
            lj = sj.strip(s)
            if int(li) and int(lj):
                if int(si)/float(sj) == int(li)/float(lj):
                    return si, sj
    return None

def is_validnum(n):
    s = str(n)
    if s[0] == s[1] or not n % 10:
        return 0
    else:
        return n

def main():
    ret = Fraction(1, 1)
    for i, j in [(i, j) for i in xrange(13, 99) if is_validnum(i) for j in xrange(12, i) if is_validnum(j)]:
        if cur(str(i), str(j)):
            ret *= Fraction(j, i)
    print ret

if __name__ == '__main__':
    main()
