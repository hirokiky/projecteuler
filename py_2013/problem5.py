def isdividedall(num):
   for d in xrange(1, 20):
      if num % d: return 0
   return 1

if __name__ == "__main__":
   num = 20
   while True:
      if isdividedall(num): break
      num += 20
   print num
