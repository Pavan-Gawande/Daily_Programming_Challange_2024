def Get_Water_Trapped(height):
    n = len(height)
    if(n < 3):
        return 0
    l_Max = height[0]
    left_Max = [l_Max]
    r_Max = height[n-1]
    right_Max = [r_Max]
    for i in range(1, n):
        l_Max = max(left_Max[i-1], height[i])
        left_Max.append(l_Max)
        r_Max = max(r_Max, height[n-i-1])
        right_Max.insert(0, r_Max)
    
    water_Trapped = 0
    for i in range(n):
        min_Height = min(left_Max[i], right_Max[i])
        water_Trapped += min_Height - height[i]
    
    return water_Trapped

height = list(map(int, input().split()))
result = Get_Water_Trapped(height)
print(result)