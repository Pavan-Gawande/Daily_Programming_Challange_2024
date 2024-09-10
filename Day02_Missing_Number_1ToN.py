# take input from user
input_list = list(map(int, input().split(',')))

# calculate n
n = len(input_list) + 1

# calculate sum of 1 to n  numbers
needed_sum = n*(n+1)//2

# remove each input list element from needed sum 
for i in input_list:
    needed_sum -= i

# at last only the missing number will remain in needed sum variable
print(needed_sum)