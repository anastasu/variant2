def F(n):
    if n <= 3:
        F(n) = n + 3
    if n>3 and F(n-1) %2 == 0:
        F(n)= F(n - 2)
    if n >3 and F(n-1) %2!= 0 :
        F(n) = F(n - 2) + 2*n
print (F(40))
