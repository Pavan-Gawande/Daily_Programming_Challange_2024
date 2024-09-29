def Get_Reversed_Array_Using_Recursion(arr):
    if(len(arr)<=1):
        return
    start = arr.pop(0)
    Get_Reversed_Array_Using_Recursion(arr)
    arr.append(start)

arr = list(map(int, input().split()))
Get_Reversed_Array_Using_Recursion(arr)
print(arr)