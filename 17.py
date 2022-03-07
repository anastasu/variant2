f = open ('17-202.txt')
a = [int (i) for i in f]
s=0
k=0
ma = 0
def call(x):
    return 100<= x <1000 and x % 10 ==5
for i in range (len(a)):
    if ( not call(a [i-2])) and (call(a [i-1])) and (not call(a [i])):
        k+=1
        s = a [i-2] +a [i-1] + a [i]
    ma= max (ma,s)
print (k,ma)
