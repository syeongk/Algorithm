import sys
from collections import deque

n, m, k, x = map(int, input().split())

graph = [ [] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0


queue = deque([x])
while queue:
    now = queue.popleft()
    for city in graph[now]:
        if distance[city] == -1:
            distance[city] = distance[now] + 1
            queue.append(city)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


