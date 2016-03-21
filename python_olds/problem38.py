# -*- coding: utf-8 -*-
#!/usr/bin/env python -tt

def is_conc(s):
    l = list(s)
    for s in [str(i) for i in range(1, 10)]:
        if s in l:
            l.pop(l.index(s))
        else:
            return 0
    return 1

def get_9pad(n):
    s = ""
    for i in xrange(1, 10):
        s += str(n * i)
        if len(s) == 9:
            break
        elif len(s) > 9:
            return 0
    if is_conc(s):
        return s
    else:
        return None

def main():
    for i in xrange(9876, 1, -1):
        if not i % 10 or not i % 5:
            continue
        a = get_9pad(i)
        if a:
            print a
            return 0

if __name__ == '__main__':
    main()
