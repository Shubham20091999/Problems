
def dynamicArray(n, q):
    seqlist=[[] for j in range(n)]
    lastAns=0
    ans=[]
    for i in range(len(q)):
        if(q[i][0]==1):
            seqlist[(q[i][1]^lastAns)%n].append(q[i][2])
        else:
            temp=seqlist[(q[i][1]^lastAns)%n]
            size=len(temp)
            lastAns=temp[q[i][2]%size]
            ans.append(lastAns)
    return ans
        

n=2
que=[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
dynamicArray(n,que)