# https://www.hackerrank.com/challenges/beautiful-path/problem

from collections import *

graph = defaultdict(list)
N, E = map(int, input().split())
for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
dq = deque()
start, end = map(int, input().split())
distance = [dict() for j in range(N+1)]
dq.append((start, 0))
distance[start][0] = 0
'''BFS'''
while dq:
    vertex, dist = dq.popleft()
    for k, v in graph[vertex]:
        cost = v | dist
        '''Calculate the new cost , if cost is not in the dictionary of that node it means it is new so add it.Do not add cost that is greater then 1024 as that is the limit.'''
        if cost not in distance[k] and cost <= 1024:
            distance[k][cost] = 1
            dq.append((k, cost))
print(sorted(distance[end])[0] if distance[end] else "-1")
