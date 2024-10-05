def Get_Shortest_Path(arr, v, start, end):
    paths = []
    adj = [[] for i in range(v)]
    for i, j in arr:
        adj[i].append(j)
        adj[j].append(i)
    def calc_path(curr_node, path_len, end, visited):
        visited.add(curr_node)
        for neighbour in adj[curr_node]:
            if neighbour not in visited:
                calc_path(neighbour, path_len+1, end, visited)
            if neighbour == end:
                paths.append(path_len)
                return
        return False
    visited = set({start})
    path_len = 1
    for neighbour in adj[start]:
        calc_path(neighbour, path_len, end, visited)
    if(len(paths) == 0):
        return -1
    return min(paths)+1

v = int(input())
# enter input as simple space separated values like 0 1 1 2 2 3....
temp = list(map(int, input().split()))
arr = [temp[2*i:2*(i+1)] for i in range(len(temp)//2)]
start, end = map(int, input().split())
print(Get_Shortest_Path(arr, v, start, end))