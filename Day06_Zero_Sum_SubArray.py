def Get_SubArrays(input_List):
    result = []
    n = len(input_List)
    for start in range(n):
        sum = 0
        for end in range(start, n):
            sum += input_List[end]
            if(sum == 0):
                result.append((start, end))
    return result

input_List = list(map( int, input().split()))
print(Get_SubArrays(input_List))