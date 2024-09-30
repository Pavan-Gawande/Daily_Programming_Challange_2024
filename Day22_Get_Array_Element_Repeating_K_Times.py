def Get_Array_Element(arr, k):
    d = {}
    k_list = []
    n = len(arr)
    if(n==1 and k==1):
        return arr[0]
    for i in arr:
        if(i in d):
            d[i] += 1
            if(d[i] == k):
                k_list.append(i)
        else:
            d[i] = 1
    for ele in k_list:
        if(d[ele] == k):
            return ele
    return -1

arr = list(map(int, input().split()))
k = int(input())
print(Get_Array_Element(arr, k))