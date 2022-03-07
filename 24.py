f= open ('24-157.txt')
s = f .readline ()
k = 0
ma = -1000
for i in range (0,len(s)-1):
    if (s[i] != 'P') and (s[i+1] != 'R') or (s[i] != 'R') and (s[i+1] != 'P'):
        k = k+1


  #  if s[i-1] + s[i] not in ('PR','RP'):
  #      k = k+1

    else:
        ma = max (ma, k)
        k=0
print (ma)