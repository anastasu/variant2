k=0
for i in range (500000, 1000000):
    max_d = 0
    for d in range(2, int(i**0.5)+1):
        if i%d == 0:
            if d% 10 == 8 and d!=8:
                max_d = d
                break
        if (i // d % 10) == 8:
            max_d = i// d
    print (i, max_d)