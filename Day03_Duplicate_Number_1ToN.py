def Find_Duplicate(input_list):
    n = len(input_list)-1
    sum_1toN = n*(n+1)//2
    return sum(input_list)-sum_1toN

input_list = list(map(int, input().split(',')))
print(Find_Duplicate(input_list))