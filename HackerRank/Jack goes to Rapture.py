# https://www.hackerrank.com/challenges/jack-goes-to-rapture/problem

from queue import PriorityQueue
nn,ne=map(int,input().split())
g=[[] for _ in range(nn)]
for _ in range(ne):
    l,r,c=map(int,input().split())
    l-=1
    r-=1
    g[l].append((r,c))
    g[r].append((l,c))

# BFS
# To determine if the path exists
# O(V+E)
def isConnected():
    openNodes=[0]
    closed=[False]*nn
    closed[0]=True
    while len(openNodes):
        p=openNodes.pop(0)
        for child,_ in g[p]:
            if(closed[child]==False):
                openNodes.append(child)
                closed[child]=True
                if(child==nn-1):
                    return True
    return False
if(isConnected()):
    dist=[float('inf')]*nn
    dist[0]=0
    closed = [False]*nn
    q = PriorityQueue()
    q.put((0,0))
    while(True):
        m,p=q.get()
        if(closed[p]==True):
            continue
        closed[p]=True

        if(p==nn-1):
            break
        for child,cost in g[p]:
            newCost=max(dist[p],cost)
            if(dist[child]>newCost):
                dist[child]=newCost
                q.put((newCost,child))

    print(dist[-1])
else:
    print('NO PATH EXISTS')