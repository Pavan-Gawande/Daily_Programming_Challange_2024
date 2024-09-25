def Get_Prime_Factors(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i
    
    if N > 2:
        factors.append(N)

    return factors


N = int(input())
print(Get_Prime_Factors(N))
