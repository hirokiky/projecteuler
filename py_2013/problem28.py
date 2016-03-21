#!/usr/bin/env python -tt

n = 1
r = 1
for i in xrange(1, 501):
    n += i*8
    r += n * 4 - i *12

print r
