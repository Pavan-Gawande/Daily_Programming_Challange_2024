def leaders_array(l):
    n = len(l)
    maximum = l[n-1]
    leaders = [maximum]
    for i in range(2, n+1):
        ele = l[n-i]
        if(ele >  maximum):
            maximum =  ele
            leaders.insert(0, ele)
    return leaders

l = list(map(int, input().split()))
print(leaders_array(l))