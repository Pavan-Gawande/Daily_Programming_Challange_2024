import math
def Get_Lowest_Common_Ancestor(arr, p, q):
    if( p == q ):
        return p
    elif(arr[0]==p or arr[0]==q):
        return arr[0]
    else:
        lngth = len(arr)
        lvl = int(math.log(lngth, 2))
        for i in range(1, lngth+1):
            if(arr[i-1]== p):
                p_ind = i-1
                p_lvl = int(math.log(i, 2))
            elif(arr[i-1]==q):
                q_ind = i-1
                q_lvl = int(math.log(i, 2))
        if(p_lvl < q_lvl):
            return p
        elif(p_lvl > q_lvl):
            return q
        else:
            minimum = 99999
            for i in range(p_lvl):
                p_anc_ind = (p_ind - 1)//2
                q_anc_ind = (q_ind - 1)//2
                if(p_anc_ind == q_anc_ind):
                    if(arr[p_anc_ind] < minimum):
                        minimum = arr[p_anc_ind]
            return minimum
    
arr = list(map(int, input().replace('null', '999999').split()))
p, q = map(int, input().split())
print(Get_Lowest_Common_Ancestor(arr, p, q))