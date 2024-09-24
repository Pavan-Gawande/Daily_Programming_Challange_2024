def Get_Lcm(a, b):
    high = max(a, b)
    low = min(a, b)
    for i in range(high, a*b+1):
        if(i%high == 0 and i%low == 0):
            return i

a, b = map(int, input().split())
print(Get_Lcm(a, b))