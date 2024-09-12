def Merge_Sorted_Arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    pointer1, pointer2 = 0, 0
    while(pointer1 < len(arr1)):
        if(arr1[pointer1] > arr2[pointer2]):
            arr1[pointer1], arr2[pointer2] = arr2[pointer2], arr1[pointer1]
            miss_placed = arr2.pop(pointer2)
            inserted = False
            for i in range(n-1):
                if(miss_placed<arr2[i]):
                    arr2.insert(i,  miss_placed)
                    inserted = True
                    break
            if not inserted:
                arr2.append(miss_placed)
        pointer1 += 1
    

arr1 = list(map(int, input('\n Enter array 1 elements separated by comma(,) : ').split(',')))
arr2 = list(map(int, input('\n Enter array 2 elements separated by comma(,) : ').split(',')))


Merge_Sorted_Arrays(arr1, arr2)
print('Array 1 : ', arr1)
print('Array 2 : ', arr2)