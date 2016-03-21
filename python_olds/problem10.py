#!/usr/env python -tt
from math import sqrt

def isprime(n):
   if n == 2 or n == 3: return 1
   d = 2
   h = int(sqrt(n))
   while d <= h:
      if not n % d: return 0
      d += 1
   return 1

def getsumbelow(n):
   r = 0
   c = 2
   while n > c:
       if isprime(c): r += c
       c += 1
   return r

if __name__ == "__main__":
   import sys
   print getsumbelow(int(sys.argv[1]))
