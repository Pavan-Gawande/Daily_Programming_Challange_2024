def Get_Window_Max(arr, k):
    n = len(arr)
    maximum = max(arr[:k])
    if(k == n):
        return maximum
    result = [maximum]
    start = 1
    for i in range(k, n):
        maximum = max(arr[start:i+1])
        result.append(maximum)
        start += 1
    return result

arr = list(map(int, input().split()))
k = int(input())
print(Get_Window_Max(arr, k))