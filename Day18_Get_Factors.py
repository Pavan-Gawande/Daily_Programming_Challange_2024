def Get_Factors(N):
    if(N == 1):
        return 1
    else:
        factor_num = 1
        low = 1
        high = N//2
        while(low <= high):
            mult = low*high
            if(mult == N ):
                factor_num += 1
                if(low != high):
                    factor_num += 1
            elif(mult > N):
                high -= 1
                continue
            low += 1
        return factor_num+1

N = int(input())
print(Get_Factors(N))