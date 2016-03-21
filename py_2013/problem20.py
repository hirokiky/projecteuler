#!/usr/env/python -tt

if __name__ == '__main__':
    f = lambda n: n and n * f(n - 1) or 1
    i = f(100)
    r = 0
    for s in str(i):
        r += int(s)
    print r
