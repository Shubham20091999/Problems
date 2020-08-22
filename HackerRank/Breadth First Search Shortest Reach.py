# https://www.hackerrank.com/challenges/bfsshortreach/problem

def bfs(adj, start):
    openNodes = [start]
    closed = [False]*len(adj)
    dist = [-1]*len(adj)
    dist[start]=0
    closed[start]=True
    while(len(openNodes)):
        for _ in range(len(openNodes)):
            p = openNodes.pop(0)
            for child in adj[p]:
                if(closed[child]==False):
                    closed[child]=True
                    dist[child]=dist[p]+1
                    openNodes.append(child)
    return dist


for _ in range(int(input())):
    n, ne = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(ne):
        l, r = map(int, input().split())
        adj[l-1].append(r-1)
        adj[r-1].append(l-1)
    start = int(input())-1
    
    for i in bfs(adj,start):
        if(i==0):
            continue
        if(i==-1):
            print(-1,end=' ')
        else:
            print(6*i,end=' ')
    print("")
