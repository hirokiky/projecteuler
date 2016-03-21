#!/usr/bin/env python -tt

r = 0
for n in xrange(2, 200000):
    t = 0
    for i in str(n):
        t += int(i)**5
    if n == t:
        r += n

print r
