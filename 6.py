for i in range (1,1000):
    s=i
    n = 10
    while s - n < 1000:
        s = s+ n
        n = n+ 5
    if (n==80):
        print (s)

