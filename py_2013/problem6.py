#!/usr/bin/python -tt

def getsumofsquare(n):
   return n * (n + 1) * (2 * n + 1) / 6

def getsquareofsum(n):
   return (n * (n + 1) / 2)** 2

print getsquareofsum(100) - getsumofsquare(100)
