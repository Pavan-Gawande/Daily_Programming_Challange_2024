def Nth_Fab_Num(n):
    if(n <= 1):
        return n
    else:
        a1, a2 = 0, 1
        for i in range(n-1):
            a2 += a1
            a1 = a2 - a1
        return a2

n = int(input())
print(Nth_Fab_Num(n))
