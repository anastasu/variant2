for i in range (0,10):
  x=i
  x = (x - x % 8) * 10
  a= 1
  b= 0
while x > 0:
  if x % 2 != 0:
    a = a * (x % 4)
else:
  b = b + (x % 4)
  x = x // 8
if (a==9) and (b==5):
  print (i)