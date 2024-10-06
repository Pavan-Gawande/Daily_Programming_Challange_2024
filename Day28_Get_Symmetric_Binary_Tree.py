import math
def Is_Symmetric_B_Tree(arr):
    def is_Symmetric(lvl):
        global arr
        start = 2**lvl - 1
        end = 2**(lvl + 1) - 2
        for i in range(lvl):
            if(arr[(start + i)] == arr[end - i]):
                continue
            return False
        return True
    n = len(arr)
    if(n <= 1):
        return True
    lvl = math.log(n+1, 2)
    if(bool(lvl - int(lvl))):
        return False
    else:
        for i in range(int(lvl)):
            if(is_Symmetric(i)):
                continue
            else:
                return False
        return True
                
#The value of each node is between −100 and 100.
#therefore null is replaced with -101
arr = list(map(int, input().replace('null', '-101').split()))
print(Is_Symmetric_B_Tree(arr))