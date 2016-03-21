#!/usr/bin/env python -tt

r = []

for i in xrange(2, 101):
    for j in xrange(2, 101):
        t = i ** j
        if t not in r:
            r.append(t)

print len(r)
