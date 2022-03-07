s= open ('24-157.txt').readline ()
k = 1
ma = 1
for i in range (1,len(s)):
    if s[i-1] + s[i] not in ('PR','RP'):
        k = k+1

    else:
        ma = max (ma, k)
        k=1
print (ma)