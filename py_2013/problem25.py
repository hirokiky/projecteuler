#!/usr/bin/env python -tt

from math import log

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    f = fibonacci()

    c = 0
    while True:
        c += 1
        if int(log(f.next(), 10)+1) == 1000:
            print c
            break    
