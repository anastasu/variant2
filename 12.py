s = 17 * '3'+ 23* '4'+29*'5'
while '43' or '53' in s:
    if '43' in s:
        s = s.replace('43','33',1)
        print (s)
    else:
        s = s.replace ('53','433',1)
        print (s)
n=0
for i in range(0,len(s)):
    if s[i]=='3':
        n = n+1
print (n)