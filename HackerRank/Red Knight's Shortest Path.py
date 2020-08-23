# https://www.hackerrank.com/challenges/red-knights-shortest-path/problem

n=int(input())

istart,jstart,iend,jend=map(int,input().split())

start=(istart,jstart)
end=(iend,jend)


def getChild(i,j):
    ret=[]
    # this Specific order of inputs bcuz it is stated in the question as a note
    if(i-2>=0 and j-1>=0):
        ret.append([(i-2,j-1),'UL'])
    if(i-2>=0 and j+1<n):
        ret.append([(i-2,j+1),'UR'])
    if(j+2<n):
        ret.append([(i,j+2),'R'])
    if(i+2<n and j+1<n):
        ret.append([(i+2,j+1),'LR'])
    if(i+2<n and j-1>=0):
        ret.append([(i+2,j-1),'LL'])
    if(j-2>=0):
        ret.append([(i,j-2),'L'])
    return ret

def BFS(start,end):
    # BFS 
    openNodes=[start]
    pos=[[None]*n for _ in range(n)]
    pos[start[0]][start[1]]=(None,None)
    path=[]
    while(len(openNodes)):
        for _ in range(len(openNodes)):
            p=openNodes.pop(0)
            for child in getChild(p[0],p[1]):
                if(pos[child[0][0]][child[0][1]]!=None):
                    continue
                pos[child[0][0]][child[0][1]]=(p,child[1])
                openNodes.append(child[0])
                # if we reach the end
                if(child[0]==end):
                    tp=p
                    path.insert(0,child[1])
                    while tp!=None:
                        path.insert(0,pos[tp[0]][tp[1]][1])
                        tp=pos[tp[0]][tp[1]][0]
                    return path[1:]
    return []
ans=BFS(start,end)
if(len(ans)==0):
    print('Impossible')
else:
    print(len(ans))
    print(' '.join(ans))