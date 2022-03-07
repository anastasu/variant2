print ('a','b','c','d')
for a in range (2):
    for b in range (2):
        for c in range (2):
            for d in range (2):
             f = (not a or b) and not (b == c)and (not d or a)
             if (f==1):
                 print (a,b,c,d,f)
