def Get_Coin_Change(coins, k):
    if(k == 0):
        return 0
    else:
        num = 0
        for i in coins[::-1]:
            num += k//i
            k = k%i
            if(k == 0):
                return num
        else:
            return -1

coins = list(map(int, input().split()))
k = int(input())
print(Get_Coin_Change(coins, k))
            