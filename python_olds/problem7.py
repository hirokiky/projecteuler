#!/usr/bin/python -tt
from math import sqrt

def isprimenumber(n):
   if n == 2 or n == 3: return 1
   d = 2
   h = int(sqrt(n))
   while d <= h:
      if not n % d: return 0
      d += 1
   return 1

if __name__ == "__main__":
   n = 2
   c = 1
   while c != 10001 + 1:
      if isprimenumber(n):
         print n, c
         c += 1
      n += 1
   print n - 1
