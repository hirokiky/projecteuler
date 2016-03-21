#!/usr/bin/python -tt

def ispalindrome(s):
   h = len(s) / 2
   for a, b in zip(s[:h], reversed(s[h:])):
      if a != b: return 0
   return 1

if __name__ == "__main__":
   a = 999
   b = 999
   m = 0
   while a >= 100:
      while b >= 100:
         t = a * b
         if ispalindrome(str(t)):
            if t > m: m = t
         b -= 1
      b = 999
      a -= 1
   print m

