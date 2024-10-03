flag = True

def Is_BST(arr, ind):
    global flag, n
    left_child_index = (2*ind) + 1
    right_child_index = (2*ind) + 2
    if(right_child_index < n):
        if((arr[left_child_index] < arr[ind]) and (arr[right_child_index] > arr[ind])):
            flag = flag and True
        else:
            flag = flag and False
    elif((left_child_index < n) and (arr[left_child_index] < arr[ind])):
        flag = flag and True
    else:
        return
    left_child_index = (2*ind) + 1
    Is_BST(arr, left_child_index)
    right_child_index = (2*ind) + 2
    Is_BST(arr, right_child_index)

arr = list(map(int, input().replace('null','0').split()))
n = len(arr)
Is_BST(arr, 0)
print(flag)