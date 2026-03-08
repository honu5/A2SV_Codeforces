from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
degree = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1    
    graph[a].append(b)
    graph[b].append(a)
    
    degree[a] += 1
    degree[b] += 1
removed = [False] * n
answer = 0

while True:
    lv = []
    
    for i in range(n):
        if not removed[i] and degree[i] == 1:
            lv.append(i)
    
    if not lv:
        break    
    answer += 1
    
    for node in lv:
        removed[node] = True
    
    for node in lv:
        for nei in graph[node]:
            if not removed[nei]:
                degree[nei] -= 1
print(answer)