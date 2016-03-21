#!/usr/bin/env python -tt

def atol(s):
    return [ord(s)-64 for s in s]

def get_names():
    r = []
    for s in open('./names.txt', 'r'):
        s = s.replace('"', '')
        r += s.split(',')
    r.sort()
    return r

if __name__ == '__main__':
    names = get_names()
    namenums = [atol(s) for s in names]
    scores = [(i+1) * sum(n) for i, n in enumerate(namenums)]
    print sum(scores)
