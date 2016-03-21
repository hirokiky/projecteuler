#!/usr/bin/env python -tt

f = lambda n: n and n * f(n - 1) or 1

def is_funcdig(n):
    l = [f(int(s)) for s in str(n)]
    return sum(l) == n

def main():
    ret = [i for i in xrange(3, 100000) if is_funcdig(i)]
    print sum(ret)

if __name__ == '__main__':
    main()
