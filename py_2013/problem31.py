#!/usr/bin/env python -tt

c = 1
for i in xrange(3):
    for j in xrange(5):
        for k in xrange(11):
            for l in xrange(21):
                for m in xrange(41):
                    for n in xrange(101):
                        for o in xrange(201):
                            if i*100 + j*50 + k*20 + l*10 + m*5 + n*2 + o > 200:
                                break
                            elif i*100 + j*50 + k*20 + l*10 + m*5 + n*2 + o == 200:
                                print i, j, k, l, m, n, o
                                c += 1
print c
