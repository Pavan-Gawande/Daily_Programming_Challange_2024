def Get_If_Cyclic_Graph(arr, v, e):
    if(v <= 2 or e <= 2):
        return False
    elif(e >= v):
        return True
    else:
        graph = {}
        for i, j in arr:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        def is_cycle(vertex, parent):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if is_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False
        for vertex in graph:
            if vertex not in visited:
                if is_cycle(vertex, -1):
                    return True
        return False

temp = list(map(int, input().split()))
arr = [temp[2*i:2*(i+1)] for i in range(len(temp)//2)]
v, e = map(int, input().split())
print(Get_If_Cyclic_Graph(arr, v, e))