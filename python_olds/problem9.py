#!/user/env python -tt
from math import sqrt

def isinteger(x):
   if isinstance(x, float):
      return int(x) == float(x)
   else:
      raise TypeError, "Input float"

def pythagotrip(a, b):
   c = sqrt(a ** 2 + b ** 2)
   if isinteger(c):
      return int(c)
   else:
      return -1

if __name__ == '__main__':
   for a in xrange(1, 500):
      for b in xrange(1, 500):
         c = pythagotrip(a, b)
         if a + b + c == 1000:
            print a * b * c
