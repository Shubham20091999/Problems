from queue import PriorityQueue
for _ in range(int(input())):
    n, e = map(int, input().split())
    edges = [set(i for i in range(n)) for _ in range(n)]
    for _ in range(e):
        l, r = map(lambda e: int(e)-1, input().split())
        edges[l].remove(r)
        edges[r].remove(l)
    s = int(input())-1
    dist = [float('inf')]*n
    closed = [False]*n
    q = PriorityQueue()
    q.put((0, s))
    while not(q.empty()):
        distTraveled, parent = q.get()
        if(closed[parent]==True):
            continue
        closed[parent]=True
        for child in edges[parent]:
            nxtdist = distTraveled+1
            if(dist[child] > nxtdist):
                dist[child] = nxtdist
                q.put((dist[child], child))
    for i in range(n):
        if(i!=s):
            print(dist[i],end=' ')
    print("")

# ---------------------
tests = int(input())

for _ in range(tests):
    [n, e] = [int(i) for i in input().split(" ")]
    dists = [1] * n
    roads = {}
    for _ in range(e):
        [n1, n2] = [int(i) for i in input().split(" ")]
        if n1 not in roads:
            roads[n1] = set()
        if n2 not in roads:
            roads[n2] = set()
        roads[n1].add(n2)
        roads[n2].add(n1)
    start_loc = int(input())
    not_visited = roads[start_loc] if start_loc in roads else set()
    newly_visited = set()
    curr_dist = 2
    while len(not_visited) > 0:
        for i in not_visited:
            diff = not_visited | roads[i]
            if len(diff) < n:
                dists[i-1] = curr_dist
                newly_visited.add(i)
        not_visited = not_visited - newly_visited
        newly_visited = set()
        curr_dist += 1
    del dists[start_loc-1]
    print(" ".join(str(i) for i in dists))