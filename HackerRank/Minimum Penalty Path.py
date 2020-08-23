# https://www.hackerrank.com/challenges/beautiful-path/problem
from collections import *

graph = defaultdict(list)
N, E = map(int, input().split())
for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

start, end = map(int, input().split())

openNodes = deque()
distance = [set() for j in range(N+1)]
openNodes.append((start, 0))
distance[start].add(0)
# BFS
while openNodes:
    vertex, dist = openNodes.popleft()
    for k, v in graph[vertex]:
        cost = v | dist
        if cost not in distance[k] and cost <= 1024:
            # Saving every possible cost to that point and checking while comming to that point if the cost exists already
            # if it exists then no need to add new object to the open list
            # otherwise add it in the open list
            distance[k].add(cost)
            openNodes.append((k, cost))
print(min(distance[end]) if distance[end] else -1)