def sort_array_012(arr):
    low, mid = 0, 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

input_list = list(map(int, input('Enter list elements separated by space : ').split()))
sort_array_012(input_list)
print(input_list)
