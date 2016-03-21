#!/usr/env/python -tt

from calendar import Calendar

if __name__ == '__main__':
    cal = Calendar()
    r = 0
    for y in xrange(1901, 2000+1):
        for m in xrange(1, 12+1):
            for d in cal.itermonthdays2(y, m):
                if d[0] == 1:
                    if d[1] == 6:
                        r += 1
                    break
    print r
