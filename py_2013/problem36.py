#!/usr/bin/env python -tt

def is_palindromic(n):
    sn = str(n)
    sb = str(format(n, 'b'))
    return sn == sn[::-1] and sb == sb[::-1]
    

def main(n):
    ret = 0
    for i in xrange(1, n+1):
        if is_palindromic(i):
            ret += i
    print ret

if __name__ == '__main__':
    main(1000000)
