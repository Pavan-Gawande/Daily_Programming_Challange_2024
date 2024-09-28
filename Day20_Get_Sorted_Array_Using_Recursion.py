def Get_Sorted_Array(arr):
    n = len(arr)
    if(n <= 1):
        return arr
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    last = arr.pop()
    Get_Sorted_Array(arr)
    arr.append(last)

arr = list(map(int, input().split()))
Get_Sorted_Array(arr)
print(arr)